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


import typing
from dataclasses import dataclass

import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v1.ontologies import models as ontologies_models


class ActionContainsDuplicateEditsParameters(typing_extensions.TypedDict):
    """The given action request has multiple edits on the same object."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ActionContainsDuplicateEdits(errors.ConflictError):
    name: typing.Literal["ActionContainsDuplicateEdits"]
    parameters: ActionContainsDuplicateEditsParameters
    error_instance_id: str


class ActionEditedPropertiesNotFoundParameters(typing_extensions.TypedDict):
    """
    Actions attempted to edit properties that could not be found on the object type.
    Please contact the Ontology administrator to resolve this issue.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ActionEditedPropertiesNotFound(errors.BadRequestError):
    name: typing.Literal["ActionEditedPropertiesNotFound"]
    parameters: ActionEditedPropertiesNotFoundParameters
    error_instance_id: str


class ActionEditsReadOnlyEntityParameters(typing_extensions.TypedDict):
    """The given action request performs edits on a type that is read-only or does not allow edits."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    entityTypeRid: typing_extensions.NotRequired[ontologies_models.ObjectTypeRid]


@dataclass
class ActionEditsReadOnlyEntity(errors.BadRequestError):
    name: typing.Literal["ActionEditsReadOnlyEntity"]
    parameters: ActionEditsReadOnlyEntityParameters
    error_instance_id: str


class ActionNotFoundParameters(typing_extensions.TypedDict):
    """The action is not found, or the user does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    actionRid: ontologies_models.ActionRid


@dataclass
class ActionNotFound(errors.NotFoundError):
    name: typing.Literal["ActionNotFound"]
    parameters: ActionNotFoundParameters
    error_instance_id: str


class ActionParameterInterfaceTypeNotFoundParameters(typing_extensions.TypedDict):
    """The parameter references an interface type that could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameterId: ontologies_models.ParameterId


@dataclass
class ActionParameterInterfaceTypeNotFound(errors.NotFoundError):
    name: typing.Literal["ActionParameterInterfaceTypeNotFound"]
    parameters: ActionParameterInterfaceTypeNotFoundParameters
    error_instance_id: str


class ActionParameterObjectNotFoundParameters(typing_extensions.TypedDict):
    """The parameter object reference or parameter default value is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameterId: ontologies_models.ParameterId


@dataclass
class ActionParameterObjectNotFound(errors.NotFoundError):
    name: typing.Literal["ActionParameterObjectNotFound"]
    parameters: ActionParameterObjectNotFoundParameters
    error_instance_id: str


class ActionParameterObjectTypeNotFoundParameters(typing_extensions.TypedDict):
    """The parameter references an object type that could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameterId: ontologies_models.ParameterId


@dataclass
class ActionParameterObjectTypeNotFound(errors.NotFoundError):
    name: typing.Literal["ActionParameterObjectTypeNotFound"]
    parameters: ActionParameterObjectTypeNotFoundParameters
    error_instance_id: str


class ActionTypeNotFoundParameters(typing_extensions.TypedDict):
    """The action type is not found, or the user does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    actionType: typing_extensions.NotRequired[ontologies_models.ActionTypeApiName]
    rid: typing_extensions.NotRequired[ontologies_models.ActionTypeRid]


@dataclass
class ActionTypeNotFound(errors.NotFoundError):
    name: typing.Literal["ActionTypeNotFound"]
    parameters: ActionTypeNotFoundParameters
    error_instance_id: str


class ActionValidationFailedParameters(typing_extensions.TypedDict):
    """
    The validation failed for the given action parameters. Please use the `validateAction` endpoint for more
    details.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    actionType: ontologies_models.ActionTypeApiName


@dataclass
class ActionValidationFailed(errors.BadRequestError):
    name: typing.Literal["ActionValidationFailed"]
    parameters: ActionValidationFailedParameters
    error_instance_id: str


class AggregationAccuracyNotSupportedParameters(typing_extensions.TypedDict):
    """
    The given aggregation cannot be performed with the requested accuracy.
    Try allowing approximate results or adjust your aggregation request.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class AggregationAccuracyNotSupported(errors.BadRequestError):
    name: typing.Literal["AggregationAccuracyNotSupported"]
    parameters: AggregationAccuracyNotSupportedParameters
    error_instance_id: str


class AggregationGroupCountExceededLimitParameters(typing_extensions.TypedDict):
    """
    The number of groups in the aggregations grouping exceeded the allowed limit. This can typically be fixed by
    adjusting your query to reduce the number of groups created by your aggregation. For instance:
    - If you are using multiple `groupBy` clauses, try reducing the number of clauses.
    - If you are using a `groupBy` clause with a high cardinality property, try filtering the data first
      to reduce the number of groups.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupsCount: typing_extensions.NotRequired[int]
    groupsLimit: typing_extensions.NotRequired[int]


@dataclass
class AggregationGroupCountExceededLimit(errors.BadRequestError):
    name: typing.Literal["AggregationGroupCountExceededLimit"]
    parameters: AggregationGroupCountExceededLimitParameters
    error_instance_id: str


class AggregationMemoryExceededLimitParameters(typing_extensions.TypedDict):
    """
    The amount of memory used in the request exceeded the limit. This can typically be fixed by
    adjusting your query to reduce the number of groups created by your aggregation. For instance:
    - If you are using multiple `groupBy` clauses, try reducing the number of clauses.
    - If you are using a `groupBy` clause with a high cardinality property, try filtering the data first
      to reduce the number of groups.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    memoryUsedBytes: typing_extensions.NotRequired[str]
    memoryLimitBytes: str


@dataclass
class AggregationMemoryExceededLimit(errors.BadRequestError):
    name: typing.Literal["AggregationMemoryExceededLimit"]
    parameters: AggregationMemoryExceededLimitParameters
    error_instance_id: str


class AggregationNestedObjectSetSizeExceededLimitParameters(typing_extensions.TypedDict):
    """
    A nested object set within the aggregation exceeded the allowed limit.
    This can be fixed by aggregating over fewer objects, such as by applying a filter.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectsCount: int
    objectsLimit: int


@dataclass
class AggregationNestedObjectSetSizeExceededLimit(errors.BadRequestError):
    name: typing.Literal["AggregationNestedObjectSetSizeExceededLimit"]
    parameters: AggregationNestedObjectSetSizeExceededLimitParameters
    error_instance_id: str


class ApplyActionFailedParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ApplyActionFailed(errors.BadRequestError):
    name: typing.Literal["ApplyActionFailed"]
    parameters: ApplyActionFailedParameters
    error_instance_id: str


class AttachmentNotFoundParameters(typing_extensions.TypedDict):
    """
    The requested attachment is not found, or the client token does not have access to it.
    Attachments that are not attached to any objects are deleted after two weeks.
    Attachments that have not been attached to an object can only be viewed by the user who uploaded them.
    Attachments that have been attached to an object can be viewed by users who can view the object.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    attachmentRid: typing_extensions.NotRequired[ontologies_models.AttachmentRid]


@dataclass
class AttachmentNotFound(errors.NotFoundError):
    name: typing.Literal["AttachmentNotFound"]
    parameters: AttachmentNotFoundParameters
    error_instance_id: str


class AttachmentSizeExceededLimitParameters(typing_extensions.TypedDict):
    """
    The file is too large to be uploaded as an attachment.
    The maximum attachment size is 200MB.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fileSizeBytes: str
    fileLimitBytes: str


@dataclass
class AttachmentSizeExceededLimit(errors.BadRequestError):
    name: typing.Literal["AttachmentSizeExceededLimit"]
    parameters: AttachmentSizeExceededLimitParameters
    error_instance_id: str


class CipherChannelNotFoundParameters(typing_extensions.TypedDict):
    """
    The Cipher Channel was not found.
    It either does not exist, or you do not have permission to see it.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    cipherChannel: core.RID


