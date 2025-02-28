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
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.connectivity import errors as connectivity_errors
from foundry.v2.connectivity.models._connection import Connection
from foundry.v2.connectivity.models._connection_configuration import ConnectionConfiguration  # NOQA
from foundry.v2.connectivity.models._connection_display_name import ConnectionDisplayName  # NOQA
from foundry.v2.connectivity.models._connection_rid import ConnectionRid
from foundry.v2.connectivity.models._create_connection_request_connection_configuration import (
    CreateConnectionRequestConnectionConfiguration,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_connection_configuration_dict import (
    CreateConnectionRequestConnectionConfigurationDict,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_runtime_platform import (
    CreateConnectionRequestRuntimePlatform,
)  # NOQA
from foundry.v2.connectivity.models._create_connection_request_runtime_platform_dict import (
    CreateConnectionRequestRuntimePlatformDict,
)  # NOQA
from foundry.v2.connectivity.models._plaintext_value import PlaintextValue
from foundry.v2.connectivity.models._secret_name import SecretName
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.filesystem.models._folder_rid import FolderRid


class ConnectionClient:
    """
    The API client for the Connection Resource.

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
        self.with_streaming_response = _ConnectionClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ConnectionClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def FileImport(self):
        from foundry.v2.connectivity.file_import import FileImportClient

        return FileImportClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def TableImport(self):
        from foundry.v2.connectivity.table_import import TableImportClient

        return TableImportClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        configuration: Union[
            CreateConnectionRequestConnectionConfiguration,
            CreateConnectionRequestConnectionConfigurationDict,
        ],
        display_name: ConnectionDisplayName,
        parent_folder_rid: FolderRid,
        runtime_platform: Union[
            CreateConnectionRequestRuntimePlatform, CreateConnectionRequestRuntimePlatformDict
        ],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Connection:
        """
        Creates a new Connection.
        Any secrets specified in the request body are transmitted over the network encrypted using TLS. Once the
        secrets reach Foundry's servers, they will be temporarily decrypted and remain in plaintext in memory to
        be processed as needed. They will stay in plaintext in memory until the garbage collection process cleans
        up the memory. The secrets are always stored encrypted on our servers.
        By using this endpoint, you acknowledge and accept any potential risks associated with the temporary
        in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should
        use the Foundry UI instead.

        :param configuration:
        :type configuration: Union[CreateConnectionRequestConnectionConfiguration, CreateConnectionRequestConnectionConfigurationDict]
        :param display_name: The display name of the Connection. The display name must not be blank.
        :type display_name: ConnectionDisplayName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param runtime_platform:
        :type runtime_platform: Union[CreateConnectionRequestRuntimePlatform, CreateConnectionRequestRuntimePlatformDict]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Connection

        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises CreateConnectionPermissionDenied: Could not create the Connection.
        :raises ParentFolderNotFoundForConnection: The parent folder for the specified connection could not be found.
        :raises PropertyCannotBeBlank: The specified property cannot be blank.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parentFolderRid": parent_folder_rid,
                    "runtimePlatform": runtime_platform,
                    "configuration": configuration,
                    "displayName": display_name,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": FolderRid,
                        "runtimePlatform": Union[
                            CreateConnectionRequestRuntimePlatform,
                            CreateConnectionRequestRuntimePlatformDict,
                        ],
                        "configuration": Union[
                            CreateConnectionRequestConnectionConfiguration,
                            CreateConnectionRequestConnectionConfigurationDict,
                        ],
                        "displayName": ConnectionDisplayName,
                    },
                ),
                response_type=Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "CreateConnectionPermissionDenied": connectivity_errors.CreateConnectionPermissionDenied,
                    "ParentFolderNotFoundForConnection": connectivity_errors.ParentFolderNotFoundForConnection,
                    "PropertyCannotBeBlank": connectivity_errors.PropertyCannotBeBlank,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        connection_rid: ConnectionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Connection:
        """
        Get the Connection with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Connection

        :raises ConnectionNotFound: The given Connection could not be found.
        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises ParentFolderNotFoundForConnection: The parent folder for the specified connection could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}",
                query_params={
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
                response_type=Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "ParentFolderNotFoundForConnection": connectivity_errors.ParentFolderNotFoundForConnection,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_configuration(
        self,
        connection_rid: ConnectionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ConnectionConfiguration:
        """
        Retrieves the ConnectionConfiguration of the [Connection](/docs/foundry/data-connection/set-up-source/) itself.
        This operation is intended for use when other Connection data is not required, providing a lighter-weight alternative to `getConnection` operation.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ConnectionConfiguration

        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises GetConfigurationPermissionDenied: Could not getConfiguration the Connection.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/getConfiguration",
                query_params={
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
                response_type=ConnectionConfiguration,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "GetConfigurationPermissionDenied": connectivity_errors.GetConfigurationPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def update_secrets(
        self,
        connection_rid: ConnectionRid,
        *,
        secrets: Dict[SecretName, PlaintextValue],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Updates the secrets on the connection to the specified secret values.
        Secrets that are currently configured on the connection but are omitted in the request will remain unchanged.

        Secrets are transmitted over the network encrypted using TLS. Once the secrets reach Foundry's servers,
        they will be temporarily decrypted and remain in plaintext in memory to be processed as needed.
        They will stay in plaintext in memory until the garbage collection process cleans up the memory.
        The secrets are always stored encrypted on our servers.

        By using this endpoint, you acknowledge and accept any potential risks associated with the temporary
        in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should
        use the Foundry UI instead.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param secrets: The secrets to be updated. The specified secret names must already be configured on the connection.
        :type secrets: Dict[SecretName, PlaintextValue]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises SecretNamesDoNotExist: The secret names provided do not exist on the connection.
        :raises UpdateSecretsForConnectionPermissionDenied: Could not update secrets for the Connection.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/updateSecrets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "secrets": secrets,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "secrets": Dict[SecretName, PlaintextValue],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "SecretNamesDoNotExist": connectivity_errors.SecretNamesDoNotExist,
                    "UpdateSecretsForConnectionPermissionDenied": connectivity_errors.UpdateSecretsForConnectionPermissionDenied,
                },
            ),
        ).decode()


