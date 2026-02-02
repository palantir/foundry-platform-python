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

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.connectivity import errors as connectivity_errors
from foundry_sdk.v2.connectivity import models as connectivity_models
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.filesystem import models as filesystem_models


class VirtualTableClient:
    """
    The API client for the VirtualTable Resource.

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

        self.with_streaming_response = _VirtualTableClientStreaming(self)
        self.with_raw_response = _VirtualTableClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        config: connectivity_models.VirtualTableConfig,
        name: connectivity_models.TableName,
        parent_rid: filesystem_models.FolderRid,
        markings: typing.Optional[typing.List[core_models.MarkingId]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> connectivity_models.VirtualTable:
        """
        Creates a new [Virtual Table](https://palantir.com/docs/foundry/data-integration/virtual-tables/) from an upstream table. The VirtualTable will be created
        in the specified parent folder and can be queried through Foundry's data access APIs.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param config:
        :type config: VirtualTableConfig
        :param name:
        :type name: TableName
        :param parent_rid:
        :type parent_rid: FolderRid
        :param markings:
        :type markings: Optional[List[MarkingId]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: connectivity_models.VirtualTable

        :raises ConnectionNotFound: The given Connection could not be found.
        :raises CreateVirtualTablePermissionDenied: Could not create the VirtualTable.
        :raises InvalidVirtualTableConnection: The specified connection is invalid or inaccessible.
        :raises VirtualTableAlreadyExists: A VirtualTable with the same name already exists in the parent folder.
        :raises VirtualTableRegisterFromSourcePermissionDenied: User lacks permission to use the specified connection for virtual table registration.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/virtualTables",
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
                body=connectivity_models.CreateVirtualTableRequest(
                    markings=markings,
                    parent_rid=parent_rid,
                    name=name,
                    config=config,
                ),
                response_type=connectivity_models.VirtualTable,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "CreateVirtualTablePermissionDenied": connectivity_errors.CreateVirtualTablePermissionDenied,
                    "InvalidVirtualTableConnection": connectivity_errors.InvalidVirtualTableConnection,
                    "VirtualTableAlreadyExists": connectivity_errors.VirtualTableAlreadyExists,
                    "VirtualTableRegisterFromSourcePermissionDenied": connectivity_errors.VirtualTableRegisterFromSourcePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _VirtualTableClientRaw:
    def __init__(self, client: VirtualTableClient) -> None:
        def create(_: connectivity_models.VirtualTable): ...

        self.create = core.with_raw_response(create, client.create)


class _VirtualTableClientStreaming:
    def __init__(self, client: VirtualTableClient) -> None:
        def create(_: connectivity_models.VirtualTable): ...

        self.create = core.with_streaming_response(create, client.create)


class AsyncVirtualTableClient:
    """
    The API client for the VirtualTable Resource.

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
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncVirtualTableClientStreaming(self)
        self.with_raw_response = _AsyncVirtualTableClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        config: connectivity_models.VirtualTableConfig,
        name: connectivity_models.TableName,
        parent_rid: filesystem_models.FolderRid,
        markings: typing.Optional[typing.List[core_models.MarkingId]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[connectivity_models.VirtualTable]:
        """
        Creates a new [Virtual Table](https://palantir.com/docs/foundry/data-integration/virtual-tables/) from an upstream table. The VirtualTable will be created
        in the specified parent folder and can be queried through Foundry's data access APIs.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param config:
        :type config: VirtualTableConfig
        :param name:
        :type name: TableName
        :param parent_rid:
        :type parent_rid: FolderRid
        :param markings:
        :type markings: Optional[List[MarkingId]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[connectivity_models.VirtualTable]

        :raises ConnectionNotFound: The given Connection could not be found.
        :raises CreateVirtualTablePermissionDenied: Could not create the VirtualTable.
        :raises InvalidVirtualTableConnection: The specified connection is invalid or inaccessible.
        :raises VirtualTableAlreadyExists: A VirtualTable with the same name already exists in the parent folder.
        :raises VirtualTableRegisterFromSourcePermissionDenied: User lacks permission to use the specified connection for virtual table registration.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/virtualTables",
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
                body=connectivity_models.CreateVirtualTableRequest(
                    markings=markings,
                    parent_rid=parent_rid,
                    name=name,
                    config=config,
                ),
                response_type=connectivity_models.VirtualTable,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "CreateVirtualTablePermissionDenied": connectivity_errors.CreateVirtualTablePermissionDenied,
                    "InvalidVirtualTableConnection": connectivity_errors.InvalidVirtualTableConnection,
                    "VirtualTableAlreadyExists": connectivity_errors.VirtualTableAlreadyExists,
                    "VirtualTableRegisterFromSourcePermissionDenied": connectivity_errors.VirtualTableRegisterFromSourcePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncVirtualTableClientRaw:
    def __init__(self, client: AsyncVirtualTableClient) -> None:
        def create(_: connectivity_models.VirtualTable): ...

        self.create = core.async_with_raw_response(create, client.create)


class _AsyncVirtualTableClientStreaming:
    def __init__(self, client: AsyncVirtualTableClient) -> None:
        def create(_: connectivity_models.VirtualTable): ...

        self.create = core.async_with_streaming_response(create, client.create)
