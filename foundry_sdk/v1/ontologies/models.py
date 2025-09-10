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
from foundry_sdk.v1.core import models as core_models

ActionRid = core.RID
"""The unique resource identifier for an action."""


class ActionType(core.ModelBase):
    """Represents an action type in the Ontology."""

    api_name: ActionTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    parameters: typing.Dict[ParameterId, Parameter]
    rid: ActionTypeRid
    operations: typing.List[LogicRule]


ActionTypeApiName = str
"""
The name of the action type in the API. To find the API name for your Action Type, use the `List action types`
endpoint or check the **Ontology Manager**.
"""


ActionTypeRid = core.RID
"""The unique resource identifier of an action type, useful for interacting with other Foundry APIs."""


class AggregateObjectsResponse(core.ModelBase):
    """AggregateObjectsResponse"""

    excluded_items: typing.Optional[int] = pydantic.Field(alias=str("excludedItems"), default=None)  # type: ignore[literal-required]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[AggregateObjectsResponseItem]


class AggregateObjectsResponseItem(core.ModelBase):
    """AggregateObjectsResponseItem"""

    group: typing.Dict[AggregationGroupKey, AggregationGroupValue]
    metrics: typing.List[AggregationMetricResult]


Aggregation = typing_extensions.Annotated[
    typing.Union[
        "ApproximateDistinctAggregation",
        "MinAggregation",
        "AvgAggregation",
        "MaxAggregation",
        "CountAggregation",
        "SumAggregation",
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies an aggregation function."""


class AggregationDurationGrouping(core.ModelBase):
    """
    Divides objects into groups according to an interval. Note that this grouping applies only on date types.
    The interval uses the ISO 8601 notation. For example, "PT1H2M34S" represents a duration of 3754 seconds.
    """

    field: FieldNameV1
    duration: Duration
    type: typing.Literal["duration"] = "duration"


class AggregationExactGrouping(core.ModelBase):
    """Divides objects into groups according to an exact value."""

    field: FieldNameV1
    max_group_count: typing.Optional[int] = pydantic.Field(alias=str("maxGroupCount"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["exact"] = "exact"


class AggregationFixedWidthGrouping(core.ModelBase):
    """Divides objects into groups with the specified width."""

    field: FieldNameV1
    fixed_width: int = pydantic.Field(alias=str("fixedWidth"))  # type: ignore[literal-required]
    type: typing.Literal["fixedWidth"] = "fixedWidth"


AggregationGroupBy = typing_extensions.Annotated[
    typing.Union[
        AggregationDurationGrouping,
        AggregationFixedWidthGrouping,
        "AggregationRangesGrouping",
        AggregationExactGrouping,
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies a grouping for aggregation results."""


AggregationGroupKey = str
"""AggregationGroupKey"""


AggregationGroupValue = typing.Any
"""AggregationGroupValue"""


AggregationMetricName = str
"""A user-specified alias for an aggregation metric name."""


class AggregationMetricResult(core.ModelBase):
    """AggregationMetricResult"""

    name: str
    value: typing.Optional[float] = None
    """TBD"""


class AggregationRange(core.ModelBase):
    """Specifies a date range from an inclusive start date to an exclusive end date."""

    lt: typing.Optional[typing.Any] = None
    """Exclusive end date."""

    lte: typing.Optional[typing.Any] = None
    """Inclusive end date."""

    gt: typing.Optional[typing.Any] = None
    """Exclusive start date."""

    gte: typing.Optional[typing.Any] = None
    """Inclusive start date."""


class AggregationRangesGrouping(core.ModelBase):
    """Divides objects into groups according to specified ranges."""

    field: FieldNameV1
    ranges: typing.List[AggregationRange]
    type: typing.Literal["ranges"] = "ranges"


class AllTermsQuery(core.ModelBase):
    """
    Returns objects where the specified field contains all of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching.
    """

    field: FieldNameV1
    value: str
    fuzzy: typing.Optional[Fuzzy] = None
    type: typing.Literal["allTerms"] = "allTerms"


class AndQuery(core.ModelBase):
    """Returns objects where every query is satisfied."""

    value: typing.List[SearchJsonQuery]
    type: typing.Literal["and"] = "and"


class AnyTermQuery(core.ModelBase):
    """
    Returns objects where the specified field contains any of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching.
    """

    field: FieldNameV1
    value: str
    fuzzy: typing.Optional[Fuzzy] = None
    type: typing.Literal["anyTerm"] = "anyTerm"


ApplyActionMode = typing.Literal["VALIDATE_ONLY", "VALIDATE_AND_EXECUTE"]
"""ApplyActionMode"""


class ApplyActionRequest(core.ModelBase):
    """ApplyActionRequest"""

    parameters: typing.Dict[ParameterId, typing.Optional[DataValue]]


class ApplyActionRequestOptions(core.ModelBase):
    """ApplyActionRequestOptions"""

    mode: typing.Optional[ApplyActionMode] = None
    return_edits: typing.Optional[ReturnEditsMode] = pydantic.Field(alias=str("returnEdits"), default=None)  # type: ignore[literal-required]


class ApplyActionResponse(core.ModelBase):
    """ApplyActionResponse"""


class ApproximateDistinctAggregation(core.ModelBase):
    """Computes an approximate number of distinct values for the provided field."""

    field: FieldNameV1
    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["approximateDistinct"] = "approximateDistinct"


class ArrayEvaluatedConstraint(core.ModelBase):
    """Evaluated constraints of array parameters that support per-entry constraint evaluations."""

    entries: typing.List[ArrayEntryEvaluatedConstraint]
    type: typing.Literal["array"] = "array"


class ArraySizeConstraint(core.ModelBase):
    """The parameter expects an array of values and the size of the array must fall within the defined range."""

    lt: typing.Optional[typing.Any] = None
    """Less than"""

    lte: typing.Optional[typing.Any] = None
    """Less than or equal"""

    gt: typing.Optional[typing.Any] = None
    """Greater than"""

    gte: typing.Optional[typing.Any] = None
    """Greater than or equal"""

    type: typing.Literal["arraySize"] = "arraySize"


ArtifactRepositoryRid = core.RID
"""ArtifactRepositoryRid"""


class Attachment(core.ModelBase):
    """The representation of an attachment."""

    rid: AttachmentRid
    filename: core_models.Filename
    size_bytes: core_models.SizeBytes = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    media_type: core_models.MediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]


AttachmentRid = core.RID
"""The unique resource identifier of an attachment."""


class AvgAggregation(core.ModelBase):
    """Computes the average value for the provided field."""

    field: FieldNameV1
    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["avg"] = "avg"


class BatchApplyActionResponse(core.ModelBase):
    """BatchApplyActionResponse"""


class ContainsQuery(core.ModelBase):
    """Returns objects where the specified array contains a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["contains"] = "contains"


class CountAggregation(core.ModelBase):
    """Computes the total count of objects."""

    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["count"] = "count"


class CreateInterfaceObjectRule(core.ModelBase):
    """CreateInterfaceObjectRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["createInterfaceObject"] = "createInterfaceObject"


class CreateLinkRule(core.ModelBase):
    """CreateLinkRule"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("aSideObjectTypeApiName"))  # type: ignore[literal-required]
    b_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("bSideObjectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["createLink"] = "createLink"


class CreateObjectRule(core.ModelBase):
    """CreateObjectRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["createObject"] = "createObject"


DataValue = typing.Any
"""
Represents the value of data in the following format. Note that these values can be nested, for example an array of structs.
| Type                                | JSON encoding                                         | Example                                                                                                                                                       |
|-------------------------------------|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Array                               | array                                                 | `["alpha", "bravo", "charlie"]`                                                                                                                               |
| Attachment                          | string                                                | `"ri.attachments.main.attachment.2f944bae-5851-4204-8615-920c969a9f2e"`                                                                                       |
| Boolean                             | boolean                                               | `true`                                                                                                                                                        |
| Byte                                | number                                                | `31`                                                                                                                                                          |
| CipherText                          | string                                                | `"CIPHER::ri.bellaso.main.cipher-channel.e414ab9e-b606-499a-a0e1-844fa296ba7e::unzjs3VifsTxuIpf1fH1CJ7OaPBr2bzMMdozPaZJtCii8vVG60yXIEmzoOJaEl9mfFFe::CIPHER"` |
| Date                                | ISO 8601 extended local date string                   | `"2021-05-01"`                                                                                                                                                |
| Decimal                             | string                                                | `"2.718281828"`                                                                                                                                               |
| Double                              | number                                                | `3.14159265`                                                                                                                                                  |
| EntrySet                            | array of JSON objects                                 | `[{"key": "EMP1234", "value": "true"}, {"key": "EMP4444", "value": "false"}]`                                                                                 |
| Float                               | number                                                | `3.14159265`                                                                                                                                                  |
| Integer                             | number                                                | `238940`                                                                                                                                                      |
| Long                                | string                                                | `"58319870951433"`                                                                                                                                            |
| Marking                             | string                                                | `"MU"`                                                                                                                                                        |
| Null                                | null                                                  | `null`                                                                                                                                                        |
| Object Set                          | string OR the object set definition                   | `ri.object-set.main.versioned-object-set.h13274m8-23f5-431c-8aee-a4554157c57z`                                                                                |
| Ontology Object Reference           | JSON encoding of the object's primary key             | `10033123` or `"EMP1234"`                                                                                                                                     |
| Ontology Interface Object Reference | JSON encoding of the object's API name and primary key| `{"objectTypeApiName":"Employee", "primaryKeyValue":"EMP1234"}`                                                                                               |
| Ontology Object Type Reference      | string of the object type's api name                  | `"Employee"`                                                                                                                                                  |
| Set                                 | array                                                 | `["alpha", "bravo", "charlie"]`                                                                                                                               |
| Short                               | number                                                | `8739`                                                                                                                                                        |
| String                              | string                                                | `"Call me Ishmael"`                                                                                                                                           |
| Struct                              | JSON object                                           | `{"name": "John Doe", "age": 42}`                                                                                                                             |
| TwoDimensionalAggregation           | JSON object                                           | `{"groups": [{"key": "alpha", "value": 100}, {"key": "beta", "value": 101}]}`                                                                                 |
| ThreeDimensionalAggregation         | JSON object                                           | `{"groups": [{"key": "NYC", "groups": [{"key": "Engineer", "value" : 100}]}]}`                                                                                |
| Timestamp                           | ISO 8601 extended offset date-time string in UTC zone | `"2021-01-04T05:00:00Z"`                                                                                                                                      |
"""


class DeleteInterfaceObjectRule(core.ModelBase):
    """DeleteInterfaceObjectRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteInterfaceObject"] = "deleteInterfaceObject"


class DeleteLinkRule(core.ModelBase):
    """DeleteLinkRule"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("aSideObjectTypeApiName"))  # type: ignore[literal-required]
    b_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("bSideObjectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteLink"] = "deleteLink"


class DeleteObjectRule(core.ModelBase):
    """DeleteObjectRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteObject"] = "deleteObject"


DerivedPropertyApiName = str
"""The name of the derived property that will be returned."""


Duration = str
"""An ISO 8601 formatted duration."""


class EntrySetType(core.ModelBase):
    """EntrySetType"""

    key_type: QueryDataType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: QueryDataType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["entrySet"] = "entrySet"


class EqualsQuery(core.ModelBase):
    """Returns objects where the specified field is equal to a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["eq"] = "eq"


class ExecuteQueryResponse(core.ModelBase):
    """ExecuteQueryResponse"""

    value: DataValue


FieldNameV1 = str
"""A reference to an Ontology object property with the form `properties.{propertyApiName}`."""


FilterValue = str
"""
Represents the value of a property filter. For instance, false is the FilterValue in
`properties.{propertyApiName}.isNull=false`.
"""


FunctionRid = core.RID
"""The unique resource identifier of a Function, useful for interacting with other Foundry APIs."""


FunctionVersion = str
"""
The version of the given Function, written `<major>.<minor>.<patch>-<tag>`, where `-<tag>` is optional.
Examples: `1.2.3`, `1.2.3-rc1`.
"""


Fuzzy = bool
"""Setting fuzzy to `true` allows approximate matching in search queries that support it."""


class GroupMemberConstraint(core.ModelBase):
    """The parameter value must be the user id of a member belonging to at least one of the groups defined by the constraint."""

    type: typing.Literal["groupMember"] = "groupMember"


class GtQuery(core.ModelBase):
    """Returns objects where the specified field is greater than a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["gt"] = "gt"


class GteQuery(core.ModelBase):
    """Returns objects where the specified field is greater than or equal to a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["gte"] = "gte"


InterfaceLinkTypeApiName = str
"""
The name of the interface link type in the API. To find the API name for your Interface Link Type, check the 
[Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
"""


InterfaceLinkTypeRid = core.RID
"""The unique resource identifier of an interface link type, useful for interacting with other Foundry APIs."""


InterfaceTypeApiName = str
"""
The name of the interface type in the API in UpperCamelCase format. To find the API name for your interface
type, use the `List interface types` endpoint or check the **Ontology Manager**.
"""


InterfaceTypeRid = core.RID
"""The unique resource identifier of an interface, useful for interacting with other Foundry APIs."""


class IsNullQuery(core.ModelBase):
    """Returns objects based on the existence of the specified field."""

    field: FieldNameV1
    value: bool
    type: typing.Literal["isNull"] = "isNull"


LegacyObjectTypeId = str
"""
The unique ID of an object type. This is a legacy identifier and is not recommended for use in new applications.
To find the ID for your Object Type, check the **Ontology Manager**.
"""


LegacyPropertyId = str
"""
The unique ID of a property. This is a legacy identifier and is not recommended for use in new applications.
To find the ID for your property, check the **Ontology Manager**.
"""


LinkTypeApiName = str
"""
The name of the link type in the API. To find the API name for your Link Type, check the **Ontology Manager**
application.
"""


LinkTypeId = str
"""The unique ID of a link type. To find the ID for your link type, check the **Ontology Manager** application."""


class LinkTypeSide(core.ModelBase):
    """LinkTypeSide"""

    api_name: LinkTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    cardinality: LinkTypeSideCardinality
    foreign_key_property_api_name: typing.Optional[PropertyApiName] = pydantic.Field(alias=str("foreignKeyPropertyApiName"), default=None)  # type: ignore[literal-required]


LinkTypeSideCardinality = typing.Literal["ONE", "MANY"]
"""LinkTypeSideCardinality"""


class ListActionTypesResponse(core.ModelBase):
    """ListActionTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[ActionType]


class ListLinkedObjectsResponse(core.ModelBase):
    """ListLinkedObjectsResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[OntologyObject]


class ListObjectTypesResponse(core.ModelBase):
    """ListObjectTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[ObjectType]
    """The list of object types in the current page."""


class ListObjectsResponse(core.ModelBase):
    """ListObjectsResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[OntologyObject]
    """The list of objects in the current page."""

    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]


