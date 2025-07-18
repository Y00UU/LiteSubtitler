# coding: utf8
import copy
import os
from pathlib import Path
import threading
from typing import Any, LiteralString

from PyQt6.QtWidgets import QApplication
from fastapi import WebSocket

from core.asr.asr_data import ASRData
from core.asr.asr_data_builder import AsrDataBuilder
from core.base_object import BaseObject
from enums.supported_audio_enum import SupportedAudioEnum
from enums.supported_subtitle_enum import SupportedSubtitleEnum
from enums.supported_video_enum import SupportedVideoEnum
from model.file_vo import FileVO
from service.api_service import ApiServer, WebSocketManager
from service.asr_service import AsrService
from service.translate_service import TranslateService
from service.video_service import VideoService
from task.step_processor import StepProcessor
from task.task_obj import TaskObj
from task.task_scheduler import TaskScheduler
from ui.data.array_table_model import ArrayTableModel
from utils.file_utils import FileUtils


class MainController(BaseObject):
    """
    主控制器，用来发起整个处理流程，完成视频或者音频的识别和翻译工作，并把结果合成到视频文件中。
    """

    def __init__(self, model: ArrayTableModel, config_args, finished_all_callback=None, log_to_ui_func=None):
        """
        创建函数

        Args:
            model: 任务列表中的数据model。
            finished_all_callback: 所有任务执行结束后的回调。
            config_args: 配置参数。
            log_to_ui_func: 打印日志信息到UI界面的处理函数。
        """
        super().__init__(log_to_ui_func=log_to_ui_func)

        self.config_args = copy.deepcopy(config_args)
        self.model = model

        self.video_service = VideoService(log_to_ui_func=log_to_ui_func)  # 视频处理服务
        self.asr_service = AsrService(log_to_ui_func=log_to_ui_func)  # ASR识别服务
        self.translate_service = TranslateService(log_to_ui_func=log_to_ui_func)  # 翻译服务
        self.api_service = ApiServer(log_to_ui_func=log_to_ui_func)

        self.scheduler = TaskScheduler(log_to_ui_func=log_to_ui_func)  # 任务调度器
        self.stopped = False
        self.active_step_processor = set()  # 活动中的步骤处理器

        self.task_count = 0  # 未处理的任务数
        self.finished_all_callback = finished_all_callback
        self.use_cuda = False

    def stop(self):
        """
        停止任务执行，不能立即停止，需要步骤处理结束后才能停止。
        """
        self.stopped = True
        self.scheduler.stop()
        for processor in self.active_step_processor:
            processor.stop()

    def run(self, tasks, args):
        """
        运行任务。

        Args:
            tasks: 要运行的任务列表。
            args: 配置参数。
        """
        if args:
            # 用新参数覆盖config_args
            self.config_args = copy.deepcopy(args)

        self.stopped = False
        self.scheduler.stopped = False

        self.task_count = len(tasks)
        self.log_info(f"开始处理任务，总任务数：{self.task_count}.")

        if self.task_count > 0:
            for task in tasks:
                self.log_info(f"任务({task['id']})待处理，名称：{task['fileName']}.")
                self._run_task(task)

            self._active_config()  # 激活配置参数
            self.scheduler.run()  # 用指定参数执行任务

    def api_server_request_reg(self, slots_dict: dict[str, Any]):
        self.api_service.request_scan_connect(slots_dict["scan"])
        self.api_service.request_add_connect(slots_dict["add"])
        self.api_service.request_start_connect(slots_dict["start"])
        self.api_service.request_stop_connect(slots_dict["stop"])
        self.api_service.request_clear_connect(slots_dict["clear"])
        self.api_service.request_selectLang_connect(slots_dict["selectLang"])
        self.api_service.request_exit_connect(slots_dict["exit"])

    def api_server_start(self, args):
        self.api_service.run(host=args["host"], port=int(args["port"]))

    def api_server_stop(self):
        self.api_service.shutdown()

    def api_server_callback(self, callback_func_name: str, arg: any):
        self.api_service.callback_call(callback_func_name=callback_func_name, arg=arg)

    def api_server_writelog(self, log_text: str):
        self.api_service.response_call(WebSocketManager.WebSocketConnection.CLIENT_LOG, arg=log_text)

    def _active_config(self):
        """激活配置参数"""
        self.video_service.reset_args(self.config_args["subtitle_args"], files_args=self.config_args["files_args"])
        self.asr_service.reset_args(self.config_args["asr_args"])
        self.translate_service.reset_args(self.config_args["translate_args"])

    def _run_task(self, task):
        """
        运行单个任务.

        Args:
            task: 要运行的任务。
        """
        task_id = task["id"]
        file_name = task["fileName"]
        if SupportedVideoEnum.is_video_file(file_name):
            self._create_task(task_id, self._run_for_video, task["filePath"])
        elif SupportedAudioEnum.is_audio_file(file_name):
            self._create_task(task_id, self._run_for_audio, task["filePath"])
        elif SupportedSubtitleEnum.is_subtitle_file(file_name):
            self._create_task(task_id, self._run_for_srt, task["filePath"])
        else:
            self.log_info(f"任务({task['id']})：{task['fileName']} 不支持这个文件类型")
            self.task_count -= 1

    def _create_task(self, task_id, task_func, file_path):
        """
        创建任务并添加到调度器。

        Args:
            task_id: 任务ID。
            task_func: 任务处理的函数。
            file_path: 任务对应的文件。
        """
        task = TaskObj(task_id, self.on_task_finished, task_func, self.log_to_ui_func, file_path)
        self.scheduler.add_task(task)

    def on_task_finished(self, task_id: str, msg: str):
        """
        任务完成时的回调函数。

        Args:
            task_id: 任务ID。
            msg: 提示信息。
        """
        self.log_info(f"----------------------- 任务 {task_id}: {msg} -----------------------")

        self.task_count -= 1
        if self.task_count <= 0:
            if self.finished_all_callback:
                self.finished_all_callback()
                self.log_info("所有任务执行结束")

        self.api_service.response_call(WebSocketManager.WebSocketConnection.PROCESS_PROGRESS, arg=self.task_count)

    def on_task_progress(self, task_id: str, rate: int, msg: str):
        """
        任务进度更新时的回调函数。

        Args:
            task_id: 任务ID。
            rate: 进度。
            msg: 提示信息。
        """
        self.model.update_cell(task_id, 2, f"{rate}%")
        self.model.update_cell(task_id, 3, msg)
        QApplication.processEvents()

    def _save_srt_file(self, asr_data: ASRData, out_srt_file):
        """
        保存SRT文件。

        Args:
            asr_data: 要处理的ASR数据。
            out_srt_file: 输出的文件。
        """
        if asr_data:
            layout = "仅原文" if not self.config_args["translate_args"]["need_translate"] else self.config_args["subtitle_args"]["subtitle_layout"]
            asr_data.to_srt(layout=layout, save_path=out_srt_file)

    def _run_for_video(self, task_id: str, video_file_path: str):
        """
        处理视频文件，输出合成字幕和配音以后的视频文件。

        Args:
            task_id: 任务ID。
            video_file_path: 要处理的视频文件。
        """
        temp_files = self._generate_output_file_paths(FileVO(video_file_path), ["_word.srt", "_asr.srt", "_translate.srt"])
        if self.config_args["files_args"]["directory"]["Output"]:
            out_files = self.config_args["files_args"]["directory"]["Output"] + "/" + Path(video_file_path).stem + "-C.srt"
        else:
            out_files = Path(video_file_path).parent + "/" + Path(video_file_path).stem + "-C.srt"
        steps = [
            (task_id, 0, "提取音频...", self.video_service.extract_wav, None),
            (task_id, 20, "音频（按词）识别...", self.asr_service.asr_process, temp_files[0]),
            (task_id, 50, "字幕合并处理...", self.asr_service.merge_words, temp_files[1]),
            (task_id, 60, "翻译字幕...", self.translate_service.translate_srt, temp_files[2]),
            (task_id, 90, "字幕合成到视频...", self.video_service.embed_subtitles, video_file_path),
        ]
        processor = self._create_and_run_processor(steps, task_id, video_file_path)
        try:
            final_ret = processor.run(video_file_path)
            if final_ret is not None:
                self._save_srt_file(asr_data=final_ret, out_srt_file=out_files)
            return final_ret
        finally:
            self._on_task_finished(processor, temp_files)

    def _run_for_audio(self, task_id: str, audio_file_path: str):
        """
        处理音频文件，输出翻译后的字幕文件。

        Args:
            task_id: 任务ID。
            audio_file_path: 要处理的音频文件。
        """
        temp_files = self._generate_output_file_paths(FileVO(audio_file_path), ["_word.srt", "_asr.srt", "_translate.srt"])
        if self.config_args["files_args"]["directory"]["Output"]:
            out_files = self.config_args["files_args"]["directory"]["Output"] + "/" + Path(audio_file_path).stem + "-C.srt"
        else:
            out_files = Path(audio_file_path).parent + "/" + Path(audio_file_path).stem + "-C.srt"
        steps = [
            (task_id, 0, "音频（按词）识别...", self.asr_service.asr_process, temp_files[0]),
            (task_id, 20, "字幕合并处理...", self.asr_service.merge_words, temp_files[1]),
            (task_id, 40, "翻译字幕...", self.translate_service.translate_srt, temp_files[2]),
            (task_id, 90, "字幕整理...", self.organize_asr, out_files),
        ]
        processor = self._create_and_run_processor(steps, task_id, audio_file_path)
        try:
            return processor.run(audio_file_path)
        finally:
            self._on_task_finished(processor, temp_files)

    def _run_for_srt(self, task_id: str, word_file_path: str):
        """
        处理字幕文件，输出翻译后的字幕文件。

        Args:
            task_id: 任务ID。
            word_file_path: 按字词ASR识别的字幕文件。
        """
        file_vo = FileVO(word_file_path)
        temp_files = self._generate_output_file_paths(file_vo, ["_asr.srt", "_translate.srt"])
        if self.config_args["files_args"]["directory"]["Output"]:
            out_files = self.config_args["files_args"]["directory"]["Output"] + "/" + Path(word_file_path).stem + "-C.srt"
        else:
            out_files = Path(word_file_path).parent + "/" + Path(word_file_path).stem + "-C.srt"
        steps = [
            (task_id, 0, "字幕合并处理...", self.asr_service.merge_words, temp_files[0]),
            (task_id, 30, "翻译字幕...", self.translate_service.translate_srt, temp_files[1]),
            (task_id, 90, "字幕整理...", self.organize_asr, out_files),
        ]
        asr_data = AsrDataBuilder.from_subtitle_file(word_file_path)
        processor = self._create_and_run_processor(steps, task_id, asr_data)
        try:
            return processor.run(asr_data)
        finally:
            self._on_task_finished(processor, temp_files)

    def organize_asr(self, out_file_path: str, asr_data: ASRData) -> ASRData:
        """
        整理字幕文件。

        Args:
            out_file_path: 输出文件。
            asr_data: 要处理的ASR数据。
        Returns:
                ASRData: 字幕整理后的ASR数据。
        """
        file_vo = FileVO(out_file_path)
        temp_file_path = os.path.join(file_vo.file_dir, file_vo.file_only_name + "_tmp.srt")
        self._save_srt_file(asr_data=asr_data, out_srt_file=temp_file_path)
        try:
            if not FileUtils.convert_to_unix_format(input_file_path=temp_file_path, output_file_path=out_file_path):
                self._save_srt_file(asr_data=asr_data, out_srt_file=out_file_path)
            self.log_info("完成字幕整理")
            return asr_data
        finally:
            self._remove_temp_file(str(temp_file_path))

    def _create_and_run_processor(self, steps, task_id, asr_data):
        """
        创建并运行步骤处理器。

        Args:
            steps: 处理步骤。
            task_id: 任务ID。
            asr_data: 对应的ASR数据。
        """
        processor = StepProcessor(steps=steps, log_to_ui_func=self.log_to_ui_func)
        processor.progress_signal.connect(self.on_task_progress)
        self.active_step_processor.add(processor)
        return processor

    @staticmethod
    def _generate_output_file_paths(file_vo: FileVO, suffixes: list[str]) -> list[LiteralString | str | bytes]:
        """
        生成输出文件路径。

        Args:
            file_vo: 处理的文件对象。
            suffixes：定义的文件后缀列表，每个后缀对应一个文件。
        Returns:
              list[str]: 文件路径名列表。
        """
        return [os.path.join(file_vo.file_dir, file_vo.file_only_name + suffix) for suffix in suffixes]

    def _remove_temp_file(self, file_path: str):
        """
        移除临时文件。

        Args:
            file_path: 要删除的文件。
        """
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                self.log_error(f"删除临时文件异常：{file_path}", e)

    def _on_task_finished(self, processor, temp_files: list[LiteralString | str | bytes] = None):
        """
        任务完成的触发器。

        Args:
            processor: 任务处理器。
            temp_files: 临时文件列表。
        """
        self.active_step_processor.discard(processor)
        if self.config_args["subtitle_args"]["need_remove_temp_file"] and temp_files:
            for file in temp_files:
                self._remove_temp_file(file)

    def check_tool(self) -> bool:
        is_available = True
        try:
            thread = threading.Thread(
                target=self._check_tool,
                args=(),
                daemon=True,
            )
            thread.start()
        except Exception as e:
            is_available = False
            self.log_warning("工具检查执行异常!")
        return is_available

    def _check_tool(self) -> None:
        # 检查FFmpeg是否安装
        if self.video_service.check_ffmpeg_available():
            self.log_info("FFmpeg 准备就绪!")
            # 检查 CUDA 是否可用。
            if self.video_service.check_cuda_available():
                self.log_info("FFmpeg 可以使用 CUDA 加速。")
                self.use_cuda = True
        else:
            is_available = False
            self.log_warning("FFmpeg 没有安装。")

        # 检查FasterWhisper是否安装
        if self.asr_service.check_fasterwhisper_available(self.config_args["asr_args"]):
            self.log_info("FasterWhisper 准备就绪!")
        else:
            is_available = False
            self.log_warning("Faster Whisper 没有安装。")

        # 检查FasterWhisper模型是否安装
        if self.asr_service.check_fasterwhisper_model_available(self.config_args["asr_args"]):
            self.log_info("FasterWhisper模型准备就绪!")
        else:
            is_available = False
            model = os.path.join(self.config_args["asr_args"]["model_dir"], "faster-whisper-" + self.config_args["asr_args"]["whisper_model"])
            self.log_warning(f"Faster Whisper 模型没有安装: {model}")

        # 检查LLM配置是否有效
        s, m = self.translate_service.check_llm_available(self.config_args["translate_args"])
        if s:
            self.log_info("LLM 准备就绪!")
        else:
            is_available = False
            self.log_warning(f"LLM配置有问题：{m}")
