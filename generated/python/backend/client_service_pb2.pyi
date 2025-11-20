from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_TYPE_UNSPECIFIED: _ClassVar[UserType]
    USER_TYPE_USER: _ClassVar[UserType]
    USER_TYPE_API_KEY: _ClassVar[UserType]

class CodeHostingResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CODE_HOSTING_RESOURCE_TYPE_UNSPECIFIED: _ClassVar[CodeHostingResourceType]
    CODE_HOSTING_RESOURCE_TYPE_GITHUB: _ClassVar[CodeHostingResourceType]
    CODE_HOSTING_RESOURCE_TYPE_GITLAB: _ClassVar[CodeHostingResourceType]

class ServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_TYPE_UNSPECIFIED: _ClassVar[ServiceType]
    SERVICE_TYPE_NODE: _ClassVar[ServiceType]

class CreateObservableServiceResponseErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREATE_OBSERVABLE_SERVICE_RESPONSE_ERROR_CODE_UNSPECIFIED: _ClassVar[CreateObservableServiceResponseErrorCode]
    CREATE_OBSERVABLE_SERVICE_RESPONSE_ERROR_CODE_INTERNAL: _ClassVar[CreateObservableServiceResponseErrorCode]
    CREATE_OBSERVABLE_SERVICE_RESPONSE_ERROR_CODE_NOT_AUTHORIZED: _ClassVar[CreateObservableServiceResponseErrorCode]
    CREATE_OBSERVABLE_SERVICE_RESPONSE_ERROR_CODE_NO_CODE_HOSTING_RESOURCE: _ClassVar[CreateObservableServiceResponseErrorCode]
    CREATE_OBSERVABLE_SERVICE_RESPONSE_ERROR_CODE_NO_REPO_FOUND: _ClassVar[CreateObservableServiceResponseErrorCode]

class VerifyRepoAccessResponseErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERIFY_REPO_ACCESS_RESPONSE_ERROR_CODE_UNSPECIFIED: _ClassVar[VerifyRepoAccessResponseErrorCode]
    VERIFY_REPO_ACCESS_RESPONSE_ERROR_CODE_INTERNAL: _ClassVar[VerifyRepoAccessResponseErrorCode]
    VERIFY_REPO_ACCESS_RESPONSE_ERROR_CODE_NOT_AUTHORIZED: _ClassVar[VerifyRepoAccessResponseErrorCode]
    VERIFY_REPO_ACCESS_RESPONSE_ERROR_CODE_NO_CODE_HOSTING_RESOURCE: _ClassVar[VerifyRepoAccessResponseErrorCode]
    VERIFY_REPO_ACCESS_RESPONSE_ERROR_CODE_REPO_NOT_FOUND: _ClassVar[VerifyRepoAccessResponseErrorCode]

class CreateApiKeyResponseErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREATE_API_KEY_RESPONSE_ERROR_CODE_UNSPECIFIED: _ClassVar[CreateApiKeyResponseErrorCode]
    CREATE_API_KEY_RESPONSE_ERROR_CODE_INTERNAL: _ClassVar[CreateApiKeyResponseErrorCode]
    CREATE_API_KEY_RESPONSE_ERROR_CODE_NOT_AUTHORIZED: _ClassVar[CreateApiKeyResponseErrorCode]
USER_TYPE_UNSPECIFIED: UserType
USER_TYPE_USER: UserType
USER_TYPE_API_KEY: UserType
CODE_HOSTING_RESOURCE_TYPE_UNSPECIFIED: CodeHostingResourceType
CODE_HOSTING_RESOURCE_TYPE_GITHUB: CodeHostingResourceType
CODE_HOSTING_RESOURCE_TYPE_GITLAB: CodeHostingResourceType
SERVICE_TYPE_UNSPECIFIED: ServiceType
SERVICE_TYPE_NODE: ServiceType
CREATE_OBSERVABLE_SERVICE_RESPONSE_ERROR_CODE_UNSPECIFIED: CreateObservableServiceResponseErrorCode
CREATE_OBSERVABLE_SERVICE_RESPONSE_ERROR_CODE_INTERNAL: CreateObservableServiceResponseErrorCode
CREATE_OBSERVABLE_SERVICE_RESPONSE_ERROR_CODE_NOT_AUTHORIZED: CreateObservableServiceResponseErrorCode
CREATE_OBSERVABLE_SERVICE_RESPONSE_ERROR_CODE_NO_CODE_HOSTING_RESOURCE: CreateObservableServiceResponseErrorCode
CREATE_OBSERVABLE_SERVICE_RESPONSE_ERROR_CODE_NO_REPO_FOUND: CreateObservableServiceResponseErrorCode
VERIFY_REPO_ACCESS_RESPONSE_ERROR_CODE_UNSPECIFIED: VerifyRepoAccessResponseErrorCode
VERIFY_REPO_ACCESS_RESPONSE_ERROR_CODE_INTERNAL: VerifyRepoAccessResponseErrorCode
VERIFY_REPO_ACCESS_RESPONSE_ERROR_CODE_NOT_AUTHORIZED: VerifyRepoAccessResponseErrorCode
VERIFY_REPO_ACCESS_RESPONSE_ERROR_CODE_NO_CODE_HOSTING_RESOURCE: VerifyRepoAccessResponseErrorCode
VERIFY_REPO_ACCESS_RESPONSE_ERROR_CODE_REPO_NOT_FOUND: VerifyRepoAccessResponseErrorCode
CREATE_API_KEY_RESPONSE_ERROR_CODE_UNSPECIFIED: CreateApiKeyResponseErrorCode
CREATE_API_KEY_RESPONSE_ERROR_CODE_INTERNAL: CreateApiKeyResponseErrorCode
CREATE_API_KEY_RESPONSE_ERROR_CODE_NOT_AUTHORIZED: CreateApiKeyResponseErrorCode

