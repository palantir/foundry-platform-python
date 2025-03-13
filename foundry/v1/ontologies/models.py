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

ActionRid = core.RID
"""The unique resource identifier for an action."""


class ActionType(pydantic.BaseModel):
    """Represents an action type in the Ontology."""

    api_name: ActionTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    parameters: typing.Dict[ParameterId, Parameter]
    rid: ActionTypeRid
    operations: typing.List[LogicRule]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ActionTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ActionTypeDict, self.model_dump(by_alias=True, exclude_none=True))


ActionTypeApiName = str
"""
The name of the action type in the API. To find the API name for your Action Type, use the `List action types`
endpoint or check the **Ontology Manager**.
"""


class ActionTypeDict(typing_extensions.TypedDict):
    """Represents an action type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: ActionTypeApiName
    description: typing_extensions.NotRequired[str]
    displayName: typing_extensions.NotRequired[core_models.DisplayName]
    status: core_models.ReleaseStatus
    parameters: typing.Dict[ParameterId, ParameterDict]
    rid: ActionTypeRid
    operations: typing.List[LogicRuleDict]


ActionTypeRid = core.RID
"""The unique resource identifier of an action type, useful for interacting with other Foundry APIs."""


class AggregateObjectsResponse(pydantic.BaseModel):
    """AggregateObjectsResponse"""

    excluded_items: typing.Optional[int] = pydantic.Field(alias=str("excludedItems"), default=None)  # type: ignore[literal-required]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[AggregateObjectsResponseItem]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregateObjectsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregateObjectsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregateObjectsResponseDict(typing_extensions.TypedDict):
    """AggregateObjectsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    excludedItems: typing_extensions.NotRequired[int]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[AggregateObjectsResponseItemDict]


class AggregateObjectsResponseItem(pydantic.BaseModel):
    """AggregateObjectsResponseItem"""

    group: typing.Dict[AggregationGroupKey, AggregationGroupValue]
    metrics: typing.List[AggregationMetricResult]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregateObjectsResponseItemDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregateObjectsResponseItemDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregateObjectsResponseItemDict(typing_extensions.TypedDict):
    """AggregateObjectsResponseItem"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    group: typing.Dict[AggregationGroupKey, AggregationGroupValue]
    metrics: typing.List[AggregationMetricResultDict]


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


AggregationDict = typing_extensions.Annotated[
    typing.Union[
        "ApproximateDistinctAggregationDict",
        "MinAggregationDict",
        "AvgAggregationDict",
        "MaxAggregationDict",
        "CountAggregationDict",
        "SumAggregationDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies an aggregation function."""


class AggregationDurationGrouping(pydantic.BaseModel):
    """
    Divides objects into groups according to an interval. Note that this grouping applies only on date types.
    The interval uses the ISO 8601 notation. For example, "PT1H2M34S" represents a duration of 3754 seconds.
    """

    field: FieldNameV1
    duration: Duration
    type: typing.Literal["duration"] = "duration"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregationDurationGroupingDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregationDurationGroupingDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregationDurationGroupingDict(typing_extensions.TypedDict):
    """
    Divides objects into groups according to an interval. Note that this grouping applies only on date types.
    The interval uses the ISO 8601 notation. For example, "PT1H2M34S" represents a duration of 3754 seconds.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    duration: Duration
    type: typing.Literal["duration"]


class AggregationExactGrouping(pydantic.BaseModel):
    """Divides objects into groups according to an exact value."""

    field: FieldNameV1
    max_group_count: typing.Optional[int] = pydantic.Field(alias=str("maxGroupCount"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["exact"] = "exact"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregationExactGroupingDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregationExactGroupingDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregationExactGroupingDict(typing_extensions.TypedDict):
    """Divides objects into groups according to an exact value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    maxGroupCount: typing_extensions.NotRequired[int]
    type: typing.Literal["exact"]


class AggregationFixedWidthGrouping(pydantic.BaseModel):
    """Divides objects into groups with the specified width."""

    field: FieldNameV1
    fixed_width: int = pydantic.Field(alias=str("fixedWidth"))  # type: ignore[literal-required]
    type: typing.Literal["fixedWidth"] = "fixedWidth"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregationFixedWidthGroupingDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregationFixedWidthGroupingDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregationFixedWidthGroupingDict(typing_extensions.TypedDict):
    """Divides objects into groups with the specified width."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    fixedWidth: int
    type: typing.Literal["fixedWidth"]


AggregationGroupBy = typing_extensions.Annotated[
    typing.Union[
        "AggregationDurationGrouping",
        "AggregationFixedWidthGrouping",
        "AggregationRangesGrouping",
        "AggregationExactGrouping",
    ],
    pydantic.Field(discriminator="type"),
]
"""Specifies a grouping for aggregation results."""


AggregationGroupByDict = typing_extensions.Annotated[
    typing.Union[
        "AggregationDurationGroupingDict",
        "AggregationFixedWidthGroupingDict",
        "AggregationRangesGroupingDict",
        "AggregationExactGroupingDict",
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


class AggregationMetricResult(pydantic.BaseModel):
    """AggregationMetricResult"""

    name: str
    value: typing.Optional[float] = None
    """TBD"""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregationMetricResultDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregationMetricResultDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregationMetricResultDict(typing_extensions.TypedDict):
    """AggregationMetricResult"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: str
    value: typing_extensions.NotRequired[float]
    """TBD"""


