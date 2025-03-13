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
import warnings

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.connectivity import errors as connectivity_errors
from foundry.v2.connectivity import models as connectivity_models
from foundry.v2.core import models as core_models
from foundry.v2.datasets import errors as datasets_errors
from foundry.v2.datasets import models as datasets_models


class FileImportClient:
    """
    The API client for the FileImport Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _FileImportClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _FileImportClientRaw(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        dataset_rid: datasets_models.DatasetRid,
        display_name: connectivity_models.FileImportDisplayName,
        file_import_filters: typing.List[
            typing.Union[
                connectivity_models.FileImportFilter, connectivity_models.FileImportFilterDict
            ]
        ],
        import_mode: connectivity_models.FileImportMode,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        subfolder: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> connectivity_models.FileImport:
        """
        Creates a new FileImport.
        :param connection_rid:
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
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: connectivity_models.FileImport

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises ConnectionNotFound: The given Connection could not be found.
        :raises CreateFileImportPermissionDenied: Could not create the FileImport.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileImportNotSupportedForConnection: The specified connection does not support file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": datasets_models.DatasetRid,
                        "importMode": connectivity_models.FileImportMode,
                        "displayName": connectivity_models.FileImportDisplayName,
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "subfolder": typing.Optional[str],
                        "fileImportFilters": typing.List[
                            typing.Union[
                                connectivity_models.FileImportFilter,
                                connectivity_models.FileImportFilterDict,
                            ]
                        ],
                    },
                ),
                response_type=connectivity_models.FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "CreateFileImportPermissionDenied": connectivity_errors.CreateFileImportPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Delete the FileImport with the specified RID.
        Deleting the file import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
        :type file_import_rid: FileImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteFileImportPermissionDenied: Could not delete the FileImport.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core_models.BuildRid:
        """
        Executes the FileImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
        :type file_import_rid: FileImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core_models.BuildRid

        :raises ExecuteFileImportPermissionDenied: Could not execute the FileImport.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=core_models.BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteFileImportPermissionDenied": connectivity_errors.ExecuteFileImportPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> connectivity_models.FileImport:
        """
        Get the FileImport with the specified rid.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
        :type file_import_rid: FileImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: connectivity_models.FileImport

        :raises FileImportNotFound: The given FileImport could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=connectivity_models.FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "FileImportNotFound": connectivity_errors.FileImportNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[connectivity_models.FileImport]:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[connectivity_models.FileImport]
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
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
                response_type=connectivity_models.ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> connectivity_models.ListFileImportsResponse:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: connectivity_models.ListFileImportsResponse
        """

        warnings.warn(
            "The client.connectivity.FileImport.page(...) method has been deprecated. Please use client.connectivity.FileImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=connectivity_models.ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        dataset_rid: datasets_models.DatasetRid,
        display_name: connectivity_models.FileImportDisplayName,
        file_import_filters: typing.List[
            typing.Union[
                connectivity_models.FileImportFilter, connectivity_models.FileImportFilterDict
            ]
        ],
        import_mode: connectivity_models.FileImportMode,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        subfolder: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> connectivity_models.FileImport:
        """
        Replace the FileImport with the specified rid.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
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
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: connectivity_models.FileImport

        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        :raises ReplaceFileImportPermissionDenied: Could not replace the FileImport.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": datasets_models.DatasetRid,
                        "importMode": connectivity_models.FileImportMode,
                        "displayName": connectivity_models.FileImportDisplayName,
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "subfolder": typing.Optional[str],
                        "fileImportFilters": typing.List[
                            typing.Union[
                                connectivity_models.FileImportFilter,
                                connectivity_models.FileImportFilterDict,
                            ]
                        ],
                    },
                ),
                response_type=connectivity_models.FileImport,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        dataset_rid: datasets_models.DatasetRid,
        display_name: connectivity_models.FileImportDisplayName,
        file_import_filters: typing.List[
            typing.Union[
                connectivity_models.FileImportFilter, connectivity_models.FileImportFilterDict
            ]
        ],
        import_mode: connectivity_models.FileImportMode,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        subfolder: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[connectivity_models.FileImport]:
        """
        Creates a new FileImport.
        :param connection_rid:
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
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[connectivity_models.FileImport]

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises ConnectionNotFound: The given Connection could not be found.
        :raises CreateFileImportPermissionDenied: Could not create the FileImport.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileImportNotSupportedForConnection: The specified connection does not support file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": datasets_models.DatasetRid,
                        "importMode": connectivity_models.FileImportMode,
                        "displayName": connectivity_models.FileImportDisplayName,
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "subfolder": typing.Optional[str],
                        "fileImportFilters": typing.List[
                            typing.Union[
                                connectivity_models.FileImportFilter,
                                connectivity_models.FileImportFilterDict,
                            ]
                        ],
                    },
                ),
                response_type=connectivity_models.FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "CreateFileImportPermissionDenied": connectivity_errors.CreateFileImportPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Delete the FileImport with the specified RID.
        Deleting the file import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
        :type file_import_rid: FileImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises DeleteFileImportPermissionDenied: Could not delete the FileImport.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[core_models.BuildRid]:
        """
        Executes the FileImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
        :type file_import_rid: FileImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[core_models.BuildRid]

        :raises ExecuteFileImportPermissionDenied: Could not execute the FileImport.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=core_models.BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteFileImportPermissionDenied": connectivity_errors.ExecuteFileImportPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[connectivity_models.FileImport]:
        """
        Get the FileImport with the specified rid.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
        :type file_import_rid: FileImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[connectivity_models.FileImport]

        :raises FileImportNotFound: The given FileImport could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=connectivity_models.FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "FileImportNotFound": connectivity_errors.FileImportNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[connectivity_models.ListFileImportsResponse]:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[connectivity_models.ListFileImportsResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=connectivity_models.ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[connectivity_models.ListFileImportsResponse]:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[connectivity_models.ListFileImportsResponse]
        """

        warnings.warn(
            "The client.connectivity.FileImport.page(...) method has been deprecated. Please use client.connectivity.FileImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=connectivity_models.ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        dataset_rid: datasets_models.DatasetRid,
        display_name: connectivity_models.FileImportDisplayName,
        file_import_filters: typing.List[
            typing.Union[
                connectivity_models.FileImportFilter, connectivity_models.FileImportFilterDict
            ]
        ],
        import_mode: connectivity_models.FileImportMode,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        subfolder: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[connectivity_models.FileImport]:
        """
        Replace the FileImport with the specified rid.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
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
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[connectivity_models.FileImport]

        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        :raises ReplaceFileImportPermissionDenied: Could not replace the FileImport.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": datasets_models.DatasetRid,
                        "importMode": connectivity_models.FileImportMode,
                        "displayName": connectivity_models.FileImportDisplayName,
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "subfolder": typing.Optional[str],
                        "fileImportFilters": typing.List[
                            typing.Union[
                                connectivity_models.FileImportFilter,
                                connectivity_models.FileImportFilterDict,
                            ]
                        ],
                    },
                ),
                response_type=connectivity_models.FileImport,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        dataset_rid: datasets_models.DatasetRid,
        display_name: connectivity_models.FileImportDisplayName,
        file_import_filters: typing.List[
            typing.Union[
                connectivity_models.FileImportFilter, connectivity_models.FileImportFilterDict
            ]
        ],
        import_mode: connectivity_models.FileImportMode,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        subfolder: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[connectivity_models.FileImport]:
        """
        Creates a new FileImport.
        :param connection_rid:
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
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[connectivity_models.FileImport]

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises ConnectionNotFound: The given Connection could not be found.
        :raises CreateFileImportPermissionDenied: Could not create the FileImport.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileImportNotSupportedForConnection: The specified connection does not support file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": datasets_models.DatasetRid,
                        "importMode": connectivity_models.FileImportMode,
                        "displayName": connectivity_models.FileImportDisplayName,
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "subfolder": typing.Optional[str],
                        "fileImportFilters": typing.List[
                            typing.Union[
                                connectivity_models.FileImportFilter,
                                connectivity_models.FileImportFilterDict,
                            ]
                        ],
                    },
                ),
                response_type=connectivity_models.FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "CreateFileImportPermissionDenied": connectivity_errors.CreateFileImportPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Delete the FileImport with the specified RID.
        Deleting the file import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
        :type file_import_rid: FileImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises DeleteFileImportPermissionDenied: Could not delete the FileImport.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[core_models.BuildRid]:
        """
        Executes the FileImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
        :type file_import_rid: FileImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[core_models.BuildRid]

        :raises ExecuteFileImportPermissionDenied: Could not execute the FileImport.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=core_models.BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteFileImportPermissionDenied": connectivity_errors.ExecuteFileImportPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[connectivity_models.FileImport]:
        """
        Get the FileImport with the specified rid.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
        :type file_import_rid: FileImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[connectivity_models.FileImport]

        :raises FileImportNotFound: The given FileImport could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=connectivity_models.FileImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "FileImportNotFound": connectivity_errors.FileImportNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[connectivity_models.ListFileImportsResponse]:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[connectivity_models.ListFileImportsResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=connectivity_models.ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[connectivity_models.ListFileImportsResponse]:
        """
        Lists all file imports defined for this connection.
        Only file imports that the user has permissions to view will be returned.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[connectivity_models.ListFileImportsResponse]
        """

        warnings.warn(
            "The client.connectivity.FileImport.page(...) method has been deprecated. Please use client.connectivity.FileImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=connectivity_models.ListFileImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        file_import_rid: connectivity_models.FileImportRid,
        *,
        dataset_rid: datasets_models.DatasetRid,
        display_name: connectivity_models.FileImportDisplayName,
        file_import_filters: typing.List[
            typing.Union[
                connectivity_models.FileImportFilter, connectivity_models.FileImportFilterDict
            ]
        ],
        import_mode: connectivity_models.FileImportMode,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        subfolder: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[connectivity_models.FileImport]:
        """
        Replace the FileImport with the specified rid.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param file_import_rid:
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
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[connectivity_models.FileImport]

        :raises FileAtLeastCountFilterInvalidMinCount: The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0.
        :raises FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports: Custom file import filters can be fetched but cannot currently be used when creating or updating file imports.
        :raises FileSizeFilterGreaterThanCannotBeNegative: The `gt` property in the FileSizeFilter cannot be a negative number.
        :raises FileSizeFilterInvalidGreaterThanAndLessThanRange: The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`.
        :raises FileSizeFilterLessThanMustBeOneByteOrLarger: The `lt` property in the FileSizeFilter must be at least 1 byte.
        :raises FileSizeFilterMissingGreaterThanAndLessThan: Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present
        :raises ReplaceFileImportPermissionDenied: Could not replace the FileImport.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": datasets_models.DatasetRid,
                        "importMode": connectivity_models.FileImportMode,
                        "displayName": connectivity_models.FileImportDisplayName,
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "subfolder": typing.Optional[str],
                        "fileImportFilters": typing.List[
                            typing.Union[
                                connectivity_models.FileImportFilter,
                                connectivity_models.FileImportFilterDict,
                            ]
                        ],
                    },
                ),
                response_type=connectivity_models.FileImport,
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
