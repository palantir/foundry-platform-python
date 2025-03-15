#  Copyright 2024 Palantir Technologies, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from __future__ import annotations

import typing

import pydantic
import typing_extensions

from foundry import _core as core

DataValue = typing.Any
"""
Represents the value of data in the following format. Note that these values can be nested, for example an array of structs.
| Type                        | JSON encoding                                         | Example                                                                       |
|-----------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------|
| Array                       | array                                                 | `["alpha", "bravo", "charlie"]`                                               |
| Attachment                  | string                                                | `"ri.attachments.main.attachment.2f944bae-5851-4204-8615-920c969a9f2e"`       |
| Boolean                     | boolean                                               | `true`                                                                        |
| Byte                        | number                                                | `31`                                                                          |
| Date                        | ISO 8601 extended local date string                   | `"2021-05-01"`                                                                |
| Decimal                     | string                                                | `"2.718281828"`                                                               |
| Float                       | number                                                | `3.14159265`                                                                  |
| Double                      | number                                                | `3.14159265`                                                                  |
| Integer                     | number                                                | `238940`                                                                      |
| Long                        | string                                                | `"58319870951433"`                                                            |
| Marking                     | string                                                | `"MU"`                                                                        |
| Null                        | null                                                  | `null`                                                                        |
| Set                         | array                                                 | `["alpha", "bravo", "charlie"]`                                               |
| Short                       | number                                                | `8739`                                                                        |
| String                      | string                                                | `"Call me Ishmael"`                                                           |
| Struct                      | JSON object                                           | `{"name": "John Doe", "age": 42}`                                             |
| TwoDimensionalAggregation   | JSON object                                           | `{"groups": [{"key": "alpha", "value": 100}, {"key": "beta", "value": 101}]}` |
| ThreeDimensionalAggregation | JSON object                                           | `{"groups": [{"key": "NYC", "groups": [{"key": "Engineer", "value" : 100}]}]}`|
| Timestamp                   | ISO 8601 extended offset date-time string in UTC zone | `"2021-01-04T05:00:00Z"`                                                      |
"""


class ExecuteQueryResponse(pydantic.BaseModel):
    """ExecuteQueryResponse"""

    value: DataValue
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ExecuteQueryResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ExecuteQueryResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ExecuteQueryResponseDict(typing_extensions.TypedDict):
    """ExecuteQueryResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: DataValue


FunctionRid = core.RID
"""The unique resource identifier of a Function, useful for interacting with other Foundry APIs."""


FunctionVersion = str
"""
The version of the given Function, written `<major>.<minor>.<patch>-<tag>`, where `-<tag>` is optional.
Examples: `1.2.3`, `1.2.3-rc1`.
"""


class Parameter(pydantic.BaseModel):
    """Details about a parameter of a query."""

    description: typing.Optional[str] = None
    data_type: QueryDataType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ParameterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ParameterDict, self.model_dump(by_alias=True, exclude_none=True))


class ParameterDict(typing_extensions.TypedDict):
    """Details about a parameter of a query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    description: typing_extensions.NotRequired[str]
    dataType: QueryDataTypeDict


ParameterId = str
"""
The unique identifier of the parameter. Parameters are used as inputs when an action or query is applied.
Parameters can be viewed and managed in the **Ontology Manager**.
"""


class Query(pydantic.BaseModel):
    """Query"""

    api_name: QueryApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, Parameter]
    output: QueryDataType
    rid: FunctionRid
    version: FunctionVersion
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "QueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(QueryDict, self.model_dump(by_alias=True, exclude_none=True))


QueryAggregationKeyType = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateType",
        "core_models.BooleanType",
        "core_models.StringType",
        "core_models.DoubleType",
        "QueryAggregationRangeType",
        "core_models.IntegerType",
        "core_models.TimestampType",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by query aggregation keys."""


QueryAggregationKeyTypeDict = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateTypeDict",
        "core_models.BooleanTypeDict",
        "core_models.StringTypeDict",
        "core_models.DoubleTypeDict",
        "QueryAggregationRangeTypeDict",
        "core_models.IntegerTypeDict",
        "core_models.TimestampTypeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by query aggregation keys."""


