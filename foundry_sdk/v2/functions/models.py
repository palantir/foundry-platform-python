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

from foundry_sdk import _core as core
from foundry_sdk.v2.core import models as core_models

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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


QueryAggregationKeyType = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        core_models.BooleanType,
        core_models.StringType,
        core_models.DoubleType,
        "QueryAggregationRangeType",
        core_models.IntegerType,
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by query aggregation keys."""


QueryAggregationRangeSubType = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        core_models.DoubleType,
        core_models.IntegerType,
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by query aggregation ranges."""


class QueryAggregationRangeType(pydantic.BaseModel):
    """QueryAggregationRangeType"""

    sub_type: QueryAggregationRangeSubType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["range"] = "range"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


QueryAggregationValueType = typing_extensions.Annotated[
    typing.Union[core_models.DateType, core_models.DoubleType, core_models.TimestampType],
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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


QueryDataType = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "QueryStructType",
        "QuerySetType",
        core_models.StringType,
        core_models.DoubleType,
        core_models.IntegerType,
        "ThreeDimensionalAggregation",
        "QueryUnionType",
        core_models.FloatType,
        core_models.LongType,
        core_models.BooleanType,
        core_models.UnsupportedType,
        core_models.AttachmentType,
        core_models.NullType,
        QueryArrayType,
        "TwoDimensionalAggregation",
        "ValueTypeReference",
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Query parameters or outputs."""


QueryRuntimeErrorParameter = str
"""QueryRuntimeErrorParameter"""


class QuerySetType(pydantic.BaseModel):
    """QuerySetType"""

    sub_type: QueryDataType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["set"] = "set"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class QueryStructField(pydantic.BaseModel):
    """QueryStructField"""

    name: StructFieldName
    field_type: QueryDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class QueryStructType(pydantic.BaseModel):
    """QueryStructType"""

    fields: typing.List[QueryStructField]
    type: typing.Literal["struct"] = "struct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class QueryUnionType(pydantic.BaseModel):
    """QueryUnionType"""

    union_types: typing.List[QueryDataType] = pydantic.Field(alias=str("unionTypes"))  # type: ignore[literal-required]
    type: typing.Literal["union"] = "union"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


StructFieldName = str
"""The name of a field in a `Struct`."""


class ThreeDimensionalAggregation(pydantic.BaseModel):
    """ThreeDimensionalAggregation"""

    key_type: QueryAggregationKeyType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: TwoDimensionalAggregation = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["threeDimensionalAggregation"] = "threeDimensionalAggregation"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class TwoDimensionalAggregation(pydantic.BaseModel):
    """TwoDimensionalAggregation"""

    key_type: QueryAggregationKeyType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: QueryAggregationValueType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["twoDimensionalAggregation"] = "twoDimensionalAggregation"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeBinaryType(pydantic.BaseModel):
    """ValueTypeDataTypeBinaryType"""

    type: typing.Literal["binary"] = "binary"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeBooleanType(pydantic.BaseModel):
    """ValueTypeDataTypeBooleanType"""

    type: typing.Literal["boolean"] = "boolean"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeByteType(pydantic.BaseModel):
    """ValueTypeDataTypeByteType"""

    type: typing.Literal["byte"] = "byte"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeDateType(pydantic.BaseModel):
    """ValueTypeDataTypeDateType"""

    type: typing.Literal["date"] = "date"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeDecimalType(pydantic.BaseModel):
    """ValueTypeDataTypeDecimalType"""

    type: typing.Literal["decimal"] = "decimal"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeDoubleType(pydantic.BaseModel):
    """ValueTypeDataTypeDoubleType"""

    type: typing.Literal["double"] = "double"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeFloatType(pydantic.BaseModel):
    """ValueTypeDataTypeFloatType"""

    type: typing.Literal["float"] = "float"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeIntegerType(pydantic.BaseModel):
    """ValueTypeDataTypeIntegerType"""

    type: typing.Literal["integer"] = "integer"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeLongType(pydantic.BaseModel):
    """ValueTypeDataTypeLongType"""

    type: typing.Literal["long"] = "long"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeMapType(pydantic.BaseModel):
    """ValueTypeDataTypeMapType"""

    key_type: ValueTypeDataType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: ValueTypeDataType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeOptionalType(pydantic.BaseModel):
    """ValueTypeDataTypeOptionalType"""

    wrapped_type: ValueTypeDataType = pydantic.Field(alias=str("wrappedType"))  # type: ignore[literal-required]
    type: typing.Literal["optional"] = "optional"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeShortType(pydantic.BaseModel):
    """ValueTypeDataTypeShortType"""

    type: typing.Literal["short"] = "short"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeStringType(pydantic.BaseModel):
    """ValueTypeDataTypeStringType"""

    type: typing.Literal["string"] = "string"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeStructElement(pydantic.BaseModel):
    """ValueTypeDataTypeStructElement"""

    name: ValueTypeDataTypeStructFieldIdentifier
    field_type: ValueTypeDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ValueTypeDataTypeStructFieldIdentifier = str
"""ValueTypeDataTypeStructFieldIdentifier"""


class ValueTypeDataTypeStructType(pydantic.BaseModel):
    """ValueTypeDataTypeStructType"""

    fields: typing.List[ValueTypeDataTypeStructElement]
    type: typing.Literal["struct"] = "struct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeTimestampType(pydantic.BaseModel):
    """ValueTypeDataTypeTimestampType"""

    type: typing.Literal["timestamp"] = "timestamp"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeUnionType(pydantic.BaseModel):
    """ValueTypeDataTypeUnionType"""

    member_types: typing.List[ValueTypeDataType] = pydantic.Field(alias=str("memberTypes"))  # type: ignore[literal-required]
    type: typing.Literal["union"] = "union"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValueTypeDataTypeValueTypeReference(pydantic.BaseModel):
    """ValueTypeDataTypeValueTypeReference"""

    rid: ValueTypeRid
    version_id: ValueTypeVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    type: typing.Literal["valueTypeReference"] = "valueTypeReference"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ValueTypeDescription = str
"""A description of the value type."""


class ValueTypeReference(pydantic.BaseModel):
    """A reference to a value type that has been registered in the Ontology."""

    rid: ValueTypeRid
    version_id: ValueTypeVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    type: typing.Literal["valueTypeReference"] = "valueTypeReference"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


core.resolve_forward_references(QueryAggregationKeyType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryAggregationRangeSubType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryAggregationValueType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryDataType, globalns=globals(), localns=locals())
core.resolve_forward_references(ValueTypeDataType, globalns=globals(), localns=locals())

__all__ = [
    "DataValue",
    "ExecuteQueryResponse",
    "FunctionRid",
    "FunctionVersion",
    "Parameter",
    "ParameterId",
    "Query",
    "QueryAggregationKeyType",
    "QueryAggregationRangeSubType",
    "QueryAggregationRangeType",
    "QueryAggregationValueType",
    "QueryApiName",
    "QueryArrayType",
    "QueryDataType",
    "QueryRuntimeErrorParameter",
    "QuerySetType",
    "QueryStructField",
    "QueryStructType",
    "QueryUnionType",
    "StructFieldName",
    "ThreeDimensionalAggregation",
    "TwoDimensionalAggregation",
    "ValueType",
    "ValueTypeApiName",
    "ValueTypeDataType",
    "ValueTypeDataTypeArrayType",
    "ValueTypeDataTypeBinaryType",
    "ValueTypeDataTypeBooleanType",
    "ValueTypeDataTypeByteType",
    "ValueTypeDataTypeDateType",
    "ValueTypeDataTypeDecimalType",
    "ValueTypeDataTypeDoubleType",
    "ValueTypeDataTypeFloatType",
    "ValueTypeDataTypeIntegerType",
    "ValueTypeDataTypeLongType",
    "ValueTypeDataTypeMapType",
    "ValueTypeDataTypeOptionalType",
    "ValueTypeDataTypeShortType",
    "ValueTypeDataTypeStringType",
    "ValueTypeDataTypeStructElement",
    "ValueTypeDataTypeStructFieldIdentifier",
    "ValueTypeDataTypeStructType",
    "ValueTypeDataTypeTimestampType",
    "ValueTypeDataTypeUnionType",
    "ValueTypeDataTypeValueTypeReference",
    "ValueTypeDescription",
    "ValueTypeReference",
    "ValueTypeRid",
    "ValueTypeVersion",
    "ValueTypeVersionId",
    "VersionId",
]