@dataclass
class CipherChannelNotFound(errors.NotFoundError):
    name: typing.Literal["CipherChannelNotFound"]
    parameters: CipherChannelNotFoundParameters
    error_instance_id: str


class CompositePrimaryKeyNotSupportedParameters(typing_extensions.TypedDict):
    """
    Primary keys consisting of multiple properties are not supported by this API. If you need support for this,
    please reach out to Palantir Support.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: ontologies_models.ObjectTypeApiName
    primaryKey: typing.List[ontologies_models.PropertyApiName]


@dataclass
class CompositePrimaryKeyNotSupported(errors.BadRequestError):
    name: typing.Literal["CompositePrimaryKeyNotSupported"]
    parameters: CompositePrimaryKeyNotSupportedParameters
    error_instance_id: str


class DefaultAndNullGroupsNotSupportedParameters(typing_extensions.TypedDict):
    """Exact match groupBy clause cannot specify a default value and allow null values."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class DefaultAndNullGroupsNotSupported(errors.BadRequestError):
    name: typing.Literal["DefaultAndNullGroupsNotSupported"]
    parameters: DefaultAndNullGroupsNotSupportedParameters
    error_instance_id: str


class DerivedPropertyApiNamesNotUniqueParameters(typing_extensions.TypedDict):
    """At least one of the requested derived property API names already exist on the object set."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    derivedPropertyApiNames: typing.List[ontologies_models.DerivedPropertyApiName]


@dataclass
class DerivedPropertyApiNamesNotUnique(errors.BadRequestError):
    name: typing.Literal["DerivedPropertyApiNamesNotUnique"]
    parameters: DerivedPropertyApiNamesNotUniqueParameters
    error_instance_id: str


class DuplicateOrderByParameters(typing_extensions.TypedDict):
    """The requested sort order includes duplicate properties."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    properties: typing.List[ontologies_models.PropertyApiName]


@dataclass
class DuplicateOrderBy(errors.BadRequestError):
    name: typing.Literal["DuplicateOrderBy"]
    parameters: DuplicateOrderByParameters
    error_instance_id: str


class EditObjectPermissionDeniedParameters(typing_extensions.TypedDict):
    """The user does not have permission to edit this `ObjectType`."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class EditObjectPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["EditObjectPermissionDenied"]
    parameters: EditObjectPermissionDeniedParameters
    error_instance_id: str


class FunctionEncounteredUserFacingErrorParameters(typing_extensions.TypedDict):
    """
    The authored function failed to execute because of a user induced error. The message argument
    is meant to be displayed to the user.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: ontologies_models.FunctionRid
    functionVersion: ontologies_models.FunctionVersion
    message: str


@dataclass
class FunctionEncounteredUserFacingError(errors.BadRequestError):
    name: typing.Literal["FunctionEncounteredUserFacingError"]
    parameters: FunctionEncounteredUserFacingErrorParameters
    error_instance_id: str


class FunctionExecutionFailedParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: ontologies_models.FunctionRid
    functionVersion: ontologies_models.FunctionVersion
    message: typing_extensions.NotRequired[str]
    stacktrace: typing_extensions.NotRequired[str]


@dataclass
class FunctionExecutionFailed(errors.BadRequestError):
    name: typing.Literal["FunctionExecutionFailed"]
    parameters: FunctionExecutionFailedParameters
    error_instance_id: str


class FunctionExecutionTimedOutParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: ontologies_models.FunctionRid
    functionVersion: ontologies_models.FunctionVersion


@dataclass
class FunctionExecutionTimedOut(errors.InternalServerError):
    name: typing.Literal["FunctionExecutionTimedOut"]
    parameters: FunctionExecutionTimedOutParameters
    error_instance_id: str


class FunctionInvalidInputParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: ontologies_models.FunctionRid
    functionVersion: ontologies_models.FunctionVersion


@dataclass
class FunctionInvalidInput(errors.BadRequestError):
    name: typing.Literal["FunctionInvalidInput"]
    parameters: FunctionInvalidInputParameters
    error_instance_id: str


class HighScaleComputationNotEnabledParameters(typing_extensions.TypedDict):
    """High-scale compute was required for this Ontology query but is not enabled on this enrollment."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class HighScaleComputationNotEnabled(errors.InternalServerError):
    name: typing.Literal["HighScaleComputationNotEnabled"]
    parameters: HighScaleComputationNotEnabledParameters
    error_instance_id: str


class InterfaceLinkTypeNotFoundParameters(typing_extensions.TypedDict):
    """The requested interface link type is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    interfaceTypeApiName: typing_extensions.NotRequired[ontologies_models.InterfaceTypeApiName]
    interfaceTypeRid: typing_extensions.NotRequired[ontologies_models.InterfaceTypeRid]
    interfaceLinkTypeApiName: typing_extensions.NotRequired[
        ontologies_models.InterfaceLinkTypeApiName
    ]
    interfaceLinkTypeRid: typing_extensions.NotRequired[ontologies_models.InterfaceLinkTypeRid]


@dataclass
class InterfaceLinkTypeNotFound(errors.NotFoundError):
    name: typing.Literal["InterfaceLinkTypeNotFound"]
    parameters: InterfaceLinkTypeNotFoundParameters
    error_instance_id: str


class InterfaceTypeNotFoundParameters(typing_extensions.TypedDict):
    """The requested interface type is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: typing_extensions.NotRequired[ontologies_models.InterfaceTypeApiName]
    rid: typing_extensions.NotRequired[ontologies_models.InterfaceTypeRid]


@dataclass
class InterfaceTypeNotFound(errors.NotFoundError):
    name: typing.Literal["InterfaceTypeNotFound"]
    parameters: InterfaceTypeNotFoundParameters
    error_instance_id: str


class InterfaceTypesNotFoundParameters(typing_extensions.TypedDict):
    """The requested interface types were not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: typing.List[ontologies_models.InterfaceTypeApiName]
    rid: typing.List[ontologies_models.InterfaceTypeRid]


@dataclass
class InterfaceTypesNotFound(errors.NotFoundError):
    name: typing.Literal["InterfaceTypesNotFound"]
    parameters: InterfaceTypesNotFoundParameters
    error_instance_id: str


class InvalidAggregationOrderingParameters(typing_extensions.TypedDict):
    """Aggregation ordering can only be applied to metrics with exactly one groupBy clause."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidAggregationOrdering(errors.BadRequestError):
    name: typing.Literal["InvalidAggregationOrdering"]
    parameters: InvalidAggregationOrderingParameters
    error_instance_id: str


class InvalidAggregationOrderingWithNullValuesParameters(typing_extensions.TypedDict):
    """Aggregation ordering cannot be applied for groupBy clauses that allow null values."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidAggregationOrderingWithNullValues(errors.BadRequestError):
    name: typing.Literal["InvalidAggregationOrderingWithNullValues"]
    parameters: InvalidAggregationOrderingWithNullValuesParameters
    error_instance_id: str


class InvalidAggregationRangeParameters(typing_extensions.TypedDict):
    """Aggregation range should include one lt or lte and one gt or gte."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidAggregationRange(errors.BadRequestError):
    name: typing.Literal["InvalidAggregationRange"]
    parameters: InvalidAggregationRangeParameters
    error_instance_id: str


class InvalidAggregationRangePropertyTypeParameters(typing_extensions.TypedDict):
    """Range group by is not supported by property type."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    property: ontologies_models.PropertyApiName
    objectType: ontologies_models.ObjectTypeApiName
    propertyBaseType: ontologies_models.ValueType


@dataclass
class InvalidAggregationRangePropertyType(errors.BadRequestError):
    name: typing.Literal["InvalidAggregationRangePropertyType"]
    parameters: InvalidAggregationRangePropertyTypeParameters
    error_instance_id: str