QueryAggregationRangeSubType = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateType",
        "core_models.DoubleType",
        "core_models.IntegerType",
        "core_models.TimestampType",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by query aggregation ranges."""


QueryAggregationRangeSubTypeDict = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateTypeDict",
        "core_models.DoubleTypeDict",
        "core_models.IntegerTypeDict",
        "core_models.TimestampTypeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by query aggregation ranges."""


class QueryAggregationRangeType(pydantic.BaseModel):
    """QueryAggregationRangeType"""

    sub_type: QueryAggregationRangeSubType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["range"] = "range"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "QueryAggregationRangeTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            QueryAggregationRangeTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class QueryAggregationRangeTypeDict(typing_extensions.TypedDict):
    """QueryAggregationRangeType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: QueryAggregationRangeSubTypeDict
    type: typing.Literal["range"]


QueryAggregationValueType = typing_extensions.Annotated[
    typing.Union["core_models.DateType", "core_models.DoubleType", "core_models.TimestampType"],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by query aggregation keys."""


QueryAggregationValueTypeDict = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateTypeDict", "core_models.DoubleTypeDict", "core_models.TimestampTypeDict"
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by query aggregation keys."""


QueryApiName = str
"""The name of the Query in the API."""


class QueryArrayType(pydantic.BaseModel):
    """QueryArrayType"""

    sub_type: QueryDataType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "QueryArrayTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(QueryArrayTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class QueryArrayTypeDict(typing_extensions.TypedDict):
    """QueryArrayType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: QueryDataTypeDict
    type: typing.Literal["array"]


QueryDataType = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateType",
        "QueryStructType",
        "QuerySetType",
        "core_models.StringType",
        "core_models.DoubleType",
        "core_models.IntegerType",
        "ThreeDimensionalAggregation",
        "QueryUnionType",
        "core_models.FloatType",
        "core_models.LongType",
        "core_models.BooleanType",
        "core_models.UnsupportedType",
        "core_models.AttachmentType",
        "core_models.NullType",
        "QueryArrayType",
        "TwoDimensionalAggregation",
        "ValueTypeReference",
        "core_models.TimestampType",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Query parameters or outputs."""


QueryDataTypeDict = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateTypeDict",
        "QueryStructTypeDict",
        "QuerySetTypeDict",
        "core_models.StringTypeDict",
        "core_models.DoubleTypeDict",
        "core_models.IntegerTypeDict",
        "ThreeDimensionalAggregationDict",
        "QueryUnionTypeDict",
        "core_models.FloatTypeDict",
        "core_models.LongTypeDict",
        "core_models.BooleanTypeDict",
        "core_models.UnsupportedTypeDict",
        "core_models.AttachmentTypeDict",
        "core_models.NullTypeDict",
        "QueryArrayTypeDict",
        "TwoDimensionalAggregationDict",
        "ValueTypeReferenceDict",
        "core_models.TimestampTypeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Query parameters or outputs."""


class QueryDict(typing_extensions.TypedDict):
    """Query"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: QueryApiName
    description: typing_extensions.NotRequired[str]
    displayName: typing_extensions.NotRequired[core_models.DisplayName]
    parameters: typing.Dict[ParameterId, ParameterDict]
    output: QueryDataTypeDict
    rid: FunctionRid
    version: FunctionVersion


QueryRuntimeErrorParameter = str
"""QueryRuntimeErrorParameter"""


class QuerySetType(pydantic.BaseModel):
    """QuerySetType"""

    sub_type: QueryDataType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["set"] = "set"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "QuerySetTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(QuerySetTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class QuerySetTypeDict(typing_extensions.TypedDict):
    """QuerySetType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: QueryDataTypeDict
    type: typing.Literal["set"]


class QueryStructField(pydantic.BaseModel):
    """QueryStructField"""

    name: StructFieldName
    field_type: QueryDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "QueryStructFieldDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(QueryStructFieldDict, self.model_dump(by_alias=True, exclude_none=True))


class QueryStructFieldDict(typing_extensions.TypedDict):
    """QueryStructField"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: StructFieldName
    fieldType: QueryDataTypeDict


class QueryStructType(pydantic.BaseModel):
    """QueryStructType"""

    fields: typing.List[QueryStructField]
    type: typing.Literal["struct"] = "struct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "QueryStructTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(QueryStructTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class QueryStructTypeDict(typing_extensions.TypedDict):
    """QueryStructType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fields: typing.List[QueryStructFieldDict]
    type: typing.Literal["struct"]


