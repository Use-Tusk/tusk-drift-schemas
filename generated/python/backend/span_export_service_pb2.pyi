from core import span_pb2 as _span_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportSpansRequest(_message.Message):
    __slots__ = ()
    OBSERVABLE_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    SDK_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SPANS_FIELD_NUMBER: _ClassVar[int]
    observable_service_id: str
    environment: str
    sdk_version: str
    sdk_instance_id: str
    spans: _containers.RepeatedCompositeFieldContainer[_span_pb2.Span]
    def __init__(self, observable_service_id: _Optional[str] = ..., environment: _Optional[str] = ..., sdk_version: _Optional[str] = ..., sdk_instance_id: _Optional[str] = ..., spans: _Optional[_Iterable[_Union[_span_pb2.Span, _Mapping]]] = ...) -> None: ...

class ExportSpansResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...
