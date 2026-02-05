from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PaginationRequest(_message.Message):
    __slots__ = ("page", "page_size")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class PaginationResponse(_message.Message):
    __slots__ = ("total_count", "current_page", "total_pages")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    current_page: int
    total_pages: int
    def __init__(self, total_count: _Optional[int] = ..., current_page: _Optional[int] = ..., total_pages: _Optional[int] = ...) -> None: ...

class Skill(_message.Message):
    __slots__ = ("name", "level", "is_hard_skill")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_HARD_SKILL_FIELD_NUMBER: _ClassVar[int]
    name: str
    level: str
    is_hard_skill: bool
    def __init__(self, name: _Optional[str] = ..., level: _Optional[str] = ..., is_hard_skill: bool = ...) -> None: ...