class AggregationRange(pydantic.BaseModel):
    """Specifies a date range from an inclusive start date to an exclusive end date."""

    lt: typing.Optional[typing.Any] = None
    """Exclusive end date."""

    lte: typing.Optional[typing.Any] = None
    """Inclusive end date."""

    gt: typing.Optional[typing.Any] = None
    """Exclusive start date."""

    gte: typing.Optional[typing.Any] = None
    """Inclusive start date."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregationRangeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AggregationRangeDict, self.model_dump(by_alias=True, exclude_none=True))


class AggregationRangeDict(typing_extensions.TypedDict):
    """Specifies a date range from an inclusive start date to an exclusive end date."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    lt: typing_extensions.NotRequired[typing.Any]
    """Exclusive end date."""

    lte: typing_extensions.NotRequired[typing.Any]
    """Inclusive end date."""

    gt: typing_extensions.NotRequired[typing.Any]
    """Exclusive start date."""

    gte: typing_extensions.NotRequired[typing.Any]
    """Inclusive start date."""


class AggregationRangesGrouping(pydantic.BaseModel):
    """Divides objects into groups according to specified ranges."""

    field: FieldNameV1
    ranges: typing.List[AggregationRange]
    type: typing.Literal["ranges"] = "ranges"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AggregationRangesGroupingDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AggregationRangesGroupingDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AggregationRangesGroupingDict(typing_extensions.TypedDict):
    """Divides objects into groups according to specified ranges."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    ranges: typing.List[AggregationRangeDict]
    type: typing.Literal["ranges"]


class AllTermsQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field contains all of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching.
    """

    field: FieldNameV1
    value: str
    fuzzy: typing.Optional[Fuzzy] = None
    type: typing.Literal["allTerms"] = "allTerms"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AllTermsQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AllTermsQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class AllTermsQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field contains all of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    value: str
    fuzzy: typing_extensions.NotRequired[Fuzzy]
    type: typing.Literal["allTerms"]


class AndQuery(pydantic.BaseModel):
    """Returns objects where every query is satisfied."""

    value: typing.List[SearchJsonQuery]
    type: typing.Literal["and"] = "and"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AndQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AndQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class AndQueryDict(typing_extensions.TypedDict):
    """Returns objects where every query is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: typing.List[SearchJsonQueryDict]
    type: typing.Literal["and"]


class AnyTermQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field contains any of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching.
    """

    field: FieldNameV1
    value: str
    fuzzy: typing.Optional[Fuzzy] = None
    type: typing.Literal["anyTerm"] = "anyTerm"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AnyTermQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AnyTermQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class AnyTermQueryDict(typing_extensions.TypedDict):
    """
    Returns objects where the specified field contains any of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    value: str
    fuzzy: typing_extensions.NotRequired[Fuzzy]
    type: typing.Literal["anyTerm"]


ApplyActionMode = typing.Literal["VALIDATE_ONLY", "VALIDATE_AND_EXECUTE"]
"""ApplyActionMode"""


class ApplyActionRequest(pydantic.BaseModel):
    """ApplyActionRequest"""

    parameters: typing.Dict[ParameterId, typing.Optional[DataValue]]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ApplyActionRequestDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ApplyActionRequestDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ApplyActionRequestDict(typing_extensions.TypedDict):
    """ApplyActionRequest"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameters: typing.Dict[ParameterId, typing.Optional[DataValue]]


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


class ApplyActionResponse(pydantic.BaseModel):
    """ApplyActionResponse"""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ApplyActionResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ApplyActionResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ApplyActionResponseDict(typing_extensions.TypedDict):
    """ApplyActionResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


class ApproximateDistinctAggregation(pydantic.BaseModel):
    """Computes an approximate number of distinct values for the provided field."""

    field: FieldNameV1
    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["approximateDistinct"] = "approximateDistinct"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ApproximateDistinctAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ApproximateDistinctAggregationDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ApproximateDistinctAggregationDict(typing_extensions.TypedDict):
    """Computes an approximate number of distinct values for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    name: typing_extensions.NotRequired[AggregationMetricName]
    type: typing.Literal["approximateDistinct"]


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