class InvalidAggregationRangeValueParameters(typing_extensions.TypedDict):
    """Aggregation value does not conform to the expected underlying type."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    property: ontologies_models.PropertyApiName
    objectType: ontologies_models.ObjectTypeApiName
    propertyBaseType: ontologies_models.ValueType


@dataclass
class InvalidAggregationRangeValue(errors.BadRequestError):
    name: typing.Literal["InvalidAggregationRangeValue"]
    parameters: InvalidAggregationRangeValueParameters
    error_instance_id: str


class InvalidApplyActionOptionCombinationParameters(typing_extensions.TypedDict):
    """The given options are individually valid but cannot be used in the given combination."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    invalidCombination: typing_extensions.NotRequired[ontologies_models.ApplyActionRequestOptions]


@dataclass
class InvalidApplyActionOptionCombination(errors.BadRequestError):
    name: typing.Literal["InvalidApplyActionOptionCombination"]
    parameters: InvalidApplyActionOptionCombinationParameters
    error_instance_id: str


class InvalidContentLengthParameters(typing_extensions.TypedDict):
    """A `Content-Length` header is required for all uploads, but was missing or invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidContentLength(errors.BadRequestError):
    name: typing.Literal["InvalidContentLength"]
    parameters: InvalidContentLengthParameters
    error_instance_id: str


class InvalidContentTypeParameters(typing_extensions.TypedDict):
    """
    The `Content-Type` cannot be inferred from the request content and filename.
    Please check your request content and filename to ensure they are compatible.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidContentType(errors.BadRequestError):
    name: typing.Literal["InvalidContentType"]
    parameters: InvalidContentTypeParameters
    error_instance_id: str


class InvalidDerivedPropertyDefinitionParameters(typing_extensions.TypedDict):
    """Derived property definition was invalid due to shape of query or type checking."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: ontologies_models.ObjectTypeApiName
    derivedProperty: ontologies_models.DerivedPropertyApiName


@dataclass
class InvalidDerivedPropertyDefinition(errors.BadRequestError):
    name: typing.Literal["InvalidDerivedPropertyDefinition"]
    parameters: InvalidDerivedPropertyDefinitionParameters
    error_instance_id: str


class InvalidDurationGroupByPropertyTypeParameters(typing_extensions.TypedDict):
    """Invalid property type for duration groupBy."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    property: ontologies_models.PropertyApiName
    objectType: ontologies_models.ObjectTypeApiName
    propertyBaseType: ontologies_models.ValueType


@dataclass
class InvalidDurationGroupByPropertyType(errors.BadRequestError):
    name: typing.Literal["InvalidDurationGroupByPropertyType"]
    parameters: InvalidDurationGroupByPropertyTypeParameters
    error_instance_id: str


class InvalidDurationGroupByValueParameters(typing_extensions.TypedDict):
    """
    Duration groupBy value is invalid. Units larger than day must have value `1` and date properties do not support
    filtering on units smaller than day. As examples, neither bucketing by every two weeks nor bucketing a date by
    every two hours are allowed.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class InvalidDurationGroupByValue(errors.BadRequestError):
    name: typing.Literal["InvalidDurationGroupByValue"]
    parameters: InvalidDurationGroupByValueParameters
    error_instance_id: str


class InvalidFieldsParameters(typing_extensions.TypedDict):
    """
    The value of the given field does not match the expected pattern. For example, an Ontology object property `id`
    should be written `properties.id`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    properties: typing.List[str]


@dataclass
class InvalidFields(errors.BadRequestError):
    name: typing.Literal["InvalidFields"]
    parameters: InvalidFieldsParameters
    error_instance_id: str


class InvalidGroupIdParameters(typing_extensions.TypedDict):
    """The provided value for a group id must be a UUID."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: str


@dataclass
class InvalidGroupId(errors.BadRequestError):
    name: typing.Literal["InvalidGroupId"]
    parameters: InvalidGroupIdParameters
    error_instance_id: str


class InvalidOrderTypeParameters(typing_extensions.TypedDict):
    """This query type does not support the provided order type"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    orderType: typing_extensions.NotRequired[ontologies_models.SearchOrderByType]


@dataclass
class InvalidOrderType(errors.BadRequestError):
    name: typing.Literal["InvalidOrderType"]
    parameters: InvalidOrderTypeParameters
    error_instance_id: str


class InvalidParameterValueParameters(typing_extensions.TypedDict):
    """
    The value of the given parameter is invalid. See the documentation of `DataValue` for details on
    how parameters are represented.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameterBaseType: typing_extensions.NotRequired[ontologies_models.ValueType]
    parameterDataType: typing_extensions.NotRequired[ontologies_models.OntologyDataType]
    parameterId: ontologies_models.ParameterId
    parameterValue: typing_extensions.NotRequired[ontologies_models.DataValue]


@dataclass
class InvalidParameterValue(errors.BadRequestError):
    name: typing.Literal["InvalidParameterValue"]
    parameters: InvalidParameterValueParameters
    error_instance_id: str


class InvalidPropertyFilterValueParameters(typing_extensions.TypedDict):
    """
    The value of the given property filter is invalid. For instance, 2 is an invalid value for
    `isNull` in `properties.address.isNull=2` because the `isNull` filter expects a value of boolean type.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    expectedType: ontologies_models.ValueType
    propertyFilter: ontologies_models.PropertyFilter
    propertyFilterValue: ontologies_models.FilterValue
    property: ontologies_models.PropertyApiName


@dataclass
class InvalidPropertyFilterValue(errors.BadRequestError):
    name: typing.Literal["InvalidPropertyFilterValue"]
    parameters: InvalidPropertyFilterValueParameters
    error_instance_id: str


class InvalidPropertyFiltersCombinationParameters(typing_extensions.TypedDict):
    """The provided filters cannot be used together."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyFilters: typing.List[ontologies_models.PropertyFilter]
    property: ontologies_models.PropertyApiName


@dataclass
class InvalidPropertyFiltersCombination(errors.BadRequestError):
    name: typing.Literal["InvalidPropertyFiltersCombination"]
    parameters: InvalidPropertyFiltersCombinationParameters
    error_instance_id: str


class InvalidPropertyTypeParameters(typing_extensions.TypedDict):
    """The given property type is not of the expected type."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyBaseType: ontologies_models.ValueType
    property: ontologies_models.PropertyApiName


@dataclass
class InvalidPropertyType(errors.BadRequestError):
    name: typing.Literal["InvalidPropertyType"]
    parameters: InvalidPropertyTypeParameters
    error_instance_id: str


class InvalidPropertyValueParameters(typing_extensions.TypedDict):
    """
    The value of the given property is invalid. See the documentation of `PropertyValue` for details on
    how properties are represented.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyBaseType: ontologies_models.ValueType
    property: ontologies_models.PropertyApiName
    propertyValue: ontologies_models.PropertyValue


@dataclass
class InvalidPropertyValue(errors.BadRequestError):
    name: typing.Literal["InvalidPropertyValue"]
    parameters: InvalidPropertyValueParameters
    error_instance_id: str


class InvalidQueryOutputValueParameters(typing_extensions.TypedDict):
    """
    The value of the query's output is invalid. This may be because the return value did not match the specified
    output type or constraints.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    outputDataType: ontologies_models.QueryDataType
    outputValue: typing_extensions.NotRequired[ontologies_models.DataValue]
    functionRid: ontologies_models.FunctionRid
    functionVersion: ontologies_models.FunctionVersion


@dataclass
class InvalidQueryOutputValue(errors.BadRequestError):
    name: typing.Literal["InvalidQueryOutputValue"]
    parameters: InvalidQueryOutputValueParameters
    error_instance_id: str