class QueryUnionType(pydantic.BaseModel):
    """QueryUnionType"""

    union_types: typing.List[QueryDataType] = pydantic.Field(alias=str("unionTypes"))  # type: ignore[literal-required]
    type: typing.Literal["union"] = "union"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "QueryUnionTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(QueryUnionTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class QueryUnionTypeDict(typing_extensions.TypedDict):
    """QueryUnionType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    unionTypes: typing.List[QueryDataTypeDict]
    type: typing.Literal["union"]


StructFieldName = str
"""The name of a field in a `Struct`."""


class ThreeDimensionalAggregation(pydantic.BaseModel):
    """ThreeDimensionalAggregation"""

    key_type: QueryAggregationKeyType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: TwoDimensionalAggregation = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["threeDimensionalAggregation"] = "threeDimensionalAggregation"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ThreeDimensionalAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ThreeDimensionalAggregationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ThreeDimensionalAggregationDict(typing_extensions.TypedDict):
    """ThreeDimensionalAggregation"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    keyType: QueryAggregationKeyTypeDict
    valueType: TwoDimensionalAggregationDict
    type: typing.Literal["threeDimensionalAggregation"]


class TwoDimensionalAggregation(pydantic.BaseModel):
    """TwoDimensionalAggregation"""

    key_type: QueryAggregationKeyType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: QueryAggregationValueType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["twoDimensionalAggregation"] = "twoDimensionalAggregation"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "TwoDimensionalAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            TwoDimensionalAggregationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class TwoDimensionalAggregationDict(typing_extensions.TypedDict):
    """TwoDimensionalAggregation"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    keyType: QueryAggregationKeyTypeDict
    valueType: QueryAggregationValueTypeDict
    type: typing.Literal["twoDimensionalAggregation"]


class ValueType(pydantic.BaseModel):
    """ValueType"""

    rid: ValueTypeRid
    version: ValueTypeVersion
    version_id: ValueTypeVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    api_name: ValueTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[ValueTypeDescription] = None
    base_type: typing.Optional[ValueTypeDataType] = pydantic.Field(alias=str("baseType"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ValueTypeDict, self.model_dump(by_alias=True, exclude_none=True))


ValueTypeApiName = str
"""The registered API name for the value type."""


ValueTypeDataType = typing_extensions.Annotated[
    typing.Union[
        "ValueTypeDataTypeDateType",
        "ValueTypeDataTypeStructType",
        "ValueTypeDataTypeStringType",
        "ValueTypeDataTypeByteType",
        "ValueTypeDataTypeDoubleType",
        "ValueTypeDataTypeOptionalType",
        "ValueTypeDataTypeIntegerType",
        "ValueTypeDataTypeUnionType",
        "ValueTypeDataTypeFloatType",
        "ValueTypeDataTypeLongType",
        "ValueTypeDataTypeBooleanType",
        "ValueTypeDataTypeArrayType",
        "ValueTypeDataTypeBinaryType",
        "ValueTypeDataTypeValueTypeReference",
        "ValueTypeDataTypeShortType",
        "ValueTypeDataTypeDecimalType",
        "ValueTypeDataTypeMapType",
        "ValueTypeDataTypeTimestampType",
    ],
    pydantic.Field(discriminator="type"),
]
"""The underlying base type of a value type."""


class ValueTypeDataTypeArrayType(pydantic.BaseModel):
    """ValueTypeDataTypeArrayType"""

    sub_type: ValueTypeDataType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeArrayTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeArrayTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeArrayTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeArrayType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: ValueTypeDataTypeDict
    type: typing.Literal["array"]


class ValueTypeDataTypeBinaryType(pydantic.BaseModel):
    """ValueTypeDataTypeBinaryType"""

    type: typing.Literal["binary"] = "binary"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeBinaryTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeBinaryTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeBinaryTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeBinaryType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["binary"]


class ValueTypeDataTypeBooleanType(pydantic.BaseModel):
    """ValueTypeDataTypeBooleanType"""

    type: typing.Literal["boolean"] = "boolean"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeBooleanTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeBooleanTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeBooleanTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeBooleanType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["boolean"]


class ValueTypeDataTypeByteType(pydantic.BaseModel):
    """ValueTypeDataTypeByteType"""

    type: typing.Literal["byte"] = "byte"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeByteTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeByteTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeByteTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeByteType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["byte"]


class ValueTypeDataTypeDateType(pydantic.BaseModel):
    """ValueTypeDataTypeDateType"""

    type: typing.Literal["date"] = "date"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeDateTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeDateTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeDateTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeDateType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["date"]


class ValueTypeDataTypeDecimalType(pydantic.BaseModel):
    """ValueTypeDataTypeDecimalType"""

    type: typing.Literal["decimal"] = "decimal"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeDecimalTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeDecimalTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeDecimalTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeDecimalType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["decimal"]


ValueTypeDataTypeDict = typing_extensions.Annotated[
    typing.Union[
        "ValueTypeDataTypeDateTypeDict",
        "ValueTypeDataTypeStructTypeDict",
        "ValueTypeDataTypeStringTypeDict",
        "ValueTypeDataTypeByteTypeDict",
        "ValueTypeDataTypeDoubleTypeDict",
        "ValueTypeDataTypeOptionalTypeDict",
        "ValueTypeDataTypeIntegerTypeDict",
        "ValueTypeDataTypeUnionTypeDict",
        "ValueTypeDataTypeFloatTypeDict",
        "ValueTypeDataTypeLongTypeDict",
        "ValueTypeDataTypeBooleanTypeDict",
        "ValueTypeDataTypeArrayTypeDict",
        "ValueTypeDataTypeBinaryTypeDict",
        "ValueTypeDataTypeValueTypeReferenceDict",
        "ValueTypeDataTypeShortTypeDict",
        "ValueTypeDataTypeDecimalTypeDict",
        "ValueTypeDataTypeMapTypeDict",
        "ValueTypeDataTypeTimestampTypeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""The underlying base type of a value type."""