AttachmentRid = core.RID
"""The unique resource identifier of an attachment."""


class AvgAggregation(pydantic.BaseModel):
    """Computes the average value for the provided field."""

    field: FieldNameV1
    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["avg"] = "avg"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AvgAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(AvgAggregationDict, self.model_dump(by_alias=True, exclude_none=True))


class AvgAggregationDict(typing_extensions.TypedDict):
    """Computes the average value for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    name: typing_extensions.NotRequired[AggregationMetricName]
    type: typing.Literal["avg"]


class BatchApplyActionResponse(pydantic.BaseModel):
    """BatchApplyActionResponse"""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "BatchApplyActionResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            BatchApplyActionResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class BatchApplyActionResponseDict(typing_extensions.TypedDict):
    """BatchApplyActionResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


class ContainsQuery(pydantic.BaseModel):
    """Returns objects where the specified array contains a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["contains"] = "contains"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ContainsQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ContainsQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class ContainsQueryDict(typing_extensions.TypedDict):
    """Returns objects where the specified array contains a value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["contains"]


class CountAggregation(pydantic.BaseModel):
    """Computes the total count of objects."""

    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["count"] = "count"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CountAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(CountAggregationDict, self.model_dump(by_alias=True, exclude_none=True))


class CountAggregationDict(typing_extensions.TypedDict):
    """Computes the total count of objects."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: typing_extensions.NotRequired[AggregationMetricName]
    type: typing.Literal["count"]


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


DerivedPropertyApiName = str
"""The name of the derived property that will be returned."""


Duration = str
"""An ISO 8601 formatted duration."""


class EntrySetTypeDict(typing_extensions.TypedDict):
    """EntrySetType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    keyType: QueryDataTypeDict
    valueType: QueryDataTypeDict
    type: typing.Literal["entrySet"]


class EqualsQuery(pydantic.BaseModel):
    """Returns objects where the specified field is equal to a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["eq"] = "eq"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "EqualsQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(EqualsQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class EqualsQueryDict(typing_extensions.TypedDict):
    """Returns objects where the specified field is equal to a value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["eq"]


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


class GtQuery(pydantic.BaseModel):
    """Returns objects where the specified field is greater than a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["gt"] = "gt"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GtQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GtQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class GtQueryDict(typing_extensions.TypedDict):
    """Returns objects where the specified field is greater than a value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["gt"]


class GteQuery(pydantic.BaseModel):
    """Returns objects where the specified field is greater than or equal to a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["gte"] = "gte"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GteQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GteQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class GteQueryDict(typing_extensions.TypedDict):
    """Returns objects where the specified field is greater than or equal to a value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["gte"]


InterfaceTypeApiName = str
"""
The name of the interface type in the API in UpperCamelCase format. To find the API name for your interface
type, use the `List interface types` endpoint or check the **Ontology Manager**.
"""


InterfaceTypeRid = core.RID
"""The unique resource identifier of an interface, useful for interacting with other Foundry APIs."""


class IsNullQuery(pydantic.BaseModel):
    """Returns objects based on the existence of the specified field."""

    field: FieldNameV1
    value: bool
    type: typing.Literal["isNull"] = "isNull"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "IsNullQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(IsNullQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class IsNullQueryDict(typing_extensions.TypedDict):
    """Returns objects based on the existence of the specified field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    value: bool
    type: typing.Literal["isNull"]


LinkTypeApiName = str
"""
The name of the link type in the API. To find the API name for your Link Type, check the **Ontology Manager**
application.
"""


class LinkTypeSide(pydantic.BaseModel):
    """LinkTypeSide"""

    api_name: LinkTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    cardinality: LinkTypeSideCardinality
    foreign_key_property_api_name: typing.Optional[PropertyApiName] = pydantic.Field(alias=str("foreignKeyPropertyApiName"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "LinkTypeSideDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(LinkTypeSideDict, self.model_dump(by_alias=True, exclude_none=True))


LinkTypeSideCardinality = typing.Literal["ONE", "MANY"]
"""LinkTypeSideCardinality"""


class LinkTypeSideDict(typing_extensions.TypedDict):
    """LinkTypeSide"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: LinkTypeApiName
    displayName: core_models.DisplayName
    status: core_models.ReleaseStatus
    objectTypeApiName: ObjectTypeApiName
    cardinality: LinkTypeSideCardinality
    foreignKeyPropertyApiName: typing_extensions.NotRequired[PropertyApiName]


class ListActionTypesResponse(pydantic.BaseModel):
    """ListActionTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[ActionType]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListActionTypesResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListActionTypesResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListActionTypesResponseDict(typing_extensions.TypedDict):
    """ListActionTypesResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[ActionTypeDict]


