# coding: utf8
from enum import Enum

from enums.base_enums import ThreeFieldEnum


class FasterWhisperModelEnum(Enum):
    # TINY = "tiny"
    # BASE = "base"
    SMALL = "small"
    MEDIUM = "medium"
    # LARGE_V1 = "large-v1"
    LARGE_V2 = "large-v2"
    LARGE_V3 = "large-v3"
    MEDIUM_EN = "medium-en"
    LARGE_V3_JA = "large-v3-ja"
    LARGE_V3_ZH = "large-v3-zh"

    @staticmethod
    def read_name(value: str):
        for item in FasterWhisperModelEnum:
            if item._value_ == value:
                return item._value_
        return None


class FasterWhisperDeviceEnum(Enum):
    AUTO = "auto"
    CDUA = "cuda"
    CPU = "cpu"


class VadMethodEnum(ThreeFieldEnum):
    """ VAD方法 """
    SILERO_V3 = ("silero_v3", "silero_v3", "适用于需要实时处理的应用")
    SILERO_V4 = ("silero_v4", "silero_v4", "适用于需要实时处理的应用")
    PYANNOTE_V3 = ("pyannote_v3", "pyannote_v3", "适用于语音重叠或多说话人场景")
    PYANNOTE_ONNX_V3 = ("pyannote_onnx_v3", "pyannote_onnx_v3", "适用于推理速度至关重要的场景")
    AUDITOK = ("auditok", "auditok", "非常适合处理大量音频文件")
    WEBRTC = ("webrtc", "webrtc", "适用于对低延迟至关重要的场景")
    NONE = ("", "", "")

    @staticmethod
    def read_code(value: str):
        for item in VadMethodEnum:
            if item._value_ == value:
                return item.code
        return None

    @staticmethod
    def read_desc(value: str):
        for item in VadMethodEnum:
            if item._value_ == value:
                return item.description
        return None