class ListOntologiesResponse(core.ModelBase):
    """ListOntologiesResponse"""

    data: typing.List[Ontology]
    """The list of Ontologies the user has access to."""


class ListOutgoingLinkTypesResponse(core.ModelBase):
    """ListOutgoingLinkTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[LinkTypeSide]
    """The list of link type sides in the current page."""


class ListQueryTypesResponse(core.ModelBase):
    """ListQueryTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[QueryType]


LogicRule = typing_extensions.Annotated[
    typing.Union[
        DeleteInterfaceObjectRule,
        "ModifyInterfaceObjectRule",
        "ModifyObjectRule",
        DeleteObjectRule,
        CreateInterfaceObjectRule,
        DeleteLinkRule,
        CreateObjectRule,
        CreateLinkRule,
    ],
    pydantic.Field(discriminator="type"),
]
"""LogicRule"""


class LtQuery(core.ModelBase):
    """Returns objects where the specified field is less than a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["lt"] = "lt"


class LteQuery(core.ModelBase):
    """Returns objects where the specified field is less than or equal to a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["lte"] = "lte"


class MaxAggregation(core.ModelBase):
    """Computes the maximum value for the provided field."""

    field: FieldNameV1
    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["max"] = "max"


class MinAggregation(core.ModelBase):
    """Computes the minimum value for the provided field."""

    field: FieldNameV1
    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["min"] = "min"