class ListLinkedObjectsResponse(pydantic.BaseModel):
    """ListLinkedObjectsResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[OntologyObject]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListLinkedObjectsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListLinkedObjectsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListLinkedObjectsResponseDict(typing_extensions.TypedDict):
    """ListLinkedObjectsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[OntologyObjectDict]


class ListObjectTypesResponse(pydantic.BaseModel):
    """ListObjectTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[ObjectType]
    """The list of object types in the current page."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListObjectTypesResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListObjectTypesResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListObjectTypesResponseDict(typing_extensions.TypedDict):
    """ListObjectTypesResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[ObjectTypeDict]
    """The list of object types in the current page."""


class ListObjectsResponse(pydantic.BaseModel):
    """ListObjectsResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[OntologyObject]
    """The list of objects in the current page."""

    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListObjectsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListObjectsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListObjectsResponseDict(typing_extensions.TypedDict):
    """ListObjectsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[OntologyObjectDict]
    """The list of objects in the current page."""

    totalCount: core_models.TotalCount


class ListOntologiesResponse(pydantic.BaseModel):
    """ListOntologiesResponse"""

    data: typing.List[Ontology]
    """The list of Ontologies the user has access to."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListOntologiesResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListOntologiesResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListOntologiesResponseDict(typing_extensions.TypedDict):
    """ListOntologiesResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[OntologyDict]
    """The list of Ontologies the user has access to."""


class ListOutgoingLinkTypesResponse(pydantic.BaseModel):
    """ListOutgoingLinkTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[LinkTypeSide]
    """The list of link type sides in the current page."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListOutgoingLinkTypesResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListOutgoingLinkTypesResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListOutgoingLinkTypesResponseDict(typing_extensions.TypedDict):
    """ListOutgoingLinkTypesResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[LinkTypeSideDict]
    """The list of link type sides in the current page."""


class ListQueryTypesResponse(pydantic.BaseModel):
    """ListQueryTypesResponse"""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[QueryType]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListQueryTypesResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListQueryTypesResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListQueryTypesResponseDict(typing_extensions.TypedDict):
    """ListQueryTypesResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    data: typing.List[QueryTypeDict]


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


class LtQuery(pydantic.BaseModel):
    """Returns objects where the specified field is less than a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["lt"] = "lt"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "LtQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(LtQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class LtQueryDict(typing_extensions.TypedDict):
    """Returns objects where the specified field is less than a value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["lt"]


class LteQuery(pydantic.BaseModel):
    """Returns objects where the specified field is less than or equal to a value."""

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["lte"] = "lte"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "LteQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(LteQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class LteQueryDict(typing_extensions.TypedDict):
    """Returns objects where the specified field is less than or equal to a value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    value: PropertyValue
    type: typing.Literal["lte"]


class MaxAggregation(pydantic.BaseModel):
    """Computes the maximum value for the provided field."""

    field: FieldNameV1
    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["max"] = "max"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MaxAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MaxAggregationDict, self.model_dump(by_alias=True, exclude_none=True))


class MaxAggregationDict(typing_extensions.TypedDict):
    """Computes the maximum value for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    name: typing_extensions.NotRequired[AggregationMetricName]
    type: typing.Literal["max"]


class MinAggregation(pydantic.BaseModel):
    """Computes the minimum value for the provided field."""

    field: FieldNameV1
    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["min"] = "min"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MinAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MinAggregationDict, self.model_dump(by_alias=True, exclude_none=True))


class MinAggregationDict(typing_extensions.TypedDict):
    """Computes the minimum value for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    name: typing_extensions.NotRequired[AggregationMetricName]
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


class NotQuery(pydantic.BaseModel):
    """Returns objects where the query is not satisfied."""

    value: SearchJsonQuery
    type: typing.Literal["not"] = "not"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "NotQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(NotQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class NotQueryDict(typing_extensions.TypedDict):
    """Returns objects where the query is not satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: SearchJsonQueryDict
    type: typing.Literal["not"]


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


ObjectSetRid = core.RID
"""ObjectSetRid"""


class ObjectType(pydantic.BaseModel):
    """Represents an object type in the Ontology."""

    api_name: ObjectTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
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
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ObjectTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ObjectTypeDict, self.model_dump(by_alias=True, exclude_none=True))


ObjectTypeApiName = str
"""
The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the
`List object types` endpoint or check the **Ontology Manager**.
"""


class ObjectTypeDict(typing_extensions.TypedDict):
    """Represents an object type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: ObjectTypeApiName
    displayName: typing_extensions.NotRequired[core_models.DisplayName]
    status: core_models.ReleaseStatus
    description: typing_extensions.NotRequired[str]
    """The description of the object type."""

    visibility: typing_extensions.NotRequired[ObjectTypeVisibility]
    primaryKey: typing.List[PropertyApiName]
    """The primary key of the object. This is a list of properties that can be used to uniquely identify the object."""

    properties: typing.Dict[PropertyApiName, PropertyDict]
    """A map of the properties of the object type."""

    rid: ObjectTypeRid


