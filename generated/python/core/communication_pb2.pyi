import datetime

from core import span_pb2 as _span_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE_TYPE_UNSPECIFIED: _ClassVar[MessageType]
    MESSAGE_TYPE_SDK_CONNECT: _ClassVar[MessageType]
    MESSAGE_TYPE_MOCK_REQUEST: _ClassVar[MessageType]
    MESSAGE_TYPE_INBOUND_SPAN: _ClassVar[MessageType]
    MESSAGE_TYPE_ALERT: _ClassVar[MessageType]
    MESSAGE_TYPE_ENV_VAR_REQUEST: _ClassVar[MessageType]
MESSAGE_TYPE_UNSPECIFIED: MessageType
MESSAGE_TYPE_SDK_CONNECT: MessageType
MESSAGE_TYPE_MOCK_REQUEST: MessageType
MESSAGE_TYPE_INBOUND_SPAN: MessageType
MESSAGE_TYPE_ALERT: MessageType
MESSAGE_TYPE_ENV_VAR_REQUEST: MessageType

class ConnectRequest(_message.Message):
    __slots__ = ()
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    MIN_CLI_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    service_id: str
    sdk_version: str
    min_cli_version: str
    metadata: _struct_pb2.Struct
    def __init__(self, service_id: _Optional[str] = ..., sdk_version: _Optional[str] = ..., min_cli_version: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ConnectResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str
    def __init__(self, success: _Optional[bool] = ..., error: _Optional[str] = ...) -> None: ...

class GetMockRequest(_message.Message):
    __slots__ = ()
    class TagsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_SPAN_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    test_id: str
    outbound_span: _span_pb2.Span
    stack_trace: str
    operation: str
    tags: _containers.ScalarMap[str, str]
    requested_at: _timestamp_pb2.Timestamp
    def __init__(self, request_id: _Optional[str] = ..., test_id: _Optional[str] = ..., outbound_span: _Optional[_Union[_span_pb2.Span, _Mapping]] = ..., stack_trace: _Optional[str] = ..., operation: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., requested_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetMockResponse(_message.Message):
    __slots__ = ()
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    MATCHED_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    MATCHED_AT_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    found: bool
    response_data: _struct_pb2.Struct
    metadata: _struct_pb2.Struct
    error: str
    error_code: str
    matched_span_id: str
    matched_at: _timestamp_pb2.Timestamp
    def __init__(self, request_id: _Optional[str] = ..., found: _Optional[bool] = ..., response_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., error: _Optional[str] = ..., error_code: _Optional[str] = ..., matched_span_id: _Optional[str] = ..., matched_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SDKMessage(_message.Message):
    __slots__ = ()
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_MOCK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SEND_INBOUND_SPAN_FOR_REPLAY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SEND_ALERT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ENV_VAR_REQUEST_FIELD_NUMBER: _ClassVar[int]
    type: MessageType
    request_id: str
    connect_request: ConnectRequest
    get_mock_request: GetMockRequest
    send_inbound_span_for_replay_request: SendInboundSpanForReplayRequest
    send_alert_request: SendAlertRequest
    env_var_request: EnvVarRequest
    def __init__(self, type: _Optional[_Union[MessageType, str]] = ..., request_id: _Optional[str] = ..., connect_request: _Optional[_Union[ConnectRequest, _Mapping]] = ..., get_mock_request: _Optional[_Union[GetMockRequest, _Mapping]] = ..., send_inbound_span_for_replay_request: _Optional[_Union[SendInboundSpanForReplayRequest, _Mapping]] = ..., send_alert_request: _Optional[_Union[SendAlertRequest, _Mapping]] = ..., env_var_request: _Optional[_Union[EnvVarRequest, _Mapping]] = ...) -> None: ...

class CLIMessage(_message.Message):
    __slots__ = ()
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_MOCK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SEND_INBOUND_SPAN_FOR_REPLAY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ENV_VAR_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    type: MessageType
    request_id: str
    connect_response: ConnectResponse
    get_mock_response: GetMockResponse
    send_inbound_span_for_replay_response: SendInboundSpanForReplayResponse
    env_var_response: EnvVarResponse
    def __init__(self, type: _Optional[_Union[MessageType, str]] = ..., request_id: _Optional[str] = ..., connect_response: _Optional[_Union[ConnectResponse, _Mapping]] = ..., get_mock_response: _Optional[_Union[GetMockResponse, _Mapping]] = ..., send_inbound_span_for_replay_response: _Optional[_Union[SendInboundSpanForReplayResponse, _Mapping]] = ..., env_var_response: _Optional[_Union[EnvVarResponse, _Mapping]] = ...) -> None: ...

class SendInboundSpanForReplayRequest(_message.Message):
    __slots__ = ()
    SPAN_FIELD_NUMBER: _ClassVar[int]
    span: _span_pb2.Span
    def __init__(self, span: _Optional[_Union[_span_pb2.Span, _Mapping]] = ...) -> None: ...

class SendInboundSpanForReplayResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class SendAlertRequest(_message.Message):
    __slots__ = ()
    VERSION_MISMATCH_FIELD_NUMBER: _ClassVar[int]
    UNPATCHED_DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    version_mismatch: InstrumentationVersionMismatchAlert
    unpatched_dependency: UnpatchedDependencyAlert
    def __init__(self, version_mismatch: _Optional[_Union[InstrumentationVersionMismatchAlert, _Mapping]] = ..., unpatched_dependency: _Optional[_Union[UnpatchedDependencyAlert, _Mapping]] = ...) -> None: ...

class InstrumentationVersionMismatchAlert(_message.Message):
    __slots__ = ()
    MODULE_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    module_name: str
    requested_version: str
    supported_versions: _containers.RepeatedScalarFieldContainer[str]
    sdk_version: str
    def __init__(self, module_name: _Optional[str] = ..., requested_version: _Optional[str] = ..., supported_versions: _Optional[_Iterable[str]] = ..., sdk_version: _Optional[str] = ...) -> None: ...

class UnpatchedDependencyAlert(_message.Message):
    __slots__ = ()
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    TRACE_TEST_SERVER_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    stack_trace: str
    trace_test_server_span_id: str
    sdk_version: str
    def __init__(self, stack_trace: _Optional[str] = ..., trace_test_server_span_id: _Optional[str] = ..., sdk_version: _Optional[str] = ...) -> None: ...

class EnvVarRequest(_message.Message):
    __slots__ = ()
    TRACE_TEST_SERVER_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    trace_test_server_span_id: str
    def __init__(self, trace_test_server_span_id: _Optional[str] = ...) -> None: ...

class EnvVarResponse(_message.Message):
    __slots__ = ()
    class EnvVarsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENV_VARS_FIELD_NUMBER: _ClassVar[int]
    env_vars: _containers.ScalarMap[str, str]
    def __init__(self, env_vars: _Optional[_Mapping[str, str]] = ...) -> None: ...