class ModifyInterfaceObjectRule(core.ModelBase):
    """ModifyInterfaceObjectRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["modifyInterfaceObject"] = "modifyInterfaceObject"


class ModifyObjectRule(core.ModelBase):
    """ModifyObjectRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["modifyObject"] = "modifyObject"


class NotQuery(core.ModelBase):
    """Returns objects where the query is not satisfied."""

    value: SearchJsonQuery
    type: typing.Literal["not"] = "not"


class ObjectPropertyValueConstraint(core.ModelBase):
    """The parameter value must be a property value of an object found within an object set."""

    type: typing.Literal["objectPropertyValue"] = "objectPropertyValue"


class ObjectQueryResultConstraint(core.ModelBase):
    """The parameter value must be the primary key of an object found within an object set."""

    type: typing.Literal["objectQueryResult"] = "objectQueryResult"


ObjectRid = core.RID
"""The unique resource identifier of an object, useful for interacting with other Foundry APIs."""


ObjectSetRid = core.RID
"""ObjectSetRid"""


class ObjectType(core.ModelBase):
    """Represents an object type in the Ontology."""

    api_name: ObjectTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    legacy_object_type_id: typing.Optional[LegacyObjectTypeId] = pydantic.Field(alias=str("legacyObjectTypeId"), default=None)  # type: ignore[literal-required]
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    description: typing.Optional[str] = None
    """The description of the object type."""

    visibility: typing.Optional[ObjectTypeVisibility] = None
    primary_key: typing.List[PropertyApiName] = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    """The primary key of the object. This is a list of properties that can be used to uniquely identify the object."""

    properties: typing.Dict[PropertyApiName, Property]
    """A map of the properties of the object type."""

    rid: ObjectTypeRid