ObjectTypeRid = core.RID
"""The unique resource identifier of an object type, useful for interacting with other Foundry APIs."""


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


class Ontology(pydantic.BaseModel):
    """Metadata about an Ontology."""

    api_name: OntologyApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: str
    rid: OntologyRid
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OntologyDict, self.model_dump(by_alias=True, exclude_none=True))


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


class OntologyDict(typing_extensions.TypedDict):
    """Metadata about an Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: OntologyApiName
    displayName: core_models.DisplayName
    description: str
    rid: OntologyRid


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


class OntologyObject(pydantic.BaseModel):
    """Represents an object in the Ontology."""

    properties: typing.Dict[PropertyApiName, typing.Optional[PropertyValue]]
    """A map of the property values of the object."""

    rid: ObjectRid
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OntologyObjectDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OntologyObjectDict, self.model_dump(by_alias=True, exclude_none=True))


class OntologyObjectDict(typing_extensions.TypedDict):
    """Represents an object in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    properties: typing.Dict[PropertyApiName, typing.Optional[PropertyValue]]
    """A map of the property values of the object."""

    rid: ObjectRid


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


class OrQuery(pydantic.BaseModel):
    """Returns objects where at least 1 query is satisfied."""

    value: typing.List[SearchJsonQuery]
    type: typing.Literal["or"] = "or"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OrQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OrQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class OrQueryDict(typing_extensions.TypedDict):
    """Returns objects where at least 1 query is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: typing.List[SearchJsonQueryDict]
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


class Parameter(pydantic.BaseModel):
    """Details about a parameter of an action or query."""

    description: typing.Optional[str] = None
    base_type: ValueType = pydantic.Field(alias=str("baseType"))  # type: ignore[literal-required]
    data_type: typing.Optional[OntologyDataType] = pydantic.Field(alias=str("dataType"), default=None)  # type: ignore[literal-required]
    required: bool
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ParameterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ParameterDict, self.model_dump(by_alias=True, exclude_none=True))


class ParameterDict(typing_extensions.TypedDict):
    """Details about a parameter of an action or query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    description: typing_extensions.NotRequired[str]
    baseType: ValueType
    dataType: typing_extensions.NotRequired[OntologyDataTypeDict]
    required: bool


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


class PhraseQuery(pydantic.BaseModel):
    """Returns objects where the specified field contains the provided value as a substring."""

    field: FieldNameV1
    value: str
    type: typing.Literal["phrase"] = "phrase"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "PhraseQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(PhraseQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class PhraseQueryDict(typing_extensions.TypedDict):
    """Returns objects where the specified field contains the provided value as a substring."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    value: str
    type: typing.Literal["phrase"]


PreciseTimeUnit = typing.Literal[
    "NANOSECONDS", "SECONDS", "MINUTES", "HOURS", "DAYS", "WEEKS", "MONTHS", "YEARS"
]
"""The unit of duration."""


class PrefixQuery(pydantic.BaseModel):
    """Returns objects where the specified field starts with the provided value."""

    field: FieldNameV1
    value: str
    type: typing.Literal["prefix"] = "prefix"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "PrefixQueryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(PrefixQueryDict, self.model_dump(by_alias=True, exclude_none=True))


class PrefixQueryDict(typing_extensions.TypedDict):
    """Returns objects where the specified field starts with the provided value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    value: str
    type: typing.Literal["prefix"]


PrimaryKeyValue = typing.Any
"""Represents the primary key value that is used as a unique identifier for an object."""