class ValueTypeDataTypeDoubleType(pydantic.BaseModel):
    """ValueTypeDataTypeDoubleType"""

    type: typing.Literal["double"] = "double"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeDoubleTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeDoubleTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeDoubleTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeDoubleType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["double"]


class ValueTypeDataTypeFloatType(pydantic.BaseModel):
    """ValueTypeDataTypeFloatType"""

    type: typing.Literal["float"] = "float"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeFloatTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeFloatTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeFloatTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeFloatType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["float"]


class ValueTypeDataTypeIntegerType(pydantic.BaseModel):
    """ValueTypeDataTypeIntegerType"""

    type: typing.Literal["integer"] = "integer"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeIntegerTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeIntegerTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeIntegerTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeIntegerType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["integer"]


class ValueTypeDataTypeLongType(pydantic.BaseModel):
    """ValueTypeDataTypeLongType"""

    type: typing.Literal["long"] = "long"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeLongTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeLongTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeLongTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeLongType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["long"]


class ValueTypeDataTypeMapType(pydantic.BaseModel):
    """ValueTypeDataTypeMapType"""

    key_type: ValueTypeDataType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: ValueTypeDataType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeMapTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeMapTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeMapTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeMapType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    keyType: ValueTypeDataTypeDict
    valueType: ValueTypeDataTypeDict
    type: typing.Literal["map"]


class ValueTypeDataTypeOptionalType(pydantic.BaseModel):
    """ValueTypeDataTypeOptionalType"""

    wrapped_type: ValueTypeDataType = pydantic.Field(alias=str("wrappedType"))  # type: ignore[literal-required]
    type: typing.Literal["optional"] = "optional"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeOptionalTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeOptionalTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeOptionalTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeOptionalType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    wrappedType: ValueTypeDataTypeDict
    type: typing.Literal["optional"]


class ValueTypeDataTypeShortType(pydantic.BaseModel):
    """ValueTypeDataTypeShortType"""

    type: typing.Literal["short"] = "short"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeShortTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeShortTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeShortTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeShortType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["short"]


