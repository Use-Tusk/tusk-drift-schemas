from core import span_pb2 as _span_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MATCH_SCOPE_UNSPECIFIED: _ClassVar[MatchScope]
    MATCH_SCOPE_TRACE: _ClassVar[MatchScope]
    MATCH_SCOPE_GLOBAL: _ClassVar[MatchScope]

class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MATCH_TYPE_UNSPECIFIED: _ClassVar[MatchType]
    MATCH_TYPE_INPUT_VALUE_HASH: _ClassVar[MatchType]
    MATCH_TYPE_INPUT_VALUE_HASH_REDUCED_SCHEMA: _ClassVar[MatchType]
    MATCH_TYPE_INPUT_SCHEMA_HASH: _ClassVar[MatchType]
    MATCH_TYPE_INPUT_SCHEMA_HASH_REDUCED_SCHEMA: _ClassVar[MatchType]
    MATCH_TYPE_FUZZY: _ClassVar[MatchType]
    MATCH_TYPE_FALLBACK: _ClassVar[MatchType]

class TraceTestFailureReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_TEST_FAILURE_REASON_UNSPECIFIED: _ClassVar[TraceTestFailureReason]
    TRACE_TEST_FAILURE_REASON_MOCK_NOT_FOUND: _ClassVar[TraceTestFailureReason]
    TRACE_TEST_FAILURE_REASON_RESPONSE_MISMATCH: _ClassVar[TraceTestFailureReason]
    TRACE_TEST_FAILURE_REASON_NO_RESPONSE: _ClassVar[TraceTestFailureReason]

class DriftRunCIStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DRIFT_RUN_CI_STATUS_UNSPECIFIED: _ClassVar[DriftRunCIStatus]
    DRIFT_RUN_CI_STATUS_RUNNING: _ClassVar[DriftRunCIStatus]
    DRIFT_RUN_CI_STATUS_SUCCESS: _ClassVar[DriftRunCIStatus]
    DRIFT_RUN_CI_STATUS_FAILURE: _ClassVar[DriftRunCIStatus]
MATCH_SCOPE_UNSPECIFIED: MatchScope
MATCH_SCOPE_TRACE: MatchScope
MATCH_SCOPE_GLOBAL: MatchScope
MATCH_TYPE_UNSPECIFIED: MatchType
MATCH_TYPE_INPUT_VALUE_HASH: MatchType
MATCH_TYPE_INPUT_VALUE_HASH_REDUCED_SCHEMA: MatchType
MATCH_TYPE_INPUT_SCHEMA_HASH: MatchType
MATCH_TYPE_INPUT_SCHEMA_HASH_REDUCED_SCHEMA: MatchType
MATCH_TYPE_FUZZY: MatchType
MATCH_TYPE_FALLBACK: MatchType
TRACE_TEST_FAILURE_REASON_UNSPECIFIED: TraceTestFailureReason
TRACE_TEST_FAILURE_REASON_MOCK_NOT_FOUND: TraceTestFailureReason
TRACE_TEST_FAILURE_REASON_RESPONSE_MISMATCH: TraceTestFailureReason
TRACE_TEST_FAILURE_REASON_NO_RESPONSE: TraceTestFailureReason
DRIFT_RUN_CI_STATUS_UNSPECIFIED: DriftRunCIStatus
DRIFT_RUN_CI_STATUS_RUNNING: DriftRunCIStatus
DRIFT_RUN_CI_STATUS_SUCCESS: DriftRunCIStatus
DRIFT_RUN_CI_STATUS_FAILURE: DriftRunCIStatus