class Property(pydantic.BaseModel):
    """Details about some property of an object."""

    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    base_type: ValueType = pydantic.Field(alias=str("baseType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "PropertyDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(PropertyDict, self.model_dump(by_alias=True, exclude_none=True))


PropertyApiName = str
"""
The name of the property in the API. To find the API name for your property, use the `Get object type`
endpoint or check the **Ontology Manager**.
"""


class PropertyDict(typing_extensions.TypedDict):
    """Details about some property of an object."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    description: typing_extensions.NotRequired[str]
    displayName: typing_extensions.NotRequired[core_models.DisplayName]
    baseType: ValueType


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


class QueryAggregationRangeTypeDict(typing_extensions.TypedDict):
    """QueryAggregationRangeType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: QueryAggregationRangeSubTypeDict
    type: typing.Literal["range"]


QueryAggregationValueTypeDict = typing_extensions.Annotated[
    typing.Union[
        "core_models.DateTypeDict", "core_models.DoubleTypeDict", "core_models.TimestampTypeDict"
    ],
    pydantic.Field(discriminator="type"),
]
"""A union of all the types supported by query aggregation keys."""


QueryApiName = str
"""The name of the Query in the API."""


class QueryArrayTypeDict(typing_extensions.TypedDict):
    """QueryArrayType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: QueryDataTypeDict
    type: typing.Literal["array"]


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


QueryRuntimeErrorParameter = str
"""QueryRuntimeErrorParameter"""


class QuerySetTypeDict(typing_extensions.TypedDict):
    """QuerySetType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    subType: QueryDataTypeDict
    type: typing.Literal["set"]


class QueryStructFieldDict(typing_extensions.TypedDict):
    """QueryStructField"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    name: core_models.StructFieldName
    fieldType: QueryDataTypeDict


class QueryStructTypeDict(typing_extensions.TypedDict):
    """QueryStructType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fields: typing.List[QueryStructFieldDict]
    type: typing.Literal["struct"]


class QueryType(pydantic.BaseModel):
    """Represents a query type in the Ontology."""

    api_name: QueryApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, Parameter]
    output: typing.Optional[OntologyDataType] = None
    rid: FunctionRid
    version: FunctionVersion
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "QueryTypeDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(QueryTypeDict, self.model_dump(by_alias=True, exclude_none=True))


class QueryTypeDict(typing_extensions.TypedDict):
    """Represents a query type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: QueryApiName
    description: typing_extensions.NotRequired[str]
    displayName: typing_extensions.NotRequired[core_models.DisplayName]
    parameters: typing.Dict[ParameterId, ParameterDict]
    output: typing_extensions.NotRequired[OntologyDataTypeDict]
    rid: FunctionRid
    version: FunctionVersion


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


ReturnEditsMode = typing.Literal["ALL", "ALL_V2_WITH_DELETIONS", "NONE"]
"""ReturnEditsMode"""


SdkPackageName = str
"""SdkPackageName"""


SearchJsonQuery = typing_extensions.Annotated[
    typing.Union[
        "OrQuery",
        "PrefixQuery",
        "LtQuery",
        "AllTermsQuery",
        "EqualsQuery",
        "GtQuery",
        "ContainsQuery",
        "NotQuery",
        "PhraseQuery",
        "AndQuery",
        "IsNullQuery",
        "GteQuery",
        "AnyTermQuery",
        "LteQuery",
    ],
    pydantic.Field(discriminator="type"),
]
"""SearchJsonQuery"""


SearchJsonQueryDict = typing_extensions.Annotated[
    typing.Union[
        "OrQueryDict",
        "PrefixQueryDict",
        "LtQueryDict",
        "AllTermsQueryDict",
        "EqualsQueryDict",
        "GtQueryDict",
        "ContainsQueryDict",
        "NotQueryDict",
        "PhraseQueryDict",
        "AndQueryDict",
        "IsNullQueryDict",
        "GteQueryDict",
        "AnyTermQueryDict",
        "LteQueryDict",
    ],
    pydantic.Field(discriminator="type"),
]
"""SearchJsonQuery"""


class SearchObjectsResponse(pydantic.BaseModel):
    """SearchObjectsResponse"""

    data: typing.List[OntologyObject]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchObjectsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchObjectsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchObjectsResponseDict(typing_extensions.TypedDict):
    """SearchObjectsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[OntologyObjectDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]
    totalCount: core_models.TotalCount


class SearchOrderBy(pydantic.BaseModel):
    """Specifies the ordering of search results by a field and an ordering direction."""

    fields: typing.List[SearchOrdering]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchOrderByDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(SearchOrderByDict, self.model_dump(by_alias=True, exclude_none=True))


class SearchOrderByDict(typing_extensions.TypedDict):
    """Specifies the ordering of search results by a field and an ordering direction."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fields: typing.List[SearchOrderingDict]


SearchOrderByType = typing.Literal["fields", "relevance"]
"""SearchOrderByType"""


class SearchOrdering(pydantic.BaseModel):
    """SearchOrdering"""

    field: FieldNameV1
    direction: typing.Optional[str] = None
    """Specifies the ordering direction (can be either `asc` or `desc`)"""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchOrderingDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(SearchOrderingDict, self.model_dump(by_alias=True, exclude_none=True))


class SearchOrderingDict(typing_extensions.TypedDict):
    """SearchOrdering"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
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


SharedPropertyTypeApiName = str
"""
The name of the shared property type in the API in lowerCamelCase format. To find the API name for your
shared property type, use the `List shared property types` endpoint or check the **Ontology Manager**.
"""


SharedPropertyTypeRid = core.RID
"""The unique resource identifier of an shared property type, useful for interacting with other Foundry APIs."""


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


class SumAggregation(pydantic.BaseModel):
    """Computes the sum of values for the provided field."""

    field: FieldNameV1
    name: typing.Optional[AggregationMetricName] = None
    type: typing.Literal["sum"] = "sum"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SumAggregationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(SumAggregationDict, self.model_dump(by_alias=True, exclude_none=True))


class SumAggregationDict(typing_extensions.TypedDict):
    """Computes the sum of values for the provided field."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    field: FieldNameV1
    name: typing_extensions.NotRequired[AggregationMetricName]
    type: typing.Literal["sum"]


class ThreeDimensionalAggregationDict(typing_extensions.TypedDict):
    """ThreeDimensionalAggregation"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    keyType: QueryAggregationKeyTypeDict
    valueType: TwoDimensionalAggregationDict
    type: typing.Literal["threeDimensionalAggregation"]


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


class ValidateActionResponse(pydantic.BaseModel):
    """ValidateActionResponse"""

    result: ValidationResult
    submission_criteria: typing.List[SubmissionCriteriaEvaluation] = pydantic.Field(alias=str("submissionCriteria"))  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, ParameterEvaluationResult]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ValidateActionResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ValidateActionResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ValidateActionResponseDict(typing_extensions.TypedDict):
    """ValidateActionResponse"""

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