ObjectTypeApiName = str
"""
The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the
`List object types` endpoint or check the **Ontology Manager**.
"""


ObjectTypeRid = core.RID
"""The unique resource identifier of an object type, useful for interacting with other Foundry APIs."""


ObjectTypeVisibility = typing.Literal["NORMAL", "PROMINENT", "HIDDEN"]
"""The suggested visibility of the object type."""


class OneOfConstraint(core.ModelBase):
    """The parameter has a manually predefined set of options."""

    options: typing.List[ParameterOption]
    other_values_allowed: bool = pydantic.Field(alias=str("otherValuesAllowed"))  # type: ignore[literal-required]
    """A flag denoting whether custom, user provided values will be considered valid. This is configured via the **Allowed "Other" value** toggle in the **Ontology Manager**."""

    type: typing.Literal["oneOf"] = "oneOf"


class Ontology(core.ModelBase):
    """Metadata about an Ontology."""

    api_name: OntologyApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: str
    rid: OntologyRid


OntologyApiName = str
"""OntologyApiName"""


class OntologyArrayType(core.ModelBase):
    """OntologyArrayType"""

    item_type: OntologyDataType = pydantic.Field(alias=str("itemType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"


OntologyDataType = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "OntologyStructType",
        "OntologySetType",
        core_models.StringType,
        core_models.ByteType,
        core_models.DoubleType,
        core_models.IntegerType,
        core_models.FloatType,
        core_models.AnyType,
        core_models.LongType,
        core_models.BooleanType,
        core_models.CipherTextType,
        core_models.MarkingType,
        core_models.UnsupportedType,
        OntologyArrayType,
        "OntologyObjectSetType",
        core_models.BinaryType,
        core_models.ShortType,
        core_models.DecimalType,
        "OntologyMapType",
        core_models.TimestampType,
        "OntologyObjectType",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the primitive types used by Palantir's Ontology-based products."""


class OntologyInterfaceObjectSetType(core.ModelBase):
    """OntologyInterfaceObjectSetType"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["interfaceObjectSet"] = "interfaceObjectSet"


class OntologyInterfaceObjectType(core.ModelBase):
    """OntologyInterfaceObjectType"""

    interface_type_api_name: typing.Optional[InterfaceTypeApiName] = pydantic.Field(alias=str("interfaceTypeApiName"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["interfaceObject"] = "interfaceObject"


class OntologyMapType(core.ModelBase):
    """OntologyMapType"""

    key_type: OntologyDataType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: OntologyDataType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"


class OntologyObject(core.ModelBase):
    """Represents an object in the Ontology."""

    properties: typing.Dict[PropertyApiName, typing.Optional[PropertyValue]]
    """A map of the property values of the object."""

    rid: ObjectRid


class OntologyObjectSetType(core.ModelBase):
    """OntologyObjectSetType"""

    object_api_name: typing.Optional[ObjectTypeApiName] = pydantic.Field(alias=str("objectApiName"), default=None)  # type: ignore[literal-required]
    object_type_api_name: typing.Optional[ObjectTypeApiName] = pydantic.Field(alias=str("objectTypeApiName"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["objectSet"] = "objectSet"


class OntologyObjectType(core.ModelBase):
    """OntologyObjectType"""

    object_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectApiName"))  # type: ignore[literal-required]
    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["object"] = "object"


OntologyRid = core.RID
"""
The unique Resource Identifier (RID) of the Ontology. To look up your Ontology RID, please use the
`List ontologies` endpoint or check the **Ontology Manager**.
"""


class OntologySetType(core.ModelBase):
    """OntologySetType"""

    item_type: OntologyDataType = pydantic.Field(alias=str("itemType"))  # type: ignore[literal-required]
    type: typing.Literal["set"] = "set"


class OntologyStructField(core.ModelBase):
    """OntologyStructField"""

    name: core_models.StructFieldName
    field_type: OntologyDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    required: bool


class OntologyStructType(core.ModelBase):
    """OntologyStructType"""

    fields: typing.List[OntologyStructField]
    type: typing.Literal["struct"] = "struct"


class OrQuery(core.ModelBase):
    """Returns objects where at least 1 query is satisfied."""

    value: typing.List[SearchJsonQuery]
    type: typing.Literal["or"] = "or"


OrderBy = str
"""
A command representing the list of properties to order by. Properties should be delimited by commas and
prefixed by `p` or `properties`. The format expected format is
`orderBy=properties.{property}:{sortDirection},properties.{property}:{sortDirection}...`

By default, the ordering for a property is ascending, and this can be explicitly specified by appending 
`:asc` (for ascending) or `:desc` (for descending).

Example: use `orderBy=properties.lastName:asc` to order by a single property, 
`orderBy=properties.lastName,properties.firstName,properties.age:desc` to order by multiple properties. 
You may also use the shorthand `p` instead of `properties` such as `orderBy=p.lastName:asc`.
"""


class Parameter(core.ModelBase):
    """Details about a parameter of an action or query."""

    description: typing.Optional[str] = None
    base_type: ValueType = pydantic.Field(alias=str("baseType"))  # type: ignore[literal-required]
    data_type: typing.Optional[OntologyDataType] = pydantic.Field(alias=str("dataType"), default=None)  # type: ignore[literal-required]
    required: bool


ParameterEvaluatedConstraint = typing_extensions.Annotated[
    typing.Union[
        "StructEvaluatedConstraint",
        OneOfConstraint,
        ArrayEvaluatedConstraint,
        GroupMemberConstraint,
        ObjectPropertyValueConstraint,
        "RangeConstraint",
        ArraySizeConstraint,
        ObjectQueryResultConstraint,
        "StringLengthConstraint",
        "StringRegexMatchConstraint",
        "UnevaluableConstraint",
    ],
    pydantic.Field(discriminator="type"),
]
"""
A constraint that an action parameter value must satisfy in order to be considered valid.
Constraints can be configured on action parameters in the **Ontology Manager**. 
Applicable constraints are determined dynamically based on parameter inputs. 
Parameter values are evaluated against the final set of constraints.

The type of the constraint.
| Type                  | Description                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `arraySize`           | The parameter expects an array of values and the size of the array must fall within the defined range.                                                                                                                          |
| `groupMember`         | The parameter value must be the user id of a member belonging to at least one of the groups defined by the constraint.                                                                                                          |
| `objectPropertyValue` | The parameter value must be a property value of an object found within an object set.                                                                                                                                           |
| `objectQueryResult`   | The parameter value must be the primary key of an object found within an object set.                                                                                                                                            |
| `oneOf`               | The parameter has a manually predefined set of options.                                                                                                                                                                         |
| `range`               | The parameter value must be within the defined range.                                                                                                                                                                           |
| `stringLength`        | The parameter value must have a length within the defined range.                                                                                                                                                                |
| `stringRegexMatch`    | The parameter value must match a predefined regular expression.                                                                                                                                                                 |
| `unevaluable`         | The parameter cannot be evaluated because it depends on another parameter or object set that can't be evaluated. This can happen when a parameter's allowed values are defined by another parameter that is missing or invalid. |
"""


class ParameterEvaluationResult(core.ModelBase):
    """Represents the validity of a parameter against the configured constraints."""

    result: ValidationResult
    evaluated_constraints: typing.List[ParameterEvaluatedConstraint] = pydantic.Field(alias=str("evaluatedConstraints"))  # type: ignore[literal-required]
    required: bool
    """Represents whether the parameter is a required input to the action."""


ParameterId = str
"""
The unique identifier of the parameter. Parameters are used as inputs when an action or query is applied.
Parameters can be viewed and managed in the **Ontology Manager**.
"""


class ParameterOption(core.ModelBase):
    """A possible value for the parameter. This is defined in the **Ontology Manager** by Actions admins."""

    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    value: typing.Optional[typing.Any] = None
    """An allowed configured value for a parameter within an action."""


class PhraseQuery(core.ModelBase):
    """Returns objects where the specified field contains the provided value as a substring."""

    field: FieldNameV1
    value: str
    type: typing.Literal["phrase"] = "phrase"


class PrefixQuery(core.ModelBase):
    """Returns objects where the specified field starts with the provided value."""

    field: FieldNameV1
    value: str
    type: typing.Literal["prefix"] = "prefix"


PrimaryKeyValue = typing.Any
"""Represents the primary key value that is used as a unique identifier for an object."""


class Property(core.ModelBase):
    """Details about some property of an object."""

    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    base_type: ValueType = pydantic.Field(alias=str("baseType"))  # type: ignore[literal-required]
    legacy_property_id: typing.Optional[LegacyPropertyId] = pydantic.Field(alias=str("legacyPropertyId"), default=None)  # type: ignore[literal-required]


PropertyApiName = str
"""
The name of the property in the API. To find the API name for your property, use the `Get object type`
endpoint or check the **Ontology Manager**.
"""


PropertyFilter = str
"""
Represents a filter used on properties.

Endpoints that accept this supports optional parameters that have the form:
`properties.{propertyApiName}.{propertyFilter}={propertyValueEscapedString}` to filter the returned objects.
For instance, you may use `properties.firstName.eq=John` to find objects that contain a property called
"firstName" that has the exact value of "John".

The following are a list of supported property filters:

- `properties.{propertyApiName}.contains` - supported on arrays and can be used to filter array properties
  that have at least one of the provided values. If multiple query parameters are provided, then objects
  that have any of the given values for the specified property will be matched.
- `properties.{propertyApiName}.eq` - used to filter objects that have the exact value for the provided
  property. If multiple query parameters are provided, then objects that have any of the given values
  will be matched. For instance, if the user provides a request by doing
  `?properties.firstName.eq=John&properties.firstName.eq=Anna`, then objects that have a firstName property
  of either John or Anna will be matched. This filter is supported on all property types except Arrays.
- `properties.{propertyApiName}.neq` - used to filter objects that do not have the provided property values.
  Similar to the `eq` filter, if multiple values are provided, then objects that have any of the given values
  will be excluded from the result.
- `properties.{propertyApiName}.lt`, `properties.{propertyApiName}.lte`, `properties.{propertyApiName}.gt`
  `properties.{propertyApiName}.gte` - represent less than, less than or equal to, greater than, and greater
  than or equal to respectively. These are supported on date, timestamp, byte, integer, long, double, decimal.
- `properties.{propertyApiName}.isNull` - used to filter objects where the provided property is (or is not) null.
  This filter is supported on all property types.
"""


PropertyId = str
"""
The immutable ID of a property. Property IDs are only used to identify properties in the **Ontology Manager**
application and assign them API names. In every other case, API names should be used instead of property IDs.
"""


PropertyTypeRid = core.RID
"""PropertyTypeRid"""


PropertyValue = typing.Any
"""
Represents the value of a property in the following format.

| Type                                                                                                                      | JSON encoding                                               | Example                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Array                                                                                                                     | array                                                       | `["alpha", "bravo", "charlie"]`                                                                    |
| [Attachment](https://palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/attachment-property-basics/)              | JSON encoded `AttachmentProperty` object                    | `{"rid":"ri.blobster.main.attachment.2f944bae-5851-4204-8615-920c969a9f2e"}`                       |
| Boolean                                                                                                                   | boolean                                                     | `true`                                                                                             |
| Byte                                                                                                                      | number                                                      | `31`                                                                                               |
| CipherText                                                                                                                | string                                                      | `"CIPHER::ri.bellaso.main.cipher-channel.e414ab9e-b606-499a-a0e1-844fa296ba7e::unzjs3VifsTxuIpf1fH1CJ7OaPBr2bzMMdozPaZJtCii8vVG60yXIEmzoOJaEl9mfFFe::CIPHER"`                                                                                                                                                                                        |        
| Date                                                                                                                      | ISO 8601 extended local date string                         | `"2021-05-01"`                                                                                     |
| Decimal                                                                                                                   | string                                                      | `"2.718281828"`                                                                                    |
| Double                                                                                                                    | number                                                      | `3.14159265`                                                                                       |
| Float                                                                                                                     | number                                                      | `3.14159265`                                                                                       |
| GeoPoint                                                                                                                  | geojson                                                     | `{"type":"Point","coordinates":[102.0,0.5]}`                                                       |
| GeoShape                                                                                                                  | geojson                                                     | `{"type":"LineString","coordinates":[[102.0,0.0],[103.0,1.0],[104.0,0.0],[105.0,1.0]]}`            |
| Integer                                                                                                                   | number                                                      | `238940`                                                                                           |
| Long                                                                                                                      | string                                                      | `"58319870951433"`                                                                                 |
| [MediaReference](https://palantir.com/docs/foundry/api/v2/ontologies-v2-resources/media-reference-properties/media-reference-property-basics/)| JSON encoded `MediaReference` object                        | `{"mimeType":"application/pdf","reference":{"type":"mediaSetViewItem","mediaSetViewItem":{"mediaSetRid":"ri.mio.main.media-set.4153d42f-ca4b-4e42-8ca5-8e6aa7edb642","mediaSetViewRid":"ri.mio.main.view.82a798ad-d637-4595-acc6-987bcf16629b","mediaItemRid":"ri.mio.main.media-item.001ec98b-1620-4814-9e17-8e9c4e536225"}}}`                       |
| Short                                                                                                                     | number                                                      | `8739`                                                                                             |
| String                                                                                                                    | string                                                      | `"Call me Ishmael"`                                                                                |
| Struct                                                                                                                    | JSON object of struct field API name -> value               | {"firstName": "Alex", "lastName": "Karp"}                                                          |
| Timestamp                                                                                                                 | ISO 8601 extended offset date-time string in UTC zone       | `"2021-01-04T05:00:00Z"`                                                                           |
| [Timeseries](https://palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-properties/time-series-property-basics/)            | JSON encoded `TimeseriesProperty` object or seriesId string | `{"seriesId": "wellPressureSeriesId", "syncRid": ri.time-series-catalog.main.sync.04f5ac1f-91bf-44f9-a51f-4f34e06e42df"}` or `{"templateRid": "ri.codex-emu.main.template.367cac64-e53b-4653-b111-f61856a63df9", "templateVersion": "0.0.0"}` or `"wellPressureSeriesId"`|                                                                           |
| Vector                                                                                                                    | array                                                       | `[0.1, 0.3, 0.02, 0.05 , 0.8, 0.4]`                                                                |

Note that for backwards compatibility, the Boolean, Byte, Double, Float, Integer, and Short types can also be encoded as JSON strings.
"""


PropertyValueEscapedString = str
"""Represents the value of a property in string format. This is used in URL parameters."""


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
        OntologyInterfaceObjectType,
        "QueryStructType",
        "QuerySetType",
        core_models.StringType,
        EntrySetType,
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
        OntologyObjectSetType,
        "TwoDimensionalAggregation",
        OntologyInterfaceObjectSetType,
        OntologyObjectType,
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Query parameters or outputs."""


QueryRuntimeErrorParameter = str
"""QueryRuntimeErrorParameter"""


class QuerySetType(core.ModelBase):
    """QuerySetType"""

    sub_type: QueryDataType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["set"] = "set"


class QueryStructField(core.ModelBase):
    """QueryStructField"""

    name: core_models.StructFieldName
    field_type: QueryDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]


class QueryStructType(core.ModelBase):
    """QueryStructType"""

    fields: typing.List[QueryStructField]
    type: typing.Literal["struct"] = "struct"


class QueryType(core.ModelBase):
    """Represents a query type in the Ontology."""

    api_name: QueryApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, Parameter]
    output: typing.Optional[OntologyDataType] = None
    rid: FunctionRid
    version: FunctionVersion


class QueryUnionType(core.ModelBase):
    """QueryUnionType"""

    union_types: typing.List[QueryDataType] = pydantic.Field(alias=str("unionTypes"))  # type: ignore[literal-required]
    type: typing.Literal["union"] = "union"


class RangeConstraint(core.ModelBase):
    """The parameter value must be within the defined range."""

    lt: typing.Optional[typing.Any] = None
    """Less than"""

    lte: typing.Optional[typing.Any] = None
    """Less than or equal"""

    gt: typing.Optional[typing.Any] = None
    """Greater than"""

    gte: typing.Optional[typing.Any] = None
    """Greater than or equal"""

    type: typing.Literal["range"] = "range"


ReturnEditsMode = typing.Literal["ALL", "ALL_V2_WITH_DELETIONS", "NONE"]
"""ReturnEditsMode"""


SdkPackageName = str
"""SdkPackageName"""


SdkPackageRid = core.RID
"""SdkPackageRid"""


SdkVersion = str
"""SdkVersion"""


SearchJsonQuery = typing_extensions.Annotated[
    typing.Union[
        OrQuery,
        PrefixQuery,
        LtQuery,
        AllTermsQuery,
        EqualsQuery,
        GtQuery,
        ContainsQuery,
        NotQuery,
        PhraseQuery,
        AndQuery,
        IsNullQuery,
        GteQuery,
        AnyTermQuery,
        LteQuery,
    ],
    pydantic.Field(discriminator="type"),
]
"""SearchJsonQuery"""


class SearchObjectsResponse(core.ModelBase):
    """SearchObjectsResponse"""

    data: typing.List[OntologyObject]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]


class SearchOrderBy(core.ModelBase):
    """Specifies the ordering of search results by a field and an ordering direction."""

    fields: typing.List[SearchOrdering]


SearchOrderByType = typing.Literal["fields", "relevance"]
"""SearchOrderByType"""


class SearchOrdering(core.ModelBase):
    """SearchOrdering"""

    field: FieldNameV1
    direction: typing.Optional[str] = None
    """Specifies the ordering direction (can be either `asc` or `desc`)"""


SelectedPropertyApiName = str
"""
By default, whenever an object is requested, all of its properties are returned, except for properties of the 
following types:
- Vector

The response can be filtered to only include certain properties using the `properties` query parameter. Note
that ontology object set endpoints refer to this parameter as `select`.

Properties to include can be specified in one of two ways.

- A comma delimited list as the value for the `properties` query parameter
  `properties={property1ApiName},{property2ApiName}`
- Multiple `properties` query parameters.
  `properties={property1ApiName}&properties={property2ApiName}`

The primary key of the object will always be returned even if it wasn't specified in the `properties` values.

Unknown properties specified in the `properties` list will result in a `PropertiesNotFound` error.

To find the API name for your property, use the `Get object type` endpoint or check the **Ontology Manager**.
"""


SharedPropertyTypeApiName = str
"""
The name of the shared property type in the API in lowerCamelCase format. To find the API name for your
shared property type, use the `List shared property types` endpoint or check the **Ontology Manager**.
"""


SharedPropertyTypeRid = core.RID
"""The unique resource identifier of an shared property type, useful for interacting with other Foundry APIs."""


class StringLengthConstraint(core.ModelBase):
    """
    The parameter value must have a length within the defined range.
    *This range is always inclusive.*
    """

    lt: typing.Optional[typing.Any] = None
    """Less than"""

    lte: typing.Optional[typing.Any] = None
    """Less than or equal"""

    gt: typing.Optional[typing.Any] = None
    """Greater than"""

    gte: typing.Optional[typing.Any] = None
    """Greater than or equal"""

    type: typing.Literal["stringLength"] = "stringLength"


class StringRegexMatchConstraint(core.ModelBase):
    """The parameter value must match a predefined regular expression."""

    regex: str
    """The regular expression configured in the **Ontology Manager**."""

    configured_failure_message: typing.Optional[str] = pydantic.Field(alias=str("configuredFailureMessage"), default=None)  # type: ignore[literal-required]
    """
    The message indicating that the regular expression was not matched.
    This is configured per parameter in the **Ontology Manager**.
    """

    type: typing.Literal["stringRegexMatch"] = "stringRegexMatch"


class StructEvaluatedConstraint(core.ModelBase):
    """Represents the validity of a singleton struct parameter."""

    struct_fields: typing.Dict[StructParameterFieldApiName, StructFieldEvaluationResult] = pydantic.Field(alias=str("structFields"))  # type: ignore[literal-required]
    type: typing.Literal["struct"] = "struct"


StructFieldEvaluatedConstraint = typing_extensions.Annotated[
    typing.Union[
        OneOfConstraint, RangeConstraint, StringLengthConstraint, StringRegexMatchConstraint
    ],
    pydantic.Field(discriminator="type"),
]
"""
A constraint that an action struct parameter field value must satisfy in order to be considered valid.
Constraints can be configured on fields of struct parameters in the **Ontology Manager**. 
Applicable constraints are determined dynamically based on parameter inputs. 
Parameter values are evaluated against the final set of constraints.

The type of the constraint.
| Type                  | Description                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `oneOf`               | The struct parameter field has a manually predefined set of options.                                                                                                                                                            |
| `range`               | The struct parameter field value must be within the defined range.                                                                                                                                                              |
| `stringLength`        | The struct parameter field value must have a length within the defined range.                                                                                                                                                   |
| `stringRegexMatch`    | The struct parameter field value must match a predefined regular expression.                                                                                                                                                    |
"""


class StructFieldEvaluationResult(core.ModelBase):
    """Represents the validity of a struct parameter's fields against the configured constraints."""

    result: ValidationResult
    evaluated_constraints: typing.List[StructFieldEvaluatedConstraint] = pydantic.Field(alias=str("evaluatedConstraints"))  # type: ignore[literal-required]
    required: bool
    """Represents whether the parameter is a required input to the action."""


StructParameterFieldApiName = str
"""The unique identifier of the struct parameter field."""


class SubmissionCriteriaEvaluation(core.ModelBase):
    """
    Contains the status of the **submission criteria**.
    **Submission criteria** are the prerequisites that need to be satisfied before an Action can be applied.
    These are configured in the **Ontology Manager**.
    """

    configured_failure_message: typing.Optional[str] = pydantic.Field(alias=str("configuredFailureMessage"), default=None)  # type: ignore[literal-required]
    """
    The message indicating one of the **submission criteria** was not satisfied.
    This is configured per **submission criteria** in the **Ontology Manager**.
    """

    result: ValidationResult


class SumAggregation(core.ModelBase):
    """Computes the sum of values for the provided field."""

    field: FieldNameV1
    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["sum"] = "sum"


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


class UnevaluableConstraint(core.ModelBase):
    """
    The parameter cannot be evaluated because it depends on another parameter or object set that can't be evaluated.
    This can happen when a parameter's allowed values are defined by another parameter that is missing or invalid.
    """

    type: typing.Literal["unevaluable"] = "unevaluable"


class ValidateActionResponse(core.ModelBase):
    """ValidateActionResponse"""

    result: ValidationResult
    submission_criteria: typing.List[SubmissionCriteriaEvaluation] = pydantic.Field(alias=str("submissionCriteria"))  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, ParameterEvaluationResult]


ValidationResult = typing.Literal["VALID", "INVALID"]
"""Represents the state of a validation."""


ValueType = str
"""
A string indicating the type of each data value. Note that these types can be nested, for example an array of
structs.

| Type                | JSON value                                                                                                        |
|---------------------|-------------------------------------------------------------------------------------------------------------------|
| Array               | `Array<T>`, where `T` is the type of the array elements, e.g. `Array<String>`.                                    |
| Attachment          | `Attachment`                                                                                                      |
| Boolean             | `Boolean`                                                                                                         |
| Byte                | `Byte`                                                                                                            |
| CipherText          | `CipherText`                                                                                                      |
| Date                | `LocalDate`                                                                                                       |
| Decimal             | `Decimal`                                                                                                         |
| Double              | `Double`                                                                                                          |
| Float               | `Float`                                                                                                           |
| Integer             | `Integer`                                                                                                         |
| Long                | `Long`                                                                                                            |
| Marking             | `Marking`                                                                                                         |
| OntologyObject      | `OntologyObject<T>` where `T` is the API name of the referenced object type.                                      |
| Short               | `Short`                                                                                                           |
| String              | `String`                                                                                                          |
| Struct              | `Struct<T>` where `T` contains field name and type pairs, e.g. `Struct<{ firstName: String, lastName: string }>`  |
| Timeseries          | `TimeSeries<T>` where `T` is either `String` for an enum series or `Double` for a numeric series.                 |
| Timestamp           | `Timestamp`                                                                                                       |
"""


ValueTypeApiName = str
"""The name of the value type in the API in camelCase format."""


ValueTypeRid = core.RID
"""ValueTypeRid"""


ArrayEntryEvaluatedConstraint = StructEvaluatedConstraint
"""Evaluated constraints for entries of array parameters for which per-entry evaluation is supported."""


core.resolve_forward_references(Aggregation, globalns=globals(), localns=locals())
core.resolve_forward_references(AggregationGroupBy, globalns=globals(), localns=locals())
core.resolve_forward_references(LogicRule, globalns=globals(), localns=locals())
core.resolve_forward_references(OntologyDataType, globalns=globals(), localns=locals())
core.resolve_forward_references(ParameterEvaluatedConstraint, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryAggregationKeyType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryAggregationRangeSubType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryAggregationValueType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryDataType, globalns=globals(), localns=locals())
core.resolve_forward_references(SearchJsonQuery, globalns=globals(), localns=locals())
core.resolve_forward_references(
    StructFieldEvaluatedConstraint, globalns=globals(), localns=locals()
)

__all__ = [
    "ActionRid",
    "ActionType",
    "ActionTypeApiName",
    "ActionTypeRid",
    "AggregateObjectsResponse",
    "AggregateObjectsResponseItem",
    "Aggregation",
    "AggregationDurationGrouping",
    "AggregationExactGrouping",
    "AggregationFixedWidthGrouping",
    "AggregationGroupBy",
    "AggregationGroupKey",
    "AggregationGroupValue",
    "AggregationMetricName",
    "AggregationMetricResult",
    "AggregationRange",
    "AggregationRangesGrouping",
    "AllTermsQuery",
    "AndQuery",
    "AnyTermQuery",
    "ApplyActionMode",
    "ApplyActionRequest",
    "ApplyActionRequestOptions",
    "ApplyActionResponse",
    "ApproximateDistinctAggregation",
    "ArrayEntryEvaluatedConstraint",
    "ArrayEvaluatedConstraint",
    "ArraySizeConstraint",
    "ArtifactRepositoryRid",
    "Attachment",
    "AttachmentRid",
    "AvgAggregation",
    "BatchApplyActionResponse",
    "ContainsQuery",
    "CountAggregation",
    "CreateInterfaceObjectRule",
    "CreateLinkRule",
    "CreateObjectRule",
    "DataValue",
    "DeleteInterfaceObjectRule",
    "DeleteLinkRule",
    "DeleteObjectRule",
    "DerivedPropertyApiName",
    "Duration",
    "EntrySetType",
    "EqualsQuery",
    "ExecuteQueryResponse",
    "FieldNameV1",
    "FilterValue",
    "FunctionRid",
    "FunctionVersion",
    "Fuzzy",
    "GroupMemberConstraint",
    "GtQuery",
    "GteQuery",
    "InterfaceLinkTypeApiName",
    "InterfaceLinkTypeRid",
    "InterfaceTypeApiName",
    "InterfaceTypeRid",
    "IsNullQuery",
    "LegacyObjectTypeId",
    "LegacyPropertyId",
    "LinkTypeApiName",
    "LinkTypeId",
    "LinkTypeSide",
    "LinkTypeSideCardinality",
    "ListActionTypesResponse",
    "ListLinkedObjectsResponse",
    "ListObjectTypesResponse",
    "ListObjectsResponse",
    "ListOntologiesResponse",
    "ListOutgoingLinkTypesResponse",
    "ListQueryTypesResponse",
    "LogicRule",
    "LtQuery",
    "LteQuery",
    "MaxAggregation",
    "MinAggregation",
    "ModifyInterfaceObjectRule",
    "ModifyObjectRule",
    "NotQuery",
    "ObjectPropertyValueConstraint",
    "ObjectQueryResultConstraint",
    "ObjectRid",
    "ObjectSetRid",
    "ObjectType",
    "ObjectTypeApiName",
    "ObjectTypeRid",
    "ObjectTypeVisibility",
    "OneOfConstraint",
    "Ontology",
    "OntologyApiName",
    "OntologyArrayType",
    "OntologyDataType",
    "OntologyInterfaceObjectSetType",
    "OntologyInterfaceObjectType",
    "OntologyMapType",
    "OntologyObject",
    "OntologyObjectSetType",
    "OntologyObjectType",
    "OntologyRid",
    "OntologySetType",
    "OntologyStructField",
    "OntologyStructType",
    "OrQuery",
    "OrderBy",
    "Parameter",
    "ParameterEvaluatedConstraint",
    "ParameterEvaluationResult",
    "ParameterId",
    "ParameterOption",
    "PhraseQuery",
    "PrefixQuery",
    "PrimaryKeyValue",
    "Property",
    "PropertyApiName",
    "PropertyFilter",
    "PropertyId",
    "PropertyTypeRid",
    "PropertyValue",
    "PropertyValueEscapedString",
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
    "QueryType",
    "QueryUnionType",
    "RangeConstraint",
    "ReturnEditsMode",
    "SdkPackageName",
    "SdkPackageRid",
    "SdkVersion",
    "SearchJsonQuery",
    "SearchObjectsResponse",
    "SearchOrderBy",
    "SearchOrderByType",
    "SearchOrdering",
    "SelectedPropertyApiName",
    "SharedPropertyTypeApiName",
    "SharedPropertyTypeRid",
    "StringLengthConstraint",
    "StringRegexMatchConstraint",
    "StructEvaluatedConstraint",
    "StructFieldEvaluatedConstraint",
    "StructFieldEvaluationResult",
    "StructParameterFieldApiName",
    "SubmissionCriteriaEvaluation",
    "SumAggregation",
    "ThreeDimensionalAggregation",
    "TwoDimensionalAggregation",
    "UnevaluableConstraint",
    "ValidateActionResponse",
    "ValidationResult",
    "ValueType",
    "ValueTypeApiName",
    "ValueTypeRid",
]
