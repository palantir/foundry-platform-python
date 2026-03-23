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
from foundry_sdk.v2.admin import errors as admin_errors
from foundry_sdk.v2.admin import models as admin_models
from foundry_sdk.v2.core import models as core_models


class CbacBannerClient:
    """
    The API client for the CbacBanner Resource.

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

        self.with_streaming_response = _CbacBannerClientStreaming(self)
        self.with_raw_response = _CbacBannerClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        *,
        display_type: typing.Optional[admin_models.ClassificationBannerDisplayType] = None,
        marking_ids: typing.Optional[typing.List[core_models.MarkingId]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.CbacBanner:
        """
        Returns a classification banner string and colors for the given set of marking IDs.
        :param display_type: The display type of the banner. Defaults to PORTION_MARKING.
        :type display_type: Optional[ClassificationBannerDisplayType]
        :param marking_ids: The marking IDs for which to generate a banner.
        :type marking_ids: Optional[List[MarkingId]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.CbacBanner

        :raises CbacBannerNotFound: The given CbacBanner could not be found.
        :raises CbacUnavailable: CBAC is not available.
        :raises GetCbacBannerPermissionDenied: The provided token does not have permission to get the CBAC banner for the markings.
        :raises UnknownClassificationBannerDisplayType: The provided classification banner display type is not recognized.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/cbacBanner",
                query_params={
                    "displayType": display_type,
                    "markingIds": marking_ids,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=admin_models.CbacBanner,
                request_timeout=request_timeout,
                throwable_errors={
                    "CbacBannerNotFound": admin_errors.CbacBannerNotFound,
                    "CbacUnavailable": admin_errors.CbacUnavailable,
                    "GetCbacBannerPermissionDenied": admin_errors.GetCbacBannerPermissionDenied,
                    "UnknownClassificationBannerDisplayType": admin_errors.UnknownClassificationBannerDisplayType,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _CbacBannerClientRaw:
    def __init__(self, client: CbacBannerClient) -> None:
        def get(_: admin_models.CbacBanner): ...

        self.get = core.with_raw_response(get, client.get)


class _CbacBannerClientStreaming:
    def __init__(self, client: CbacBannerClient) -> None:
        def get(_: admin_models.CbacBanner): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncCbacBannerClient:
    """
    The API client for the CbacBanner Resource.

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

        self.with_streaming_response = _AsyncCbacBannerClientStreaming(self)
        self.with_raw_response = _AsyncCbacBannerClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        *,
        display_type: typing.Optional[admin_models.ClassificationBannerDisplayType] = None,
        marking_ids: typing.Optional[typing.List[core_models.MarkingId]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.CbacBanner]:
        """
        Returns a classification banner string and colors for the given set of marking IDs.
        :param display_type: The display type of the banner. Defaults to PORTION_MARKING.
        :type display_type: Optional[ClassificationBannerDisplayType]
        :param marking_ids: The marking IDs for which to generate a banner.
        :type marking_ids: Optional[List[MarkingId]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.CbacBanner]

        :raises CbacBannerNotFound: The given CbacBanner could not be found.
        :raises CbacUnavailable: CBAC is not available.
        :raises GetCbacBannerPermissionDenied: The provided token does not have permission to get the CBAC banner for the markings.
        :raises UnknownClassificationBannerDisplayType: The provided classification banner display type is not recognized.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/cbacBanner",
                query_params={
                    "displayType": display_type,
                    "markingIds": marking_ids,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=admin_models.CbacBanner,
                request_timeout=request_timeout,
                throwable_errors={
                    "CbacBannerNotFound": admin_errors.CbacBannerNotFound,
                    "CbacUnavailable": admin_errors.CbacUnavailable,
                    "GetCbacBannerPermissionDenied": admin_errors.GetCbacBannerPermissionDenied,
                    "UnknownClassificationBannerDisplayType": admin_errors.UnknownClassificationBannerDisplayType,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncCbacBannerClientRaw:
    def __init__(self, client: AsyncCbacBannerClient) -> None:
        def get(_: admin_models.CbacBanner): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncCbacBannerClientStreaming:
    def __init__(self, client: AsyncCbacBannerClient) -> None:
        def get(_: admin_models.CbacBanner): ...

        self.get = core.async_with_streaming_response(get, client.get)
