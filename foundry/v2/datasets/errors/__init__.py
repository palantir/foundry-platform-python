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


from foundry.v2.datasets.errors._abort_transaction_permission_denied import (
    AbortTransactionPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._branch_already_exists import BranchAlreadyExists
from foundry.v2.datasets.errors._branch_not_found import BranchNotFound
from foundry.v2.datasets.errors._build_transaction_permission_denied import (
    BuildTransactionPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._column_types_not_supported import ColumnTypesNotSupported  # NOQA
from foundry.v2.datasets.errors._commit_transaction_permission_denied import (
    CommitTransactionPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._create_branch_permission_denied import (
    CreateBranchPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._create_dataset_permission_denied import (
    CreateDatasetPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._create_transaction_permission_denied import (
    CreateTransactionPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._dataset_not_found import DatasetNotFound
from foundry.v2.datasets.errors._dataset_read_not_supported import DatasetReadNotSupported  # NOQA
from foundry.v2.datasets.errors._delete_branch_permission_denied import (
    DeleteBranchPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._delete_file_permission_denied import (
    DeleteFilePermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._delete_schema_permission_denied import (
    DeleteSchemaPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._file_already_exists import FileAlreadyExists
from foundry.v2.datasets.errors._file_not_found import FileNotFound
from foundry.v2.datasets.errors._file_not_found_on_branch import FileNotFoundOnBranch
from foundry.v2.datasets.errors._file_not_found_on_transaction_range import (
    FileNotFoundOnTransactionRange,
)  # NOQA
from foundry.v2.datasets.errors._get_file_content_permission_denied import (
    GetFileContentPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._invalid_branch_name import InvalidBranchName
from foundry.v2.datasets.errors._invalid_transaction_type import InvalidTransactionType
from foundry.v2.datasets.errors._job_transaction_permission_denied import (
    JobTransactionPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._open_transaction_already_exists import (
    OpenTransactionAlreadyExists,
)  # NOQA
from foundry.v2.datasets.errors._put_schema_permission_denied import (
    PutSchemaPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._read_table_dataset_permission_denied import (
    ReadTableDatasetPermissionDenied,
)  # NOQA
from foundry.v2.datasets.errors._read_table_error import ReadTableError
from foundry.v2.datasets.errors._read_table_row_limit_exceeded import (
    ReadTableRowLimitExceeded,
)  # NOQA
from foundry.v2.datasets.errors._read_table_timeout import ReadTableTimeout
from foundry.v2.datasets.errors._schema_not_found import SchemaNotFound
from foundry.v2.datasets.errors._transaction_not_committed import TransactionNotCommitted  # NOQA
from foundry.v2.datasets.errors._transaction_not_found import TransactionNotFound
from foundry.v2.datasets.errors._transaction_not_open import TransactionNotOpen
from foundry.v2.datasets.errors._upload_file_permission_denied import (
    UploadFilePermissionDenied,
)  # NOQA

__all__ = [
    "AbortTransactionPermissionDenied",
    "BranchAlreadyExists",
    "BranchNotFound",
    "BuildTransactionPermissionDenied",
    "ColumnTypesNotSupported",
    "CommitTransactionPermissionDenied",
    "CreateBranchPermissionDenied",
    "CreateDatasetPermissionDenied",
    "CreateTransactionPermissionDenied",
    "DatasetNotFound",
    "DatasetReadNotSupported",
    "DeleteBranchPermissionDenied",
    "DeleteFilePermissionDenied",
    "DeleteSchemaPermissionDenied",
    "FileAlreadyExists",
    "FileNotFound",
    "FileNotFoundOnBranch",
    "FileNotFoundOnTransactionRange",
    "GetFileContentPermissionDenied",
    "InvalidBranchName",
    "InvalidTransactionType",
    "JobTransactionPermissionDenied",
    "OpenTransactionAlreadyExists",
    "PutSchemaPermissionDenied",
    "ReadTableDatasetPermissionDenied",
    "ReadTableError",
    "ReadTableRowLimitExceeded",
    "ReadTableTimeout",
    "SchemaNotFound",
    "TransactionNotCommitted",
    "TransactionNotFound",
    "TransactionNotOpen",
    "UploadFilePermissionDenied",
]
