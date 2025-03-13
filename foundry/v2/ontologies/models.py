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
from datetime import datetime

import pydantic
import typing_extensions

from foundry import _core as core


class AbsoluteTimeRange(pydantic.BaseModel):
    """ISO 8601 timestamps forming a range for a time series query. Start is inclusive and end is exclusive."""

    start_time: typing.Optional[datetime] = pydantic.Field(alias=str("startTime"), default=None)  # type: ignore[literal-required]
    end_time: typing.Optional[datetime] = pydantic.Field(alias=str("endTime"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["absolute"] = "absolute"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AbsoluteTimeRangeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AbsoluteTimeRangeDict, self.model_dump(by_alias=True, exclude_none=True))


class AbsoluteTimeRangeDict(typing_extensions.TypedDict):
    """ISO 8601 timestamps forming a range for a time series query. Start is inclusive and end is exclusive."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    startTime: typing_extensions.NotRequired[datetime]
    endTime: typing_extensions.NotRequired[datetime]
    type: typing.Literal["absolute"]


class AbsoluteValuePropertyExpression(pydantic.BaseModel):
    """Calculates absolute value of a numeric value."""

    property: DerivedPropertyDefinition
    type: typing.Literal["absoluteValue"] = "absoluteValue"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AbsoluteValuePropertyExpressionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AbsoluteValuePropertyExpressionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AbsoluteValuePropertyExpressionDict(typing_extensions.TypedDict):
    """Calculates absolute value of a numeric value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    property: DerivedPropertyDefinitionDict
    type: typing.Literal["absoluteValue"]


class ActionParameterArrayType(pydantic.BaseModel):
    """ActionParameterArrayType"""

    sub_type: ActionParameterType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ActionParameterArrayTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ActionParameterArrayTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ActionParameterArrayTypeDict(typing_extensions.TypedDict):
    """ActionParameterArrayType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: ActionParameterTypeDict
    type: typing.Literal["array"]


ActionParameterType = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateType",
        "OntologyInterfaceObjectType",
        "OntologyStructType",
        "core_models.StringType",
        "core_models.DoubleType",
        "core_models.IntegerType",
        "core_models.LongType",
        "OntologyObjectTypeReferenceType",
        "core_models.BooleanType",
        "core_models.MarkingType",
        "core_models.AttachmentType",
        "core_models.MediaReferenceType",
        "ActionParameterArrayType",
        "OntologyObjectSetType",
        "OntologyObjectType",
        "core_models.TimestampType",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Action parameters."""


ActionParameterTypeDict = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateTypeDict",
        "OntologyInterfaceObjectTypeDict",
        "OntologyStructTypeDict",
        "core_models.StringTypeDict",
        "core_models.DoubleTypeDict",
        "core_models.IntegerTypeDict",
        "core_models.LongTypeDict",
        "OntologyObjectTypeReferenceTypeDict",
        "core_models.BooleanTypeDict",
        "core_models.MarkingTypeDict",
        "core_models.AttachmentTypeDict",
        "core_models.MediaReferenceTypeDict",
        "ActionParameterArrayTypeDict",
        "OntologyObjectSetTypeDict",
        "OntologyObjectTypeDict",
        "core_models.TimestampTypeDict",
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

    def to_dict(self) -> "ActionParameterV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ActionParameterV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class ActionParameterV2Dict(typing_extensions.TypedDict):
    """Details about a parameter of an action."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    displayName: core_models.DisplayName
    description: typing_extensions.NotRequired[str]
    dataType: ActionParameterTypeDict
    required: bool


ActionResults = typing_extensions.Annotated[
    typing.Union["ObjectEdits", "ObjectTypeEdits"], pydantic.Field(discriminator="type")
]
"""ActionResults"""


ActionResultsDict = typing_extensions.Annotated[
    typing.Union["ObjectEditsDict", "ObjectTypeEditsDict"], pydantic.Field(discriminator="type")
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

    def to_dict(self) -> "ActionTypeV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ActionTypeV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class ActionTypeV2Dict(typing_extensions.TypedDict):
    """Represents an action type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: ActionTypeApiName
    description: typing_extensions.NotRequired[str]
    displayName: typing_extensions.NotRequired[core_models.DisplayName]
    status: core_models.ReleaseStatus
    parameters: typing.Dict[ParameterId, ActionParameterV2Dict]
    rid: ActionTypeRid
    operations: typing.List[LogicRuleDict]


class ActivePropertyTypeStatus(pydantic.BaseModel):
    """
    This status indicates that the PropertyType will not change on short notice and should thus be safe to use in
    user facing workflows.
    """

    type: typing.Literal["active"] = "active"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ActivePropertyTypeStatusDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ActivePropertyTypeStatusDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ActivePropertyTypeStatusDict(typing_extensions.TypedDict):
    """
    This status indicates that the PropertyType will not change on short notice and should thus be safe to use in
    user facing workflows.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["active"]


class AddLink(pydantic.BaseModel):
    """AddLink"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object: LinkSideObject = pydantic.Field(alias=str("aSideObject"))  # type: ignore[literal-required]
    b_side_object: LinkSideObject = pydantic.Field(alias=str("bSideObject"))  # type: ignore[literal-required]
    type: typing.Literal["addLink"] = "addLink"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AddLinkDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AddLinkDict, self.model_dump(by_alias=True, exclude_none=True))


class AddLinkDict(typing_extensions.TypedDict):
    """AddLink"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    linkTypeApiNameAtoB: LinkTypeApiName
    linkTypeApiNameBtoA: LinkTypeApiName
    aSideObject: LinkSideObjectDict
    bSideObject: LinkSideObjectDict
    type: typing.Literal["addLink"]


class AddObject(pydantic.BaseModel):
    """AddObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    type: typing.Literal["addObject"] = "addObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AddObjectDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AddObjectDict, self.model_dump(by_alias=True, exclude_none=True))


class AddObjectDict(typing_extensions.TypedDict):
    """AddObject"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKey: PropertyValue
    objectType: ObjectTypeApiName
    type: typing.Literal["addObject"]


class AddPropertyExpression(pydantic.BaseModel):
    """Adds two or more numeric values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["add"] = "add"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AddPropertyExpressionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AddPropertyExpressionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AddPropertyExpressionDict(typing_extensions.TypedDict):
    """Adds two or more numeric values."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    properties: typing.List[DerivedPropertyDefinitionDict]
    type: typing.Literal["add"]


class AggregateObjectsResponseItemV2(pydantic.BaseModel):
    """AggregateObjectsResponseItemV2"""

    group: typing.Dict[AggregationGroupKeyV2, AggregationGroupValueV2]
    metrics: typing.List[AggregationMetricResultV2]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregateObjectsResponseItemV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregateObjectsResponseItemV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregateObjectsResponseItemV2Dict(typing_extensions.TypedDict):
    """AggregateObjectsResponseItemV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    group: typing.Dict[AggregationGroupKeyV2, AggregationGroupValueV2]
    metrics: typing.List[AggregationMetricResultV2Dict]


class AggregateObjectsResponseV2(pydantic.BaseModel):
    """AggregateObjectsResponseV2"""

    excluded_items: typing.Optional[int] = pydantic.Field(alias=str("excludedItems"), default=None)  # type: ignore[literal-required]
    accuracy: AggregationAccuracy
    data: typing.List[AggregateObjectsResponseItemV2]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregateObjectsResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregateObjectsResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregateObjectsResponseV2Dict(typing_extensions.TypedDict):
    """AggregateObjectsResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    excludedItems: typing_extensions.NotRequired[int]
    accuracy: AggregationAccuracy
    data: typing.List[AggregateObjectsResponseItemV2Dict]


class AggregateTimeSeries(pydantic.BaseModel):
    """AggregateTimeSeries"""

    method: TimeSeriesAggregationMethod
    strategy: TimeSeriesAggregationStrategy
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregateTimeSeriesDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregateTimeSeriesDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregateTimeSeriesDict(typing_extensions.TypedDict):
    """AggregateTimeSeries"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    method: TimeSeriesAggregationMethod
    strategy: TimeSeriesAggregationStrategyDict


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

    def to_dict(self) -> "AggregationDurationGroupingV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregationDurationGroupingV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregationDurationGroupingV2Dict(typing_extensions.TypedDict):
    """
    Divides objects into groups according to an interval. Note that this grouping applies only on date and timestamp types.
    When grouping by `YEARS`, `QUARTERS`, `MONTHS`, or `WEEKS`, the `value` must be set to `1`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    value: int
    unit: TimeUnit
    type: typing.Literal["duration"]


class AggregationExactGroupingV2(pydantic.BaseModel):
    """Divides objects into groups according to an exact value."""

    field: PropertyApiName
    max_group_count: typing.Optional[int] = pydantic.Field(alias=str("maxGroupCount"), default=None)  # type: ignore[literal-required]
    default_value: typing.Optional[str] = pydantic.Field(alias=str("defaultValue"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["exact"] = "exact"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregationExactGroupingV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregationExactGroupingV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregationExactGroupingV2Dict(typing_extensions.TypedDict):
    """Divides objects into groups according to an exact value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    maxGroupCount: typing_extensions.NotRequired[int]
    defaultValue: typing_extensions.NotRequired[str]
    type: typing.Literal["exact"]


class AggregationFixedWidthGroupingV2(pydantic.BaseModel):
    """Divides objects into groups with the specified width."""

    field: PropertyApiName
    fixed_width: int = pydantic.Field(alias=str("fixedWidth"))  # type: ignore[literal-required]
    type: typing.Literal["fixedWidth"] = "fixedWidth"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregationFixedWidthGroupingV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregationFixedWidthGroupingV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregationFixedWidthGroupingV2Dict(typing_extensions.TypedDict):
    """Divides objects into groups with the specified width."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    fixedWidth: int
    type: typing.Literal["fixedWidth"]


AggregationGroupByV2 = typing_extensions.Annotated[
    typing.Union[
        "AggregationDurationGroupingV2",
        "AggregationFixedWidthGroupingV2",
        "AggregationRangesGroupingV2",
        "AggregationExactGroupingV2",
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies a grouping for aggregation results."""