class InvalidQueryParameterValueParameters(typing_extensions.TypedDict):
    """
    The value of the given parameter is invalid. See the documentation of `DataValue` for details on
    how parameters are represented.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameterDataType: ontologies_models.QueryDataType
    parameterId: ontologies_models.ParameterId
    parameterValue: typing_extensions.NotRequired[ontologies_models.DataValue]


@dataclass
class InvalidQueryParameterValue(errors.BadRequestError):
    name: typing.Literal["InvalidQueryParameterValue"]
    parameters: InvalidQueryParameterValueParameters
    error_instance_id: str


class InvalidRangeQueryParameters(typing_extensions.TypedDict):
    """The specified query range filter is invalid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    lt: typing_extensions.NotRequired[typing.Any]
    """Less than"""

    gt: typing_extensions.NotRequired[typing.Any]
    """Greater than"""

    lte: typing_extensions.NotRequired[typing.Any]
    """Less than or equal"""

    gte: typing_extensions.NotRequired[typing.Any]
    """Greater than or equal"""

    field: str


@dataclass
class InvalidRangeQuery(errors.BadRequestError):
    name: typing.Literal["InvalidRangeQuery"]
    parameters: InvalidRangeQueryParameters
    error_instance_id: str


class InvalidSortOrderParameters(typing_extensions.TypedDict):
    """
    The requested sort order of one or more properties is invalid. Valid sort orders are 'asc' or 'desc'. Sort
    order can also be omitted, and defaults to 'asc'.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    invalidSortOrder: str


@dataclass
class InvalidSortOrder(errors.BadRequestError):
    name: typing.Literal["InvalidSortOrder"]
    parameters: InvalidSortOrderParameters
    error_instance_id: str


class InvalidSortTypeParameters(typing_extensions.TypedDict):
    """The requested sort type of one or more clauses is invalid. Valid sort types are 'p' or 'properties'."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    invalidSortType: str


@dataclass
class InvalidSortType(errors.BadRequestError):
    name: typing.Literal["InvalidSortType"]
    parameters: InvalidSortTypeParameters
    error_instance_id: str


class InvalidUserIdParameters(typing_extensions.TypedDict):
    """The provided value for a user id must be a UUID."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: str


@dataclass
class InvalidUserId(errors.BadRequestError):
    name: typing.Literal["InvalidUserId"]
    parameters: InvalidUserIdParameters
    error_instance_id: str


class InvalidVectorDimensionParameters(typing_extensions.TypedDict):
    """The dimensions of the provided vector don't match the dimensions of the embedding model being queried."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    expectedSize: int
    providedSize: int


@dataclass
class InvalidVectorDimension(errors.BadRequestError):
    name: typing.Literal["InvalidVectorDimension"]
    parameters: InvalidVectorDimensionParameters
    error_instance_id: str


class LinkAlreadyExistsParameters(typing_extensions.TypedDict):
    """The link the user is attempting to create already exists."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class LinkAlreadyExists(errors.ConflictError):
    name: typing.Literal["LinkAlreadyExists"]
    parameters: LinkAlreadyExistsParameters
    error_instance_id: str


class LinkTypeNotFoundParameters(typing_extensions.TypedDict):
    """The link type is not found, or the user does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: typing_extensions.NotRequired[ontologies_models.ObjectTypeApiName]
    linkType: typing_extensions.NotRequired[ontologies_models.LinkTypeApiName]
    linkTypeId: typing_extensions.NotRequired[ontologies_models.LinkTypeId]


@dataclass
class LinkTypeNotFound(errors.NotFoundError):
    name: typing.Literal["LinkTypeNotFound"]
    parameters: LinkTypeNotFoundParameters
    error_instance_id: str


class LinkedObjectNotFoundParameters(typing_extensions.TypedDict):
    """The linked object with the given primary key is not found, or the user does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    linkType: ontologies_models.LinkTypeApiName
    linkedObjectType: ontologies_models.ObjectTypeApiName
    linkedObjectPrimaryKey: typing.Dict[
        ontologies_models.PropertyApiName, ontologies_models.PrimaryKeyValue
    ]


@dataclass
class LinkedObjectNotFound(errors.NotFoundError):
    name: typing.Literal["LinkedObjectNotFound"]
    parameters: LinkedObjectNotFoundParameters
    error_instance_id: str


class MalformedPropertyFiltersParameters(typing_extensions.TypedDict):
    """At least one of requested filters are malformed. Please look at the documentation of `PropertyFilter`."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    malformedPropertyFilter: str


@dataclass
class MalformedPropertyFilters(errors.BadRequestError):
    name: typing.Literal["MalformedPropertyFilters"]
    parameters: MalformedPropertyFiltersParameters
    error_instance_id: str


class MarketplaceActionMappingNotFoundParameters(typing_extensions.TypedDict):
    """The given action could not be mapped to a Marketplace installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    actionType: ontologies_models.ActionTypeApiName
    artifactRepository: ontologies_models.ArtifactRepositoryRid
    packageName: ontologies_models.SdkPackageName


@dataclass
class MarketplaceActionMappingNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceActionMappingNotFound"]
    parameters: MarketplaceActionMappingNotFoundParameters
    error_instance_id: str


class MarketplaceInstallationNotFoundParameters(typing_extensions.TypedDict):
    """The given marketplace installation could not be found or the user does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    artifactRepository: ontologies_models.ArtifactRepositoryRid
    packageName: ontologies_models.SdkPackageName


@dataclass
class MarketplaceInstallationNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceInstallationNotFound"]
    parameters: MarketplaceInstallationNotFoundParameters
    error_instance_id: str


class MarketplaceLinkMappingNotFoundParameters(typing_extensions.TypedDict):
    """The given link could not be mapped to a Marketplace installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    linkType: ontologies_models.LinkTypeApiName
    artifactRepository: ontologies_models.ArtifactRepositoryRid
    packageName: ontologies_models.SdkPackageName


@dataclass
class MarketplaceLinkMappingNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceLinkMappingNotFound"]
    parameters: MarketplaceLinkMappingNotFoundParameters
    error_instance_id: str


class MarketplaceObjectMappingNotFoundParameters(typing_extensions.TypedDict):
    """The given object could not be mapped to a Marketplace installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: ontologies_models.ObjectTypeApiName
    artifactRepository: ontologies_models.ArtifactRepositoryRid
    packageName: ontologies_models.SdkPackageName


@dataclass
class MarketplaceObjectMappingNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceObjectMappingNotFound"]
    parameters: MarketplaceObjectMappingNotFoundParameters
    error_instance_id: str


class MarketplaceQueryMappingNotFoundParameters(typing_extensions.TypedDict):
    """The given query could not be mapped to a Marketplace installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryType: ontologies_models.QueryApiName
    artifactRepository: ontologies_models.ArtifactRepositoryRid
    packageName: ontologies_models.SdkPackageName


@dataclass
class MarketplaceQueryMappingNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceQueryMappingNotFound"]
    parameters: MarketplaceQueryMappingNotFoundParameters
    error_instance_id: str


class MarketplaceSdkActionMappingNotFoundParameters(typing_extensions.TypedDict):
    """The given action could not be mapped to a Marketplace installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    actionType: ontologies_models.ActionTypeApiName
    sdkPackageRid: ontologies_models.SdkPackageRid
    sdkVersion: ontologies_models.SdkVersion


@dataclass
class MarketplaceSdkActionMappingNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceSdkActionMappingNotFound"]
    parameters: MarketplaceSdkActionMappingNotFoundParameters
    error_instance_id: str


class MarketplaceSdkInstallationNotFoundParameters(typing_extensions.TypedDict):
    """The given marketplace installation could not be found or the user does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    sdkPackageRid: ontologies_models.SdkPackageRid
    sdkVersion: ontologies_models.SdkVersion


@dataclass
class MarketplaceSdkInstallationNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceSdkInstallationNotFound"]
    parameters: MarketplaceSdkInstallationNotFoundParameters
    error_instance_id: str


class MarketplaceSdkLinkMappingNotFoundParameters(typing_extensions.TypedDict):
    """The given link could not be mapped to a Marketplace installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    linkType: ontologies_models.LinkTypeApiName
    sdkPackageRid: ontologies_models.SdkPackageRid
    sdkVersion: ontologies_models.SdkVersion