from foundry.v1.core import models as core_models  # noqa: E402

__all__ = [
    "ActionRid",
    "ActionType",
    "ActionTypeApiName",
    "ActionTypeDict",
    "ActionTypeRid",
    "AggregateObjectsResponse",
    "AggregateObjectsResponseDict",
    "AggregateObjectsResponseItem",
    "AggregateObjectsResponseItemDict",
    "Aggregation",
    "AggregationDict",
    "AggregationDurationGrouping",
    "AggregationDurationGroupingDict",
    "AggregationExactGrouping",
    "AggregationExactGroupingDict",
    "AggregationFixedWidthGrouping",
    "AggregationFixedWidthGroupingDict",
    "AggregationGroupBy",
    "AggregationGroupByDict",
    "AggregationGroupKey",
    "AggregationGroupValue",
    "AggregationMetricName",
    "AggregationMetricResult",
    "AggregationMetricResultDict",
    "AggregationRange",
    "AggregationRangeDict",
    "AggregationRangesGrouping",
    "AggregationRangesGroupingDict",
    "AllTermsQuery",
    "AllTermsQueryDict",
    "AndQuery",
    "AndQueryDict",
    "AnyTermQuery",
    "AnyTermQueryDict",
    "ApplyActionMode",
    "ApplyActionRequest",
    "ApplyActionRequestDict",
    "ApplyActionRequestOptions",
    "ApplyActionRequestOptionsDict",
    "ApplyActionResponse",
    "ApplyActionResponseDict",
    "ApproximateDistinctAggregation",
    "ApproximateDistinctAggregationDict",
    "ArraySizeConstraint",
    "ArraySizeConstraintDict",
    "ArtifactRepositoryRid",
    "AttachmentRid",
    "AvgAggregation",
    "AvgAggregationDict",
    "BatchApplyActionResponse",
    "BatchApplyActionResponseDict",
    "ContainsQuery",
    "ContainsQueryDict",
    "CountAggregation",
    "CountAggregationDict",
    "CreateInterfaceObjectRule",
    "CreateInterfaceObjectRuleDict",
    "CreateLinkRule",
    "CreateLinkRuleDict",
    "CreateObjectRule",
    "CreateObjectRuleDict",
    "DataValue",
    "DeleteInterfaceObjectRule",
    "DeleteInterfaceObjectRuleDict",
    "DeleteLinkRule",
    "DeleteLinkRuleDict",
    "DeleteObjectRule",
    "DeleteObjectRuleDict",
    "DerivedPropertyApiName",
    "Duration",
    "EntrySetTypeDict",
    "EqualsQuery",
    "EqualsQueryDict",
    "ExecuteQueryResponse",
    "ExecuteQueryResponseDict",
    "FieldNameV1",
    "FilterValue",
    "FunctionRid",
    "FunctionVersion",
    "Fuzzy",
    "GroupMemberConstraint",
    "GroupMemberConstraintDict",
    "GtQuery",
    "GtQueryDict",
    "GteQuery",
    "GteQueryDict",
    "InterfaceTypeApiName",
    "InterfaceTypeRid",
    "IsNullQuery",
    "IsNullQueryDict",
    "LinkTypeApiName",
    "LinkTypeSide",
    "LinkTypeSideCardinality",
    "LinkTypeSideDict",
    "ListActionTypesResponse",
    "ListActionTypesResponseDict",
    "ListLinkedObjectsResponse",
    "ListLinkedObjectsResponseDict",
    "ListObjectTypesResponse",
    "ListObjectTypesResponseDict",
    "ListObjectsResponse",
    "ListObjectsResponseDict",
    "ListOntologiesResponse",
    "ListOntologiesResponseDict",
    "ListOutgoingLinkTypesResponse",
    "ListOutgoingLinkTypesResponseDict",
    "ListQueryTypesResponse",
    "ListQueryTypesResponseDict",
    "LogicRule",
    "LogicRuleDict",
    "LtQuery",
    "LtQueryDict",
    "LteQuery",
    "LteQueryDict",
    "MaxAggregation",
    "MaxAggregationDict",
    "MinAggregation",
    "MinAggregationDict",
    "ModifyInterfaceObjectRule",
    "ModifyInterfaceObjectRuleDict",
    "ModifyObjectRule",
    "ModifyObjectRuleDict",
    "NotQuery",
    "NotQueryDict",
    "ObjectPropertyValueConstraint",
    "ObjectPropertyValueConstraintDict",
    "ObjectQueryResultConstraint",
    "ObjectQueryResultConstraintDict",
    "ObjectRid",
    "ObjectSetRid",
    "ObjectType",
    "ObjectTypeApiName",
    "ObjectTypeDict",
    "ObjectTypeRid",
    "ObjectTypeVisibility",
    "OneOfConstraint",
    "OneOfConstraintDict",
    "Ontology",
    "OntologyApiName",
    "OntologyArrayType",
    "OntologyArrayTypeDict",
    "OntologyDataType",
    "OntologyDataTypeDict",
    "OntologyDict",
    "OntologyMapType",
    "OntologyMapTypeDict",
    "OntologyObject",
    "OntologyObjectDict",
    "OntologyObjectSetType",
    "OntologyObjectSetTypeDict",
    "OntologyObjectType",
    "OntologyObjectTypeDict",
    "OntologyRid",
    "OntologySetType",
    "OntologySetTypeDict",
    "OntologyStructField",
    "OntologyStructFieldDict",
    "OntologyStructType",
    "OntologyStructTypeDict",
    "OrQuery",
    "OrQueryDict",
    "OrderBy",
    "Parameter",
    "ParameterDict",
    "ParameterEvaluatedConstraint",
    "ParameterEvaluatedConstraintDict",
    "ParameterEvaluationResult",
    "ParameterEvaluationResultDict",
    "ParameterId",
    "ParameterOption",
    "ParameterOptionDict",
    "PhraseQuery",
    "PhraseQueryDict",
    "PreciseTimeUnit",
    "PrefixQuery",
    "PrefixQueryDict",
    "PrimaryKeyValue",
    "Property",
    "PropertyApiName",
    "PropertyDict",
    "PropertyFilter",
    "PropertyId",
    "PropertyValue",
    "PropertyValueEscapedString",
    "QueryAggregationKeyTypeDict",
    "QueryAggregationRangeSubTypeDict",
    "QueryAggregationRangeTypeDict",
    "QueryAggregationValueTypeDict",
    "QueryApiName",
    "QueryArrayTypeDict",
    "QueryDataTypeDict",
    "QueryRuntimeErrorParameter",
    "QuerySetTypeDict",
    "QueryStructFieldDict",
    "QueryStructTypeDict",
    "QueryType",
    "QueryTypeDict",
    "QueryUnionTypeDict",
    "RangeConstraint",
    "RangeConstraintDict",
    "ReturnEditsMode",
    "SdkPackageName",
    "SearchJsonQuery",
    "SearchJsonQueryDict",
    "SearchObjectsResponse",
    "SearchObjectsResponseDict",
    "SearchOrderBy",
    "SearchOrderByDict",
    "SearchOrderByType",
    "SearchOrdering",
    "SearchOrderingDict",
    "SelectedPropertyApiName",
    "SharedPropertyTypeApiName",
    "SharedPropertyTypeRid",
    "StringLengthConstraint",
    "StringLengthConstraintDict",
    "StringRegexMatchConstraint",
    "StringRegexMatchConstraintDict",
    "SubmissionCriteriaEvaluation",
    "SubmissionCriteriaEvaluationDict",
    "SumAggregation",
    "SumAggregationDict",
    "ThreeDimensionalAggregationDict",
    "TwoDimensionalAggregationDict",
    "UnevaluableConstraint",
    "UnevaluableConstraintDict",
    "ValidateActionResponse",
    "ValidateActionResponseDict",
    "ValidationResult",
    "ValueType",
]
