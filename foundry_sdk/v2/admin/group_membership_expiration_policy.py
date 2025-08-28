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


class GroupMembershipExpirationPolicyClient:
    """
    The API client for the GroupMembershipExpirationPolicy Resource.

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

        self.with_streaming_response = _GroupMembershipExpirationPolicyClientStreaming(self)
        self.with_raw_response = _GroupMembershipExpirationPolicyClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        group_id: core_models.GroupId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.GroupMembershipExpirationPolicy:
        """
        Get the GroupMembershipExpirationPolicy.
        :param group_id:
        :type group_id: GroupId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.GroupMembershipExpirationPolicy

        :raises GroupMembershipExpirationPolicyNotFound: The given GroupMembershipExpirationPolicy could not be found.
        :raises GroupNotFound: The given Group could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}/membershipExpirationPolicy",
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
                response_type=admin_models.GroupMembershipExpirationPolicy,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupMembershipExpirationPolicyNotFound": admin_errors.GroupMembershipExpirationPolicyNotFound,
                    "GroupNotFound": admin_errors.GroupNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        group_id: core_models.GroupId,
        *,
        maximum_duration: typing.Optional[core_models.DurationSeconds] = None,
        maximum_value: typing.Optional[admin_models.GroupMembershipExpiration] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.GroupMembershipExpirationPolicy:
        """
        Replace the GroupMembershipExpirationPolicy.
        :param group_id:
        :type group_id: GroupId
        :param maximum_duration: Members in this group must be added with expirations that are less than this duration in seconds into the future from the time they are added.
        :type maximum_duration: Optional[DurationSeconds]
        :param maximum_value: Members in this group must be added with expiration times that occur before this value.
        :type maximum_value: Optional[GroupMembershipExpiration]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.GroupMembershipExpirationPolicy

        :raises GroupNotFound: The given Group could not be found.
        :raises ReplaceGroupMembershipExpirationPolicyPermissionDenied: Could not replace the GroupMembershipExpirationPolicy.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/admin/groups/{groupId}/membershipExpirationPolicy",
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
                    "maximumDuration": maximum_duration,
                    "maximumValue": maximum_value,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "maximumDuration": typing.Optional[core_models.DurationSeconds],
                        "maximumValue": typing.Optional[admin_models.GroupMembershipExpiration],
                    },
                ),
                response_type=admin_models.GroupMembershipExpirationPolicy,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupNotFound": admin_errors.GroupNotFound,
                    "ReplaceGroupMembershipExpirationPolicyPermissionDenied": admin_errors.ReplaceGroupMembershipExpirationPolicyPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _GroupMembershipExpirationPolicyClientRaw:
    def __init__(self, client: GroupMembershipExpirationPolicyClient) -> None:
        def get(_: admin_models.GroupMembershipExpirationPolicy): ...
        def replace(_: admin_models.GroupMembershipExpirationPolicy): ...

        self.get = core.with_raw_response(get, client.get)
        self.replace = core.with_raw_response(replace, client.replace)


class _GroupMembershipExpirationPolicyClientStreaming:
    def __init__(self, client: GroupMembershipExpirationPolicyClient) -> None:
        def get(_: admin_models.GroupMembershipExpirationPolicy): ...
        def replace(_: admin_models.GroupMembershipExpirationPolicy): ...

        self.get = core.with_streaming_response(get, client.get)
        self.replace = core.with_streaming_response(replace, client.replace)


class AsyncGroupMembershipExpirationPolicyClient:
    """
    The API client for the GroupMembershipExpirationPolicy Resource.

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

        self.with_streaming_response = _AsyncGroupMembershipExpirationPolicyClientStreaming(self)
        self.with_raw_response = _AsyncGroupMembershipExpirationPolicyClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        group_id: core_models.GroupId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.GroupMembershipExpirationPolicy]:
        """
        Get the GroupMembershipExpirationPolicy.
        :param group_id:
        :type group_id: GroupId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.GroupMembershipExpirationPolicy]

        :raises GroupMembershipExpirationPolicyNotFound: The given GroupMembershipExpirationPolicy could not be found.
        :raises GroupNotFound: The given Group could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}/membershipExpirationPolicy",
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
                response_type=admin_models.GroupMembershipExpirationPolicy,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupMembershipExpirationPolicyNotFound": admin_errors.GroupMembershipExpirationPolicyNotFound,
                    "GroupNotFound": admin_errors.GroupNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        group_id: core_models.GroupId,
        *,
        maximum_duration: typing.Optional[core_models.DurationSeconds] = None,
        maximum_value: typing.Optional[admin_models.GroupMembershipExpiration] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.GroupMembershipExpirationPolicy]:
        """
        Replace the GroupMembershipExpirationPolicy.
        :param group_id:
        :type group_id: GroupId
        :param maximum_duration: Members in this group must be added with expirations that are less than this duration in seconds into the future from the time they are added.
        :type maximum_duration: Optional[DurationSeconds]
        :param maximum_value: Members in this group must be added with expiration times that occur before this value.
        :type maximum_value: Optional[GroupMembershipExpiration]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.GroupMembershipExpirationPolicy]

        :raises GroupNotFound: The given Group could not be found.
        :raises ReplaceGroupMembershipExpirationPolicyPermissionDenied: Could not replace the GroupMembershipExpirationPolicy.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/admin/groups/{groupId}/membershipExpirationPolicy",
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
                    "maximumDuration": maximum_duration,
                    "maximumValue": maximum_value,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "maximumDuration": typing.Optional[core_models.DurationSeconds],
                        "maximumValue": typing.Optional[admin_models.GroupMembershipExpiration],
                    },
                ),
                response_type=admin_models.GroupMembershipExpirationPolicy,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupNotFound": admin_errors.GroupNotFound,
                    "ReplaceGroupMembershipExpirationPolicyPermissionDenied": admin_errors.ReplaceGroupMembershipExpirationPolicyPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncGroupMembershipExpirationPolicyClientRaw:
    def __init__(self, client: AsyncGroupMembershipExpirationPolicyClient) -> None:
        def get(_: admin_models.GroupMembershipExpirationPolicy): ...
        def replace(_: admin_models.GroupMembershipExpirationPolicy): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.replace = core.async_with_raw_response(replace, client.replace)


class _AsyncGroupMembershipExpirationPolicyClientStreaming:
    def __init__(self, client: AsyncGroupMembershipExpirationPolicyClient) -> None:
        def get(_: admin_models.GroupMembershipExpirationPolicy): ...
        def replace(_: admin_models.GroupMembershipExpirationPolicy): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.replace = core.async_with_streaming_response(replace, client.replace)
