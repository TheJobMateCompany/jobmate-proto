from google.protobuf import timestamp_pb2 as _timestamp_pb2
from proto.common.v1 import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JobCard(_message.Message):
    __slots__ = ("id", "title", "company", "location", "source_url", "is_approved", "discovered_at", "description_preview")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    IS_APPROVED_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    company: str
    location: str
    source_url: str
    is_approved: bool
    discovered_at: _timestamp_pb2.Timestamp
    description_preview: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., company: _Optional[str] = ..., location: _Optional[str] = ..., source_url: _Optional[str] = ..., is_approved: bool = ..., discovered_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description_preview: _Optional[str] = ...) -> None: ...

class GetJobFeedRequest(_message.Message):
    __slots__ = ("user_id", "pagination")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    pagination: _types_pb2.PaginationRequest
    def __init__(self, user_id: _Optional[str] = ..., pagination: _Optional[_Union[_types_pb2.PaginationRequest, _Mapping]] = ...) -> None: ...

class GetJobFeedResponse(_message.Message):
    __slots__ = ("jobs", "pagination")
    JOBS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[JobCard]
    pagination: _types_pb2.PaginationResponse
    def __init__(self, jobs: _Optional[_Iterable[_Union[JobCard, _Mapping]]] = ..., pagination: _Optional[_Union[_types_pb2.PaginationResponse, _Mapping]] = ...) -> None: ...

class ApproveJobRequest(_message.Message):
    __slots__ = ("job_id", "user_id")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    user_id: str
    def __init__(self, job_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class AddJobUrlRequest(_message.Message):
    __slots__ = ("url", "user_id")
    URL_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    user_id: str
    def __init__(self, url: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...
