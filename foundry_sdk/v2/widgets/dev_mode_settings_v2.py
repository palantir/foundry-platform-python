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
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.widgets import errors as widgets_errors
from foundry_sdk.v2.widgets import models as widgets_models


class DevModeSettingsV2Client:
    """
    The API client for the DevModeSettingsV2 Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _DevModeSettingsV2ClientStreaming(self)
        self.with_raw_response = _DevModeSettingsV2ClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def enable(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.DevModeSettingsV2:
        """
        Enable dev mode for the user associated with the provided token.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.DevModeSettingsV2

        :raises EnableDevModeSettingsV2PermissionDenied: Could not enable the DevModeSettingsV2.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettingsV2/enable",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=widgets_models.DevModeSettingsV2,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnableDevModeSettingsV2PermissionDenied": widgets_errors.EnableDevModeSettingsV2PermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def set_widget_set_manifest(
        self,
        *,
        manifest: typing.Any,
        widget_set_rid: widgets_models.WidgetSetRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.DevModeSettingsV2:
        """
        Set the dev mode settings for the given widget set using the manifest format.
        The request body is a dev settings manifest JSON object with the following
        structure:

          {
            "manifestVersion": "1.0.0",
            "devSettings": {
              "baseHref": "...",
              "widgets": { ... },
              "inputSpec": { ... }
            }
          }

        See https://github.com/palantir/osdk-ts for the widget library API types for the
        dev settings manifest.

        :param manifest:
        :type manifest: Any
        :param widget_set_rid:
        :type widget_set_rid: WidgetSetRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.DevModeSettingsV2

        :raises InvalidDevModeBaseHref: The base href in the dev mode settings is invalid. It must be a valid localhost URL with an optional port.
        :raises InvalidDevModeEntrypointCssCount: The dev mode settings contains too many CSS entrypoints. You must limit the number of CSS entrypoints to the maximum allowed.
        :raises InvalidDevModeEntrypointJsCount: The dev mode settings contains too many JavaScript entrypoints. You must limit the number of JavaScript entrypoints to the maximum allowed.
        :raises InvalidDevModeFilePath: The dev mode settings contains an invalid entrypoint file path. The file path must be a valid localhost URL with an optional port and a file path.
        :raises InvalidDevModeWidgetSettingsCount: The dev mode settings contains too many widget settings. You must limit the number of widget settings to the maximum allowed.
        :raises InvalidManifest: The provided manifest could not be parsed or is not well formed.
        :raises SetWidgetSetManifestDevModeSettingsV2PermissionDenied: Could not setWidgetSetManifest the DevModeSettingsV2.
        :raises WidgetIdNotFound: A non-existent widget id was provided. If creating a new widget, you must first publish your changes before previewing with developer mode.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettingsV2/setWidgetSetManifest",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=widgets_models.SetWidgetSetManifestDevModeSettingsV2Request(
                    widget_set_rid=widget_set_rid,
                    manifest=manifest,
                ),
                response_type=widgets_models.DevModeSettingsV2,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidDevModeBaseHref": widgets_errors.InvalidDevModeBaseHref,
                    "InvalidDevModeEntrypointCssCount": widgets_errors.InvalidDevModeEntrypointCssCount,
                    "InvalidDevModeEntrypointJsCount": widgets_errors.InvalidDevModeEntrypointJsCount,
                    "InvalidDevModeFilePath": widgets_errors.InvalidDevModeFilePath,
                    "InvalidDevModeWidgetSettingsCount": widgets_errors.InvalidDevModeWidgetSettingsCount,
                    "InvalidManifest": widgets_errors.InvalidManifest,
                    "SetWidgetSetManifestDevModeSettingsV2PermissionDenied": widgets_errors.SetWidgetSetManifestDevModeSettingsV2PermissionDenied,
                    "WidgetIdNotFound": widgets_errors.WidgetIdNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _DevModeSettingsV2ClientRaw:
    def __init__(self, client: DevModeSettingsV2Client) -> None:
        def enable(_: widgets_models.DevModeSettingsV2): ...
        def set_widget_set_manifest(_: widgets_models.DevModeSettingsV2): ...

        self.enable = core.with_raw_response(enable, client.enable)
        self.set_widget_set_manifest = core.with_raw_response(
            set_widget_set_manifest, client.set_widget_set_manifest
        )


class _DevModeSettingsV2ClientStreaming:
    def __init__(self, client: DevModeSettingsV2Client) -> None:
        def enable(_: widgets_models.DevModeSettingsV2): ...
        def set_widget_set_manifest(_: widgets_models.DevModeSettingsV2): ...

        self.enable = core.with_streaming_response(enable, client.enable)
        self.set_widget_set_manifest = core.with_streaming_response(
            set_widget_set_manifest, client.set_widget_set_manifest
        )


class AsyncDevModeSettingsV2Client:
    """
    The API client for the DevModeSettingsV2 Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncDevModeSettingsV2ClientStreaming(self)
        self.with_raw_response = _AsyncDevModeSettingsV2ClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def enable(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.DevModeSettingsV2]:
        """
        Enable dev mode for the user associated with the provided token.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.DevModeSettingsV2]

        :raises EnableDevModeSettingsV2PermissionDenied: Could not enable the DevModeSettingsV2.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettingsV2/enable",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=widgets_models.DevModeSettingsV2,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnableDevModeSettingsV2PermissionDenied": widgets_errors.EnableDevModeSettingsV2PermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def set_widget_set_manifest(
        self,
        *,
        manifest: typing.Any,
        widget_set_rid: widgets_models.WidgetSetRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.DevModeSettingsV2]:
        """
        Set the dev mode settings for the given widget set using the manifest format.
        The request body is a dev settings manifest JSON object with the following
        structure:

          {
            "manifestVersion": "1.0.0",
            "devSettings": {
              "baseHref": "...",
              "widgets": { ... },
              "inputSpec": { ... }
            }
          }

        See https://github.com/palantir/osdk-ts for the widget library API types for the
        dev settings manifest.

        :param manifest:
        :type manifest: Any
        :param widget_set_rid:
        :type widget_set_rid: WidgetSetRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.DevModeSettingsV2]

        :raises InvalidDevModeBaseHref: The base href in the dev mode settings is invalid. It must be a valid localhost URL with an optional port.
        :raises InvalidDevModeEntrypointCssCount: The dev mode settings contains too many CSS entrypoints. You must limit the number of CSS entrypoints to the maximum allowed.
        :raises InvalidDevModeEntrypointJsCount: The dev mode settings contains too many JavaScript entrypoints. You must limit the number of JavaScript entrypoints to the maximum allowed.
        :raises InvalidDevModeFilePath: The dev mode settings contains an invalid entrypoint file path. The file path must be a valid localhost URL with an optional port and a file path.
        :raises InvalidDevModeWidgetSettingsCount: The dev mode settings contains too many widget settings. You must limit the number of widget settings to the maximum allowed.
        :raises InvalidManifest: The provided manifest could not be parsed or is not well formed.
        :raises SetWidgetSetManifestDevModeSettingsV2PermissionDenied: Could not setWidgetSetManifest the DevModeSettingsV2.
        :raises WidgetIdNotFound: A non-existent widget id was provided. If creating a new widget, you must first publish your changes before previewing with developer mode.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettingsV2/setWidgetSetManifest",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=widgets_models.SetWidgetSetManifestDevModeSettingsV2Request(
                    widget_set_rid=widget_set_rid,
                    manifest=manifest,
                ),
                response_type=widgets_models.DevModeSettingsV2,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidDevModeBaseHref": widgets_errors.InvalidDevModeBaseHref,
                    "InvalidDevModeEntrypointCssCount": widgets_errors.InvalidDevModeEntrypointCssCount,
                    "InvalidDevModeEntrypointJsCount": widgets_errors.InvalidDevModeEntrypointJsCount,
                    "InvalidDevModeFilePath": widgets_errors.InvalidDevModeFilePath,
                    "InvalidDevModeWidgetSettingsCount": widgets_errors.InvalidDevModeWidgetSettingsCount,
                    "InvalidManifest": widgets_errors.InvalidManifest,
                    "SetWidgetSetManifestDevModeSettingsV2PermissionDenied": widgets_errors.SetWidgetSetManifestDevModeSettingsV2PermissionDenied,
                    "WidgetIdNotFound": widgets_errors.WidgetIdNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncDevModeSettingsV2ClientRaw:
    def __init__(self, client: AsyncDevModeSettingsV2Client) -> None:
        def enable(_: widgets_models.DevModeSettingsV2): ...
        def set_widget_set_manifest(_: widgets_models.DevModeSettingsV2): ...

        self.enable = core.async_with_raw_response(enable, client.enable)
        self.set_widget_set_manifest = core.async_with_raw_response(
            set_widget_set_manifest, client.set_widget_set_manifest
        )


class _AsyncDevModeSettingsV2ClientStreaming:
    def __init__(self, client: AsyncDevModeSettingsV2Client) -> None:
        def enable(_: widgets_models.DevModeSettingsV2): ...
        def set_widget_set_manifest(_: widgets_models.DevModeSettingsV2): ...

        self.enable = core.async_with_streaming_response(enable, client.enable)
        self.set_widget_set_manifest = core.async_with_streaming_response(
            set_widget_set_manifest, client.set_widget_set_manifest
        )
