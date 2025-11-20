import datetime

from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSACTION_STATE_UNSPECIFIED: _ClassVar[TransactionState]
    TRANSACTION_STATE_IDLE: _ClassVar[TransactionState]
    TRANSACTION_STATE_ACTIVE: _ClassVar[TransactionState]
    TRANSACTION_STATE_IDLE_IN_TRANSACTION: _ClassVar[TransactionState]
    TRANSACTION_STATE_IDLE_IN_FAILED_TRANSACTION: _ClassVar[TransactionState]

class IsolationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ISOLATION_LEVEL_UNSPECIFIED: _ClassVar[IsolationLevel]
    ISOLATION_LEVEL_READ_UNCOMMITTED: _ClassVar[IsolationLevel]
    ISOLATION_LEVEL_READ_COMMITTED: _ClassVar[IsolationLevel]
    ISOLATION_LEVEL_REPEATABLE_READ: _ClassVar[IsolationLevel]
    ISOLATION_LEVEL_SERIALIZABLE: _ClassVar[IsolationLevel]
TRANSACTION_STATE_UNSPECIFIED: TransactionState
TRANSACTION_STATE_IDLE: TransactionState
TRANSACTION_STATE_ACTIVE: TransactionState
TRANSACTION_STATE_IDLE_IN_TRANSACTION: TransactionState
TRANSACTION_STATE_IDLE_IN_FAILED_TRANSACTION: TransactionState
ISOLATION_LEVEL_UNSPECIFIED: IsolationLevel
ISOLATION_LEVEL_READ_UNCOMMITTED: IsolationLevel
ISOLATION_LEVEL_READ_COMMITTED: IsolationLevel
ISOLATION_LEVEL_REPEATABLE_READ: IsolationLevel
ISOLATION_LEVEL_SERIALIZABLE: IsolationLevel

