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

import warnings
from functools import cached_property
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.connectivity import errors as connectivity_errors
from foundry.v2.connectivity.models._connection_rid import ConnectionRid
from foundry.v2.connectivity.models._file_import import FileImport
from foundry.v2.connectivity.models._file_import_display_name import FileImportDisplayName  # NOQA
from foundry.v2.connectivity.models._file_import_filter import FileImportFilter
from foundry.v2.connectivity.models._file_import_filter_dict import FileImportFilterDict
from foundry.v2.connectivity.models._file_import_mode import FileImportMode
from foundry.v2.connectivity.models._file_import_rid import FileImportRid
from foundry.v2.connectivity.models._list_file_imports_response import (
    ListFileImportsResponse,
)  # NOQA
from foundry.v2.core.models._build_rid import BuildRid
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid


class FileImportClient:
    """
    The API client for the FileImport Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _FileImportClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _FileImportClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        connection_rid: ConnectionRid,
        *,
        dataset_rid: DatasetRid,
        display_name: FileImportDisplayName,
        file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]],
        import_mode: FileImportMode,
        branch_name: Optional[BranchName] = None,
        preview: Optional[PreviewMode] = None,
        subfolder: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> FileImport:
        """
        Creates a new FileImport.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param dataset_rid: The RID of the output dataset.
        :type dataset_rid: DatasetRid
        :param display_name:
        :type display_name: FileImportDisplayName
        :param file_import_filters: Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)
        :type file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]]
        :param import_mode:
        :type import_mode: FileImportMode
        :param branch_name: The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: FileImport

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises CreateFileImportPermissionDenied: Could not create the FileImport.
        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileImportNotSupportedForConnection: The specified connection does not support file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "datasetRid": dataset_rid,
                    "importMode": import_mode,
                    "displayName": display_name,
                    "branchName": branch_name,
                    "subfolder": subfolder,
                    "fileImportFilters": file_import_filters,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": DatasetRid,
                        "importMode": FileImportMode,
                        "displayName": FileImportDisplayName,
                        "branchName": Optional[BranchName],
                        "subfolder": Optional[str],
                        "fileImportFilters": List[Union[FileImportFilter, FileImportFilterDict]],
                    },
                ),
                response_type=FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "CreateFileImportPermissionDenied": connectivity_errors.CreateFileImportPermissionDenied,
                    "FileAtLeastCountFilterInvalidMinCount": connectivity_errors.FileAtLeastCountFilterInvalidMinCount,
                    "FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports": connectivity_errors.FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports,
                    "FileImportNotSupportedForConnection": connectivity_errors.FileImportNotSupportedForConnection,
                    "FileSizeFilterGreaterThanCannotBeNegative": connectivity_errors.FileSizeFilterGreaterThanCannotBeNegative,
                    "FileSizeFilterInvalidGreaterThanAndLessThanRange": connectivity_errors.FileSizeFilterInvalidGreaterThanAndLessThanRange,
                    "FileSizeFilterLessThanMustBeOneByteOrLarger": connectivity_errors.FileSizeFilterLessThanMustBeOneByteOrLarger,
                    "FileSizeFilterMissingGreaterThanAndLessThan": connectivity_errors.FileSizeFilterMissingGreaterThanAndLessThan,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Delete the FileImport with the specified RID.
        Deleting the file import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteFileImportPermissionDenied: Could not delete the FileImport.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteFileImportPermissionDenied": connectivity_errors.DeleteFileImportPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> BuildRid:
        """
        Executes the FileImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: BuildRid

        :raises ExecuteFileImportPermissionDenied: Could not execute the FileImport.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}/execute",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteFileImportPermissionDenied": connectivity_errors.ExecuteFileImportPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> FileImport:
        """
        Get the FileImport with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: FileImport

        :raises FileImportNotFound: The given FileImport could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "FileImportNotFound": connectivity_errors.FileImportNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        connection_rid: ConnectionRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[FileImport]:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[FileImport]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        connection_rid: ConnectionRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListFileImportsResponse:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListFileImportsResponse
        """

        warnings.warn(
            "The client.connectivity.FileImport.page(...) method has been deprecated. Please use client.connectivity.FileImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        dataset_rid: DatasetRid,
        display_name: FileImportDisplayName,
        file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]],
        import_mode: FileImportMode,
        branch_name: Optional[BranchName] = None,
        preview: Optional[PreviewMode] = None,
        subfolder: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> FileImport:
        """
        Replace the FileImport with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param dataset_rid: The RID of the output dataset.
        :type dataset_rid: DatasetRid
        :param display_name:
        :type display_name: FileImportDisplayName
        :param file_import_filters: Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)
        :type file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]]
        :param import_mode:
        :type import_mode: FileImportMode
        :param branch_name: The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: FileImport

        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        :raises ReplaceFileImportPermissionDenied: Could not replace the FileImport.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "datasetRid": dataset_rid,
                    "importMode": import_mode,
                    "displayName": display_name,
                    "branchName": branch_name,
                    "subfolder": subfolder,
                    "fileImportFilters": file_import_filters,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": DatasetRid,
                        "importMode": FileImportMode,
                        "displayName": FileImportDisplayName,
                        "branchName": Optional[BranchName],
                        "subfolder": Optional[str],
                        "fileImportFilters": List[Union[FileImportFilter, FileImportFilterDict]],
                    },
                ),
                response_type=FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "FileAtLeastCountFilterInvalidMinCount": connectivity_errors.FileAtLeastCountFilterInvalidMinCount,
                    "FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports": connectivity_errors.FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports,
                    "FileSizeFilterGreaterThanCannotBeNegative": connectivity_errors.FileSizeFilterGreaterThanCannotBeNegative,
                    "FileSizeFilterInvalidGreaterThanAndLessThanRange": connectivity_errors.FileSizeFilterInvalidGreaterThanAndLessThanRange,
                    "FileSizeFilterLessThanMustBeOneByteOrLarger": connectivity_errors.FileSizeFilterLessThanMustBeOneByteOrLarger,
                    "FileSizeFilterMissingGreaterThanAndLessThan": connectivity_errors.FileSizeFilterMissingGreaterThanAndLessThan,
                    "ReplaceFileImportPermissionDenied": connectivity_errors.ReplaceFileImportPermissionDenied,
                },
            ),
        ).decode()