@dataclass
class MarketplaceSdkLinkMappingNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceSdkLinkMappingNotFound"]
    parameters: MarketplaceSdkLinkMappingNotFoundParameters
    error_instance_id: str


class MarketplaceSdkObjectMappingNotFoundParameters(typing_extensions.TypedDict):
    """The given object could not be mapped to a Marketplace installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    localObjectType: typing_extensions.NotRequired[ontologies_models.ObjectTypeApiName]
    objectType: typing_extensions.NotRequired[ontologies_models.ObjectTypeRid]
    sdkPackageRid: ontologies_models.SdkPackageRid
    sdkVersion: ontologies_models.SdkVersion


@dataclass
class MarketplaceSdkObjectMappingNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceSdkObjectMappingNotFound"]
    parameters: MarketplaceSdkObjectMappingNotFoundParameters
    error_instance_id: str


class MarketplaceSdkPropertyMappingNotFoundParameters(typing_extensions.TypedDict):
    """The given property could not be mapped to a Marketplace installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyType: ontologies_models.PropertyApiName
    objectType: ontologies_models.ObjectTypeApiName
    sdkPackageRid: ontologies_models.SdkPackageRid
    sdkVersion: ontologies_models.SdkVersion


@dataclass
class MarketplaceSdkPropertyMappingNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceSdkPropertyMappingNotFound"]
    parameters: MarketplaceSdkPropertyMappingNotFoundParameters
    error_instance_id: str


class MarketplaceSdkQueryMappingNotFoundParameters(typing_extensions.TypedDict):
    """The given query could not be mapped to a Marketplace installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    queryType: ontologies_models.QueryApiName
    sdkPackageRid: ontologies_models.SdkPackageRid
    sdkVersion: ontologies_models.SdkVersion


@dataclass
class MarketplaceSdkQueryMappingNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceSdkQueryMappingNotFound"]
    parameters: MarketplaceSdkQueryMappingNotFoundParameters
    error_instance_id: str


class MissingParameterParameters(typing_extensions.TypedDict):
    """
    Required parameters are missing. Please look at the `parameters` field to see which required parameters are
    missing from the request.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameters: typing.List[ontologies_models.ParameterId]


@dataclass
class MissingParameter(errors.BadRequestError):
    name: typing.Literal["MissingParameter"]
    parameters: MissingParameterParameters
    error_instance_id: str


class MultipleGroupByOnFieldNotSupportedParameters(typing_extensions.TypedDict):
    """Aggregation cannot group by on the same field multiple times."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    duplicateFields: typing.List[str]


@dataclass
class MultipleGroupByOnFieldNotSupported(errors.BadRequestError):
    name: typing.Literal["MultipleGroupByOnFieldNotSupported"]
    parameters: MultipleGroupByOnFieldNotSupportedParameters
    error_instance_id: str


class MultiplePropertyValuesNotSupportedParameters(typing_extensions.TypedDict):
    """
    One of the requested property filters does not support multiple values. Please include only a single value for
    it.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyFilter: ontologies_models.PropertyFilter
    property: ontologies_models.PropertyApiName


@dataclass
class MultiplePropertyValuesNotSupported(errors.BadRequestError):
    name: typing.Literal["MultiplePropertyValuesNotSupported"]
    parameters: MultiplePropertyValuesNotSupportedParameters
    error_instance_id: str


class NotCipherFormattedParameters(typing_extensions.TypedDict):
    """
    The value intended for decryption with Cipher is not formatted correctly.
    It may already be a plaintext value and not require decryption.
    Ensure it is correctly formatted (CIPHER::<cipher-channel-rid>::<encrypted-value>::CIPHER).
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: str


@dataclass
class NotCipherFormatted(errors.BadRequestError):
    name: typing.Literal["NotCipherFormatted"]
    parameters: NotCipherFormattedParameters
    error_instance_id: str


class ObjectAlreadyExistsParameters(typing_extensions.TypedDict):
    """The object the user is attempting to create already exists."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ObjectAlreadyExists(errors.ConflictError):
    name: typing.Literal["ObjectAlreadyExists"]
    parameters: ObjectAlreadyExistsParameters
    error_instance_id: str


class ObjectChangedParameters(typing_extensions.TypedDict):
    """An object used by this `Action` was changed by someone else while the `Action` was running."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKey: typing_extensions.NotRequired[ontologies_models.PropertyValue]
    objectType: typing_extensions.NotRequired[ontologies_models.ObjectTypeApiName]


@dataclass
class ObjectChanged(errors.ConflictError):
    name: typing.Literal["ObjectChanged"]
    parameters: ObjectChangedParameters
    error_instance_id: str


class ObjectNotFoundParameters(typing_extensions.TypedDict):
    """The requested object is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: typing_extensions.NotRequired[ontologies_models.ObjectTypeApiName]
    primaryKey: typing.Dict[ontologies_models.PropertyApiName, ontologies_models.PrimaryKeyValue]


@dataclass
class ObjectNotFound(errors.NotFoundError):
    name: typing.Literal["ObjectNotFound"]
    parameters: ObjectNotFoundParameters
    error_instance_id: str


class ObjectSetNotFoundParameters(typing_extensions.TypedDict):
    """The requested object set is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSetRid: ontologies_models.ObjectSetRid


@dataclass
class ObjectSetNotFound(errors.NotFoundError):
    name: typing.Literal["ObjectSetNotFound"]
    parameters: ObjectSetNotFoundParameters
    error_instance_id: str


class ObjectTypeNotFoundParameters(typing_extensions.TypedDict):
    """The requested object type is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: typing_extensions.NotRequired[ontologies_models.ObjectTypeApiName]
    objectTypeRid: typing_extensions.NotRequired[ontologies_models.ObjectTypeRid]


@dataclass
class ObjectTypeNotFound(errors.NotFoundError):
    name: typing.Literal["ObjectTypeNotFound"]
    parameters: ObjectTypeNotFoundParameters
    error_instance_id: str


class ObjectTypeNotSyncedParameters(typing_extensions.TypedDict):
    """
    The requested object type is not synced into the ontology. Please reach out to your Ontology
    Administrator to re-index the object type in Ontology Management Application.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: ontologies_models.ObjectTypeApiName


@dataclass
class ObjectTypeNotSynced(errors.ConflictError):
    name: typing.Literal["ObjectTypeNotSynced"]
    parameters: ObjectTypeNotSyncedParameters
    error_instance_id: str


class ObjectTypesNotSyncedParameters(typing_extensions.TypedDict):
    """
    One or more of the requested object types are not synced into the ontology. Please reach out to your Ontology
    Administrator to re-index the object type(s) in Ontology Management Application.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectTypes: typing.List[ontologies_models.ObjectTypeApiName]


@dataclass
class ObjectTypesNotSynced(errors.ConflictError):
    name: typing.Literal["ObjectTypesNotSynced"]
    parameters: ObjectTypesNotSyncedParameters
    error_instance_id: str


class ObjectsExceededLimitParameters(typing_extensions.TypedDict):
    """
    There are more objects, but they cannot be returned by this API. Only 10,000 objects are available through this
    API for a given request.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ObjectsExceededLimit(errors.BadRequestError):
    name: typing.Literal["ObjectsExceededLimit"]
    parameters: ObjectsExceededLimitParameters
    error_instance_id: str


class OntologyApiNameNotUniqueParameters(typing_extensions.TypedDict):
    """The given Ontology API name is not unique. Use the Ontology RID in place of the Ontology API name."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    ontologyApiName: ontologies_models.OntologyApiName


@dataclass
class OntologyApiNameNotUnique(errors.BadRequestError):
    name: typing.Literal["OntologyApiNameNotUnique"]
    parameters: OntologyApiNameNotUniqueParameters
    error_instance_id: str