class ValueTypeDataTypeStringType(pydantic.BaseModel):
    """ValueTypeDataTypeStringType"""

    type: typing.Literal["string"] = "string"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeStringTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeStringTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeStringTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeStringType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["string"]


class ValueTypeDataTypeStructElement(pydantic.BaseModel):
    """ValueTypeDataTypeStructElement"""

    name: ValueTypeDataTypeStructFieldIdentifier
    field_type: ValueTypeDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeStructElementDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeStructElementDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeStructElementDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeStructElement"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: ValueTypeDataTypeStructFieldIdentifier
    fieldType: ValueTypeDataTypeDict


ValueTypeDataTypeStructFieldIdentifier = str
"""ValueTypeDataTypeStructFieldIdentifier"""


class ValueTypeDataTypeStructType(pydantic.BaseModel):
    """ValueTypeDataTypeStructType"""

    fields: typing.List[ValueTypeDataTypeStructElement]
    type: typing.Literal["struct"] = "struct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeStructTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeStructTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeStructTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeStructType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fields: typing.List[ValueTypeDataTypeStructElementDict]
    type: typing.Literal["struct"]


class ValueTypeDataTypeTimestampType(pydantic.BaseModel):
    """ValueTypeDataTypeTimestampType"""

    type: typing.Literal["timestamp"] = "timestamp"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeTimestampTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeTimestampTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeTimestampTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeTimestampType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["timestamp"]


class ValueTypeDataTypeUnionType(pydantic.BaseModel):
    """ValueTypeDataTypeUnionType"""

    member_types: typing.List[ValueTypeDataType] = pydantic.Field(alias=str("memberTypes"))  # type: ignore[literal-required]
    type: typing.Literal["union"] = "union"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeUnionTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeUnionTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeDataTypeUnionTypeDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeUnionType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    memberTypes: typing.List[ValueTypeDataTypeDict]
    type: typing.Literal["union"]


class ValueTypeDataTypeValueTypeReference(pydantic.BaseModel):
    """ValueTypeDataTypeValueTypeReference"""

    rid: ValueTypeRid
    version_id: ValueTypeVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    type: typing.Literal["valueTypeReference"] = "valueTypeReference"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeDataTypeValueTypeReferenceDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeDataTypeValueTypeReferenceDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class ValueTypeDataTypeValueTypeReferenceDict(typing_extensions.TypedDict):
    """ValueTypeDataTypeValueTypeReference"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ValueTypeRid
    versionId: ValueTypeVersionId
    type: typing.Literal["valueTypeReference"]


ValueTypeDescription = str
"""A description of the value type."""


class ValueTypeDict(typing_extensions.TypedDict):
    """ValueType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ValueTypeRid
    version: ValueTypeVersion
    versionId: ValueTypeVersionId
    apiName: ValueTypeApiName
    displayName: core_models.DisplayName
    description: typing_extensions.NotRequired[ValueTypeDescription]
    baseType: typing_extensions.NotRequired[ValueTypeDataTypeDict]


class ValueTypeReference(pydantic.BaseModel):
    """A reference to a value type that has been registered in the Ontology."""

    rid: ValueTypeRid
    version_id: ValueTypeVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    type: typing.Literal["valueTypeReference"] = "valueTypeReference"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValueTypeReferenceDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValueTypeReferenceDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValueTypeReferenceDict(typing_extensions.TypedDict):
    """A reference to a value type that has been registered in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ValueTypeRid
    versionId: ValueTypeVersionId
    type: typing.Literal["valueTypeReference"]


ValueTypeRid = core.RID
"""The RID of a value type that has been registered in the Ontology."""


ValueTypeVersion = str
"""The version of a value type that has been registered in the Ontology."""


ValueTypeVersionId = core.UUID
"""The version ID of a value type that has been registered in the Ontology."""


class VersionId(pydantic.BaseModel):
    """VersionId"""

    rid: ValueTypeRid
    version: ValueTypeVersion
    version_id: ValueTypeVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    api_name: ValueTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[ValueTypeDescription] = None
    base_type: typing.Optional[ValueTypeDataType] = pydantic.Field(alias=str("baseType"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "VersionIdDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(VersionIdDict, self.model_dump(by_alias=True, exclude_none=True))


class VersionIdDict(typing_extensions.TypedDict):
    """VersionId"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ValueTypeRid
    version: ValueTypeVersion
    versionId: ValueTypeVersionId
    apiName: ValueTypeApiName
    displayName: core_models.DisplayName
    description: typing_extensions.NotRequired[ValueTypeDescription]
    baseType: typing_extensions.NotRequired[ValueTypeDataTypeDict]


