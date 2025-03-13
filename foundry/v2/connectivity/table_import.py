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


class TableImportClient:
    """
    The API client for the TableImport Resource.

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
        self.with_streaming_response = _TableImportClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _TableImportClientRaw(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        config: typing.Union[
            connectivity_models.CreateTableImportRequestTableImportConfig,
            connectivity_models.CreateTableImportRequestTableImportConfigDict,
        ],
        dataset_rid: datasets_models.DatasetRid,
        display_name: connectivity_models.TableImportDisplayName,
        import_mode: connectivity_models.TableImportMode,
        allow_schema_changes: typing.Optional[
            connectivity_models.TableImportAllowSchemaChanges
        ] = None,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> connectivity_models.TableImport:
        """
        Creates a new TableImport.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param config:
        :type config: Union[CreateTableImportRequestTableImportConfig, CreateTableImportRequestTableImportConfigDict]
        :param dataset_rid: The RID of the output dataset.
        :type dataset_rid: DatasetRid
        :param display_name:
        :type display_name: TableImportDisplayName
        :param import_mode:
        :type import_mode: TableImportMode
        :param allow_schema_changes: Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports.
        :type allow_schema_changes: Optional[TableImportAllowSchemaChanges]
        :param branch_name: The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: connectivity_models.TableImport

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises ConnectionNotFound: The given Connection could not be found.
        :raises CreateTableImportPermissionDenied: Could not create the TableImport.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises TableImportNotSupportedForConnection: The specified connection does not support creating a table import with the specified config.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports",
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
                    "allowSchemaChanges": allow_schema_changes,
                    "branchName": branch_name,
                    "config": config,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": datasets_models.DatasetRid,
                        "importMode": connectivity_models.TableImportMode,
                        "displayName": connectivity_models.TableImportDisplayName,
                        "allowSchemaChanges": typing.Optional[
                            connectivity_models.TableImportAllowSchemaChanges
                        ],
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "config": typing.Union[
                            connectivity_models.CreateTableImportRequestTableImportConfig,
                            connectivity_models.CreateTableImportRequestTableImportConfigDict,
                        ],
                    },
                ),
                response_type=connectivity_models.TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "CreateTableImportPermissionDenied": connectivity_errors.CreateTableImportPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "TableImportNotSupportedForConnection": connectivity_errors.TableImportNotSupportedForConnection,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        table_import_rid: connectivity_models.TableImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Delete the TableImport with the specified RID.
        Deleting the table import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param table_import_rid:
        :type table_import_rid: TableImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteTableImportPermissionDenied: Could not delete the TableImport.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "tableImportRid": table_import_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteTableImportPermissionDenied": connectivity_errors.DeleteTableImportPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        table_import_rid: connectivity_models.TableImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core_models.BuildRid:
        """
        Executes the TableImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param table_import_rid:
        :type table_import_rid: TableImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core_models.BuildRid

        :raises ExecuteTableImportPermissionDenied: Could not execute the TableImport.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}/execute",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "tableImportRid": table_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=core_models.BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteTableImportPermissionDenied": connectivity_errors.ExecuteTableImportPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        table_import_rid: connectivity_models.TableImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> connectivity_models.TableImport:
        """
        Get the TableImport with the specified rid.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param table_import_rid:
        :type table_import_rid: TableImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: connectivity_models.TableImport

        :raises TableImportNotFound: The given TableImport could not be found.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "tableImportRid": table_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=connectivity_models.TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "TableImportNotFound": connectivity_errors.TableImportNotFound,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
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
    ) -> core.ResourceIterator[connectivity_models.TableImport]:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: core.ResourceIterator[connectivity_models.TableImport]

        :raises ConnectionNotFound: The given Connection could not be found.
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports",
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
                response_type=connectivity_models.ListTableImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                },
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
    ) -> connectivity_models.ListTableImportsResponse:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: connectivity_models.ListTableImportsResponse

        :raises ConnectionNotFound: The given Connection could not be found.
        """

        warnings.warn(
            "The client.connectivity.TableImport.page(...) method has been deprecated. Please use client.connectivity.TableImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports",
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
                response_type=connectivity_models.ListTableImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                },
            ),
        ).decode()


class _TableImportClientRaw:
    """
    The API client for the TableImport Resource.

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
        config: typing.Union[
            connectivity_models.CreateTableImportRequestTableImportConfig,
            connectivity_models.CreateTableImportRequestTableImportConfigDict,
        ],
        dataset_rid: datasets_models.DatasetRid,
        display_name: connectivity_models.TableImportDisplayName,
        import_mode: connectivity_models.TableImportMode,
        allow_schema_changes: typing.Optional[
            connectivity_models.TableImportAllowSchemaChanges
        ] = None,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[connectivity_models.TableImport]:
        """
        Creates a new TableImport.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param config:
        :type config: Union[CreateTableImportRequestTableImportConfig, CreateTableImportRequestTableImportConfigDict]
        :param dataset_rid: The RID of the output dataset.
        :type dataset_rid: DatasetRid
        :param display_name:
        :type display_name: TableImportDisplayName
        :param import_mode:
        :type import_mode: TableImportMode
        :param allow_schema_changes: Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports.
        :type allow_schema_changes: Optional[TableImportAllowSchemaChanges]
        :param branch_name: The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[connectivity_models.TableImport]

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises ConnectionNotFound: The given Connection could not be found.
        :raises CreateTableImportPermissionDenied: Could not create the TableImport.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises TableImportNotSupportedForConnection: The specified connection does not support creating a table import with the specified config.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports",
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
                    "allowSchemaChanges": allow_schema_changes,
                    "branchName": branch_name,
                    "config": config,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": datasets_models.DatasetRid,
                        "importMode": connectivity_models.TableImportMode,
                        "displayName": connectivity_models.TableImportDisplayName,
                        "allowSchemaChanges": typing.Optional[
                            connectivity_models.TableImportAllowSchemaChanges
                        ],
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "config": typing.Union[
                            connectivity_models.CreateTableImportRequestTableImportConfig,
                            connectivity_models.CreateTableImportRequestTableImportConfigDict,
                        ],
                    },
                ),
                response_type=connectivity_models.TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "CreateTableImportPermissionDenied": connectivity_errors.CreateTableImportPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "TableImportNotSupportedForConnection": connectivity_errors.TableImportNotSupportedForConnection,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        table_import_rid: connectivity_models.TableImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Delete the TableImport with the specified RID.
        Deleting the table import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param table_import_rid:
        :type table_import_rid: TableImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises DeleteTableImportPermissionDenied: Could not delete the TableImport.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "tableImportRid": table_import_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteTableImportPermissionDenied": connectivity_errors.DeleteTableImportPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        table_import_rid: connectivity_models.TableImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[core_models.BuildRid]:
        """
        Executes the TableImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param table_import_rid:
        :type table_import_rid: TableImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[core_models.BuildRid]

        :raises ExecuteTableImportPermissionDenied: Could not execute the TableImport.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}/execute",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "tableImportRid": table_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=core_models.BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteTableImportPermissionDenied": connectivity_errors.ExecuteTableImportPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        table_import_rid: connectivity_models.TableImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[connectivity_models.TableImport]:
        """
        Get the TableImport with the specified rid.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param table_import_rid:
        :type table_import_rid: TableImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[connectivity_models.TableImport]

        :raises TableImportNotFound: The given TableImport could not be found.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "tableImportRid": table_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=connectivity_models.TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "TableImportNotFound": connectivity_errors.TableImportNotFound,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
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
    ) -> core.ApiResponse[connectivity_models.ListTableImportsResponse]:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: core.ApiResponse[connectivity_models.ListTableImportsResponse]

        :raises ConnectionNotFound: The given Connection could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports",
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
                response_type=connectivity_models.ListTableImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                },
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
    ) -> core.ApiResponse[connectivity_models.ListTableImportsResponse]:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: core.ApiResponse[connectivity_models.ListTableImportsResponse]

        :raises ConnectionNotFound: The given Connection could not be found.
        """

        warnings.warn(
            "The client.connectivity.TableImport.page(...) method has been deprecated. Please use client.connectivity.TableImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports",
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
                response_type=connectivity_models.ListTableImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                },
            ),
        )


