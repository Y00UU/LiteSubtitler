# coding: utf8
from enum import Enum
import time


class CommonUtils:
    """通用工具类，提供一些常用的工具方法。"""

    @staticmethod
    def hex_to_int(hex_color):
        # 去掉颜色值前面的 '#' 符号
        hex_color = hex_color.lstrip("#")
        # 将十六进制字符串转换为整数
        color_int = int(hex_color, 16)
        return color_int

    @staticmethod
    def rgb_to_int(r, g, b):
        # 使用位操作将 RGB 组合成一个整数
        color_int = (r << 16) | (g << 8) | b
        return color_int

    @staticmethod
    def print_progress_bar(
        iteration: int, total: int, prefix: str = "", suffix: str = "", decimals: int = 1, length: int = 50, fill: str = "█", print_end: str = ""
    ):
        """在终端中打印进度条。

        该方法用于在终端中动态显示进度条，适用于长时间任务的进度跟踪。

        Args:
            iteration (int): 当前进度（必须）。
            total (int): 总步数（必须）。
            prefix (str, optional): 进度条前缀，默认为空。
            suffix (str, optional): 进度条后缀，默认为空。
            decimals (int, optional): 百分比的小数位数，默认为1。
            length (int, optional): 进度条的长度（字符数），默认为50。
            fill (str, optional): 进度条填充字符，默认为'█'。
            print_end (str, optional): 结束时打印的字符，默认为回车符（\r）。
        """
        # 计算当前进度百分比
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        # 计算填充的长度
        filled_length = int(length * iteration // total)
        # 构建进度条字符串
        bar = fill * filled_length + "-" * (length - filled_length)
        # 打印进度条
        print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=print_end)
        # 当进度达到100%时打印新行
        if iteration == total:
            print()

    from typing import Any

    @staticmethod
    def convert_to_str(message: Any) -> str:
        """
        将基础数据类型的 message 转换为字符串。

        支持的类型包括：
        - int, float
        - bool
        - str（原样返回）
        - None
        - list, tuple, set, dict（使用 str() 原生转换）
        - Enum 成员（返回 name 或 value）
        """
        if isinstance(message, str):
            return message
        elif message is None:
            return "None"
        elif isinstance(message, bool):
            return str(message).lower()  # "true" 或 "false"
        elif isinstance(message, (int, float)):
            return str(message)
        elif isinstance(message, list) or isinstance(message, tuple) or isinstance(message, set):
            return ", ".join(CommonUtils.convert_to_str(item) for item in message)
        elif isinstance(message, dict):
            return "{" + ", ".join(f"{CommonUtils.convert_to_str(k)}: {CommonUtils.convert_to_str(v)}" for k, v in message.items()) + "}"
        elif isinstance(message, Enum):
            return str(message.value)  # 或者返回 message.name，根据需求选择
        else:
            return str(message)


if __name__ == "__main__":
    # 示例用法
    total_steps = 100
    for i in range(total_steps + 1):
        time.sleep(0.1)  # 模拟工作负载
        CommonUtils.print_progress_bar(i, total_steps, prefix="进度:", suffix="完成", length=50)
