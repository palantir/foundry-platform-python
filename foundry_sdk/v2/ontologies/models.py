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


class AbsoluteTimeRange(pydantic.BaseModel):
    """ISO 8601 timestamps forming a range for a time series query. Start is inclusive and end is exclusive."""

    start_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("startTime"), default=None)  # type: ignore[literal-required]
    end_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("endTime"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["absolute"] = "absolute"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AbsoluteValuePropertyExpression(pydantic.BaseModel):
    """Calculates absolute value of a numeric value."""

    property: DerivedPropertyDefinition
    type: typing.Literal["absoluteValue"] = "absoluteValue"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ActionParameterArrayType(pydantic.BaseModel):
    """ActionParameterArrayType"""

    sub_type: ActionParameterType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class ActionParameterV2(pydantic.BaseModel):
    """Details about a parameter of an action."""

    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    data_type: ActionParameterType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    required: bool
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class ActionTypeV2(pydantic.BaseModel):
    """Represents an action type in the Ontology."""

    api_name: ActionTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    parameters: typing.Dict[ParameterId, ActionParameterV2]
    rid: ActionTypeRid
    operations: typing.List[LogicRule]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ActivePropertyTypeStatus(pydantic.BaseModel):
    """
    This status indicates that the PropertyType will not change on short notice and should thus be safe to use in
    user facing workflows.
    """

    type: typing.Literal["active"] = "active"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AddLink(pydantic.BaseModel):
    """AddLink"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object: LinkSideObject = pydantic.Field(alias=str("aSideObject"))  # type: ignore[literal-required]
    b_side_object: LinkSideObject = pydantic.Field(alias=str("bSideObject"))  # type: ignore[literal-required]
    type: typing.Literal["addLink"] = "addLink"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AddObject(pydantic.BaseModel):
    """AddObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    type: typing.Literal["addObject"] = "addObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AddPropertyExpression(pydantic.BaseModel):
    """Adds two or more numeric values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["add"] = "add"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AggregateObjectsResponseItemV2(pydantic.BaseModel):
    """AggregateObjectsResponseItemV2"""

    group: typing.Dict[AggregationGroupKeyV2, AggregationGroupValueV2]
    metrics: typing.List[AggregationMetricResultV2]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AggregateObjectsResponseV2(pydantic.BaseModel):
    """AggregateObjectsResponseV2"""

    excluded_items: typing.Optional[int] = pydantic.Field(alias=str("excludedItems"), default=None)  # type: ignore[literal-required]
    accuracy: AggregationAccuracy
    data: typing.List[AggregateObjectsResponseItemV2]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AggregateTimeSeries(pydantic.BaseModel):
    """AggregateTimeSeries"""

    method: TimeSeriesAggregationMethod
    strategy: TimeSeriesAggregationStrategy
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


AggregationAccuracy = typing.Literal["ACCURATE", "APPROXIMATE"]
"""AggregationAccuracy"""


AggregationAccuracyRequest = typing.Literal["REQUIRE_ACCURATE", "ALLOW_APPROXIMATE"]
"""AggregationAccuracyRequest"""


class AggregationDurationGroupingV2(pydantic.BaseModel):
    """
    Divides objects into groups according to an interval. Note that this grouping applies only on date and timestamp types.
    When grouping by `YEARS`, `QUARTERS`, `MONTHS`, or `WEEKS`, the `value` must be set to `1`.
    """

    field: PropertyApiName
    value: int
    unit: TimeUnit
    type: typing.Literal["duration"] = "duration"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AggregationExactGroupingV2(pydantic.BaseModel):
    """Divides objects into groups according to an exact value."""

    field: PropertyApiName
    max_group_count: typing.Optional[int] = pydantic.Field(alias=str("maxGroupCount"), default=None)  # type: ignore[literal-required]
    default_value: typing.Optional[str] = pydantic.Field(alias=str("defaultValue"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["exact"] = "exact"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AggregationFixedWidthGroupingV2(pydantic.BaseModel):
    """Divides objects into groups with the specified width."""

    field: PropertyApiName
    fixed_width: int = pydantic.Field(alias=str("fixedWidth"))  # type: ignore[literal-required]
    type: typing.Literal["fixedWidth"] = "fixedWidth"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class AggregationMetricResultV2(pydantic.BaseModel):
    """AggregationMetricResultV2"""

    name: str
    value: typing.Optional[typing.Any] = None
    """
    The value of the metric. This will be a double in the case of
    a numeric metric, or a date string in the case of a date metric.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AggregationRangeV2(pydantic.BaseModel):
    """Specifies a range from an inclusive start value to an exclusive end value."""

    start_value: typing.Any = pydantic.Field(alias=str("startValue"))  # type: ignore[literal-required]
    """Inclusive start."""

    end_value: typing.Any = pydantic.Field(alias=str("endValue"))  # type: ignore[literal-required]
    """Exclusive end."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AggregationRangesGroupingV2(pydantic.BaseModel):
    """Divides objects into groups according to specified ranges."""

    field: PropertyApiName
    ranges: typing.List[AggregationRangeV2]
    type: typing.Literal["ranges"] = "ranges"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class AndQueryV2(pydantic.BaseModel):
    """Returns objects where every query is satisfied."""

    value: typing.List[SearchJsonQueryV2]
    type: typing.Literal["and"] = "and"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ApplyActionMode = typing.Literal["VALIDATE_ONLY", "VALIDATE_AND_EXECUTE"]
"""ApplyActionMode"""


class ApplyActionRequestOptions(pydantic.BaseModel):
    """ApplyActionRequestOptions"""

    mode: typing.Optional[ApplyActionMode] = None
    return_edits: typing.Optional[ReturnEditsMode] = pydantic.Field(alias=str("returnEdits"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ApproximateDistinctAggregationV2(pydantic.BaseModel):
    """Computes an approximate number of distinct values for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["approximateDistinct"] = "approximateDistinct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ApproximatePercentileAggregationV2(pydantic.BaseModel):
    """Computes the approximate percentile value for the provided field. Requires Object Storage V2."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    approximate_percentile: float = pydantic.Field(alias=str("approximatePercentile"))  # type: ignore[literal-required]
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["approximatePercentile"] = "approximatePercentile"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ArraySizeConstraint(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ArtifactRepositoryRid = core.RID
"""ArtifactRepositoryRid"""


AttachmentMetadataResponse = typing_extensions.Annotated[
    typing.Union["AttachmentV2", "ListAttachmentsResponseV2"], pydantic.Field(discriminator="type")
]
"""The attachment metadata response"""


AttachmentRid = core.RID
"""The unique resource identifier of an attachment."""


class AttachmentV2(pydantic.BaseModel):
    """The representation of an attachment."""

    rid: AttachmentRid
    filename: core_models.Filename
    size_bytes: core_models.SizeBytes = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    media_type: core_models.MediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]
    type: typing.Literal["single"] = "single"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AvgAggregationV2(pydantic.BaseModel):
    """Computes the average value for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["avg"] = "avg"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


BatchActionObjectEdit = typing_extensions.Annotated[
    typing.Union["ModifyObject", AddObject, AddLink], pydantic.Field(discriminator="type")
]
"""BatchActionObjectEdit"""


class BatchActionObjectEdits(pydantic.BaseModel):
    """BatchActionObjectEdits"""

    edits: typing.List[BatchActionObjectEdit]
    added_object_count: int = pydantic.Field(alias=str("addedObjectCount"))  # type: ignore[literal-required]
    modified_objects_count: int = pydantic.Field(alias=str("modifiedObjectsCount"))  # type: ignore[literal-required]
    deleted_objects_count: int = pydantic.Field(alias=str("deletedObjectsCount"))  # type: ignore[literal-required]
    added_links_count: int = pydantic.Field(alias=str("addedLinksCount"))  # type: ignore[literal-required]
    deleted_links_count: int = pydantic.Field(alias=str("deletedLinksCount"))  # type: ignore[literal-required]
    type: typing.Literal["edits"] = "edits"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


BatchActionResults = typing_extensions.Annotated[
    typing.Union[BatchActionObjectEdits, "ObjectTypeEdits"], pydantic.Field(discriminator="type")
]
"""BatchActionResults"""


class BatchApplyActionRequestItem(pydantic.BaseModel):
    """BatchApplyActionRequestItem"""

    parameters: typing.Dict[ParameterId, typing.Optional[DataValue]]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class BatchApplyActionRequestOptions(pydantic.BaseModel):
    """BatchApplyActionRequestOptions"""

    return_edits: typing.Optional[BatchReturnEditsMode] = pydantic.Field(alias=str("returnEdits"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class BatchApplyActionResponseV2(pydantic.BaseModel):
    """BatchApplyActionResponseV2"""

    edits: typing.Optional[BatchActionResults] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


BatchReturnEditsMode = typing.Literal["ALL", "NONE"]
"""BatchReturnEditsMode"""


class BlueprintIcon(pydantic.BaseModel):
    """BlueprintIcon"""

    color: str
    """A hexadecimal color code."""

    name: str
    """
    The [name](https://blueprintjs.com/docs/#icons/icons-list) of the Blueprint icon. 
    Used to specify the Blueprint icon to represent the object type in a React app.
    """

    type: typing.Literal["blueprint"] = "blueprint"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class BoundingBoxValue(pydantic.BaseModel):
    """The top left and bottom right coordinate points that make up the bounding box."""

    top_left: WithinBoundingBoxPoint = pydantic.Field(alias=str("topLeft"))  # type: ignore[literal-required]
    bottom_right: WithinBoundingBoxPoint = pydantic.Field(alias=str("bottomRight"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class CenterPoint(pydantic.BaseModel):
    """The coordinate point to use as the center of the distance query."""

    center: CenterPointTypes
    distance: core_models.Distance
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ContainsAllTermsInOrderPrefixLastTerm(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ContainsAllTermsInOrderQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field contains all of the terms in the order provided,
    but they do have to be adjacent to each other. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: str
    type: typing.Literal["containsAllTermsInOrder"] = "containsAllTermsInOrder"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ContainsAllTermsQuery(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ContainsAnyTermQuery(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ContainsQueryV2(pydantic.BaseModel):
    """
    Returns objects where the specified array contains a value. Allows you to specify a property to query on by a
    variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["contains"] = "contains"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class CountAggregationV2(pydantic.BaseModel):
    """Computes the total count of objects."""

    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["count"] = "count"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class CountObjectsResponseV2(pydantic.BaseModel):
    """CountObjectsResponseV2"""

    count: typing.Optional[int] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class CreateInterfaceObjectRule(pydantic.BaseModel):
    """CreateInterfaceObjectRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["createInterfaceObject"] = "createInterfaceObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class CreateLinkRule(pydantic.BaseModel):
    """CreateLinkRule"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("aSideObjectTypeApiName"))  # type: ignore[literal-required]
    b_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("bSideObjectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["createLink"] = "createLink"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class CreateObjectRule(pydantic.BaseModel):
    """CreateObjectRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["createObject"] = "createObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class CreateTemporaryObjectSetResponseV2(pydantic.BaseModel):
    """CreateTemporaryObjectSetResponseV2"""

    object_set_rid: ObjectSetRid = pydantic.Field(alias=str("objectSetRid"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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
| Ontology Interface Object Reference | JSON encoding of the object's api name and primary key| `{"objectTypeApiName":"Employee", "primaryKeyValue":"EMP1234"}`                                                                                               |
| Ontology Object Type Reference      | string of the object type's api name                  | `"Employee"`                                                                                                                                                  |
| Set                                 | array                                                 | `["alpha", "bravo", "charlie"]`                                                                                                                               |
| Short                               | number                                                | `8739`                                                                                                                                                        |
| String                              | string                                                | `"Call me Ishmael"`                                                                                                                                           |
| Struct                              | JSON object                                           | `{"name": "John Doe", "age": 42}`                                                                                                                             |
| TwoDimensionalAggregation           | JSON object                                           | `{"groups": [{"key": "alpha", "value": 100}, {"key": "beta", "value": 101}]}`                                                                                 |
| ThreeDimensionalAggregation         | JSON object                                           | `{"groups": [{"key": "NYC", "groups": [{"key": "Engineer", "value" : 100}]}]}`                                                                                |
| Timestamp                           | ISO 8601 extended offset date-time string in UTC zone | `"2021-01-04T05:00:00Z"`                                                                                                                                      |
"""


class DecryptionResult(pydantic.BaseModel):
    """The result of a CipherText decryption. If successful, the plaintext decrypted value will be returned. Otherwise, an error will be thrown."""

    plaintext: typing.Optional[Plaintext] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class DeleteInterfaceObjectRule(pydantic.BaseModel):
    """DeleteInterfaceObjectRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteInterfaceObject"] = "deleteInterfaceObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class DeleteLink(pydantic.BaseModel):
    """DeleteLink"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object: LinkSideObject = pydantic.Field(alias=str("aSideObject"))  # type: ignore[literal-required]
    b_side_object: LinkSideObject = pydantic.Field(alias=str("bSideObject"))  # type: ignore[literal-required]
    type: typing.Literal["deleteLink"] = "deleteLink"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class DeleteLinkRule(pydantic.BaseModel):
    """DeleteLinkRule"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("aSideObjectTypeApiName"))  # type: ignore[literal-required]
    b_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("bSideObjectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteLink"] = "deleteLink"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class DeleteObject(pydantic.BaseModel):
    """DeleteObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    type: typing.Literal["deleteObject"] = "deleteObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class DeleteObjectRule(pydantic.BaseModel):
    """DeleteObjectRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteObject"] = "deleteObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class DeprecatedPropertyTypeStatus(pydantic.BaseModel):
    """
    This status indicates that the PropertyType is reaching the end of its life and will be removed as per the
    deadline specified.
    """

    message: str
    deadline: core.AwareDatetime
    replaced_by: typing.Optional[PropertyTypeRid] = pydantic.Field(alias=str("replacedBy"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["deprecated"] = "deprecated"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class DividePropertyExpression(pydantic.BaseModel):
    """Divides the left numeric value by the right numeric value."""

    left: DerivedPropertyDefinition
    right: DerivedPropertyDefinition
    type: typing.Literal["divide"] = "divide"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class DoesNotIntersectBoundingBoxQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field does not intersect the bounding box provided. Allows you to specify a
    property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not
    both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: BoundingBoxValue
    type: typing.Literal["doesNotIntersectBoundingBox"] = "doesNotIntersectBoundingBox"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class DoesNotIntersectPolygonQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field does not intersect the polygon provided. Allows you to specify a
    property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not
    both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PolygonValue
    type: typing.Literal["doesNotIntersectPolygon"] = "doesNotIntersectPolygon"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class DoubleVector(pydantic.BaseModel):
    """
    The vector to search with. The vector must be of the same dimension as the vectors stored in the provided
    propertyIdentifier.
    """

    value: typing.List[float]
    type: typing.Literal["vector"] = "vector"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class EntrySetType(pydantic.BaseModel):
    """EntrySetType"""

    key_type: QueryDataType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: QueryDataType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["entrySet"] = "entrySet"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class EqualsQueryV2(pydantic.BaseModel):
    """
    Returns objects where the specified field is equal to a value. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["eq"] = "eq"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ExactDistinctAggregationV2(pydantic.BaseModel):
    """Computes an exact number of distinct values for the provided field. May be slower than an approximate distinct aggregation. Requires Object Storage V2."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["exactDistinct"] = "exactDistinct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ExamplePropertyTypeStatus(pydantic.BaseModel):
    """
    This status indicates that the PropertyType is an example. It is backed by notional data that should not be
    used for actual workflows, but can be used to test those workflows.
    """

    type: typing.Literal["example"] = "example"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ExecuteQueryResponse(pydantic.BaseModel):
    """ExecuteQueryResponse"""

    value: DataValue
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ExperimentalPropertyTypeStatus(pydantic.BaseModel):
    """This status indicates that the PropertyType is in development."""

    type: typing.Literal["experimental"] = "experimental"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ExtractDatePart = typing.Literal["DAYS", "MONTHS", "QUARTERS", "YEARS"]
"""ExtractDatePart"""


class ExtractPropertyExpression(pydantic.BaseModel):
    """Extracts the specified date part from a date or timestamp."""

    property: DerivedPropertyDefinition
    part: ExtractDatePart
    type: typing.Literal["extract"] = "extract"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class GetSelectedPropertyOperation(pydantic.BaseModel):
    """
    Gets a single value of a property. Throws if the target object set is on the MANY side of the link and could
    explode the cardinality.

    Use collectList or collectSet which will return a list of values in that case.
    """

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["get"] = "get"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GreatestPropertyExpression(pydantic.BaseModel):
    """Finds greatest of two or more numeric, date or timestamp values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["greatest"] = "greatest"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GroupMemberConstraint(pydantic.BaseModel):
    """The parameter value must be the user id of a member belonging to at least one of the groups defined by the constraint."""

    type: typing.Literal["groupMember"] = "groupMember"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GtQueryV2(pydantic.BaseModel):
    """
    Returns objects where the specified field is greater than a value. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["gt"] = "gt"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GteQueryV2(pydantic.BaseModel):
    """
    Returns objects where the specified field is greater than or equal to a value. Allows you to specify a property
    to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["gte"] = "gte"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class InQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field equals any of the provided values. Allows you to
    specify a property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied,
    but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: typing.List[PropertyValue]
    type: typing.Literal["in"] = "in"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class InterfaceLinkType(pydantic.BaseModel):
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

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


InterfaceLinkTypeApiName = str
"""A string indicating the API name to use for the interface link."""


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


class InterfaceSharedPropertyType(pydantic.BaseModel):
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
    required: bool
    """Whether each implementing object type must declare an implementation for this property."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


InterfaceToObjectTypeMapping = typing.Dict["SharedPropertyTypeApiName", "PropertyApiName"]
"""Represents an implementation of an interface (the mapping of interface property to local property)."""


InterfaceToObjectTypeMappings = typing.Dict["ObjectTypeApiName", InterfaceToObjectTypeMapping]
"""Map from object type to the interface-to-object-type mapping for that object type."""


class InterfaceType(pydantic.BaseModel):
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

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


InterfaceTypeApiName = str
"""
The name of the interface type in the API in UpperCamelCase format. To find the API name for your interface
type, use the `List interface types` endpoint or check the **Ontology Manager**.
"""


InterfaceTypeRid = core.RID
"""The unique resource identifier of an interface, useful for interacting with other Foundry APIs."""


class IntersectsBoundingBoxQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field intersects the bounding box provided. Allows you to specify a property
    to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: BoundingBoxValue
    type: typing.Literal["intersectsBoundingBox"] = "intersectsBoundingBox"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class IntersectsPolygonQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field intersects the polygon provided. Allows you to specify a property to
    query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PolygonValue
    type: typing.Literal["intersectsPolygon"] = "intersectsPolygon"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class IsNullQueryV2(pydantic.BaseModel):
    """
    Returns objects based on the existence of the specified field. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: bool
    type: typing.Literal["isNull"] = "isNull"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LeastPropertyExpression(pydantic.BaseModel):
    """Finds least of two or more numeric, date or timestamp values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["least"] = "least"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LinkSideObject(pydantic.BaseModel):
    """LinkSideObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


LinkTypeApiName = str
"""
The name of the link type in the API. To find the API name for your Link Type, check the **Ontology Manager**
application.
"""


LinkTypeRid = core.RID
"""LinkTypeRid"""


LinkTypeSideCardinality = typing.Literal["ONE", "MANY"]
"""LinkTypeSideCardinality"""


class LinkTypeSideV2(pydantic.BaseModel):
    """LinkTypeSideV2"""

    api_name: LinkTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    cardinality: LinkTypeSideCardinality
    foreign_key_property_api_name: typing.Optional[PropertyApiName] = pydantic.Field(alias=str("foreignKeyPropertyApiName"), default=None)  # type: ignore[literal-required]
    link_type_rid: LinkTypeRid = pydantic.Field(alias=str("linkTypeRid"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LinkedInterfaceTypeApiName(pydantic.BaseModel):
    """A reference to the linked interface type."""

    api_name: InterfaceTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    type: typing.Literal["interfaceTypeApiName"] = "interfaceTypeApiName"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LinkedObjectTypeApiName(pydantic.BaseModel):
    """A reference to the linked object type."""

    api_name: ObjectTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    type: typing.Literal["objectTypeApiName"] = "objectTypeApiName"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListActionTypesResponseV2(pydantic.BaseModel):
    """ListActionTypesResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[ActionTypeV2]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListAttachmentsResponseV2(pydantic.BaseModel):
    """ListAttachmentsResponseV2"""

    data: typing.List[AttachmentV2]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["multiple"] = "multiple"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListInterfaceTypesResponse(pydantic.BaseModel):
    """ListInterfaceTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[InterfaceType]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListLinkedObjectsResponseV2(pydantic.BaseModel):
    """ListLinkedObjectsResponseV2"""

    data: typing.List[OntologyObjectV2]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListObjectTypesV2Response(pydantic.BaseModel):
    """ListObjectTypesV2Response"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[ObjectTypeV2]
    """The list of object types in the current page."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListObjectsResponseV2(pydantic.BaseModel):
    """ListObjectsResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[OntologyObjectV2]
    """The list of objects in the current page."""

    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListOntologiesV2Response(pydantic.BaseModel):
    """ListOntologiesV2Response"""

    data: typing.List[OntologyV2]
    """The list of Ontologies the user has access to."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListOutgoingLinkTypesResponseV2(pydantic.BaseModel):
    """ListOutgoingLinkTypesResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[LinkTypeSideV2]
    """The list of link type sides in the current page."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListQueryTypesResponseV2(pydantic.BaseModel):
    """ListQueryTypesResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[QueryTypeV2]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LoadObjectSetResponseV2(pydantic.BaseModel):
    """Represents the API response when loading an `ObjectSet`."""

    data: typing.List[OntologyObjectV2]
    """The list of objects in the current Page."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LoadObjectSetV2MultipleObjectTypesResponse(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LoadObjectSetV2ObjectsOrInterfacesResponse(pydantic.BaseModel):
    """
    Represents the API response when loading an `ObjectSet`. Objects in the returned set can either have properties
    defined by an interface that the objects belong to or properties defined by the object type of the object.
    """

    data: typing.List[OntologyObjectV2]
    """The list of objects in the current page."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class LtQueryV2(pydantic.BaseModel):
    """
    Returns objects where the specified field is less than a value. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["lt"] = "lt"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LteQueryV2(pydantic.BaseModel):
    """
    Returns objects where the specified field is less than or equal to a value. Allows you to specify a property to
    query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PropertyValue
    type: typing.Literal["lte"] = "lte"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MaxAggregationV2(pydantic.BaseModel):
    """Computes the maximum value for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["max"] = "max"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MediaMetadata(pydantic.BaseModel):
    """MediaMetadata"""

    path: typing.Optional[core_models.MediaItemPath] = None
    size_bytes: core_models.SizeBytes = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    media_type: core_models.MediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MinAggregationV2(pydantic.BaseModel):
    """Computes the minimum value for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["min"] = "min"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ModifyInterfaceObjectRule(pydantic.BaseModel):
    """ModifyInterfaceObjectRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["modifyInterfaceObject"] = "modifyInterfaceObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ModifyObject(pydantic.BaseModel):
    """ModifyObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    type: typing.Literal["modifyObject"] = "modifyObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ModifyObjectRule(pydantic.BaseModel):
    """ModifyObjectRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["modifyObject"] = "modifyObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MultiplyPropertyExpression(pydantic.BaseModel):
    """Multiplies two or more numeric values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["multiply"] = "multiply"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


NearestNeighborsQuery = typing_extensions.Annotated[
    typing.Union[DoubleVector, "NearestNeighborsQueryText"], pydantic.Field(discriminator="type")
]
"""
Queries support either a vector matching the embedding model defined on the property, or text that is 
automatically embedded.
"""


class NearestNeighborsQueryText(pydantic.BaseModel):
    """Automatically embed the text in a vector using the embedding model configured for the given propertyIdentifier."""

    value: str
    type: typing.Literal["text"] = "text"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class NegatePropertyExpression(pydantic.BaseModel):
    """Negates a numeric value."""

    property: DerivedPropertyDefinition
    type: typing.Literal["negate"] = "negate"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class NotQueryV2(pydantic.BaseModel):
    """Returns objects where the query is not satisfied."""

    value: SearchJsonQueryV2
    type: typing.Literal["not"] = "not"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ObjectEdit = typing_extensions.Annotated[
    typing.Union[ModifyObject, DeleteObject, AddObject, DeleteLink, AddLink],
    pydantic.Field(discriminator="type"),
]
"""ObjectEdit"""


class ObjectEdits(pydantic.BaseModel):
    """ObjectEdits"""

    edits: typing.List[ObjectEdit]
    added_object_count: int = pydantic.Field(alias=str("addedObjectCount"))  # type: ignore[literal-required]
    modified_objects_count: int = pydantic.Field(alias=str("modifiedObjectsCount"))  # type: ignore[literal-required]
    deleted_objects_count: int = pydantic.Field(alias=str("deletedObjectsCount"))  # type: ignore[literal-required]
    added_links_count: int = pydantic.Field(alias=str("addedLinksCount"))  # type: ignore[literal-required]
    deleted_links_count: int = pydantic.Field(alias=str("deletedLinksCount"))  # type: ignore[literal-required]
    type: typing.Literal["edits"] = "edits"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class ObjectPropertyValueConstraint(pydantic.BaseModel):
    """The parameter value must be a property value of an object found within an object set."""

    type: typing.Literal["objectPropertyValue"] = "objectPropertyValue"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectQueryResultConstraint(pydantic.BaseModel):
    """The parameter value must be the primary key of an object found within an object set."""

    type: typing.Literal["objectQueryResult"] = "objectQueryResult"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ObjectRid = core.RID
"""The unique resource identifier of an object, useful for interacting with other Foundry APIs."""


ObjectSet = typing_extensions.Annotated[
    typing.Union[
        "ObjectSetSearchAroundType",
        "ObjectSetStaticType",
        "ObjectSetIntersectionType",
        "ObjectSetWithPropertiesType",
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


class ObjectSetAsBaseObjectTypesType(pydantic.BaseModel):
    """
    Casts the objects in the object set to their base type and thus ensures objects are returned with all of their
    properties in the resulting object set, not just the properties that implement interface properties. This is
    currently unsupported and an exception will be thrown if used.
    """

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    type: typing.Literal["asBaseObjectTypes"] = "asBaseObjectTypes"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetAsTypeType(pydantic.BaseModel):
    """
    Casts an object set to a specified object type or interface type API name. Any object whose object type does
    not match the object type provided or implement the interface type provided will be dropped from the resulting
    object set. This is currently unsupported and an exception will be thrown if used.
    """

    entity_type: str = pydantic.Field(alias=str("entityType"))  # type: ignore[literal-required]
    """An object type or interface type API name."""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    type: typing.Literal["asType"] = "asType"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetBaseType(pydantic.BaseModel):
    """ObjectSetBaseType"""

    object_type: str = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    """The API name of the object type."""

    type: typing.Literal["base"] = "base"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetFilterType(pydantic.BaseModel):
    """ObjectSetFilterType"""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    where: SearchJsonQueryV2
    type: typing.Literal["filter"] = "filter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetInterfaceBaseType(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetIntersectionType(pydantic.BaseModel):
    """ObjectSetIntersectionType"""

    object_sets: typing.List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]
    type: typing.Literal["intersect"] = "intersect"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetMethodInputType(pydantic.BaseModel):
    """
    ObjectSet which is the root of a MethodObjectSet definition.

    This feature is experimental and not yet generally available.
    """

    type: typing.Literal["methodInput"] = "methodInput"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetNearestNeighborsType(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetReferenceType(pydantic.BaseModel):
    """ObjectSetReferenceType"""

    reference: ObjectSetRid
    type: typing.Literal["reference"] = "reference"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ObjectSetRid = core.RID
"""ObjectSetRid"""


class ObjectSetSearchAroundType(pydantic.BaseModel):
    """ObjectSetSearchAroundType"""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    link: LinkTypeApiName
    type: typing.Literal["searchAround"] = "searchAround"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetStaticType(pydantic.BaseModel):
    """ObjectSetStaticType"""

    objects: typing.List[ObjectRid]
    type: typing.Literal["static"] = "static"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetSubtractType(pydantic.BaseModel):
    """ObjectSetSubtractType"""

    object_sets: typing.List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]
    type: typing.Literal["subtract"] = "subtract"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetUnionType(pydantic.BaseModel):
    """ObjectSetUnionType"""

    object_sets: typing.List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]
    type: typing.Literal["union"] = "union"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectSetWithPropertiesType(pydantic.BaseModel):
    """
    ObjectSet which returns objects with additional derived properties.

    This feature is experimental and not yet generally available.
    """

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    derived_properties: typing.Dict[DerivedPropertyApiName, DerivedPropertyDefinition] = pydantic.Field(alias=str("derivedProperties"))  # type: ignore[literal-required]
    """Map of the name of the derived property to return and its definition"""

    type: typing.Literal["withProperties"] = "withProperties"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ObjectTypeApiName = str
"""
The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the
`List object types` endpoint or check the **Ontology Manager**.
"""


class ObjectTypeEdits(pydantic.BaseModel):
    """ObjectTypeEdits"""

    edited_object_types: typing.List[ObjectTypeApiName] = pydantic.Field(alias=str("editedObjectTypes"))  # type: ignore[literal-required]
    type: typing.Literal["largeScaleEdits"] = "largeScaleEdits"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectTypeFullMetadata(pydantic.BaseModel):
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

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ObjectTypeId = str
"""The unique identifier (ID) for an object type. This can be viewed in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/)."""


class ObjectTypeInterfaceImplementation(pydantic.BaseModel):
    """ObjectTypeInterfaceImplementation"""

    properties: typing.Dict[SharedPropertyTypeApiName, PropertyApiName]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ObjectTypeRid = core.RID
"""The unique resource identifier of an object type, useful for interacting with other Foundry APIs."""


class ObjectTypeV2(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ObjectTypeVisibility = typing.Literal["NORMAL", "PROMINENT", "HIDDEN"]
"""The suggested visibility of the object type."""


class OneOfConstraint(pydantic.BaseModel):
    """The parameter has a manually predefined set of options."""

    options: typing.List[ParameterOption]
    other_values_allowed: bool = pydantic.Field(alias=str("otherValuesAllowed"))  # type: ignore[literal-required]
    """A flag denoting whether custom, user provided values will be considered valid. This is configured via the **Allowed "Other" value** toggle in the **Ontology Manager**."""

    type: typing.Literal["oneOf"] = "oneOf"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


OntologyApiName = str
"""OntologyApiName"""


class OntologyArrayType(pydantic.BaseModel):
    """OntologyArrayType"""

    item_type: OntologyDataType = pydantic.Field(alias=str("itemType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class OntologyFullMetadata(pydantic.BaseModel):
    """OntologyFullMetadata"""

    ontology: OntologyV2
    object_types: typing.Dict[ObjectTypeApiName, ObjectTypeFullMetadata] = pydantic.Field(alias=str("objectTypes"))  # type: ignore[literal-required]
    action_types: typing.Dict[ActionTypeApiName, ActionTypeV2] = pydantic.Field(alias=str("actionTypes"))  # type: ignore[literal-required]
    query_types: typing.Dict[VersionedQueryTypeApiName, QueryTypeV2] = pydantic.Field(alias=str("queryTypes"))  # type: ignore[literal-required]
    interface_types: typing.Dict[InterfaceTypeApiName, InterfaceType] = pydantic.Field(alias=str("interfaceTypes"))  # type: ignore[literal-required]
    shared_property_types: typing.Dict[SharedPropertyTypeApiName, SharedPropertyType] = pydantic.Field(alias=str("sharedPropertyTypes"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


OntologyIdentifier = str
"""Either an ontology rid or an ontology api name."""


class OntologyInterfaceObjectType(pydantic.BaseModel):
    """OntologyInterfaceObjectType"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["interfaceObject"] = "interfaceObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class OntologyMapType(pydantic.BaseModel):
    """OntologyMapType"""

    key_type: OntologyDataType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: OntologyDataType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class OntologyObjectArrayType(pydantic.BaseModel):
    """OntologyObjectArrayType"""

    sub_type: ObjectPropertyType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class OntologyObjectSetType(pydantic.BaseModel):
    """OntologyObjectSetType"""

    object_api_name: typing.Optional[ObjectTypeApiName] = pydantic.Field(alias=str("objectApiName"), default=None)  # type: ignore[literal-required]
    object_type_api_name: typing.Optional[ObjectTypeApiName] = pydantic.Field(alias=str("objectTypeApiName"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["objectSet"] = "objectSet"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class OntologyObjectType(pydantic.BaseModel):
    """OntologyObjectType"""

    object_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectApiName"))  # type: ignore[literal-required]
    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["object"] = "object"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class OntologyObjectTypeReferenceType(pydantic.BaseModel):
    """OntologyObjectTypeReferenceType"""

    type: typing.Literal["objectType"] = "objectType"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


OntologyObjectV2 = typing.Dict["PropertyApiName", "PropertyValue"]
"""Represents an object in the Ontology."""


OntologyRid = core.RID
"""
The unique Resource Identifier (RID) of the Ontology. To look up your Ontology RID, please use the
`List ontologies` endpoint or check the **Ontology Manager**.
"""


class OntologySetType(pydantic.BaseModel):
    """OntologySetType"""

    item_type: OntologyDataType = pydantic.Field(alias=str("itemType"))  # type: ignore[literal-required]
    type: typing.Literal["set"] = "set"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class OntologyStructField(pydantic.BaseModel):
    """OntologyStructField"""

    name: core_models.StructFieldName
    field_type: OntologyDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    required: bool
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class OntologyStructType(pydantic.BaseModel):
    """OntologyStructType"""

    fields: typing.List[OntologyStructField]
    type: typing.Literal["struct"] = "struct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class OntologyV2(pydantic.BaseModel):
    """Metadata about an Ontology."""

    api_name: OntologyApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: str
    rid: OntologyRid
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class OrQueryV2(pydantic.BaseModel):
    """Returns objects where at least 1 query is satisfied."""

    value: typing.List[SearchJsonQueryV2]
    type: typing.Literal["or"] = "or"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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
        OneOfConstraint,
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


class ParameterEvaluationResult(pydantic.BaseModel):
    """Represents the validity of a parameter against the configured constraints."""

    result: ValidationResult
    evaluated_constraints: typing.List[ParameterEvaluatedConstraint] = pydantic.Field(alias=str("evaluatedConstraints"))  # type: ignore[literal-required]
    required: bool
    """Represents whether the parameter is a required input to the action."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ParameterId = str
"""
The unique identifier of the parameter. Parameters are used as inputs when an action or query is applied.
Parameters can be viewed and managed in the **Ontology Manager**.
"""


class ParameterOption(pydantic.BaseModel):
    """A possible value for the parameter. This is defined in the **Ontology Manager** by Actions admins."""

    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    value: typing.Optional[typing.Any] = None
    """An allowed configured value for a parameter within an action."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


Plaintext = str
"""Plaintext"""


class PreciseDuration(pydantic.BaseModel):
    """A measurement of duration."""

    value: int
    """The duration value."""

    unit: PreciseTimeUnit
    type: typing.Literal["duration"] = "duration"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


PreciseTimeUnit = typing.Literal["NANOSECONDS", "SECONDS", "MINUTES", "HOURS", "DAYS", "WEEKS"]
"""The unit of a fixed-width duration. Each day is 24 hours and each week is 7 days."""


PrimaryKeyValue = typing.Any
"""Represents the primary key value that is used as a unique identifier for an object."""


PropertyApiName = str
"""
The name of the property in the API. To find the API name for your property, use the `Get object type`
endpoint or check the **Ontology Manager**.
"""


class PropertyApiNameSelector(pydantic.BaseModel):
    """A property api name that references properties to query on."""

    api_name: PropertyApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    type: typing.Literal["property"] = "property"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class PropertyV2(pydantic.BaseModel):
    """Details about some property of an object."""

    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    rid: PropertyTypeRid
    status: typing.Optional[PropertyTypeStatus] = None
    visibility: typing.Optional[PropertyTypeVisibility] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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
        OntologyObjectType,
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Query parameters or outputs."""


class QueryParameterV2(pydantic.BaseModel):
    """Details about a parameter of a query."""

    description: typing.Optional[str] = None
    data_type: QueryDataType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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

    name: core_models.StructFieldName
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


class QueryTypeV2(pydantic.BaseModel):
    """Represents a query type in the Ontology."""

    api_name: QueryApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, QueryParameterV2]
    output: QueryDataType
    rid: FunctionRid
    version: FunctionVersion
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


class RangeConstraint(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class RelativeTime(pydantic.BaseModel):
    """A relative time, such as "3 days before" or "2 hours after" the current moment."""

    when: RelativeTimeRelation
    value: int
    unit: RelativeTimeSeriesTimeUnit
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class RelativeTimeRange(pydantic.BaseModel):
    """A relative time range for a time series query."""

    start_time: typing.Optional[RelativeTime] = pydantic.Field(alias=str("startTime"), default=None)  # type: ignore[literal-required]
    end_time: typing.Optional[RelativeTime] = pydantic.Field(alias=str("endTime"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["relative"] = "relative"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


RelativeTimeRelation = typing.Literal["BEFORE", "AFTER"]
"""RelativeTimeRelation"""


RelativeTimeSeriesTimeUnit = typing.Literal[
    "MILLISECONDS", "SECONDS", "MINUTES", "HOURS", "DAYS", "WEEKS", "MONTHS", "YEARS"
]
"""RelativeTimeSeriesTimeUnit"""


ReturnEditsMode = typing.Literal["ALL", "ALL_V2_WITH_DELETIONS", "NONE"]
"""ReturnEditsMode"""


class RollingAggregateWindowPoints(pydantic.BaseModel):
    """Number of points in each window."""

    count: int
    type: typing.Literal["pointsCount"] = "pointsCount"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class SearchObjectsResponseV2(pydantic.BaseModel):
    """SearchObjectsResponseV2"""

    data: typing.List[OntologyObjectV2]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


SearchOrderByType = typing.Literal["fields", "relevance"]
"""SearchOrderByType"""


class SearchOrderByV2(pydantic.BaseModel):
    """Specifies the ordering of search results by a field and an ordering direction or by relevance if scores are required in a nearestNeighbors query. By default `orderType` is set to `fields`."""

    order_type: typing.Optional[SearchOrderByType] = pydantic.Field(alias=str("orderType"), default=None)  # type: ignore[literal-required]
    fields: typing.List[SearchOrderingV2]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SearchOrderingV2(pydantic.BaseModel):
    """SearchOrderingV2"""

    field: PropertyApiName
    direction: typing.Optional[str] = None
    """Specifies the ordering direction (can be either `asc` or `desc`)"""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class SelectedPropertyApproximateDistinctAggregation(pydantic.BaseModel):
    """Computes an approximate number of distinct values for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["approximateDistinct"] = "approximateDistinct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SelectedPropertyApproximatePercentileAggregation(pydantic.BaseModel):
    """Computes the approximate percentile value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    approximate_percentile: float = pydantic.Field(alias=str("approximatePercentile"))  # type: ignore[literal-required]
    type: typing.Literal["approximatePercentile"] = "approximatePercentile"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SelectedPropertyAvgAggregation(pydantic.BaseModel):
    """Computes the average value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["avg"] = "avg"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SelectedPropertyCollectListAggregation(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SelectedPropertyCollectSetAggregation(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SelectedPropertyCountAggregation(pydantic.BaseModel):
    """Computes the total count of objects."""

    type: typing.Literal["count"] = "count"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SelectedPropertyExactDistinctAggregation(pydantic.BaseModel):
    """Computes an exact number of distinct values for the provided field. May be slower than an approximate distinct aggregation."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["exactDistinct"] = "exactDistinct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SelectedPropertyExpression(pydantic.BaseModel):
    """Definition for a selected property over a MethodObjectSet."""

    object_set: MethodObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    operation: SelectedPropertyOperation
    type: typing.Literal["selection"] = "selection"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SelectedPropertyMaxAggregation(pydantic.BaseModel):
    """Computes the maximum value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["max"] = "max"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SelectedPropertyMinAggregation(pydantic.BaseModel):
    """Computes the minimum value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["min"] = "min"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class SelectedPropertySumAggregation(pydantic.BaseModel):
    """Computes the sum of values for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["sum"] = "sum"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SharedPropertyType(pydantic.BaseModel):
    """A property type that can be shared across object types."""

    rid: SharedPropertyTypeRid
    api_name: SharedPropertyTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """A short text that describes the SharedPropertyType."""

    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


SharedPropertyTypeApiName = str
"""
The name of the shared property type in the API in lowerCamelCase format. To find the API name for your
shared property type, use the `List shared property types` endpoint or check the **Ontology Manager**.
"""


SharedPropertyTypeRid = core.RID
"""The unique resource identifier of an shared property type, useful for interacting with other Foundry APIs."""


class StartsWithQuery(pydantic.BaseModel):
    """
    Deprecated alias for `containsAllTermsInOrderPrefixLastTerm`, which is preferred because the name `startsWith` is misleading.
    Returns objects where the specified field starts with the provided value. Allows you to specify a property to
    query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: str
    type: typing.Literal["startsWith"] = "startsWith"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


StreamingOutputFormat = typing.Literal["JSON", "ARROW"]
"""
Which format to serialize the binary stream in.
ARROW is more efficient for streaming a large sized response.
"""


class StringLengthConstraint(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class StringRegexMatchConstraint(pydantic.BaseModel):
    """The parameter value must match a predefined regular expression."""

    regex: str
    """The regular expression configured in the **Ontology Manager**."""

    configured_failure_message: typing.Optional[str] = pydantic.Field(alias=str("configuredFailureMessage"), default=None)  # type: ignore[literal-required]
    """
    The message indicating that the regular expression was not matched.
    This is configured per parameter in the **Ontology Manager**.
    """

    type: typing.Literal["stringRegexMatch"] = "stringRegexMatch"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


StructFieldApiName = str
"""The name of a struct field in the Ontology."""


class StructFieldSelector(pydantic.BaseModel):
    """
    A combination of a property API name and a struct field API name used to select struct fields. Note that you can
    still select struct properties with only a 'PropertyApiNameSelector'; the queries will then become 'OR' queries
    across the fields of the struct property, and derived property expressions will operate on the whole struct
    where applicable.
    """

    property_api_name: PropertyApiName = pydantic.Field(alias=str("propertyApiName"))  # type: ignore[literal-required]
    struct_field_api_name: StructFieldApiName = pydantic.Field(alias=str("structFieldApiName"))  # type: ignore[literal-required]
    type: typing.Literal["structField"] = "structField"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class StructFieldType(pydantic.BaseModel):
    """StructFieldType"""

    api_name: StructFieldApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class StructType(pydantic.BaseModel):
    """StructType"""

    struct_field_types: typing.List[StructFieldType] = pydantic.Field(alias=str("structFieldTypes"))  # type: ignore[literal-required]
    type: typing.Literal["struct"] = "struct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SubmissionCriteriaEvaluation(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SubtractPropertyExpression(pydantic.BaseModel):
    """Subtracts the right numeric value from the left numeric value."""

    left: DerivedPropertyDefinition
    right: DerivedPropertyDefinition
    type: typing.Literal["subtract"] = "subtract"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SumAggregationV2(pydantic.BaseModel):
    """Computes the sum of values for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["sum"] = "sum"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SyncApplyActionResponseV2(pydantic.BaseModel):
    """SyncApplyActionResponseV2"""

    validation: typing.Optional[ValidateActionResponseV2] = None
    edits: typing.Optional[ActionResults] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ThreeDimensionalAggregation(pydantic.BaseModel):
    """ThreeDimensionalAggregation"""

    key_type: QueryAggregationKeyType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: TwoDimensionalAggregation = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["threeDimensionalAggregation"] = "threeDimensionalAggregation"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class TimeSeriesCumulativeAggregate(pydantic.BaseModel):
    """
    The cumulative aggregate is calculated progressively for each point in the input time series,
    considering all preceding points up to and including the current point.
    """

    type: typing.Literal["cumulative"] = "cumulative"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class TimeSeriesPeriodicAggregate(pydantic.BaseModel):
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class TimeSeriesPoint(pydantic.BaseModel):
    """A time and value pair."""

    time: core.AwareDatetime
    """An ISO 8601 timestamp"""

    value: typing.Any
    """An object which is either an enum String or a double number."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class TimeSeriesRollingAggregate(pydantic.BaseModel):
    """TimeSeriesRollingAggregate"""

    window_size: TimeSeriesRollingAggregateWindow = pydantic.Field(alias=str("windowSize"))  # type: ignore[literal-required]
    type: typing.Literal["rolling"] = "rolling"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


class TimeseriesEntry(pydantic.BaseModel):
    """A time and value pair."""

    time: core.AwareDatetime
    """An ISO 8601 timestamp"""

    value: typing.Any
    """An object which is either an enum String, double number, or a geopoint."""

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


class UnevaluableConstraint(pydantic.BaseModel):
    """
    The parameter cannot be evaluated because it depends on another parameter or object set that can't be evaluated.
    This can happen when a parameter's allowed values are defined by another parameter that is missing or invalid.
    """

    type: typing.Literal["unevaluable"] = "unevaluable"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ValidateActionResponseV2(pydantic.BaseModel):
    """ValidateActionResponseV2"""

    result: ValidationResult
    submission_criteria: typing.List[SubmissionCriteriaEvaluation] = pydantic.Field(alias=str("submissionCriteria"))  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, ParameterEvaluationResult]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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


VersionedQueryTypeApiName = str
"""
The name of the Query in the API and an optional version identifier separated by a colon.
If the API name contains a colon, then a version identifier of either "latest" or a semantic version must
be included.
If the API does not contain a colon, then either the version identifier must be excluded or a version
identifier of a semantic version must be included.
Examples: 'myGroup:myFunction:latest', 'myGroup:myFunction:1.0.0', 'myFunction', 'myFunction:2.0.0'
"""


class WithinBoundingBoxQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field contains a point within the bounding box provided. Allows you to
    specify a property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied,
    but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: BoundingBoxValue
    type: typing.Literal["withinBoundingBox"] = "withinBoundingBox"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class WithinDistanceOfQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field contains a point within the distance provided of the center point.
    Allows you to specify a property to query on by a variety of means. Either `field` or `propertyIdentifier`
    must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: CenterPoint
    type: typing.Literal["withinDistanceOf"] = "withinDistanceOf"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class WithinPolygonQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field contains a point within the polygon provided. Allows you to specify a
    property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not
    both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: PolygonValue
    type: typing.Literal["withinPolygon"] = "withinPolygon"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


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
core.resolve_forward_references(TimeRange, globalns=globals(), localns=locals())
core.resolve_forward_references(TimeSeriesAggregationStrategy, globalns=globals(), localns=locals())
core.resolve_forward_references(
    TimeSeriesRollingAggregateWindow, globalns=globals(), localns=locals()
)

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
    "AddObject",
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
    "DeleteLinkRule",
    "DeleteObject",
    "DeleteObjectRule",
    "DeprecatedPropertyTypeStatus",
    "DerivedPropertyApiName",
    "DerivedPropertyDefinition",
    "DividePropertyExpression",
    "DoesNotIntersectBoundingBoxQuery",
    "DoesNotIntersectPolygonQuery",
    "DoubleVector",
    "EntrySetType",
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
    "LinkSideObject",
    "LinkTypeApiName",
    "LinkTypeRid",
    "LinkTypeSideCardinality",
    "LinkTypeSideV2",
    "LinkedInterfaceTypeApiName",
    "LinkedObjectTypeApiName",
    "ListActionTypesResponseV2",
    "ListAttachmentsResponseV2",
    "ListInterfaceTypesResponse",
    "ListLinkedObjectsResponseV2",
    "ListObjectTypesV2Response",
    "ListObjectsResponseV2",
    "ListOntologiesV2Response",
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
    "ModifyObjectRule",
    "MultiplyPropertyExpression",
    "NearestNeighborsQuery",
    "NearestNeighborsQueryText",
    "NegatePropertyExpression",
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
    "OntologyV2",
    "OrQueryV2",
    "OrderBy",
    "OrderByDirection",
    "ParameterEvaluatedConstraint",
    "ParameterEvaluationResult",
    "ParameterId",
    "ParameterOption",
    "Plaintext",
    "PolygonValue",
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
    "QueryTypeV2",
    "QueryUnionType",
    "RangeConstraint",
    "RelativeTime",
    "RelativeTimeRange",
    "RelativeTimeRelation",
    "RelativeTimeSeriesTimeUnit",
    "ReturnEditsMode",
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
    "StructFieldApiName",
    "StructFieldSelector",
    "StructFieldType",
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
    "TwoDimensionalAggregation",
    "UnevaluableConstraint",
    "ValidateActionResponseV2",
    "ValidationResult",
    "ValueType",
    "VersionedQueryTypeApiName",
    "WithinBoundingBoxPoint",
    "WithinBoundingBoxQuery",
    "WithinDistanceOfQuery",
    "WithinPolygonQuery",
]
