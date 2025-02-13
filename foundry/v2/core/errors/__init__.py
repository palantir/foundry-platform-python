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


from foundry.v2.core.errors._api_feature_preview_usage_only import (
    ApiFeaturePreviewUsageOnly,
)  # NOQA
from foundry.v2.core.errors._api_usage_denied import ApiUsageDenied
from foundry.v2.core.errors._batch_request_size_exceeded_limit import (
    BatchRequestSizeExceededLimit,
)  # NOQA
from foundry.v2.core.errors._folder_not_found import FolderNotFound
from foundry.v2.core.errors._invalid_and_filter import InvalidAndFilter
from foundry.v2.core.errors._invalid_change_data_capture_configuration import (
    InvalidChangeDataCaptureConfiguration,
)  # NOQA
from foundry.v2.core.errors._invalid_field_schema import InvalidFieldSchema
from foundry.v2.core.errors._invalid_filter_value import InvalidFilterValue
from foundry.v2.core.errors._invalid_or_filter import InvalidOrFilter
from foundry.v2.core.errors._invalid_page_size import InvalidPageSize
from foundry.v2.core.errors._invalid_page_token import InvalidPageToken
from foundry.v2.core.errors._invalid_parameter_combination import (
    InvalidParameterCombination,
)  # NOQA
from foundry.v2.core.errors._invalid_schema import InvalidSchema
from foundry.v2.core.errors._invalid_time_zone import InvalidTimeZone
from foundry.v2.core.errors._missing_batch_request import MissingBatchRequest
from foundry.v2.core.errors._missing_post_body import MissingPostBody
from foundry.v2.core.errors._resource_name_already_exists import ResourceNameAlreadyExists  # NOQA
from foundry.v2.core.errors._schema_is_not_stream_schema import SchemaIsNotStreamSchema
from foundry.v2.core.errors._unknown_distance_unit import UnknownDistanceUnit

__all__ = [
    "InvalidPageToken",
    "FolderNotFound",
    "InvalidFieldSchema",
    "InvalidFilterValue",
    "InvalidTimeZone",
    "InvalidSchema",
    "ApiFeaturePreviewUsageOnly",
    "BatchRequestSizeExceededLimit",
    "InvalidChangeDataCaptureConfiguration",
    "SchemaIsNotStreamSchema",
    "InvalidOrFilter",
    "InvalidParameterCombination",
    "InvalidAndFilter",
    "ApiUsageDenied",
    "UnknownDistanceUnit",
    "ResourceNameAlreadyExists",
    "MissingBatchRequest",
    "InvalidPageSize",
    "MissingPostBody",
]
