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


from foundry.v2.connectivity.errors._additional_secrets_must_be_specified_as_plaintext_value_map import (
    AdditionalSecretsMustBeSpecifiedAsPlaintextValueMap,
)  # NOQA
from foundry.v2.connectivity.errors._changing_branch_name_not_supported_for_imports import (
    ChangingBranchNameNotSupportedForImports,
)  # NOQA
from foundry.v2.connectivity.errors._changing_output_dataset_not_supported_for_imports import (
    ChangingOutputDatasetNotSupportedForImports,
)  # NOQA
from foundry.v2.connectivity.errors._connection_details_not_determined import (
    ConnectionDetailsNotDetermined,
)  # NOQA
from foundry.v2.connectivity.errors._connection_not_found import ConnectionNotFound
from foundry.v2.connectivity.errors._connection_type_not_supported import (
    ConnectionTypeNotSupported,
)  # NOQA
from foundry.v2.connectivity.errors._create_connection_permission_denied import (
    CreateConnectionPermissionDenied,
)  # NOQA
from foundry.v2.connectivity.errors._create_file_import_permission_denied import (
    CreateFileImportPermissionDenied,
)  # NOQA
from foundry.v2.connectivity.errors._create_table_import_permission_denied import (
    CreateTableImportPermissionDenied,
)  # NOQA
from foundry.v2.connectivity.errors._delete_file_import_permission_denied import (
    DeleteFileImportPermissionDenied,
)  # NOQA
from foundry.v2.connectivity.errors._delete_table_import_permission_denied import (
    DeleteTableImportPermissionDenied,
)  # NOQA
from foundry.v2.connectivity.errors._domain_must_use_https_with_authentication import (
    DomainMustUseHttpsWithAuthentication,
)  # NOQA
from foundry.v2.connectivity.errors._encrypted_property_must_be_specified_as_plaintext_value import (
    EncryptedPropertyMustBeSpecifiedAsPlaintextValue,
)  # NOQA
from foundry.v2.connectivity.errors._execute_file_import_permission_denied import (
    ExecuteFileImportPermissionDenied,
)  # NOQA
from foundry.v2.connectivity.errors._execute_table_import_permission_denied import (
    ExecuteTableImportPermissionDenied,
)  # NOQA
from foundry.v2.connectivity.errors._file_at_least_count_filter_invalid_min_count import (
    FileAtLeastCountFilterInvalidMinCount,
)  # NOQA
from foundry.v2.connectivity.errors._file_import_custom_filter_cannot_be_used_to_create_or_update_file_imports import (
    FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports,
)  # NOQA
from foundry.v2.connectivity.errors._file_import_not_found import FileImportNotFound
from foundry.v2.connectivity.errors._file_import_not_supported_for_connection import (
    FileImportNotSupportedForConnection,
)  # NOQA
from foundry.v2.connectivity.errors._file_size_filter_greater_than_cannot_be_negative import (
    FileSizeFilterGreaterThanCannotBeNegative,
)  # NOQA
from foundry.v2.connectivity.errors._file_size_filter_invalid_greater_than_and_less_than_range import (
    FileSizeFilterInvalidGreaterThanAndLessThanRange,
)  # NOQA
from foundry.v2.connectivity.errors._file_size_filter_less_than_must_be_one_byte_or_larger import (
    FileSizeFilterLessThanMustBeOneByteOrLarger,
)  # NOQA
from foundry.v2.connectivity.errors._file_size_filter_missing_greater_than_and_less_than import (
    FileSizeFilterMissingGreaterThanAndLessThan,
)  # NOQA
from foundry.v2.connectivity.errors._files_count_limit_filter_invalid_limit import (
    FilesCountLimitFilterInvalidLimit,
)  # NOQA
from foundry.v2.connectivity.errors._get_configuration_permission_denied import (
    GetConfigurationPermissionDenied,
)  # NOQA
from foundry.v2.connectivity.errors._parent_folder_not_found_for_connection import (
    ParentFolderNotFoundForConnection,
)  # NOQA
from foundry.v2.connectivity.errors._property_cannot_be_blank import PropertyCannotBeBlank  # NOQA
from foundry.v2.connectivity.errors._property_cannot_be_empty import PropertyCannotBeEmpty  # NOQA
from foundry.v2.connectivity.errors._replace_file_import_permission_denied import (
    ReplaceFileImportPermissionDenied,
)  # NOQA
from foundry.v2.connectivity.errors._secret_names_do_not_exist import SecretNamesDoNotExist  # NOQA
from foundry.v2.connectivity.errors._table_import_not_found import TableImportNotFound
from foundry.v2.connectivity.errors._table_import_not_supported_for_connection import (
    TableImportNotSupportedForConnection,
)  # NOQA
from foundry.v2.connectivity.errors._table_import_type_not_supported import (
    TableImportTypeNotSupported,
)  # NOQA
from foundry.v2.connectivity.errors._update_secrets_for_connection_permission_denied import (
    UpdateSecretsForConnectionPermissionDenied,
)  # NOQA

__all__ = [
    "AdditionalSecretsMustBeSpecifiedAsPlaintextValueMap",
    "ChangingBranchNameNotSupportedForImports",
    "ChangingOutputDatasetNotSupportedForImports",
    "ConnectionDetailsNotDetermined",
    "ConnectionNotFound",
    "ConnectionTypeNotSupported",
    "CreateConnectionPermissionDenied",
    "CreateFileImportPermissionDenied",
    "CreateTableImportPermissionDenied",
    "DeleteFileImportPermissionDenied",
    "DeleteTableImportPermissionDenied",
    "DomainMustUseHttpsWithAuthentication",
    "EncryptedPropertyMustBeSpecifiedAsPlaintextValue",
    "ExecuteFileImportPermissionDenied",
    "ExecuteTableImportPermissionDenied",
    "FileAtLeastCountFilterInvalidMinCount",
    "FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports",
    "FileImportNotFound",
    "FileImportNotSupportedForConnection",
    "FileSizeFilterGreaterThanCannotBeNegative",
    "FileSizeFilterInvalidGreaterThanAndLessThanRange",
    "FileSizeFilterLessThanMustBeOneByteOrLarger",
    "FileSizeFilterMissingGreaterThanAndLessThan",
    "FilesCountLimitFilterInvalidLimit",
    "GetConfigurationPermissionDenied",
    "ParentFolderNotFoundForConnection",
    "PropertyCannotBeBlank",
    "PropertyCannotBeEmpty",
    "ReplaceFileImportPermissionDenied",
    "SecretNamesDoNotExist",
    "TableImportNotFound",
    "TableImportNotSupportedForConnection",
    "TableImportTypeNotSupported",
    "UpdateSecretsForConnectionPermissionDenied",
]
