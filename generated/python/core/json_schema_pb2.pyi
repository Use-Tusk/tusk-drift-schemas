from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JsonSchemaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JSON_SCHEMA_TYPE_UNSPECIFIED: _ClassVar[JsonSchemaType]
    JSON_SCHEMA_TYPE_NUMBER: _ClassVar[JsonSchemaType]
    JSON_SCHEMA_TYPE_STRING: _ClassVar[JsonSchemaType]
    JSON_SCHEMA_TYPE_BOOLEAN: _ClassVar[JsonSchemaType]
    JSON_SCHEMA_TYPE_NULL: _ClassVar[JsonSchemaType]
    JSON_SCHEMA_TYPE_UNDEFINED: _ClassVar[JsonSchemaType]
    JSON_SCHEMA_TYPE_OBJECT: _ClassVar[JsonSchemaType]
    JSON_SCHEMA_TYPE_ORDERED_LIST: _ClassVar[JsonSchemaType]
    JSON_SCHEMA_TYPE_UNORDERED_LIST: _ClassVar[JsonSchemaType]
    JSON_SCHEMA_TYPE_FUNCTION: _ClassVar[JsonSchemaType]

class EncodingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENCODING_TYPE_UNSPECIFIED: _ClassVar[EncodingType]
    ENCODING_TYPE_BASE64: _ClassVar[EncodingType]

class DecodedType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DECODED_TYPE_UNSPECIFIED: _ClassVar[DecodedType]
    DECODED_TYPE_JSON: _ClassVar[DecodedType]
    DECODED_TYPE_HTML: _ClassVar[DecodedType]
    DECODED_TYPE_CSS: _ClassVar[DecodedType]
    DECODED_TYPE_JAVASCRIPT: _ClassVar[DecodedType]
    DECODED_TYPE_XML: _ClassVar[DecodedType]
    DECODED_TYPE_YAML: _ClassVar[DecodedType]
    DECODED_TYPE_MARKDOWN: _ClassVar[DecodedType]
    DECODED_TYPE_CSV: _ClassVar[DecodedType]
    DECODED_TYPE_SQL: _ClassVar[DecodedType]
    DECODED_TYPE_GRAPHQL: _ClassVar[DecodedType]
    DECODED_TYPE_PLAIN_TEXT: _ClassVar[DecodedType]
    DECODED_TYPE_FORM_DATA: _ClassVar[DecodedType]
    DECODED_TYPE_MULTIPART_FORM: _ClassVar[DecodedType]
    DECODED_TYPE_PDF: _ClassVar[DecodedType]
    DECODED_TYPE_AUDIO: _ClassVar[DecodedType]
    DECODED_TYPE_VIDEO: _ClassVar[DecodedType]
    DECODED_TYPE_GZIP: _ClassVar[DecodedType]
    DECODED_TYPE_BINARY: _ClassVar[DecodedType]
    DECODED_TYPE_JPEG: _ClassVar[DecodedType]
    DECODED_TYPE_PNG: _ClassVar[DecodedType]
    DECODED_TYPE_GIF: _ClassVar[DecodedType]
    DECODED_TYPE_WEBP: _ClassVar[DecodedType]
    DECODED_TYPE_SVG: _ClassVar[DecodedType]
    DECODED_TYPE_ZIP: _ClassVar[DecodedType]
JSON_SCHEMA_TYPE_UNSPECIFIED: JsonSchemaType
JSON_SCHEMA_TYPE_NUMBER: JsonSchemaType
JSON_SCHEMA_TYPE_STRING: JsonSchemaType
JSON_SCHEMA_TYPE_BOOLEAN: JsonSchemaType
JSON_SCHEMA_TYPE_NULL: JsonSchemaType
JSON_SCHEMA_TYPE_UNDEFINED: JsonSchemaType
JSON_SCHEMA_TYPE_OBJECT: JsonSchemaType
JSON_SCHEMA_TYPE_ORDERED_LIST: JsonSchemaType
JSON_SCHEMA_TYPE_UNORDERED_LIST: JsonSchemaType
JSON_SCHEMA_TYPE_FUNCTION: JsonSchemaType
ENCODING_TYPE_UNSPECIFIED: EncodingType
ENCODING_TYPE_BASE64: EncodingType
DECODED_TYPE_UNSPECIFIED: DecodedType
DECODED_TYPE_JSON: DecodedType
DECODED_TYPE_HTML: DecodedType
DECODED_TYPE_CSS: DecodedType
DECODED_TYPE_JAVASCRIPT: DecodedType
DECODED_TYPE_XML: DecodedType
DECODED_TYPE_YAML: DecodedType
DECODED_TYPE_MARKDOWN: DecodedType
DECODED_TYPE_CSV: DecodedType
DECODED_TYPE_SQL: DecodedType
DECODED_TYPE_GRAPHQL: DecodedType
DECODED_TYPE_PLAIN_TEXT: DecodedType
DECODED_TYPE_FORM_DATA: DecodedType
DECODED_TYPE_MULTIPART_FORM: DecodedType
DECODED_TYPE_PDF: DecodedType
DECODED_TYPE_AUDIO: DecodedType
DECODED_TYPE_VIDEO: DecodedType
DECODED_TYPE_GZIP: DecodedType
DECODED_TYPE_BINARY: DecodedType
DECODED_TYPE_JPEG: DecodedType
DECODED_TYPE_PNG: DecodedType
DECODED_TYPE_GIF: DecodedType
DECODED_TYPE_WEBP: DecodedType
DECODED_TYPE_SVG: DecodedType
DECODED_TYPE_ZIP: DecodedType

class JsonSchema(_message.Message):
    __slots__ = ()
    class PropertiesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: JsonSchema
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[JsonSchema, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    DECODED_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    type: JsonSchemaType
    properties: _containers.MessageMap[str, JsonSchema]
    items: JsonSchema
    encoding: EncodingType
    decoded_type: DecodedType
    match_importance: float
    def __init__(self, type: _Optional[_Union[JsonSchemaType, str]] = ..., properties: _Optional[_Mapping[str, JsonSchema]] = ..., items: _Optional[_Union[JsonSchema, _Mapping]] = ..., encoding: _Optional[_Union[EncodingType, str]] = ..., decoded_type: _Optional[_Union[DecodedType, str]] = ..., match_importance: _Optional[float] = ...) -> None: ...
