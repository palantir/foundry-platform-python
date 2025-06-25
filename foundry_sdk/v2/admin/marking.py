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

import annotated_types
import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.admin import errors as admin_errors
from foundry_sdk.v2.admin import models as admin_models
from foundry_sdk.v2.core import errors as core_errors
from foundry_sdk.v2.core import models as core_models


class MarkingClient:
    """
    The API client for the Marking Resource.

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

        self.with_streaming_response = _MarkingClientStreaming(self)
        self.with_raw_response = _MarkingClientRaw(self)

    @cached_property
    def MarkingMember(self):
        from foundry_sdk.v2.admin.marking_member import MarkingMemberClient

        return MarkingMemberClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def MarkingRoleAssignment(self):
        from foundry_sdk.v2.admin.marking_role_assignment import MarkingRoleAssignmentClient  # NOQA

        return MarkingRoleAssignmentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        category_id: admin_models.MarkingCategoryId,
        initial_members: typing.List[core_models.PrincipalId],
        initial_role_assignments: typing.List[admin_models.MarkingRoleUpdate],
        name: admin_models.MarkingName,
        description: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.Marking:
        """
        Creates a new Marking.
        :param category_id:
        :type category_id: MarkingCategoryId
        :param initial_members: Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.
        :type initial_members: List[PrincipalId]
        :param initial_role_assignments: The initial roles that will be assigned when the Marking is created. At least one ADMIN role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.
        :type initial_role_assignments: List[MarkingRoleUpdate]
        :param name:
        :type name: MarkingName
        :param description:
        :type description: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Marking

        :raises CreateMarkingMissingInitialAdminRole: At least one ADMIN role assignment must be provided when creating a marking.
        :raises CreateMarkingPermissionDenied: Could not create the Marking.
        :raises GetMarkingCategoryPermissionDenied: The provided token does not have permission to view the marking category.
        :raises MarkingCategoryNotFound: The given MarkingCategory could not be found.
        :raises MarkingNameInCategoryAlreadyExists: A marking with the same name already exists in the category.
        :raises MarkingNameIsEmpty: The marking name is empty.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "initialRoleAssignments": initial_role_assignments,
                    "initialMembers": initial_members,
                    "name": name,
                    "description": description,
                    "categoryId": category_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "initialRoleAssignments": typing.List[admin_models.MarkingRoleUpdate],
                        "initialMembers": typing.List[core_models.PrincipalId],
                        "name": admin_models.MarkingName,
                        "description": typing.Optional[str],
                        "categoryId": admin_models.MarkingCategoryId,
                    },
                ),
                response_type=admin_models.Marking,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateMarkingMissingInitialAdminRole": admin_errors.CreateMarkingMissingInitialAdminRole,
                    "CreateMarkingPermissionDenied": admin_errors.CreateMarkingPermissionDenied,
                    "GetMarkingCategoryPermissionDenied": admin_errors.GetMarkingCategoryPermissionDenied,
                    "MarkingCategoryNotFound": admin_errors.MarkingCategoryNotFound,
                    "MarkingNameInCategoryAlreadyExists": admin_errors.MarkingNameInCategoryAlreadyExists,
                    "MarkingNameIsEmpty": admin_errors.MarkingNameIsEmpty,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marking_id: core_models.MarkingId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.Marking:
        """
        Get the Marking with the specified id.
        :param marking_id:
        :type marking_id: MarkingId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Marking

        :raises GetMarkingPermissionDenied: The provided token does not have permission to view the marking.
        :raises MarkingNotFound: The given Marking could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}",
                query_params={
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
                response_type=admin_models.Marking,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetMarkingPermissionDenied": admin_errors.GetMarkingPermissionDenied,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[admin_models.GetMarkingsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.GetMarkingsBatchResponse:
        """
        Execute multiple get requests on Marking.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[GetMarkingsBatchRequestElement]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.GetMarkingsBatchResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[admin_models.GetMarkingsBatchRequestElement],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=admin_models.GetMarkingsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[admin_models.Marking]:
        """
        Maximum page size 100.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[admin_models.Marking]

        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListMarkingsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidPageSize": core_errors.InvalidPageSize,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        marking_id: core_models.MarkingId,
        *,
        name: admin_models.MarkingName,
        description: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.Marking:
        """
        Replace the Marking with the specified id.
        :param marking_id:
        :type marking_id: MarkingId
        :param name:
        :type name: MarkingName
        :param description:
        :type description: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Marking

        :raises GetMarkingCategoryPermissionDenied: The provided token does not have permission to view the marking category.
        :raises GetMarkingPermissionDenied: The provided token does not have permission to view the marking.
        :raises MarkingNameInCategoryAlreadyExists: A marking with the same name already exists in the category.
        :raises MarkingNameIsEmpty: The marking name is empty.
        :raises MarkingNotFound: The given Marking could not be found.
        :raises ReplaceMarkingPermissionDenied: Could not replace the Marking.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/admin/markings/{markingId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "description": description,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.MarkingName,
                        "description": typing.Optional[str],
                    },
                ),
                response_type=admin_models.Marking,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetMarkingCategoryPermissionDenied": admin_errors.GetMarkingCategoryPermissionDenied,
                    "GetMarkingPermissionDenied": admin_errors.GetMarkingPermissionDenied,
                    "MarkingNameInCategoryAlreadyExists": admin_errors.MarkingNameInCategoryAlreadyExists,
                    "MarkingNameIsEmpty": admin_errors.MarkingNameIsEmpty,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "ReplaceMarkingPermissionDenied": admin_errors.ReplaceMarkingPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MarkingClientRaw:
    def __init__(self, client: MarkingClient) -> None:
        def create(_: admin_models.Marking): ...
        def get(_: admin_models.Marking): ...
        def get_batch(_: admin_models.GetMarkingsBatchResponse): ...
        def list(_: admin_models.ListMarkingsResponse): ...
        def replace(_: admin_models.Marking): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.get_batch = core.with_raw_response(get_batch, client.get_batch)
        self.list = core.with_raw_response(list, client.list)
        self.replace = core.with_raw_response(replace, client.replace)


