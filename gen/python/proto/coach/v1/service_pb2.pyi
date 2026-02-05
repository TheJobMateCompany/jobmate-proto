from proto.common.v1 import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AnalyzeJobRequest(_message.Message):
    __slots__ = ("user_id", "job_id", "job_description_text")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_DESCRIPTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    job_id: str
    job_description_text: str
    def __init__(self, user_id: _Optional[str] = ..., job_id: _Optional[str] = ..., job_description_text: _Optional[str] = ...) -> None: ...

class AnalysisResult(_message.Message):
    __slots__ = ("match_score", "pros", "cons", "missing_keywords")
    MATCH_SCORE_FIELD_NUMBER: _ClassVar[int]
    PROS_FIELD_NUMBER: _ClassVar[int]
    CONS_FIELD_NUMBER: _ClassVar[int]
    MISSING_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    match_score: int
    pros: _containers.RepeatedScalarFieldContainer[str]
    cons: _containers.RepeatedScalarFieldContainer[str]
    missing_keywords: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, match_score: _Optional[int] = ..., pros: _Optional[_Iterable[str]] = ..., cons: _Optional[_Iterable[str]] = ..., missing_keywords: _Optional[_Iterable[str]] = ...) -> None: ...

class GenerateCoverLetterRequest(_message.Message):
    __slots__ = ("user_id", "job_description", "tone")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    job_description: str
    tone: str
    def __init__(self, user_id: _Optional[str] = ..., job_description: _Optional[str] = ..., tone: _Optional[str] = ...) -> None: ...

class GenerateCoverLetterResponse(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...