class _FileImportClientRaw:
    """
    The API client for the FileImport Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        connection_rid: ConnectionRid,
        *,
        dataset_rid: DatasetRid,
        display_name: FileImportDisplayName,
        file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]],
        import_mode: FileImportMode,
        branch_name: Optional[BranchName] = None,
        preview: Optional[PreviewMode] = None,
        subfolder: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[FileImport]:
        """
        Creates a new FileImport.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param dataset_rid: The RID of the output dataset.
        :type dataset_rid: DatasetRid
        :param display_name:
        :type display_name: FileImportDisplayName
        :param file_import_filters: Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)
        :type file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]]
        :param import_mode:
        :type import_mode: FileImportMode
        :param branch_name: The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[FileImport]

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises CreateFileImportPermissionDenied: Could not create the FileImport.
        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileImportNotSupportedForConnection: The specified connection does not support file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "datasetRid": dataset_rid,
                    "importMode": import_mode,
                    "displayName": display_name,
                    "branchName": branch_name,
                    "subfolder": subfolder,
                    "fileImportFilters": file_import_filters,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": DatasetRid,
                        "importMode": FileImportMode,
                        "displayName": FileImportDisplayName,
                        "branchName": Optional[BranchName],
                        "subfolder": Optional[str],
                        "fileImportFilters": List[Union[FileImportFilter, FileImportFilterDict]],
                    },
                ),
                response_type=FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "CreateFileImportPermissionDenied": connectivity_errors.CreateFileImportPermissionDenied,
                    "FileAtLeastCountFilterInvalidMinCount": connectivity_errors.FileAtLeastCountFilterInvalidMinCount,
                    "FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports": connectivity_errors.FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports,
                    "FileImportNotSupportedForConnection": connectivity_errors.FileImportNotSupportedForConnection,
                    "FileSizeFilterGreaterThanCannotBeNegative": connectivity_errors.FileSizeFilterGreaterThanCannotBeNegative,
                    "FileSizeFilterInvalidGreaterThanAndLessThanRange": connectivity_errors.FileSizeFilterInvalidGreaterThanAndLessThanRange,
                    "FileSizeFilterLessThanMustBeOneByteOrLarger": connectivity_errors.FileSizeFilterLessThanMustBeOneByteOrLarger,
                    "FileSizeFilterMissingGreaterThanAndLessThan": connectivity_errors.FileSizeFilterMissingGreaterThanAndLessThan,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Delete the FileImport with the specified RID.
        Deleting the file import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises DeleteFileImportPermissionDenied: Could not delete the FileImport.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteFileImportPermissionDenied": connectivity_errors.DeleteFileImportPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[BuildRid]:
        """
        Executes the FileImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[BuildRid]

        :raises ExecuteFileImportPermissionDenied: Could not execute the FileImport.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}/execute",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteFileImportPermissionDenied": connectivity_errors.ExecuteFileImportPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[FileImport]:
        """
        Get the FileImport with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[FileImport]

        :raises FileImportNotFound: The given FileImport could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "FileImportNotFound": connectivity_errors.FileImportNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        connection_rid: ConnectionRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListFileImportsResponse]:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListFileImportsResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        connection_rid: ConnectionRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListFileImportsResponse]:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListFileImportsResponse]
        """

        warnings.warn(
            "The client.connectivity.FileImport.page(...) method has been deprecated. Please use client.connectivity.FileImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        dataset_rid: DatasetRid,
        display_name: FileImportDisplayName,
        file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]],
        import_mode: FileImportMode,
        branch_name: Optional[BranchName] = None,
        preview: Optional[PreviewMode] = None,
        subfolder: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[FileImport]:
        """
        Replace the FileImport with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param dataset_rid: The RID of the output dataset.
        :type dataset_rid: DatasetRid
        :param display_name:
        :type display_name: FileImportDisplayName
        :param file_import_filters: Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)
        :type file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]]
        :param import_mode:
        :type import_mode: FileImportMode
        :param branch_name: The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[FileImport]

        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        :raises ReplaceFileImportPermissionDenied: Could not replace the FileImport.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "datasetRid": dataset_rid,
                    "importMode": import_mode,
                    "displayName": display_name,
                    "branchName": branch_name,
                    "subfolder": subfolder,
                    "fileImportFilters": file_import_filters,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": DatasetRid,
                        "importMode": FileImportMode,
                        "displayName": FileImportDisplayName,
                        "branchName": Optional[BranchName],
                        "subfolder": Optional[str],
                        "fileImportFilters": List[Union[FileImportFilter, FileImportFilterDict]],
                    },
                ),
                response_type=FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "FileAtLeastCountFilterInvalidMinCount": connectivity_errors.FileAtLeastCountFilterInvalidMinCount,
                    "FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports": connectivity_errors.FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports,
                    "FileSizeFilterGreaterThanCannotBeNegative": connectivity_errors.FileSizeFilterGreaterThanCannotBeNegative,
                    "FileSizeFilterInvalidGreaterThanAndLessThanRange": connectivity_errors.FileSizeFilterInvalidGreaterThanAndLessThanRange,
                    "FileSizeFilterLessThanMustBeOneByteOrLarger": connectivity_errors.FileSizeFilterLessThanMustBeOneByteOrLarger,
                    "FileSizeFilterMissingGreaterThanAndLessThan": connectivity_errors.FileSizeFilterMissingGreaterThanAndLessThan,
                    "ReplaceFileImportPermissionDenied": connectivity_errors.ReplaceFileImportPermissionDenied,
                },
            ),
        )


