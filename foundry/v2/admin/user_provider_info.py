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
from foundry.v2.admin import errors as admin_errors
from foundry.v2.admin.models._provider_id import ProviderId
from foundry.v2.admin.models._user_provider_info import UserProviderInfo
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.core.models._principal_id import PrincipalId


class UserProviderInfoClient:
    """
    The API client for the UserProviderInfo Resource.

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
        self.with_streaming_response = _UserProviderInfoClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _UserProviderInfoClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        user_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> UserProviderInfo:
        """
        Get the UserProviderInfo.
        :param user_id: userId
        :type user_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: UserProviderInfo

        :raises UserProviderInfoNotFound: The given UserProviderInfo could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=UserProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "UserProviderInfoNotFound": admin_errors.UserProviderInfoNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        user_id: PrincipalId,
        *,
        provider_id: ProviderId,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> UserProviderInfo:
        """
        Replace the UserProviderInfo.
        :param user_id: userId
        :type user_id: PrincipalId
        :param provider_id: The ID of the User in the external authentication provider. This value is determined by the authentication provider. At most one User can have a given provider ID in a given Realm.
        :type provider_id: ProviderId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: UserProviderInfo

        :raises ReplaceUserProviderInfoPermissionDenied: Could not replace the UserProviderInfo.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/admin/users/{userId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "providerId": provider_id,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "providerId": ProviderId,
                    },
                ),
                response_type=UserProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceUserProviderInfoPermissionDenied": admin_errors.ReplaceUserProviderInfoPermissionDenied,
                },
            ),
        ).decode()


class _UserProviderInfoClientRaw:
    """
    The API client for the UserProviderInfo Resource.

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
    def get(
        self,
        user_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[UserProviderInfo]:
        """
        Get the UserProviderInfo.
        :param user_id: userId
        :type user_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[UserProviderInfo]

        :raises UserProviderInfoNotFound: The given UserProviderInfo could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=UserProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "UserProviderInfoNotFound": admin_errors.UserProviderInfoNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        user_id: PrincipalId,
        *,
        provider_id: ProviderId,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[UserProviderInfo]:
        """
        Replace the UserProviderInfo.
        :param user_id: userId
        :type user_id: PrincipalId
        :param provider_id: The ID of the User in the external authentication provider. This value is determined by the authentication provider. At most one User can have a given provider ID in a given Realm.
        :type provider_id: ProviderId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[UserProviderInfo]

        :raises ReplaceUserProviderInfoPermissionDenied: Could not replace the UserProviderInfo.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/admin/users/{userId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "providerId": provider_id,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "providerId": ProviderId,
                    },
                ),
                response_type=UserProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceUserProviderInfoPermissionDenied": admin_errors.ReplaceUserProviderInfoPermissionDenied,
                },
            ),
        )


class _UserProviderInfoClientStreaming:
    """
    The API client for the UserProviderInfo Resource.

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
    def get(
        self,
        user_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[UserProviderInfo]:
        """
        Get the UserProviderInfo.
        :param user_id: userId
        :type user_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[UserProviderInfo]

        :raises UserProviderInfoNotFound: The given UserProviderInfo could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=UserProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "UserProviderInfoNotFound": admin_errors.UserProviderInfoNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        user_id: PrincipalId,
        *,
        provider_id: ProviderId,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[UserProviderInfo]:
        """
        Replace the UserProviderInfo.
        :param user_id: userId
        :type user_id: PrincipalId
        :param provider_id: The ID of the User in the external authentication provider. This value is determined by the authentication provider. At most one User can have a given provider ID in a given Realm.
        :type provider_id: ProviderId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[UserProviderInfo]

        :raises ReplaceUserProviderInfoPermissionDenied: Could not replace the UserProviderInfo.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/admin/users/{userId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "providerId": provider_id,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "providerId": ProviderId,
                    },
                ),
                response_type=UserProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceUserProviderInfoPermissionDenied": admin_errors.ReplaceUserProviderInfoPermissionDenied,
                },
            ),
        )
