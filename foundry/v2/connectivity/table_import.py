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
from foundry.v2.connectivity.models._create_table_import_request_table_import_config import (
    CreateTableImportRequestTableImportConfig,
)  # NOQA
from foundry.v2.connectivity.models._create_table_import_request_table_import_config_dict import (
    CreateTableImportRequestTableImportConfigDict,
)  # NOQA
from foundry.v2.connectivity.models._list_table_imports_response import (
    ListTableImportsResponse,
)  # NOQA
from foundry.v2.connectivity.models._table_import import TableImport
from foundry.v2.connectivity.models._table_import_allow_schema_changes import (
    TableImportAllowSchemaChanges,
)  # NOQA
from foundry.v2.connectivity.models._table_import_display_name import TableImportDisplayName  # NOQA
from foundry.v2.connectivity.models._table_import_mode import TableImportMode
from foundry.v2.connectivity.models._table_import_rid import TableImportRid
from foundry.v2.core.models._build_rid import BuildRid
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid


class TableImportClient:
    """
    The API client for the TableImport Resource.

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
        self.with_streaming_response = _TableImportClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _TableImportClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        connection_rid: ConnectionRid,
        *,
        config: Union[
            CreateTableImportRequestTableImportConfig, CreateTableImportRequestTableImportConfigDict
        ],
        dataset_rid: DatasetRid,
        display_name: TableImportDisplayName,
        import_mode: TableImportMode,
        allow_schema_changes: Optional[TableImportAllowSchemaChanges] = None,
        branch_name: Optional[BranchName] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> TableImport:
        """
        Creates a new TableImport.
        :param connection_rid: connectionRid
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
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: TableImport

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises CreateTableImportPermissionDenied: Could not create the TableImport.
        :raises TableImportNotSupportedForConnection: The specified connection does not support creating a table import with the specified config.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": DatasetRid,
                        "importMode": TableImportMode,
                        "displayName": TableImportDisplayName,
                        "allowSchemaChanges": Optional[TableImportAllowSchemaChanges],
                        "branchName": Optional[BranchName],
                        "config": Union[
                            CreateTableImportRequestTableImportConfig,
                            CreateTableImportRequestTableImportConfigDict,
                        ],
                    },
                ),
                response_type=TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "CreateTableImportPermissionDenied": connectivity_errors.CreateTableImportPermissionDenied,
                    "TableImportNotSupportedForConnection": connectivity_errors.TableImportNotSupportedForConnection,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        connection_rid: ConnectionRid,
        table_import_rid: TableImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Delete the TableImport with the specified RID.
        Deleting the table import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param table_import_rid: tableImportRid
        :type table_import_rid: TableImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteTableImportPermissionDenied: Could not delete the TableImport.
        """

        return self._api_client.call_api(
            RequestInfo(
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

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        connection_rid: ConnectionRid,
        table_import_rid: TableImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> BuildRid:
        """
        Executes the TableImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param table_import_rid: tableImportRid
        :type table_import_rid: TableImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: BuildRid

        :raises ExecuteTableImportPermissionDenied: Could not execute the TableImport.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteTableImportPermissionDenied": connectivity_errors.ExecuteTableImportPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        connection_rid: ConnectionRid,
        table_import_rid: TableImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> TableImport:
        """
        Get the TableImport with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param table_import_rid: tableImportRid
        :type table_import_rid: TableImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: TableImport

        :raises TableImportNotFound: The given TableImport could not be found.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "TableImportNotFound": connectivity_errors.TableImportNotFound,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
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
    ) -> ResourceIterator[TableImport]:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: ResourceIterator[TableImport]
        """

        return self._api_client.iterate_api(
            RequestInfo(
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
                response_type=ListTableImportsResponse,
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
    ) -> ListTableImportsResponse:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: ListTableImportsResponse
        """

        warnings.warn(
            "The client.connectivity.TableImport.page(...) method has been deprecated. Please use client.connectivity.TableImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListTableImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
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
        config: Union[
            CreateTableImportRequestTableImportConfig, CreateTableImportRequestTableImportConfigDict
        ],
        dataset_rid: DatasetRid,
        display_name: TableImportDisplayName,
        import_mode: TableImportMode,
        allow_schema_changes: Optional[TableImportAllowSchemaChanges] = None,
        branch_name: Optional[BranchName] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[TableImport]:
        """
        Creates a new TableImport.
        :param connection_rid: connectionRid
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
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[TableImport]

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises CreateTableImportPermissionDenied: Could not create the TableImport.
        :raises TableImportNotSupportedForConnection: The specified connection does not support creating a table import with the specified config.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": DatasetRid,
                        "importMode": TableImportMode,
                        "displayName": TableImportDisplayName,
                        "allowSchemaChanges": Optional[TableImportAllowSchemaChanges],
                        "branchName": Optional[BranchName],
                        "config": Union[
                            CreateTableImportRequestTableImportConfig,
                            CreateTableImportRequestTableImportConfigDict,
                        ],
                    },
                ),
                response_type=TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "CreateTableImportPermissionDenied": connectivity_errors.CreateTableImportPermissionDenied,
                    "TableImportNotSupportedForConnection": connectivity_errors.TableImportNotSupportedForConnection,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        connection_rid: ConnectionRid,
        table_import_rid: TableImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Delete the TableImport with the specified RID.
        Deleting the table import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param table_import_rid: tableImportRid
        :type table_import_rid: TableImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises DeleteTableImportPermissionDenied: Could not delete the TableImport.
        """

        return self._api_client.call_api(
            RequestInfo(
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

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        connection_rid: ConnectionRid,
        table_import_rid: TableImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[BuildRid]:
        """
        Executes the TableImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param table_import_rid: tableImportRid
        :type table_import_rid: TableImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[BuildRid]

        :raises ExecuteTableImportPermissionDenied: Could not execute the TableImport.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteTableImportPermissionDenied": connectivity_errors.ExecuteTableImportPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        connection_rid: ConnectionRid,
        table_import_rid: TableImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[TableImport]:
        """
        Get the TableImport with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param table_import_rid: tableImportRid
        :type table_import_rid: TableImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[TableImport]

        :raises TableImportNotFound: The given TableImport could not be found.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "TableImportNotFound": connectivity_errors.TableImportNotFound,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
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
    ) -> ApiResponse[ListTableImportsResponse]:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: ApiResponse[ListTableImportsResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListTableImportsResponse,
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
    ) -> ApiResponse[ListTableImportsResponse]:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: ApiResponse[ListTableImportsResponse]
        """

        warnings.warn(
            "The client.connectivity.TableImport.page(...) method has been deprecated. Please use client.connectivity.TableImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListTableImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
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
        config: Union[
            CreateTableImportRequestTableImportConfig, CreateTableImportRequestTableImportConfigDict
        ],
        dataset_rid: DatasetRid,
        display_name: TableImportDisplayName,
        import_mode: TableImportMode,
        allow_schema_changes: Optional[TableImportAllowSchemaChanges] = None,
        branch_name: Optional[BranchName] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[TableImport]:
        """
        Creates a new TableImport.
        :param connection_rid: connectionRid
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
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[TableImport]

        :raises ConnectionDetailsNotDetermined: Details of the connection (such as which types of import it supports) could not be determined.
        :raises CreateTableImportPermissionDenied: Could not create the TableImport.
        :raises TableImportNotSupportedForConnection: The specified connection does not support creating a table import with the specified config.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": DatasetRid,
                        "importMode": TableImportMode,
                        "displayName": TableImportDisplayName,
                        "allowSchemaChanges": Optional[TableImportAllowSchemaChanges],
                        "branchName": Optional[BranchName],
                        "config": Union[
                            CreateTableImportRequestTableImportConfig,
                            CreateTableImportRequestTableImportConfigDict,
                        ],
                    },
                ),
                response_type=TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionDetailsNotDetermined": connectivity_errors.ConnectionDetailsNotDetermined,
                    "CreateTableImportPermissionDenied": connectivity_errors.CreateTableImportPermissionDenied,
                    "TableImportNotSupportedForConnection": connectivity_errors.TableImportNotSupportedForConnection,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        connection_rid: ConnectionRid,
        table_import_rid: TableImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Delete the TableImport with the specified RID.
        Deleting the table import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param table_import_rid: tableImportRid
        :type table_import_rid: TableImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises DeleteTableImportPermissionDenied: Could not delete the TableImport.
        """

        return self._api_client.stream_api(
            RequestInfo(
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

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        connection_rid: ConnectionRid,
        table_import_rid: TableImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[BuildRid]:
        """
        Executes the TableImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param table_import_rid: tableImportRid
        :type table_import_rid: TableImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[BuildRid]

        :raises ExecuteTableImportPermissionDenied: Could not execute the TableImport.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=BuildRid,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteTableImportPermissionDenied": connectivity_errors.ExecuteTableImportPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        connection_rid: ConnectionRid,
        table_import_rid: TableImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[TableImport]:
        """
        Get the TableImport with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param table_import_rid: tableImportRid
        :type table_import_rid: TableImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[TableImport]

        :raises TableImportNotFound: The given TableImport could not be found.
        :raises TableImportTypeNotSupported: The specified table import type is not yet supported in the Platform API.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=TableImport,
                request_timeout=request_timeout,
                throwable_errors={
                    "TableImportNotFound": connectivity_errors.TableImportNotFound,
                    "TableImportTypeNotSupported": connectivity_errors.TableImportTypeNotSupported,
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
    ) -> StreamingContextManager[ListTableImportsResponse]:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: StreamingContextManager[ListTableImportsResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListTableImportsResponse,
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
    ) -> StreamingContextManager[ListTableImportsResponse]:
        """
        Lists all table imports defined for this connection.
        Only table imports that the user has permissions to view will be returned.

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
        :rtype: StreamingContextManager[ListTableImportsResponse]
        """

        warnings.warn(
            "The client.connectivity.TableImport.page(...) method has been deprecated. Please use client.connectivity.TableImport.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListTableImportsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
