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


class MarkingRoleAssignmentClient:
    """
    The API client for the MarkingRoleAssignment Resource.

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

        self.with_streaming_response = _MarkingRoleAssignmentClientStreaming(self)
        self.with_raw_response = _MarkingRoleAssignmentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        marking_id: core_models.MarkingId,
        *,
        role_assignments: typing.List[admin_models.MarkingRoleUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[MarkingRoleUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddMarkingRoleAssignmentsPermissionDenied: Could not add the MarkingRoleAssignment.
        :raises AddMarkingRoleAssignmentsPermissionDenied: Could not add the MarkingRoleAssignment.
        :raises GetMarkingPermissionDenied: The provided token does not have permission to view the marking.
        :raises MarkingNotFound: The given Marking could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[admin_models.MarkingRoleUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingRoleAssignmentsPermissionDenied": admin_errors.AddMarkingRoleAssignmentsPermissionDenied,
                    "AddMarkingRoleAssignmentsPermissionDenied": admin_errors.AddMarkingRoleAssignmentsPermissionDenied,
                    "GetMarkingPermissionDenied": admin_errors.GetMarkingPermissionDenied,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        marking_id: core_models.MarkingId,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[admin_models.MarkingRoleAssignment]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[admin_models.MarkingRoleAssignment]

        :raises ListMarkingRoleAssignmentsPermissionDenied: The provided token does not have permission to list assigned roles for this marking.
        :raises MarkingNotFound: The given Marking could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListMarkingRoleAssignmentsPermissionDenied": admin_errors.ListMarkingRoleAssignmentsPermissionDenied,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        marking_id: core_models.MarkingId,
        *,
        role_assignments: typing.List[admin_models.MarkingRoleUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[MarkingRoleUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises GetMarkingPermissionDenied: The provided token does not have permission to view the marking.
        :raises ListMarkingRoleAssignmentsPermissionDenied: The provided token does not have permission to list assigned roles for this marking.
        :raises MarkingNotFound: The given Marking could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveMarkingMembersPermissionDenied: Could not remove the MarkingMember.
        :raises RemoveMarkingRoleAssignmentsPermissionDenied: Could not remove the MarkingRoleAssignment.
        :raises RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed: You cannot remove all administrators from a marking.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[admin_models.MarkingRoleUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetMarkingPermissionDenied": admin_errors.GetMarkingPermissionDenied,
                    "ListMarkingRoleAssignmentsPermissionDenied": admin_errors.ListMarkingRoleAssignmentsPermissionDenied,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveMarkingMembersPermissionDenied": admin_errors.RemoveMarkingMembersPermissionDenied,
                    "RemoveMarkingRoleAssignmentsPermissionDenied": admin_errors.RemoveMarkingRoleAssignmentsPermissionDenied,
                    "RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed": admin_errors.RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MarkingRoleAssignmentClientRaw:
    def __init__(self, client: MarkingRoleAssignmentClient) -> None:
        def add(_: None): ...
        def list(_: admin_models.ListMarkingRoleAssignmentsResponse): ...
        def remove(_: None): ...

        self.add = core.with_raw_response(add, client.add)
        self.list = core.with_raw_response(list, client.list)
        self.remove = core.with_raw_response(remove, client.remove)


class _MarkingRoleAssignmentClientStreaming:
    def __init__(self, client: MarkingRoleAssignmentClient) -> None:
        def list(_: admin_models.ListMarkingRoleAssignmentsResponse): ...

        self.list = core.with_streaming_response(list, client.list)


class AsyncMarkingRoleAssignmentClient:
    """
    The API client for the MarkingRoleAssignment Resource.

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

        self.with_streaming_response = _AsyncMarkingRoleAssignmentClientStreaming(self)
        self.with_raw_response = _AsyncMarkingRoleAssignmentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        marking_id: core_models.MarkingId,
        *,
        role_assignments: typing.List[admin_models.MarkingRoleUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[MarkingRoleUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises AddMarkingRoleAssignmentsPermissionDenied: Could not add the MarkingRoleAssignment.
        :raises AddMarkingRoleAssignmentsPermissionDenied: Could not add the MarkingRoleAssignment.
        :raises GetMarkingPermissionDenied: The provided token does not have permission to view the marking.
        :raises MarkingNotFound: The given Marking could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[admin_models.MarkingRoleUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingRoleAssignmentsPermissionDenied": admin_errors.AddMarkingRoleAssignmentsPermissionDenied,
                    "AddMarkingRoleAssignmentsPermissionDenied": admin_errors.AddMarkingRoleAssignmentsPermissionDenied,
                    "GetMarkingPermissionDenied": admin_errors.GetMarkingPermissionDenied,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        marking_id: core_models.MarkingId,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[admin_models.MarkingRoleAssignment]:
        """
        List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

        :param marking_id:
        :type marking_id: MarkingId
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[admin_models.MarkingRoleAssignment]

        :raises ListMarkingRoleAssignmentsPermissionDenied: The provided token does not have permission to list assigned roles for this marking.
        :raises MarkingNotFound: The given Marking could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListMarkingRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListMarkingRoleAssignmentsPermissionDenied": admin_errors.ListMarkingRoleAssignmentsPermissionDenied,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        marking_id: core_models.MarkingId,
        *,
        role_assignments: typing.List[admin_models.MarkingRoleUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """

        :param marking_id:
        :type marking_id: MarkingId
        :param role_assignments:
        :type role_assignments: List[MarkingRoleUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises GetMarkingPermissionDenied: The provided token does not have permission to view the marking.
        :raises ListMarkingRoleAssignmentsPermissionDenied: The provided token does not have permission to list assigned roles for this marking.
        :raises MarkingNotFound: The given Marking could not be found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveMarkingMembersPermissionDenied: Could not remove the MarkingMember.
        :raises RemoveMarkingRoleAssignmentsPermissionDenied: Could not remove the MarkingRoleAssignment.
        :raises RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed: You cannot remove all administrators from a marking.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/{markingId}/roleAssignments/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[admin_models.MarkingRoleUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetMarkingPermissionDenied": admin_errors.GetMarkingPermissionDenied,
                    "ListMarkingRoleAssignmentsPermissionDenied": admin_errors.ListMarkingRoleAssignmentsPermissionDenied,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveMarkingMembersPermissionDenied": admin_errors.RemoveMarkingMembersPermissionDenied,
                    "RemoveMarkingRoleAssignmentsPermissionDenied": admin_errors.RemoveMarkingRoleAssignmentsPermissionDenied,
                    "RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed": admin_errors.RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncMarkingRoleAssignmentClientRaw:
    def __init__(self, client: AsyncMarkingRoleAssignmentClient) -> None:
        def add(_: None): ...
        def list(_: admin_models.ListMarkingRoleAssignmentsResponse): ...
        def remove(_: None): ...

        self.add = core.async_with_raw_response(add, client.add)
        self.list = core.async_with_raw_response(list, client.list)
        self.remove = core.async_with_raw_response(remove, client.remove)


class _AsyncMarkingRoleAssignmentClientStreaming:
    def __init__(self, client: AsyncMarkingRoleAssignmentClient) -> None:
        def list(_: admin_models.ListMarkingRoleAssignmentsResponse): ...

        self.list = core.async_with_streaming_response(list, client.list)
