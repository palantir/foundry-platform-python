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


class CbacMarkingRestrictionsClient:
    """
    The API client for the CbacMarkingRestrictions Resource.

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

        self.with_streaming_response = _CbacMarkingRestrictionsClientStreaming(self)
        self.with_raw_response = _CbacMarkingRestrictionsClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        *,
        marking_ids: typing.Optional[typing.List[core_models.MarkingId]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.CbacMarkingRestrictions:
        """
        Returns disallowed, implied, and required markings for the given set of marking IDs.
        :param marking_ids: The marking IDs for which to get restrictions.
        :type marking_ids: Optional[List[MarkingId]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.CbacMarkingRestrictions

        :raises CbacMarkingRestrictionsNotFound: The given CbacMarkingRestrictions could not be found.
        :raises CbacUnavailable: CBAC is not available.
        :raises GetCbacMarkingRestrictionInfoPermissionDenied: The provided token does not have permission to get the CBAC marking restrictions for the markings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/cbacMarkingRestrictions",
                query_params={
                    "markingIds": marking_ids,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=admin_models.CbacMarkingRestrictions,
                request_timeout=request_timeout,
                throwable_errors={
                    "CbacMarkingRestrictionsNotFound": admin_errors.CbacMarkingRestrictionsNotFound,
                    "CbacUnavailable": admin_errors.CbacUnavailable,
                    "GetCbacMarkingRestrictionInfoPermissionDenied": admin_errors.GetCbacMarkingRestrictionInfoPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _CbacMarkingRestrictionsClientRaw:
    def __init__(self, client: CbacMarkingRestrictionsClient) -> None:
        def get(_: admin_models.CbacMarkingRestrictions): ...

        self.get = core.with_raw_response(get, client.get)


class _CbacMarkingRestrictionsClientStreaming:
    def __init__(self, client: CbacMarkingRestrictionsClient) -> None:
        def get(_: admin_models.CbacMarkingRestrictions): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncCbacMarkingRestrictionsClient:
    """
    The API client for the CbacMarkingRestrictions Resource.

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

        self.with_streaming_response = _AsyncCbacMarkingRestrictionsClientStreaming(self)
        self.with_raw_response = _AsyncCbacMarkingRestrictionsClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        *,
        marking_ids: typing.Optional[typing.List[core_models.MarkingId]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.CbacMarkingRestrictions]:
        """
        Returns disallowed, implied, and required markings for the given set of marking IDs.
        :param marking_ids: The marking IDs for which to get restrictions.
        :type marking_ids: Optional[List[MarkingId]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.CbacMarkingRestrictions]

        :raises CbacMarkingRestrictionsNotFound: The given CbacMarkingRestrictions could not be found.
        :raises CbacUnavailable: CBAC is not available.
        :raises GetCbacMarkingRestrictionInfoPermissionDenied: The provided token does not have permission to get the CBAC marking restrictions for the markings.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/cbacMarkingRestrictions",
                query_params={
                    "markingIds": marking_ids,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=admin_models.CbacMarkingRestrictions,
                request_timeout=request_timeout,
                throwable_errors={
                    "CbacMarkingRestrictionsNotFound": admin_errors.CbacMarkingRestrictionsNotFound,
                    "CbacUnavailable": admin_errors.CbacUnavailable,
                    "GetCbacMarkingRestrictionInfoPermissionDenied": admin_errors.GetCbacMarkingRestrictionInfoPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncCbacMarkingRestrictionsClientRaw:
    def __init__(self, client: AsyncCbacMarkingRestrictionsClient) -> None:
        def get(_: admin_models.CbacMarkingRestrictions): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncCbacMarkingRestrictionsClientStreaming:
    def __init__(self, client: AsyncCbacMarkingRestrictionsClient) -> None:
        def get(_: admin_models.CbacMarkingRestrictions): ...

        self.get = core.async_with_streaming_response(get, client.get)
