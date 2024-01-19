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

# coding: utf-8

# flake8: noqa
"""
    Palantir OpenAPI

    The Palantir REST API. Please see https://www.palantir.com/docs for more details.

    The version of the OpenAPI document: 1.738.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from foundry.models.abort_transaction_permission_denied import AbortTransactionPermissionDenied
from foundry.models.abort_transaction_permission_denied_parameters import (
    AbortTransactionPermissionDeniedParameters,
)
from foundry.models.action_contains_duplicate_edits import ActionContainsDuplicateEdits
from foundry.models.action_edited_properties_not_found import ActionEditedPropertiesNotFound
from foundry.models.action_not_found import ActionNotFound
from foundry.models.action_not_found_parameters import ActionNotFoundParameters
from foundry.models.action_parameter_type import ActionParameterArrayType
from foundry.models.action_parameter_object_not_found import ActionParameterObjectNotFound
from foundry.models.action_parameter_object_not_found_parameters import (
    ActionParameterObjectNotFoundParameters,
)
from foundry.models.action_parameter_object_type_not_found import ActionParameterObjectTypeNotFound
from foundry.models.action_parameter_type import ActionParameterType
from foundry.models.action_parameter_v2 import ActionParameterV2
from foundry.models.action_type import ActionType
from foundry.models.action_type_not_found import ActionTypeNotFound
from foundry.models.action_type_not_found_parameters import ActionTypeNotFoundParameters
from foundry.models.action_type_v2 import ActionTypeV2
from foundry.models.action_validation_failed import ActionValidationFailed
from foundry.models.action_validation_failed_parameters import ActionValidationFailedParameters
from foundry.models.aggregation_group_count_exceeded_limit import AggregationGroupCountExceededLimit
from foundry.models.aggregation_group_count_exceeded_limit_parameters import (
    AggregationGroupCountExceededLimitParameters,
)
from foundry.models.any_type import AnyType
from foundry.models.api_feature_preview_usage_only import ApiFeaturePreviewUsageOnly
from foundry.models.api_usage_denied import ApiUsageDenied
from foundry.models.apply_action_failed import ApplyActionFailed
from foundry.models.apply_action_mode import ApplyActionMode
from foundry.models.apply_action_request_options import ApplyActionRequestOptions
from foundry.models.async_operation_error import AsyncOperationError
from foundry.models.attachment_not_found import AttachmentNotFound
from foundry.models.attachment_not_found_parameters import AttachmentNotFoundParameters
from foundry.models.attachment_size_exceeded_limit import AttachmentSizeExceededLimit
from foundry.models.attachment_size_exceeded_limit_parameters import (
    AttachmentSizeExceededLimitParameters,
)
from foundry.models.attachment_type import AttachmentType
from foundry.models.binary_type import BinaryType
from foundry.models.boolean_type import BooleanType
from foundry.models.branch import Branch
from foundry.models.branch_already_exists import BranchAlreadyExists
from foundry.models.branch_already_exists_parameters import BranchAlreadyExistsParameters
from foundry.models.branch_not_found import BranchNotFound
from foundry.models.byte_type import ByteType
from foundry.models.column_types_not_supported import ColumnTypesNotSupported
from foundry.models.column_types_not_supported_parameters import ColumnTypesNotSupportedParameters
from foundry.models.commit_transaction_permission_denied import CommitTransactionPermissionDenied
from foundry.models.composite_primary_key_not_supported import CompositePrimaryKeyNotSupported
from foundry.models.composite_primary_key_not_supported_parameters import (
    CompositePrimaryKeyNotSupportedParameters,
)
from foundry.models.create_branch_permission_denied import CreateBranchPermissionDenied
from foundry.models.create_branch_request import CreateBranchRequest
from foundry.models.create_dataset_permission_denied import CreateDatasetPermissionDenied
from foundry.models.create_dataset_permission_denied_parameters import (
    CreateDatasetPermissionDeniedParameters,
)
from foundry.models.create_dataset_request import CreateDatasetRequest
from foundry.models.create_link_rule import CreateLinkRule
from foundry.models.create_object_rule import CreateObjectRule
from foundry.models.create_transaction_permission_denied import CreateTransactionPermissionDenied
from foundry.models.create_transaction_request import CreateTransactionRequest
from foundry.models.dataset import Dataset
from foundry.models.dataset_not_found import DatasetNotFound
from foundry.models.date_type import DateType
from foundry.models.decimal_type import DecimalType
from foundry.models.delete_branch_permission_denied import DeleteBranchPermissionDenied
from foundry.models.delete_link_rule import DeleteLinkRule
from foundry.models.delete_object_rule import DeleteObjectRule
from foundry.models.delete_schema_permission_denied import DeleteSchemaPermissionDenied
from foundry.models.delete_schema_permission_denied_parameters import (
    DeleteSchemaPermissionDeniedParameters,
)
from foundry.models.deployment_api import DeploymentApi
from foundry.models.deployment_listing import DeploymentListing
from foundry.models.deployment_metadata import DeploymentMetadata
from foundry.models.deployment_not_available import DeploymentNotAvailable
from foundry.models.deployment_not_available_parameters import DeploymentNotAvailableParameters
from foundry.models.deployment_not_found import DeploymentNotFound
from foundry.models.deployment_transform_api import DeploymentTransformApi
from foundry.models.distance_unit import DistanceUnit
from foundry.models.double_type import DoubleType
from foundry.models.duplicate_order_by import DuplicateOrderBy
from foundry.models.duplicate_order_by_parameters import DuplicateOrderByParameters
from foundry.models.edit_object_permission_denied import EditObjectPermissionDenied
from foundry.models.file import File
from foundry.models.file_already_exists import FileAlreadyExists
from foundry.models.file_already_exists_parameters import FileAlreadyExistsParameters
from foundry.models.file_not_found_on_branch import FileNotFoundOnBranch
from foundry.models.file_not_found_on_branch_parameters import FileNotFoundOnBranchParameters
from foundry.models.file_not_found_on_transaction_range import FileNotFoundOnTransactionRange
from foundry.models.file_not_found_on_transaction_range_parameters import (
    FileNotFoundOnTransactionRangeParameters,
)
from foundry.models.float_type import FloatType
from foundry.models.folder_not_found import FolderNotFound
from foundry.models.folder_not_found_parameters import FolderNotFoundParameters
from foundry.models.function_encountered_user_facing_error import FunctionEncounteredUserFacingError
from foundry.models.function_encountered_user_facing_error_parameters import (
    FunctionEncounteredUserFacingErrorParameters,
)
from foundry.models.function_execution_failed import FunctionExecutionFailed
from foundry.models.function_execution_failed_parameters import FunctionExecutionFailedParameters
from foundry.models.function_execution_timed_out import FunctionExecutionTimedOut
from foundry.models.function_invalid_input import FunctionInvalidInput
from foundry.models.geo_point import GeoPoint
from foundry.models.geo_point_type import GeoPointType
from foundry.models.geo_shape_type import GeoShapeType
from foundry.models.geometry import Geometry
from foundry.models.geometry import GeometryCollection
from foundry.models.integer_type import IntegerType
from foundry.models.invalid_aggregation_range import InvalidAggregationRange
from foundry.models.invalid_aggregation_range_property_type import (
    InvalidAggregationRangePropertyType,
)
from foundry.models.invalid_aggregation_range_property_type_parameters import (
    InvalidAggregationRangePropertyTypeParameters,
)
from foundry.models.invalid_aggregation_range_value import InvalidAggregationRangeValue
from foundry.models.invalid_apply_action_option_combination import (
    InvalidApplyActionOptionCombination,
)
from foundry.models.invalid_apply_action_option_combination_parameters import (
    InvalidApplyActionOptionCombinationParameters,
)
from foundry.models.invalid_branch_id import InvalidBranchId
from foundry.models.invalid_branch_id_parameters import InvalidBranchIdParameters
from foundry.models.invalid_content_length import InvalidContentLength
from foundry.models.invalid_content_type import InvalidContentType
from foundry.models.invalid_duration_group_by_property_type import (
    InvalidDurationGroupByPropertyType,
)
from foundry.models.invalid_duration_group_by_value import InvalidDurationGroupByValue
from foundry.models.invalid_fields import InvalidFields
from foundry.models.invalid_fields_parameters import InvalidFieldsParameters
from foundry.models.invalid_group_id import InvalidGroupId
from foundry.models.invalid_group_id_parameters import InvalidGroupIdParameters
from foundry.models.invalid_page_size import InvalidPageSize
from foundry.models.invalid_page_size_parameters import InvalidPageSizeParameters
from foundry.models.invalid_page_token import InvalidPageToken
from foundry.models.invalid_page_token_parameters import InvalidPageTokenParameters
from foundry.models.invalid_parameter_combination import InvalidParameterCombination
from foundry.models.invalid_parameter_combination_parameters import (
    InvalidParameterCombinationParameters,
)
from foundry.models.invalid_parameter_value import InvalidParameterValue
from foundry.models.invalid_parameter_value_parameters import InvalidParameterValueParameters
from foundry.models.invalid_property_filter_value import InvalidPropertyFilterValue
from foundry.models.invalid_property_filter_value_parameters import (
    InvalidPropertyFilterValueParameters,
)
from foundry.models.invalid_property_filters_combination import InvalidPropertyFiltersCombination
from foundry.models.invalid_property_filters_combination_parameters import (
    InvalidPropertyFiltersCombinationParameters,
)
from foundry.models.invalid_property_type import InvalidPropertyType
from foundry.models.invalid_property_type_parameters import InvalidPropertyTypeParameters
from foundry.models.invalid_property_value import InvalidPropertyValue
from foundry.models.invalid_property_value_parameters import InvalidPropertyValueParameters
from foundry.models.invalid_query_parameter_value import InvalidQueryParameterValue
from foundry.models.invalid_query_parameter_value_parameters import (
    InvalidQueryParameterValueParameters,
)
from foundry.models.invalid_range_query import InvalidRangeQuery
from foundry.models.invalid_range_query_parameters import InvalidRangeQueryParameters
from foundry.models.invalid_sort_order import InvalidSortOrder
from foundry.models.invalid_sort_order_parameters import InvalidSortOrderParameters
from foundry.models.invalid_sort_type import InvalidSortType
from foundry.models.invalid_sort_type_parameters import InvalidSortTypeParameters
from foundry.models.invalid_transaction_type import InvalidTransactionType
from foundry.models.invalid_transaction_type_parameters import InvalidTransactionTypeParameters
from foundry.models.invalid_user_id import InvalidUserId
from foundry.models.invalid_user_id_parameters import InvalidUserIdParameters
from foundry.models.language_model_source import LanguageModelSource
from foundry.models.language_model_source_not_supported import LanguageModelSourceNotSupported
from foundry.models.language_model_source_not_supported_parameters import (
    LanguageModelSourceNotSupportedParameters,
)
from foundry.models.line_string import LineString
from foundry.models.link_already_exists import LinkAlreadyExists
from foundry.models.link_type_not_found import LinkTypeNotFound
from foundry.models.link_type_not_found_parameters import LinkTypeNotFoundParameters
from foundry.models.link_type_side import LinkTypeSide
from foundry.models.link_type_side_cardinality import LinkTypeSideCardinality
from foundry.models.link_type_side_v2 import LinkTypeSideV2
from foundry.models.linked_object_not_found import LinkedObjectNotFound
from foundry.models.linked_object_not_found_parameters import LinkedObjectNotFoundParameters
from foundry.models.list_action_types_response import ListActionTypesResponse
from foundry.models.list_action_types_response_v2 import ListActionTypesResponseV2
from foundry.models.list_branches_response import ListBranchesResponse
from foundry.models.list_deployments_response import ListDeploymentsResponse
from foundry.models.list_files_response import ListFilesResponse
from foundry.models.list_object_types_response import ListObjectTypesResponse
from foundry.models.list_object_types_v2_response import ListObjectTypesV2Response
from foundry.models.list_ontologies_response import ListOntologiesResponse
from foundry.models.list_ontologies_v2_response import ListOntologiesV2Response
from foundry.models.list_outgoing_link_types_response import ListOutgoingLinkTypesResponse
from foundry.models.list_outgoing_link_types_response_v2 import ListOutgoingLinkTypesResponseV2
from foundry.models.list_query_types_response import ListQueryTypesResponse
from foundry.models.list_query_types_response_v2 import ListQueryTypesResponseV2
from foundry.models.logic_rule import LogicRule
from foundry.models.long_type import LongType
from foundry.models.malformed_property_filters import MalformedPropertyFilters
from foundry.models.malformed_property_filters_parameters import MalformedPropertyFiltersParameters
from foundry.models.marketplace_action_mapping_not_found import MarketplaceActionMappingNotFound
from foundry.models.marketplace_action_mapping_not_found_parameters import (
    MarketplaceActionMappingNotFoundParameters,
)
from foundry.models.marketplace_installation_not_found import MarketplaceInstallationNotFound
from foundry.models.marketplace_installation_not_found_parameters import (
    MarketplaceInstallationNotFoundParameters,
)
from foundry.models.marketplace_link_mapping_not_found import MarketplaceLinkMappingNotFound
from foundry.models.marketplace_link_mapping_not_found_parameters import (
    MarketplaceLinkMappingNotFoundParameters,
)
from foundry.models.marketplace_object_mapping_not_found import MarketplaceObjectMappingNotFound
from foundry.models.marketplace_object_mapping_not_found_parameters import (
    MarketplaceObjectMappingNotFoundParameters,
)
from foundry.models.marketplace_query_mapping_not_found import MarketplaceQueryMappingNotFound
from foundry.models.marketplace_query_mapping_not_found_parameters import (
    MarketplaceQueryMappingNotFoundParameters,
)
from foundry.models.missing_parameter import MissingParameter
from foundry.models.missing_parameter_parameters import MissingParameterParameters
from foundry.models.missing_post_body import MissingPostBody
from foundry.models.model_api_type import ModelApiArrayType
from foundry.models.model_api_data_type import ModelApiDataType
from foundry.models.model_api_type import ModelApiMapType
from foundry.models.model_api_type import ModelApiStructField
from foundry.models.model_api_type import ModelApiStructType
from foundry.models.model_api_type import ModelApiType
from foundry.models.model_api_type import ModelApiUnionType
from foundry.models.model_property import ModelProperty
from foundry.models.modify_object_rule import ModifyObjectRule
from foundry.models.multi_line_string import MultiLineString
from foundry.models.multi_point import MultiPoint
from foundry.models.multi_polygon import MultiPolygon
from foundry.models.multiple_group_by_on_field_not_supported import (
    MultipleGroupByOnFieldNotSupported,
)
from foundry.models.multiple_group_by_on_field_not_supported_parameters import (
    MultipleGroupByOnFieldNotSupportedParameters,
)
from foundry.models.multiple_property_values_not_supported import MultiplePropertyValuesNotSupported
from foundry.models.multiple_property_values_not_supported_parameters import (
    MultiplePropertyValuesNotSupportedParameters,
)
from foundry.models.null_type import NullType
from foundry.models.object_already_exists import ObjectAlreadyExists
from foundry.models.object_changed import ObjectChanged
from foundry.models.object_not_found import ObjectNotFound
from foundry.models.object_not_found_parameters import ObjectNotFoundParameters
from foundry.models.object_property_type import ObjectPropertyType
from foundry.models.object_type import ObjectType
from foundry.models.object_type_not_found import ObjectTypeNotFound
from foundry.models.object_type_not_found_parameters import ObjectTypeNotFoundParameters
from foundry.models.object_type_not_synced import ObjectTypeNotSynced
from foundry.models.object_type_not_synced_parameters import ObjectTypeNotSyncedParameters
from foundry.models.object_type_v2 import ObjectTypeV2
from foundry.models.object_type_visibility import ObjectTypeVisibility
from foundry.models.object_type_with_link import ObjectTypeWithLink
from foundry.models.objects_exceeded_limit import ObjectsExceededLimit
from foundry.models.ontology import Ontology
from foundry.models.ontology_data_type import OntologyArrayType
from foundry.models.ontology_data_type import OntologyDataType
from foundry.models.ontology_edits_exceeded_limit import OntologyEditsExceededLimit
from foundry.models.ontology_edits_exceeded_limit_parameters import (
    OntologyEditsExceededLimitParameters,
)
from foundry.models.ontology_full_metadata import OntologyFullMetadata
from foundry.models.ontology_data_type import OntologyMapType
from foundry.models.ontology_not_found import OntologyNotFound
from foundry.models.ontology_not_found_parameters import OntologyNotFoundParameters
from foundry.models.object_property_type import OntologyObjectArrayType
from foundry.models.ontology_object_set_type import OntologyObjectSetType
from foundry.models.ontology_object_type import OntologyObjectType
from foundry.models.ontology_data_type import OntologySetType
from foundry.models.ontology_data_type import OntologyStructField
from foundry.models.ontology_data_type import OntologyStructType
from foundry.models.ontology_syncing import OntologySyncing
from foundry.models.ontology_v2 import OntologyV2
from foundry.models.open_transaction_already_exists import OpenTransactionAlreadyExists
from foundry.models.operation_not_found import OperationNotFound
from foundry.models.operation_not_found_parameters import OperationNotFoundParameters
from foundry.models.parameter import Parameter
from foundry.models.parameter_object_not_found import ParameterObjectNotFound
from foundry.models.parameter_object_not_found_parameters import ParameterObjectNotFoundParameters
from foundry.models.parameter_object_set_rid_not_found import ParameterObjectSetRidNotFound
from foundry.models.parameter_object_set_rid_not_found_parameters import (
    ParameterObjectSetRidNotFoundParameters,
)
from foundry.models.parameter_type_not_supported import ParameterTypeNotSupported
from foundry.models.parameter_type_not_supported_parameters import (
    ParameterTypeNotSupportedParameters,
)
from foundry.models.parameters_not_found import ParametersNotFound
from foundry.models.parameters_not_found_parameters import ParametersNotFoundParameters
from foundry.models.parent_attachment_permission_denied import ParentAttachmentPermissionDenied
from foundry.models.polygon import Polygon
from foundry.models.properties_not_filterable import PropertiesNotFilterable
from foundry.models.properties_not_found import PropertiesNotFound
from foundry.models.properties_not_found_parameters import PropertiesNotFoundParameters
from foundry.models.properties_not_searchable import PropertiesNotSearchable
from foundry.models.properties_not_searchable_parameters import PropertiesNotSearchableParameters
from foundry.models.properties_not_sortable import PropertiesNotSortable
from foundry.models.property_api_name_not_found import PropertyApiNameNotFound
from foundry.models.property_api_name_not_found_parameters import PropertyApiNameNotFoundParameters
from foundry.models.property_base_type_not_supported import PropertyBaseTypeNotSupported
from foundry.models.property_filters_not_supported import PropertyFiltersNotSupported
from foundry.models.property_types_search_not_supported import PropertyTypesSearchNotSupported
from foundry.models.property_types_search_not_supported_parameters import (
    PropertyTypesSearchNotSupportedParameters,
)
from foundry.models.property_v2 import PropertyV2
from foundry.models.put_schema_permission_denied import PutSchemaPermissionDenied
from foundry.models.query_aggregation_key_type import QueryAggregationKeyType
from foundry.models.query_aggregation_range_sub_type import QueryAggregationRangeSubType
from foundry.models.query_aggregation_range_type import QueryAggregationRangeType
from foundry.models.query_aggregation_value_type import QueryAggregationValueType
from foundry.models.query_data_type import QueryArrayType
from foundry.models.query_data_type import QueryDataType
from foundry.models.query_encountered_user_facing_error import QueryEncounteredUserFacingError
from foundry.models.query_memory_exceeded_limit import QueryMemoryExceededLimit
from foundry.models.query_not_found import QueryNotFound
from foundry.models.query_not_found_parameters import QueryNotFoundParameters
from foundry.models.query_parameter_v2 import QueryParameterV2
from foundry.models.query_data_type import QuerySetType
from foundry.models.query_data_type import QueryStructField
from foundry.models.query_data_type import QueryStructType
from foundry.models.query_time_exceeded_limit import QueryTimeExceededLimit
from foundry.models.query_type import QueryType
from foundry.models.query_type_v2 import QueryTypeV2
from foundry.models.query_data_type import QueryUnionType
from foundry.models.read_table_permission_denied import ReadTablePermissionDenied
from foundry.models.release_status import ReleaseStatus
from foundry.models.resource_name_already_exists import ResourceNameAlreadyExists
from foundry.models.resource_name_already_exists_parameters import (
    ResourceNameAlreadyExistsParameters,
)
from foundry.models.return_edits_mode import ReturnEditsMode
from foundry.models.schema_not_found import SchemaNotFound
from foundry.models.short_type import ShortType
from foundry.models.string_type import StringType
from foundry.models.table_export_format import TableExportFormat
from foundry.models.three_dimensional_aggregation import ThreeDimensionalAggregation
from foundry.models.time_series_item_type import TimeSeriesItemType
from foundry.models.timeseries_type import TimeseriesType
from foundry.models.timestamp_type import TimestampType
from foundry.models.transaction import Transaction
from foundry.models.transaction_not_committed import TransactionNotCommitted
from foundry.models.transaction_not_committed_parameters import TransactionNotCommittedParameters
from foundry.models.transaction_not_found import TransactionNotFound
from foundry.models.transaction_not_open import TransactionNotOpen
from foundry.models.transaction_status import TransactionStatus
from foundry.models.transaction_type import TransactionType
from foundry.models.two_dimensional_aggregation import TwoDimensionalAggregation
from foundry.models.unknown_distance_unit import UnknownDistanceUnit
from foundry.models.unknown_distance_unit_parameters import UnknownDistanceUnitParameters
from foundry.models.unknown_parameter import UnknownParameter
from foundry.models.unknown_parameter_parameters import UnknownParameterParameters
from foundry.models.unsupported_object_set import UnsupportedObjectSet
from foundry.models.unsupported_type import UnsupportedType
from foundry.models.upload_file_permission_denied import UploadFilePermissionDenied
from foundry.models.view_object_permission_denied import ViewObjectPermissionDenied
