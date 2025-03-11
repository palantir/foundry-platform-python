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
import warnings
from functools import cached_property

import annotated_types
import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.admin import errors as admin_errors
from foundry.v2.admin import models as admin_models
from foundry.v2.core import models as core_models


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
        self.with_streaming_response = _MarkingClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _MarkingClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def MarkingMember(self):
        from foundry.v2.admin.marking_member import MarkingMemberClient

        return MarkingMemberClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def MarkingRoleAssignment(self):
        from foundry.v2.admin.marking_role_assignment import MarkingRoleAssignmentClient

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
        initial_role_assignments: typing.List[
            typing.Union[admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict]
        ],
        name: admin_models.MarkingName,
        description: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.Marking:
        """
        Creates a new Marking.
        :param category_id:
        :type category_id: MarkingCategoryId
        :param initial_members: Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.
        :type initial_members: List[PrincipalId]
        :param initial_role_assignments: The initial roles that will be assigned when the Marking is created. At least one ADMIN role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.
        :type initial_role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
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
        :raises CreateMarkingNameInCategoryAlreadyExists: A marking with the same name already exists in the category.
        :raises CreateMarkingPermissionDenied: Could not create the Marking.
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
                        "initialRoleAssignments": typing.List[
                            typing.Union[
                                admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict
                            ]
                        ],
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
                    "CreateMarkingNameInCategoryAlreadyExists": admin_errors.CreateMarkingNameInCategoryAlreadyExists,
                    "CreateMarkingPermissionDenied": admin_errors.CreateMarkingPermissionDenied,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marking_id: core_models.MarkingId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
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
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[
                typing.Union[
                    admin_models.GetMarkingsBatchRequestElement,
                    admin_models.GetMarkingsBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.GetMarkingsBatchResponse:
        """
        Execute multiple get requests on Marking.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[Union[GetMarkingsBatchRequestElement, GetMarkingsBatchRequestElementDict]]
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
                    typing.List[admin_models.GetMarkingsBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=admin_models.GetMarkingsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

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
        """

        return self._api_client.iterate_api(
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
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.ListMarkingsResponse:
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
        :rtype: admin_models.ListMarkingsResponse
        """

        warnings.warn(
            "The client.admin.Marking.page(...) method has been deprecated. Please use client.admin.Marking.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

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
                throwable_errors={},
            ),
        ).decode()


class _MarkingClientRaw:
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        category_id: admin_models.MarkingCategoryId,
        initial_members: typing.List[core_models.PrincipalId],
        initial_role_assignments: typing.List[
            typing.Union[admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict]
        ],
        name: admin_models.MarkingName,
        description: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.Marking]:
        """
        Creates a new Marking.
        :param category_id:
        :type category_id: MarkingCategoryId
        :param initial_members: Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.
        :type initial_members: List[PrincipalId]
        :param initial_role_assignments: The initial roles that will be assigned when the Marking is created. At least one ADMIN role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.
        :type initial_role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param name:
        :type name: MarkingName
        :param description:
        :type description: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.Marking]

        :raises CreateMarkingMissingInitialAdminRole: At least one ADMIN role assignment must be provided when creating a marking.
        :raises CreateMarkingNameInCategoryAlreadyExists: A marking with the same name already exists in the category.
        :raises CreateMarkingPermissionDenied: Could not create the Marking.
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
                        "initialRoleAssignments": typing.List[
                            typing.Union[
                                admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict
                            ]
                        ],
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
                    "CreateMarkingNameInCategoryAlreadyExists": admin_errors.CreateMarkingNameInCategoryAlreadyExists,
                    "CreateMarkingPermissionDenied": admin_errors.CreateMarkingPermissionDenied,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
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
    ) -> core.ApiResponse[admin_models.Marking]:
        """
        Get the Marking with the specified id.
        :param marking_id:
        :type marking_id: MarkingId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.Marking]

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
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[
                typing.Union[
                    admin_models.GetMarkingsBatchRequestElement,
                    admin_models.GetMarkingsBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.GetMarkingsBatchResponse]:
        """
        Execute multiple get requests on Marking.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[Union[GetMarkingsBatchRequestElement, GetMarkingsBatchRequestElementDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.GetMarkingsBatchResponse]
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
                    typing.List[admin_models.GetMarkingsBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=admin_models.GetMarkingsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
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
    ) -> core.ApiResponse[admin_models.ListMarkingsResponse]:
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
        :rtype: core.ApiResponse[admin_models.ListMarkingsResponse]
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
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.ListMarkingsResponse]:
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
        :rtype: core.ApiResponse[admin_models.ListMarkingsResponse]
        """

        warnings.warn(
            "The client.admin.Marking.page(...) method has been deprecated. Please use client.admin.Marking.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

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
                throwable_errors={},
            ),
        )


class _MarkingClientStreaming:
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        category_id: admin_models.MarkingCategoryId,
        initial_members: typing.List[core_models.PrincipalId],
        initial_role_assignments: typing.List[
            typing.Union[admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict]
        ],
        name: admin_models.MarkingName,
        description: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.Marking]:
        """
        Creates a new Marking.
        :param category_id:
        :type category_id: MarkingCategoryId
        :param initial_members: Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.
        :type initial_members: List[PrincipalId]
        :param initial_role_assignments: The initial roles that will be assigned when the Marking is created. At least one ADMIN role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.
        :type initial_role_assignments: List[Union[MarkingRoleUpdate, MarkingRoleUpdateDict]]
        :param name:
        :type name: MarkingName
        :param description:
        :type description: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.Marking]

        :raises CreateMarkingMissingInitialAdminRole: At least one ADMIN role assignment must be provided when creating a marking.
        :raises CreateMarkingNameInCategoryAlreadyExists: A marking with the same name already exists in the category.
        :raises CreateMarkingPermissionDenied: Could not create the Marking.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.stream_api(
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
                        "initialRoleAssignments": typing.List[
                            typing.Union[
                                admin_models.MarkingRoleUpdate, admin_models.MarkingRoleUpdateDict
                            ]
                        ],
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
                    "CreateMarkingNameInCategoryAlreadyExists": admin_errors.CreateMarkingNameInCategoryAlreadyExists,
                    "CreateMarkingPermissionDenied": admin_errors.CreateMarkingPermissionDenied,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
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
    ) -> core.StreamingContextManager[admin_models.Marking]:
        """
        Get the Marking with the specified id.
        :param marking_id:
        :type marking_id: MarkingId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.Marking]

        :raises GetMarkingPermissionDenied: The provided token does not have permission to view the marking.
        :raises MarkingNotFound: The given Marking could not be found.
        """

        return self._api_client.stream_api(
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
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[
                typing.Union[
                    admin_models.GetMarkingsBatchRequestElement,
                    admin_models.GetMarkingsBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.GetMarkingsBatchResponse]:
        """
        Execute multiple get requests on Marking.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[Union[GetMarkingsBatchRequestElement, GetMarkingsBatchRequestElementDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.GetMarkingsBatchResponse]
        """

        return self._api_client.stream_api(
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
                    typing.List[admin_models.GetMarkingsBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=admin_models.GetMarkingsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
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
    ) -> core.StreamingContextManager[admin_models.ListMarkingsResponse]:
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
        :rtype: core.StreamingContextManager[admin_models.ListMarkingsResponse]
        """

        return self._api_client.stream_api(
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
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.ListMarkingsResponse]:
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
        :rtype: core.StreamingContextManager[admin_models.ListMarkingsResponse]
        """

        warnings.warn(
            "The client.admin.Marking.page(...) method has been deprecated. Please use client.admin.Marking.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
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
                throwable_errors={},
            ),
        )