class _FileImportClientStreaming:
    """
    The API client for the FileImport Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        connection_rid: ConnectionRid,
        *,
        dataset_rid: DatasetRid,
        display_name: FileImportDisplayName,
        file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]],
        import_mode: FileImportMode,
        branch_name: Optional[BranchName] = None,
        preview: Optional[PreviewMode] = None,
        subfolder: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[FileImport]:
        """
        Creates a new FileImport.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param dataset_rid: The RID of the output dataset.
        :type dataset_rid: DatasetRid
        :param display_name:
        :type display_name: FileImportDisplayName
        :param file_import_filters: Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)
        :type file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]]
        :param import_mode:
        :type import_mode: FileImportMode
        :param branch_name: The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[FileImport]

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises CreateFileImportPermissionDenied: Could not create the FileImport.
        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileImportNotSupportedForConnection: The specified connection does not support file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "datasetRid": dataset_rid,
                    "importMode": import_mode,
                    "displayName": display_name,
                    "branchName": branch_name,
                    "subfolder": subfolder,
                    "fileImportFilters": file_import_filters,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": DatasetRid,
                        "importMode": FileImportMode,
                        "displayName": FileImportDisplayName,
                        "branchName": Optional[BranchName],
                        "subfolder": Optional[str],
                        "fileImportFilters": List[Union[FileImportFilter, FileImportFilterDict]],
                    },
                ),
                response_type=FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "CreateFileImportPermissionDenied": connectivity_errors.CreateFileImportPermissionDenied,
                    "FileAtLeastCountFilterInvalidMinCount": connectivity_errors.FileAtLeastCountFilterInvalidMinCount,
                    "FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports": connectivity_errors.FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports,
                    "FileImportNotSupportedForConnection": connectivity_errors.FileImportNotSupportedForConnection,
                    "FileSizeFilterGreaterThanCannotBeNegative": connectivity_errors.FileSizeFilterGreaterThanCannotBeNegative,
                    "FileSizeFilterInvalidGreaterThanAndLessThanRange": connectivity_errors.FileSizeFilterInvalidGreaterThanAndLessThanRange,
                    "FileSizeFilterLessThanMustBeOneByteOrLarger": connectivity_errors.FileSizeFilterLessThanMustBeOneByteOrLarger,
                    "FileSizeFilterMissingGreaterThanAndLessThan": connectivity_errors.FileSizeFilterMissingGreaterThanAndLessThan,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Delete the FileImport with the specified RID.
        Deleting the file import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises DeleteFileImportPermissionDenied: Could not delete the FileImport.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteFileImportPermissionDenied": connectivity_errors.DeleteFileImportPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[BuildRid]:
        """
        Executes the FileImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[BuildRid]

        :raises ExecuteFileImportPermissionDenied: Could not execute the FileImport.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}/execute",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteFileImportPermissionDenied": connectivity_errors.ExecuteFileImportPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[FileImport]:
        """
        Get the FileImport with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[FileImport]

        :raises FileImportNotFound: The given FileImport could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "FileImportNotFound": connectivity_errors.FileImportNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        connection_rid: ConnectionRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListFileImportsResponse]:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListFileImportsResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        connection_rid: ConnectionRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListFileImportsResponse]:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListFileImportsResponse]
        """

        warnings.warn(
            "The client.connectivity.FileImport.page(...) method has been deprecated. Please use client.connectivity.FileImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        connection_rid: ConnectionRid,
        file_import_rid: FileImportRid,
        *,
        dataset_rid: DatasetRid,
        display_name: FileImportDisplayName,
        file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]],
        import_mode: FileImportMode,
        branch_name: Optional[BranchName] = None,
        preview: Optional[PreviewMode] = None,
        subfolder: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[FileImport]:
        """
        Replace the FileImport with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param dataset_rid: The RID of the output dataset.
        :type dataset_rid: DatasetRid
        :param display_name:
        :type display_name: FileImportDisplayName
        :param file_import_filters: Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)
        :type file_import_filters: List[Union[FileImportFilter, FileImportFilterDict]]
        :param import_mode:
        :type import_mode: FileImportMode
        :param branch_name: The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[FileImport]

        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        :raises ReplaceFileImportPermissionDenied: Could not replace the FileImport.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "fileImportRid": file_import_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "datasetRid": dataset_rid,
                    "importMode": import_mode,
                    "displayName": display_name,
                    "branchName": branch_name,
                    "subfolder": subfolder,
                    "fileImportFilters": file_import_filters,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": DatasetRid,
                        "importMode": FileImportMode,
                        "displayName": FileImportDisplayName,
                        "branchName": Optional[BranchName],
                        "subfolder": Optional[str],
                        "fileImportFilters": List[Union[FileImportFilter, FileImportFilterDict]],
                    },
                ),
                response_type=FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "FileAtLeastCountFilterInvalidMinCount": connectivity_errors.FileAtLeastCountFilterInvalidMinCount,
                    "FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports": connectivity_errors.FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports,
                    "FileSizeFilterGreaterThanCannotBeNegative": connectivity_errors.FileSizeFilterGreaterThanCannotBeNegative,
                    "FileSizeFilterInvalidGreaterThanAndLessThanRange": connectivity_errors.FileSizeFilterInvalidGreaterThanAndLessThanRange,
                    "FileSizeFilterLessThanMustBeOneByteOrLarger": connectivity_errors.FileSizeFilterLessThanMustBeOneByteOrLarger,
                    "FileSizeFilterMissingGreaterThanAndLessThan": connectivity_errors.FileSizeFilterMissingGreaterThanAndLessThan,
                    "ReplaceFileImportPermissionDenied": connectivity_errors.ReplaceFileImportPermissionDenied,
                },
            ),
        )