class _ConnectionClientRaw:
    """
    The API client for the Connection Resource.

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
        *,
        configuration: Union[
            CreateConnectionRequestConnectionConfiguration,
            CreateConnectionRequestConnectionConfigurationDict,
        ],
        display_name: ConnectionDisplayName,
        parent_folder_rid: FolderRid,
        runtime_platform: Union[
            CreateConnectionRequestRuntimePlatform, CreateConnectionRequestRuntimePlatformDict
        ],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Connection]:
        """
        Creates a new Connection.
        Any secrets specified in the request body are transmitted over the network encrypted using TLS. Once the
        secrets reach Foundry's servers, they will be temporarily decrypted and remain in plaintext in memory to
        be processed as needed. They will stay in plaintext in memory until the garbage collection process cleans
        up the memory. The secrets are always stored encrypted on our servers.
        By using this endpoint, you acknowledge and accept any potential risks associated with the temporary
        in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should
        use the Foundry UI instead.

        :param configuration:
        :type configuration: Union[CreateConnectionRequestConnectionConfiguration, CreateConnectionRequestConnectionConfigurationDict]
        :param display_name: The display name of the Connection. The display name must not be blank.
        :type display_name: ConnectionDisplayName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param runtime_platform:
        :type runtime_platform: Union[CreateConnectionRequestRuntimePlatform, CreateConnectionRequestRuntimePlatformDict]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Connection]

        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises CreateConnectionPermissionDenied: Could not create the Connection.
        :raises ParentFolderNotFoundForConnection: The parent folder for the specified connection could not be found.
        :raises PropertyCannotBeBlank: The specified property cannot be blank.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parentFolderRid": parent_folder_rid,
                    "runtimePlatform": runtime_platform,
                    "configuration": configuration,
                    "displayName": display_name,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": FolderRid,
                        "runtimePlatform": Union[
                            CreateConnectionRequestRuntimePlatform,
                            CreateConnectionRequestRuntimePlatformDict,
                        ],
                        "configuration": Union[
                            CreateConnectionRequestConnectionConfiguration,
                            CreateConnectionRequestConnectionConfigurationDict,
                        ],
                        "displayName": ConnectionDisplayName,
                    },
                ),
                response_type=Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "CreateConnectionPermissionDenied": connectivity_errors.CreateConnectionPermissionDenied,
                    "ParentFolderNotFoundForConnection": connectivity_errors.ParentFolderNotFoundForConnection,
                    "PropertyCannotBeBlank": connectivity_errors.PropertyCannotBeBlank,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        connection_rid: ConnectionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Connection]:
        """
        Get the Connection with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Connection]

        :raises ConnectionNotFound: The given Connection could not be found.
        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises ParentFolderNotFoundForConnection: The parent folder for the specified connection could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}",
                query_params={
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
                response_type=Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "ParentFolderNotFoundForConnection": connectivity_errors.ParentFolderNotFoundForConnection,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_configuration(
        self,
        connection_rid: ConnectionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ConnectionConfiguration]:
        """
        Retrieves the ConnectionConfiguration of the [Connection](/docs/foundry/data-connection/set-up-source/) itself.
        This operation is intended for use when other Connection data is not required, providing a lighter-weight alternative to `getConnection` operation.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ConnectionConfiguration]

        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises GetConfigurationPermissionDenied: Could not getConfiguration the Connection.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/getConfiguration",
                query_params={
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
                response_type=ConnectionConfiguration,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "GetConfigurationPermissionDenied": connectivity_errors.GetConfigurationPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def update_secrets(
        self,
        connection_rid: ConnectionRid,
        *,
        secrets: Dict[SecretName, PlaintextValue],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Updates the secrets on the connection to the specified secret values.
        Secrets that are currently configured on the connection but are omitted in the request will remain unchanged.

        Secrets are transmitted over the network encrypted using TLS. Once the secrets reach Foundry's servers,
        they will be temporarily decrypted and remain in plaintext in memory to be processed as needed.
        They will stay in plaintext in memory until the garbage collection process cleans up the memory.
        The secrets are always stored encrypted on our servers.

        By using this endpoint, you acknowledge and accept any potential risks associated with the temporary
        in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should
        use the Foundry UI instead.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param secrets: The secrets to be updated. The specified secret names must already be configured on the connection.
        :type secrets: Dict[SecretName, PlaintextValue]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises SecretNamesDoNotExist: The secret names provided do not exist on the connection.
        :raises UpdateSecretsForConnectionPermissionDenied: Could not update secrets for the Connection.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/updateSecrets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "secrets": secrets,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "secrets": Dict[SecretName, PlaintextValue],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "SecretNamesDoNotExist": connectivity_errors.SecretNamesDoNotExist,
                    "UpdateSecretsForConnectionPermissionDenied": connectivity_errors.UpdateSecretsForConnectionPermissionDenied,
                },
            ),
        )


