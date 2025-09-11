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
from foundry_sdk.v2.geo import models as geo_models


class AbsoluteTimeRange(core.ModelBase):
    """ISO 8601 timestamps forming a range for a time series query. Start is inclusive and end is exclusive."""

    start_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("startTime"), default=None)  # type: ignore[literal-required]
    end_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("endTime"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["absolute"] = "absolute"


class AbsoluteValuePropertyExpression(core.ModelBase):
    """Calculates absolute value of a numeric value."""

    property: DerivedPropertyDefinition
    type: typing.Literal["absoluteValue"] = "absoluteValue"


class ActionParameterArrayType(core.ModelBase):
    """ActionParameterArrayType"""

    sub_type: ActionParameterType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"


ActionParameterType = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "OntologyInterfaceObjectType",
        "OntologyStructType",
        core_models.StringType,
        core_models.DoubleType,
        core_models.IntegerType,
        core_models.GeoShapeType,
        core_models.LongType,
        "OntologyObjectTypeReferenceType",
        core_models.BooleanType,
        core_models.MarkingType,
        core_models.AttachmentType,
        core_models.MediaReferenceType,
        ActionParameterArrayType,
        "OntologyObjectSetType",
        core_models.GeohashType,
        core_models.VectorType,
        "OntologyObjectType",
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Action parameters."""


class ActionParameterV2(core.ModelBase):
    """Details about a parameter of an action."""

    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    data_type: ActionParameterType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    required: bool


ActionResults = typing_extensions.Annotated[
    typing.Union["ObjectEdits", "ObjectTypeEdits"], pydantic.Field(discriminator="type")
]
"""ActionResults"""


ActionRid = core.RID
"""The unique resource identifier for an action."""


ActionTypeApiName = str
"""
The name of the action type in the API. To find the API name for your Action Type, use the `List action types`
endpoint or check the **Ontology Manager**.
"""


ActionTypeRid = core.RID
"""The unique resource identifier of an action type, useful for interacting with other Foundry APIs."""


class ActionTypeV2(core.ModelBase):
    """Represents an action type in the Ontology."""

    api_name: ActionTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    parameters: typing.Dict[ParameterId, ActionParameterV2]
    rid: ActionTypeRid
    operations: typing.List[LogicRule]


class ActivePropertyTypeStatus(core.ModelBase):
    """
    This status indicates that the PropertyType will not change on short notice and should thus be safe to use in
    user facing workflows.
    """

    type: typing.Literal["active"] = "active"


class AddLink(core.ModelBase):
    """AddLink"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object: LinkSideObject = pydantic.Field(alias=str("aSideObject"))  # type: ignore[literal-required]
    b_side_object: LinkSideObject = pydantic.Field(alias=str("bSideObject"))  # type: ignore[literal-required]
    type: typing.Literal["addLink"] = "addLink"


class AddLinkEdit(core.ModelBase):
    """AddLinkEdit"""

    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    primary_key: PrimaryKeyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    link_type: LinkTypeApiName = pydantic.Field(alias=str("linkType"))  # type: ignore[literal-required]
    linked_object_primary_key: PrimaryKeyValue = pydantic.Field(alias=str("linkedObjectPrimaryKey"))  # type: ignore[literal-required]
    type: typing.Literal["addLink"] = "addLink"


class AddObject(core.ModelBase):
    """AddObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    type: typing.Literal["addObject"] = "addObject"


class AddObjectEdit(core.ModelBase):
    """AddObjectEdit"""

    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    properties: typing.Dict[PropertyApiName, DataValue]
    type: typing.Literal["addObject"] = "addObject"


class AddPropertyExpression(core.ModelBase):
    """Adds two or more numeric values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["add"] = "add"


class AggregateObjectsResponseItemV2(core.ModelBase):
    """AggregateObjectsResponseItemV2"""

    group: typing.Dict[AggregationGroupKeyV2, typing.Optional[AggregationGroupValueV2]]
    metrics: typing.List[AggregationMetricResultV2]


class AggregateObjectsResponseV2(core.ModelBase):
    """AggregateObjectsResponseV2"""

    excluded_items: typing.Optional[int] = pydantic.Field(alias=str("excludedItems"), default=None)  # type: ignore[literal-required]
    accuracy: AggregationAccuracy
    data: typing.List[AggregateObjectsResponseItemV2]
    compute_usage: typing.Optional[core_models.ComputeSeconds] = pydantic.Field(alias=str("computeUsage"), default=None)  # type: ignore[literal-required]


class AggregateTimeSeries(core.ModelBase):
    """AggregateTimeSeries"""

    method: TimeSeriesAggregationMethod
    strategy: TimeSeriesAggregationStrategy


AggregationAccuracy = typing.Literal["ACCURATE", "APPROXIMATE"]
"""AggregationAccuracy"""


AggregationAccuracyRequest = typing.Literal["REQUIRE_ACCURATE", "ALLOW_APPROXIMATE"]
"""AggregationAccuracyRequest"""


class AggregationDurationGroupingV2(core.ModelBase):
    """
    Divides objects into groups according to an interval. Note that this grouping applies only on date and timestamp types.
    When grouping by `YEARS`, `QUARTERS`, `MONTHS`, or `WEEKS`, the `value` must be set to `1`.
    """

    field: PropertyApiName
    value: int
    unit: TimeUnit
    type: typing.Literal["duration"] = "duration"


class AggregationExactGroupingV2(core.ModelBase):
    """Divides objects into groups according to an exact value."""

    field: PropertyApiName
    max_group_count: typing.Optional[int] = pydantic.Field(alias=str("maxGroupCount"), default=None)  # type: ignore[literal-required]
    default_value: typing.Optional[str] = pydantic.Field(alias=str("defaultValue"), default=None)  # type: ignore[literal-required]
    """
    Includes a group with the specified default value that includes all objects where the specified field's value is null.
    Cannot be used with includeNullValues.
    """

    include_null_values: typing.Optional[bool] = pydantic.Field(alias=str("includeNullValues"), default=None)  # type: ignore[literal-required]
    """
    Includes a group with a null value that includes all objects where the specified field's value is null.
    Cannot be used with defaultValue or orderBy clauses on the aggregation.
    """

    type: typing.Literal["exact"] = "exact"


class AggregationFixedWidthGroupingV2(core.ModelBase):
    """Divides objects into groups with the specified width."""

    field: PropertyApiName
    fixed_width: int = pydantic.Field(alias=str("fixedWidth"))  # type: ignore[literal-required]
    type: typing.Literal["fixedWidth"] = "fixedWidth"


AggregationGroupByV2 = typing_extensions.Annotated[
    typing.Union[
        AggregationDurationGroupingV2,
        AggregationFixedWidthGroupingV2,
        "AggregationRangesGroupingV2",
        AggregationExactGroupingV2,
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies a grouping for aggregation results."""


AggregationGroupKeyV2 = str
"""AggregationGroupKeyV2"""


AggregationGroupValueV2 = typing.Any
"""AggregationGroupValueV2"""


AggregationMetricName = str
"""A user-specified alias for an aggregation metric name."""


class AggregationMetricResultV2(core.ModelBase):
    """AggregationMetricResultV2"""

    name: str
    value: typing.Optional[typing.Any] = None
    """
    The value of the metric. This will be a double in the case of
    a numeric metric, or a date string in the case of a date metric.
    """


class AggregationRangeV2(core.ModelBase):
    """Specifies a range from an inclusive start value to an exclusive end value."""

    start_value: typing.Any = pydantic.Field(alias=str("startValue"))  # type: ignore[literal-required]
    """Inclusive start."""

    end_value: typing.Any = pydantic.Field(alias=str("endValue"))  # type: ignore[literal-required]
    """Exclusive end."""


class AggregationRangesGroupingV2(core.ModelBase):
    """Divides objects into groups according to specified ranges."""

    field: PropertyApiName
    ranges: typing.List[AggregationRangeV2]
    type: typing.Literal["ranges"] = "ranges"


AggregationV2 = typing_extensions.Annotated[
    typing.Union[
        "ApproximateDistinctAggregationV2",
        "MinAggregationV2",
        "AvgAggregationV2",
        "MaxAggregationV2",
        "ApproximatePercentileAggregationV2",
        "CountAggregationV2",
        "SumAggregationV2",
        "ExactDistinctAggregationV2",
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies an aggregation function."""


class AndQueryV2(core.ModelBase):
    """Returns objects where every query is satisfied."""

    value: typing.List[SearchJsonQueryV2]
    type: typing.Literal["and"] = "and"


ApplyActionMode = typing.Literal["VALIDATE_ONLY", "VALIDATE_AND_EXECUTE"]
"""ApplyActionMode"""


class ApplyActionRequestOptions(core.ModelBase):
    """ApplyActionRequestOptions"""

    mode: typing.Optional[ApplyActionMode] = None
    return_edits: typing.Optional[ReturnEditsMode] = pydantic.Field(alias=str("returnEdits"), default=None)  # type: ignore[literal-required]


class ApproximateDistinctAggregationV2(core.ModelBase):
    """Computes an approximate number of distinct values for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["approximateDistinct"] = "approximateDistinct"


class ApproximatePercentileAggregationV2(core.ModelBase):
    """Computes the approximate percentile value for the provided field. Requires Object Storage V2."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    approximate_percentile: float = pydantic.Field(alias=str("approximatePercentile"))  # type: ignore[literal-required]
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["approximatePercentile"] = "approximatePercentile"


class ArrayConstraint(core.ModelBase):
    """ArrayConstraint"""

    minimum_size: typing.Optional[int] = pydantic.Field(alias=str("minimumSize"), default=None)  # type: ignore[literal-required]
    maximum_size: typing.Optional[int] = pydantic.Field(alias=str("maximumSize"), default=None)  # type: ignore[literal-required]
    unique_values: bool = pydantic.Field(alias=str("uniqueValues"))  # type: ignore[literal-required]
    value_constraint: typing.Optional[ValueTypeConstraint] = pydantic.Field(alias=str("valueConstraint"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"


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


AttachmentMetadataResponse = typing_extensions.Annotated[
    typing.Union["AttachmentV2", "ListAttachmentsResponseV2"], pydantic.Field(discriminator="type")
]
"""The attachment metadata response"""


AttachmentRid = core.RID
"""The unique resource identifier of an attachment."""


class AttachmentV2(core.ModelBase):
    """The representation of an attachment."""

    rid: AttachmentRid
    filename: core_models.Filename
    size_bytes: core_models.SizeBytes = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    media_type: core_models.MediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]
    type: typing.Literal["single"] = "single"


class AvgAggregationV2(core.ModelBase):
    """Computes the average value for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["avg"] = "avg"


BatchActionObjectEdit = typing_extensions.Annotated[
    typing.Union["ModifyObject", AddObject, AddLink], pydantic.Field(discriminator="type")
]
"""BatchActionObjectEdit"""


class BatchActionObjectEdits(core.ModelBase):
    """BatchActionObjectEdits"""

    edits: typing.List[BatchActionObjectEdit]
    added_object_count: int = pydantic.Field(alias=str("addedObjectCount"))  # type: ignore[literal-required]
    modified_objects_count: int = pydantic.Field(alias=str("modifiedObjectsCount"))  # type: ignore[literal-required]
    deleted_objects_count: int = pydantic.Field(alias=str("deletedObjectsCount"))  # type: ignore[literal-required]
    added_links_count: int = pydantic.Field(alias=str("addedLinksCount"))  # type: ignore[literal-required]
    deleted_links_count: int = pydantic.Field(alias=str("deletedLinksCount"))  # type: ignore[literal-required]
    type: typing.Literal["edits"] = "edits"


BatchActionResults = typing_extensions.Annotated[
    typing.Union[BatchActionObjectEdits, "ObjectTypeEdits"], pydantic.Field(discriminator="type")
]
"""BatchActionResults"""


class BatchApplyActionRequestItem(core.ModelBase):
    """BatchApplyActionRequestItem"""

    parameters: typing.Dict[ParameterId, typing.Optional[DataValue]]


class BatchApplyActionRequestOptions(core.ModelBase):
    """BatchApplyActionRequestOptions"""

    return_edits: typing.Optional[BatchReturnEditsMode] = pydantic.Field(alias=str("returnEdits"), default=None)  # type: ignore[literal-required]


class BatchApplyActionResponseV2(core.ModelBase):
    """BatchApplyActionResponseV2"""

    edits: typing.Optional[BatchActionResults] = None


BatchReturnEditsMode = typing.Literal["ALL", "NONE"]
"""BatchReturnEditsMode"""


class BlueprintIcon(core.ModelBase):
    """BlueprintIcon"""

    color: str
    """A hexadecimal color code."""

    name: str
    """
    The [name](https://blueprintjs.com/docs/#icons/icons-list) of the Blueprint icon. 
    Used to specify the Blueprint icon to represent the object type in a React app.
    """

    type: typing.Literal["blueprint"] = "blueprint"


class BoundingBoxValue(core.ModelBase):
    """The top left and bottom right coordinate points that make up the bounding box."""

    top_left: WithinBoundingBoxPoint = pydantic.Field(alias=str("topLeft"))  # type: ignore[literal-required]
    bottom_right: WithinBoundingBoxPoint = pydantic.Field(alias=str("bottomRight"))  # type: ignore[literal-required]


class CenterPoint(core.ModelBase):
    """The coordinate point to use as the center of the distance query."""

    center: CenterPointTypes
    distance: core_models.Distance


class ContainsAllTermsInOrderPrefixLastTerm(core.ModelBase):
    """
    Returns objects where the specified field contains all of the terms in the order provided,
    but they do have to be adjacent to each other.
    The last term can be a partial prefix match. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` can be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: str
    type: typing.Literal["containsAllTermsInOrderPrefixLastTerm"] = (
        "containsAllTermsInOrderPrefixLastTerm"
    )


class ContainsAllTermsInOrderQuery(core.ModelBase):
    """
    Returns objects where the specified field contains all of the terms in the order provided,
    but they do have to be adjacent to each other. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: str
    type: typing.Literal["containsAllTermsInOrder"] = "containsAllTermsInOrder"


class ContainsAllTermsQuery(core.ModelBase):
    """
    Returns objects where the specified field contains all of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: str
    fuzzy: typing.Optional[FuzzyV2] = None
    type: typing.Literal["containsAllTerms"] = "containsAllTerms"


class ContainsAnyTermQuery(core.ModelBase):
    """
    Returns objects where the specified field contains any of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: str
    fuzzy: typing.Optional[FuzzyV2] = None
    type: typing.Literal["containsAnyTerm"] = "containsAnyTerm"


class ContainsQueryV2(core.ModelBase):
    """
    Returns objects where the specified array contains a value. Allows you to specify a property to query on by a
    variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["contains"] = "contains"


class CountAggregationV2(core.ModelBase):
    """Computes the total count of objects."""

    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["count"] = "count"


class CountObjectsResponseV2(core.ModelBase):
    """CountObjectsResponseV2"""

    count: typing.Optional[int] = None


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


class CreateTemporaryObjectSetResponseV2(core.ModelBase):
    """CreateTemporaryObjectSetResponseV2"""

    object_set_rid: ObjectSetRid = pydantic.Field(alias=str("objectSetRid"))  # type: ignore[literal-required]


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


class DecryptionResult(core.ModelBase):
    """The result of a CipherText decryption. If successful, the plaintext decrypted value will be returned. Otherwise, an error will be thrown."""

    plaintext: typing.Optional[Plaintext] = None


class DeleteInterfaceObjectRule(core.ModelBase):
    """DeleteInterfaceObjectRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteInterfaceObject"] = "deleteInterfaceObject"


class DeleteLink(core.ModelBase):
    """DeleteLink"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object: LinkSideObject = pydantic.Field(alias=str("aSideObject"))  # type: ignore[literal-required]
    b_side_object: LinkSideObject = pydantic.Field(alias=str("bSideObject"))  # type: ignore[literal-required]
    type: typing.Literal["deleteLink"] = "deleteLink"


class DeleteLinkEdit(core.ModelBase):
    """DeleteLinkEdit"""

    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    primary_key: PrimaryKeyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    link_type: LinkTypeApiName = pydantic.Field(alias=str("linkType"))  # type: ignore[literal-required]
    linked_object_primary_key: PrimaryKeyValue = pydantic.Field(alias=str("linkedObjectPrimaryKey"))  # type: ignore[literal-required]
    type: typing.Literal["removeLink"] = "removeLink"


class DeleteLinkRule(core.ModelBase):
    """DeleteLinkRule"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("aSideObjectTypeApiName"))  # type: ignore[literal-required]
    b_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("bSideObjectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteLink"] = "deleteLink"


class DeleteObject(core.ModelBase):
    """DeleteObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    type: typing.Literal["deleteObject"] = "deleteObject"


class DeleteObjectEdit(core.ModelBase):
    """DeleteObjectEdit"""

    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    type: typing.Literal["deleteObject"] = "deleteObject"


class DeleteObjectRule(core.ModelBase):
    """DeleteObjectRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteObject"] = "deleteObject"


class DeprecatedPropertyTypeStatus(core.ModelBase):
    """
    This status indicates that the PropertyType is reaching the end of its life and will be removed as per the
    deadline specified.
    """

    message: str
    deadline: core.AwareDatetime
    replaced_by: typing.Optional[PropertyTypeRid] = pydantic.Field(alias=str("replacedBy"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["deprecated"] = "deprecated"


DerivedPropertyApiName = str
"""The name of the derived property that will be returned."""


DerivedPropertyDefinition = typing_extensions.Annotated[
    typing.Union[
        AddPropertyExpression,
        AbsoluteValuePropertyExpression,
        "ExtractPropertyExpression",
        "SelectedPropertyExpression",
        "NegatePropertyExpression",
        "SubtractPropertyExpression",
        "PropertyApiNameSelector",
        "LeastPropertyExpression",
        "DividePropertyExpression",
        "MultiplyPropertyExpression",
        "GreatestPropertyExpression",
    ],
    pydantic.Field(discriminator="type"),
]
"""Definition of a derived property."""


class DividePropertyExpression(core.ModelBase):
    """Divides the left numeric value by the right numeric value."""

    left: DerivedPropertyDefinition
    right: DerivedPropertyDefinition
    type: typing.Literal["divide"] = "divide"


class DoesNotIntersectBoundingBoxQuery(core.ModelBase):
    """
    Returns objects where the specified field does not intersect the bounding box provided. Allows you to specify a
    property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not
    both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: BoundingBoxValue
    type: typing.Literal["doesNotIntersectBoundingBox"] = "doesNotIntersectBoundingBox"


class DoesNotIntersectPolygonQuery(core.ModelBase):
    """
    Returns objects where the specified field does not intersect the polygon provided. Allows you to specify a
    property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not
    both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PolygonValue
    type: typing.Literal["doesNotIntersectPolygon"] = "doesNotIntersectPolygon"


class DoubleVector(core.ModelBase):
    """
    The vector to search with. The vector must be of the same dimension as the vectors stored in the provided
    propertyIdentifier.
    """

    value: typing.List[float]
    type: typing.Literal["vector"] = "vector"


class EntrySetType(core.ModelBase):
    """EntrySetType"""

    key_type: QueryDataType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: QueryDataType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["entrySet"] = "entrySet"


class EnumConstraint(core.ModelBase):
    """EnumConstraint"""

    options: typing.List[typing.Optional[PropertyValue]]
    type: typing.Literal["enum"] = "enum"


class EqualsQueryV2(core.ModelBase):
    """
    Returns objects where the specified field is equal to a value. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["eq"] = "eq"


class ExactDistinctAggregationV2(core.ModelBase):
    """Computes an exact number of distinct values for the provided field. May be slower than an approximate distinct aggregation. Requires Object Storage V2."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["exactDistinct"] = "exactDistinct"


class ExamplePropertyTypeStatus(core.ModelBase):
    """
    This status indicates that the PropertyType is an example. It is backed by notional data that should not be
    used for actual workflows, but can be used to test those workflows.
    """

    type: typing.Literal["example"] = "example"


class ExecuteQueryResponse(core.ModelBase):
    """ExecuteQueryResponse"""

    value: DataValue


class ExperimentalPropertyTypeStatus(core.ModelBase):
    """This status indicates that the PropertyType is in development."""

    type: typing.Literal["experimental"] = "experimental"


ExtractDatePart = typing.Literal["DAYS", "MONTHS", "QUARTERS", "YEARS"]
"""ExtractDatePart"""


class ExtractPropertyExpression(core.ModelBase):
    """Extracts the specified date part from a date or timestamp."""

    property: DerivedPropertyDefinition
    part: ExtractDatePart
    type: typing.Literal["extract"] = "extract"


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


FuzzyV2 = bool
"""Setting fuzzy to `true` allows approximate matching in search queries that support it."""


class GetSelectedPropertyOperation(core.ModelBase):
    """
    Gets a single value of a property. Throws if the target object set is on the MANY side of the link and could
    explode the cardinality.

    Use collectList or collectSet which will return a list of values in that case.
    """

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["get"] = "get"


class GreatestPropertyExpression(core.ModelBase):
    """Finds greatest of two or more numeric, date or timestamp values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["greatest"] = "greatest"


class GroupMemberConstraint(core.ModelBase):
    """The parameter value must be the user id of a member belonging to at least one of the groups defined by the constraint."""

    type: typing.Literal["groupMember"] = "groupMember"


class GtQueryV2(core.ModelBase):
    """
    Returns objects where the specified field is greater than a value. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["gt"] = "gt"


class GteQueryV2(core.ModelBase):
    """
    Returns objects where the specified field is greater than or equal to a value. Allows you to specify a property
    to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["gte"] = "gte"


class InQuery(core.ModelBase):
    """
    Returns objects where the specified field equals any of the provided values. Allows you to
    specify a property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied,
    but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: typing.List[PropertyValue]
    type: typing.Literal["in"] = "in"


class InterfaceLinkType(core.ModelBase):
    """
    A link type constraint defined at the interface level where the implementation of the links is provided
    by the implementing object types.
    """

    rid: InterfaceLinkTypeRid
    api_name: InterfaceLinkTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """The description of the interface link type."""

    linked_entity_api_name: InterfaceLinkTypeLinkedEntityApiName = pydantic.Field(alias=str("linkedEntityApiName"))  # type: ignore[literal-required]
    cardinality: InterfaceLinkTypeCardinality
    required: bool
    """Whether each implementing object type must declare at least one implementation of this link."""


InterfaceLinkTypeApiName = str
"""
The name of the interface link type in the API. To find the API name for your Interface Link Type, check the 
[Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
"""


InterfaceLinkTypeCardinality = typing.Literal["ONE", "MANY"]
"""
The cardinality of the link in the given direction. Cardinality can be "ONE", meaning an object can
link to zero or one other objects, or "MANY", meaning an object can link to any number of other objects.
"""


InterfaceLinkTypeLinkedEntityApiName = typing_extensions.Annotated[
    typing.Union["LinkedObjectTypeApiName", "LinkedInterfaceTypeApiName"],
    pydantic.Field(discriminator="type"),
]
"""A reference to the linked entity. This can either be an object or an interface type."""


InterfaceLinkTypeRid = core.RID
"""The unique resource identifier of an interface link type, useful for interacting with other Foundry APIs."""


class InterfaceSharedPropertyType(core.ModelBase):
    """
    A shared property type with an additional field to indicate whether the property must be included on every
    object type that implements the interface, or whether it is optional.
    """

    rid: SharedPropertyTypeRid
    api_name: SharedPropertyTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """A short text that describes the SharedPropertyType."""

    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    value_type_api_name: typing.Optional[ValueTypeApiName] = pydantic.Field(alias=str("valueTypeApiName"), default=None)  # type: ignore[literal-required]
    required: bool
    """Whether each implementing object type must declare an implementation for this property."""


InterfaceToObjectTypeMapping = typing.Dict["SharedPropertyTypeApiName", "PropertyApiName"]
"""Represents an implementation of an interface (the mapping of interface property to local property)."""


InterfaceToObjectTypeMappings = typing.Dict["ObjectTypeApiName", InterfaceToObjectTypeMapping]
"""Map from object type to the interface-to-object-type mapping for that object type."""


class InterfaceType(core.ModelBase):
    """Represents an interface type in the Ontology."""

    rid: InterfaceTypeRid
    api_name: InterfaceTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """The description of the interface."""

    properties: typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType]
    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has. A shared property type must be unique across all of the properties.
    """

    all_properties: typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType] = pydantic.Field(alias=str("allProperties"))  # type: ignore[literal-required]
    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has, including properties from all directly and indirectly extended 
    interfaces.
    """

    extends_interfaces: typing.List[InterfaceTypeApiName] = pydantic.Field(alias=str("extendsInterfaces"))  # type: ignore[literal-required]
    """
    A list of interface API names that this interface extends. An interface can extend other interfaces to 
    inherit their properties.
    """

    all_extends_interfaces: typing.List[InterfaceTypeApiName] = pydantic.Field(alias=str("allExtendsInterfaces"))  # type: ignore[literal-required]
    """A list of interface API names that this interface extends, both directly and indirectly."""

    implemented_by_object_types: typing.List[ObjectTypeApiName] = pydantic.Field(alias=str("implementedByObjectTypes"))  # type: ignore[literal-required]
    """A list of object API names that implement this interface."""

    links: typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkType]
    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has.
    """

    all_links: typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkType] = pydantic.Field(alias=str("allLinks"))  # type: ignore[literal-required]
    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has, including links from all directly and indirectly extended interfaces.
    """


InterfaceTypeApiName = str
"""
The name of the interface type in the API in UpperCamelCase format. To find the API name for your interface
type, use the `List interface types` endpoint or check the **Ontology Manager**.
"""


InterfaceTypeRid = core.RID
"""The unique resource identifier of an interface, useful for interacting with other Foundry APIs."""


class IntersectsBoundingBoxQuery(core.ModelBase):
    """
    Returns objects where the specified field intersects the bounding box provided. Allows you to specify a property
    to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: BoundingBoxValue
    type: typing.Literal["intersectsBoundingBox"] = "intersectsBoundingBox"


class IntersectsPolygonQuery(core.ModelBase):
    """
    Returns objects where the specified field intersects the polygon provided. Allows you to specify a property to
    query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PolygonValue
    type: typing.Literal["intersectsPolygon"] = "intersectsPolygon"


class IsNullQueryV2(core.ModelBase):
    """
    Returns objects based on the existence of the specified field. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: bool
    type: typing.Literal["isNull"] = "isNull"


class LeastPropertyExpression(core.ModelBase):
    """Finds least of two or more numeric, date or timestamp values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["least"] = "least"


class LengthConstraint(core.ModelBase):
    """LengthConstraint"""

    minimum_length: typing.Optional[float] = pydantic.Field(alias=str("minimumLength"), default=None)  # type: ignore[literal-required]
    maximum_length: typing.Optional[float] = pydantic.Field(alias=str("maximumLength"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["length"] = "length"


class LinkSideObject(core.ModelBase):
    """LinkSideObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]


LinkTypeApiName = str
"""
The name of the link type in the API. To find the API name for your Link Type, check the **Ontology Manager**
application.
"""


LinkTypeId = str
"""The unique ID of a link type. To find the ID for your link type, check the **Ontology Manager** application."""


LinkTypeRid = core.RID
"""LinkTypeRid"""


LinkTypeSideCardinality = typing.Literal["ONE", "MANY"]
"""LinkTypeSideCardinality"""


class LinkTypeSideV2(core.ModelBase):
    """
    `foreignKeyPropertyApiName` is the API name of the foreign key on this object type. If absent, the link is
    either a m2m link or the linked object has the foreign key and this object type has the primary key.
    """

    api_name: LinkTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    cardinality: LinkTypeSideCardinality
    foreign_key_property_api_name: typing.Optional[PropertyApiName] = pydantic.Field(alias=str("foreignKeyPropertyApiName"), default=None)  # type: ignore[literal-required]
    link_type_rid: LinkTypeRid = pydantic.Field(alias=str("linkTypeRid"))  # type: ignore[literal-required]


class LinkedInterfaceTypeApiName(core.ModelBase):
    """A reference to the linked interface type."""

    api_name: InterfaceTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    type: typing.Literal["interfaceTypeApiName"] = "interfaceTypeApiName"


class LinkedObjectTypeApiName(core.ModelBase):
    """A reference to the linked object type."""

    api_name: ObjectTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    type: typing.Literal["objectTypeApiName"] = "objectTypeApiName"


class ListActionTypesResponseV2(core.ModelBase):
    """ListActionTypesResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[ActionTypeV2]


class ListAttachmentsResponseV2(core.ModelBase):
    """ListAttachmentsResponseV2"""

    data: typing.List[AttachmentV2]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["multiple"] = "multiple"


class ListInterfaceLinkedObjectsResponse(core.ModelBase):
    """ListInterfaceLinkedObjectsResponse"""

    data: typing.List[OntologyObjectV2]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListInterfaceTypesResponse(core.ModelBase):
    """ListInterfaceTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[InterfaceType]


class ListLinkedObjectsResponseV2(core.ModelBase):
    """ListLinkedObjectsResponseV2"""

    data: typing.List[OntologyObjectV2]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListObjectTypesV2Response(core.ModelBase):
    """ListObjectTypesV2Response"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[ObjectTypeV2]
    """The list of object types in the current page."""


class ListObjectsForInterfaceResponse(core.ModelBase):
    """ListObjectsForInterfaceResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[OntologyObjectV2]
    """The list of interface instances in the current page."""

    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]


class ListObjectsResponseV2(core.ModelBase):
    """ListObjectsResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[OntologyObjectV2]
    """The list of objects in the current page."""

    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]


class ListOntologiesV2Response(core.ModelBase):
    """ListOntologiesV2Response"""

    data: typing.List[OntologyV2]
    """The list of Ontologies the user has access to."""


class ListOntologyValueTypesResponse(core.ModelBase):
    """ListOntologyValueTypesResponse"""

    data: typing.List[OntologyValueType]


class ListOutgoingInterfaceLinkTypesResponse(core.ModelBase):
    """ListOutgoingInterfaceLinkTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[InterfaceLinkType]
    """The list of interface link types in the current page."""


class ListOutgoingLinkTypesResponseV2(core.ModelBase):
    """ListOutgoingLinkTypesResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[LinkTypeSideV2]
    """The list of link type sides in the current page."""


class ListQueryTypesResponseV2(core.ModelBase):
    """ListQueryTypesResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[QueryTypeV2]


class LoadObjectSetResponseV2(core.ModelBase):
    """Represents the API response when loading an `ObjectSet`."""

    data: typing.List[OntologyObjectV2]
    """The list of objects in the current Page."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    compute_usage: typing.Optional[core_models.ComputeSeconds] = pydantic.Field(alias=str("computeUsage"), default=None)  # type: ignore[literal-required]


class LoadObjectSetV2MultipleObjectTypesResponse(core.ModelBase):
    """
    Represents the API response when loading an `ObjectSet`. An `interfaceToObjectTypeMappings` field is
    optionally returned if the type scope of the returned object set includes any interfaces. The "type scope"
    of an object set refers to whether objects contain all their properties (object-type type scope) or just the
    properties that implement interface properties (interface type scope). There can be multiple type scopes in a
    single object set- some objects may have all their properties and some may only have interface properties.

    The `interfaceToObjectTypeMappings` field contains mappings from `SharedPropertyTypeApiName`s on the interface(s) to
    `PropertyApiName` for properties on the object(s).
    """

    data: typing.List[OntologyObjectV2]
    """The list of objects in the current page."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    interface_to_object_type_mappings: typing.Dict[InterfaceTypeApiName, InterfaceToObjectTypeMappings] = pydantic.Field(alias=str("interfaceToObjectTypeMappings"))  # type: ignore[literal-required]
    compute_usage: typing.Optional[core_models.ComputeSeconds] = pydantic.Field(alias=str("computeUsage"), default=None)  # type: ignore[literal-required]


class LoadObjectSetV2ObjectsOrInterfacesResponse(core.ModelBase):
    """
    Represents the API response when loading an `ObjectSet`. Objects in the returned set can either have properties
    defined by an interface that the objects belong to or properties defined by the object type of the object.
    """

    data: typing.List[OntologyObjectV2]
    """The list of objects in the current page."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]


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


class LtQueryV2(core.ModelBase):
    """
    Returns objects where the specified field is less than a value. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["lt"] = "lt"


class LteQueryV2(core.ModelBase):
    """
    Returns objects where the specified field is less than or equal to a value. Allows you to specify a property to
    query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["lte"] = "lte"


class MaxAggregationV2(core.ModelBase):
    """Computes the maximum value for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["max"] = "max"


class MediaMetadata(core.ModelBase):
    """MediaMetadata"""

    path: typing.Optional[core_models.MediaItemPath] = None
    size_bytes: core_models.SizeBytes = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    media_type: core_models.MediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]


class MinAggregationV2(core.ModelBase):
    """Computes the minimum value for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["min"] = "min"


class ModifyInterfaceObjectRule(core.ModelBase):
    """ModifyInterfaceObjectRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["modifyInterfaceObject"] = "modifyInterfaceObject"


class ModifyObject(core.ModelBase):
    """ModifyObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    type: typing.Literal["modifyObject"] = "modifyObject"


class ModifyObjectEdit(core.ModelBase):
    """ModifyObjectEdit"""

    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    properties: typing.Dict[PropertyApiName, DataValue]
    type: typing.Literal["modifyObject"] = "modifyObject"


class ModifyObjectRule(core.ModelBase):
    """ModifyObjectRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["modifyObject"] = "modifyObject"


class MultiplyPropertyExpression(core.ModelBase):
    """Multiplies two or more numeric values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["multiply"] = "multiply"


NearestNeighborsQuery = typing_extensions.Annotated[
    typing.Union[DoubleVector, "NearestNeighborsQueryText"], pydantic.Field(discriminator="type")
]
"""
Queries support either a vector matching the embedding model defined on the property, or text that is 
automatically embedded.
"""


class NearestNeighborsQueryText(core.ModelBase):
    """Automatically embed the text in a vector using the embedding model configured for the given propertyIdentifier."""

    value: str
    type: typing.Literal["text"] = "text"


class NegatePropertyExpression(core.ModelBase):
    """Negates a numeric value."""

    property: DerivedPropertyDefinition
    type: typing.Literal["negate"] = "negate"


class NestedQueryAggregation(core.ModelBase):
    """NestedQueryAggregation"""

    key: typing.Any
    groups: typing.List[QueryAggregation]


class NotQueryV2(core.ModelBase):
    """Returns objects where the query is not satisfied."""

    value: SearchJsonQueryV2
    type: typing.Literal["not"] = "not"


ObjectEdit = typing_extensions.Annotated[
    typing.Union[ModifyObject, DeleteObject, AddObject, DeleteLink, AddLink],
    pydantic.Field(discriminator="type"),
]
"""ObjectEdit"""


class ObjectEdits(core.ModelBase):
    """ObjectEdits"""

    edits: typing.List[ObjectEdit]
    added_object_count: int = pydantic.Field(alias=str("addedObjectCount"))  # type: ignore[literal-required]
    modified_objects_count: int = pydantic.Field(alias=str("modifiedObjectsCount"))  # type: ignore[literal-required]
    deleted_objects_count: int = pydantic.Field(alias=str("deletedObjectsCount"))  # type: ignore[literal-required]
    added_links_count: int = pydantic.Field(alias=str("addedLinksCount"))  # type: ignore[literal-required]
    deleted_links_count: int = pydantic.Field(alias=str("deletedLinksCount"))  # type: ignore[literal-required]
    type: typing.Literal["edits"] = "edits"


ObjectPropertyType = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "StructType",
        core_models.StringType,
        core_models.ByteType,
        core_models.DoubleType,
        core_models.GeoPointType,
        core_models.GeotimeSeriesReferenceType,
        core_models.IntegerType,
        core_models.FloatType,
        core_models.GeoShapeType,
        core_models.LongType,
        core_models.BooleanType,
        core_models.CipherTextType,
        core_models.MarkingType,
        core_models.AttachmentType,
        core_models.MediaReferenceType,
        core_models.TimeseriesType,
        "OntologyObjectArrayType",
        core_models.ShortType,
        core_models.VectorType,
        core_models.DecimalType,
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Object properties."""


class ObjectPropertyValueConstraint(core.ModelBase):
    """The parameter value must be a property value of an object found within an object set."""

    type: typing.Literal["objectPropertyValue"] = "objectPropertyValue"


class ObjectQueryResultConstraint(core.ModelBase):
    """The parameter value must be the primary key of an object found within an object set."""

    type: typing.Literal["objectQueryResult"] = "objectQueryResult"


ObjectRid = core.RID
"""The unique resource identifier of an object, useful for interacting with other Foundry APIs."""


ObjectSet = typing_extensions.Annotated[
    typing.Union[
        "ObjectSetSearchAroundType",
        "ObjectSetStaticType",
        "ObjectSetIntersectionType",
        "ObjectSetWithPropertiesType",
        "ObjectSetInterfaceLinkSearchAroundType",
        "ObjectSetSubtractType",
        "ObjectSetNearestNeighborsType",
        "ObjectSetUnionType",
        "ObjectSetAsTypeType",
        "ObjectSetMethodInputType",
        "ObjectSetReferenceType",
        "ObjectSetFilterType",
        "ObjectSetInterfaceBaseType",
        "ObjectSetAsBaseObjectTypesType",
        "ObjectSetBaseType",
    ],
    pydantic.Field(discriminator="type"),
]
"""Represents the definition of an `ObjectSet` in the `Ontology`."""


class ObjectSetAsBaseObjectTypesType(core.ModelBase):
    """
    Casts the objects in the object set to their base type and thus ensures objects are returned with all of their
    properties in the resulting object set, not just the properties that implement interface properties.
    """

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    type: typing.Literal["asBaseObjectTypes"] = "asBaseObjectTypes"


class ObjectSetAsTypeType(core.ModelBase):
    """
    Casts an object set to a specified object type or interface type API name. Any object whose object type does
    not match the object type provided or implement the interface type provided will be dropped from the resulting
    object set.
    """

    entity_type: str = pydantic.Field(alias=str("entityType"))  # type: ignore[literal-required]
    """An object type or interface type API name."""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    type: typing.Literal["asType"] = "asType"


class ObjectSetBaseType(core.ModelBase):
    """ObjectSetBaseType"""

    object_type: str = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    """The API name of the object type."""

    type: typing.Literal["base"] = "base"


class ObjectSetFilterType(core.ModelBase):
    """ObjectSetFilterType"""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    where: SearchJsonQueryV2
    type: typing.Literal["filter"] = "filter"


class ObjectSetInterfaceBaseType(core.ModelBase):
    """ObjectSetInterfaceBaseType"""

    interface_type: str = pydantic.Field(alias=str("interfaceType"))  # type: ignore[literal-required]
    """
    An object set with objects that implement the interface with the given interface API name. The objects in 
    the object set will only have properties that implement properties of the given interface, unless you set the includeAllBaseObjectProperties flag.
    """

    include_all_base_object_properties: typing.Optional[bool] = pydantic.Field(alias=str("includeAllBaseObjectProperties"), default=None)  # type: ignore[literal-required]
    """
    A flag that will return all of the underlying object properties for the objects that implement the interface. 
    This includes properties that don't explicitly implement an SPT on the interface.
    """

    type: typing.Literal["interfaceBase"] = "interfaceBase"


class ObjectSetInterfaceLinkSearchAroundType(core.ModelBase):
    """ObjectSetInterfaceLinkSearchAroundType"""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    interface_link: InterfaceLinkTypeApiName = pydantic.Field(alias=str("interfaceLink"))  # type: ignore[literal-required]
    type: typing.Literal["interfaceLinkSearchAround"] = "interfaceLinkSearchAround"


class ObjectSetIntersectionType(core.ModelBase):
    """ObjectSetIntersectionType"""

    object_sets: typing.List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]
    type: typing.Literal["intersect"] = "intersect"


class ObjectSetMethodInputType(core.ModelBase):
    """
    ObjectSet which is the root of a MethodObjectSet definition.

    This feature is experimental and not yet generally available.
    """

    type: typing.Literal["methodInput"] = "methodInput"


class ObjectSetNearestNeighborsType(core.ModelBase):
    """
    ObjectSet containing the top `numNeighbors` objects with `propertyIdentifier` nearest to the input vector or
    text. This can only be performed on a property with type vector that has been configured to be searched with
    approximate nearest neighbors using a similarity function configured in the Ontology.

    A non-zero score for each resulting object is returned when the `orderType` in the `orderBy` field is set to
    `relevance`. Note that:
      - Scores will not be returned if a nearestNeighbors object set is composed through union, subtraction
        or intersection with non-nearestNeighbors object sets.
      - If results have scores, the order of the scores will be decreasing (duplicate scores are possible).
    """

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    property_identifier: PropertyIdentifier = pydantic.Field(alias=str("propertyIdentifier"))  # type: ignore[literal-required]
    num_neighbors: int = pydantic.Field(alias=str("numNeighbors"))  # type: ignore[literal-required]
    """
    The number of objects to return. If the number of documents in the objectType is less than the provided
    value, all objects will be returned. This value is limited to 1 &lt;= numNeighbors &lt;= 500.
    """

    query: NearestNeighborsQuery
    type: typing.Literal["nearestNeighbors"] = "nearestNeighbors"


class ObjectSetReferenceType(core.ModelBase):
    """ObjectSetReferenceType"""

    reference: ObjectSetRid
    type: typing.Literal["reference"] = "reference"


ObjectSetRid = core.RID
"""ObjectSetRid"""


class ObjectSetSearchAroundType(core.ModelBase):
    """ObjectSetSearchAroundType"""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    link: LinkTypeApiName
    type: typing.Literal["searchAround"] = "searchAround"


class ObjectSetStaticType(core.ModelBase):
    """ObjectSetStaticType"""

    objects: typing.List[ObjectRid]
    type: typing.Literal["static"] = "static"


class ObjectSetSubtractType(core.ModelBase):
    """ObjectSetSubtractType"""

    object_sets: typing.List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]
    type: typing.Literal["subtract"] = "subtract"


class ObjectSetUnionType(core.ModelBase):
    """ObjectSetUnionType"""

    object_sets: typing.List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]
    type: typing.Literal["union"] = "union"


class ObjectSetWithPropertiesType(core.ModelBase):
    """
    ObjectSet which returns objects with additional derived properties.

    This feature is experimental and not yet generally available.
    """

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    derived_properties: typing.Dict[DerivedPropertyApiName, DerivedPropertyDefinition] = pydantic.Field(alias=str("derivedProperties"))  # type: ignore[literal-required]
    """Map of the name of the derived property to return and its definition"""

    type: typing.Literal["withProperties"] = "withProperties"


ObjectTypeApiName = str
"""
The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the
`List object types` endpoint or check the **Ontology Manager**.
"""


class ObjectTypeEdits(core.ModelBase):
    """ObjectTypeEdits"""

    edited_object_types: typing.List[ObjectTypeApiName] = pydantic.Field(alias=str("editedObjectTypes"))  # type: ignore[literal-required]
    type: typing.Literal["largeScaleEdits"] = "largeScaleEdits"


class ObjectTypeFullMetadata(core.ModelBase):
    """ObjectTypeFullMetadata"""

    object_type: ObjectTypeV2 = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    link_types: typing.List[LinkTypeSideV2] = pydantic.Field(alias=str("linkTypes"))  # type: ignore[literal-required]
    implements_interfaces: typing.List[InterfaceTypeApiName] = pydantic.Field(alias=str("implementsInterfaces"))  # type: ignore[literal-required]
    """A list of interfaces that this object type implements."""

    implements_interfaces2: typing.Dict[InterfaceTypeApiName, ObjectTypeInterfaceImplementation] = pydantic.Field(alias=str("implementsInterfaces2"))  # type: ignore[literal-required]
    """A list of interfaces that this object type implements and how it implements them."""

    shared_property_type_mapping: typing.Dict[SharedPropertyTypeApiName, PropertyApiName] = pydantic.Field(alias=str("sharedPropertyTypeMapping"))  # type: ignore[literal-required]
    """
    A map from shared property type API name to backing local property API name for the shared property types 
    present on this object type.
    """


ObjectTypeId = str
"""The unique identifier (ID) for an object type. This can be viewed in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/)."""


class ObjectTypeInterfaceImplementation(core.ModelBase):
    """ObjectTypeInterfaceImplementation"""

    properties: typing.Dict[SharedPropertyTypeApiName, PropertyApiName]
    links: typing.Dict[InterfaceLinkTypeApiName, typing.List[LinkTypeApiName]]


ObjectTypeRid = core.RID
"""The unique resource identifier of an object type, useful for interacting with other Foundry APIs."""


class ObjectTypeV2(core.ModelBase):
    """Represents an object type in the Ontology."""

    api_name: ObjectTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    description: typing.Optional[str] = None
    """The description of the object type."""

    plural_display_name: str = pydantic.Field(alias=str("pluralDisplayName"))  # type: ignore[literal-required]
    """The plural display name of the object type."""

    icon: Icon
    primary_key: PropertyApiName = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    properties: typing.Dict[PropertyApiName, PropertyV2]
    """A map of the properties of the object type."""

    rid: ObjectTypeRid
    title_property: PropertyApiName = pydantic.Field(alias=str("titleProperty"))  # type: ignore[literal-required]
    visibility: typing.Optional[ObjectTypeVisibility] = None


ObjectTypeVisibility = typing.Literal["NORMAL", "PROMINENT", "HIDDEN"]
"""The suggested visibility of the object type."""


class OneOfConstraint(core.ModelBase):
    """The parameter has a manually predefined set of options."""

    options: typing.List[ParameterOption]
    other_values_allowed: bool = pydantic.Field(alias=str("otherValuesAllowed"))  # type: ignore[literal-required]
    """A flag denoting whether custom, user provided values will be considered valid. This is configured via the **Allowed "Other" value** toggle in the **Ontology Manager**."""

    type: typing.Literal["oneOf"] = "oneOf"


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


class OntologyFullMetadata(core.ModelBase):
    """OntologyFullMetadata"""

    ontology: OntologyV2
    object_types: typing.Dict[ObjectTypeApiName, ObjectTypeFullMetadata] = pydantic.Field(alias=str("objectTypes"))  # type: ignore[literal-required]
    action_types: typing.Dict[ActionTypeApiName, ActionTypeV2] = pydantic.Field(alias=str("actionTypes"))  # type: ignore[literal-required]
    query_types: typing.Dict[VersionedQueryTypeApiName, QueryTypeV2] = pydantic.Field(alias=str("queryTypes"))  # type: ignore[literal-required]
    interface_types: typing.Dict[InterfaceTypeApiName, InterfaceType] = pydantic.Field(alias=str("interfaceTypes"))  # type: ignore[literal-required]
    shared_property_types: typing.Dict[SharedPropertyTypeApiName, SharedPropertyType] = pydantic.Field(alias=str("sharedPropertyTypes"))  # type: ignore[literal-required]
    branch: typing.Optional[core_models.BranchMetadata] = None
    value_types: typing.Dict[ValueTypeApiName, OntologyValueType] = pydantic.Field(alias=str("valueTypes"))  # type: ignore[literal-required]


OntologyIdentifier = str
"""
The API name or RID of the Ontology. To find the API name or RID, use the **List Ontologies** endpoint or
check the **Ontology Manager**.
"""


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


class OntologyObjectArrayType(core.ModelBase):
    """OntologyObjectArrayType"""

    sub_type: ObjectPropertyType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"


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


class OntologyObjectTypeReferenceType(core.ModelBase):
    """OntologyObjectTypeReferenceType"""

    type: typing.Literal["objectType"] = "objectType"


OntologyObjectV2 = typing.Dict["PropertyApiName", "PropertyValue"]
"""Represents an object in the Ontology."""


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


OntologyTransactionRid = core.RID
"""The RID identifying a transaction."""


class OntologyV2(core.ModelBase):
    """Metadata about an Ontology."""

    api_name: OntologyApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: str
    rid: OntologyRid


class OntologyValueType(core.ModelBase):
    """OntologyValueType"""

    api_name: ValueTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    rid: ValueTypeRid
    status: typing.Optional[ValueTypeStatus] = None
    field_type: ValueTypeFieldType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    version: str
    constraints: typing.List[ValueTypeConstraint]


class OrQueryV2(core.ModelBase):
    """Returns objects where at least 1 query is satisfied."""

    value: typing.List[SearchJsonQueryV2]
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


OrderByDirection = typing.Literal["ASC", "DESC"]
"""OrderByDirection"""


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


Plaintext = str
"""Plaintext"""


class PostTransactionEditsResponse(core.ModelBase):
    """PostTransactionEditsResponse"""


class PreciseDuration(core.ModelBase):
    """A measurement of duration."""

    value: int
    """The duration value."""

    unit: PreciseTimeUnit
    type: typing.Literal["duration"] = "duration"


PreciseTimeUnit = typing.Literal["NANOSECONDS", "SECONDS", "MINUTES", "HOURS", "DAYS", "WEEKS"]
"""The unit of a fixed-width duration. Each day is 24 hours and each week is 7 days."""


PrimaryKeyValue = typing.Any
"""Represents the primary key value that is used as a unique identifier for an object."""


PropertyApiName = str
"""
The name of the property in the API. To find the API name for your property, use the `Get object type`
endpoint or check the **Ontology Manager**.
"""


class PropertyApiNameSelector(core.ModelBase):
    """A property api name that references properties to query on."""

    api_name: PropertyApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    type: typing.Literal["property"] = "property"


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


PropertyIdentifier = typing_extensions.Annotated[
    typing.Union[PropertyApiNameSelector, "StructFieldSelector"],
    pydantic.Field(discriminator="type"),
]
"""An identifier used to select properties or struct fields."""


PropertyTypeRid = core.RID
"""PropertyTypeRid"""


PropertyTypeStatus = typing_extensions.Annotated[
    typing.Union[
        DeprecatedPropertyTypeStatus,
        ActivePropertyTypeStatus,
        ExperimentalPropertyTypeStatus,
        ExamplePropertyTypeStatus,
    ],
    pydantic.Field(discriminator="type"),
]
"""The status to indicate whether the PropertyType is either Experimental, Active, Deprecated, or Example."""


PropertyTypeVisibility = typing.Literal["NORMAL", "PROMINENT", "HIDDEN"]
"""PropertyTypeVisibility"""


class PropertyV2(core.ModelBase):
    """Details about some property of an object."""

    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    rid: PropertyTypeRid
    status: typing.Optional[PropertyTypeStatus] = None
    visibility: typing.Optional[PropertyTypeVisibility] = None
    value_type_api_name: typing.Optional[ValueTypeApiName] = pydantic.Field(alias=str("valueTypeApiName"), default=None)  # type: ignore[literal-required]


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


class QueryAggregation(core.ModelBase):
    """QueryAggregation"""

    key: typing.Any
    value: typing.Any


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


class QueryParameterV2(core.ModelBase):
    """Details about a parameter of a query."""

    description: typing.Optional[str] = None
    data_type: QueryDataType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]


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


class QueryThreeDimensionalAggregation(core.ModelBase):
    """QueryThreeDimensionalAggregation"""

    groups: typing.List[NestedQueryAggregation]


class QueryTwoDimensionalAggregation(core.ModelBase):
    """QueryTwoDimensionalAggregation"""

    groups: typing.List[QueryAggregation]


class QueryTypeV2(core.ModelBase):
    """Represents a query type in the Ontology."""

    api_name: QueryApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, QueryParameterV2]
    output: QueryDataType
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


class RangesConstraint(core.ModelBase):
    """RangesConstraint"""

    minimum_value: typing.Optional[PropertyValue] = pydantic.Field(alias=str("minimumValue"), default=None)  # type: ignore[literal-required]
    maximum_value: typing.Optional[PropertyValue] = pydantic.Field(alias=str("maximumValue"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["range"] = "range"


class RegexConstraint(core.ModelBase):
    """RegexConstraint"""

    pattern: str
    partial_match: bool = pydantic.Field(alias=str("partialMatch"))  # type: ignore[literal-required]
    type: typing.Literal["regex"] = "regex"


class RelativeTime(core.ModelBase):
    """A relative time, such as "3 days before" or "2 hours after" the current moment."""

    when: RelativeTimeRelation
    value: int
    unit: RelativeTimeSeriesTimeUnit


class RelativeTimeRange(core.ModelBase):
    """A relative time range for a time series query."""

    start_time: typing.Optional[RelativeTime] = pydantic.Field(alias=str("startTime"), default=None)  # type: ignore[literal-required]
    end_time: typing.Optional[RelativeTime] = pydantic.Field(alias=str("endTime"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["relative"] = "relative"


RelativeTimeRelation = typing.Literal["BEFORE", "AFTER"]
"""RelativeTimeRelation"""


RelativeTimeSeriesTimeUnit = typing.Literal[
    "MILLISECONDS", "SECONDS", "MINUTES", "HOURS", "DAYS", "WEEKS", "MONTHS", "YEARS"
]
"""RelativeTimeSeriesTimeUnit"""


ReturnEditsMode = typing.Literal["ALL", "ALL_V2_WITH_DELETIONS", "NONE"]
"""ReturnEditsMode"""


class RidConstraint(core.ModelBase):
    """The string must be a valid RID (Resource Identifier)."""

    type: typing.Literal["rid"] = "rid"


class RollingAggregateWindowPoints(core.ModelBase):
    """Number of points in each window."""

    count: int
    type: typing.Literal["pointsCount"] = "pointsCount"


SdkPackageName = str
"""SdkPackageName"""


SdkPackageRid = core.RID
"""SdkPackageRid"""


SdkVersion = str
"""SdkVersion"""


SearchJsonQueryV2 = typing_extensions.Annotated[
    typing.Union[
        OrQueryV2,
        InQuery,
        DoesNotIntersectPolygonQuery,
        LtQueryV2,
        DoesNotIntersectBoundingBoxQuery,
        EqualsQueryV2,
        ContainsAllTermsQuery,
        GtQueryV2,
        "WildcardQuery",
        "WithinDistanceOfQuery",
        "WithinBoundingBoxQuery",
        ContainsQueryV2,
        NotQueryV2,
        IntersectsBoundingBoxQuery,
        AndQueryV2,
        IsNullQueryV2,
        ContainsAllTermsInOrderPrefixLastTerm,
        ContainsAnyTermQuery,
        GteQueryV2,
        ContainsAllTermsInOrderQuery,
        "WithinPolygonQuery",
        IntersectsPolygonQuery,
        LteQueryV2,
        "StartsWithQuery",
    ],
    pydantic.Field(discriminator="type"),
]
"""SearchJsonQueryV2"""


class SearchObjectsResponseV2(core.ModelBase):
    """SearchObjectsResponseV2"""

    data: typing.List[OntologyObjectV2]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]


SearchOrderByType = typing.Literal["fields", "relevance"]
"""SearchOrderByType"""


class SearchOrderByV2(core.ModelBase):
    """Specifies the ordering of search results by a field and an ordering direction or by relevance if scores are required in a nearestNeighbors query. By default `orderType` is set to `fields`."""

    order_type: typing.Optional[SearchOrderByType] = pydantic.Field(alias=str("orderType"), default=None)  # type: ignore[literal-required]
    fields: typing.List[SearchOrderingV2]


class SearchOrderingV2(core.ModelBase):
    """SearchOrderingV2"""

    field: PropertyApiName
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


class SelectedPropertyApproximateDistinctAggregation(core.ModelBase):
    """Computes an approximate number of distinct values for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["approximateDistinct"] = "approximateDistinct"


class SelectedPropertyApproximatePercentileAggregation(core.ModelBase):
    """Computes the approximate percentile value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    approximate_percentile: float = pydantic.Field(alias=str("approximatePercentile"))  # type: ignore[literal-required]
    type: typing.Literal["approximatePercentile"] = "approximatePercentile"


class SelectedPropertyAvgAggregation(core.ModelBase):
    """Computes the average value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["avg"] = "avg"


class SelectedPropertyCollectListAggregation(core.ModelBase):
    """
    Lists all values of a property up to the specified limit. The maximum supported limit is 100, by default.

    NOTE: A separate count aggregation should be used to determine the total count of values, to account for
    a possible truncation of the returned list.

    Ignores objects for which a property is absent, so the returned list will contain non-null values only.
    Returns an empty list when none of the objects have values for a provided property.
    """

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    limit: int
    """Maximum number of values to collect. The maximum supported limit is 100."""

    type: typing.Literal["collectList"] = "collectList"


class SelectedPropertyCollectSetAggregation(core.ModelBase):
    """
    Lists all distinct values of a property up to the specified limit. The maximum supported limit is 100.

    NOTE: A separate cardinality / exactCardinality aggregation should be used to determine the total count of
    values, to account for a possible truncation of the returned set.

    Ignores objects for which a property is absent, so the returned list will contain non-null values only.
    Returns an empty list when none of the objects have values for a provided property.
    """

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    limit: int
    """Maximum number of values to collect. The maximum supported limit is 100."""

    type: typing.Literal["collectSet"] = "collectSet"


class SelectedPropertyCountAggregation(core.ModelBase):
    """Computes the total count of objects."""

    type: typing.Literal["count"] = "count"


class SelectedPropertyExactDistinctAggregation(core.ModelBase):
    """Computes an exact number of distinct values for the provided field. May be slower than an approximate distinct aggregation."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["exactDistinct"] = "exactDistinct"


class SelectedPropertyExpression(core.ModelBase):
    """Definition for a selected property over a MethodObjectSet."""

    object_set: MethodObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    operation: SelectedPropertyOperation
    type: typing.Literal["selection"] = "selection"


class SelectedPropertyMaxAggregation(core.ModelBase):
    """Computes the maximum value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["max"] = "max"


class SelectedPropertyMinAggregation(core.ModelBase):
    """Computes the minimum value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["min"] = "min"


SelectedPropertyOperation = typing_extensions.Annotated[
    typing.Union[
        SelectedPropertyApproximateDistinctAggregation,
        SelectedPropertyMinAggregation,
        SelectedPropertyAvgAggregation,
        SelectedPropertyMaxAggregation,
        SelectedPropertyApproximatePercentileAggregation,
        GetSelectedPropertyOperation,
        SelectedPropertyCountAggregation,
        "SelectedPropertySumAggregation",
        SelectedPropertyCollectListAggregation,
        SelectedPropertyExactDistinctAggregation,
        SelectedPropertyCollectSetAggregation,
    ],
    pydantic.Field(discriminator="type"),
]
"""Operation on a selected property, can be an aggregation function or retrieval of a single selected property"""


class SelectedPropertySumAggregation(core.ModelBase):
    """Computes the sum of values for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["sum"] = "sum"


class SharedPropertyType(core.ModelBase):
    """A property type that can be shared across object types."""

    rid: SharedPropertyTypeRid
    api_name: SharedPropertyTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """A short text that describes the SharedPropertyType."""

    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    value_type_api_name: typing.Optional[ValueTypeApiName] = pydantic.Field(alias=str("valueTypeApiName"), default=None)  # type: ignore[literal-required]


SharedPropertyTypeApiName = str
"""
The name of the shared property type in the API in lowerCamelCase format. To find the API name for your
shared property type, use the `List shared property types` endpoint or check the **Ontology Manager**.
"""


SharedPropertyTypeRid = core.RID
"""The unique resource identifier of an shared property type, useful for interacting with other Foundry APIs."""


class StartsWithQuery(core.ModelBase):
    """
    Deprecated alias for `containsAllTermsInOrderPrefixLastTerm`, which is preferred because the name `startsWith` is misleading.
    Returns objects where the specified field starts with the provided value. Allows you to specify a property to
    query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: str
    type: typing.Literal["startsWith"] = "startsWith"


StreamingOutputFormat = typing.Literal["JSON", "ARROW"]
"""
Which format to serialize the binary stream in.
ARROW is more efficient for streaming a large sized response.
"""


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


class StructConstraint(core.ModelBase):
    """StructConstraint"""

    properties: typing.Dict[PropertyApiName, ValueTypeApiName]
    """A map of the properties of the struct type to the value type applied to that property."""

    type: typing.Literal["struct"] = "struct"


class StructEvaluatedConstraint(core.ModelBase):
    """Represents the validity of a singleton struct parameter."""

    struct_fields: typing.Dict[StructParameterFieldApiName, StructFieldEvaluationResult] = pydantic.Field(alias=str("structFields"))  # type: ignore[literal-required]
    type: typing.Literal["struct"] = "struct"


StructFieldApiName = str
"""The name of a struct field in the Ontology."""


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


class StructFieldSelector(core.ModelBase):
    """
    A combination of a property API name and a struct field API name used to select struct fields. Note that you can
    still select struct properties with only a 'PropertyApiNameSelector'; the queries will then become 'OR' queries
    across the fields of the struct property, and derived property expressions will operate on the whole struct
    where applicable.
    """

    property_api_name: PropertyApiName = pydantic.Field(alias=str("propertyApiName"))  # type: ignore[literal-required]
    struct_field_api_name: StructFieldApiName = pydantic.Field(alias=str("structFieldApiName"))  # type: ignore[literal-required]
    type: typing.Literal["structField"] = "structField"


class StructFieldType(core.ModelBase):
    """StructFieldType"""

    api_name: StructFieldApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    rid: StructFieldTypeRid
    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]


StructFieldTypeRid = core.RID
"""The unique resource identifier of a struct field, useful for interacting with other Foundry APIs."""


StructParameterFieldApiName = str
"""The unique identifier of the struct parameter field."""


class StructType(core.ModelBase):
    """StructType"""

    struct_field_types: typing.List[StructFieldType] = pydantic.Field(alias=str("structFieldTypes"))  # type: ignore[literal-required]
    type: typing.Literal["struct"] = "struct"


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


class SubtractPropertyExpression(core.ModelBase):
    """Subtracts the right numeric value from the left numeric value."""

    left: DerivedPropertyDefinition
    right: DerivedPropertyDefinition
    type: typing.Literal["subtract"] = "subtract"


class SumAggregationV2(core.ModelBase):
    """Computes the sum of values for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["sum"] = "sum"


class SyncApplyActionResponseV2(core.ModelBase):
    """SyncApplyActionResponseV2"""

    validation: typing.Optional[ValidateActionResponseV2] = None
    edits: typing.Optional[ActionResults] = None


class ThreeDimensionalAggregation(core.ModelBase):
    """ThreeDimensionalAggregation"""

    key_type: QueryAggregationKeyType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: TwoDimensionalAggregation = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["threeDimensionalAggregation"] = "threeDimensionalAggregation"


TimeRange = typing_extensions.Annotated[
    typing.Union[AbsoluteTimeRange, RelativeTimeRange], pydantic.Field(discriminator="type")
]
"""An absolute or relative range for a time series query."""


TimeSeriesAggregationMethod = typing.Literal[
    "SUM",
    "MEAN",
    "STANDARD_DEVIATION",
    "MAX",
    "MIN",
    "PERCENT_CHANGE",
    "DIFFERENCE",
    "PRODUCT",
    "COUNT",
    "FIRST",
    "LAST",
]
"""The aggregation function to use for aggregating time series data."""


TimeSeriesAggregationStrategy = typing_extensions.Annotated[
    typing.Union[
        "TimeSeriesRollingAggregate", "TimeSeriesPeriodicAggregate", "TimeSeriesCumulativeAggregate"
    ],
    pydantic.Field(discriminator="type"),
]
"""
CUMULATIVE aggregates all points up to the current point.
ROLLING aggregates all points in a rolling window whose size is either the specified number of points or
time duration.
PERIODIC aggregates all points in specified time windows.
"""


class TimeSeriesCumulativeAggregate(core.ModelBase):
    """
    The cumulative aggregate is calculated progressively for each point in the input time series,
    considering all preceding points up to and including the current point.
    """

    type: typing.Literal["cumulative"] = "cumulative"


class TimeSeriesPeriodicAggregate(core.ModelBase):
    """
    Aggregates values over discrete, periodic windows for a given time series.

    A periodic window divides the time series into windows of fixed durations.
    For each window, an aggregate function is applied to the points within that window. The result is a time series
    with values representing the aggregate for each window. Windows with no data points are not included
    in the output.

    Periodic aggregation is useful for downsampling a continuous stream of data to larger granularities such as
    hourly, daily, monthly.
    """

    window_size: PreciseDuration = pydantic.Field(alias=str("windowSize"))  # type: ignore[literal-required]
    alignment_timestamp: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("alignmentTimestamp"), default=None)  # type: ignore[literal-required]
    """
    The timestamp used to align the result, such that ticks in the result time series will lie at integer
    multiples of the window duration from the alignment timestamp.

    Default is the first epoch timestamp (January 1, 1970, 00:00:00 UTC) so that all aggregated points have
    timestamps at midnight UTC at the start of each window duration.

    For example, for a weekly aggregate with alignment timestamp 5 January, 8:33PM, 
    each aggregated timestamp will lie on the 7 day intervals at 8:33PM starting at 5 January.
    """

    window_type: TimeSeriesWindowType = pydantic.Field(alias=str("windowType"))  # type: ignore[literal-required]
    type: typing.Literal["periodic"] = "periodic"


class TimeSeriesPoint(core.ModelBase):
    """A time and value pair."""

    time: core.AwareDatetime
    """An ISO 8601 timestamp"""

    value: typing.Any
    """An object which is either an enum String or a double number."""


class TimeSeriesRollingAggregate(core.ModelBase):
    """TimeSeriesRollingAggregate"""

    window_size: TimeSeriesRollingAggregateWindow = pydantic.Field(alias=str("windowSize"))  # type: ignore[literal-required]
    type: typing.Literal["rolling"] = "rolling"


TimeSeriesRollingAggregateWindow = typing_extensions.Annotated[
    typing.Union[PreciseDuration, RollingAggregateWindowPoints],
    pydantic.Field(discriminator="type"),
]
"""
A rolling window is a moving subset of data points that ends at the current timestamp (inclusive)
and spans a specified duration (window size). As new data points are added, old points fall out of the
window if they are outside the specified duration.

Rolling windows are commonly used for smoothing data, detecting trends, and reducing noise
in time series analysis.
"""


TimeSeriesWindowType = typing.Literal["START", "END"]
"""TimeSeriesWindowType"""


TimeUnit = typing.Literal[
    "MILLISECONDS", "SECONDS", "MINUTES", "HOURS", "DAYS", "WEEKS", "MONTHS", "YEARS", "QUARTERS"
]
"""TimeUnit"""


class TimeseriesEntry(core.ModelBase):
    """A time and value pair."""

    time: core.AwareDatetime
    """An ISO 8601 timestamp"""

    value: typing.Any
    """An object which is either an enum String, double number, or a geopoint."""


TransactionEdit = typing_extensions.Annotated[
    typing.Union[ModifyObjectEdit, DeleteObjectEdit, AddObjectEdit, DeleteLinkEdit, AddLinkEdit],
    pydantic.Field(discriminator="type"),
]
"""TransactionEdit"""


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


class UuidConstraint(core.ModelBase):
    """The string must be a valid UUID (Universally Unique Identifier)."""

    type: typing.Literal["uuid"] = "uuid"


class ValidateActionResponseV2(core.ModelBase):
    """ValidateActionResponseV2"""

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


class ValueTypeArrayType(core.ModelBase):
    """ValueTypeArrayType"""

    sub_type: typing.Optional[ValueTypeFieldType] = pydantic.Field(alias=str("subType"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"


ValueTypeConstraint = typing_extensions.Annotated[
    typing.Union[
        StructConstraint,
        RegexConstraint,
        core_models.UnsupportedType,
        ArrayConstraint,
        LengthConstraint,
        RangesConstraint,
        RidConstraint,
        UuidConstraint,
        EnumConstraint,
    ],
    pydantic.Field(discriminator="type"),
]
"""ValueTypeConstraint"""


class ValueTypeDecimalType(core.ModelBase):
    """ValueTypeDecimalType"""

    type: typing.Literal["decimal"] = "decimal"


ValueTypeFieldType = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "ValueTypeStructType",
        core_models.StringType,
        core_models.ByteType,
        core_models.DoubleType,
        "ValueTypeOptionalType",
        core_models.IntegerType,
        "ValueTypeUnionType",
        core_models.FloatType,
        core_models.LongType,
        "ValueTypeReferenceType",
        core_models.BooleanType,
        ValueTypeArrayType,
        core_models.BinaryType,
        core_models.ShortType,
        ValueTypeDecimalType,
        "ValueTypeMapType",
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""ValueTypeFieldType"""


class ValueTypeMapType(core.ModelBase):
    """ValueTypeMapType"""

    key_type: typing.Optional[ValueTypeFieldType] = pydantic.Field(alias=str("keyType"), default=None)  # type: ignore[literal-required]
    value_type: typing.Optional[ValueTypeFieldType] = pydantic.Field(alias=str("valueType"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"


class ValueTypeOptionalType(core.ModelBase):
    """ValueTypeOptionalType"""

    wrapped_type: typing.Optional[ValueTypeFieldType] = pydantic.Field(alias=str("wrappedType"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["optional"] = "optional"


class ValueTypeReferenceType(core.ModelBase):
    """ValueTypeReferenceType"""

    type: typing.Literal["reference"] = "reference"


ValueTypeRid = core.RID
"""ValueTypeRid"""


ValueTypeStatus = typing.Literal["ACTIVE", "DEPRECATED"]
"""ValueTypeStatus"""


class ValueTypeStructField(core.ModelBase):
    """ValueTypeStructField"""

    name: typing.Optional[core_models.StructFieldName] = None
    field_type: typing.Optional[ValueTypeFieldType] = pydantic.Field(alias=str("fieldType"), default=None)  # type: ignore[literal-required]


class ValueTypeStructType(core.ModelBase):
    """ValueTypeStructType"""

    fields: typing.List[ValueTypeStructField]
    type: typing.Literal["struct"] = "struct"


class ValueTypeUnionType(core.ModelBase):
    """ValueTypeUnionType"""

    member_types: typing.List[ValueTypeFieldType] = pydantic.Field(alias=str("memberTypes"))  # type: ignore[literal-required]
    type: typing.Literal["union"] = "union"


VersionedQueryTypeApiName = str
"""
The name of the Query in the API and an optional version identifier separated by a colon.
If the API name contains a colon, then a version identifier of either "latest" or a semantic version must
be included.
If the API does not contain a colon, then either the version identifier must be excluded or a version
identifier of a semantic version must be included.
Examples: 'myGroup:myFunction:latest', 'myGroup:myFunction:1.0.0', 'myFunction', 'myFunction:2.0.0'
"""


class WildcardQuery(core.ModelBase):
    """
    Returns objects where the specified field matches the wildcard pattern provided.
    Either `field` or `propertyIdentifier` can be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: str
    type: typing.Literal["wildcard"] = "wildcard"


class WithinBoundingBoxQuery(core.ModelBase):
    """
    Returns objects where the specified field contains a point within the bounding box provided. Allows you to
    specify a property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied,
    but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: BoundingBoxValue
    type: typing.Literal["withinBoundingBox"] = "withinBoundingBox"


class WithinDistanceOfQuery(core.ModelBase):
    """
    Returns objects where the specified field contains a point within the distance provided of the center point.
    Allows you to specify a property to query on by a variety of means. Either `field` or `propertyIdentifier`
    must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: CenterPoint
    type: typing.Literal["withinDistanceOf"] = "withinDistanceOf"


class WithinPolygonQuery(core.ModelBase):
    """
    Returns objects where the specified field contains a point within the polygon provided. Allows you to specify a
    property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not
    both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PolygonValue
    type: typing.Literal["withinPolygon"] = "withinPolygon"


ArrayEntryEvaluatedConstraint = StructEvaluatedConstraint
"""Evaluated constraints for entries of array parameters for which per-entry evaluation is supported."""


CenterPointTypes = geo_models.GeoPoint
"""CenterPointTypes"""


Icon = BlueprintIcon
"""A union currently only consisting of the BlueprintIcon (more icon types may be added in the future)."""


MethodObjectSet = ObjectSet
"""MethodObjectSet"""


PolygonValue = geo_models.Polygon
"""PolygonValue"""


WithinBoundingBoxPoint = geo_models.GeoPoint
"""WithinBoundingBoxPoint"""


core.resolve_forward_references(ActionParameterType, globalns=globals(), localns=locals())
core.resolve_forward_references(ActionResults, globalns=globals(), localns=locals())
core.resolve_forward_references(AggregationGroupByV2, globalns=globals(), localns=locals())
core.resolve_forward_references(AggregationV2, globalns=globals(), localns=locals())
core.resolve_forward_references(AttachmentMetadataResponse, globalns=globals(), localns=locals())
core.resolve_forward_references(BatchActionObjectEdit, globalns=globals(), localns=locals())
core.resolve_forward_references(BatchActionResults, globalns=globals(), localns=locals())
core.resolve_forward_references(DerivedPropertyDefinition, globalns=globals(), localns=locals())
core.resolve_forward_references(
    InterfaceLinkTypeLinkedEntityApiName, globalns=globals(), localns=locals()
)
core.resolve_forward_references(InterfaceToObjectTypeMapping, globalns=globals(), localns=locals())
core.resolve_forward_references(InterfaceToObjectTypeMappings, globalns=globals(), localns=locals())
core.resolve_forward_references(LogicRule, globalns=globals(), localns=locals())
core.resolve_forward_references(NearestNeighborsQuery, globalns=globals(), localns=locals())
core.resolve_forward_references(ObjectEdit, globalns=globals(), localns=locals())
core.resolve_forward_references(ObjectPropertyType, globalns=globals(), localns=locals())
core.resolve_forward_references(ObjectSet, globalns=globals(), localns=locals())
core.resolve_forward_references(OntologyDataType, globalns=globals(), localns=locals())
core.resolve_forward_references(OntologyObjectV2, globalns=globals(), localns=locals())
core.resolve_forward_references(ParameterEvaluatedConstraint, globalns=globals(), localns=locals())
core.resolve_forward_references(PropertyIdentifier, globalns=globals(), localns=locals())
core.resolve_forward_references(PropertyTypeStatus, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryAggregationKeyType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryAggregationRangeSubType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryAggregationValueType, globalns=globals(), localns=locals())
core.resolve_forward_references(QueryDataType, globalns=globals(), localns=locals())
core.resolve_forward_references(SearchJsonQueryV2, globalns=globals(), localns=locals())
core.resolve_forward_references(SelectedPropertyOperation, globalns=globals(), localns=locals())
core.resolve_forward_references(
    StructFieldEvaluatedConstraint, globalns=globals(), localns=locals()
)
core.resolve_forward_references(TimeRange, globalns=globals(), localns=locals())
core.resolve_forward_references(TimeSeriesAggregationStrategy, globalns=globals(), localns=locals())
core.resolve_forward_references(
    TimeSeriesRollingAggregateWindow, globalns=globals(), localns=locals()
)
core.resolve_forward_references(TransactionEdit, globalns=globals(), localns=locals())
core.resolve_forward_references(ValueTypeConstraint, globalns=globals(), localns=locals())
core.resolve_forward_references(ValueTypeFieldType, globalns=globals(), localns=locals())

__all__ = [
    "AbsoluteTimeRange",
    "AbsoluteValuePropertyExpression",
    "ActionParameterArrayType",
    "ActionParameterType",
    "ActionParameterV2",
    "ActionResults",
    "ActionRid",
    "ActionTypeApiName",
    "ActionTypeRid",
    "ActionTypeV2",
    "ActivePropertyTypeStatus",
    "AddLink",
    "AddLinkEdit",
    "AddObject",
    "AddObjectEdit",
    "AddPropertyExpression",
    "AggregateObjectsResponseItemV2",
    "AggregateObjectsResponseV2",
    "AggregateTimeSeries",
    "AggregationAccuracy",
    "AggregationAccuracyRequest",
    "AggregationDurationGroupingV2",
    "AggregationExactGroupingV2",
    "AggregationFixedWidthGroupingV2",
    "AggregationGroupByV2",
    "AggregationGroupKeyV2",
    "AggregationGroupValueV2",
    "AggregationMetricName",
    "AggregationMetricResultV2",
    "AggregationRangeV2",
    "AggregationRangesGroupingV2",
    "AggregationV2",
    "AndQueryV2",
    "ApplyActionMode",
    "ApplyActionRequestOptions",
    "ApproximateDistinctAggregationV2",
    "ApproximatePercentileAggregationV2",
    "ArrayConstraint",
    "ArrayEntryEvaluatedConstraint",
    "ArrayEvaluatedConstraint",
    "ArraySizeConstraint",
    "ArtifactRepositoryRid",
    "AttachmentMetadataResponse",
    "AttachmentRid",
    "AttachmentV2",
    "AvgAggregationV2",
    "BatchActionObjectEdit",
    "BatchActionObjectEdits",
    "BatchActionResults",
    "BatchApplyActionRequestItem",
    "BatchApplyActionRequestOptions",
    "BatchApplyActionResponseV2",
    "BatchReturnEditsMode",
    "BlueprintIcon",
    "BoundingBoxValue",
    "CenterPoint",
    "CenterPointTypes",
    "ContainsAllTermsInOrderPrefixLastTerm",
    "ContainsAllTermsInOrderQuery",
    "ContainsAllTermsQuery",
    "ContainsAnyTermQuery",
    "ContainsQueryV2",
    "CountAggregationV2",
    "CountObjectsResponseV2",
    "CreateInterfaceObjectRule",
    "CreateLinkRule",
    "CreateObjectRule",
    "CreateTemporaryObjectSetResponseV2",
    "DataValue",
    "DecryptionResult",
    "DeleteInterfaceObjectRule",
    "DeleteLink",
    "DeleteLinkEdit",
    "DeleteLinkRule",
    "DeleteObject",
    "DeleteObjectEdit",
    "DeleteObjectRule",
    "DeprecatedPropertyTypeStatus",
    "DerivedPropertyApiName",
    "DerivedPropertyDefinition",
    "DividePropertyExpression",
    "DoesNotIntersectBoundingBoxQuery",
    "DoesNotIntersectPolygonQuery",
    "DoubleVector",
    "EntrySetType",
    "EnumConstraint",
    "EqualsQueryV2",
    "ExactDistinctAggregationV2",
    "ExamplePropertyTypeStatus",
    "ExecuteQueryResponse",
    "ExperimentalPropertyTypeStatus",
    "ExtractDatePart",
    "ExtractPropertyExpression",
    "FilterValue",
    "FunctionRid",
    "FunctionVersion",
    "FuzzyV2",
    "GetSelectedPropertyOperation",
    "GreatestPropertyExpression",
    "GroupMemberConstraint",
    "GtQueryV2",
    "GteQueryV2",
    "Icon",
    "InQuery",
    "InterfaceLinkType",
    "InterfaceLinkTypeApiName",
    "InterfaceLinkTypeCardinality",
    "InterfaceLinkTypeLinkedEntityApiName",
    "InterfaceLinkTypeRid",
    "InterfaceSharedPropertyType",
    "InterfaceToObjectTypeMapping",
    "InterfaceToObjectTypeMappings",
    "InterfaceType",
    "InterfaceTypeApiName",
    "InterfaceTypeRid",
    "IntersectsBoundingBoxQuery",
    "IntersectsPolygonQuery",
    "IsNullQueryV2",
    "LeastPropertyExpression",
    "LengthConstraint",
    "LinkSideObject",
    "LinkTypeApiName",
    "LinkTypeId",
    "LinkTypeRid",
    "LinkTypeSideCardinality",
    "LinkTypeSideV2",
    "LinkedInterfaceTypeApiName",
    "LinkedObjectTypeApiName",
    "ListActionTypesResponseV2",
    "ListAttachmentsResponseV2",
    "ListInterfaceLinkedObjectsResponse",
    "ListInterfaceTypesResponse",
    "ListLinkedObjectsResponseV2",
    "ListObjectTypesV2Response",
    "ListObjectsForInterfaceResponse",
    "ListObjectsResponseV2",
    "ListOntologiesV2Response",
    "ListOntologyValueTypesResponse",
    "ListOutgoingInterfaceLinkTypesResponse",
    "ListOutgoingLinkTypesResponseV2",
    "ListQueryTypesResponseV2",
    "LoadObjectSetResponseV2",
    "LoadObjectSetV2MultipleObjectTypesResponse",
    "LoadObjectSetV2ObjectsOrInterfacesResponse",
    "LogicRule",
    "LtQueryV2",
    "LteQueryV2",
    "MaxAggregationV2",
    "MediaMetadata",
    "MethodObjectSet",
    "MinAggregationV2",
    "ModifyInterfaceObjectRule",
    "ModifyObject",
    "ModifyObjectEdit",
    "ModifyObjectRule",
    "MultiplyPropertyExpression",
    "NearestNeighborsQuery",
    "NearestNeighborsQueryText",
    "NegatePropertyExpression",
    "NestedQueryAggregation",
    "NotQueryV2",
    "ObjectEdit",
    "ObjectEdits",
    "ObjectPropertyType",
    "ObjectPropertyValueConstraint",
    "ObjectQueryResultConstraint",
    "ObjectRid",
    "ObjectSet",
    "ObjectSetAsBaseObjectTypesType",
    "ObjectSetAsTypeType",
    "ObjectSetBaseType",
    "ObjectSetFilterType",
    "ObjectSetInterfaceBaseType",
    "ObjectSetInterfaceLinkSearchAroundType",
    "ObjectSetIntersectionType",
    "ObjectSetMethodInputType",
    "ObjectSetNearestNeighborsType",
    "ObjectSetReferenceType",
    "ObjectSetRid",
    "ObjectSetSearchAroundType",
    "ObjectSetStaticType",
    "ObjectSetSubtractType",
    "ObjectSetUnionType",
    "ObjectSetWithPropertiesType",
    "ObjectTypeApiName",
    "ObjectTypeEdits",
    "ObjectTypeFullMetadata",
    "ObjectTypeId",
    "ObjectTypeInterfaceImplementation",
    "ObjectTypeRid",
    "ObjectTypeV2",
    "ObjectTypeVisibility",
    "OneOfConstraint",
    "OntologyApiName",
    "OntologyArrayType",
    "OntologyDataType",
    "OntologyFullMetadata",
    "OntologyIdentifier",
    "OntologyInterfaceObjectSetType",
    "OntologyInterfaceObjectType",
    "OntologyMapType",
    "OntologyObjectArrayType",
    "OntologyObjectSetType",
    "OntologyObjectType",
    "OntologyObjectTypeReferenceType",
    "OntologyObjectV2",
    "OntologyRid",
    "OntologySetType",
    "OntologyStructField",
    "OntologyStructType",
    "OntologyTransactionRid",
    "OntologyV2",
    "OntologyValueType",
    "OrQueryV2",
    "OrderBy",
    "OrderByDirection",
    "ParameterEvaluatedConstraint",
    "ParameterEvaluationResult",
    "ParameterId",
    "ParameterOption",
    "Plaintext",
    "PolygonValue",
    "PostTransactionEditsResponse",
    "PreciseDuration",
    "PreciseTimeUnit",
    "PrimaryKeyValue",
    "PropertyApiName",
    "PropertyApiNameSelector",
    "PropertyFilter",
    "PropertyId",
    "PropertyIdentifier",
    "PropertyTypeRid",
    "PropertyTypeStatus",
    "PropertyTypeVisibility",
    "PropertyV2",
    "PropertyValue",
    "PropertyValueEscapedString",
    "QueryAggregation",
    "QueryAggregationKeyType",
    "QueryAggregationRangeSubType",
    "QueryAggregationRangeType",
    "QueryAggregationValueType",
    "QueryApiName",
    "QueryArrayType",
    "QueryDataType",
    "QueryParameterV2",
    "QueryRuntimeErrorParameter",
    "QuerySetType",
    "QueryStructField",
    "QueryStructType",
    "QueryThreeDimensionalAggregation",
    "QueryTwoDimensionalAggregation",
    "QueryTypeV2",
    "QueryUnionType",
    "RangeConstraint",
    "RangesConstraint",
    "RegexConstraint",
    "RelativeTime",
    "RelativeTimeRange",
    "RelativeTimeRelation",
    "RelativeTimeSeriesTimeUnit",
    "ReturnEditsMode",
    "RidConstraint",
    "RollingAggregateWindowPoints",
    "SdkPackageName",
    "SdkPackageRid",
    "SdkVersion",
    "SearchJsonQueryV2",
    "SearchObjectsResponseV2",
    "SearchOrderByType",
    "SearchOrderByV2",
    "SearchOrderingV2",
    "SelectedPropertyApiName",
    "SelectedPropertyApproximateDistinctAggregation",
    "SelectedPropertyApproximatePercentileAggregation",
    "SelectedPropertyAvgAggregation",
    "SelectedPropertyCollectListAggregation",
    "SelectedPropertyCollectSetAggregation",
    "SelectedPropertyCountAggregation",
    "SelectedPropertyExactDistinctAggregation",
    "SelectedPropertyExpression",
    "SelectedPropertyMaxAggregation",
    "SelectedPropertyMinAggregation",
    "SelectedPropertyOperation",
    "SelectedPropertySumAggregation",
    "SharedPropertyType",
    "SharedPropertyTypeApiName",
    "SharedPropertyTypeRid",
    "StartsWithQuery",
    "StreamingOutputFormat",
    "StringLengthConstraint",
    "StringRegexMatchConstraint",
    "StructConstraint",
    "StructEvaluatedConstraint",
    "StructFieldApiName",
    "StructFieldEvaluatedConstraint",
    "StructFieldEvaluationResult",
    "StructFieldSelector",
    "StructFieldType",
    "StructFieldTypeRid",
    "StructParameterFieldApiName",
    "StructType",
    "SubmissionCriteriaEvaluation",
    "SubtractPropertyExpression",
    "SumAggregationV2",
    "SyncApplyActionResponseV2",
    "ThreeDimensionalAggregation",
    "TimeRange",
    "TimeSeriesAggregationMethod",
    "TimeSeriesAggregationStrategy",
    "TimeSeriesCumulativeAggregate",
    "TimeSeriesPeriodicAggregate",
    "TimeSeriesPoint",
    "TimeSeriesRollingAggregate",
    "TimeSeriesRollingAggregateWindow",
    "TimeSeriesWindowType",
    "TimeUnit",
    "TimeseriesEntry",
    "TransactionEdit",
    "TwoDimensionalAggregation",
    "UnevaluableConstraint",
    "UuidConstraint",
    "ValidateActionResponseV2",
    "ValidationResult",
    "ValueType",
    "ValueTypeApiName",
    "ValueTypeArrayType",
    "ValueTypeConstraint",
    "ValueTypeDecimalType",
    "ValueTypeFieldType",
    "ValueTypeMapType",
    "ValueTypeOptionalType",
    "ValueTypeReferenceType",
    "ValueTypeRid",
    "ValueTypeStatus",
    "ValueTypeStructField",
    "ValueTypeStructType",
    "ValueTypeUnionType",
    "VersionedQueryTypeApiName",
    "WildcardQuery",
    "WithinBoundingBoxPoint",
    "WithinBoundingBoxQuery",
    "WithinDistanceOfQuery",
    "WithinPolygonQuery",
]