class OntologyEditsExceededLimitParameters(typing_extensions.TypedDict):
    """
    The number of edits to the Ontology exceeded the allowed limit.
    This may happen because of the request or because the Action is modifying too many objects.
    Please change the size of your request or contact the Ontology administrator.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    editsCount: int
    editsLimit: int


@dataclass
class OntologyEditsExceededLimit(errors.BadRequestError):
    name: typing.Literal["OntologyEditsExceededLimit"]
    parameters: OntologyEditsExceededLimitParameters
    error_instance_id: str


class OntologyNotFoundParameters(typing_extensions.TypedDict):
    """The requested Ontology is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    ontologyRid: typing_extensions.NotRequired[ontologies_models.OntologyRid]
    apiName: typing_extensions.NotRequired[ontologies_models.OntologyApiName]


@dataclass
class OntologyNotFound(errors.NotFoundError):
    name: typing.Literal["OntologyNotFound"]
    parameters: OntologyNotFoundParameters
    error_instance_id: str


class OntologySyncingParameters(typing_extensions.TypedDict):
    """
    The requested object type has been changed in the **Ontology Manager** and changes are currently being applied. Wait a
    few seconds and try again.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: ontologies_models.ObjectTypeApiName


@dataclass
class OntologySyncing(errors.ConflictError):
    name: typing.Literal["OntologySyncing"]
    parameters: OntologySyncingParameters
    error_instance_id: str


class OntologySyncingObjectTypesParameters(typing_extensions.TypedDict):
    """
    One or more requested object types have been changed in the **Ontology Manager** and changes are currently being
    applied. Wait a few seconds and try again.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectTypes: typing.List[ontologies_models.ObjectTypeApiName]


@dataclass
class OntologySyncingObjectTypes(errors.ConflictError):
    name: typing.Literal["OntologySyncingObjectTypes"]
    parameters: OntologySyncingObjectTypesParameters
    error_instance_id: str


class ParameterObjectNotFoundParameters(typing_extensions.TypedDict):
    """The parameter object reference or parameter default value is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: ontologies_models.ObjectTypeApiName
    primaryKey: typing.Dict[ontologies_models.PropertyApiName, ontologies_models.PrimaryKeyValue]


@dataclass
class ParameterObjectNotFound(errors.NotFoundError):
    name: typing.Literal["ParameterObjectNotFound"]
    parameters: ParameterObjectNotFoundParameters
    error_instance_id: str


class ParameterObjectSetRidNotFoundParameters(typing_extensions.TypedDict):
    """The parameter object set RID is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSetRid: core.RID


@dataclass
class ParameterObjectSetRidNotFound(errors.NotFoundError):
    name: typing.Literal["ParameterObjectSetRidNotFound"]
    parameters: ParameterObjectSetRidNotFoundParameters
    error_instance_id: str


class ParameterTypeNotSupportedParameters(typing_extensions.TypedDict):
    """
    The type of the requested parameter is not currently supported by this API. If you need support for this,
    please reach out to Palantir Support.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameterId: ontologies_models.ParameterId
    parameterBaseType: ontologies_models.ValueType


@dataclass
class ParameterTypeNotSupported(errors.BadRequestError):
    name: typing.Literal["ParameterTypeNotSupported"]
    parameters: ParameterTypeNotSupportedParameters
    error_instance_id: str


class ParametersNotFoundParameters(typing_extensions.TypedDict):
    """
    The provided parameter ID was not found for the action. Please look at the `configuredParameterIds` field
    to see which ones are available.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    actionType: ontologies_models.ActionTypeApiName
    unknownParameterIds: typing.List[ontologies_models.ParameterId]
    configuredParameterIds: typing.List[ontologies_models.ParameterId]


@dataclass
class ParametersNotFound(errors.BadRequestError):
    name: typing.Literal["ParametersNotFound"]
    parameters: ParametersNotFoundParameters
    error_instance_id: str


class ParentAttachmentPermissionDeniedParameters(typing_extensions.TypedDict):
    """The user does not have permission to parent attachments."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ParentAttachmentPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ParentAttachmentPermissionDenied"]
    parameters: ParentAttachmentPermissionDeniedParameters
    error_instance_id: str


class PropertiesHaveDifferentIdsParameters(typing_extensions.TypedDict):
    """Properties used in ordering must have the same ids. Temporary restriction imposed due to OSS limitations."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    properties: typing.List[ontologies_models.SharedPropertyTypeApiName]


@dataclass
class PropertiesHaveDifferentIds(errors.BadRequestError):
    name: typing.Literal["PropertiesHaveDifferentIds"]
    parameters: PropertiesHaveDifferentIdsParameters
    error_instance_id: str


class PropertiesNotFilterableParameters(typing_extensions.TypedDict):
    """
    Results could not be filtered by the requested properties. Please mark the properties as *Searchable* and
    *Selectable* in the **Ontology Manager** to be able to filter on those properties. There may be a short delay
    between the time a property is marked *Searchable* and *Selectable* and when it can be used.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    properties: typing.List[ontologies_models.PropertyApiName]


@dataclass
class PropertiesNotFilterable(errors.BadRequestError):
    name: typing.Literal["PropertiesNotFilterable"]
    parameters: PropertiesNotFilterableParameters
    error_instance_id: str


class PropertiesNotFoundParameters(typing_extensions.TypedDict):
    """The requested properties are not found on the object type."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: ontologies_models.ObjectTypeApiName
    properties: typing.List[ontologies_models.PropertyApiName]


@dataclass
class PropertiesNotFound(errors.NotFoundError):
    name: typing.Literal["PropertiesNotFound"]
    parameters: PropertiesNotFoundParameters
    error_instance_id: str


class PropertiesNotSearchableParameters(typing_extensions.TypedDict):
    """
    Search is not enabled on the specified properties. Please mark the properties as *Searchable*
    in the **Ontology Manager** to enable search on them. There may be a short delay
    between the time a property is marked *Searchable* and when it can be used.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyApiNames: typing.List[ontologies_models.PropertyApiName]


@dataclass
class PropertiesNotSearchable(errors.BadRequestError):
    name: typing.Literal["PropertiesNotSearchable"]
    parameters: PropertiesNotSearchableParameters
    error_instance_id: str


class PropertiesNotSortableParameters(typing_extensions.TypedDict):
    """
    Results could not be ordered by the requested properties. Please mark the properties as *Searchable* and
    *Sortable* in the **Ontology Manager** to enable their use in `orderBy` parameters. There may be a short delay
    between the time a property is set to *Searchable* and *Sortable* and when it can be used.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    properties: typing.List[ontologies_models.PropertyApiName]


@dataclass
class PropertiesNotSortable(errors.BadRequestError):
    name: typing.Literal["PropertiesNotSortable"]
    parameters: PropertiesNotSortableParameters
    error_instance_id: str


class PropertyApiNameNotFoundParameters(typing_extensions.TypedDict):
    """
    A property that was required to have an API name, such as a primary key, is missing one. You can set an API
    name for it using the **Ontology Manager**.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyId: ontologies_models.PropertyId
    propertyBaseType: ontologies_models.ValueType


@dataclass
class PropertyApiNameNotFound(errors.BadRequestError):
    name: typing.Literal["PropertyApiNameNotFound"]
    parameters: PropertyApiNameNotFoundParameters
    error_instance_id: str


class PropertyBaseTypeNotSupportedParameters(typing_extensions.TypedDict):
    """
    The type of the requested property is not currently supported by this API. If you need support for this,
    please reach out to Palantir Support.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: ontologies_models.ObjectTypeApiName
    property: ontologies_models.PropertyApiName
    propertyBaseType: ontologies_models.ValueType


@dataclass
class PropertyBaseTypeNotSupported(errors.BadRequestError):
    name: typing.Literal["PropertyBaseTypeNotSupported"]
    parameters: PropertyBaseTypeNotSupportedParameters
    error_instance_id: str


