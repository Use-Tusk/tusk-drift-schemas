import datetime

from core import json_schema_pb2 as _json_schema_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PACKAGE_TYPE_UNSPECIFIED: _ClassVar[PackageType]
    PACKAGE_TYPE_HTTP: _ClassVar[PackageType]
    PACKAGE_TYPE_GRAPHQL: _ClassVar[PackageType]
    PACKAGE_TYPE_GRPC: _ClassVar[PackageType]
    PACKAGE_TYPE_PG: _ClassVar[PackageType]
    PACKAGE_TYPE_MYSQL: _ClassVar[PackageType]
    PACKAGE_TYPE_MONGODB: _ClassVar[PackageType]
    PACKAGE_TYPE_REDIS: _ClassVar[PackageType]
    PACKAGE_TYPE_KAFKA: _ClassVar[PackageType]
    PACKAGE_TYPE_RABBITMQ: _ClassVar[PackageType]
    PACKAGE_TYPE_FIRESTORE: _ClassVar[PackageType]
    PACKAGE_TYPE_PRISMA: _ClassVar[PackageType]

class SpanKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPAN_KIND_UNSPECIFIED: _ClassVar[SpanKind]
    SPAN_KIND_INTERNAL: _ClassVar[SpanKind]
    SPAN_KIND_SERVER: _ClassVar[SpanKind]
    SPAN_KIND_CLIENT: _ClassVar[SpanKind]
    SPAN_KIND_PRODUCER: _ClassVar[SpanKind]
    SPAN_KIND_CONSUMER: _ClassVar[SpanKind]

class StatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_CODE_UNSPECIFIED: _ClassVar[StatusCode]
    STATUS_CODE_OK: _ClassVar[StatusCode]
    STATUS_CODE_ERROR: _ClassVar[StatusCode]
PACKAGE_TYPE_UNSPECIFIED: PackageType
PACKAGE_TYPE_HTTP: PackageType
PACKAGE_TYPE_GRAPHQL: PackageType
PACKAGE_TYPE_GRPC: PackageType
PACKAGE_TYPE_PG: PackageType
PACKAGE_TYPE_MYSQL: PackageType
PACKAGE_TYPE_MONGODB: PackageType
PACKAGE_TYPE_REDIS: PackageType
PACKAGE_TYPE_KAFKA: PackageType
PACKAGE_TYPE_RABBITMQ: PackageType
PACKAGE_TYPE_FIRESTORE: PackageType
PACKAGE_TYPE_PRISMA: PackageType
SPAN_KIND_UNSPECIFIED: SpanKind
SPAN_KIND_INTERNAL: SpanKind
SPAN_KIND_SERVER: SpanKind
SPAN_KIND_CLIENT: SpanKind
SPAN_KIND_PRODUCER: SpanKind
SPAN_KIND_CONSUMER: SpanKind
STATUS_CODE_UNSPECIFIED: StatusCode
STATUS_CODE_OK: StatusCode
STATUS_CODE_ERROR: StatusCode

class Span(_message.Message):
    __slots__ = ()
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBMODULE_NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INPUT_VALUE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VALUE_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_HASH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_HASH_FIELD_NUMBER: _ClassVar[int]
    INPUT_VALUE_HASH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VALUE_HASH_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_PRE_APP_START_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_SPAN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    span_id: str
    parent_span_id: str
    name: str
    package_name: str
    instrumentation_name: str
    submodule_name: str
    package_type: PackageType
    input_value: _struct_pb2.Struct
    output_value: _struct_pb2.Struct
    input_schema: _json_schema_pb2.JsonSchema
    output_schema: _json_schema_pb2.JsonSchema
    input_schema_hash: str
    output_schema_hash: str
    input_value_hash: str
    output_value_hash: str
    kind: SpanKind
    status: SpanStatus
    is_pre_app_start: bool
    timestamp: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    is_root_span: bool
    metadata: _struct_pb2.Struct
    def __init__(self, trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., parent_span_id: _Optional[str] = ..., name: _Optional[str] = ..., package_name: _Optional[str] = ..., instrumentation_name: _Optional[str] = ..., submodule_name: _Optional[str] = ..., package_type: _Optional[_Union[PackageType, str]] = ..., input_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., output_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., input_schema: _Optional[_Union[_json_schema_pb2.JsonSchema, _Mapping]] = ..., output_schema: _Optional[_Union[_json_schema_pb2.JsonSchema, _Mapping]] = ..., input_schema_hash: _Optional[str] = ..., output_schema_hash: _Optional[str] = ..., input_value_hash: _Optional[str] = ..., output_value_hash: _Optional[str] = ..., kind: _Optional[_Union[SpanKind, str]] = ..., status: _Optional[_Union[SpanStatus, _Mapping]] = ..., is_pre_app_start: _Optional[bool] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., is_root_span: _Optional[bool] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class SpanStatus(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: StatusCode
    message: str
    def __init__(self, code: _Optional[_Union[StatusCode, str]] = ..., message: _Optional[str] = ...) -> None: ...

class SpanEvent(_message.Message):
    __slots__ = ()
    class AttributesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    timestamp: _timestamp_pb2.Timestamp
    attributes: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, name: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., attributes: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class SpanLink(_message.Message):
    __slots__ = ()
    class AttributesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    span_id: str
    attributes: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., attributes: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class Trace(_message.Message):
    __slots__ = ()
    class MetadataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPANS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    spans: _containers.RepeatedCompositeFieldContainer[Span]
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, trace_id: _Optional[str] = ..., spans: _Optional[_Iterable[_Union[Span, _Mapping]]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
