from google.protobuf import timestamp_pb2 as _timestamp_pb2
from proto.common.v1 import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNKNOWN: _ClassVar[ApplicationStatus]
    STATUS_TO_APPLY: _ClassVar[ApplicationStatus]
    STATUS_APPLIED: _ClassVar[ApplicationStatus]
    STATUS_INTERVIEW: _ClassVar[ApplicationStatus]
    STATUS_OFFER: _ClassVar[ApplicationStatus]
    STATUS_REJECTED: _ClassVar[ApplicationStatus]
    STATUS_HIRED: _ClassVar[ApplicationStatus]
STATUS_UNKNOWN: ApplicationStatus
STATUS_TO_APPLY: ApplicationStatus
STATUS_APPLIED: ApplicationStatus
STATUS_INTERVIEW: ApplicationStatus
STATUS_OFFER: ApplicationStatus
STATUS_REJECTED: ApplicationStatus
STATUS_HIRED: ApplicationStatus

class Profile(_message.Message):
    __slots__ = ("user_id", "status", "skills", "location", "bio")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    BIO_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    status: str
    skills: _containers.RepeatedCompositeFieldContainer[_types_pb2.Skill]
    location: str
    bio: str
    def __init__(self, user_id: _Optional[str] = ..., status: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[_types_pb2.Skill, _Mapping]]] = ..., location: _Optional[str] = ..., bio: _Optional[str] = ...) -> None: ...

class GetProfileRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class UpdateProfileRequest(_message.Message):
    __slots__ = ("user_id", "profile_data")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_DATA_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    profile_data: Profile
    def __init__(self, user_id: _Optional[str] = ..., profile_data: _Optional[_Union[Profile, _Mapping]] = ...) -> None: ...

class Application(_message.Message):
    __slots__ = ("id", "user_id", "job_id", "status", "company_name", "job_title", "created_at", "updated_at", "match_score")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_TITLE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    MATCH_SCORE_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    job_id: str
    status: ApplicationStatus
    company_name: str
    job_title: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    match_score: int
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., job_id: _Optional[str] = ..., status: _Optional[_Union[ApplicationStatus, str]] = ..., company_name: _Optional[str] = ..., job_title: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., match_score: _Optional[int] = ...) -> None: ...

class CreateApplicationRequest(_message.Message):
    __slots__ = ("user_id", "job_feed_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_FEED_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    job_feed_id: str
    def __init__(self, user_id: _Optional[str] = ..., job_feed_id: _Optional[str] = ...) -> None: ...

class GetApplicationsRequest(_message.Message):
    __slots__ = ("user_id", "pagination")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    pagination: _types_pb2.PaginationRequest
    def __init__(self, user_id: _Optional[str] = ..., pagination: _Optional[_Union[_types_pb2.PaginationRequest, _Mapping]] = ...) -> None: ...

class GetApplicationsResponse(_message.Message):
    __slots__ = ("applications", "pagination")
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    applications: _containers.RepeatedCompositeFieldContainer[Application]
    pagination: _types_pb2.PaginationResponse
    def __init__(self, applications: _Optional[_Iterable[_Union[Application, _Mapping]]] = ..., pagination: _Optional[_Union[_types_pb2.PaginationResponse, _Mapping]] = ...) -> None: ...

class UpdateStatusRequest(_message.Message):
    __slots__ = ("application_id", "new_status")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    new_status: ApplicationStatus
    def __init__(self, application_id: _Optional[str] = ..., new_status: _Optional[_Union[ApplicationStatus, str]] = ...) -> None: ...
