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

from foundry_sdk import _errors as errors
from foundry_sdk.v2.connectivity import models as connectivity_models
from foundry_sdk.v2.core import models as core_models


class AdditionalSecretsMustBeSpecifiedAsPlaintextValueMapParameters(typing_extensions.TypedDict):
    """The additional secrets must be specified as a plaintext value map."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class AdditionalSecretsMustBeSpecifiedAsPlaintextValueMap(errors.BadRequestError):
    name: typing.Literal["AdditionalSecretsMustBeSpecifiedAsPlaintextValueMap"]
    parameters: AdditionalSecretsMustBeSpecifiedAsPlaintextValueMapParameters
    error_instance_id: str


class ConnectionDetailsNotDeterminedParameters(typing_extensions.TypedDict):
    """Details of the connection (such as which types of import it supports) could not be determined."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid
    connectionType: str


@dataclass
class ConnectionDetailsNotDetermined(errors.InternalServerError):
    name: typing.Literal["ConnectionDetailsNotDetermined"]
    parameters: ConnectionDetailsNotDeterminedParameters
    error_instance_id: str


class ConnectionNotFoundParameters(typing_extensions.TypedDict):
    """The given Connection could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid


@dataclass
class ConnectionNotFound(errors.NotFoundError):
    name: typing.Literal["ConnectionNotFound"]
    parameters: ConnectionNotFoundParameters
    error_instance_id: str


class ConnectionTypeNotSupportedParameters(typing_extensions.TypedDict):
    """The specified connection is not yet supported in the Platform API."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionType: str


@dataclass
class ConnectionTypeNotSupported(errors.BadRequestError):
    name: typing.Literal["ConnectionTypeNotSupported"]
    parameters: ConnectionTypeNotSupportedParameters
    error_instance_id: str


class CreateConnectionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the Connection."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class CreateConnectionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateConnectionPermissionDenied"]
    parameters: CreateConnectionPermissionDeniedParameters
    error_instance_id: str


class CreateFileImportPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the FileImport."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid


@dataclass
class CreateFileImportPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateFileImportPermissionDenied"]
    parameters: CreateFileImportPermissionDeniedParameters
    error_instance_id: str


class CreateTableImportPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not create the TableImport."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid


@dataclass
class CreateTableImportPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateTableImportPermissionDenied"]
    parameters: CreateTableImportPermissionDeniedParameters
    error_instance_id: str


class DeleteFileImportPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the FileImport."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fileImportRid: connectivity_models.FileImportRid
    connectionRid: connectivity_models.ConnectionRid


@dataclass
class DeleteFileImportPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteFileImportPermissionDenied"]
    parameters: DeleteFileImportPermissionDeniedParameters
    error_instance_id: str


class DeleteTableImportPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not delete the TableImport."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    tableImportRid: connectivity_models.TableImportRid
    connectionRid: connectivity_models.ConnectionRid


@dataclass
class DeleteTableImportPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DeleteTableImportPermissionDenied"]
    parameters: DeleteTableImportPermissionDeniedParameters
    error_instance_id: str


class DomainMustUseHttpsWithAuthenticationParameters(typing_extensions.TypedDict):
    """The domain must use HTTPS if authentication is required."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class DomainMustUseHttpsWithAuthentication(errors.BadRequestError):
    name: typing.Literal["DomainMustUseHttpsWithAuthentication"]
    parameters: DomainMustUseHttpsWithAuthenticationParameters
    error_instance_id: str


class DriverContentMustBeUploadedAsJarParameters(typing_extensions.TypedDict):
    """The driver content must be provided as a jar."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    driverName: str


@dataclass
class DriverContentMustBeUploadedAsJar(errors.BadRequestError):
    name: typing.Literal["DriverContentMustBeUploadedAsJar"]
    parameters: DriverContentMustBeUploadedAsJarParameters
    error_instance_id: str