class _MarkingClientStreaming:
    def __init__(self, client: MarkingClient) -> None:
        def create(_: admin_models.Marking): ...
        def get(_: admin_models.Marking): ...
        def get_batch(_: admin_models.GetMarkingsBatchResponse): ...
        def list(_: admin_models.ListMarkingsResponse): ...
        def replace(_: admin_models.Marking): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.get_batch = core.with_streaming_response(get_batch, client.get_batch)
        self.list = core.with_streaming_response(list, client.list)
        self.replace = core.with_streaming_response(replace, client.replace)


class AsyncMarkingClient:
    """
    The API client for the Marking Resource.

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

        self.with_streaming_response = _AsyncMarkingClientStreaming(self)
        self.with_raw_response = _AsyncMarkingClientRaw(self)

    @cached_property
    def MarkingMember(self):
        from foundry_sdk.v2.admin.marking_member import AsyncMarkingMemberClient

        return AsyncMarkingMemberClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def MarkingRoleAssignment(self):
        from foundry_sdk.v2.admin.marking_role_assignment import (
            AsyncMarkingRoleAssignmentClient,
        )  # NOQA

        return AsyncMarkingRoleAssignmentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        category_id: admin_models.MarkingCategoryId,
        initial_members: typing.List[core_models.PrincipalId],
        initial_role_assignments: typing.List[admin_models.MarkingRoleUpdate],
        name: admin_models.MarkingName,
        description: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.Marking]:
        """
        Creates a new Marking.
        :param category_id:
        :type category_id: MarkingCategoryId
        :param initial_members: Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.
        :type initial_members: List[PrincipalId]
        :param initial_role_assignments: The initial roles that will be assigned when the Marking is created. At least one ADMIN role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.
        :type initial_role_assignments: List[MarkingRoleUpdate]
        :param name:
        :type name: MarkingName
        :param description:
        :type description: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.Marking]

        :raises CreateMarkingMissingInitialAdminRole: At least one ADMIN role assignment must be provided when creating a marking.
        :raises CreateMarkingPermissionDenied: Could not create the Marking.
        :raises GetMarkingCategoryPermissionDenied: The provided token does not have permission to view the marking category.
        :raises MarkingCategoryNotFound: The given MarkingCategory could not be found.
        :raises MarkingNameInCategoryAlreadyExists: A marking with the same name already exists in the category.
        :raises MarkingNameIsEmpty: The marking name is empty.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "initialRoleAssignments": initial_role_assignments,
                    "initialMembers": initial_members,
                    "name": name,
                    "description": description,
                    "categoryId": category_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "initialRoleAssignments": typing.List[admin_models.MarkingRoleUpdate],
                        "initialMembers": typing.List[core_models.PrincipalId],
                        "name": admin_models.MarkingName,
                        "description": typing.Optional[str],
                        "categoryId": admin_models.MarkingCategoryId,
                    },
                ),
                response_type=admin_models.Marking,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateMarkingMissingInitialAdminRole": admin_errors.CreateMarkingMissingInitialAdminRole,
                    "CreateMarkingPermissionDenied": admin_errors.CreateMarkingPermissionDenied,
                    "GetMarkingCategoryPermissionDenied": admin_errors.GetMarkingCategoryPermissionDenied,
                    "MarkingCategoryNotFound": admin_errors.MarkingCategoryNotFound,
                    "MarkingNameInCategoryAlreadyExists": admin_errors.MarkingNameInCategoryAlreadyExists,
                    "MarkingNameIsEmpty": admin_errors.MarkingNameIsEmpty,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marking_id: core_models.MarkingId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.Marking]:
        """
        Get the Marking with the specified id.
        :param marking_id:
        :type marking_id: MarkingId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.Marking]

        :raises GetMarkingPermissionDenied: The provided token does not have permission to view the marking.
        :raises MarkingNotFound: The given Marking could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings/{markingId}",
                query_params={
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
                response_type=admin_models.Marking,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetMarkingPermissionDenied": admin_errors.GetMarkingPermissionDenied,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[admin_models.GetMarkingsBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.GetMarkingsBatchResponse]:
        """
        Execute multiple get requests on Marking.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[GetMarkingsBatchRequestElement]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.GetMarkingsBatchResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/markings/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[admin_models.GetMarkingsBatchRequestElement],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=admin_models.GetMarkingsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[admin_models.Marking]:
        """
        Maximum page size 100.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[admin_models.Marking]

        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/markings",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListMarkingsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidPageSize": core_errors.InvalidPageSize,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        marking_id: core_models.MarkingId,
        *,
        name: admin_models.MarkingName,
        description: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.Marking]:
        """
        Replace the Marking with the specified id.
        :param marking_id:
        :type marking_id: MarkingId
        :param name:
        :type name: MarkingName
        :param description:
        :type description: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.Marking]

        :raises GetMarkingCategoryPermissionDenied: The provided token does not have permission to view the marking category.
        :raises GetMarkingPermissionDenied: The provided token does not have permission to view the marking.
        :raises MarkingNameInCategoryAlreadyExists: A marking with the same name already exists in the category.
        :raises MarkingNameIsEmpty: The marking name is empty.
        :raises MarkingNotFound: The given Marking could not be found.
        :raises ReplaceMarkingPermissionDenied: Could not replace the Marking.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/admin/markings/{markingId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "markingId": marking_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "description": description,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.MarkingName,
                        "description": typing.Optional[str],
                    },
                ),
                response_type=admin_models.Marking,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetMarkingCategoryPermissionDenied": admin_errors.GetMarkingCategoryPermissionDenied,
                    "GetMarkingPermissionDenied": admin_errors.GetMarkingPermissionDenied,
                    "MarkingNameInCategoryAlreadyExists": admin_errors.MarkingNameInCategoryAlreadyExists,
                    "MarkingNameIsEmpty": admin_errors.MarkingNameIsEmpty,
                    "MarkingNotFound": admin_errors.MarkingNotFound,
                    "ReplaceMarkingPermissionDenied": admin_errors.ReplaceMarkingPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncMarkingClientRaw:
    def __init__(self, client: AsyncMarkingClient) -> None:
        def create(_: admin_models.Marking): ...
        def get(_: admin_models.Marking): ...
        def get_batch(_: admin_models.GetMarkingsBatchResponse): ...
        def list(_: admin_models.ListMarkingsResponse): ...
        def replace(_: admin_models.Marking): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_batch = core.async_with_raw_response(get_batch, client.get_batch)
        self.list = core.async_with_raw_response(list, client.list)
        self.replace = core.async_with_raw_response(replace, client.replace)


class _AsyncMarkingClientStreaming:
    def __init__(self, client: AsyncMarkingClient) -> None:
        def create(_: admin_models.Marking): ...
        def get(_: admin_models.Marking): ...
        def get_batch(_: admin_models.GetMarkingsBatchResponse): ...
        def list(_: admin_models.ListMarkingsResponse): ...
        def replace(_: admin_models.Marking): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_batch = core.async_with_streaming_response(get_batch, client.get_batch)
        self.list = core.async_with_streaming_response(list, client.list)
        self.replace = core.async_with_streaming_response(replace, client.replace)
