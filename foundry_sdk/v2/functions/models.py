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


class ArrayConstraint(core.ModelBase):
    """ArrayConstraint"""

    minimum_size: typing.Optional[int] = pydantic.Field(alias=str("minimumSize"), default=None)  # type: ignore[literal-required]
    maximum_size: typing.Optional[int] = pydantic.Field(alias=str("maximumSize"), default=None)  # type: ignore[literal-required]
    unique_values: bool = pydantic.Field(alias=str("uniqueValues"))  # type: ignore[literal-required]
    value_constraint: typing.Optional[ValueTypeConstraint] = pydantic.Field(alias=str("valueConstraint"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"


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


class EnumConstraint(core.ModelBase):
    """EnumConstraint"""

    options: typing.List[typing.Any]
    type: typing.Literal["enum"] = "enum"


class ExecuteQueryResponse(core.ModelBase):
    """ExecuteQueryResponse"""

    value: DataValue


FunctionRid = core.RID
"""The unique resource identifier of a Function, useful for interacting with other Foundry APIs."""


FunctionVersion = str
"""
The version of the given Function, written `<major>.<minor>.<patch>-<tag>`, where `-<tag>` is optional.
Examples: `1.2.3`, `1.2.3-rc1`.
"""


class LengthConstraint(core.ModelBase):
    """LengthConstraint"""

    minimum_length: typing.Optional[int] = pydantic.Field(alias=str("minimumLength"), default=None)  # type: ignore[literal-required]
    maximum_length: typing.Optional[int] = pydantic.Field(alias=str("maximumLength"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["length"] = "length"


class MapConstraint(core.ModelBase):
    """MapConstraint"""

    key_constraints: typing.List[ValueTypeConstraint] = pydantic.Field(alias=str("keyConstraints"))  # type: ignore[literal-required]
    value_constraints: typing.List[ValueTypeConstraint] = pydantic.Field(alias=str("valueConstraints"))  # type: ignore[literal-required]
    unique_values: bool = pydantic.Field(alias=str("uniqueValues"))  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"


class NullableConstraint(core.ModelBase):
    """NullableConstraint"""

    value: NullableConstraintValue
    type: typing.Literal["nullable"] = "nullable"


NullableConstraintValue = typing.Literal["NULLABLE", "NOT_NULLABLE"]
"""NullableConstraintValue"""


class Parameter(core.ModelBase):
    """Details about a parameter of a query."""

    description: typing.Optional[str] = None
    data_type: QueryDataType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]


ParameterId = str
"""
The unique identifier of the parameter. Parameters are used as inputs when an action or query is applied.
Parameters can be viewed and managed in the **Ontology Manager**.
"""


class Query(core.ModelBase):
    """Query"""

    api_name: QueryApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, Parameter]
    output: QueryDataType
    rid: FunctionRid
    version: FunctionVersion


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


class QueryAggregationRangeType(core.ModelBase):
    """QueryAggregationRangeType"""

    sub_type: QueryAggregationRangeSubType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["range"] = "range"


QueryAggregationValueType = typing_extensions.Annotated[
    typing.Union[core_models.DateType, core_models.DoubleType, core_models.TimestampType],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by query aggregation keys."""


QueryApiName = str
"""The name of the Query in the API."""


class QueryArrayType(core.ModelBase):
    """QueryArrayType"""

    sub_type: QueryDataType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"


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


class QuerySetType(core.ModelBase):
    """QuerySetType"""

    sub_type: QueryDataType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["set"] = "set"


class QueryStructField(core.ModelBase):
    """QueryStructField"""

    name: StructFieldName
    field_type: QueryDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]


class QueryStructType(core.ModelBase):
    """QueryStructType"""

    fields: typing.List[QueryStructField]
    type: typing.Literal["struct"] = "struct"


class QueryUnionType(core.ModelBase):
    """QueryUnionType"""

    union_types: typing.List[QueryDataType] = pydantic.Field(alias=str("unionTypes"))  # type: ignore[literal-required]
    type: typing.Literal["union"] = "union"


class RangesConstraint(core.ModelBase):
    """RangesConstraint"""

    minimum_value: typing.Optional[typing.Any] = pydantic.Field(alias=str("minimumValue"), default=None)  # type: ignore[literal-required]
    maximum_value: typing.Optional[typing.Any] = pydantic.Field(alias=str("maximumValue"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["range"] = "range"


class RegexConstraint(core.ModelBase):
    """RegexConstraint"""

    pattern: str
    partial_match: bool = pydantic.Field(alias=str("partialMatch"))  # type: ignore[literal-required]
    type: typing.Literal["regex"] = "regex"


class RidConstraint(core.ModelBase):
    """RidConstraint"""

    type: typing.Literal["rid"] = "rid"


class StructConstraint(core.ModelBase):
    """StructConstraint"""

    fields: typing.Dict[StructFieldApiName, ValueTypeApiName]
    type: typing.Literal["struct"] = "struct"


StructFieldApiName = str
"""StructFieldApiName"""


StructFieldName = str
"""The name of a field in a `Struct`."""


class StructV1Constraint(core.ModelBase):
    """StructV1Constraint"""

    fields: typing.Dict[StructFieldApiName, ValueTypeConstraint]
    type: typing.Literal["structV1"] = "structV1"


class ThreeDimensionalAggregation(core.ModelBase):
    """ThreeDimensionalAggregation"""

    key_type: QueryAggregationKeyType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: TwoDimensionalAggregation = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["threeDimensionalAggregation"] = "threeDimensionalAggregation"


class TwoDimensionalAggregation(core.ModelBase):
    """TwoDimensionalAggregation"""

    key_type: QueryAggregationKeyType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: QueryAggregationValueType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["twoDimensionalAggregation"] = "twoDimensionalAggregation"


class UuidConstraint(core.ModelBase):
    """UuidConstraint"""

    type: typing.Literal["uuid"] = "uuid"


class ValueType(core.ModelBase):
    """ValueType"""

    rid: ValueTypeRid
    version: ValueTypeVersion
    version_id: ValueTypeVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    api_name: ValueTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[ValueTypeDescription] = None
    base_type: typing.Optional[ValueTypeDataType] = pydantic.Field(alias=str("baseType"), default=None)  # type: ignore[literal-required]
    constraints: typing.List[ValueTypeConstraint]


ValueTypeApiName = str
"""The registered API name for the value type."""


ValueTypeConstraint = typing_extensions.Annotated[
    typing.Union[
        StructConstraint,
        StructV1Constraint,
        RegexConstraint,
        NullableConstraint,
        ArrayConstraint,
        LengthConstraint,
        RangesConstraint,
        RidConstraint,
        MapConstraint,
        UuidConstraint,
        EnumConstraint,
    ],
    pydantic.Field(discriminator="type"),
]
"""ValueTypeConstraint"""


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


class ValueTypeDataTypeArrayType(core.ModelBase):
    """ValueTypeDataTypeArrayType"""

    sub_type: ValueTypeDataType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"


class ValueTypeDataTypeBinaryType(core.ModelBase):
    """ValueTypeDataTypeBinaryType"""

    type: typing.Literal["binary"] = "binary"


class ValueTypeDataTypeBooleanType(core.ModelBase):
    """ValueTypeDataTypeBooleanType"""

    type: typing.Literal["boolean"] = "boolean"


class ValueTypeDataTypeByteType(core.ModelBase):
    """ValueTypeDataTypeByteType"""

    type: typing.Literal["byte"] = "byte"


class ValueTypeDataTypeDateType(core.ModelBase):
    """ValueTypeDataTypeDateType"""

    type: typing.Literal["date"] = "date"


class ValueTypeDataTypeDecimalType(core.ModelBase):
    """ValueTypeDataTypeDecimalType"""

    type: typing.Literal["decimal"] = "decimal"


class ValueTypeDataTypeDoubleType(core.ModelBase):
    """ValueTypeDataTypeDoubleType"""

    type: typing.Literal["double"] = "double"


class ValueTypeDataTypeFloatType(core.ModelBase):
    """ValueTypeDataTypeFloatType"""

    type: typing.Literal["float"] = "float"


class ValueTypeDataTypeIntegerType(core.ModelBase):
    """ValueTypeDataTypeIntegerType"""

    type: typing.Literal["integer"] = "integer"


class ValueTypeDataTypeLongType(core.ModelBase):
    """ValueTypeDataTypeLongType"""

    type: typing.Literal["long"] = "long"


class ValueTypeDataTypeMapType(core.ModelBase):
    """ValueTypeDataTypeMapType"""

    key_type: ValueTypeDataType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: ValueTypeDataType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"


class ValueTypeDataTypeOptionalType(core.ModelBase):
    """ValueTypeDataTypeOptionalType"""

    wrapped_type: ValueTypeDataType = pydantic.Field(alias=str("wrappedType"))  # type: ignore[literal-required]
    type: typing.Literal["optional"] = "optional"


class ValueTypeDataTypeShortType(core.ModelBase):
    """ValueTypeDataTypeShortType"""

    type: typing.Literal["short"] = "short"


class ValueTypeDataTypeStringType(core.ModelBase):
    """ValueTypeDataTypeStringType"""

    type: typing.Literal["string"] = "string"


class ValueTypeDataTypeStructElement(core.ModelBase):
    """ValueTypeDataTypeStructElement"""

    name: ValueTypeDataTypeStructFieldIdentifier
    field_type: ValueTypeDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]


ValueTypeDataTypeStructFieldIdentifier = str
"""ValueTypeDataTypeStructFieldIdentifier"""


class ValueTypeDataTypeStructType(core.ModelBase):
    """ValueTypeDataTypeStructType"""

    fields: typing.List[ValueTypeDataTypeStructElement]
    type: typing.Literal["struct"] = "struct"


class ValueTypeDataTypeTimestampType(core.ModelBase):
    """ValueTypeDataTypeTimestampType"""

    type: typing.Literal["timestamp"] = "timestamp"


class ValueTypeDataTypeUnionType(core.ModelBase):
    """ValueTypeDataTypeUnionType"""

    member_types: typing.List[ValueTypeDataType] = pydantic.Field(alias=str("memberTypes"))  # type: ignore[literal-required]
    type: typing.Literal["union"] = "union"


class ValueTypeDataTypeValueTypeReference(core.ModelBase):
    """ValueTypeDataTypeValueTypeReference"""

    rid: ValueTypeRid
    version_id: ValueTypeVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    type: typing.Literal["valueTypeReference"] = "valueTypeReference"


ValueTypeDescription = str
"""A description of the value type."""


class ValueTypeReference(core.ModelBase):
    """A reference to a value type that has been registered in the Ontology."""

    rid: ValueTypeRid
    version_id: ValueTypeVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    type: typing.Literal["valueTypeReference"] = "valueTypeReference"


ValueTypeRid = core.RID
"""The RID of a value type that has been registered in the Ontology."""


ValueTypeVersion = str
"""The version of a value type that has been registered in the Ontology."""


ValueTypeVersionId = core.UUID
"""The version ID of a value type that has been registered in the Ontology."""


class VersionId(core.ModelBase):
    """VersionId"""

    rid: ValueTypeRid
    version: ValueTypeVersion
    version_id: ValueTypeVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    api_name: ValueTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[ValueTypeDescription] = None
    base_type: typing.Optional[ValueTypeDataType] = pydantic.Field(alias=str("baseType"), default=None)  # type: ignore[literal-required]
    constraints: typing.List[ValueTypeConstraint]


core.resolve_forward_references(QueryAggregationKeyType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryAggregationRangeSubType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryAggregationValueType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryDataType, globalns=globals(), localns=locals())
core.resolve_forward_references(ValueTypeConstraint, globalns=globals(), localns=locals())
core.resolve_forward_references(ValueTypeDataType, globalns=globals(), localns=locals())

__all__ = [
    "ArrayConstraint",
    "DataValue",
    "EnumConstraint",
    "ExecuteQueryResponse",
    "FunctionRid",
    "FunctionVersion",
    "LengthConstraint",
    "MapConstraint",
    "NullableConstraint",
    "NullableConstraintValue",
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
    "RangesConstraint",
    "RegexConstraint",
    "RidConstraint",
    "StructConstraint",
    "StructFieldApiName",
    "StructFieldName",
    "StructV1Constraint",
    "ThreeDimensionalAggregation",
    "TwoDimensionalAggregation",
    "UuidConstraint",
    "ValueType",
    "ValueTypeApiName",
    "ValueTypeConstraint",
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