class PropertyExactMatchingNotSupportedParameters(typing_extensions.TypedDict):
    """A property that does not support exact matching is used in a setting that requires exact matching."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyBaseType: ontologies_models.ValueType
    propertyTypeRid: typing_extensions.NotRequired[ontologies_models.PropertyTypeRid]


@dataclass
class PropertyExactMatchingNotSupported(errors.BadRequestError):
    name: typing.Literal["PropertyExactMatchingNotSupported"]
    parameters: PropertyExactMatchingNotSupportedParameters
    error_instance_id: str


class PropertyFiltersNotSupportedParameters(typing_extensions.TypedDict):
    """
    At least one of the requested property filters are not supported. See the documentation of `PropertyFilter` for
    a list of supported property filters.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyFilters: typing.List[ontologies_models.PropertyFilter]
    property: ontologies_models.PropertyApiName


@dataclass
class PropertyFiltersNotSupported(errors.BadRequestError):
    name: typing.Literal["PropertyFiltersNotSupported"]
    parameters: PropertyFiltersNotSupportedParameters
    error_instance_id: str


class PropertyNotFoundParameters(typing_extensions.TypedDict):
    """Failed to find a provided property for a given object."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class PropertyNotFound(errors.BadRequestError):
    name: typing.Literal["PropertyNotFound"]
    parameters: PropertyNotFoundParameters
    error_instance_id: str


class PropertyNotFoundOnObjectParameters(typing_extensions.TypedDict):
    """Could not find the given property on the object. The user may not have permissions to see this property or it may be configured incorrectly."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectTypeRid: ontologies_models.ObjectTypeRid
    objectRid: ontologies_models.ObjectRid
    objectPropertyRid: ontologies_models.PropertyTypeRid


@dataclass
class PropertyNotFoundOnObject(errors.BadRequestError):
    name: typing.Literal["PropertyNotFoundOnObject"]
    parameters: PropertyNotFoundOnObjectParameters
    error_instance_id: str


class PropertyTypeDoesNotSupportNearestNeighborsParameters(typing_extensions.TypedDict):
    """The provided propertyIdentifier is not configured with an embedding model in the ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class PropertyTypeDoesNotSupportNearestNeighbors(errors.BadRequestError):
    name: typing.Literal["PropertyTypeDoesNotSupportNearestNeighbors"]
    parameters: PropertyTypeDoesNotSupportNearestNeighborsParameters
    error_instance_id: str


class PropertyTypeNotFoundParameters(typing_extensions.TypedDict):
    """The requested property type is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectTypeApiName: typing_extensions.NotRequired[ontologies_models.ObjectTypeApiName]
    propertyApiName: typing_extensions.NotRequired[ontologies_models.PropertyApiName]


@dataclass
class PropertyTypeNotFound(errors.NotFoundError):
    name: typing.Literal["PropertyTypeNotFound"]
    parameters: PropertyTypeNotFoundParameters
    error_instance_id: str


class PropertyTypeRidNotFoundParameters(typing_extensions.TypedDict):
    """The requested property type RID is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyTypeRid: typing_extensions.NotRequired[ontologies_models.PropertyTypeRid]


@dataclass
class PropertyTypeRidNotFound(errors.NotFoundError):
    name: typing.Literal["PropertyTypeRidNotFound"]
    parameters: PropertyTypeRidNotFoundParameters
    error_instance_id: str


class PropertyTypesSearchNotSupportedParameters(typing_extensions.TypedDict):
    """
    The search on the property types are not supported. See the `Search Objects` documentation for
    a list of supported search queries on different property types.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameters: typing.Dict[
        ontologies_models.PropertyFilter, typing.List[ontologies_models.PropertyApiName]
    ]


@dataclass
class PropertyTypesSearchNotSupported(errors.BadRequestError):
    name: typing.Literal["PropertyTypesSearchNotSupported"]
    parameters: PropertyTypesSearchNotSupportedParameters
    error_instance_id: str


class QueryEncounteredUserFacingErrorParameters(typing_extensions.TypedDict):
    """
    The authored `Query` failed to execute because of a user induced error. The message argument
    is meant to be displayed to the user.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: ontologies_models.FunctionRid
    functionVersion: ontologies_models.FunctionVersion
    message: str


@dataclass
class QueryEncounteredUserFacingError(errors.ConflictError):
    name: typing.Literal["QueryEncounteredUserFacingError"]
    parameters: QueryEncounteredUserFacingErrorParameters
    error_instance_id: str


class QueryMemoryExceededLimitParameters(typing_extensions.TypedDict):
    """Memory limits were exceeded for the `Query` execution."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: ontologies_models.FunctionRid
    functionVersion: ontologies_models.FunctionVersion


@dataclass
class QueryMemoryExceededLimit(errors.InternalServerError):
    name: typing.Literal["QueryMemoryExceededLimit"]
    parameters: QueryMemoryExceededLimitParameters
    error_instance_id: str


class QueryNotFoundParameters(typing_extensions.TypedDict):
    """The query is not found, or the user does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    query: ontologies_models.QueryApiName


@dataclass
class QueryNotFound(errors.NotFoundError):
    name: typing.Literal["QueryNotFound"]
    parameters: QueryNotFoundParameters
    error_instance_id: str


class QueryRuntimeErrorParameters(typing_extensions.TypedDict):
    """The authored `Query` failed to execute because of a runtime error."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: ontologies_models.FunctionRid
    functionVersion: ontologies_models.FunctionVersion
    message: typing_extensions.NotRequired[str]
    stacktrace: typing_extensions.NotRequired[str]
    parameters: typing.Dict[ontologies_models.QueryRuntimeErrorParameter, str]


@dataclass
class QueryRuntimeError(errors.BadRequestError):
    name: typing.Literal["QueryRuntimeError"]
    parameters: QueryRuntimeErrorParameters
    error_instance_id: str


class QueryTimeExceededLimitParameters(typing_extensions.TypedDict):
    """Time limits were exceeded for the `Query` execution."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    functionRid: ontologies_models.FunctionRid
    functionVersion: ontologies_models.FunctionVersion


@dataclass
class QueryTimeExceededLimit(errors.InternalServerError):
    name: typing.Literal["QueryTimeExceededLimit"]
    parameters: QueryTimeExceededLimitParameters
    error_instance_id: str


class QueryVersionNotFoundParameters(typing_extensions.TypedDict):
    """The query could not be found at the provided version."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: ontologies_models.QueryApiName
    version: ontologies_models.FunctionVersion


@dataclass
class QueryVersionNotFound(errors.NotFoundError):
    name: typing.Literal["QueryVersionNotFound"]
    parameters: QueryVersionNotFoundParameters
    error_instance_id: str


class RateLimitReachedParameters(typing_extensions.TypedDict):
    """Unable to decrypt this CipherText because the available rate limits in Cipher licenses were reached."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    cipherChannel: core.RID


@dataclass
class RateLimitReached(errors.PermissionDeniedError):
    name: typing.Literal["RateLimitReached"]
    parameters: RateLimitReachedParameters
    error_instance_id: str


class SharedPropertiesNotFoundParameters(typing_extensions.TypedDict):
    """The requested shared property types are not present on every object type."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: typing.List[ontologies_models.ObjectTypeApiName]
    missingSharedProperties: typing.List[ontologies_models.SharedPropertyTypeApiName]


@dataclass
class SharedPropertiesNotFound(errors.NotFoundError):
    name: typing.Literal["SharedPropertiesNotFound"]
    parameters: SharedPropertiesNotFoundParameters
    error_instance_id: str


class SharedPropertyTypeNotFoundParameters(typing_extensions.TypedDict):
    """The requested shared property type is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: typing_extensions.NotRequired[ontologies_models.SharedPropertyTypeApiName]
    rid: typing_extensions.NotRequired[ontologies_models.SharedPropertyTypeRid]


@dataclass
class SharedPropertyTypeNotFound(errors.NotFoundError):
    name: typing.Literal["SharedPropertyTypeNotFound"]
    parameters: SharedPropertyTypeNotFoundParameters
    error_instance_id: str


class TooManyNearestNeighborsRequestedParameters(typing_extensions.TypedDict):
    """The value of numNeighbors must be in the range 1 &lt;= numNeighbors &lt;= 500."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    requestedNumNeighbors: int
    maxNumNeighbors: int