from foundry.v2.core import models as core_models  # noqa: E402

__all__ = [
    "DataValue",
    "ExecuteQueryResponse",
    "ExecuteQueryResponseDict",
    "FunctionRid",
    "FunctionVersion",
    "Parameter",
    "ParameterDict",
    "ParameterId",
    "Query",
    "QueryAggregationKeyType",
    "QueryAggregationKeyTypeDict",
    "QueryAggregationRangeSubType",
    "QueryAggregationRangeSubTypeDict",
    "QueryAggregationRangeType",
    "QueryAggregationRangeTypeDict",
    "QueryAggregationValueType",
    "QueryAggregationValueTypeDict",
    "QueryApiName",
    "QueryArrayType",
    "QueryArrayTypeDict",
    "QueryDataType",
    "QueryDataTypeDict",
    "QueryDict",
    "QueryRuntimeErrorParameter",
    "QuerySetType",
    "QuerySetTypeDict",
    "QueryStructField",
    "QueryStructFieldDict",
    "QueryStructType",
    "QueryStructTypeDict",
    "QueryUnionType",
    "QueryUnionTypeDict",
    "StructFieldName",
    "ThreeDimensionalAggregation",
    "ThreeDimensionalAggregationDict",
    "TwoDimensionalAggregation",
    "TwoDimensionalAggregationDict",
    "ValueType",
    "ValueTypeApiName",
    "ValueTypeDataType",
    "ValueTypeDataTypeArrayType",
    "ValueTypeDataTypeArrayTypeDict",
    "ValueTypeDataTypeBinaryType",
    "ValueTypeDataTypeBinaryTypeDict",
    "ValueTypeDataTypeBooleanType",
    "ValueTypeDataTypeBooleanTypeDict",
    "ValueTypeDataTypeByteType",
    "ValueTypeDataTypeByteTypeDict",
    "ValueTypeDataTypeDateType",
    "ValueTypeDataTypeDateTypeDict",
    "ValueTypeDataTypeDecimalType",
    "ValueTypeDataTypeDecimalTypeDict",
    "ValueTypeDataTypeDict",
    "ValueTypeDataTypeDoubleType",
    "ValueTypeDataTypeDoubleTypeDict",
    "ValueTypeDataTypeFloatType",
    "ValueTypeDataTypeFloatTypeDict",
    "ValueTypeDataTypeIntegerType",
    "ValueTypeDataTypeIntegerTypeDict",
    "ValueTypeDataTypeLongType",
    "ValueTypeDataTypeLongTypeDict",
    "ValueTypeDataTypeMapType",
    "ValueTypeDataTypeMapTypeDict",
    "ValueTypeDataTypeOptionalType",
    "ValueTypeDataTypeOptionalTypeDict",
    "ValueTypeDataTypeShortType",
    "ValueTypeDataTypeShortTypeDict",
    "ValueTypeDataTypeStringType",
    "ValueTypeDataTypeStringTypeDict",
    "ValueTypeDataTypeStructElement",
    "ValueTypeDataTypeStructElementDict",
    "ValueTypeDataTypeStructFieldIdentifier",
    "ValueTypeDataTypeStructType",
    "ValueTypeDataTypeStructTypeDict",
    "ValueTypeDataTypeTimestampType",
    "ValueTypeDataTypeTimestampTypeDict",
    "ValueTypeDataTypeUnionType",
    "ValueTypeDataTypeUnionTypeDict",
    "ValueTypeDataTypeValueTypeReference",
    "ValueTypeDataTypeValueTypeReferenceDict",
    "ValueTypeDescription",
    "ValueTypeDict",
    "ValueTypeReference",
    "ValueTypeReferenceDict",
    "ValueTypeRid",
    "ValueTypeVersion",
    "ValueTypeVersionId",
    "VersionId",
    "VersionIdDict",
]