AggregationGroupByV2Dict = typing_extensions.Annotated[
    typing.Union[
        "AggregationDurationGroupingV2Dict",
        "AggregationFixedWidthGroupingV2Dict",
        "AggregationRangesGroupingV2Dict",
        "AggregationExactGroupingV2Dict",
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

    def to_dict(self) -> "AggregationMetricResultV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregationMetricResultV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregationMetricResultV2Dict(typing_extensions.TypedDict):
    """AggregationMetricResultV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: str
    value: typing_extensions.NotRequired[typing.Any]
    """
    The value of the metric. This will be a double in the case of
    a numeric metric, or a date string in the case of a date metric.
    """


class AggregationRangeV2(pydantic.BaseModel):
    """Specifies a range from an inclusive start value to an exclusive end value."""

    start_value: typing.Any = pydantic.Field(alias=str("startValue"))  # type: ignore[literal-required]
    """Inclusive start."""

    end_value: typing.Any = pydantic.Field(alias=str("endValue"))  # type: ignore[literal-required]
    """Exclusive end."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregationRangeV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregationRangeV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregationRangeV2Dict(typing_extensions.TypedDict):
    """Specifies a range from an inclusive start value to an exclusive end value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    startValue: typing.Any
    """Inclusive start."""

    endValue: typing.Any
    """Exclusive end."""


class AggregationRangesGroupingV2(pydantic.BaseModel):
    """Divides objects into groups according to specified ranges."""

    field: PropertyApiName
    ranges: typing.List[AggregationRangeV2]
    type: typing.Literal["ranges"] = "ranges"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregationRangesGroupingV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregationRangesGroupingV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregationRangesGroupingV2Dict(typing_extensions.TypedDict):
    """Divides objects into groups according to specified ranges."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    ranges: typing.List[AggregationRangeV2Dict]
    type: typing.Literal["ranges"]


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


AggregationV2Dict = typing_extensions.Annotated[
    typing.Union[
        "ApproximateDistinctAggregationV2Dict",
        "MinAggregationV2Dict",
        "AvgAggregationV2Dict",
        "MaxAggregationV2Dict",
        "ApproximatePercentileAggregationV2Dict",
        "CountAggregationV2Dict",
        "SumAggregationV2Dict",
        "ExactDistinctAggregationV2Dict",
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies an aggregation function."""


class AndQueryV2(pydantic.BaseModel):
    """Returns objects where every query is satisfied."""

    value: typing.List[SearchJsonQueryV2]
    type: typing.Literal["and"] = "and"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AndQueryV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AndQueryV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class AndQueryV2Dict(typing_extensions.TypedDict):
    """Returns objects where every query is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: typing.List[SearchJsonQueryV2Dict]
    type: typing.Literal["and"]


ApplyActionMode = typing.Literal["VALIDATE_ONLY", "VALIDATE_AND_EXECUTE"]
"""ApplyActionMode"""


class ApplyActionRequestOptions(pydantic.BaseModel):
    """ApplyActionRequestOptions"""

    mode: typing.Optional[ApplyActionMode] = None
    return_edits: typing.Optional[ReturnEditsMode] = pydantic.Field(alias=str("returnEdits"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ApplyActionRequestOptionsDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ApplyActionRequestOptionsDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ApplyActionRequestOptionsDict(typing_extensions.TypedDict):
    """ApplyActionRequestOptions"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mode: typing_extensions.NotRequired[ApplyActionMode]
    returnEdits: typing_extensions.NotRequired[ReturnEditsMode]


class ApproximateDistinctAggregationV2(pydantic.BaseModel):
    """Computes an approximate number of distinct values for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["approximateDistinct"] = "approximateDistinct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ApproximateDistinctAggregationV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ApproximateDistinctAggregationV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ApproximateDistinctAggregationV2Dict(typing_extensions.TypedDict):
    """Computes an approximate number of distinct values for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    name: typing_extensions.NotRequired[AggregationMetricName]
    direction: typing_extensions.NotRequired[OrderByDirection]
    type: typing.Literal["approximateDistinct"]


class ApproximatePercentileAggregationV2(pydantic.BaseModel):
    """Computes the approximate percentile value for the provided field. Requires Object Storage V2."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    approximate_percentile: float = pydantic.Field(alias=str("approximatePercentile"))  # type: ignore[literal-required]
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["approximatePercentile"] = "approximatePercentile"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ApproximatePercentileAggregationV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ApproximatePercentileAggregationV2Dict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class ApproximatePercentileAggregationV2Dict(typing_extensions.TypedDict):
    """Computes the approximate percentile value for the provided field. Requires Object Storage V2."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    name: typing_extensions.NotRequired[AggregationMetricName]
    approximatePercentile: float
    direction: typing_extensions.NotRequired[OrderByDirection]
    type: typing.Literal["approximatePercentile"]


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

    def to_dict(self) -> "ArraySizeConstraintDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ArraySizeConstraintDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ArraySizeConstraintDict(typing_extensions.TypedDict):
    """The parameter expects an array of values and the size of the array must fall within the defined range."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    lt: typing_extensions.NotRequired[typing.Any]
    """Less than"""

    lte: typing_extensions.NotRequired[typing.Any]
    """Less than or equal"""

    gt: typing_extensions.NotRequired[typing.Any]
    """Greater than"""

    gte: typing_extensions.NotRequired[typing.Any]
    """Greater than or equal"""

    type: typing.Literal["arraySize"]


ArtifactRepositoryRid = core.RID
"""ArtifactRepositoryRid"""


AttachmentMetadataResponse = typing_extensions.Annotated[
    typing.Union["AttachmentV2", "ListAttachmentsResponseV2"], pydantic.Field(discriminator="type")
]
"""The attachment metadata response"""


AttachmentMetadataResponseDict = typing_extensions.Annotated[
    typing.Union["AttachmentV2Dict", "ListAttachmentsResponseV2Dict"],
    pydantic.Field(discriminator="type"),
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

    def to_dict(self) -> "AttachmentV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AttachmentV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class AttachmentV2Dict(typing_extensions.TypedDict):
    """The representation of an attachment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: AttachmentRid
    filename: core_models.Filename
    sizeBytes: core_models.SizeBytes
    mediaType: core_models.MediaType
    type: typing.Literal["single"]


class AvgAggregationV2(pydantic.BaseModel):
    """Computes the average value for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["avg"] = "avg"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AvgAggregationV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AvgAggregationV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class AvgAggregationV2Dict(typing_extensions.TypedDict):
    """Computes the average value for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    name: typing_extensions.NotRequired[AggregationMetricName]
    direction: typing_extensions.NotRequired[OrderByDirection]
    type: typing.Literal["avg"]


BatchActionObjectEdit = typing_extensions.Annotated[
    typing.Union["ModifyObject", "AddObject", "AddLink"], pydantic.Field(discriminator="type")
]
"""BatchActionObjectEdit"""


BatchActionObjectEditDict = typing_extensions.Annotated[
    typing.Union["ModifyObjectDict", "AddObjectDict", "AddLinkDict"],
    pydantic.Field(discriminator="type"),
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

    def to_dict(self) -> "BatchActionObjectEditsDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            BatchActionObjectEditsDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class BatchActionObjectEditsDict(typing_extensions.TypedDict):
    """BatchActionObjectEdits"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    edits: typing.List[BatchActionObjectEditDict]
    addedObjectCount: int
    modifiedObjectsCount: int
    deletedObjectsCount: int
    addedLinksCount: int
    deletedLinksCount: int
    type: typing.Literal["edits"]


BatchActionResults = typing_extensions.Annotated[
    typing.Union["BatchActionObjectEdits", "ObjectTypeEdits"], pydantic.Field(discriminator="type")
]
"""BatchActionResults"""


BatchActionResultsDict = typing_extensions.Annotated[
    typing.Union["BatchActionObjectEditsDict", "ObjectTypeEditsDict"],
    pydantic.Field(discriminator="type"),
]
"""BatchActionResults"""


class BatchApplyActionRequestItem(pydantic.BaseModel):
    """BatchApplyActionRequestItem"""

    parameters: typing.Dict[ParameterId, typing.Optional[DataValue]]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "BatchApplyActionRequestItemDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            BatchApplyActionRequestItemDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class BatchApplyActionRequestItemDict(typing_extensions.TypedDict):
    """BatchApplyActionRequestItem"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameters: typing.Dict[ParameterId, typing.Optional[DataValue]]


class BatchApplyActionRequestOptions(pydantic.BaseModel):
    """BatchApplyActionRequestOptions"""

    return_edits: typing.Optional[BatchReturnEditsMode] = pydantic.Field(alias=str("returnEdits"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "BatchApplyActionRequestOptionsDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            BatchApplyActionRequestOptionsDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class BatchApplyActionRequestOptionsDict(typing_extensions.TypedDict):
    """BatchApplyActionRequestOptions"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    returnEdits: typing_extensions.NotRequired[BatchReturnEditsMode]


class BatchApplyActionResponseV2(pydantic.BaseModel):
    """BatchApplyActionResponseV2"""

    edits: typing.Optional[BatchActionResults] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "BatchApplyActionResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            BatchApplyActionResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class BatchApplyActionResponseV2Dict(typing_extensions.TypedDict):
    """BatchApplyActionResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    edits: typing_extensions.NotRequired[BatchActionResultsDict]


BatchReturnEditsMode = typing.Literal["ALL", "NONE"]
"""BatchReturnEditsMode"""


class BoundingBoxValue(pydantic.BaseModel):
    """The top left and bottom right coordinate points that make up the bounding box."""

    top_left: WithinBoundingBoxPoint = pydantic.Field(alias=str("topLeft"))  # type: ignore[literal-required]
    bottom_right: WithinBoundingBoxPoint = pydantic.Field(alias=str("bottomRight"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "BoundingBoxValueDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(BoundingBoxValueDict, self.model_dump(by_alias=True, exclude_none=True))


class BoundingBoxValueDict(typing_extensions.TypedDict):
    """The top left and bottom right coordinate points that make up the bounding box."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    topLeft: WithinBoundingBoxPointDict
    bottomRight: WithinBoundingBoxPointDict


class CenterPoint(pydantic.BaseModel):
    """The coordinate point to use as the center of the distance query."""

    center: CenterPointTypes
    distance: core_models.Distance
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CenterPointDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(CenterPointDict, self.model_dump(by_alias=True, exclude_none=True))


class CenterPointDict(typing_extensions.TypedDict):
    """The coordinate point to use as the center of the distance query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    center: CenterPointTypesDict
    distance: core_models.DistanceDict


class CenterPointTypes(pydantic.BaseModel):
    """CenterPointTypes"""

    coordinates: geo_models.Position
    bbox: typing.Optional[geo_models.BBox] = None
    type: typing.Literal["Point"] = "Point"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CenterPointTypesDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(CenterPointTypesDict, self.model_dump(by_alias=True, exclude_none=True))


class CenterPointTypesDict(typing_extensions.TypedDict):
    """CenterPointTypes"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    coordinates: geo_models.Position
    bbox: typing_extensions.NotRequired[geo_models.BBox]
    type: typing.Literal["Point"]


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

    def to_dict(self) -> "ContainsAllTermsInOrderPrefixLastTermDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ContainsAllTermsInOrderPrefixLastTermDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class ContainsAllTermsInOrderPrefixLastTermDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field contains all of the terms in the order provided,
    but they do have to be adjacent to each other.
    The last term can be a partial prefix match. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` can be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: str
    type: typing.Literal["containsAllTermsInOrderPrefixLastTerm"]


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

    def to_dict(self) -> "ContainsAllTermsInOrderQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ContainsAllTermsInOrderQueryDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ContainsAllTermsInOrderQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field contains all of the terms in the order provided,
    but they do have to be adjacent to each other. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: str
    type: typing.Literal["containsAllTermsInOrder"]


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

    def to_dict(self) -> "ContainsAllTermsQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ContainsAllTermsQueryDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ContainsAllTermsQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field contains all of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: str
    fuzzy: typing_extensions.NotRequired[FuzzyV2]
    type: typing.Literal["containsAllTerms"]


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

    def to_dict(self) -> "ContainsAnyTermQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ContainsAnyTermQueryDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ContainsAnyTermQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field contains any of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: str
    fuzzy: typing_extensions.NotRequired[FuzzyV2]
    type: typing.Literal["containsAnyTerm"]


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

    def to_dict(self) -> "ContainsQueryV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ContainsQueryV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class ContainsQueryV2Dict(typing_extensions.TypedDict):
    """
    Returns objects where the specified array contains a value. Allows you to specify a property to query on by a
    variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: PropertyValue
    type: typing.Literal["contains"]


class CountAggregationV2(pydantic.BaseModel):
    """Computes the total count of objects."""

    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["count"] = "count"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CountAggregationV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CountAggregationV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class CountAggregationV2Dict(typing_extensions.TypedDict):
    """Computes the total count of objects."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: typing_extensions.NotRequired[AggregationMetricName]
    direction: typing_extensions.NotRequired[OrderByDirection]
    type: typing.Literal["count"]


class CountObjectsResponseV2(pydantic.BaseModel):
    """CountObjectsResponseV2"""

    count: typing.Optional[int] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CountObjectsResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CountObjectsResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class CountObjectsResponseV2Dict(typing_extensions.TypedDict):
    """CountObjectsResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    count: typing_extensions.NotRequired[int]


class CreateInterfaceObjectRule(pydantic.BaseModel):
    """CreateInterfaceObjectRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["createInterfaceObject"] = "createInterfaceObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateInterfaceObjectRuleDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateInterfaceObjectRuleDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class CreateInterfaceObjectRuleDict(typing_extensions.TypedDict):
    """CreateInterfaceObjectRule"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    interfaceTypeApiName: InterfaceTypeApiName
    type: typing.Literal["createInterfaceObject"]


class CreateLinkRule(pydantic.BaseModel):
    """CreateLinkRule"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("aSideObjectTypeApiName"))  # type: ignore[literal-required]
    b_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("bSideObjectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["createLink"] = "createLink"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateLinkRuleDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(CreateLinkRuleDict, self.model_dump(by_alias=True, exclude_none=True))


class CreateLinkRuleDict(typing_extensions.TypedDict):
    """CreateLinkRule"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    linkTypeApiNameAtoB: LinkTypeApiName
    linkTypeApiNameBtoA: LinkTypeApiName
    aSideObjectTypeApiName: ObjectTypeApiName
    bSideObjectTypeApiName: ObjectTypeApiName
    type: typing.Literal["createLink"]


class CreateObjectRule(pydantic.BaseModel):
    """CreateObjectRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["createObject"] = "createObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateObjectRuleDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(CreateObjectRuleDict, self.model_dump(by_alias=True, exclude_none=True))


class CreateObjectRuleDict(typing_extensions.TypedDict):
    """CreateObjectRule"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectTypeApiName: ObjectTypeApiName
    type: typing.Literal["createObject"]


class CreateTemporaryObjectSetResponseV2(pydantic.BaseModel):
    """CreateTemporaryObjectSetResponseV2"""

    object_set_rid: ObjectSetRid = pydantic.Field(alias=str("objectSetRid"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CreateTemporaryObjectSetResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            CreateTemporaryObjectSetResponseV2Dict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class CreateTemporaryObjectSetResponseV2Dict(typing_extensions.TypedDict):
    """CreateTemporaryObjectSetResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSetRid: ObjectSetRid


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


class DeleteInterfaceObjectRule(pydantic.BaseModel):
    """DeleteInterfaceObjectRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteInterfaceObject"] = "deleteInterfaceObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DeleteInterfaceObjectRuleDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            DeleteInterfaceObjectRuleDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class DeleteInterfaceObjectRuleDict(typing_extensions.TypedDict):
    """DeleteInterfaceObjectRule"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    interfaceTypeApiName: InterfaceTypeApiName
    type: typing.Literal["deleteInterfaceObject"]


class DeleteLink(pydantic.BaseModel):
    """DeleteLink"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object: LinkSideObject = pydantic.Field(alias=str("aSideObject"))  # type: ignore[literal-required]
    b_side_object: LinkSideObject = pydantic.Field(alias=str("bSideObject"))  # type: ignore[literal-required]
    type: typing.Literal["deleteLink"] = "deleteLink"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DeleteLinkDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DeleteLinkDict, self.model_dump(by_alias=True, exclude_none=True))


class DeleteLinkDict(typing_extensions.TypedDict):
    """DeleteLink"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    linkTypeApiNameAtoB: LinkTypeApiName
    linkTypeApiNameBtoA: LinkTypeApiName
    aSideObject: LinkSideObjectDict
    bSideObject: LinkSideObjectDict
    type: typing.Literal["deleteLink"]


class DeleteLinkRule(pydantic.BaseModel):
    """DeleteLinkRule"""

    link_type_api_name_ato_b: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameAtoB"))  # type: ignore[literal-required]
    link_type_api_name_bto_a: LinkTypeApiName = pydantic.Field(alias=str("linkTypeApiNameBtoA"))  # type: ignore[literal-required]
    a_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("aSideObjectTypeApiName"))  # type: ignore[literal-required]
    b_side_object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("bSideObjectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteLink"] = "deleteLink"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DeleteLinkRuleDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DeleteLinkRuleDict, self.model_dump(by_alias=True, exclude_none=True))


class DeleteLinkRuleDict(typing_extensions.TypedDict):
    """DeleteLinkRule"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    linkTypeApiNameAtoB: LinkTypeApiName
    linkTypeApiNameBtoA: LinkTypeApiName
    aSideObjectTypeApiName: ObjectTypeApiName
    bSideObjectTypeApiName: ObjectTypeApiName
    type: typing.Literal["deleteLink"]


class DeleteObject(pydantic.BaseModel):
    """DeleteObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    type: typing.Literal["deleteObject"] = "deleteObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DeleteObjectDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DeleteObjectDict, self.model_dump(by_alias=True, exclude_none=True))


class DeleteObjectDict(typing_extensions.TypedDict):
    """DeleteObject"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKey: PropertyValue
    objectType: ObjectTypeApiName
    type: typing.Literal["deleteObject"]


class DeleteObjectRule(pydantic.BaseModel):
    """DeleteObjectRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["deleteObject"] = "deleteObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DeleteObjectRuleDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DeleteObjectRuleDict, self.model_dump(by_alias=True, exclude_none=True))


class DeleteObjectRuleDict(typing_extensions.TypedDict):
    """DeleteObjectRule"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectTypeApiName: ObjectTypeApiName
    type: typing.Literal["deleteObject"]


class DeprecatedPropertyTypeStatus(pydantic.BaseModel):
    """
    This status indicates that the PropertyType is reaching the end of its life and will be removed as per the
    deadline specified.
    """

    message: str
    deadline: datetime
    replaced_by: typing.Optional[PropertyTypeRid] = pydantic.Field(alias=str("replacedBy"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["deprecated"] = "deprecated"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DeprecatedPropertyTypeStatusDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            DeprecatedPropertyTypeStatusDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class DeprecatedPropertyTypeStatusDict(typing_extensions.TypedDict):
    """
    This status indicates that the PropertyType is reaching the end of its life and will be removed as per the
    deadline specified.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    message: str
    deadline: datetime
    replacedBy: typing_extensions.NotRequired[PropertyTypeRid]
    type: typing.Literal["deprecated"]


DerivedPropertyApiName = str
"""The name of the derived property that will be returned."""


DerivedPropertyDefinition = typing_extensions.Annotated[
    typing.Union[
        "AddPropertyExpression",
        "AbsoluteValuePropertyExpression",
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


DerivedPropertyDefinitionDict = typing_extensions.Annotated[
    typing.Union[
        "AddPropertyExpressionDict",
        "AbsoluteValuePropertyExpressionDict",
        "ExtractPropertyExpressionDict",
        "SelectedPropertyExpressionDict",
        "NegatePropertyExpressionDict",
        "SubtractPropertyExpressionDict",
        "PropertyApiNameSelectorDict",
        "LeastPropertyExpressionDict",
        "DividePropertyExpressionDict",
        "MultiplyPropertyExpressionDict",
        "GreatestPropertyExpressionDict",
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

    def to_dict(self) -> "DividePropertyExpressionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            DividePropertyExpressionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class DividePropertyExpressionDict(typing_extensions.TypedDict):
    """Divides the left numeric value by the right numeric value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    left: DerivedPropertyDefinitionDict
    right: DerivedPropertyDefinitionDict
    type: typing.Literal["divide"]


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

    def to_dict(self) -> "DoesNotIntersectBoundingBoxQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            DoesNotIntersectBoundingBoxQueryDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class DoesNotIntersectBoundingBoxQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field does not intersect the bounding box provided. Allows you to specify a
    property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not
    both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: BoundingBoxValueDict
    type: typing.Literal["doesNotIntersectBoundingBox"]


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

    def to_dict(self) -> "DoesNotIntersectPolygonQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            DoesNotIntersectPolygonQueryDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class DoesNotIntersectPolygonQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field does not intersect the polygon provided. Allows you to specify a
    property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not
    both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: PolygonValueDict
    type: typing.Literal["doesNotIntersectPolygon"]


class DoubleVector(pydantic.BaseModel):
    """
    The vector to search with. The vector must be of the same dimension as the vectors stored in the provided
    propertyIdentifier.
    """

    value: typing.List[float]
    type: typing.Literal["vector"] = "vector"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "DoubleVectorDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(DoubleVectorDict, self.model_dump(by_alias=True, exclude_none=True))


class DoubleVectorDict(typing_extensions.TypedDict):
    """
    The vector to search with. The vector must be of the same dimension as the vectors stored in the provided
    propertyIdentifier.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: typing.List[float]
    type: typing.Literal["vector"]


class EntrySetType(pydantic.BaseModel):
    """EntrySetType"""

    key_type: QueryDataType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: QueryDataType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["entrySet"] = "entrySet"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "EntrySetTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(EntrySetTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class EntrySetTypeDict(typing_extensions.TypedDict):
    """EntrySetType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    keyType: QueryDataTypeDict
    valueType: QueryDataTypeDict
    type: typing.Literal["entrySet"]


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

    def to_dict(self) -> "EqualsQueryV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(EqualsQueryV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class EqualsQueryV2Dict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field is equal to a value. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: PropertyValue
    type: typing.Literal["eq"]


class ExactDistinctAggregationV2(pydantic.BaseModel):
    """Computes an exact number of distinct values for the provided field. May be slower than an approximate distinct aggregation. Requires Object Storage V2."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["exactDistinct"] = "exactDistinct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ExactDistinctAggregationV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ExactDistinctAggregationV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ExactDistinctAggregationV2Dict(typing_extensions.TypedDict):
    """Computes an exact number of distinct values for the provided field. May be slower than an approximate distinct aggregation. Requires Object Storage V2."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    name: typing_extensions.NotRequired[AggregationMetricName]
    direction: typing_extensions.NotRequired[OrderByDirection]
    type: typing.Literal["exactDistinct"]


class ExamplePropertyTypeStatus(pydantic.BaseModel):
    """
    This status indicates that the PropertyType is an example. It is backed by notional data that should not be
    used for actual workflows, but can be used to test those workflows.
    """

    type: typing.Literal["example"] = "example"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ExamplePropertyTypeStatusDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ExamplePropertyTypeStatusDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ExamplePropertyTypeStatusDict(typing_extensions.TypedDict):
    """
    This status indicates that the PropertyType is an example. It is backed by notional data that should not be
    used for actual workflows, but can be used to test those workflows.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["example"]


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


class ExperimentalPropertyTypeStatus(pydantic.BaseModel):
    """This status indicates that the PropertyType is in development."""

    type: typing.Literal["experimental"] = "experimental"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ExperimentalPropertyTypeStatusDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ExperimentalPropertyTypeStatusDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ExperimentalPropertyTypeStatusDict(typing_extensions.TypedDict):
    """This status indicates that the PropertyType is in development."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["experimental"]


ExtractDatePart = typing.Literal["DAYS", "MONTHS", "QUARTERS", "YEARS"]
"""ExtractDatePart"""


class ExtractPropertyExpression(pydantic.BaseModel):
    """Extracts the specified date part from a date or timestamp."""

    property: DerivedPropertyDefinition
    part: ExtractDatePart
    type: typing.Literal["extract"] = "extract"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ExtractPropertyExpressionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ExtractPropertyExpressionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ExtractPropertyExpressionDict(typing_extensions.TypedDict):
    """Extracts the specified date part from a date or timestamp."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    property: DerivedPropertyDefinitionDict
    part: ExtractDatePart
    type: typing.Literal["extract"]


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

    def to_dict(self) -> "GetSelectedPropertyOperationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GetSelectedPropertyOperationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GetSelectedPropertyOperationDict(typing_extensions.TypedDict):
    """
    Gets a single value of a property. Throws if the target object set is on the MANY side of the link and could
    explode the cardinality.

    Use collectList or collectSet which will return a list of values in that case.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    selectedPropertyApiName: PropertyApiName
    type: typing.Literal["get"]


class GreatestPropertyExpression(pydantic.BaseModel):
    """Finds greatest of two or more numeric, date or timestamp values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["greatest"] = "greatest"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GreatestPropertyExpressionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GreatestPropertyExpressionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GreatestPropertyExpressionDict(typing_extensions.TypedDict):
    """Finds greatest of two or more numeric, date or timestamp values."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    properties: typing.List[DerivedPropertyDefinitionDict]
    type: typing.Literal["greatest"]


class GroupMemberConstraint(pydantic.BaseModel):
    """The parameter value must be the user id of a member belonging to at least one of the groups defined by the constraint."""

    type: typing.Literal["groupMember"] = "groupMember"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GroupMemberConstraintDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GroupMemberConstraintDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GroupMemberConstraintDict(typing_extensions.TypedDict):
    """The parameter value must be the user id of a member belonging to at least one of the groups defined by the constraint."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["groupMember"]


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

    def to_dict(self) -> "GtQueryV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GtQueryV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class GtQueryV2Dict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field is greater than a value. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: PropertyValue
    type: typing.Literal["gt"]


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

    def to_dict(self) -> "GteQueryV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GteQueryV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class GteQueryV2Dict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field is greater than or equal to a value. Allows you to specify a property
    to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: PropertyValue
    type: typing.Literal["gte"]


class Icon(pydantic.BaseModel):
    """A union currently only consisting of the BlueprintIcon (more icon types may be added in the future)."""

    color: str
    """A hexadecimal color code."""

    name: str
    """
    The [name](https://blueprintjs.com/docs/#icons/icons-list) of the Blueprint icon. 
    Used to specify the Blueprint icon to represent the object type in a React app.
    """

    type: typing.Literal["blueprint"] = "blueprint"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "IconDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(IconDict, self.model_dump(by_alias=True, exclude_none=True))


class IconDict(typing_extensions.TypedDict):
    """A union currently only consisting of the BlueprintIcon (more icon types may be added in the future)."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    color: str
    """A hexadecimal color code."""

    name: str
    """
    The [name](https://blueprintjs.com/docs/#icons/icons-list) of the Blueprint icon. 
    Used to specify the Blueprint icon to represent the object type in a React app.
    """

    type: typing.Literal["blueprint"]


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

    def to_dict(self) -> "InQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(InQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class InQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field equals any of the provided values. Allows you to
    specify a property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied,
    but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: typing.List[PropertyValue]
    type: typing.Literal["in"]


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

    def to_dict(self) -> "InterfaceLinkTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(InterfaceLinkTypeDict, self.model_dump(by_alias=True, exclude_none=True))


InterfaceLinkTypeApiName = str
"""A string indicating the API name to use for the interface link."""


InterfaceLinkTypeCardinality = typing.Literal["ONE", "MANY"]
"""
The cardinality of the link in the given direction. Cardinality can be "ONE", meaning an object can
link to zero or one other objects, or "MANY", meaning an object can link to any number of other objects.
"""


class InterfaceLinkTypeDict(typing_extensions.TypedDict):
    """
    A link type constraint defined at the interface level where the implementation of the links is provided
    by the implementing object types.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: InterfaceLinkTypeRid
    apiName: InterfaceLinkTypeApiName
    displayName: core_models.DisplayName
    description: typing_extensions.NotRequired[str]
    """The description of the interface link type."""

    linkedEntityApiName: InterfaceLinkTypeLinkedEntityApiNameDict
    cardinality: InterfaceLinkTypeCardinality
    required: bool
    """Whether each implementing object type must declare at least one implementation of this link."""


InterfaceLinkTypeLinkedEntityApiName = typing_extensions.Annotated[
    typing.Union["LinkedObjectTypeApiName", "LinkedInterfaceTypeApiName"],
    pydantic.Field(discriminator="type"),
]
"""A reference to the linked entity. This can either be an object or an interface type."""


InterfaceLinkTypeLinkedEntityApiNameDict = typing_extensions.Annotated[
    typing.Union["LinkedObjectTypeApiNameDict", "LinkedInterfaceTypeApiNameDict"],
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

    def to_dict(self) -> "InterfaceSharedPropertyTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            InterfaceSharedPropertyTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class InterfaceSharedPropertyTypeDict(typing_extensions.TypedDict):
    """
    A shared property type with an additional field to indicate whether the property must be included on every
    object type that implements the interface, or whether it is optional.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: SharedPropertyTypeRid
    apiName: SharedPropertyTypeApiName
    displayName: core_models.DisplayName
    description: typing_extensions.NotRequired[str]
    """A short text that describes the SharedPropertyType."""

    dataType: ObjectPropertyTypeDict
    required: bool
    """Whether each implementing object type must declare an implementation for this property."""


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

    def to_dict(self) -> "InterfaceTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(InterfaceTypeDict, self.model_dump(by_alias=True, exclude_none=True))


InterfaceTypeApiName = str
"""
The name of the interface type in the API in UpperCamelCase format. To find the API name for your interface
type, use the `List interface types` endpoint or check the **Ontology Manager**.
"""


class InterfaceTypeDict(typing_extensions.TypedDict):
    """Represents an interface type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: InterfaceTypeRid
    apiName: InterfaceTypeApiName
    displayName: core_models.DisplayName
    description: typing_extensions.NotRequired[str]
    """The description of the interface."""

    properties: typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyTypeDict]
    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has. A shared property type must be unique across all of the properties.
    """

    allProperties: typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyTypeDict]
    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has, including properties from all directly and indirectly extended 
    interfaces.
    """

    extendsInterfaces: typing.List[InterfaceTypeApiName]
    """
    A list of interface API names that this interface extends. An interface can extend other interfaces to 
    inherit their properties.
    """

    allExtendsInterfaces: typing.List[InterfaceTypeApiName]
    """A list of interface API names that this interface extends, both directly and indirectly."""

    implementedByObjectTypes: typing.List[ObjectTypeApiName]
    """A list of object API names that implement this interface."""

    links: typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkTypeDict]
    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has.
    """

    allLinks: typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkTypeDict]
    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has, including links from all directly and indirectly extended interfaces.
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

    def to_dict(self) -> "IntersectsBoundingBoxQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            IntersectsBoundingBoxQueryDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class IntersectsBoundingBoxQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field intersects the bounding box provided. Allows you to specify a property
    to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: BoundingBoxValueDict
    type: typing.Literal["intersectsBoundingBox"]


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

    def to_dict(self) -> "IntersectsPolygonQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            IntersectsPolygonQueryDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class IntersectsPolygonQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field intersects the polygon provided. Allows you to specify a property to
    query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: PolygonValueDict
    type: typing.Literal["intersectsPolygon"]


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

    def to_dict(self) -> "IsNullQueryV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(IsNullQueryV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class IsNullQueryV2Dict(typing_extensions.TypedDict):
    """
    Returns objects based on the existence of the specified field. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: bool
    type: typing.Literal["isNull"]


class LeastPropertyExpression(pydantic.BaseModel):
    """Finds least of two or more numeric, date or timestamp values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["least"] = "least"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "LeastPropertyExpressionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            LeastPropertyExpressionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class LeastPropertyExpressionDict(typing_extensions.TypedDict):
    """Finds least of two or more numeric, date or timestamp values."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    properties: typing.List[DerivedPropertyDefinitionDict]
    type: typing.Literal["least"]


class LinkSideObject(pydantic.BaseModel):
    """LinkSideObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "LinkSideObjectDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(LinkSideObjectDict, self.model_dump(by_alias=True, exclude_none=True))


class LinkSideObjectDict(typing_extensions.TypedDict):
    """LinkSideObject"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKey: PropertyValue
    objectType: ObjectTypeApiName


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

    def to_dict(self) -> "LinkTypeSideV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(LinkTypeSideV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class LinkTypeSideV2Dict(typing_extensions.TypedDict):
    """LinkTypeSideV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: LinkTypeApiName
    displayName: core_models.DisplayName
    status: core_models.ReleaseStatus
    objectTypeApiName: ObjectTypeApiName
    cardinality: LinkTypeSideCardinality
    foreignKeyPropertyApiName: typing_extensions.NotRequired[PropertyApiName]
    linkTypeRid: LinkTypeRid


class LinkedInterfaceTypeApiName(pydantic.BaseModel):
    """A reference to the linked interface type."""

    api_name: InterfaceTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    type: typing.Literal["interfaceTypeApiName"] = "interfaceTypeApiName"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "LinkedInterfaceTypeApiNameDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            LinkedInterfaceTypeApiNameDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class LinkedInterfaceTypeApiNameDict(typing_extensions.TypedDict):
    """A reference to the linked interface type."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: InterfaceTypeApiName
    type: typing.Literal["interfaceTypeApiName"]


class LinkedObjectTypeApiName(pydantic.BaseModel):
    """A reference to the linked object type."""

    api_name: ObjectTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    type: typing.Literal["objectTypeApiName"] = "objectTypeApiName"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "LinkedObjectTypeApiNameDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            LinkedObjectTypeApiNameDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class LinkedObjectTypeApiNameDict(typing_extensions.TypedDict):
    """A reference to the linked object type."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: ObjectTypeApiName
    type: typing.Literal["objectTypeApiName"]


class ListActionTypesResponseV2(pydantic.BaseModel):
    """ListActionTypesResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[ActionTypeV2]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListActionTypesResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListActionTypesResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListActionTypesResponseV2Dict(typing_extensions.TypedDict):
    """ListActionTypesResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[ActionTypeV2Dict]


class ListAttachmentsResponseV2(pydantic.BaseModel):
    """ListAttachmentsResponseV2"""

    data: typing.List[AttachmentV2]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["multiple"] = "multiple"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListAttachmentsResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListAttachmentsResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListAttachmentsResponseV2Dict(typing_extensions.TypedDict):
    """ListAttachmentsResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[AttachmentV2Dict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    type: typing.Literal["multiple"]


class ListInterfaceTypesResponse(pydantic.BaseModel):
    """ListInterfaceTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[InterfaceType]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListInterfaceTypesResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListInterfaceTypesResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListInterfaceTypesResponseDict(typing_extensions.TypedDict):
    """ListInterfaceTypesResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[InterfaceTypeDict]


class ListLinkedObjectsResponseV2(pydantic.BaseModel):
    """ListLinkedObjectsResponseV2"""

    data: typing.List[OntologyObjectV2]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListLinkedObjectsResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListLinkedObjectsResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListLinkedObjectsResponseV2Dict(typing_extensions.TypedDict):
    """ListLinkedObjectsResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[OntologyObjectV2]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListObjectTypesV2Response(pydantic.BaseModel):
    """ListObjectTypesV2Response"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[ObjectTypeV2]
    """The list of object types in the current page."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListObjectTypesV2ResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListObjectTypesV2ResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListObjectTypesV2ResponseDict(typing_extensions.TypedDict):
    """ListObjectTypesV2Response"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[ObjectTypeV2Dict]
    """The list of object types in the current page."""


class ListObjectsResponseV2(pydantic.BaseModel):
    """ListObjectsResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[OntologyObjectV2]
    """The list of objects in the current page."""

    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListObjectsResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListObjectsResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListObjectsResponseV2Dict(typing_extensions.TypedDict):
    """ListObjectsResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[OntologyObjectV2]
    """The list of objects in the current page."""

    totalCount: core_models.TotalCount


class ListOutgoingLinkTypesResponseV2(pydantic.BaseModel):
    """ListOutgoingLinkTypesResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[LinkTypeSideV2]
    """The list of link type sides in the current page."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListOutgoingLinkTypesResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListOutgoingLinkTypesResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListOutgoingLinkTypesResponseV2Dict(typing_extensions.TypedDict):
    """ListOutgoingLinkTypesResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[LinkTypeSideV2Dict]
    """The list of link type sides in the current page."""


class ListQueryTypesResponseV2(pydantic.BaseModel):
    """ListQueryTypesResponseV2"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[QueryTypeV2]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListQueryTypesResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListQueryTypesResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListQueryTypesResponseV2Dict(typing_extensions.TypedDict):
    """ListQueryTypesResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[QueryTypeV2Dict]


class LoadObjectSetResponseV2(pydantic.BaseModel):
    """Represents the API response when loading an `ObjectSet`."""

    data: typing.List[OntologyObjectV2]
    """The list of objects in the current Page."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "LoadObjectSetResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            LoadObjectSetResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class LoadObjectSetResponseV2Dict(typing_extensions.TypedDict):
    """Represents the API response when loading an `ObjectSet`."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[OntologyObjectV2]
    """The list of objects in the current Page."""

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    totalCount: core_models.TotalCount


LogicRule = typing_extensions.Annotated[
    typing.Union[
        "DeleteInterfaceObjectRule",
        "ModifyInterfaceObjectRule",
        "ModifyObjectRule",
        "DeleteObjectRule",
        "CreateInterfaceObjectRule",
        "DeleteLinkRule",
        "CreateObjectRule",
        "CreateLinkRule",
    ],
    pydantic.Field(discriminator="type"),
]
"""LogicRule"""


LogicRuleDict = typing_extensions.Annotated[
    typing.Union[
        "DeleteInterfaceObjectRuleDict",
        "ModifyInterfaceObjectRuleDict",
        "ModifyObjectRuleDict",
        "DeleteObjectRuleDict",
        "CreateInterfaceObjectRuleDict",
        "DeleteLinkRuleDict",
        "CreateObjectRuleDict",
        "CreateLinkRuleDict",
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

    def to_dict(self) -> "LtQueryV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(LtQueryV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class LtQueryV2Dict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field is less than a value. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: PropertyValue
    type: typing.Literal["lt"]


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

    def to_dict(self) -> "LteQueryV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(LteQueryV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class LteQueryV2Dict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field is less than or equal to a value. Allows you to specify a property to
    query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: PropertyValue
    type: typing.Literal["lte"]


class MaxAggregationV2(pydantic.BaseModel):
    """Computes the maximum value for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["max"] = "max"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MaxAggregationV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MaxAggregationV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class MaxAggregationV2Dict(typing_extensions.TypedDict):
    """Computes the maximum value for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    name: typing_extensions.NotRequired[AggregationMetricName]
    direction: typing_extensions.NotRequired[OrderByDirection]
    type: typing.Literal["max"]


MethodObjectSet = typing_extensions.Annotated[
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
"""MethodObjectSet"""


MethodObjectSetDict = typing_extensions.Annotated[
    typing.Union[
        "ObjectSetSearchAroundTypeDict",
        "ObjectSetStaticTypeDict",
        "ObjectSetIntersectionTypeDict",
        "ObjectSetWithPropertiesTypeDict",
        "ObjectSetSubtractTypeDict",
        "ObjectSetNearestNeighborsTypeDict",
        "ObjectSetUnionTypeDict",
        "ObjectSetAsTypeTypeDict",
        "ObjectSetMethodInputTypeDict",
        "ObjectSetReferenceTypeDict",
        "ObjectSetFilterTypeDict",
        "ObjectSetInterfaceBaseTypeDict",
        "ObjectSetAsBaseObjectTypesTypeDict",
        "ObjectSetBaseTypeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""MethodObjectSet"""


class MinAggregationV2(pydantic.BaseModel):
    """Computes the minimum value for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["min"] = "min"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MinAggregationV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MinAggregationV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class MinAggregationV2Dict(typing_extensions.TypedDict):
    """Computes the minimum value for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    name: typing_extensions.NotRequired[AggregationMetricName]
    direction: typing_extensions.NotRequired[OrderByDirection]
    type: typing.Literal["min"]


class ModifyInterfaceObjectRule(pydantic.BaseModel):
    """ModifyInterfaceObjectRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["modifyInterfaceObject"] = "modifyInterfaceObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ModifyInterfaceObjectRuleDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ModifyInterfaceObjectRuleDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ModifyInterfaceObjectRuleDict(typing_extensions.TypedDict):
    """ModifyInterfaceObjectRule"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    interfaceTypeApiName: InterfaceTypeApiName
    type: typing.Literal["modifyInterfaceObject"]


class ModifyObject(pydantic.BaseModel):
    """ModifyObject"""

    primary_key: PropertyValue = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    object_type: ObjectTypeApiName = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    type: typing.Literal["modifyObject"] = "modifyObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ModifyObjectDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ModifyObjectDict, self.model_dump(by_alias=True, exclude_none=True))


class ModifyObjectDict(typing_extensions.TypedDict):
    """ModifyObject"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKey: PropertyValue
    objectType: ObjectTypeApiName
    type: typing.Literal["modifyObject"]


class ModifyObjectRule(pydantic.BaseModel):
    """ModifyObjectRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["modifyObject"] = "modifyObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ModifyObjectRuleDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ModifyObjectRuleDict, self.model_dump(by_alias=True, exclude_none=True))


class ModifyObjectRuleDict(typing_extensions.TypedDict):
    """ModifyObjectRule"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectTypeApiName: ObjectTypeApiName
    type: typing.Literal["modifyObject"]


class MultiplyPropertyExpression(pydantic.BaseModel):
    """Multiplies two or more numeric values."""

    properties: typing.List[DerivedPropertyDefinition]
    type: typing.Literal["multiply"] = "multiply"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MultiplyPropertyExpressionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            MultiplyPropertyExpressionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class MultiplyPropertyExpressionDict(typing_extensions.TypedDict):
    """Multiplies two or more numeric values."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    properties: typing.List[DerivedPropertyDefinitionDict]
    type: typing.Literal["multiply"]


NearestNeighborsQuery = typing_extensions.Annotated[
    typing.Union["DoubleVector", "NearestNeighborsQueryText"], pydantic.Field(discriminator="type")
]
"""
Queries support either a vector matching the embedding model defined on the property, or text that is 
automatically embedded.
"""


NearestNeighborsQueryDict = typing_extensions.Annotated[
    typing.Union["DoubleVectorDict", "NearestNeighborsQueryTextDict"],
    pydantic.Field(discriminator="type"),
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

    def to_dict(self) -> "NearestNeighborsQueryTextDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            NearestNeighborsQueryTextDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class NearestNeighborsQueryTextDict(typing_extensions.TypedDict):
    """Automatically embed the text in a vector using the embedding model configured for the given propertyIdentifier."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: str
    type: typing.Literal["text"]


class NegatePropertyExpression(pydantic.BaseModel):
    """Negates a numeric value."""

    property: DerivedPropertyDefinition
    type: typing.Literal["negate"] = "negate"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "NegatePropertyExpressionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            NegatePropertyExpressionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class NegatePropertyExpressionDict(typing_extensions.TypedDict):
    """Negates a numeric value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    property: DerivedPropertyDefinitionDict
    type: typing.Literal["negate"]


class NotQueryV2(pydantic.BaseModel):
    """Returns objects where the query is not satisfied."""

    value: SearchJsonQueryV2
    type: typing.Literal["not"] = "not"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "NotQueryV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(NotQueryV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class NotQueryV2Dict(typing_extensions.TypedDict):
    """Returns objects where the query is not satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: SearchJsonQueryV2Dict
    type: typing.Literal["not"]


ObjectEdit = typing_extensions.Annotated[
    typing.Union["ModifyObject", "DeleteObject", "AddObject", "DeleteLink", "AddLink"],
    pydantic.Field(discriminator="type"),
]
"""ObjectEdit"""


ObjectEditDict = typing_extensions.Annotated[
    typing.Union[
        "ModifyObjectDict", "DeleteObjectDict", "AddObjectDict", "DeleteLinkDict", "AddLinkDict"
    ],
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

    def to_dict(self) -> "ObjectEditsDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ObjectEditsDict, self.model_dump(by_alias=True, exclude_none=True))


class ObjectEditsDict(typing_extensions.TypedDict):
    """ObjectEdits"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    edits: typing.List[ObjectEditDict]
    addedObjectCount: int
    modifiedObjectsCount: int
    deletedObjectsCount: int
    addedLinksCount: int
    deletedLinksCount: int
    type: typing.Literal["edits"]


ObjectPropertyType = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateType",
        "StructType",
        "core_models.StringType",
        "core_models.ByteType",
        "core_models.DoubleType",
        "core_models.GeoPointType",
        "core_models.GeotimeSeriesReferenceType",
        "core_models.IntegerType",
        "core_models.FloatType",
        "core_models.GeoShapeType",
        "core_models.LongType",
        "core_models.BooleanType",
        "core_models.CipherTextType",
        "core_models.MarkingType",
        "core_models.AttachmentType",
        "core_models.MediaReferenceType",
        "core_models.TimeseriesType",
        "OntologyObjectArrayType",
        "core_models.ShortType",
        "core_models.VectorType",
        "core_models.DecimalType",
        "core_models.TimestampType",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Object properties."""


ObjectPropertyTypeDict = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateTypeDict",
        "StructTypeDict",
        "core_models.StringTypeDict",
        "core_models.ByteTypeDict",
        "core_models.DoubleTypeDict",
        "core_models.GeoPointTypeDict",
        "core_models.GeotimeSeriesReferenceTypeDict",
        "core_models.IntegerTypeDict",
        "core_models.FloatTypeDict",
        "core_models.GeoShapeTypeDict",
        "core_models.LongTypeDict",
        "core_models.BooleanTypeDict",
        "core_models.CipherTextTypeDict",
        "core_models.MarkingTypeDict",
        "core_models.AttachmentTypeDict",
        "core_models.MediaReferenceTypeDict",
        "core_models.TimeseriesTypeDict",
        "OntologyObjectArrayTypeDict",
        "core_models.ShortTypeDict",
        "core_models.VectorTypeDict",
        "core_models.DecimalTypeDict",
        "core_models.TimestampTypeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Object properties."""


class ObjectPropertyValueConstraint(pydantic.BaseModel):
    """The parameter value must be a property value of an object found within an object set."""

    type: typing.Literal["objectPropertyValue"] = "objectPropertyValue"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectPropertyValueConstraintDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectPropertyValueConstraintDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectPropertyValueConstraintDict(typing_extensions.TypedDict):
    """The parameter value must be a property value of an object found within an object set."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["objectPropertyValue"]


class ObjectQueryResultConstraint(pydantic.BaseModel):
    """The parameter value must be the primary key of an object found within an object set."""

    type: typing.Literal["objectQueryResult"] = "objectQueryResult"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectQueryResultConstraintDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectQueryResultConstraintDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectQueryResultConstraintDict(typing_extensions.TypedDict):
    """The parameter value must be the primary key of an object found within an object set."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["objectQueryResult"]


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

    def to_dict(self) -> "ObjectSetAsBaseObjectTypesTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetAsBaseObjectTypesTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetAsBaseObjectTypesTypeDict(typing_extensions.TypedDict):
    """
    Casts the objects in the object set to their base type and thus ensures objects are returned with all of their
    properties in the resulting object set, not just the properties that implement interface properties. This is
    currently unsupported and an exception will be thrown if used.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict
    type: typing.Literal["asBaseObjectTypes"]


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

    def to_dict(self) -> "ObjectSetAsTypeTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetAsTypeTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetAsTypeTypeDict(typing_extensions.TypedDict):
    """
    Casts an object set to a specified object type or interface type API name. Any object whose object type does
    not match the object type provided or implement the interface type provided will be dropped from the resulting
    object set. This is currently unsupported and an exception will be thrown if used.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    entityType: str
    """An object type or interface type API name."""

    objectSet: ObjectSetDict
    type: typing.Literal["asType"]


class ObjectSetBaseType(pydantic.BaseModel):
    """ObjectSetBaseType"""

    object_type: str = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    """The API name of the object type."""

    type: typing.Literal["base"] = "base"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetBaseTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ObjectSetBaseTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class ObjectSetBaseTypeDict(typing_extensions.TypedDict):
    """ObjectSetBaseType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: str
    """The API name of the object type."""

    type: typing.Literal["base"]


ObjectSetDict = typing_extensions.Annotated[
    typing.Union[
        "ObjectSetSearchAroundTypeDict",
        "ObjectSetStaticTypeDict",
        "ObjectSetIntersectionTypeDict",
        "ObjectSetWithPropertiesTypeDict",
        "ObjectSetSubtractTypeDict",
        "ObjectSetNearestNeighborsTypeDict",
        "ObjectSetUnionTypeDict",
        "ObjectSetAsTypeTypeDict",
        "ObjectSetMethodInputTypeDict",
        "ObjectSetReferenceTypeDict",
        "ObjectSetFilterTypeDict",
        "ObjectSetInterfaceBaseTypeDict",
        "ObjectSetAsBaseObjectTypesTypeDict",
        "ObjectSetBaseTypeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""Represents the definition of an `ObjectSet` in the `Ontology`."""


class ObjectSetFilterType(pydantic.BaseModel):
    """ObjectSetFilterType"""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    where: SearchJsonQueryV2
    type: typing.Literal["filter"] = "filter"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetFilterTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetFilterTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetFilterTypeDict(typing_extensions.TypedDict):
    """ObjectSetFilterType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict
    where: SearchJsonQueryV2Dict
    type: typing.Literal["filter"]


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

    def to_dict(self) -> "ObjectSetInterfaceBaseTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetInterfaceBaseTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetInterfaceBaseTypeDict(typing_extensions.TypedDict):
    """ObjectSetInterfaceBaseType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    interfaceType: str
    """
    An object set with objects that implement the interface with the given interface API name. The objects in 
    the object set will only have properties that implement properties of the given interface, unless you set the includeAllBaseObjectProperties flag.
    """

    includeAllBaseObjectProperties: typing_extensions.NotRequired[bool]
    """
    A flag that will return all of the underlying object properties for the objects that implement the interface. 
    This includes properties that don't explicitly implement an SPT on the interface.
    """

    type: typing.Literal["interfaceBase"]


class ObjectSetIntersectionType(pydantic.BaseModel):
    """ObjectSetIntersectionType"""

    object_sets: typing.List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]
    type: typing.Literal["intersect"] = "intersect"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetIntersectionTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetIntersectionTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetIntersectionTypeDict(typing_extensions.TypedDict):
    """ObjectSetIntersectionType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSets: typing.List[ObjectSetDict]
    type: typing.Literal["intersect"]


class ObjectSetMethodInputType(pydantic.BaseModel):
    """
    ObjectSet which is the root of a MethodObjectSet definition.

    This feature is experimental and not yet generally available.
    """

    type: typing.Literal["methodInput"] = "methodInput"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetMethodInputTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetMethodInputTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetMethodInputTypeDict(typing_extensions.TypedDict):
    """
    ObjectSet which is the root of a MethodObjectSet definition.

    This feature is experimental and not yet generally available.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["methodInput"]


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

    def to_dict(self) -> "ObjectSetNearestNeighborsTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetNearestNeighborsTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetNearestNeighborsTypeDict(typing_extensions.TypedDict):
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

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict
    propertyIdentifier: PropertyIdentifierDict
    numNeighbors: int
    """
    The number of objects to return. If the number of documents in the objectType is less than the provided
    value, all objects will be returned. This value is limited to 1 &lt;= numNeighbors &lt;= 500.
    """

    query: NearestNeighborsQueryDict
    type: typing.Literal["nearestNeighbors"]


class ObjectSetReferenceType(pydantic.BaseModel):
    """ObjectSetReferenceType"""

    reference: ObjectSetRid
    type: typing.Literal["reference"] = "reference"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetReferenceTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetReferenceTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetReferenceTypeDict(typing_extensions.TypedDict):
    """ObjectSetReferenceType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reference: ObjectSetRid
    type: typing.Literal["reference"]


ObjectSetRid = core.RID
"""ObjectSetRid"""


class ObjectSetSearchAroundType(pydantic.BaseModel):
    """ObjectSetSearchAroundType"""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    link: LinkTypeApiName
    type: typing.Literal["searchAround"] = "searchAround"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetSearchAroundTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetSearchAroundTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetSearchAroundTypeDict(typing_extensions.TypedDict):
    """ObjectSetSearchAroundType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict
    link: LinkTypeApiName
    type: typing.Literal["searchAround"]


class ObjectSetStaticType(pydantic.BaseModel):
    """ObjectSetStaticType"""

    objects: typing.List[ObjectRid]
    type: typing.Literal["static"] = "static"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetStaticTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetStaticTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetStaticTypeDict(typing_extensions.TypedDict):
    """ObjectSetStaticType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objects: typing.List[ObjectRid]
    type: typing.Literal["static"]


class ObjectSetSubtractType(pydantic.BaseModel):
    """ObjectSetSubtractType"""

    object_sets: typing.List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]
    type: typing.Literal["subtract"] = "subtract"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetSubtractTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetSubtractTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetSubtractTypeDict(typing_extensions.TypedDict):
    """ObjectSetSubtractType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSets: typing.List[ObjectSetDict]
    type: typing.Literal["subtract"]


class ObjectSetUnionType(pydantic.BaseModel):
    """ObjectSetUnionType"""

    object_sets: typing.List[ObjectSet] = pydantic.Field(alias=str("objectSets"))  # type: ignore[literal-required]
    type: typing.Literal["union"] = "union"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectSetUnionTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetUnionTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetUnionTypeDict(typing_extensions.TypedDict):
    """ObjectSetUnionType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSets: typing.List[ObjectSetDict]
    type: typing.Literal["union"]


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

    def to_dict(self) -> "ObjectSetWithPropertiesTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectSetWithPropertiesTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectSetWithPropertiesTypeDict(typing_extensions.TypedDict):
    """
    ObjectSet which returns objects with additional derived properties.

    This feature is experimental and not yet generally available.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict
    derivedProperties: typing.Dict[DerivedPropertyApiName, DerivedPropertyDefinitionDict]
    """Map of the name of the derived property to return and its definition"""

    type: typing.Literal["withProperties"]


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

    def to_dict(self) -> "ObjectTypeEditsDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ObjectTypeEditsDict, self.model_dump(by_alias=True, exclude_none=True))


class ObjectTypeEditsDict(typing_extensions.TypedDict):
    """ObjectTypeEdits"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    editedObjectTypes: typing.List[ObjectTypeApiName]
    type: typing.Literal["largeScaleEdits"]


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

    def to_dict(self) -> "ObjectTypeFullMetadataDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectTypeFullMetadataDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectTypeFullMetadataDict(typing_extensions.TypedDict):
    """ObjectTypeFullMetadata"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: ObjectTypeV2Dict
    linkTypes: typing.List[LinkTypeSideV2Dict]
    implementsInterfaces: typing.List[InterfaceTypeApiName]
    """A list of interfaces that this object type implements."""

    implementsInterfaces2: typing.Dict[InterfaceTypeApiName, ObjectTypeInterfaceImplementationDict]
    """A list of interfaces that this object type implements and how it implements them."""

    sharedPropertyTypeMapping: typing.Dict[SharedPropertyTypeApiName, PropertyApiName]
    """
    A map from shared property type API name to backing local property API name for the shared property types 
    present on this object type.
    """


ObjectTypeId = str
"""The unique identifier (ID) for an object type. This can be viewed in [Ontology Manager](/docs/foundry/ontology-manager/overview/)."""


class ObjectTypeInterfaceImplementation(pydantic.BaseModel):
    """ObjectTypeInterfaceImplementation"""

    properties: typing.Dict[SharedPropertyTypeApiName, PropertyApiName]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectTypeInterfaceImplementationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ObjectTypeInterfaceImplementationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ObjectTypeInterfaceImplementationDict(typing_extensions.TypedDict):
    """ObjectTypeInterfaceImplementation"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    properties: typing.Dict[SharedPropertyTypeApiName, PropertyApiName]


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

    def to_dict(self) -> "ObjectTypeV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ObjectTypeV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class ObjectTypeV2Dict(typing_extensions.TypedDict):
    """Represents an object type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: ObjectTypeApiName
    displayName: core_models.DisplayName
    status: core_models.ReleaseStatus
    description: typing_extensions.NotRequired[str]
    """The description of the object type."""

    pluralDisplayName: str
    """The plural display name of the object type."""

    icon: IconDict
    primaryKey: PropertyApiName
    properties: typing.Dict[PropertyApiName, PropertyV2Dict]
    """A map of the properties of the object type."""

    rid: ObjectTypeRid
    titleProperty: PropertyApiName
    visibility: typing_extensions.NotRequired[ObjectTypeVisibility]


ObjectTypeVisibility = typing.Literal["NORMAL", "PROMINENT", "HIDDEN"]
"""The suggested visibility of the object type."""


class OneOfConstraint(pydantic.BaseModel):
    """The parameter has a manually predefined set of options."""

    options: typing.List[ParameterOption]
    other_values_allowed: bool = pydantic.Field(alias=str("otherValuesAllowed"))  # type: ignore[literal-required]
    """A flag denoting whether custom, user provided values will be considered valid. This is configured via the **Allowed "Other" value** toggle in the **Ontology Manager**."""

    type: typing.Literal["oneOf"] = "oneOf"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OneOfConstraintDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OneOfConstraintDict, self.model_dump(by_alias=True, exclude_none=True))


class OneOfConstraintDict(typing_extensions.TypedDict):
    """The parameter has a manually predefined set of options."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    options: typing.List[ParameterOptionDict]
    otherValuesAllowed: bool
    """A flag denoting whether custom, user provided values will be considered valid. This is configured via the **Allowed "Other" value** toggle in the **Ontology Manager**."""

    type: typing.Literal["oneOf"]


OntologyApiName = str
"""OntologyApiName"""


class OntologyArrayType(pydantic.BaseModel):
    """OntologyArrayType"""

    item_type: OntologyDataType = pydantic.Field(alias=str("itemType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyArrayTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OntologyArrayTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class OntologyArrayTypeDict(typing_extensions.TypedDict):
    """OntologyArrayType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    itemType: OntologyDataTypeDict
    type: typing.Literal["array"]


OntologyDataType = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateType",
        "OntologyStructType",
        "OntologySetType",
        "core_models.StringType",
        "core_models.ByteType",
        "core_models.DoubleType",
        "core_models.IntegerType",
        "core_models.FloatType",
        "core_models.AnyType",
        "core_models.LongType",
        "core_models.BooleanType",
        "core_models.CipherTextType",
        "core_models.MarkingType",
        "core_models.UnsupportedType",
        "OntologyArrayType",
        "OntologyObjectSetType",
        "core_models.BinaryType",
        "core_models.ShortType",
        "core_models.DecimalType",
        "OntologyMapType",
        "core_models.TimestampType",
        "OntologyObjectType",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the primitive types used by Palantir's Ontology-based products."""


OntologyDataTypeDict = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateTypeDict",
        "OntologyStructTypeDict",
        "OntologySetTypeDict",
        "core_models.StringTypeDict",
        "core_models.ByteTypeDict",
        "core_models.DoubleTypeDict",
        "core_models.IntegerTypeDict",
        "core_models.FloatTypeDict",
        "core_models.AnyTypeDict",
        "core_models.LongTypeDict",
        "core_models.BooleanTypeDict",
        "core_models.CipherTextTypeDict",
        "core_models.MarkingTypeDict",
        "core_models.UnsupportedTypeDict",
        "OntologyArrayTypeDict",
        "OntologyObjectSetTypeDict",
        "core_models.BinaryTypeDict",
        "core_models.ShortTypeDict",
        "core_models.DecimalTypeDict",
        "OntologyMapTypeDict",
        "core_models.TimestampTypeDict",
        "OntologyObjectTypeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the primitive types used by Palantir's Ontology-based products."""


class OntologyFullMetadata(pydantic.BaseModel):
    """OntologyFullMetadata"""

    ontology: OntologyV2
    object_types: typing.Dict[ObjectTypeApiName, ObjectTypeFullMetadata] = pydantic.Field(alias=str("objectTypes"))  # type: ignore[literal-required]
    action_types: typing.Dict[ActionTypeApiName, ActionTypeV2] = pydantic.Field(alias=str("actionTypes"))  # type: ignore[literal-required]
    query_types: typing.Dict[QueryApiName, QueryTypeV2] = pydantic.Field(alias=str("queryTypes"))  # type: ignore[literal-required]
    interface_types: typing.Dict[InterfaceTypeApiName, InterfaceType] = pydantic.Field(alias=str("interfaceTypes"))  # type: ignore[literal-required]
    shared_property_types: typing.Dict[SharedPropertyTypeApiName, SharedPropertyType] = pydantic.Field(alias=str("sharedPropertyTypes"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyFullMetadataDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            OntologyFullMetadataDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class OntologyFullMetadataDict(typing_extensions.TypedDict):
    """OntologyFullMetadata"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    ontology: OntologyV2Dict
    objectTypes: typing.Dict[ObjectTypeApiName, ObjectTypeFullMetadataDict]
    actionTypes: typing.Dict[ActionTypeApiName, ActionTypeV2Dict]
    queryTypes: typing.Dict[QueryApiName, QueryTypeV2Dict]
    interfaceTypes: typing.Dict[InterfaceTypeApiName, InterfaceTypeDict]
    sharedPropertyTypes: typing.Dict[SharedPropertyTypeApiName, SharedPropertyTypeDict]


OntologyIdentifier = str
"""Either an ontology rid or an ontology api name."""


class OntologyInterfaceObjectType(pydantic.BaseModel):
    """OntologyInterfaceObjectType"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["interfaceObject"] = "interfaceObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyInterfaceObjectTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            OntologyInterfaceObjectTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class OntologyInterfaceObjectTypeDict(typing_extensions.TypedDict):
    """OntologyInterfaceObjectType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    interfaceTypeApiName: InterfaceTypeApiName
    type: typing.Literal["interfaceObject"]


class OntologyMapType(pydantic.BaseModel):
    """OntologyMapType"""

    key_type: OntologyDataType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: OntologyDataType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["map"] = "map"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyMapTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OntologyMapTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class OntologyMapTypeDict(typing_extensions.TypedDict):
    """OntologyMapType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    keyType: OntologyDataTypeDict
    valueType: OntologyDataTypeDict
    type: typing.Literal["map"]


class OntologyObjectArrayType(pydantic.BaseModel):
    """OntologyObjectArrayType"""

    sub_type: ObjectPropertyType = pydantic.Field(alias=str("subType"))  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyObjectArrayTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            OntologyObjectArrayTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class OntologyObjectArrayTypeDict(typing_extensions.TypedDict):
    """OntologyObjectArrayType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: ObjectPropertyTypeDict
    type: typing.Literal["array"]


class OntologyObjectSetType(pydantic.BaseModel):
    """OntologyObjectSetType"""

    object_api_name: typing.Optional[ObjectTypeApiName] = pydantic.Field(alias=str("objectApiName"), default=None)  # type: ignore[literal-required]
    object_type_api_name: typing.Optional[ObjectTypeApiName] = pydantic.Field(alias=str("objectTypeApiName"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["objectSet"] = "objectSet"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyObjectSetTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            OntologyObjectSetTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class OntologyObjectSetTypeDict(typing_extensions.TypedDict):
    """OntologyObjectSetType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectApiName: typing_extensions.NotRequired[ObjectTypeApiName]
    objectTypeApiName: typing_extensions.NotRequired[ObjectTypeApiName]
    type: typing.Literal["objectSet"]


class OntologyObjectType(pydantic.BaseModel):
    """OntologyObjectType"""

    object_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectApiName"))  # type: ignore[literal-required]
    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    type: typing.Literal["object"] = "object"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyObjectTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            OntologyObjectTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class OntologyObjectTypeDict(typing_extensions.TypedDict):
    """OntologyObjectType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectApiName: ObjectTypeApiName
    objectTypeApiName: ObjectTypeApiName
    type: typing.Literal["object"]


class OntologyObjectTypeReferenceType(pydantic.BaseModel):
    """OntologyObjectTypeReferenceType"""

    type: typing.Literal["objectType"] = "objectType"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyObjectTypeReferenceTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            OntologyObjectTypeReferenceTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class OntologyObjectTypeReferenceTypeDict(typing_extensions.TypedDict):
    """OntologyObjectTypeReferenceType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["objectType"]


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

    def to_dict(self) -> "OntologySetTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OntologySetTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class OntologySetTypeDict(typing_extensions.TypedDict):
    """OntologySetType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    itemType: OntologyDataTypeDict
    type: typing.Literal["set"]


class OntologyStructField(pydantic.BaseModel):
    """OntologyStructField"""

    name: core_models.StructFieldName
    field_type: OntologyDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    required: bool
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyStructFieldDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            OntologyStructFieldDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class OntologyStructFieldDict(typing_extensions.TypedDict):
    """OntologyStructField"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: core_models.StructFieldName
    fieldType: OntologyDataTypeDict
    required: bool


class OntologyStructType(pydantic.BaseModel):
    """OntologyStructType"""

    fields: typing.List[OntologyStructField]
    type: typing.Literal["struct"] = "struct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyStructTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            OntologyStructTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class OntologyStructTypeDict(typing_extensions.TypedDict):
    """OntologyStructType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fields: typing.List[OntologyStructFieldDict]
    type: typing.Literal["struct"]


class OntologyV2(pydantic.BaseModel):
    """Metadata about an Ontology."""

    api_name: OntologyApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: str
    rid: OntologyRid
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OntologyV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class OntologyV2Dict(typing_extensions.TypedDict):
    """Metadata about an Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: OntologyApiName
    displayName: core_models.DisplayName
    description: str
    rid: OntologyRid


class OrQueryV2(pydantic.BaseModel):
    """Returns objects where at least 1 query is satisfied."""

    value: typing.List[SearchJsonQueryV2]
    type: typing.Literal["or"] = "or"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OrQueryV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OrQueryV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class OrQueryV2Dict(typing_extensions.TypedDict):
    """Returns objects where at least 1 query is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: typing.List[SearchJsonQueryV2Dict]
    type: typing.Literal["or"]


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
        "OneOfConstraint",
        "GroupMemberConstraint",
        "ObjectPropertyValueConstraint",
        "RangeConstraint",
        "ArraySizeConstraint",
        "ObjectQueryResultConstraint",
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


ParameterEvaluatedConstraintDict = typing_extensions.Annotated[
    typing.Union[
        "OneOfConstraintDict",
        "GroupMemberConstraintDict",
        "ObjectPropertyValueConstraintDict",
        "RangeConstraintDict",
        "ArraySizeConstraintDict",
        "ObjectQueryResultConstraintDict",
        "StringLengthConstraintDict",
        "StringRegexMatchConstraintDict",
        "UnevaluableConstraintDict",
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

    def to_dict(self) -> "ParameterEvaluationResultDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ParameterEvaluationResultDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ParameterEvaluationResultDict(typing_extensions.TypedDict):
    """Represents the validity of a parameter against the configured constraints."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    result: ValidationResult
    evaluatedConstraints: typing.List[ParameterEvaluatedConstraintDict]
    required: bool
    """Represents whether the parameter is a required input to the action."""


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

    def to_dict(self) -> "ParameterOptionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ParameterOptionDict, self.model_dump(by_alias=True, exclude_none=True))


class ParameterOptionDict(typing_extensions.TypedDict):
    """A possible value for the parameter. This is defined in the **Ontology Manager** by Actions admins."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    displayName: typing_extensions.NotRequired[core_models.DisplayName]
    value: typing_extensions.NotRequired[typing.Any]
    """An allowed configured value for a parameter within an action."""


class PolygonValue(pydantic.BaseModel):
    """PolygonValue"""

    coordinates: typing.List[geo_models.LinearRing]
    bbox: typing.Optional[geo_models.BBox] = None
    type: typing.Literal["Polygon"] = "Polygon"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "PolygonValueDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(PolygonValueDict, self.model_dump(by_alias=True, exclude_none=True))


class PolygonValueDict(typing_extensions.TypedDict):
    """PolygonValue"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    coordinates: typing.List[geo_models.LinearRing]
    bbox: typing_extensions.NotRequired[geo_models.BBox]
    type: typing.Literal["Polygon"]


class PreciseDuration(pydantic.BaseModel):
    """A measurement of duration."""

    value: int
    """The duration value."""

    unit: PreciseTimeUnit
    type: typing.Literal["duration"] = "duration"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "PreciseDurationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(PreciseDurationDict, self.model_dump(by_alias=True, exclude_none=True))


class PreciseDurationDict(typing_extensions.TypedDict):
    """A measurement of duration."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: int
    """The duration value."""

    unit: PreciseTimeUnit
    type: typing.Literal["duration"]


PreciseTimeUnit = typing.Literal[
    "NANOSECONDS", "SECONDS", "MINUTES", "HOURS", "DAYS", "WEEKS", "MONTHS", "YEARS"
]
"""The unit of duration."""


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

    def to_dict(self) -> "PropertyApiNameSelectorDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            PropertyApiNameSelectorDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class PropertyApiNameSelectorDict(typing_extensions.TypedDict):
    """A property api name that references properties to query on."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: PropertyApiName
    type: typing.Literal["property"]


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
    typing.Union["PropertyApiNameSelector", "StructFieldSelector"],
    pydantic.Field(discriminator="type"),
]
"""An identifier used to select properties or struct fields."""


PropertyIdentifierDict = typing_extensions.Annotated[
    typing.Union["PropertyApiNameSelectorDict", "StructFieldSelectorDict"],
    pydantic.Field(discriminator="type"),
]
"""An identifier used to select properties or struct fields."""


PropertyTypeRid = core.RID
"""PropertyTypeRid"""


PropertyTypeStatus = typing_extensions.Annotated[
    typing.Union[
        "DeprecatedPropertyTypeStatus",
        "ActivePropertyTypeStatus",
        "ExperimentalPropertyTypeStatus",
        "ExamplePropertyTypeStatus",
    ],
    pydantic.Field(discriminator="type"),
]
"""The status to indicate whether the PropertyType is either Experimental, Active, Deprecated, or Example."""


PropertyTypeStatusDict = typing_extensions.Annotated[
    typing.Union[
        "DeprecatedPropertyTypeStatusDict",
        "ActivePropertyTypeStatusDict",
        "ExperimentalPropertyTypeStatusDict",
        "ExamplePropertyTypeStatusDict",
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

    def to_dict(self) -> "PropertyV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(PropertyV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class PropertyV2Dict(typing_extensions.TypedDict):
    """Details about some property of an object."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    description: typing_extensions.NotRequired[str]
    displayName: typing_extensions.NotRequired[core_models.DisplayName]
    dataType: ObjectPropertyTypeDict
    rid: PropertyTypeRid
    status: typing_extensions.NotRequired[PropertyTypeStatusDict]
    visibility: typing_extensions.NotRequired[PropertyTypeVisibility]


PropertyValue = typing.Any
"""
Represents the value of a property in the following format.

| Type            | JSON encoding                                               | Example                                                                                            |
|---------------- |-------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Array           | array                                                       | `["alpha", "bravo", "charlie"]`                                                                    |
| Attachment      | JSON encoded `AttachmentProperty` object                    | `{"rid":"ri.blobster.main.attachment.2f944bae-5851-4204-8615-920c969a9f2e"}`                       |
| Boolean         | boolean                                                     | `true`                                                                                             |
| Byte            | number                                                      | `31`                                                                                               |
| CipherText      | string                                                      | `"CIPHER::ri.bellaso.main.cipher-channel.e414ab9e-b606-499a-a0e1-844fa296ba7e::unzjs3VifsTxuIpf1fH1CJ7OaPBr2bzMMdozPaZJtCii8vVG60yXIEmzoOJaEl9mfFFe::CIPHER"`                                                                                                                                                                                        |        
| Date            | ISO 8601 extended local date string                         | `"2021-05-01"`                                                                                     |
| Decimal         | string                                                      | `"2.718281828"`                                                                                    |
| Double          | number                                                      | `3.14159265`                                                                                       |
| Float           | number                                                      | `3.14159265`                                                                                       |
| GeoPoint        | geojson                                                     | `{"type":"Point","coordinates":[102.0,0.5]}`                                                       |
| GeoShape        | geojson                                                     | `{"type":"LineString","coordinates":[[102.0,0.0],[103.0,1.0],[104.0,0.0],[105.0,1.0]]}`            |
| Integer         | number                                                      | `238940`                                                                                           |
| Long            | string                                                      | `"58319870951433"`                                                                                 |
| MediaReference  | JSON encoded `MediaReference` object                        | `{"mimeType":"application/pdf","reference":{"type":"mediaSetViewItem","mediaSetViewItem":{"mediaSetRid":"ri.mio.main.media-set.4153d42f-ca4b-4e42-8ca5-8e6aa7edb642","mediaSetViewRid":"ri.mio.main.view.82a798ad-d637-4595-acc6-987bcf16629b","mediaItemRid":"ri.mio.main.media-item.001ec98b-1620-4814-9e17-8e9c4e536225"}}}`                       |
| Short           | number                                                      | `8739`                                                                                             |
| String          | string                                                      | `"Call me Ishmael"`                                                                                |
| Struct          | JSON object of struct field API name -> value               | {"firstName": "Alex", "lastName": "Karp"}                                                          |
| Timestamp       | ISO 8601 extended offset date-time string in UTC zone       | `"2021-01-04T05:00:00Z"`                                                                           |
| Timeseries      | JSON encoded `TimeseriesProperty` object or seriesId string | `{"seriesId": "wellPressureSeriesId", "syncRid": ri.time-series-catalog.main.sync.04f5ac1f-91bf-44f9-a51f-4f34e06e42df"}` or `{"templateRid": "ri.codex-emu.main.template.367cac64-e53b-4653-b111-f61856a63df9", "templateVersion": "0.0.0"}` or `"wellPressureSeriesId"`|                                                                           |

Note that for backwards compatibility, the Boolean, Byte, Double, Float, Integer, and Short types can also be encoded as JSON strings.
"""


PropertyValueEscapedString = str
"""Represents the value of a property in string format. This is used in URL parameters."""


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
        "EntrySetType",
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
        "OntologyObjectSetType",
        "TwoDimensionalAggregation",
        "OntologyObjectType",
        "core_models.TimestampType",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Query parameters or outputs."""


QueryDataTypeDict = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateTypeDict",
        "QueryStructTypeDict",
        "QuerySetTypeDict",
        "core_models.StringTypeDict",
        "EntrySetTypeDict",
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
        "OntologyObjectSetTypeDict",
        "TwoDimensionalAggregationDict",
        "OntologyObjectTypeDict",
        "core_models.TimestampTypeDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by Ontology Query parameters or outputs."""


class QueryParameterV2(pydantic.BaseModel):
    """Details about a parameter of a query."""

    description: typing.Optional[str] = None
    data_type: QueryDataType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "QueryParameterV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(QueryParameterV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class QueryParameterV2Dict(typing_extensions.TypedDict):
    """Details about a parameter of a query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    description: typing_extensions.NotRequired[str]
    dataType: QueryDataTypeDict


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

    name: core_models.StructFieldName
    field_type: QueryDataType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "QueryStructFieldDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(QueryStructFieldDict, self.model_dump(by_alias=True, exclude_none=True))


class QueryStructFieldDict(typing_extensions.TypedDict):
    """QueryStructField"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: core_models.StructFieldName
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

    def to_dict(self) -> "QueryTypeV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(QueryTypeV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class QueryTypeV2Dict(typing_extensions.TypedDict):
    """Represents a query type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: QueryApiName
    description: typing_extensions.NotRequired[str]
    displayName: typing_extensions.NotRequired[core_models.DisplayName]
    parameters: typing.Dict[ParameterId, QueryParameterV2Dict]
    output: QueryDataTypeDict
    rid: FunctionRid
    version: FunctionVersion


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

    def to_dict(self) -> "RangeConstraintDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(RangeConstraintDict, self.model_dump(by_alias=True, exclude_none=True))


class RangeConstraintDict(typing_extensions.TypedDict):
    """The parameter value must be within the defined range."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    lt: typing_extensions.NotRequired[typing.Any]
    """Less than"""

    lte: typing_extensions.NotRequired[typing.Any]
    """Less than or equal"""

    gt: typing_extensions.NotRequired[typing.Any]
    """Greater than"""

    gte: typing_extensions.NotRequired[typing.Any]
    """Greater than or equal"""

    type: typing.Literal["range"]


class RelativeTime(pydantic.BaseModel):
    """A relative time, such as "3 days before" or "2 hours after" the current moment."""

    when: RelativeTimeRelation
    value: int
    unit: RelativeTimeSeriesTimeUnit
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "RelativeTimeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(RelativeTimeDict, self.model_dump(by_alias=True, exclude_none=True))


class RelativeTimeDict(typing_extensions.TypedDict):
    """A relative time, such as "3 days before" or "2 hours after" the current moment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    when: RelativeTimeRelation
    value: int
    unit: RelativeTimeSeriesTimeUnit


class RelativeTimeRange(pydantic.BaseModel):
    """A relative time range for a time series query."""

    start_time: typing.Optional[RelativeTime] = pydantic.Field(alias=str("startTime"), default=None)  # type: ignore[literal-required]
    end_time: typing.Optional[RelativeTime] = pydantic.Field(alias=str("endTime"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["relative"] = "relative"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "RelativeTimeRangeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(RelativeTimeRangeDict, self.model_dump(by_alias=True, exclude_none=True))


class RelativeTimeRangeDict(typing_extensions.TypedDict):
    """A relative time range for a time series query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    startTime: typing_extensions.NotRequired[RelativeTimeDict]
    endTime: typing_extensions.NotRequired[RelativeTimeDict]
    type: typing.Literal["relative"]


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

    def to_dict(self) -> "RollingAggregateWindowPointsDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            RollingAggregateWindowPointsDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class RollingAggregateWindowPointsDict(typing_extensions.TypedDict):
    """Number of points in each window."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    count: int
    type: typing.Literal["pointsCount"]


SdkPackageName = str
"""SdkPackageName"""


SearchJsonQueryV2 = typing_extensions.Annotated[
    typing.Union[
        "OrQueryV2",
        "InQuery",
        "DoesNotIntersectPolygonQuery",
        "LtQueryV2",
        "DoesNotIntersectBoundingBoxQuery",
        "EqualsQueryV2",
        "ContainsAllTermsQuery",
        "GtQueryV2",
        "WithinDistanceOfQuery",
        "WithinBoundingBoxQuery",
        "ContainsQueryV2",
        "NotQueryV2",
        "IntersectsBoundingBoxQuery",
        "AndQueryV2",
        "IsNullQueryV2",
        "ContainsAllTermsInOrderPrefixLastTerm",
        "ContainsAnyTermQuery",
        "GteQueryV2",
        "ContainsAllTermsInOrderQuery",
        "WithinPolygonQuery",
        "IntersectsPolygonQuery",
        "LteQueryV2",
        "StartsWithQuery",
    ],
    pydantic.Field(discriminator="type"),
]
"""SearchJsonQueryV2"""


SearchJsonQueryV2Dict = typing_extensions.Annotated[
    typing.Union[
        "OrQueryV2Dict",
        "InQueryDict",
        "DoesNotIntersectPolygonQueryDict",
        "LtQueryV2Dict",
        "DoesNotIntersectBoundingBoxQueryDict",
        "EqualsQueryV2Dict",
        "ContainsAllTermsQueryDict",
        "GtQueryV2Dict",
        "WithinDistanceOfQueryDict",
        "WithinBoundingBoxQueryDict",
        "ContainsQueryV2Dict",
        "NotQueryV2Dict",
        "IntersectsBoundingBoxQueryDict",
        "AndQueryV2Dict",
        "IsNullQueryV2Dict",
        "ContainsAllTermsInOrderPrefixLastTermDict",
        "ContainsAnyTermQueryDict",
        "GteQueryV2Dict",
        "ContainsAllTermsInOrderQueryDict",
        "WithinPolygonQueryDict",
        "IntersectsPolygonQueryDict",
        "LteQueryV2Dict",
        "StartsWithQueryDict",
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

    def to_dict(self) -> "SearchObjectsResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchObjectsResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchObjectsResponseV2Dict(typing_extensions.TypedDict):
    """SearchObjectsResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[OntologyObjectV2]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    totalCount: core_models.TotalCount


SearchOrderByType = typing.Literal["fields", "relevance"]
"""SearchOrderByType"""


class SearchOrderByV2(pydantic.BaseModel):
    """Specifies the ordering of search results by a field and an ordering direction or by relevance if scores are required in a nearestNeighbors query. By default `orderType` is set to `fields`."""

    order_type: typing.Optional[SearchOrderByType] = pydantic.Field(alias=str("orderType"), default=None)  # type: ignore[literal-required]
    fields: typing.List[SearchOrderingV2]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchOrderByV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(SearchOrderByV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class SearchOrderByV2Dict(typing_extensions.TypedDict):
    """Specifies the ordering of search results by a field and an ordering direction or by relevance if scores are required in a nearestNeighbors query. By default `orderType` is set to `fields`."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    orderType: typing_extensions.NotRequired[SearchOrderByType]
    fields: typing.List[SearchOrderingV2Dict]


class SearchOrderingV2(pydantic.BaseModel):
    """SearchOrderingV2"""

    field: PropertyApiName
    direction: typing.Optional[str] = None
    """Specifies the ordering direction (can be either `asc` or `desc`)"""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchOrderingV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(SearchOrderingV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class SearchOrderingV2Dict(typing_extensions.TypedDict):
    """SearchOrderingV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    direction: typing_extensions.NotRequired[str]
    """Specifies the ordering direction (can be either `asc` or `desc`)"""


SelectedPropertyApiName = str
"""
By default, anytime an object is requested, every property belonging to that object is returned.
The response can be filtered to only include certain properties using the `properties` query parameter.

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

    def to_dict(self) -> "SelectedPropertyApproximateDistinctAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SelectedPropertyApproximateDistinctAggregationDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class SelectedPropertyApproximateDistinctAggregationDict(typing_extensions.TypedDict):
    """Computes an approximate number of distinct values for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    selectedPropertyApiName: PropertyApiName
    type: typing.Literal["approximateDistinct"]


class SelectedPropertyApproximatePercentileAggregation(pydantic.BaseModel):
    """Computes the approximate percentile value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    approximate_percentile: float = pydantic.Field(alias=str("approximatePercentile"))  # type: ignore[literal-required]
    type: typing.Literal["approximatePercentile"] = "approximatePercentile"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SelectedPropertyApproximatePercentileAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SelectedPropertyApproximatePercentileAggregationDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class SelectedPropertyApproximatePercentileAggregationDict(typing_extensions.TypedDict):
    """Computes the approximate percentile value for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    selectedPropertyApiName: PropertyApiName
    approximatePercentile: float
    type: typing.Literal["approximatePercentile"]


class SelectedPropertyAvgAggregation(pydantic.BaseModel):
    """Computes the average value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["avg"] = "avg"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SelectedPropertyAvgAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SelectedPropertyAvgAggregationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SelectedPropertyAvgAggregationDict(typing_extensions.TypedDict):
    """Computes the average value for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    selectedPropertyApiName: PropertyApiName
    type: typing.Literal["avg"]


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

    def to_dict(self) -> "SelectedPropertyCollectListAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SelectedPropertyCollectListAggregationDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class SelectedPropertyCollectListAggregationDict(typing_extensions.TypedDict):
    """
    Lists all values of a property up to the specified limit. The maximum supported limit is 100, by default.

    NOTE: A separate count aggregation should be used to determine the total count of values, to account for
    a possible truncation of the returned list.

    Ignores objects for which a property is absent, so the returned list will contain non-null values only.
    Returns an empty list when none of the objects have values for a provided property.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    selectedPropertyApiName: PropertyApiName
    limit: int
    """Maximum number of values to collect. The maximum supported limit is 100."""

    type: typing.Literal["collectList"]


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

    def to_dict(self) -> "SelectedPropertyCollectSetAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SelectedPropertyCollectSetAggregationDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class SelectedPropertyCollectSetAggregationDict(typing_extensions.TypedDict):
    """
    Lists all distinct values of a property up to the specified limit. The maximum supported limit is 100.

    NOTE: A separate cardinality / exactCardinality aggregation should be used to determine the total count of
    values, to account for a possible truncation of the returned set.

    Ignores objects for which a property is absent, so the returned list will contain non-null values only.
    Returns an empty list when none of the objects have values for a provided property.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    selectedPropertyApiName: PropertyApiName
    limit: int
    """Maximum number of values to collect. The maximum supported limit is 100."""

    type: typing.Literal["collectSet"]


class SelectedPropertyCountAggregation(pydantic.BaseModel):
    """Computes the total count of objects."""

    type: typing.Literal["count"] = "count"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SelectedPropertyCountAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SelectedPropertyCountAggregationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SelectedPropertyCountAggregationDict(typing_extensions.TypedDict):
    """Computes the total count of objects."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["count"]


class SelectedPropertyExactDistinctAggregation(pydantic.BaseModel):
    """Computes an exact number of distinct values for the provided field. May be slower than an approximate distinct aggregation."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["exactDistinct"] = "exactDistinct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SelectedPropertyExactDistinctAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SelectedPropertyExactDistinctAggregationDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class SelectedPropertyExactDistinctAggregationDict(typing_extensions.TypedDict):
    """Computes an exact number of distinct values for the provided field. May be slower than an approximate distinct aggregation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    selectedPropertyApiName: PropertyApiName
    type: typing.Literal["exactDistinct"]


class SelectedPropertyExpression(pydantic.BaseModel):
    """Definition for a selected property over a MethodObjectSet."""

    object_set: MethodObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    operation: SelectedPropertyOperation
    type: typing.Literal["selection"] = "selection"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SelectedPropertyExpressionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SelectedPropertyExpressionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SelectedPropertyExpressionDict(typing_extensions.TypedDict):
    """Definition for a selected property over a MethodObjectSet."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: MethodObjectSetDict
    operation: SelectedPropertyOperationDict
    type: typing.Literal["selection"]


class SelectedPropertyMaxAggregation(pydantic.BaseModel):
    """Computes the maximum value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["max"] = "max"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SelectedPropertyMaxAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SelectedPropertyMaxAggregationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SelectedPropertyMaxAggregationDict(typing_extensions.TypedDict):
    """Computes the maximum value for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    selectedPropertyApiName: PropertyApiName
    type: typing.Literal["max"]


class SelectedPropertyMinAggregation(pydantic.BaseModel):
    """Computes the minimum value for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["min"] = "min"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SelectedPropertyMinAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SelectedPropertyMinAggregationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SelectedPropertyMinAggregationDict(typing_extensions.TypedDict):
    """Computes the minimum value for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    selectedPropertyApiName: PropertyApiName
    type: typing.Literal["min"]


SelectedPropertyOperation = typing_extensions.Annotated[
    typing.Union[
        "SelectedPropertyApproximateDistinctAggregation",
        "SelectedPropertyMinAggregation",
        "SelectedPropertyAvgAggregation",
        "SelectedPropertyMaxAggregation",
        "SelectedPropertyApproximatePercentileAggregation",
        "GetSelectedPropertyOperation",
        "SelectedPropertyCountAggregation",
        "SelectedPropertySumAggregation",
        "SelectedPropertyCollectListAggregation",
        "SelectedPropertyExactDistinctAggregation",
        "SelectedPropertyCollectSetAggregation",
    ],
    pydantic.Field(discriminator="type"),
]
"""Operation on a selected property, can be an aggregation function or retrieval of a single selected property"""


SelectedPropertyOperationDict = typing_extensions.Annotated[
    typing.Union[
        "SelectedPropertyApproximateDistinctAggregationDict",
        "SelectedPropertyMinAggregationDict",
        "SelectedPropertyAvgAggregationDict",
        "SelectedPropertyMaxAggregationDict",
        "SelectedPropertyApproximatePercentileAggregationDict",
        "GetSelectedPropertyOperationDict",
        "SelectedPropertyCountAggregationDict",
        "SelectedPropertySumAggregationDict",
        "SelectedPropertyCollectListAggregationDict",
        "SelectedPropertyExactDistinctAggregationDict",
        "SelectedPropertyCollectSetAggregationDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""Operation on a selected property, can be an aggregation function or retrieval of a single selected property"""


class SelectedPropertySumAggregation(pydantic.BaseModel):
    """Computes the sum of values for the provided field."""

    selected_property_api_name: PropertyApiName = pydantic.Field(alias=str("selectedPropertyApiName"))  # type: ignore[literal-required]
    type: typing.Literal["sum"] = "sum"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SelectedPropertySumAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SelectedPropertySumAggregationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SelectedPropertySumAggregationDict(typing_extensions.TypedDict):
    """Computes the sum of values for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    selectedPropertyApiName: PropertyApiName
    type: typing.Literal["sum"]


class SharedPropertyType(pydantic.BaseModel):
    """A property type that can be shared across object types."""

    rid: SharedPropertyTypeRid
    api_name: SharedPropertyTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """A short text that describes the SharedPropertyType."""

    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SharedPropertyTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SharedPropertyTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )


SharedPropertyTypeApiName = str
"""
The name of the shared property type in the API in lowerCamelCase format. To find the API name for your
shared property type, use the `List shared property types` endpoint or check the **Ontology Manager**.
"""


class SharedPropertyTypeDict(typing_extensions.TypedDict):
    """A property type that can be shared across object types."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: SharedPropertyTypeRid
    apiName: SharedPropertyTypeApiName
    displayName: core_models.DisplayName
    description: typing_extensions.NotRequired[str]
    """A short text that describes the SharedPropertyType."""

    dataType: ObjectPropertyTypeDict


SharedPropertyTypeRid = core.RID
"""The unique resource identifier of an shared property type, useful for interacting with other Foundry APIs."""


class StartsWithQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field starts with the provided value. Allows you to specify a property to
    query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: typing.Optional[PropertyApiName] = None
    property_identifier: typing.Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]
    value: str
    type: typing.Literal["startsWith"] = "startsWith"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "StartsWithQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(StartsWithQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class StartsWithQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field starts with the provided value. Allows you to specify a property to
    query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: str
    type: typing.Literal["startsWith"]


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

    def to_dict(self) -> "StringLengthConstraintDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            StringLengthConstraintDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class StringLengthConstraintDict(typing_extensions.TypedDict):
    """
    The parameter value must have a length within the defined range.
    *This range is always inclusive.*
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    lt: typing_extensions.NotRequired[typing.Any]
    """Less than"""

    lte: typing_extensions.NotRequired[typing.Any]
    """Less than or equal"""

    gt: typing_extensions.NotRequired[typing.Any]
    """Greater than"""

    gte: typing_extensions.NotRequired[typing.Any]
    """Greater than or equal"""

    type: typing.Literal["stringLength"]


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

    def to_dict(self) -> "StringRegexMatchConstraintDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            StringRegexMatchConstraintDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class StringRegexMatchConstraintDict(typing_extensions.TypedDict):
    """The parameter value must match a predefined regular expression."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    regex: str
    """The regular expression configured in the **Ontology Manager**."""

    configuredFailureMessage: typing_extensions.NotRequired[str]
    """
    The message indicating that the regular expression was not matched.
    This is configured per parameter in the **Ontology Manager**.
    """

    type: typing.Literal["stringRegexMatch"]


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

    def to_dict(self) -> "StructFieldSelectorDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            StructFieldSelectorDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class StructFieldSelectorDict(typing_extensions.TypedDict):
    """
    A combination of a property API name and a struct field API name used to select struct fields. Note that you can
    still select struct properties with only a 'PropertyApiNameSelector'; the queries will then become 'OR' queries
    across the fields of the struct property, and derived property expressions will operate on the whole struct
    where applicable.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyApiName: PropertyApiName
    structFieldApiName: StructFieldApiName
    type: typing.Literal["structField"]


class StructFieldType(pydantic.BaseModel):
    """StructFieldType"""

    api_name: StructFieldApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "StructFieldTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(StructFieldTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class StructFieldTypeDict(typing_extensions.TypedDict):
    """StructFieldType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: StructFieldApiName
    dataType: ObjectPropertyTypeDict


class StructType(pydantic.BaseModel):
    """StructType"""

    struct_field_types: typing.List[StructFieldType] = pydantic.Field(alias=str("structFieldTypes"))  # type: ignore[literal-required]
    type: typing.Literal["struct"] = "struct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "StructTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(StructTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class StructTypeDict(typing_extensions.TypedDict):
    """StructType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    structFieldTypes: typing.List[StructFieldTypeDict]
    type: typing.Literal["struct"]


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

    def to_dict(self) -> "SubmissionCriteriaEvaluationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SubmissionCriteriaEvaluationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SubmissionCriteriaEvaluationDict(typing_extensions.TypedDict):
    """
    Contains the status of the **submission criteria**.
    **Submission criteria** are the prerequisites that need to be satisfied before an Action can be applied.
    These are configured in the **Ontology Manager**.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    configuredFailureMessage: typing_extensions.NotRequired[str]
    """
    The message indicating one of the **submission criteria** was not satisfied.
    This is configured per **submission criteria** in the **Ontology Manager**.
    """

    result: ValidationResult


class SubtractPropertyExpression(pydantic.BaseModel):
    """Subtracts the right numeric value from the left numeric value."""

    left: DerivedPropertyDefinition
    right: DerivedPropertyDefinition
    type: typing.Literal["subtract"] = "subtract"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SubtractPropertyExpressionDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SubtractPropertyExpressionDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SubtractPropertyExpressionDict(typing_extensions.TypedDict):
    """Subtracts the right numeric value from the left numeric value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    left: DerivedPropertyDefinitionDict
    right: DerivedPropertyDefinitionDict
    type: typing.Literal["subtract"]


class SumAggregationV2(pydantic.BaseModel):
    """Computes the sum of values for the provided field."""

    field: PropertyApiName
    name: typing.Optional[AggregationMetricName] = None
    direction: typing.Optional[OrderByDirection] = None
    type: typing.Literal["sum"] = "sum"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SumAggregationV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(SumAggregationV2Dict, self.model_dump(by_alias=True, exclude_none=True))


class SumAggregationV2Dict(typing_extensions.TypedDict):
    """Computes the sum of values for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: PropertyApiName
    name: typing_extensions.NotRequired[AggregationMetricName]
    direction: typing_extensions.NotRequired[OrderByDirection]
    type: typing.Literal["sum"]


class SyncApplyActionResponseV2(pydantic.BaseModel):
    """SyncApplyActionResponseV2"""

    validation: typing.Optional[ValidateActionResponseV2] = None
    edits: typing.Optional[ActionResults] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SyncApplyActionResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SyncApplyActionResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SyncApplyActionResponseV2Dict(typing_extensions.TypedDict):
    """SyncApplyActionResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    validation: typing_extensions.NotRequired[ValidateActionResponseV2Dict]
    edits: typing_extensions.NotRequired[ActionResultsDict]


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


TimeRange = typing_extensions.Annotated[
    typing.Union["AbsoluteTimeRange", "RelativeTimeRange"], pydantic.Field(discriminator="type")
]
"""An absolute or relative range for a time series query."""


TimeRangeDict = typing_extensions.Annotated[
    typing.Union["AbsoluteTimeRangeDict", "RelativeTimeRangeDict"],
    pydantic.Field(discriminator="type"),
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


TimeSeriesAggregationStrategyDict = typing_extensions.Annotated[
    typing.Union[
        "TimeSeriesRollingAggregateDict",
        "TimeSeriesPeriodicAggregateDict",
        "TimeSeriesCumulativeAggregateDict",
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

    def to_dict(self) -> "TimeSeriesCumulativeAggregateDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            TimeSeriesCumulativeAggregateDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class TimeSeriesCumulativeAggregateDict(typing_extensions.TypedDict):
    """
    The cumulative aggregate is calculated progressively for each point in the input time series,
    considering all preceding points up to and including the current point.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["cumulative"]


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
    alignment_timestamp: datetime = pydantic.Field(alias=str("alignmentTimestamp"))  # type: ignore[literal-required]
    window_type: TimeSeriesWindowType = pydantic.Field(alias=str("windowType"))  # type: ignore[literal-required]
    type: typing.Literal["periodic"] = "periodic"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "TimeSeriesPeriodicAggregateDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            TimeSeriesPeriodicAggregateDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class TimeSeriesPeriodicAggregateDict(typing_extensions.TypedDict):
    """
    Aggregates values over discrete, periodic windows for a given time series.

    A periodic window divides the time series into windows of fixed durations.
    For each window, an aggregate function is applied to the points within that window. The result is a time series
    with values representing the aggregate for each window. Windows with no data points are not included
    in the output.

    Periodic aggregation is useful for downsampling a continuous stream of data to larger granularities such as
    hourly, daily, monthly.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    windowSize: PreciseDurationDict
    alignmentTimestamp: datetime
    windowType: TimeSeriesWindowType
    type: typing.Literal["periodic"]


class TimeSeriesPoint(pydantic.BaseModel):
    """A time and value pair."""

    time: datetime
    """An ISO 8601 timestamp"""

    value: typing.Any
    """An object which is either an enum String or a double number."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "TimeSeriesPointDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(TimeSeriesPointDict, self.model_dump(by_alias=True, exclude_none=True))


class TimeSeriesPointDict(typing_extensions.TypedDict):
    """A time and value pair."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    time: datetime
    """An ISO 8601 timestamp"""

    value: typing.Any
    """An object which is either an enum String or a double number."""


class TimeSeriesRollingAggregate(pydantic.BaseModel):
    """TimeSeriesRollingAggregate"""

    window_size: TimeSeriesRollingAggregateWindow = pydantic.Field(alias=str("windowSize"))  # type: ignore[literal-required]
    type: typing.Literal["rolling"] = "rolling"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "TimeSeriesRollingAggregateDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            TimeSeriesRollingAggregateDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class TimeSeriesRollingAggregateDict(typing_extensions.TypedDict):
    """TimeSeriesRollingAggregate"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    windowSize: TimeSeriesRollingAggregateWindowDict
    type: typing.Literal["rolling"]


TimeSeriesRollingAggregateWindow = typing_extensions.Annotated[
    typing.Union["PreciseDuration", "RollingAggregateWindowPoints"],
    pydantic.Field(discriminator="type"),
]
"""
A rolling window is a moving subset of data points that ends at the current timestamp (inclusive)
and spans a specified duration (window size). As new data points are added, old points fall out of the
window if they are outside the specified duration.

Rolling windows are commonly used for smoothing data, detecting trends, and reducing noise
in time series analysis.
"""


TimeSeriesRollingAggregateWindowDict = typing_extensions.Annotated[
    typing.Union["PreciseDurationDict", "RollingAggregateWindowPointsDict"],
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


class UnevaluableConstraint(pydantic.BaseModel):
    """
    The parameter cannot be evaluated because it depends on another parameter or object set that can't be evaluated.
    This can happen when a parameter's allowed values are defined by another parameter that is missing or invalid.
    """

    type: typing.Literal["unevaluable"] = "unevaluable"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "UnevaluableConstraintDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            UnevaluableConstraintDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class UnevaluableConstraintDict(typing_extensions.TypedDict):
    """
    The parameter cannot be evaluated because it depends on another parameter or object set that can't be evaluated.
    This can happen when a parameter's allowed values are defined by another parameter that is missing or invalid.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["unevaluable"]


class ValidateActionResponseV2(pydantic.BaseModel):
    """ValidateActionResponseV2"""

    result: ValidationResult
    submission_criteria: typing.List[SubmissionCriteriaEvaluation] = pydantic.Field(alias=str("submissionCriteria"))  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, ParameterEvaluationResult]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValidateActionResponseV2Dict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValidateActionResponseV2Dict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValidateActionResponseV2Dict(typing_extensions.TypedDict):
    """ValidateActionResponseV2"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    result: ValidationResult
    submissionCriteria: typing.List[SubmissionCriteriaEvaluationDict]
    parameters: typing.Dict[ParameterId, ParameterEvaluationResultDict]


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


class WithinBoundingBoxPoint(pydantic.BaseModel):
    """WithinBoundingBoxPoint"""

    coordinates: geo_models.Position
    bbox: typing.Optional[geo_models.BBox] = None
    type: typing.Literal["Point"] = "Point"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "WithinBoundingBoxPointDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            WithinBoundingBoxPointDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class WithinBoundingBoxPointDict(typing_extensions.TypedDict):
    """WithinBoundingBoxPoint"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    coordinates: geo_models.Position
    bbox: typing_extensions.NotRequired[geo_models.BBox]
    type: typing.Literal["Point"]


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

    def to_dict(self) -> "WithinBoundingBoxQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            WithinBoundingBoxQueryDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class WithinBoundingBoxQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field contains a point within the bounding box provided. Allows you to
    specify a property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied,
    but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: BoundingBoxValueDict
    type: typing.Literal["withinBoundingBox"]


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

    def to_dict(self) -> "WithinDistanceOfQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            WithinDistanceOfQueryDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class WithinDistanceOfQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field contains a point within the distance provided of the center point.
    Allows you to specify a property to query on by a variety of means. Either `field` or `propertyIdentifier`
    must be supplied, but not both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: CenterPointDict
    type: typing.Literal["withinDistanceOf"]


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

    def to_dict(self) -> "WithinPolygonQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            WithinPolygonQueryDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class WithinPolygonQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field contains a point within the polygon provided. Allows you to specify a
    property to query on by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not
    both.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: typing_extensions.NotRequired[PropertyApiName]
    propertyIdentifier: typing_extensions.NotRequired[PropertyIdentifierDict]
    value: PolygonValueDict
    type: typing.Literal["withinPolygon"]


from foundry.v2.core import models as core_models  # noqa: E402
from foundry.v2.geo import models as geo_models  # noqa: E402

__all__ = [
    "AbsoluteTimeRange",
    "AbsoluteTimeRangeDict",
    "AbsoluteValuePropertyExpression",
    "AbsoluteValuePropertyExpressionDict",
    "ActionParameterArrayType",
    "ActionParameterArrayTypeDict",
    "ActionParameterType",
    "ActionParameterTypeDict",
    "ActionParameterV2",
    "ActionParameterV2Dict",
    "ActionResults",
    "ActionResultsDict",
    "ActionRid",
    "ActionTypeApiName",
    "ActionTypeRid",
    "ActionTypeV2",
    "ActionTypeV2Dict",
    "ActivePropertyTypeStatus",
    "ActivePropertyTypeStatusDict",
    "AddLink",
    "AddLinkDict",
    "AddObject",
    "AddObjectDict",
    "AddPropertyExpression",
    "AddPropertyExpressionDict",
    "AggregateObjectsResponseItemV2",
    "AggregateObjectsResponseItemV2Dict",
    "AggregateObjectsResponseV2",
    "AggregateObjectsResponseV2Dict",
    "AggregateTimeSeries",
    "AggregateTimeSeriesDict",
    "AggregationAccuracy",
    "AggregationAccuracyRequest",
    "AggregationDurationGroupingV2",
    "AggregationDurationGroupingV2Dict",
    "AggregationExactGroupingV2",
    "AggregationExactGroupingV2Dict",
    "AggregationFixedWidthGroupingV2",
    "AggregationFixedWidthGroupingV2Dict",
    "AggregationGroupByV2",
    "AggregationGroupByV2Dict",
    "AggregationGroupKeyV2",
    "AggregationGroupValueV2",
    "AggregationMetricName",
    "AggregationMetricResultV2",
    "AggregationMetricResultV2Dict",
    "AggregationRangeV2",
    "AggregationRangeV2Dict",
    "AggregationRangesGroupingV2",
    "AggregationRangesGroupingV2Dict",
    "AggregationV2",
    "AggregationV2Dict",
    "AndQueryV2",
    "AndQueryV2Dict",
    "ApplyActionMode",
    "ApplyActionRequestOptions",
    "ApplyActionRequestOptionsDict",
    "ApproximateDistinctAggregationV2",
    "ApproximateDistinctAggregationV2Dict",
    "ApproximatePercentileAggregationV2",
    "ApproximatePercentileAggregationV2Dict",
    "ArraySizeConstraint",
    "ArraySizeConstraintDict",
    "ArtifactRepositoryRid",
    "AttachmentMetadataResponse",
    "AttachmentMetadataResponseDict",
    "AttachmentRid",
    "AttachmentV2",
    "AttachmentV2Dict",
    "AvgAggregationV2",
    "AvgAggregationV2Dict",
    "BatchActionObjectEdit",
    "BatchActionObjectEditDict",
    "BatchActionObjectEdits",
    "BatchActionObjectEditsDict",
    "BatchActionResults",
    "BatchActionResultsDict",
    "BatchApplyActionRequestItem",
    "BatchApplyActionRequestItemDict",
    "BatchApplyActionRequestOptions",
    "BatchApplyActionRequestOptionsDict",
    "BatchApplyActionResponseV2",
    "BatchApplyActionResponseV2Dict",
    "BatchReturnEditsMode",
    "BoundingBoxValue",
    "BoundingBoxValueDict",
    "CenterPoint",
    "CenterPointDict",
    "CenterPointTypes",
    "CenterPointTypesDict",
    "ContainsAllTermsInOrderPrefixLastTerm",
    "ContainsAllTermsInOrderPrefixLastTermDict",
    "ContainsAllTermsInOrderQuery",
    "ContainsAllTermsInOrderQueryDict",
    "ContainsAllTermsQuery",
    "ContainsAllTermsQueryDict",
    "ContainsAnyTermQuery",
    "ContainsAnyTermQueryDict",
    "ContainsQueryV2",
    "ContainsQueryV2Dict",
    "CountAggregationV2",
    "CountAggregationV2Dict",
    "CountObjectsResponseV2",
    "CountObjectsResponseV2Dict",
    "CreateInterfaceObjectRule",
    "CreateInterfaceObjectRuleDict",
    "CreateLinkRule",
    "CreateLinkRuleDict",
    "CreateObjectRule",
    "CreateObjectRuleDict",
    "CreateTemporaryObjectSetResponseV2",
    "CreateTemporaryObjectSetResponseV2Dict",
    "DataValue",
    "DeleteInterfaceObjectRule",
    "DeleteInterfaceObjectRuleDict",
    "DeleteLink",
    "DeleteLinkDict",
    "DeleteLinkRule",
    "DeleteLinkRuleDict",
    "DeleteObject",
    "DeleteObjectDict",
    "DeleteObjectRule",
    "DeleteObjectRuleDict",
    "DeprecatedPropertyTypeStatus",
    "DeprecatedPropertyTypeStatusDict",
    "DerivedPropertyApiName",
    "DerivedPropertyDefinition",
    "DerivedPropertyDefinitionDict",
    "DividePropertyExpression",
    "DividePropertyExpressionDict",
    "DoesNotIntersectBoundingBoxQuery",
    "DoesNotIntersectBoundingBoxQueryDict",
    "DoesNotIntersectPolygonQuery",
    "DoesNotIntersectPolygonQueryDict",
    "DoubleVector",
    "DoubleVectorDict",
    "EntrySetType",
    "EntrySetTypeDict",
    "EqualsQueryV2",
    "EqualsQueryV2Dict",
    "ExactDistinctAggregationV2",
    "ExactDistinctAggregationV2Dict",
    "ExamplePropertyTypeStatus",
    "ExamplePropertyTypeStatusDict",
    "ExecuteQueryResponse",
    "ExecuteQueryResponseDict",
    "ExperimentalPropertyTypeStatus",
    "ExperimentalPropertyTypeStatusDict",
    "ExtractDatePart",
    "ExtractPropertyExpression",
    "ExtractPropertyExpressionDict",
    "FilterValue",
    "FunctionRid",
    "FunctionVersion",
    "FuzzyV2",
    "GetSelectedPropertyOperation",
    "GetSelectedPropertyOperationDict",
    "GreatestPropertyExpression",
    "GreatestPropertyExpressionDict",
    "GroupMemberConstraint",
    "GroupMemberConstraintDict",
    "GtQueryV2",
    "GtQueryV2Dict",
    "GteQueryV2",
    "GteQueryV2Dict",
    "Icon",
    "IconDict",
    "InQuery",
    "InQueryDict",
    "InterfaceLinkType",
    "InterfaceLinkTypeApiName",
    "InterfaceLinkTypeCardinality",
    "InterfaceLinkTypeDict",
    "InterfaceLinkTypeLinkedEntityApiName",
    "InterfaceLinkTypeLinkedEntityApiNameDict",
    "InterfaceLinkTypeRid",
    "InterfaceSharedPropertyType",
    "InterfaceSharedPropertyTypeDict",
    "InterfaceType",
    "InterfaceTypeApiName",
    "InterfaceTypeDict",
    "InterfaceTypeRid",
    "IntersectsBoundingBoxQuery",
    "IntersectsBoundingBoxQueryDict",
    "IntersectsPolygonQuery",
    "IntersectsPolygonQueryDict",
    "IsNullQueryV2",
    "IsNullQueryV2Dict",
    "LeastPropertyExpression",
    "LeastPropertyExpressionDict",
    "LinkSideObject",
    "LinkSideObjectDict",
    "LinkTypeApiName",
    "LinkTypeRid",
    "LinkTypeSideCardinality",
    "LinkTypeSideV2",
    "LinkTypeSideV2Dict",
    "LinkedInterfaceTypeApiName",
    "LinkedInterfaceTypeApiNameDict",
    "LinkedObjectTypeApiName",
    "LinkedObjectTypeApiNameDict",
    "ListActionTypesResponseV2",
    "ListActionTypesResponseV2Dict",
    "ListAttachmentsResponseV2",
    "ListAttachmentsResponseV2Dict",
    "ListInterfaceTypesResponse",
    "ListInterfaceTypesResponseDict",
    "ListLinkedObjectsResponseV2",
    "ListLinkedObjectsResponseV2Dict",
    "ListObjectTypesV2Response",
    "ListObjectTypesV2ResponseDict",
    "ListObjectsResponseV2",
    "ListObjectsResponseV2Dict",
    "ListOutgoingLinkTypesResponseV2",
    "ListOutgoingLinkTypesResponseV2Dict",
    "ListQueryTypesResponseV2",
    "ListQueryTypesResponseV2Dict",
    "LoadObjectSetResponseV2",
    "LoadObjectSetResponseV2Dict",
    "LogicRule",
    "LogicRuleDict",
    "LtQueryV2",
    "LtQueryV2Dict",
    "LteQueryV2",
    "LteQueryV2Dict",
    "MaxAggregationV2",
    "MaxAggregationV2Dict",
    "MethodObjectSet",
    "MethodObjectSetDict",
    "MinAggregationV2",
    "MinAggregationV2Dict",
    "ModifyInterfaceObjectRule",
    "ModifyInterfaceObjectRuleDict",
    "ModifyObject",
    "ModifyObjectDict",
    "ModifyObjectRule",
    "ModifyObjectRuleDict",
    "MultiplyPropertyExpression",
    "MultiplyPropertyExpressionDict",
    "NearestNeighborsQuery",
    "NearestNeighborsQueryDict",
    "NearestNeighborsQueryText",
    "NearestNeighborsQueryTextDict",
    "NegatePropertyExpression",
    "NegatePropertyExpressionDict",
    "NotQueryV2",
    "NotQueryV2Dict",
    "ObjectEdit",
    "ObjectEditDict",
    "ObjectEdits",
    "ObjectEditsDict",
    "ObjectPropertyType",
    "ObjectPropertyTypeDict",
    "ObjectPropertyValueConstraint",
    "ObjectPropertyValueConstraintDict",
    "ObjectQueryResultConstraint",
    "ObjectQueryResultConstraintDict",
    "ObjectRid",
    "ObjectSet",
    "ObjectSetAsBaseObjectTypesType",
    "ObjectSetAsBaseObjectTypesTypeDict",
    "ObjectSetAsTypeType",
    "ObjectSetAsTypeTypeDict",
    "ObjectSetBaseType",
    "ObjectSetBaseTypeDict",
    "ObjectSetDict",
    "ObjectSetFilterType",
    "ObjectSetFilterTypeDict",
    "ObjectSetInterfaceBaseType",
    "ObjectSetInterfaceBaseTypeDict",
    "ObjectSetIntersectionType",
    "ObjectSetIntersectionTypeDict",
    "ObjectSetMethodInputType",
    "ObjectSetMethodInputTypeDict",
    "ObjectSetNearestNeighborsType",
    "ObjectSetNearestNeighborsTypeDict",
    "ObjectSetReferenceType",
    "ObjectSetReferenceTypeDict",
    "ObjectSetRid",
    "ObjectSetSearchAroundType",
    "ObjectSetSearchAroundTypeDict",
    "ObjectSetStaticType",
    "ObjectSetStaticTypeDict",
    "ObjectSetSubtractType",
    "ObjectSetSubtractTypeDict",
    "ObjectSetUnionType",
    "ObjectSetUnionTypeDict",
    "ObjectSetWithPropertiesType",
    "ObjectSetWithPropertiesTypeDict",
    "ObjectTypeApiName",
    "ObjectTypeEdits",
    "ObjectTypeEditsDict",
    "ObjectTypeFullMetadata",
    "ObjectTypeFullMetadataDict",
    "ObjectTypeId",
    "ObjectTypeInterfaceImplementation",
    "ObjectTypeInterfaceImplementationDict",
    "ObjectTypeRid",
    "ObjectTypeV2",
    "ObjectTypeV2Dict",
    "ObjectTypeVisibility",
    "OneOfConstraint",
    "OneOfConstraintDict",
    "OntologyApiName",
    "OntologyArrayType",
    "OntologyArrayTypeDict",
    "OntologyDataType",
    "OntologyDataTypeDict",
    "OntologyFullMetadata",
    "OntologyFullMetadataDict",
    "OntologyIdentifier",
    "OntologyInterfaceObjectType",
    "OntologyInterfaceObjectTypeDict",
    "OntologyMapType",
    "OntologyMapTypeDict",
    "OntologyObjectArrayType",
    "OntologyObjectArrayTypeDict",
    "OntologyObjectSetType",
    "OntologyObjectSetTypeDict",
    "OntologyObjectType",
    "OntologyObjectTypeDict",
    "OntologyObjectTypeReferenceType",
    "OntologyObjectTypeReferenceTypeDict",
    "OntologyObjectV2",
    "OntologyRid",
    "OntologySetType",
    "OntologySetTypeDict",
    "OntologyStructField",
    "OntologyStructFieldDict",
    "OntologyStructType",
    "OntologyStructTypeDict",
    "OntologyV2",
    "OntologyV2Dict",
    "OrQueryV2",
    "OrQueryV2Dict",
    "OrderBy",
    "OrderByDirection",
    "ParameterEvaluatedConstraint",
    "ParameterEvaluatedConstraintDict",
    "ParameterEvaluationResult",
    "ParameterEvaluationResultDict",
    "ParameterId",
    "ParameterOption",
    "ParameterOptionDict",
    "PolygonValue",
    "PolygonValueDict",
    "PreciseDuration",
    "PreciseDurationDict",
    "PreciseTimeUnit",
    "PrimaryKeyValue",
    "PropertyApiName",
    "PropertyApiNameSelector",
    "PropertyApiNameSelectorDict",
    "PropertyFilter",
    "PropertyId",
    "PropertyIdentifier",
    "PropertyIdentifierDict",
    "PropertyTypeRid",
    "PropertyTypeStatus",
    "PropertyTypeStatusDict",
    "PropertyTypeVisibility",
    "PropertyV2",
    "PropertyV2Dict",
    "PropertyValue",
    "PropertyValueEscapedString",
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
    "QueryParameterV2",
    "QueryParameterV2Dict",
    "QueryRuntimeErrorParameter",
    "QuerySetType",
    "QuerySetTypeDict",
    "QueryStructField",
    "QueryStructFieldDict",
    "QueryStructType",
    "QueryStructTypeDict",
    "QueryTypeV2",
    "QueryTypeV2Dict",
    "QueryUnionType",
    "QueryUnionTypeDict",
    "RangeConstraint",
    "RangeConstraintDict",
    "RelativeTime",
    "RelativeTimeDict",
    "RelativeTimeRange",
    "RelativeTimeRangeDict",
    "RelativeTimeRelation",
    "RelativeTimeSeriesTimeUnit",
    "ReturnEditsMode",
    "RollingAggregateWindowPoints",
    "RollingAggregateWindowPointsDict",
    "SdkPackageName",
    "SearchJsonQueryV2",
    "SearchJsonQueryV2Dict",
    "SearchObjectsResponseV2",
    "SearchObjectsResponseV2Dict",
    "SearchOrderByType",
    "SearchOrderByV2",
    "SearchOrderByV2Dict",
    "SearchOrderingV2",
    "SearchOrderingV2Dict",
    "SelectedPropertyApiName",
    "SelectedPropertyApproximateDistinctAggregation",
    "SelectedPropertyApproximateDistinctAggregationDict",
    "SelectedPropertyApproximatePercentileAggregation",
    "SelectedPropertyApproximatePercentileAggregationDict",
    "SelectedPropertyAvgAggregation",
    "SelectedPropertyAvgAggregationDict",
    "SelectedPropertyCollectListAggregation",
    "SelectedPropertyCollectListAggregationDict",
    "SelectedPropertyCollectSetAggregation",
    "SelectedPropertyCollectSetAggregationDict",
    "SelectedPropertyCountAggregation",
    "SelectedPropertyCountAggregationDict",
    "SelectedPropertyExactDistinctAggregation",
    "SelectedPropertyExactDistinctAggregationDict",
    "SelectedPropertyExpression",
    "SelectedPropertyExpressionDict",
    "SelectedPropertyMaxAggregation",
    "SelectedPropertyMaxAggregationDict",
    "SelectedPropertyMinAggregation",
    "SelectedPropertyMinAggregationDict",
    "SelectedPropertyOperation",
    "SelectedPropertyOperationDict",
    "SelectedPropertySumAggregation",
    "SelectedPropertySumAggregationDict",
    "SharedPropertyType",
    "SharedPropertyTypeApiName",
    "SharedPropertyTypeDict",
    "SharedPropertyTypeRid",
    "StartsWithQuery",
    "StartsWithQueryDict",
    "StreamingOutputFormat",
    "StringLengthConstraint",
    "StringLengthConstraintDict",
    "StringRegexMatchConstraint",
    "StringRegexMatchConstraintDict",
    "StructFieldApiName",
    "StructFieldSelector",
    "StructFieldSelectorDict",
    "StructFieldType",
    "StructFieldTypeDict",
    "StructType",
    "StructTypeDict",
    "SubmissionCriteriaEvaluation",
    "SubmissionCriteriaEvaluationDict",
    "SubtractPropertyExpression",
    "SubtractPropertyExpressionDict",
    "SumAggregationV2",
    "SumAggregationV2Dict",
    "SyncApplyActionResponseV2",
    "SyncApplyActionResponseV2Dict",
    "ThreeDimensionalAggregation",
    "ThreeDimensionalAggregationDict",
    "TimeRange",
    "TimeRangeDict",
    "TimeSeriesAggregationMethod",
    "TimeSeriesAggregationStrategy",
    "TimeSeriesAggregationStrategyDict",
    "TimeSeriesCumulativeAggregate",
    "TimeSeriesCumulativeAggregateDict",
    "TimeSeriesPeriodicAggregate",
    "TimeSeriesPeriodicAggregateDict",
    "TimeSeriesPoint",
    "TimeSeriesPointDict",
    "TimeSeriesRollingAggregate",
    "TimeSeriesRollingAggregateDict",
    "TimeSeriesRollingAggregateWindow",
    "TimeSeriesRollingAggregateWindowDict",
    "TimeSeriesWindowType",
    "TimeUnit",
    "TwoDimensionalAggregation",
    "TwoDimensionalAggregationDict",
    "UnevaluableConstraint",
    "UnevaluableConstraintDict",
    "ValidateActionResponseV2",
    "ValidateActionResponseV2Dict",
    "ValidationResult",
    "ValueType",
    "WithinBoundingBoxPoint",
    "WithinBoundingBoxPointDict",
    "WithinBoundingBoxQuery",
    "WithinBoundingBoxQueryDict",
    "WithinDistanceOfQuery",
    "WithinDistanceOfQueryDict",
    "WithinPolygonQuery",
    "WithinPolygonQueryDict",
]
