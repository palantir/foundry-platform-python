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
from foundry_sdk.v2.third_party_applications import (
    errors as third_party_applications_errors,
)  # NOQA
from foundry_sdk.v2.third_party_applications import (
    models as third_party_applications_models,
)  # NOQA


class ThirdPartyApplicationClient:
    """
    The API client for the ThirdPartyApplication Resource.

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

        self.with_streaming_response = _ThirdPartyApplicationClientStreaming(self)
        self.with_raw_response = _ThirdPartyApplicationClientRaw(self)

    @cached_property
    def Website(self):
        from foundry_sdk.v2.third_party_applications.website import WebsiteClient

        return WebsiteClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> third_party_applications_models.ThirdPartyApplication:
        """
        Get the ThirdPartyApplication with the specified rid.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: third_party_applications_models.ThirdPartyApplication

        :raises ThirdPartyApplicationNotFound: The given ThirdPartyApplication could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=third_party_applications_models.ThirdPartyApplication,
                request_timeout=request_timeout,
                throwable_errors={
                    "ThirdPartyApplicationNotFound": third_party_applications_errors.ThirdPartyApplicationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ThirdPartyApplicationClientRaw:
    def __init__(self, client: ThirdPartyApplicationClient) -> None:
        def get(_: third_party_applications_models.ThirdPartyApplication): ...

        self.get = core.with_raw_response(get, client.get)


class _ThirdPartyApplicationClientStreaming:
    def __init__(self, client: ThirdPartyApplicationClient) -> None:
        def get(_: third_party_applications_models.ThirdPartyApplication): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncThirdPartyApplicationClient:
    """
    The API client for the ThirdPartyApplication Resource.

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

        self.with_streaming_response = _AsyncThirdPartyApplicationClientStreaming(self)
        self.with_raw_response = _AsyncThirdPartyApplicationClientRaw(self)

    @cached_property
    def Website(self):
        from foundry_sdk.v2.third_party_applications.website import AsyncWebsiteClient

        return AsyncWebsiteClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[third_party_applications_models.ThirdPartyApplication]:
        """
        Get the ThirdPartyApplication with the specified rid.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[third_party_applications_models.ThirdPartyApplication]

        :raises ThirdPartyApplicationNotFound: The given ThirdPartyApplication could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=third_party_applications_models.ThirdPartyApplication,
                request_timeout=request_timeout,
                throwable_errors={
                    "ThirdPartyApplicationNotFound": third_party_applications_errors.ThirdPartyApplicationNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncThirdPartyApplicationClientRaw:
    def __init__(self, client: AsyncThirdPartyApplicationClient) -> None:
        def get(_: third_party_applications_models.ThirdPartyApplication): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncThirdPartyApplicationClientStreaming:
    def __init__(self, client: AsyncThirdPartyApplicationClient) -> None:
        def get(_: third_party_applications_models.ThirdPartyApplication): ...

        self.get = core.async_with_streaming_response(get, client.get)