class _TableImportClientStreaming:
    """
    The API client for the TableImport Resource.

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
        config: typing.Union[
            connectivity_models.CreateTableImportRequestTableImportConfig,
            connectivity_models.CreateTableImportRequestTableImportConfigDict,
        ],
        dataset_rid: datasets_models.DatasetRid,
        display_name: connectivity_models.TableImportDisplayName,
        import_mode: connectivity_models.TableImportMode,
        allow_schema_changes: typing.Optional[
            connectivity_models.TableImportAllowSchemaChanges
        ] = None,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[connectivity_models.TableImport]:
        """
        Creates a new TableImport.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param config:
        :type config: Union[CreateTableImportRequestTableImportConfig, CreateTableImportRequestTableImportConfigDict]
        :param dataset_rid: The RID of the output dataset.
        :type dataset_rid: DatasetRid
        :param display_name:
        :type display_name: TableImportDisplayName
        :param import_mode:
        :type import_mode: TableImportMode
        :param allow_schema_changes: Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports.
        :type allow_schema_changes: Optional[TableImportAllowSchemaChanges]
        :param branch_name: The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[connectivity_models.TableImport]

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises ConnectionNotFound: The given Connection could not be found.
        :raises CreateTableImportPermissionDenied: Could not create the TableImport.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises TableImportNotSupportedForConnection: The specified connection does not support creating a table import with the specified config.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports",
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
                    "allowSchemaChanges": allow_schema_changes,
                    "branchName": branch_name,
                    "config": config,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": datasets_models.DatasetRid,
                        "importMode": connectivity_models.TableImportMode,
                        "displayName": connectivity_models.TableImportDisplayName,
                        "allowSchemaChanges": typing.Optional[
                            connectivity_models.TableImportAllowSchemaChanges
                        ],
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "config": typing.Union[
                            connectivity_models.CreateTableImportRequestTableImportConfig,
                            connectivity_models.CreateTableImportRequestTableImportConfigDict,
                        ],
                    },
                ),
                response_type=connectivity_models.TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "CreateTableImportPermissionDenied": connectivity_errors.CreateTableImportPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "TableImportNotSupportedForConnection": connectivity_errors.TableImportNotSupportedForConnection,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        table_import_rid: connectivity_models.TableImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Delete the TableImport with the specified RID.
        Deleting the table import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param table_import_rid:
        :type table_import_rid: TableImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises DeleteTableImportPermissionDenied: Could not delete the TableImport.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "tableImportRid": table_import_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteTableImportPermissionDenied": connectivity_errors.DeleteTableImportPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        table_import_rid: connectivity_models.TableImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[core_models.BuildRid]:
        """
        Executes the TableImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param table_import_rid:
        :type table_import_rid: TableImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[core_models.BuildRid]

        :raises ExecuteTableImportPermissionDenied: Could not execute the TableImport.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}/execute",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "tableImportRid": table_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=core_models.BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteTableImportPermissionDenied": connectivity_errors.ExecuteTableImportPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        table_import_rid: connectivity_models.TableImportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[connectivity_models.TableImport]:
        """
        Get the TableImport with the specified rid.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param table_import_rid:
        :type table_import_rid: TableImportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[connectivity_models.TableImport]

        :raises TableImportNotFound: The given TableImport could not be found.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                    "tableImportRid": table_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=connectivity_models.TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "TableImportNotFound": connectivity_errors.TableImportNotFound,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
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
    ) -> core.StreamingContextManager[connectivity_models.ListTableImportsResponse]:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: core.StreamingContextManager[connectivity_models.ListTableImportsResponse]

        :raises ConnectionNotFound: The given Connection could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports",
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
                response_type=connectivity_models.ListTableImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                },
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
    ) -> core.StreamingContextManager[connectivity_models.ListTableImportsResponse]:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: core.StreamingContextManager[connectivity_models.ListTableImportsResponse]

        :raises ConnectionNotFound: The given Connection could not be found.
        """

        warnings.warn(
            "The client.connectivity.TableImport.page(...) method has been deprecated. Please use client.connectivity.TableImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/tableImports",
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
                response_type=connectivity_models.ListTableImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                },
            ),
        )
