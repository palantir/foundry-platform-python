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
from foundry.v2.admin.models._group_provider_info import GroupProviderInfo
from foundry.v2.admin.models._provider_id import ProviderId
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.core.models._principal_id import PrincipalId


class GroupProviderInfoClient:
    """
    The API client for the GroupProviderInfo Resource.

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
        self.with_streaming_response = _GroupProviderInfoClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _GroupProviderInfoClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        group_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> GroupProviderInfo:
        """
        Get the GroupProviderInfo.
        :param group_id: groupId
        :type group_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: GroupProviderInfo

        :raises GroupProviderInfoNotFound: The given GroupProviderInfo could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=GroupProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupProviderInfoNotFound": admin_errors.GroupProviderInfoNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        group_id: PrincipalId,
        *,
        provider_id: ProviderId,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> GroupProviderInfo:
        """
        Replace the GroupProviderInfo.
        :param group_id: groupId
        :type group_id: PrincipalId
        :param provider_id: The ID of the Group in the external authentication provider. This value is determined by the authentication provider. At most one Group can have a given provider ID in a given Realm.
        :type provider_id: ProviderId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: GroupProviderInfo

        :raises ReplaceGroupProviderInfoPermissionDenied: Could not replace the GroupProviderInfo.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/admin/groups/{groupId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "groupId": group_id,
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
                response_type=GroupProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceGroupProviderInfoPermissionDenied": admin_errors.ReplaceGroupProviderInfoPermissionDenied,
                },
            ),
        ).decode()


class _GroupProviderInfoClientRaw:
    """
    The API client for the GroupProviderInfo Resource.

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
        group_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[GroupProviderInfo]:
        """
        Get the GroupProviderInfo.
        :param group_id: groupId
        :type group_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[GroupProviderInfo]

        :raises GroupProviderInfoNotFound: The given GroupProviderInfo could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=GroupProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupProviderInfoNotFound": admin_errors.GroupProviderInfoNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        group_id: PrincipalId,
        *,
        provider_id: ProviderId,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[GroupProviderInfo]:
        """
        Replace the GroupProviderInfo.
        :param group_id: groupId
        :type group_id: PrincipalId
        :param provider_id: The ID of the Group in the external authentication provider. This value is determined by the authentication provider. At most one Group can have a given provider ID in a given Realm.
        :type provider_id: ProviderId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[GroupProviderInfo]

        :raises ReplaceGroupProviderInfoPermissionDenied: Could not replace the GroupProviderInfo.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/admin/groups/{groupId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "groupId": group_id,
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
                response_type=GroupProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceGroupProviderInfoPermissionDenied": admin_errors.ReplaceGroupProviderInfoPermissionDenied,
                },
            ),
        )


class _GroupProviderInfoClientStreaming:
    """
    The API client for the GroupProviderInfo Resource.

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
        group_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[GroupProviderInfo]:
        """
        Get the GroupProviderInfo.
        :param group_id: groupId
        :type group_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[GroupProviderInfo]

        :raises GroupProviderInfoNotFound: The given GroupProviderInfo could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=GroupProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupProviderInfoNotFound": admin_errors.GroupProviderInfoNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        group_id: PrincipalId,
        *,
        provider_id: ProviderId,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[GroupProviderInfo]:
        """
        Replace the GroupProviderInfo.
        :param group_id: groupId
        :type group_id: PrincipalId
        :param provider_id: The ID of the Group in the external authentication provider. This value is determined by the authentication provider. At most one Group can have a given provider ID in a given Realm.
        :type provider_id: ProviderId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[GroupProviderInfo]

        :raises ReplaceGroupProviderInfoPermissionDenied: Could not replace the GroupProviderInfo.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/admin/groups/{groupId}/providerInfo",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "groupId": group_id,
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
                response_type=GroupProviderInfo,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceGroupProviderInfoPermissionDenied": admin_errors.ReplaceGroupProviderInfoPermissionDenied,
                },
            ),
        )