class GetAuthInfoRequest(_message.Message):
    __slots__ = ()
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class UserAuthInfo(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CODE_HOSTING_USERNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: UserType
    name: str
    email: str
    code_hosting_username: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[UserType, str]] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., code_hosting_username: _Optional[str] = ...) -> None: ...

class AuthInfoClient(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    CODE_HOSTING_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    domain: str
    feature_flags: _containers.RepeatedScalarFieldContainer[str]
    code_hosting_resources: _containers.RepeatedCompositeFieldContainer[CodeHostingResource]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., domain: _Optional[str] = ..., feature_flags: _Optional[_Iterable[str]] = ..., code_hosting_resources: _Optional[_Iterable[_Union[CodeHostingResource, _Mapping]]] = ...) -> None: ...

class CodeHostingResource(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: CodeHostingResourceType
    external_id: str
    def __init__(self, id: _Optional[int] = ..., type: _Optional[_Union[CodeHostingResourceType, str]] = ..., external_id: _Optional[str] = ...) -> None: ...

class GetAuthInfoResponse(_message.Message):
    __slots__ = ()
    USER_FIELD_NUMBER: _ClassVar[int]
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    user: UserAuthInfo
    clients: _containers.RepeatedCompositeFieldContainer[AuthInfoClient]
    def __init__(self, user: _Optional[_Union[UserAuthInfo, _Mapping]] = ..., clients: _Optional[_Iterable[_Union[AuthInfoClient, _Mapping]]] = ...) -> None: ...

class CreateObservableServiceRequest(_message.Message):
    __slots__ = ()
    REPO_OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
    REPO_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    APP_DIR_FIELD_NUMBER: _ClassVar[int]
    repo_owner_name: str
    repo_name: str
    service_type: ServiceType
    app_dir: str
    def __init__(self, repo_owner_name: _Optional[str] = ..., repo_name: _Optional[str] = ..., service_type: _Optional[_Union[ServiceType, str]] = ..., app_dir: _Optional[str] = ...) -> None: ...

class CreateObservableServiceResponseSuccess(_message.Message):
    __slots__ = ()
    OBSERVABLE_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    observable_service_id: str
    def __init__(self, observable_service_id: _Optional[str] = ...) -> None: ...

class CreateObservableServiceResponseError(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: CreateObservableServiceResponseErrorCode
    message: str
    def __init__(self, code: _Optional[_Union[CreateObservableServiceResponseErrorCode, str]] = ..., message: _Optional[str] = ...) -> None: ...

class CreateObservableServiceResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: CreateObservableServiceResponseSuccess
    error: CreateObservableServiceResponseError
    def __init__(self, success: _Optional[_Union[CreateObservableServiceResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[CreateObservableServiceResponseError, _Mapping]] = ...) -> None: ...

class VerifyRepoAccessRequest(_message.Message):
    __slots__ = ()
    REPO_OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
    REPO_NAME_FIELD_NUMBER: _ClassVar[int]
    repo_owner_name: str
    repo_name: str
    def __init__(self, repo_owner_name: _Optional[str] = ..., repo_name: _Optional[str] = ...) -> None: ...

class VerifyRepoAccessResponseSuccess(_message.Message):
    __slots__ = ()
    REPO_ID_FIELD_NUMBER: _ClassVar[int]
    repo_id: int
    def __init__(self, repo_id: _Optional[int] = ...) -> None: ...

class VerifyRepoAccessResponseError(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: VerifyRepoAccessResponseErrorCode
    message: str
    def __init__(self, code: _Optional[_Union[VerifyRepoAccessResponseErrorCode, str]] = ..., message: _Optional[str] = ...) -> None: ...

class VerifyRepoAccessResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: VerifyRepoAccessResponseSuccess
    error: VerifyRepoAccessResponseError
    def __init__(self, success: _Optional[_Union[VerifyRepoAccessResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[VerifyRepoAccessResponseError, _Mapping]] = ...) -> None: ...

class CreateApiKeyRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateApiKeyResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: CreateApiKeyResponseSuccess
    error: CreateApiKeyResponseError
    def __init__(self, success: _Optional[_Union[CreateApiKeyResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[CreateApiKeyResponseError, _Mapping]] = ...) -> None: ...

class CreateApiKeyResponseSuccess(_message.Message):
    __slots__ = ()
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key_id: str
    api_key: str
    def __init__(self, api_key_id: _Optional[str] = ..., api_key: _Optional[str] = ...) -> None: ...

class CreateApiKeyResponseError(_message.Message):
    __slots__ = ()
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: CreateApiKeyResponseErrorCode
    message: str
    def __init__(self, code: _Optional[_Union[CreateApiKeyResponseErrorCode, str]] = ..., message: _Optional[str] = ...) -> None: ...
