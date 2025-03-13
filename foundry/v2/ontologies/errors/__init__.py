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


from foundry.v2.ontologies.errors._action_contains_duplicate_edits import (
    ActionContainsDuplicateEdits,
)  # NOQA
from foundry.v2.ontologies.errors._action_edited_properties_not_found import (
    ActionEditedPropertiesNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._action_edits_read_only_entity import (
    ActionEditsReadOnlyEntity,
)  # NOQA
from foundry.v2.ontologies.errors._action_not_found import ActionNotFound
from foundry.v2.ontologies.errors._action_parameter_interface_type_not_found import (
    ActionParameterInterfaceTypeNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._action_parameter_object_not_found import (
    ActionParameterObjectNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._action_parameter_object_type_not_found import (
    ActionParameterObjectTypeNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._action_type_not_found import ActionTypeNotFound
from foundry.v2.ontologies.errors._action_validation_failed import ActionValidationFailed  # NOQA
from foundry.v2.ontologies.errors._aggregation_group_count_exceeded_limit import (
    AggregationGroupCountExceededLimit,
)  # NOQA
from foundry.v2.ontologies.errors._aggregation_memory_exceeded_limit import (
    AggregationMemoryExceededLimit,
)  # NOQA
from foundry.v2.ontologies.errors._aggregation_nested_object_set_size_exceeded_limit import (
    AggregationNestedObjectSetSizeExceededLimit,
)  # NOQA
from foundry.v2.ontologies.errors._apply_action_failed import ApplyActionFailed
from foundry.v2.ontologies.errors._attachment_not_found import AttachmentNotFound
from foundry.v2.ontologies.errors._attachment_size_exceeded_limit import (
    AttachmentSizeExceededLimit,
)  # NOQA
from foundry.v2.ontologies.errors._composite_primary_key_not_supported import (
    CompositePrimaryKeyNotSupported,
)  # NOQA
from foundry.v2.ontologies.errors._derived_property_api_names_not_unique import (
    DerivedPropertyApiNamesNotUnique,
)  # NOQA
from foundry.v2.ontologies.errors._duplicate_order_by import DuplicateOrderBy
from foundry.v2.ontologies.errors._duration_out_of_bounds import DurationOutOfBounds
from foundry.v2.ontologies.errors._edit_object_permission_denied import (
    EditObjectPermissionDenied,
)  # NOQA
from foundry.v2.ontologies.errors._function_encountered_user_facing_error import (
    FunctionEncounteredUserFacingError,
)  # NOQA
from foundry.v2.ontologies.errors._function_execution_failed import FunctionExecutionFailed  # NOQA
from foundry.v2.ontologies.errors._function_execution_timed_out import (
    FunctionExecutionTimedOut,
)  # NOQA
from foundry.v2.ontologies.errors._function_invalid_input import FunctionInvalidInput
from foundry.v2.ontologies.errors._high_scale_computation_not_enabled import (
    HighScaleComputationNotEnabled,
)  # NOQA
from foundry.v2.ontologies.errors._interface_type_not_found import InterfaceTypeNotFound
from foundry.v2.ontologies.errors._interface_types_not_found import InterfaceTypesNotFound  # NOQA
from foundry.v2.ontologies.errors._invalid_aggregation_ordering import (
    InvalidAggregationOrdering,
)  # NOQA
from foundry.v2.ontologies.errors._invalid_aggregation_range import InvalidAggregationRange  # NOQA
from foundry.v2.ontologies.errors._invalid_aggregation_range_property_type import (
    InvalidAggregationRangePropertyType,
)  # NOQA
from foundry.v2.ontologies.errors._invalid_aggregation_range_value import (
    InvalidAggregationRangeValue,
)  # NOQA
from foundry.v2.ontologies.errors._invalid_apply_action_option_combination import (
    InvalidApplyActionOptionCombination,
)  # NOQA
from foundry.v2.ontologies.errors._invalid_content_length import InvalidContentLength
from foundry.v2.ontologies.errors._invalid_content_type import InvalidContentType
from foundry.v2.ontologies.errors._invalid_duration_group_by_property_type import (
    InvalidDurationGroupByPropertyType,
)  # NOQA
from foundry.v2.ontologies.errors._invalid_duration_group_by_value import (
    InvalidDurationGroupByValue,
)  # NOQA
from foundry.v2.ontologies.errors._invalid_fields import InvalidFields
from foundry.v2.ontologies.errors._invalid_group_id import InvalidGroupId
from foundry.v2.ontologies.errors._invalid_order_type import InvalidOrderType
from foundry.v2.ontologies.errors._invalid_parameter_value import InvalidParameterValue
from foundry.v2.ontologies.errors._invalid_property_filter_value import (
    InvalidPropertyFilterValue,
)  # NOQA
from foundry.v2.ontologies.errors._invalid_property_filters_combination import (
    InvalidPropertyFiltersCombination,
)  # NOQA
from foundry.v2.ontologies.errors._invalid_property_type import InvalidPropertyType
from foundry.v2.ontologies.errors._invalid_property_value import InvalidPropertyValue
from foundry.v2.ontologies.errors._invalid_query_parameter_value import (
    InvalidQueryParameterValue,
)  # NOQA
from foundry.v2.ontologies.errors._invalid_range_query import InvalidRangeQuery
from foundry.v2.ontologies.errors._invalid_sort_order import InvalidSortOrder
from foundry.v2.ontologies.errors._invalid_sort_type import InvalidSortType
from foundry.v2.ontologies.errors._invalid_user_id import InvalidUserId
from foundry.v2.ontologies.errors._link_already_exists import LinkAlreadyExists
from foundry.v2.ontologies.errors._link_type_not_found import LinkTypeNotFound
from foundry.v2.ontologies.errors._linked_object_not_found import LinkedObjectNotFound
from foundry.v2.ontologies.errors._malformed_property_filters import (
    MalformedPropertyFilters,
)  # NOQA
from foundry.v2.ontologies.errors._marketplace_action_mapping_not_found import (
    MarketplaceActionMappingNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._marketplace_installation_not_found import (
    MarketplaceInstallationNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._marketplace_link_mapping_not_found import (
    MarketplaceLinkMappingNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._marketplace_object_mapping_not_found import (
    MarketplaceObjectMappingNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._marketplace_query_mapping_not_found import (
    MarketplaceQueryMappingNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._missing_parameter import MissingParameter
from foundry.v2.ontologies.errors._multiple_group_by_on_field_not_supported import (
    MultipleGroupByOnFieldNotSupported,
)  # NOQA
from foundry.v2.ontologies.errors._multiple_property_values_not_supported import (
    MultiplePropertyValuesNotSupported,
)  # NOQA
from foundry.v2.ontologies.errors._object_already_exists import ObjectAlreadyExists
from foundry.v2.ontologies.errors._object_changed import ObjectChanged
from foundry.v2.ontologies.errors._object_not_found import ObjectNotFound
from foundry.v2.ontologies.errors._object_set_not_found import ObjectSetNotFound
from foundry.v2.ontologies.errors._object_type_not_found import ObjectTypeNotFound
from foundry.v2.ontologies.errors._object_type_not_synced import ObjectTypeNotSynced
from foundry.v2.ontologies.errors._object_types_not_synced import ObjectTypesNotSynced
from foundry.v2.ontologies.errors._objects_exceeded_limit import ObjectsExceededLimit
from foundry.v2.ontologies.errors._ontology_api_name_not_unique import (
    OntologyApiNameNotUnique,
)  # NOQA
from foundry.v2.ontologies.errors._ontology_edits_exceeded_limit import (
    OntologyEditsExceededLimit,
)  # NOQA
from foundry.v2.ontologies.errors._ontology_not_found import OntologyNotFound
from foundry.v2.ontologies.errors._ontology_syncing import OntologySyncing
from foundry.v2.ontologies.errors._ontology_syncing_object_types import (
    OntologySyncingObjectTypes,
)  # NOQA
from foundry.v2.ontologies.errors._parameter_object_not_found import ParameterObjectNotFound  # NOQA
from foundry.v2.ontologies.errors._parameter_object_set_rid_not_found import (
    ParameterObjectSetRidNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._parameter_type_not_supported import (
    ParameterTypeNotSupported,
)  # NOQA
from foundry.v2.ontologies.errors._parameters_not_found import ParametersNotFound
from foundry.v2.ontologies.errors._parent_attachment_permission_denied import (
    ParentAttachmentPermissionDenied,
)  # NOQA
from foundry.v2.ontologies.errors._properties_have_different_ids import (
    PropertiesHaveDifferentIds,
)  # NOQA
from foundry.v2.ontologies.errors._properties_not_filterable import PropertiesNotFilterable  # NOQA
from foundry.v2.ontologies.errors._properties_not_found import PropertiesNotFound
from foundry.v2.ontologies.errors._properties_not_searchable import PropertiesNotSearchable  # NOQA
from foundry.v2.ontologies.errors._properties_not_sortable import PropertiesNotSortable
from foundry.v2.ontologies.errors._property_api_name_not_found import (
    PropertyApiNameNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._property_base_type_not_supported import (
    PropertyBaseTypeNotSupported,
)  # NOQA
from foundry.v2.ontologies.errors._property_filters_not_supported import (
    PropertyFiltersNotSupported,
)  # NOQA
from foundry.v2.ontologies.errors._property_not_found import PropertyNotFound
from foundry.v2.ontologies.errors._property_type_does_not_support_nearest_neighbors import (
    PropertyTypeDoesNotSupportNearestNeighbors,
)  # NOQA
from foundry.v2.ontologies.errors._property_type_not_found import PropertyTypeNotFound
from foundry.v2.ontologies.errors._property_types_search_not_supported import (
    PropertyTypesSearchNotSupported,
)  # NOQA
from foundry.v2.ontologies.errors._query_encountered_user_facing_error import (
    QueryEncounteredUserFacingError,
)  # NOQA
from foundry.v2.ontologies.errors._query_memory_exceeded_limit import (
    QueryMemoryExceededLimit,
)  # NOQA
from foundry.v2.ontologies.errors._query_not_found import QueryNotFound
from foundry.v2.ontologies.errors._query_runtime_error import QueryRuntimeError
from foundry.v2.ontologies.errors._query_time_exceeded_limit import QueryTimeExceededLimit  # NOQA
from foundry.v2.ontologies.errors._search_vector_dimensions_differ import (
    SearchVectorDimensionsDiffer,
)  # NOQA
from foundry.v2.ontologies.errors._shared_properties_not_found import (
    SharedPropertiesNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._shared_property_type_not_found import (
    SharedPropertyTypeNotFound,
)  # NOQA
from foundry.v2.ontologies.errors._too_many_nearest_neighbors_requested import (
    TooManyNearestNeighborsRequested,
)  # NOQA
from foundry.v2.ontologies.errors._unknown_parameter import UnknownParameter
from foundry.v2.ontologies.errors._unsupported_object_set import UnsupportedObjectSet
from foundry.v2.ontologies.errors._view_object_permission_denied import (
    ViewObjectPermissionDenied,
)  # NOQA

__all__ = [
    "ActionTypeNotFound",
    "MarketplaceLinkMappingNotFound",
    "MalformedPropertyFilters",
    "InvalidAggregationRangeValue",
    "ObjectTypeNotSynced",
    "OntologyEditsExceededLimit",
    "ActionParameterObjectTypeNotFound",
    "AggregationGroupCountExceededLimit",
    "DerivedPropertyApiNamesNotUnique",
    "ActionParameterInterfaceTypeNotFound",
    "ActionNotFound",
    "UnknownParameter",
    "MarketplaceObjectMappingNotFound",
    "ParameterObjectSetRidNotFound",
    "FunctionExecutionFailed",
    "InvalidDurationGroupByValue",
    "InvalidContentType",
    "PropertiesNotFound",
    "FunctionInvalidInput",
    "ActionEditsReadOnlyEntity",
    "InvalidSortOrder",
    "DurationOutOfBounds",
    "InvalidAggregationOrdering",
    "InvalidSortType",
    "PropertyNotFound",
    "InvalidPropertyFiltersCombination",
    "ObjectAlreadyExists",
    "OntologyApiNameNotUnique",
    "PropertiesNotFilterable",
    "ObjectsExceededLimit",
    "ObjectSetNotFound",
    "DuplicateOrderBy",
    "FunctionEncounteredUserFacingError",
    "ParametersNotFound",
    "LinkTypeNotFound",
    "HighScaleComputationNotEnabled",
    "InvalidUserId",
    "AggregationNestedObjectSetSizeExceededLimit",
    "AggregationMemoryExceededLimit",
    "PropertyFiltersNotSupported",
    "MarketplaceQueryMappingNotFound",
    "LinkAlreadyExists",
    "ApplyActionFailed",
    "InvalidRangeQuery",
    "ActionParameterObjectNotFound",
    "ViewObjectPermissionDenied",
    "QueryNotFound",
    "InvalidPropertyValue",
    "ActionValidationFailed",
    "PropertiesNotSortable",
    "MultipleGroupByOnFieldNotSupported",
    "LinkedObjectNotFound",
    "PropertyTypesSearchNotSupported",
    "InvalidParameterValue",
    "ObjectChanged",
    "UnsupportedObjectSet",
    "SharedPropertyTypeNotFound",
    "ActionEditedPropertiesNotFound",
    "OntologySyncingObjectTypes",
    "InvalidAggregationRange",
    "FunctionExecutionTimedOut",
    "ParameterObjectNotFound",
    "QueryMemoryExceededLimit",
    "InvalidApplyActionOptionCombination",
    "QueryTimeExceededLimit",
    "CompositePrimaryKeyNotSupported",
    "InvalidPropertyFilterValue",
    "QueryEncounteredUserFacingError",
    "PropertyBaseTypeNotSupported",
    "ObjectTypesNotSynced",
    "InvalidContentLength",
    "InterfaceTypesNotFound",
    "SharedPropertiesNotFound",
    "InterfaceTypeNotFound",
    "AttachmentSizeExceededLimit",
    "MultiplePropertyValuesNotSupported",
    "QueryRuntimeError",
    "MarketplaceActionMappingNotFound",
    "PropertyTypeDoesNotSupportNearestNeighbors",
    "EditObjectPermissionDenied",
    "PropertiesNotSearchable",
    "AttachmentNotFound",
    "ActionContainsDuplicateEdits",
    "SearchVectorDimensionsDiffer",
    "ObjectTypeNotFound",
    "ObjectNotFound",
    "InvalidOrderType",
    "ParentAttachmentPermissionDenied",
    "PropertyApiNameNotFound",
    "TooManyNearestNeighborsRequested",
    "ParameterTypeNotSupported",
    "InvalidGroupId",
    "PropertiesHaveDifferentIds",
    "InvalidFields",
    "InvalidAggregationRangePropertyType",
    "OntologyNotFound",
    "InvalidQueryParameterValue",
    "OntologySyncing",
    "PropertyTypeNotFound",
    "MarketplaceInstallationNotFound",
    "InvalidPropertyType",
    "InvalidDurationGroupByPropertyType",
    "MissingParameter",
]