@dataclass
class TooManyNearestNeighborsRequested(errors.BadRequestError):
    name: typing.Literal["TooManyNearestNeighborsRequested"]
    parameters: TooManyNearestNeighborsRequestedParameters
    error_instance_id: str


class UnauthorizedCipherOperationParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to take a specific Cipher operation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    cipherChannel: core.RID


@dataclass
class UnauthorizedCipherOperation(errors.PermissionDeniedError):
    name: typing.Literal["UnauthorizedCipherOperation"]
    parameters: UnauthorizedCipherOperationParameters
    error_instance_id: str


class UndecryptableValueParameters(typing_extensions.TypedDict):
    """
    The value intended for decryption with Cipher cannot be decrypted.
    Ensure it is correctly formatted (CIPHER::<cipher-channel-rid>:<encrypted-value>::CIPHER).
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: str


@dataclass
class UndecryptableValue(errors.BadRequestError):
    name: typing.Literal["UndecryptableValue"]
    parameters: UndecryptableValueParameters
    error_instance_id: str


class UnknownParameterParameters(typing_extensions.TypedDict):
    """
    The provided parameters were not found. Please look at the `knownParameters` field
    to see which ones are available.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    unknownParameters: typing.List[ontologies_models.ParameterId]
    expectedParameters: typing.List[ontologies_models.ParameterId]


@dataclass
class UnknownParameter(errors.BadRequestError):
    name: typing.Literal["UnknownParameter"]
    parameters: UnknownParameterParameters
    error_instance_id: str


class UnsupportedObjectSetParameters(typing_extensions.TypedDict):
    """The requested object set is not supported."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class UnsupportedObjectSet(errors.BadRequestError):
    name: typing.Literal["UnsupportedObjectSet"]
    parameters: UnsupportedObjectSetParameters
    error_instance_id: str


class ValueTypeNotFoundParameters(typing_extensions.TypedDict):
    """The value type is not found, or the user does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    valueType: typing_extensions.NotRequired[ontologies_models.ValueTypeApiName]
    rid: typing_extensions.NotRequired[ontologies_models.ValueTypeRid]


@dataclass
class ValueTypeNotFound(errors.NotFoundError):
    name: typing.Literal["ValueTypeNotFound"]
    parameters: ValueTypeNotFoundParameters
    error_instance_id: str


class ViewObjectPermissionDeniedParameters(typing_extensions.TypedDict):
    """
    The provided token does not have permission to view any data sources backing this object type. Ensure the object
    type has backing data sources configured and visible.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: ontologies_models.ObjectTypeApiName


@dataclass
class ViewObjectPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ViewObjectPermissionDenied"]
    parameters: ViewObjectPermissionDeniedParameters
    error_instance_id: str


__all__ = [
    "ActionContainsDuplicateEdits",
    "ActionEditedPropertiesNotFound",
    "ActionEditsReadOnlyEntity",
    "ActionNotFound",
    "ActionParameterInterfaceTypeNotFound",
    "ActionParameterObjectNotFound",
    "ActionParameterObjectTypeNotFound",
    "ActionTypeNotFound",
    "ActionValidationFailed",
    "AggregationAccuracyNotSupported",
    "AggregationGroupCountExceededLimit",
    "AggregationMemoryExceededLimit",
    "AggregationNestedObjectSetSizeExceededLimit",
    "ApplyActionFailed",
    "AttachmentNotFound",
    "AttachmentSizeExceededLimit",
    "CipherChannelNotFound",
    "CompositePrimaryKeyNotSupported",
    "DefaultAndNullGroupsNotSupported",
    "DerivedPropertyApiNamesNotUnique",
    "DuplicateOrderBy",
    "EditObjectPermissionDenied",
    "FunctionEncounteredUserFacingError",
    "FunctionExecutionFailed",
    "FunctionExecutionTimedOut",
    "FunctionInvalidInput",
    "HighScaleComputationNotEnabled",
    "InterfaceLinkTypeNotFound",
    "InterfaceTypeNotFound",
    "InterfaceTypesNotFound",
    "InvalidAggregationOrdering",
    "InvalidAggregationOrderingWithNullValues",
    "InvalidAggregationRange",
    "InvalidAggregationRangePropertyType",
    "InvalidAggregationRangeValue",
    "InvalidApplyActionOptionCombination",
    "InvalidContentLength",
    "InvalidContentType",
    "InvalidDerivedPropertyDefinition",
    "InvalidDurationGroupByPropertyType",
    "InvalidDurationGroupByValue",
    "InvalidFields",
    "InvalidGroupId",
    "InvalidOrderType",
    "InvalidParameterValue",
    "InvalidPropertyFilterValue",
    "InvalidPropertyFiltersCombination",
    "InvalidPropertyType",
    "InvalidPropertyValue",
    "InvalidQueryOutputValue",
    "InvalidQueryParameterValue",
    "InvalidRangeQuery",
    "InvalidSortOrder",
    "InvalidSortType",
    "InvalidUserId",
    "InvalidVectorDimension",
    "LinkAlreadyExists",
    "LinkTypeNotFound",
    "LinkedObjectNotFound",
    "MalformedPropertyFilters",
    "MarketplaceActionMappingNotFound",
    "MarketplaceInstallationNotFound",
    "MarketplaceLinkMappingNotFound",
    "MarketplaceObjectMappingNotFound",
    "MarketplaceQueryMappingNotFound",
    "MarketplaceSdkActionMappingNotFound",
    "MarketplaceSdkInstallationNotFound",
    "MarketplaceSdkLinkMappingNotFound",
    "MarketplaceSdkObjectMappingNotFound",
    "MarketplaceSdkPropertyMappingNotFound",
    "MarketplaceSdkQueryMappingNotFound",
    "MissingParameter",
    "MultipleGroupByOnFieldNotSupported",
    "MultiplePropertyValuesNotSupported",
    "NotCipherFormatted",
    "ObjectAlreadyExists",
    "ObjectChanged",
    "ObjectNotFound",
    "ObjectSetNotFound",
    "ObjectTypeNotFound",
    "ObjectTypeNotSynced",
    "ObjectTypesNotSynced",
    "ObjectsExceededLimit",
    "OntologyApiNameNotUnique",
    "OntologyEditsExceededLimit",
    "OntologyNotFound",
    "OntologySyncing",
    "OntologySyncingObjectTypes",
    "ParameterObjectNotFound",
    "ParameterObjectSetRidNotFound",
    "ParameterTypeNotSupported",
    "ParametersNotFound",
    "ParentAttachmentPermissionDenied",
    "PropertiesHaveDifferentIds",
    "PropertiesNotFilterable",
    "PropertiesNotFound",
    "PropertiesNotSearchable",
    "PropertiesNotSortable",
    "PropertyApiNameNotFound",
    "PropertyBaseTypeNotSupported",
    "PropertyExactMatchingNotSupported",
    "PropertyFiltersNotSupported",
    "PropertyNotFound",
    "PropertyNotFoundOnObject",
    "PropertyTypeDoesNotSupportNearestNeighbors",
    "PropertyTypeNotFound",
    "PropertyTypeRidNotFound",
    "PropertyTypesSearchNotSupported",
    "QueryEncounteredUserFacingError",
    "QueryMemoryExceededLimit",
    "QueryNotFound",
    "QueryRuntimeError",
    "QueryTimeExceededLimit",
    "QueryVersionNotFound",
    "RateLimitReached",
    "SharedPropertiesNotFound",
    "SharedPropertyTypeNotFound",
    "TooManyNearestNeighborsRequested",
    "UnauthorizedCipherOperation",
    "UndecryptableValue",
    "UnknownParameter",
    "UnsupportedObjectSet",
    "ValueTypeNotFound",
    "ViewObjectPermissionDenied",
]
