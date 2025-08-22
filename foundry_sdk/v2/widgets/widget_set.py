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
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.widgets import errors as widgets_errors
from foundry_sdk.v2.widgets import models as widgets_models


class WidgetSetClient:
    """
    The API client for the WidgetSet Resource.

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

        self.with_streaming_response = _WidgetSetClientStreaming(self)
        self.with_raw_response = _WidgetSetClientRaw(self)

    @cached_property
    def Release(self):
        from foundry_sdk.v2.widgets.release import ReleaseClient

        return ReleaseClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        widget_set_rid: widgets_models.WidgetSetRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.WidgetSet:
        """
        Get the WidgetSet with the specified rid.
        :param widget_set_rid: A Resource Identifier (RID) identifying a widget set.
        :type widget_set_rid: WidgetSetRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.WidgetSet

        :raises WidgetSetNotFound: The given WidgetSet could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/widgets/widgetSets/{widgetSetRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "widgetSetRid": widget_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.WidgetSet,
                request_timeout=request_timeout,
                throwable_errors={
                    "WidgetSetNotFound": widgets_errors.WidgetSetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _WidgetSetClientRaw:
    def __init__(self, client: WidgetSetClient) -> None:
        def get(_: widgets_models.WidgetSet): ...

        self.get = core.with_raw_response(get, client.get)


class _WidgetSetClientStreaming:
    def __init__(self, client: WidgetSetClient) -> None:
        def get(_: widgets_models.WidgetSet): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncWidgetSetClient:
    """
    The API client for the WidgetSet Resource.

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

        self.with_streaming_response = _AsyncWidgetSetClientStreaming(self)
        self.with_raw_response = _AsyncWidgetSetClientRaw(self)

    @cached_property
    def Release(self):
        from foundry_sdk.v2.widgets.release import AsyncReleaseClient

        return AsyncReleaseClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        widget_set_rid: widgets_models.WidgetSetRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.WidgetSet]:
        """
        Get the WidgetSet with the specified rid.
        :param widget_set_rid: A Resource Identifier (RID) identifying a widget set.
        :type widget_set_rid: WidgetSetRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.WidgetSet]

        :raises WidgetSetNotFound: The given WidgetSet could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/widgets/widgetSets/{widgetSetRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "widgetSetRid": widget_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.WidgetSet,
                request_timeout=request_timeout,
                throwable_errors={
                    "WidgetSetNotFound": widgets_errors.WidgetSetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncWidgetSetClientRaw:
    def __init__(self, client: AsyncWidgetSetClient) -> None:
        def get(_: widgets_models.WidgetSet): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncWidgetSetClientStreaming:
    def __init__(self, client: AsyncWidgetSetClient) -> None:
        def get(_: widgets_models.WidgetSet): ...

        self.get = core.async_with_streaming_response(get, client.get)
