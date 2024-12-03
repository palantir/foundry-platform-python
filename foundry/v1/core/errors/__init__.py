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


from foundry.v1.core.errors._api_feature_preview_usage_only import (
    ApiFeaturePreviewUsageOnly,
)  # NOQA
from foundry.v1.core.errors._api_usage_denied import ApiUsageDenied
from foundry.v1.core.errors._folder_not_found import FolderNotFound
from foundry.v1.core.errors._invalid_page_size import InvalidPageSize
from foundry.v1.core.errors._invalid_page_token import InvalidPageToken
from foundry.v1.core.errors._invalid_parameter_combination import (
    InvalidParameterCombination,
)  # NOQA
from foundry.v1.core.errors._missing_post_body import MissingPostBody
from foundry.v1.core.errors._resource_name_already_exists import ResourceNameAlreadyExists  # NOQA
from foundry.v1.core.errors._unknown_distance_unit import UnknownDistanceUnit

__all__ = [
    "ResourceNameAlreadyExists",
    "ApiFeaturePreviewUsageOnly",
    "InvalidPageSize",
    "FolderNotFound",
    "InvalidPageToken",
    "UnknownDistanceUnit",
    "MissingPostBody",
    "InvalidParameterCombination",
    "ApiUsageDenied",
]