class GetGlobalSpansRequest(_message.Message):
    __slots__ = ()
    OBSERVABLE_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_CURSOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    observable_service_id: str
    pagination_cursor: str
    page_size: int
    def __init__(self, observable_service_id: _Optional[str] = ..., pagination_cursor: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class GetGlobalSpansResponseSuccess(_message.Message):
    __slots__ = ()
    SPANS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    spans: _containers.RepeatedCompositeFieldContainer[_span_pb2.Span]
    next_cursor: str
    total_count: int
    def __init__(self, spans: _Optional[_Iterable[_Union[_span_pb2.Span, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetGlobalSpansResponseError(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetGlobalSpansResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GetGlobalSpansResponseSuccess
    error: GetGlobalSpansResponseError
    def __init__(self, success: _Optional[_Union[GetGlobalSpansResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[GetGlobalSpansResponseError, _Mapping]] = ...) -> None: ...

class GetPreAppStartSpansRequest(_message.Message):
    __slots__ = ()
    OBSERVABLE_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_CURSOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    observable_service_id: str
    pagination_cursor: str
    page_size: int
    def __init__(self, observable_service_id: _Optional[str] = ..., pagination_cursor: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class GetPreAppStartSpansResponseSuccess(_message.Message):
    __slots__ = ()
    SPANS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    spans: _containers.RepeatedCompositeFieldContainer[_span_pb2.Span]
    next_cursor: str
    total_count: int
    def __init__(self, spans: _Optional[_Iterable[_Union[_span_pb2.Span, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetPreAppStartSpansResponseError(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetPreAppStartSpansResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GetPreAppStartSpansResponseSuccess
    error: GetPreAppStartSpansResponseError
    def __init__(self, success: _Optional[_Union[GetPreAppStartSpansResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[GetPreAppStartSpansResponseError, _Mapping]] = ...) -> None: ...

class CreateDriftRunRequest(_message.Message):
    __slots__ = ()
    OBSERVABLE_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CLI_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    PR_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CHECK_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    observable_service_id: str
    cli_version: str
    commit_sha: str
    pr_number: str
    branch_name: str
    external_check_run_id: str
    def __init__(self, observable_service_id: _Optional[str] = ..., cli_version: _Optional[str] = ..., commit_sha: _Optional[str] = ..., pr_number: _Optional[str] = ..., branch_name: _Optional[str] = ..., external_check_run_id: _Optional[str] = ...) -> None: ...

class CreateDriftRunResponseSuccess(_message.Message):
    __slots__ = ()
    DRIFT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    drift_run_id: str
    def __init__(self, drift_run_id: _Optional[str] = ...) -> None: ...

class CreateDriftRunResponseError(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class CreateDriftRunResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: CreateDriftRunResponseSuccess
    error: CreateDriftRunResponseError
    def __init__(self, success: _Optional[_Union[CreateDriftRunResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[CreateDriftRunResponseError, _Mapping]] = ...) -> None: ...

class GetDriftRunTraceTestsRequest(_message.Message):
    __slots__ = ()
    DRIFT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_CURSOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    drift_run_id: str
    pagination_cursor: str
    page_size: int
    def __init__(self, drift_run_id: _Optional[str] = ..., pagination_cursor: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class TraceTest(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_SPAN_RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    SPANS_FIELD_NUMBER: _ClassVar[int]
    id: str
    trace_id: str
    server_span_recording_id: str
    spans: _containers.RepeatedCompositeFieldContainer[_span_pb2.Span]
    def __init__(self, id: _Optional[str] = ..., trace_id: _Optional[str] = ..., server_span_recording_id: _Optional[str] = ..., spans: _Optional[_Iterable[_Union[_span_pb2.Span, _Mapping]]] = ...) -> None: ...

class GetDriftRunTraceTestsResponseSuccess(_message.Message):
    __slots__ = ()
    TRACE_TESTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    trace_tests: _containers.RepeatedCompositeFieldContainer[TraceTest]
    next_cursor: str
    total_count: int
    def __init__(self, trace_tests: _Optional[_Iterable[_Union[TraceTest, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetDriftRunTraceTestsResponseError(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetDriftRunTraceTestsResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GetDriftRunTraceTestsResponseSuccess
    error: GetDriftRunTraceTestsResponseError
    def __init__(self, success: _Optional[_Union[GetDriftRunTraceTestsResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[GetDriftRunTraceTestsResponseError, _Mapping]] = ...) -> None: ...

class GetTraceTestRequest(_message.Message):
    __slots__ = ()
    OBSERVABLE_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_TEST_ID_FIELD_NUMBER: _ClassVar[int]
    observable_service_id: str
    trace_test_id: str
    def __init__(self, observable_service_id: _Optional[str] = ..., trace_test_id: _Optional[str] = ...) -> None: ...

class GetTraceTestResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GetTraceTestResponseSuccess
    error: GetTraceTestResponseError
    def __init__(self, success: _Optional[_Union[GetTraceTestResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[GetTraceTestResponseError, _Mapping]] = ...) -> None: ...

class GetTraceTestResponseSuccess(_message.Message):
    __slots__ = ()
    TRACE_TEST_FIELD_NUMBER: _ClassVar[int]
    trace_test: TraceTest
    def __init__(self, trace_test: _Optional[_Union[TraceTest, _Mapping]] = ...) -> None: ...

class GetTraceTestResponseError(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetAllTraceTestsRequest(_message.Message):
    __slots__ = ()
    OBSERVABLE_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_CURSOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    observable_service_id: str
    pagination_cursor: str
    page_size: int
    def __init__(self, observable_service_id: _Optional[str] = ..., pagination_cursor: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class GetAllTraceTestsResponseSuccess(_message.Message):
    __slots__ = ()
    TRACE_TESTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    trace_tests: _containers.RepeatedCompositeFieldContainer[TraceTest]
    next_cursor: str
    total_count: int
    def __init__(self, trace_tests: _Optional[_Iterable[_Union[TraceTest, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetAllTraceTestsResponseError(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetAllTraceTestsResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GetAllTraceTestsResponseSuccess
    error: GetAllTraceTestsResponseError
    def __init__(self, success: _Optional[_Union[GetAllTraceTestsResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[GetAllTraceTestsResponseError, _Mapping]] = ...) -> None: ...

class Deviation(_message.Message):
    __slots__ = ()
    FIELD_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    field: str
    description: str
    def __init__(self, field: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class MatchLevel(_message.Message):
    __slots__ = ()
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_SCOPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SIMILARITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    TOP_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    match_type: MatchType
    match_scope: MatchScope
    match_description: str
    similarity_score: float
    top_candidates: _containers.RepeatedCompositeFieldContainer[SimilarityCandidate]
    def __init__(self, match_type: _Optional[_Union[MatchType, str]] = ..., match_scope: _Optional[_Union[MatchScope, str]] = ..., match_description: _Optional[str] = ..., similarity_score: _Optional[float] = ..., top_candidates: _Optional[_Iterable[_Union[SimilarityCandidate, _Mapping]]] = ...) -> None: ...

class SimilarityCandidate(_message.Message):
    __slots__ = ()
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    span_id: str
    score: float
    def __init__(self, span_id: _Optional[str] = ..., score: _Optional[float] = ...) -> None: ...

class TraceTestSpanResult(_message.Message):
    __slots__ = ()
    REPLAY_SPAN_FIELD_NUMBER: _ClassVar[int]
    MATCHED_SPAN_RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_LEVEL_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    DEVIATIONS_FIELD_NUMBER: _ClassVar[int]
    replay_span: _span_pb2.Span
    matched_span_recording_id: str
    match_level: MatchLevel
    stack_trace: str
    deviations: _containers.RepeatedCompositeFieldContainer[Deviation]
    def __init__(self, replay_span: _Optional[_Union[_span_pb2.Span, _Mapping]] = ..., matched_span_recording_id: _Optional[str] = ..., match_level: _Optional[_Union[MatchLevel, _Mapping]] = ..., stack_trace: _Optional[str] = ..., deviations: _Optional[_Iterable[_Union[Deviation, _Mapping]]] = ...) -> None: ...

class TraceTestResult(_message.Message):
    __slots__ = ()
    TRACE_TEST_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TEST_FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    TEST_FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPLAY_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    REPLAY_SERVER_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_RESULTS_FIELD_NUMBER: _ClassVar[int]
    trace_test_id: str
    test_success: bool
    test_failure_reason: TraceTestFailureReason
    test_failure_message: str
    replay_trace_id: str
    replay_server_span_id: str
    span_results: _containers.RepeatedCompositeFieldContainer[TraceTestSpanResult]
    def __init__(self, trace_test_id: _Optional[str] = ..., test_success: _Optional[bool] = ..., test_failure_reason: _Optional[_Union[TraceTestFailureReason, str]] = ..., test_failure_message: _Optional[str] = ..., replay_trace_id: _Optional[str] = ..., replay_server_span_id: _Optional[str] = ..., span_results: _Optional[_Iterable[_Union[TraceTestSpanResult, _Mapping]]] = ...) -> None: ...

class UploadTraceTestResultsRequest(_message.Message):
    __slots__ = ()
    DRIFT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CLI_VERSION_FIELD_NUMBER: _ClassVar[int]
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    TRACE_TEST_RESULTS_FIELD_NUMBER: _ClassVar[int]
    drift_run_id: str
    cli_version: str
    sdk_version: str
    trace_test_results: _containers.RepeatedCompositeFieldContainer[TraceTestResult]
    def __init__(self, drift_run_id: _Optional[str] = ..., cli_version: _Optional[str] = ..., sdk_version: _Optional[str] = ..., trace_test_results: _Optional[_Iterable[_Union[TraceTestResult, _Mapping]]] = ...) -> None: ...

class UploadTraceTestResultsResponseSuccess(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UploadTraceTestResultsResponseError(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class UploadTraceTestResultsResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: UploadTraceTestResultsResponseSuccess
    error: UploadTraceTestResultsResponseError
    def __init__(self, success: _Optional[_Union[UploadTraceTestResultsResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[UploadTraceTestResultsResponseError, _Mapping]] = ...) -> None: ...

class UpdateDriftRunCIStatusRequest(_message.Message):
    __slots__ = ()
    DRIFT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CI_STATUS_FIELD_NUMBER: _ClassVar[int]
    CI_STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    drift_run_id: str
    ci_status: DriftRunCIStatus
    ci_status_message: str
    def __init__(self, drift_run_id: _Optional[str] = ..., ci_status: _Optional[_Union[DriftRunCIStatus, str]] = ..., ci_status_message: _Optional[str] = ...) -> None: ...

class UpdateDriftRunCIStatusResponseSuccess(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UpdateDriftRunCIStatusResponseError(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class UpdateDriftRunCIStatusResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: UpdateDriftRunCIStatusResponseSuccess
    error: UpdateDriftRunCIStatusResponseError
    def __init__(self, success: _Optional[_Union[UpdateDriftRunCIStatusResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[UpdateDriftRunCIStatusResponseError, _Mapping]] = ...) -> None: ...