class PostgreSQLQuery(_message.Message):
    __slots__ = ()
    class TagsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    text: str
    values: _containers.RepeatedScalarFieldContainer[str]
    client_type: str
    connection: PostgreSQLConnection
    options: QueryOptions
    query_id: str
    tags: _containers.ScalarMap[str, str]
    def __init__(self, text: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ..., client_type: _Optional[str] = ..., connection: _Optional[_Union[PostgreSQLConnection, _Mapping]] = ..., options: _Optional[_Union[QueryOptions, _Mapping]] = ..., query_id: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PostgreSQLConnection(_message.Message):
    __slots__ = ()
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SSL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    database_name: str
    username: str
    host: str
    port: int
    application_name: str
    connection_id: str
    ssl_enabled: bool
    server_version: str
    def __init__(self, database_name: _Optional[str] = ..., username: _Optional[str] = ..., host: _Optional[str] = ..., port: _Optional[int] = ..., application_name: _Optional[str] = ..., connection_id: _Optional[str] = ..., ssl_enabled: _Optional[bool] = ..., server_version: _Optional[str] = ...) -> None: ...

class QueryOptions(_message.Message):
    __slots__ = ()
    class CustomOptionsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STATEMENT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    QUERY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    BINARY_MODE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_NAME_FIELD_NUMBER: _ClassVar[int]
    FETCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    statement_timeout: int
    query_timeout: int
    binary_mode: bool
    cursor_name: str
    fetch_size: int
    read_only: bool
    custom_options: _containers.ScalarMap[str, str]
    def __init__(self, statement_timeout: _Optional[int] = ..., query_timeout: _Optional[int] = ..., binary_mode: _Optional[bool] = ..., cursor_name: _Optional[str] = ..., fetch_size: _Optional[int] = ..., read_only: _Optional[bool] = ..., custom_options: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PostgreSQLResult(_message.Message):
    __slots__ = ()
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    OID_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    command: str
    row_count: int
    oid: int
    rows: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    fields: _containers.RepeatedCompositeFieldContainer[PostgreSQLField]
    execution_info: QueryExecutionInfo
    error: PostgreSQLError
    def __init__(self, command: _Optional[str] = ..., row_count: _Optional[int] = ..., oid: _Optional[int] = ..., rows: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ..., fields: _Optional[_Iterable[_Union[PostgreSQLField, _Mapping]]] = ..., execution_info: _Optional[_Union[QueryExecutionInfo, _Mapping]] = ..., error: _Optional[_Union[PostgreSQLError, _Mapping]] = ...) -> None: ...

class PostgreSQLField(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    table_id: int
    column_id: int
    data_type_id: int
    data_type_size: int
    data_type_modifier: int
    format: str
    data_type_name: str
    nullable: bool
    primary_key: bool
    def __init__(self, name: _Optional[str] = ..., table_id: _Optional[int] = ..., column_id: _Optional[int] = ..., data_type_id: _Optional[int] = ..., data_type_size: _Optional[int] = ..., data_type_modifier: _Optional[int] = ..., format: _Optional[str] = ..., data_type_name: _Optional[str] = ..., nullable: _Optional[bool] = ..., primary_key: _Optional[bool] = ...) -> None: ...

class QueryExecutionInfo(_message.Message):
    __slots__ = ()
    PARSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PLAN_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    ROWS_EXAMINED_FIELD_NUMBER: _ClassVar[int]
    ROWS_RETURNED_FIELD_NUMBER: _ClassVar[int]
    BYTES_SENT_FIELD_NUMBER: _ClassVar[int]
    BYTES_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_PLAN_FIELD_NUMBER: _ClassVar[int]
    NOTICES_FIELD_NUMBER: _ClassVar[int]
    parse_time_ms: int
    plan_time_ms: int
    execute_time_ms: int
    total_time_ms: int
    rows_examined: int
    rows_returned: int
    bytes_sent: int
    bytes_received: int
    execution_plan: str
    notices: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parse_time_ms: _Optional[int] = ..., plan_time_ms: _Optional[int] = ..., execute_time_ms: _Optional[int] = ..., total_time_ms: _Optional[int] = ..., rows_examined: _Optional[int] = ..., rows_returned: _Optional[int] = ..., bytes_sent: _Optional[int] = ..., bytes_received: _Optional[int] = ..., execution_plan: _Optional[str] = ..., notices: _Optional[_Iterable[str]] = ...) -> None: ...

class PostgreSQLError(_message.Message):
    __slots__ = ()
    SQL_STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_FIELD_NUMBER: _ClassVar[int]
    sql_state: str
    message: str
    detail: str
    hint: str
    position: str
    where: str
    schema_name: str
    table_name: str
    column_name: str
    constraint_name: str
    data_type_name: str
    file: str
    line: str
    routine: str
    def __init__(self, sql_state: _Optional[str] = ..., message: _Optional[str] = ..., detail: _Optional[str] = ..., hint: _Optional[str] = ..., position: _Optional[str] = ..., where: _Optional[str] = ..., schema_name: _Optional[str] = ..., table_name: _Optional[str] = ..., column_name: _Optional[str] = ..., constraint_name: _Optional[str] = ..., data_type_name: _Optional[str] = ..., file: _Optional[str] = ..., line: _Optional[str] = ..., routine: _Optional[str] = ...) -> None: ...

class PostgreSQLPreparedStatement(_message.Message):
    __slots__ = ()
    STATEMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_TYPES_FIELD_NUMBER: _ClassVar[int]
    PREPARED_AT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    statement_name: str
    query_text: str
    parameter_types: _containers.RepeatedCompositeFieldContainer[PostgreSQLParameterType]
    prepared_at: _timestamp_pb2.Timestamp
    execution_count: int
    def __init__(self, statement_name: _Optional[str] = ..., query_text: _Optional[str] = ..., parameter_types: _Optional[_Iterable[_Union[PostgreSQLParameterType, _Mapping]]] = ..., prepared_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., execution_count: _Optional[int] = ...) -> None: ...

class PostgreSQLParameterType(_message.Message):
    __slots__ = ()
    POSITION_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    position: int
    data_type_id: int
    data_type_name: str
    nullable: bool
    def __init__(self, position: _Optional[int] = ..., data_type_id: _Optional[int] = ..., data_type_name: _Optional[str] = ..., nullable: _Optional[bool] = ...) -> None: ...

class PostgreSQLTransaction(_message.Message):
    __slots__ = ()
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ISOLATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    state: TransactionState
    isolation_level: IsolationLevel
    read_only: bool
    started_at: _timestamp_pb2.Timestamp
    def __init__(self, transaction_id: _Optional[str] = ..., state: _Optional[_Union[TransactionState, str]] = ..., isolation_level: _Optional[_Union[IsolationLevel, str]] = ..., read_only: _Optional[bool] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PostgreSQLBatch(_message.Message):
    __slots__ = ()
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    STOP_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    RETURN_RESULTS_FIELD_NUMBER: _ClassVar[int]
    queries: _containers.RepeatedCompositeFieldContainer[PostgreSQLQuery]
    stop_on_error: bool
    return_results: bool
    def __init__(self, queries: _Optional[_Iterable[_Union[PostgreSQLQuery, _Mapping]]] = ..., stop_on_error: _Optional[bool] = ..., return_results: _Optional[bool] = ...) -> None: ...

class PostgreSQLBatchResult(_message.Message):
    __slots__ = ()
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_QUERIES_FIELD_NUMBER: _ClassVar[int]
    FAILED_QUERIES_FIELD_NUMBER: _ClassVar[int]
    FIRST_ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[PostgreSQLResult]
    successful_queries: int
    failed_queries: int
    first_error: PostgreSQLError
    def __init__(self, results: _Optional[_Iterable[_Union[PostgreSQLResult, _Mapping]]] = ..., successful_queries: _Optional[int] = ..., failed_queries: _Optional[int] = ..., first_error: _Optional[_Union[PostgreSQLError, _Mapping]] = ...) -> None: ...