class DriverJarAlreadyExistsParameters(typing_extensions.TypedDict):
    """Duplicate jar with different versions already exists on connection."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    driverName: str
    connectionRid: connectivity_models.ConnectionRid


@dataclass
class DriverJarAlreadyExists(errors.ConflictError):
    name: typing.Literal["DriverJarAlreadyExists"]
    parameters: DriverJarAlreadyExistsParameters
    error_instance_id: str


class EncryptedPropertyMustBeSpecifiedAsPlaintextValueParameters(typing_extensions.TypedDict):
    """The encrypted property must be specified as a plaintext value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyName: str


@dataclass
class EncryptedPropertyMustBeSpecifiedAsPlaintextValue(errors.BadRequestError):
    name: typing.Literal["EncryptedPropertyMustBeSpecifiedAsPlaintextValue"]
    parameters: EncryptedPropertyMustBeSpecifiedAsPlaintextValueParameters
    error_instance_id: str


class ExecuteFileImportPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not execute the FileImport."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fileImportRid: connectivity_models.FileImportRid
    connectionRid: connectivity_models.ConnectionRid


@dataclass
class ExecuteFileImportPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ExecuteFileImportPermissionDenied"]
    parameters: ExecuteFileImportPermissionDeniedParameters
    error_instance_id: str


class ExecuteTableImportPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not execute the TableImport."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    tableImportRid: connectivity_models.TableImportRid
    connectionRid: connectivity_models.ConnectionRid


@dataclass
class ExecuteTableImportPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ExecuteTableImportPermissionDenied"]
    parameters: ExecuteTableImportPermissionDeniedParameters
    error_instance_id: str


class FileAtLeastCountFilterInvalidMinCountParameters(typing_extensions.TypedDict):
    """The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    minFilesCount: int


@dataclass
class FileAtLeastCountFilterInvalidMinCount(errors.BadRequestError):
    name: typing.Literal["FileAtLeastCountFilterInvalidMinCount"]
    parameters: FileAtLeastCountFilterInvalidMinCountParameters
    error_instance_id: str


class FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImportsParameters(
    typing_extensions.TypedDict
):
    """
    Custom file import filters can be fetched but cannot currently be used
    when creating or updating file imports.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    config: typing.Any


@dataclass
class FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports(errors.BadRequestError):
    name: typing.Literal["FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports"]
    parameters: FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImportsParameters
    error_instance_id: str


class FileImportNotFoundParameters(typing_extensions.TypedDict):
    """The given FileImport could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fileImportRid: connectivity_models.FileImportRid
    connectionRid: connectivity_models.ConnectionRid


@dataclass
class FileImportNotFound(errors.NotFoundError):
    name: typing.Literal["FileImportNotFound"]
    parameters: FileImportNotFoundParameters
    error_instance_id: str


class FileImportNotSupportedForConnectionParameters(typing_extensions.TypedDict):
    """The specified connection does not support file imports."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid


@dataclass
class FileImportNotSupportedForConnection(errors.BadRequestError):
    name: typing.Literal["FileImportNotSupportedForConnection"]
    parameters: FileImportNotSupportedForConnectionParameters
    error_instance_id: str


class FileSizeFilterGreaterThanCannotBeNegativeParameters(typing_extensions.TypedDict):
    """The `gt` property in the FileSizeFilter cannot be a negative number."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    gt: core_models.SizeBytes


@dataclass
class FileSizeFilterGreaterThanCannotBeNegative(errors.BadRequestError):
    name: typing.Literal["FileSizeFilterGreaterThanCannotBeNegative"]
    parameters: FileSizeFilterGreaterThanCannotBeNegativeParameters
    error_instance_id: str


class FileSizeFilterInvalidGreaterThanAndLessThanRangeParameters(typing_extensions.TypedDict):
    """
    The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever
    satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    gt: core_models.SizeBytes
    lt: core_models.SizeBytes


@dataclass
class FileSizeFilterInvalidGreaterThanAndLessThanRange(errors.BadRequestError):
    name: typing.Literal["FileSizeFilterInvalidGreaterThanAndLessThanRange"]
    parameters: FileSizeFilterInvalidGreaterThanAndLessThanRangeParameters
    error_instance_id: str