class _ConnectionClientStreaming:
    """
    The API client for the Connection Resource.

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
        *,
        configuration: Union[
            CreateConnectionRequestConnectionConfiguration,
            CreateConnectionRequestConnectionConfigurationDict,
        ],
        display_name: ConnectionDisplayName,
        parent_folder_rid: FolderRid,
        runtime_platform: Union[
            CreateConnectionRequestRuntimePlatform, CreateConnectionRequestRuntimePlatformDict
        ],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Connection]:
        """
        Creates a new Connection.
        Any secrets specified in the request body are transmitted over the network encrypted using TLS. Once the
        secrets reach Foundry's servers, they will be temporarily decrypted and remain in plaintext in memory to
        be processed as needed. They will stay in plaintext in memory until the garbage collection process cleans
        up the memory. The secrets are always stored encrypted on our servers.
        By using this endpoint, you acknowledge and accept any potential risks associated with the temporary
        in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should
        use the Foundry UI instead.

        :param configuration:
        :type configuration: Union[CreateConnectionRequestConnectionConfiguration, CreateConnectionRequestConnectionConfigurationDict]
        :param display_name: The display name of the Connection. The display name must not be blank.
        :type display_name: ConnectionDisplayName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param runtime_platform:
        :type runtime_platform: Union[CreateConnectionRequestRuntimePlatform, CreateConnectionRequestRuntimePlatformDict]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Connection]

        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises CreateConnectionPermissionDenied: Could not create the Connection.
        :raises ParentFolderNotFoundForConnection: The parent folder for the specified connection could not be found.
        :raises PropertyCannotBeBlank: The specified property cannot be blank.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parentFolderRid": parent_folder_rid,
                    "runtimePlatform": runtime_platform,
                    "configuration": configuration,
                    "displayName": display_name,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": FolderRid,
                        "runtimePlatform": Union[
                            CreateConnectionRequestRuntimePlatform,
                            CreateConnectionRequestRuntimePlatformDict,
                        ],
                        "configuration": Union[
                            CreateConnectionRequestConnectionConfiguration,
                            CreateConnectionRequestConnectionConfigurationDict,
                        ],
                        "displayName": ConnectionDisplayName,
                    },
                ),
                response_type=Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "CreateConnectionPermissionDenied": connectivity_errors.CreateConnectionPermissionDenied,
                    "ParentFolderNotFoundForConnection": connectivity_errors.ParentFolderNotFoundForConnection,
                    "PropertyCannotBeBlank": connectivity_errors.PropertyCannotBeBlank,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        connection_rid: ConnectionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Connection]:
        """
        Get the Connection with the specified rid.
        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Connection]

        :raises ConnectionNotFound: The given Connection could not be found.
        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises ParentFolderNotFoundForConnection: The parent folder for the specified connection could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}",
                query_params={
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
                response_type=Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "ParentFolderNotFoundForConnection": connectivity_errors.ParentFolderNotFoundForConnection,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_configuration(
        self,
        connection_rid: ConnectionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ConnectionConfiguration]:
        """
        Retrieves the ConnectionConfiguration of the [Connection](/docs/foundry/data-connection/set-up-source/) itself.
        This operation is intended for use when other Connection data is not required, providing a lighter-weight alternative to `getConnection` operation.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ConnectionConfiguration]

        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises GetConfigurationPermissionDenied: Could not getConfiguration the Connection.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/connections/{connectionRid}/getConfiguration",
                query_params={
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
                response_type=ConnectionConfiguration,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "GetConfigurationPermissionDenied": connectivity_errors.GetConfigurationPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def update_secrets(
        self,
        connection_rid: ConnectionRid,
        *,
        secrets: Dict[SecretName, PlaintextValue],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Updates the secrets on the connection to the specified secret values.
        Secrets that are currently configured on the connection but are omitted in the request will remain unchanged.

        Secrets are transmitted over the network encrypted using TLS. Once the secrets reach Foundry's servers,
        they will be temporarily decrypted and remain in plaintext in memory to be processed as needed.
        They will stay in plaintext in memory until the garbage collection process cleans up the memory.
        The secrets are always stored encrypted on our servers.

        By using this endpoint, you acknowledge and accept any potential risks associated with the temporary
        in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should
        use the Foundry UI instead.

        :param connection_rid: connectionRid
        :type connection_rid: ConnectionRid
        :param secrets: The secrets to be updated. The specified secret names must already be configured on the connection.
        :type secrets: Dict[SecretName, PlaintextValue]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises SecretNamesDoNotExist: The secret names provided do not exist on the connection.
        :raises UpdateSecretsForConnectionPermissionDenied: Could not update secrets for the Connection.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/updateSecrets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "secrets": secrets,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "secrets": Dict[SecretName, PlaintextValue],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "SecretNamesDoNotExist": connectivity_errors.SecretNamesDoNotExist,
                    "UpdateSecretsForConnectionPermissionDenied": connectivity_errors.UpdateSecretsForConnectionPermissionDenied,
                },
            ),
        )
