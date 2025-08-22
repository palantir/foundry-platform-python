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


class DevModeSettingsClient:
    """
    The API client for the DevModeSettings Resource.

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

        self.with_streaming_response = _DevModeSettingsClientStreaming(self)
        self.with_raw_response = _DevModeSettingsClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def disable(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.DevModeSettings:
        """
        Disable dev mode for the user associated with the provided token.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.DevModeSettings

        :raises DisableDevModeSettingsPermissionDenied: Could not disable the DevModeSettings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettings/disable",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "DisableDevModeSettingsPermissionDenied": widgets_errors.DisableDevModeSettingsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def enable(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.DevModeSettings:
        """
        Enable dev mode for the user associated with the provided token.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.DevModeSettings

        :raises EnableDevModeSettingsPermissionDenied: Could not enable the DevModeSettings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettings/enable",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnableDevModeSettingsPermissionDenied": widgets_errors.EnableDevModeSettingsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.DevModeSettings:
        """
        Get the dev mode settings for the user associated with the provided token.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.DevModeSettings

        :raises DevModeSettingsNotFound: The given DevModeSettings could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/widgets/devModeSettings",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "DevModeSettingsNotFound": widgets_errors.DevModeSettingsNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def pause(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.DevModeSettings:
        """
        Pause dev mode for the user associated with the provided token.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.DevModeSettings

        :raises PauseDevModeSettingsPermissionDenied: Could not pause the DevModeSettings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettings/pause",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "PauseDevModeSettingsPermissionDenied": widgets_errors.PauseDevModeSettingsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def set_widget_set(
        self,
        *,
        settings: widgets_models.WidgetSetDevModeSettings,
        widget_set_rid: widgets_models.WidgetSetRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.DevModeSettings:
        """
        Set the dev mode settings for the given widget set for the user associated with the provided token.
        :param settings:
        :type settings: WidgetSetDevModeSettings
        :param widget_set_rid:
        :type widget_set_rid: WidgetSetRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.DevModeSettings

        :raises SetWidgetSetDevModeSettingsPermissionDenied: Could not setWidgetSet the DevModeSettings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettings/setWidgetSet",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "widgetSetRid": widget_set_rid,
                    "settings": settings,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "widgetSetRid": widgets_models.WidgetSetRid,
                        "settings": widgets_models.WidgetSetDevModeSettings,
                    },
                ),
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "SetWidgetSetDevModeSettingsPermissionDenied": widgets_errors.SetWidgetSetDevModeSettingsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def set_widget_set_by_id(
        self,
        *,
        settings: widgets_models.WidgetSetDevModeSettingsById,
        widget_set_rid: widgets_models.WidgetSetRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.DevModeSettings:
        """
        Set the dev mode settings for the given widget set for the user associated with the
        provided token. Uses widget IDs to identify widgets within the set.

        :param settings:
        :type settings: WidgetSetDevModeSettingsById
        :param widget_set_rid:
        :type widget_set_rid: WidgetSetRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.DevModeSettings

        :raises SetWidgetSetDevModeSettingsByIdPermissionDenied: Could not setWidgetSetById the DevModeSettings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettings/setWidgetSetById",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "widgetSetRid": widget_set_rid,
                    "settings": settings,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "widgetSetRid": widgets_models.WidgetSetRid,
                        "settings": widgets_models.WidgetSetDevModeSettingsById,
                    },
                ),
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "SetWidgetSetDevModeSettingsByIdPermissionDenied": widgets_errors.SetWidgetSetDevModeSettingsByIdPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _DevModeSettingsClientRaw:
    def __init__(self, client: DevModeSettingsClient) -> None:
        def disable(_: widgets_models.DevModeSettings): ...
        def enable(_: widgets_models.DevModeSettings): ...
        def get(_: widgets_models.DevModeSettings): ...
        def pause(_: widgets_models.DevModeSettings): ...
        def set_widget_set(_: widgets_models.DevModeSettings): ...
        def set_widget_set_by_id(_: widgets_models.DevModeSettings): ...

        self.disable = core.with_raw_response(disable, client.disable)
        self.enable = core.with_raw_response(enable, client.enable)
        self.get = core.with_raw_response(get, client.get)
        self.pause = core.with_raw_response(pause, client.pause)
        self.set_widget_set = core.with_raw_response(set_widget_set, client.set_widget_set)
        self.set_widget_set_by_id = core.with_raw_response(
            set_widget_set_by_id, client.set_widget_set_by_id
        )


class _DevModeSettingsClientStreaming:
    def __init__(self, client: DevModeSettingsClient) -> None:
        def disable(_: widgets_models.DevModeSettings): ...
        def enable(_: widgets_models.DevModeSettings): ...
        def get(_: widgets_models.DevModeSettings): ...
        def pause(_: widgets_models.DevModeSettings): ...
        def set_widget_set(_: widgets_models.DevModeSettings): ...
        def set_widget_set_by_id(_: widgets_models.DevModeSettings): ...

        self.disable = core.with_streaming_response(disable, client.disable)
        self.enable = core.with_streaming_response(enable, client.enable)
        self.get = core.with_streaming_response(get, client.get)
        self.pause = core.with_streaming_response(pause, client.pause)
        self.set_widget_set = core.with_streaming_response(set_widget_set, client.set_widget_set)
        self.set_widget_set_by_id = core.with_streaming_response(
            set_widget_set_by_id, client.set_widget_set_by_id
        )


class AsyncDevModeSettingsClient:
    """
    The API client for the DevModeSettings Resource.

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

        self.with_streaming_response = _AsyncDevModeSettingsClientStreaming(self)
        self.with_raw_response = _AsyncDevModeSettingsClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def disable(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.DevModeSettings]:
        """
        Disable dev mode for the user associated with the provided token.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.DevModeSettings]

        :raises DisableDevModeSettingsPermissionDenied: Could not disable the DevModeSettings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettings/disable",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "DisableDevModeSettingsPermissionDenied": widgets_errors.DisableDevModeSettingsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def enable(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.DevModeSettings]:
        """
        Enable dev mode for the user associated with the provided token.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.DevModeSettings]

        :raises EnableDevModeSettingsPermissionDenied: Could not enable the DevModeSettings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettings/enable",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnableDevModeSettingsPermissionDenied": widgets_errors.EnableDevModeSettingsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.DevModeSettings]:
        """
        Get the dev mode settings for the user associated with the provided token.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.DevModeSettings]

        :raises DevModeSettingsNotFound: The given DevModeSettings could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/widgets/devModeSettings",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "DevModeSettingsNotFound": widgets_errors.DevModeSettingsNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def pause(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.DevModeSettings]:
        """
        Pause dev mode for the user associated with the provided token.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.DevModeSettings]

        :raises PauseDevModeSettingsPermissionDenied: Could not pause the DevModeSettings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettings/pause",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "PauseDevModeSettingsPermissionDenied": widgets_errors.PauseDevModeSettingsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def set_widget_set(
        self,
        *,
        settings: widgets_models.WidgetSetDevModeSettings,
        widget_set_rid: widgets_models.WidgetSetRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.DevModeSettings]:
        """
        Set the dev mode settings for the given widget set for the user associated with the provided token.
        :param settings:
        :type settings: WidgetSetDevModeSettings
        :param widget_set_rid:
        :type widget_set_rid: WidgetSetRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.DevModeSettings]

        :raises SetWidgetSetDevModeSettingsPermissionDenied: Could not setWidgetSet the DevModeSettings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettings/setWidgetSet",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "widgetSetRid": widget_set_rid,
                    "settings": settings,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "widgetSetRid": widgets_models.WidgetSetRid,
                        "settings": widgets_models.WidgetSetDevModeSettings,
                    },
                ),
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "SetWidgetSetDevModeSettingsPermissionDenied": widgets_errors.SetWidgetSetDevModeSettingsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def set_widget_set_by_id(
        self,
        *,
        settings: widgets_models.WidgetSetDevModeSettingsById,
        widget_set_rid: widgets_models.WidgetSetRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.DevModeSettings]:
        """
        Set the dev mode settings for the given widget set for the user associated with the
        provided token. Uses widget IDs to identify widgets within the set.

        :param settings:
        :type settings: WidgetSetDevModeSettingsById
        :param widget_set_rid:
        :type widget_set_rid: WidgetSetRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.DevModeSettings]

        :raises SetWidgetSetDevModeSettingsByIdPermissionDenied: Could not setWidgetSetById the DevModeSettings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/devModeSettings/setWidgetSetById",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "widgetSetRid": widget_set_rid,
                    "settings": settings,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "widgetSetRid": widgets_models.WidgetSetRid,
                        "settings": widgets_models.WidgetSetDevModeSettingsById,
                    },
                ),
                response_type=widgets_models.DevModeSettings,
                request_timeout=request_timeout,
                throwable_errors={
                    "SetWidgetSetDevModeSettingsByIdPermissionDenied": widgets_errors.SetWidgetSetDevModeSettingsByIdPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncDevModeSettingsClientRaw:
    def __init__(self, client: AsyncDevModeSettingsClient) -> None:
        def disable(_: widgets_models.DevModeSettings): ...
        def enable(_: widgets_models.DevModeSettings): ...
        def get(_: widgets_models.DevModeSettings): ...
        def pause(_: widgets_models.DevModeSettings): ...
        def set_widget_set(_: widgets_models.DevModeSettings): ...
        def set_widget_set_by_id(_: widgets_models.DevModeSettings): ...

        self.disable = core.async_with_raw_response(disable, client.disable)
        self.enable = core.async_with_raw_response(enable, client.enable)
        self.get = core.async_with_raw_response(get, client.get)
        self.pause = core.async_with_raw_response(pause, client.pause)
        self.set_widget_set = core.async_with_raw_response(set_widget_set, client.set_widget_set)
        self.set_widget_set_by_id = core.async_with_raw_response(
            set_widget_set_by_id, client.set_widget_set_by_id
        )


class _AsyncDevModeSettingsClientStreaming:
    def __init__(self, client: AsyncDevModeSettingsClient) -> None:
        def disable(_: widgets_models.DevModeSettings): ...
        def enable(_: widgets_models.DevModeSettings): ...
        def get(_: widgets_models.DevModeSettings): ...
        def pause(_: widgets_models.DevModeSettings): ...
        def set_widget_set(_: widgets_models.DevModeSettings): ...
        def set_widget_set_by_id(_: widgets_models.DevModeSettings): ...

        self.disable = core.async_with_streaming_response(disable, client.disable)
        self.enable = core.async_with_streaming_response(enable, client.enable)
        self.get = core.async_with_streaming_response(get, client.get)
        self.pause = core.async_with_streaming_response(pause, client.pause)
        self.set_widget_set = core.async_with_streaming_response(
            set_widget_set, client.set_widget_set
        )
        self.set_widget_set_by_id = core.async_with_streaming_response(
            set_widget_set_by_id, client.set_widget_set_by_id
        )