class FileSizeFilterLessThanMustBeOneByteOrLargerParameters(typing_extensions.TypedDict):
    """The `lt` property in the FileSizeFilter must be at least 1 byte."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    lt: core_models.SizeBytes


@dataclass
class FileSizeFilterLessThanMustBeOneByteOrLarger(errors.BadRequestError):
    name: typing.Literal["FileSizeFilterLessThanMustBeOneByteOrLarger"]
    parameters: FileSizeFilterLessThanMustBeOneByteOrLargerParameters
    error_instance_id: str


class FileSizeFilterMissingGreaterThanAndLessThanParameters(typing_extensions.TypedDict):
    """
    Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these
    properties must be present
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class FileSizeFilterMissingGreaterThanAndLessThan(errors.BadRequestError):
    name: typing.Literal["FileSizeFilterMissingGreaterThanAndLessThan"]
    parameters: FileSizeFilterMissingGreaterThanAndLessThanParameters
    error_instance_id: str


class FilesCountLimitFilterInvalidLimitParameters(typing_extensions.TypedDict):
    """The `filesCount` property in the FilesCountLimitFilter must be strictly greater than 0."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    filesCount: int


@dataclass
class FilesCountLimitFilterInvalidLimit(errors.BadRequestError):
    name: typing.Literal["FilesCountLimitFilterInvalidLimit"]
    parameters: FilesCountLimitFilterInvalidLimitParameters
    error_instance_id: str


class GetConfigurationPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not getConfiguration the Connection."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid


@dataclass
class GetConfigurationPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetConfigurationPermissionDenied"]
    parameters: GetConfigurationPermissionDeniedParameters
    error_instance_id: str


class HostNameCannotHaveProtocolOrPortParameters(typing_extensions.TypedDict):
    """The hostname should not include a protocol (e.g., https://) or port number (e.g., :443)."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    hostName: str


@dataclass
class HostNameCannotHaveProtocolOrPort(errors.BadRequestError):
    name: typing.Literal["HostNameCannotHaveProtocolOrPort"]
    parameters: HostNameCannotHaveProtocolOrPortParameters
    error_instance_id: str


class ParentFolderNotFoundForConnectionParameters(typing_extensions.TypedDict):
    """The parent folder for the specified connection could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid


@dataclass
class ParentFolderNotFoundForConnection(errors.NotFoundError):
    name: typing.Literal["ParentFolderNotFoundForConnection"]
    parameters: ParentFolderNotFoundForConnectionParameters
    error_instance_id: str


class PropertyCannotBeBlankParameters(typing_extensions.TypedDict):
    """The specified property cannot be blank."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyName: str


@dataclass
class PropertyCannotBeBlank(errors.BadRequestError):
    name: typing.Literal["PropertyCannotBeBlank"]
    parameters: PropertyCannotBeBlankParameters
    error_instance_id: str


class PropertyCannotBeEmptyParameters(typing_extensions.TypedDict):
    """The specified property cannot be empty."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyName: str


@dataclass
class PropertyCannotBeEmpty(errors.BadRequestError):
    name: typing.Literal["PropertyCannotBeEmpty"]
    parameters: PropertyCannotBeEmptyParameters
    error_instance_id: str


class ReplaceFileImportPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not replace the FileImport."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fileImportRid: connectivity_models.FileImportRid
    connectionRid: connectivity_models.ConnectionRid


@dataclass
class ReplaceFileImportPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReplaceFileImportPermissionDenied"]
    parameters: ReplaceFileImportPermissionDeniedParameters
    error_instance_id: str


class ReplaceTableImportPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not replace the TableImport."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    tableImportRid: connectivity_models.TableImportRid
    connectionRid: connectivity_models.ConnectionRid


@dataclass
class ReplaceTableImportPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["ReplaceTableImportPermissionDenied"]
    parameters: ReplaceTableImportPermissionDeniedParameters
    error_instance_id: str


class SecretNamesDoNotExistParameters(typing_extensions.TypedDict):
    """The secret names provided do not exist on the connection."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid
    secretNames: typing.List[connectivity_models.SecretName]


@dataclass
class SecretNamesDoNotExist(errors.BadRequestError):
    name: typing.Literal["SecretNamesDoNotExist"]
    parameters: SecretNamesDoNotExistParameters
    error_instance_id: str


class TableImportNotFoundParameters(typing_extensions.TypedDict):
    """The given TableImport could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    tableImportRid: connectivity_models.TableImportRid
    connectionRid: connectivity_models.ConnectionRid


@dataclass
class TableImportNotFound(errors.NotFoundError):
    name: typing.Literal["TableImportNotFound"]
    parameters: TableImportNotFoundParameters
    error_instance_id: str


class TableImportNotSupportedForConnectionParameters(typing_extensions.TypedDict):
    """The specified connection does not support creating or replacing a table import with the specified config."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid
    tableImportType: str


@dataclass
class TableImportNotSupportedForConnection(errors.BadRequestError):
    name: typing.Literal["TableImportNotSupportedForConnection"]
    parameters: TableImportNotSupportedForConnectionParameters
    error_instance_id: str


class TableImportTypeNotSupportedParameters(typing_extensions.TypedDict):
    """The specified table import type is not yet supported in the Platform API."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    tableImportType: str


@dataclass
class TableImportTypeNotSupported(errors.InternalServerError):
    name: typing.Literal["TableImportTypeNotSupported"]
    parameters: TableImportTypeNotSupportedParameters
    error_instance_id: str


class UpdateExportSettingsForConnectionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not updateExportSettings the Connection."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid


@dataclass
class UpdateExportSettingsForConnectionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["UpdateExportSettingsForConnectionPermissionDenied"]
    parameters: UpdateExportSettingsForConnectionPermissionDeniedParameters
    error_instance_id: str


class UpdateSecretsForConnectionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not update secrets for the Connection."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid


@dataclass
class UpdateSecretsForConnectionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["UpdateSecretsForConnectionPermissionDenied"]
    parameters: UpdateSecretsForConnectionPermissionDeniedParameters
    error_instance_id: str


class UploadCustomJdbcDriverNotSupportForConnectionParameters(typing_extensions.TypedDict):
    """Only JDBC connections support uploading custom JDBC drivers."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionType: str


@dataclass
class UploadCustomJdbcDriverNotSupportForConnection(errors.BadRequestError):
    name: typing.Literal["UploadCustomJdbcDriverNotSupportForConnection"]
    parameters: UploadCustomJdbcDriverNotSupportForConnectionParameters
    error_instance_id: str


class UploadCustomJdbcDriversConnectionPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not uploadCustomJdbcDrivers the Connection."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    connectionRid: connectivity_models.ConnectionRid


@dataclass
class UploadCustomJdbcDriversConnectionPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["UploadCustomJdbcDriversConnectionPermissionDenied"]
    parameters: UploadCustomJdbcDriversConnectionPermissionDeniedParameters
    error_instance_id: str


__all__ = [
    "AdditionalSecretsMustBeSpecifiedAsPlaintextValueMap",
    "ConnectionDetailsNotDetermined",
    "ConnectionNotFound",
    "ConnectionTypeNotSupported",
    "CreateConnectionPermissionDenied",
    "CreateFileImportPermissionDenied",
    "CreateTableImportPermissionDenied",
    "DeleteFileImportPermissionDenied",
    "DeleteTableImportPermissionDenied",
    "DomainMustUseHttpsWithAuthentication",
    "DriverContentMustBeUploadedAsJar",
    "DriverJarAlreadyExists",
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
    "HostNameCannotHaveProtocolOrPort",
    "ParentFolderNotFoundForConnection",
    "PropertyCannotBeBlank",
    "PropertyCannotBeEmpty",
    "ReplaceFileImportPermissionDenied",
    "ReplaceTableImportPermissionDenied",
    "SecretNamesDoNotExist",
    "TableImportNotFound",
    "TableImportNotSupportedForConnection",
    "TableImportTypeNotSupported",
    "UpdateExportSettingsForConnectionPermissionDenied",
    "UpdateSecretsForConnectionPermissionDenied",
    "UploadCustomJdbcDriverNotSupportForConnection",
    "UploadCustomJdbcDriversConnectionPermissionDenied",
]
