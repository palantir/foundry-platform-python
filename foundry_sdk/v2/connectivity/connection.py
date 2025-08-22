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
from functools import cached_property

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.connectivity import errors as connectivity_errors
from foundry_sdk.v2.connectivity import models as connectivity_models
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.filesystem import errors as filesystem_errors
from foundry_sdk.v2.filesystem import models as filesystem_models


class ConnectionClient:
    """
    The API client for the Connection Resource.

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

        self.with_streaming_response = _ConnectionClientStreaming(self)
        self.with_raw_response = _ConnectionClientRaw(self)

    @cached_property
    def FileImport(self):
        from foundry_sdk.v2.connectivity.file_import import FileImportClient

        return FileImportClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def TableImport(self):
        from foundry_sdk.v2.connectivity.table_import import TableImportClient

        return TableImportClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        configuration: connectivity_models.CreateConnectionRequestConnectionConfiguration,
        display_name: connectivity_models.ConnectionDisplayName,
        parent_folder_rid: filesystem_models.FolderRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> connectivity_models.Connection:
        """
        Creates a new Connection with a [direct connection](https://palantir.com/docs/foundry/data-connection/core-concepts/#direct-connection) runtime.

        Any secrets specified in the request body are transmitted over the network encrypted using TLS. Once the
        secrets reach Foundry's servers, they will be temporarily decrypted and remain in plaintext in memory to
        be processed as needed. They will stay in plaintext in memory until the garbage collection process cleans
        up the memory. The secrets are always stored encrypted on our servers.
        By using this endpoint, you acknowledge and accept any potential risks associated with the temporary
        in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should
        use the Foundry UI instead.

        :param configuration:
        :type configuration: CreateConnectionRequestConnectionConfiguration
        :param display_name: The display name of the Connection. The display name must not be blank.
        :type display_name: ConnectionDisplayName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: connectivity_models.Connection

        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises CreateConnectionPermissionDenied: Could not create the Connection.
        :raises FolderNotFound: The given Folder could not be found.
        :raises ParentFolderNotFoundForConnection: The parent folder for the specified connection could not be found.
        :raises PropertyCannotBeBlank: The specified property cannot be blank.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                    "configuration": configuration,
                    "displayName": display_name,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": filesystem_models.FolderRid,
                        "configuration": connectivity_models.CreateConnectionRequestConnectionConfiguration,
                        "displayName": connectivity_models.ConnectionDisplayName,
                    },
                ),
                response_type=connectivity_models.Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "CreateConnectionPermissionDenied": connectivity_errors.CreateConnectionPermissionDenied,
                    "FolderNotFound": filesystem_errors.FolderNotFound,
                    "ParentFolderNotFoundForConnection": connectivity_errors.ParentFolderNotFoundForConnection,
                    "PropertyCannotBeBlank": connectivity_errors.PropertyCannotBeBlank,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> connectivity_models.Connection:
        """
        Get the Connection with the specified rid.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: connectivity_models.Connection

        :raises ConnectionNotFound: The given Connection could not be found.
        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises ParentFolderNotFoundForConnection: The parent folder for the specified connection could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=connectivity_models.Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "ParentFolderNotFoundForConnection": connectivity_errors.ParentFolderNotFoundForConnection,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_configuration(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> connectivity_models.ConnectionConfiguration:
        """
        Retrieves the ConnectionConfiguration of the [Connection](https://palantir.com/docs/foundry/data-connection/set-up-source/) itself.
        This operation is intended for use when other Connection data is not required, providing a lighter-weight alternative to `getConnection` operation.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: connectivity_models.ConnectionConfiguration

        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises GetConfigurationPermissionDenied: Could not getConfiguration the Connection.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=connectivity_models.ConnectionConfiguration,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "GetConfigurationPermissionDenied": connectivity_errors.GetConfigurationPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def update_export_settings(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        export_settings: connectivity_models.ConnectionExportSettings,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Updates the [export settings on the Connection.](https://palantir.com/docs/foundry/data-connection/export-overview/#enable-exports-for-source)
        Only users with Information Security Officer role can modify the export settings.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param export_settings:
        :type export_settings: ConnectionExportSettings
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises UpdateExportSettingsForConnectionPermissionDenied: Could not updateExportSettings the Connection.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/updateExportSettings",
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
                    "exportSettings": export_settings,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "exportSettings": connectivity_models.ConnectionExportSettings,
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "UpdateExportSettingsForConnectionPermissionDenied": connectivity_errors.UpdateExportSettingsForConnectionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def update_secrets(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        secrets: typing.Dict[connectivity_models.SecretName, connectivity_models.PlaintextValue],
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
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

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param secrets: The secrets to be updated. The specified secret names must already be configured on the connection.
        :type secrets: Dict[SecretName, PlaintextValue]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises ConnectionNotFound: The given Connection could not be found.
        :raises SecretNamesDoNotExist: The secret names provided do not exist on the connection.
        :raises UpdateSecretsForConnectionPermissionDenied: Could not update secrets for the Connection.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/updateSecrets",
                query_params={},
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "secrets": secrets,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "secrets": typing.Dict[
                            connectivity_models.SecretName, connectivity_models.PlaintextValue
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "SecretNamesDoNotExist": connectivity_errors.SecretNamesDoNotExist,
                    "UpdateSecretsForConnectionPermissionDenied": connectivity_errors.UpdateSecretsForConnectionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload_custom_jdbc_drivers(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        body: bytes,
        *,
        file_name: str,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> connectivity_models.Connection:
        """
        Upload custom jdbc drivers to an existing JDBC connection.
        The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param body: Body of the request
        :type body: bytes
        :param file_name: The file name of the uploaded JDBC driver. Must end with .jar
        :type file_name: str
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: connectivity_models.Connection

        :raises ConnectionNotFound: The given Connection could not be found.
        :raises UploadCustomJdbcDriversConnectionPermissionDenied: Could not uploadCustomJdbcDrivers the Connection.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/uploadCustomJdbcDrivers",
                query_params={
                    "fileName": file_name,
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=connectivity_models.Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "UploadCustomJdbcDriversConnectionPermissionDenied": connectivity_errors.UploadCustomJdbcDriversConnectionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ConnectionClientRaw:
    def __init__(self, client: ConnectionClient) -> None:
        def create(_: connectivity_models.Connection): ...
        def get(_: connectivity_models.Connection): ...
        def get_configuration(_: connectivity_models.ConnectionConfiguration): ...
        def update_export_settings(_: None): ...
        def update_secrets(_: None): ...
        def upload_custom_jdbc_drivers(_: connectivity_models.Connection): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.get_configuration = core.with_raw_response(get_configuration, client.get_configuration)
        self.update_export_settings = core.with_raw_response(
            update_export_settings, client.update_export_settings
        )
        self.update_secrets = core.with_raw_response(update_secrets, client.update_secrets)
        self.upload_custom_jdbc_drivers = core.with_raw_response(
            upload_custom_jdbc_drivers, client.upload_custom_jdbc_drivers
        )


class _ConnectionClientStreaming:
    def __init__(self, client: ConnectionClient) -> None:
        def create(_: connectivity_models.Connection): ...
        def get(_: connectivity_models.Connection): ...
        def get_configuration(_: connectivity_models.ConnectionConfiguration): ...
        def upload_custom_jdbc_drivers(_: connectivity_models.Connection): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.get_configuration = core.with_streaming_response(
            get_configuration, client.get_configuration
        )
        self.upload_custom_jdbc_drivers = core.with_streaming_response(
            upload_custom_jdbc_drivers, client.upload_custom_jdbc_drivers
        )


class AsyncConnectionClient:
    """
    The API client for the Connection Resource.

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

        self.with_streaming_response = _AsyncConnectionClientStreaming(self)
        self.with_raw_response = _AsyncConnectionClientRaw(self)

    @cached_property
    def FileImport(self):
        from foundry_sdk.v2.connectivity.file_import import AsyncFileImportClient

        return AsyncFileImportClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def TableImport(self):
        from foundry_sdk.v2.connectivity.table_import import AsyncTableImportClient

        return AsyncTableImportClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        configuration: connectivity_models.CreateConnectionRequestConnectionConfiguration,
        display_name: connectivity_models.ConnectionDisplayName,
        parent_folder_rid: filesystem_models.FolderRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[connectivity_models.Connection]:
        """
        Creates a new Connection with a [direct connection](https://palantir.com/docs/foundry/data-connection/core-concepts/#direct-connection) runtime.

        Any secrets specified in the request body are transmitted over the network encrypted using TLS. Once the
        secrets reach Foundry's servers, they will be temporarily decrypted and remain in plaintext in memory to
        be processed as needed. They will stay in plaintext in memory until the garbage collection process cleans
        up the memory. The secrets are always stored encrypted on our servers.
        By using this endpoint, you acknowledge and accept any potential risks associated with the temporary
        in-memory handling of secrets. If you do not want your secrets to be temporarily decrypted, you should
        use the Foundry UI instead.

        :param configuration:
        :type configuration: CreateConnectionRequestConnectionConfiguration
        :param display_name: The display name of the Connection. The display name must not be blank.
        :type display_name: ConnectionDisplayName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[connectivity_models.Connection]

        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises CreateConnectionPermissionDenied: Could not create the Connection.
        :raises FolderNotFound: The given Folder could not be found.
        :raises ParentFolderNotFoundForConnection: The parent folder for the specified connection could not be found.
        :raises PropertyCannotBeBlank: The specified property cannot be blank.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                    "configuration": configuration,
                    "displayName": display_name,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": filesystem_models.FolderRid,
                        "configuration": connectivity_models.CreateConnectionRequestConnectionConfiguration,
                        "displayName": connectivity_models.ConnectionDisplayName,
                    },
                ),
                response_type=connectivity_models.Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "CreateConnectionPermissionDenied": connectivity_errors.CreateConnectionPermissionDenied,
                    "FolderNotFound": filesystem_errors.FolderNotFound,
                    "ParentFolderNotFoundForConnection": connectivity_errors.ParentFolderNotFoundForConnection,
                    "PropertyCannotBeBlank": connectivity_errors.PropertyCannotBeBlank,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[connectivity_models.Connection]:
        """
        Get the Connection with the specified rid.
        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[connectivity_models.Connection]

        :raises ConnectionNotFound: The given Connection could not be found.
        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises ParentFolderNotFoundForConnection: The parent folder for the specified connection could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=connectivity_models.Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "ParentFolderNotFoundForConnection": connectivity_errors.ParentFolderNotFoundForConnection,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_configuration(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[connectivity_models.ConnectionConfiguration]:
        """
        Retrieves the ConnectionConfiguration of the [Connection](https://palantir.com/docs/foundry/data-connection/set-up-source/) itself.
        This operation is intended for use when other Connection data is not required, providing a lighter-weight alternative to `getConnection` operation.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[connectivity_models.ConnectionConfiguration]

        :raises ConnectionTypeNotSupported: The specified connection is not yet supported in the Platform API.
        :raises GetConfigurationPermissionDenied: Could not getConfiguration the Connection.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=connectivity_models.ConnectionConfiguration,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionTypeNotSupported": connectivity_errors.ConnectionTypeNotSupported,
                    "GetConfigurationPermissionDenied": connectivity_errors.GetConfigurationPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def update_export_settings(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        export_settings: connectivity_models.ConnectionExportSettings,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Updates the [export settings on the Connection.](https://palantir.com/docs/foundry/data-connection/export-overview/#enable-exports-for-source)
        Only users with Information Security Officer role can modify the export settings.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param export_settings:
        :type export_settings: ConnectionExportSettings
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises UpdateExportSettingsForConnectionPermissionDenied: Could not updateExportSettings the Connection.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/updateExportSettings",
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
                    "exportSettings": export_settings,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "exportSettings": connectivity_models.ConnectionExportSettings,
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "UpdateExportSettingsForConnectionPermissionDenied": connectivity_errors.UpdateExportSettingsForConnectionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def update_secrets(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        *,
        secrets: typing.Dict[connectivity_models.SecretName, connectivity_models.PlaintextValue],
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
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

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param secrets: The secrets to be updated. The specified secret names must already be configured on the connection.
        :type secrets: Dict[SecretName, PlaintextValue]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises ConnectionNotFound: The given Connection could not be found.
        :raises SecretNamesDoNotExist: The secret names provided do not exist on the connection.
        :raises UpdateSecretsForConnectionPermissionDenied: Could not update secrets for the Connection.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/updateSecrets",
                query_params={},
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "secrets": secrets,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "secrets": typing.Dict[
                            connectivity_models.SecretName, connectivity_models.PlaintextValue
                        ],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "SecretNamesDoNotExist": connectivity_errors.SecretNamesDoNotExist,
                    "UpdateSecretsForConnectionPermissionDenied": connectivity_errors.UpdateSecretsForConnectionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload_custom_jdbc_drivers(
        self,
        connection_rid: connectivity_models.ConnectionRid,
        body: bytes,
        *,
        file_name: str,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[connectivity_models.Connection]:
        """
        Upload custom jdbc drivers to an existing JDBC connection.
        The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

        :param connection_rid:
        :type connection_rid: ConnectionRid
        :param body: Body of the request
        :type body: bytes
        :param file_name: The file name of the uploaded JDBC driver. Must end with .jar
        :type file_name: str
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[connectivity_models.Connection]

        :raises ConnectionNotFound: The given Connection could not be found.
        :raises UploadCustomJdbcDriversConnectionPermissionDenied: Could not uploadCustomJdbcDrivers the Connection.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/connections/{connectionRid}/uploadCustomJdbcDrivers",
                query_params={
                    "fileName": file_name,
                    "preview": preview,
                },
                path_params={
                    "connectionRid": connection_rid,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=connectivity_models.Connection,
                request_timeout=request_timeout,
                throwable_errors={
                    "ConnectionNotFound": connectivity_errors.ConnectionNotFound,
                    "UploadCustomJdbcDriversConnectionPermissionDenied": connectivity_errors.UploadCustomJdbcDriversConnectionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncConnectionClientRaw:
    def __init__(self, client: AsyncConnectionClient) -> None:
        def create(_: connectivity_models.Connection): ...
        def get(_: connectivity_models.Connection): ...
        def get_configuration(_: connectivity_models.ConnectionConfiguration): ...
        def update_export_settings(_: None): ...
        def update_secrets(_: None): ...
        def upload_custom_jdbc_drivers(_: connectivity_models.Connection): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_configuration = core.async_with_raw_response(
            get_configuration, client.get_configuration
        )
        self.update_export_settings = core.async_with_raw_response(
            update_export_settings, client.update_export_settings
        )
        self.update_secrets = core.async_with_raw_response(update_secrets, client.update_secrets)
        self.upload_custom_jdbc_drivers = core.async_with_raw_response(
            upload_custom_jdbc_drivers, client.upload_custom_jdbc_drivers
        )


class _AsyncConnectionClientStreaming:
    def __init__(self, client: AsyncConnectionClient) -> None:
        def create(_: connectivity_models.Connection): ...
        def get(_: connectivity_models.Connection): ...
        def get_configuration(_: connectivity_models.ConnectionConfiguration): ...
        def upload_custom_jdbc_drivers(_: connectivity_models.Connection): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_configuration = core.async_with_streaming_response(
            get_configuration, client.get_configuration
        )
        self.upload_custom_jdbc_drivers = core.async_with_streaming_response(
            upload_custom_jdbc_drivers, client.upload_custom_jdbc_drivers
        )
