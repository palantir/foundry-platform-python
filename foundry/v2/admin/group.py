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


class GroupClient:
    """
    The API client for the Group Resource.

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
        self.with_streaming_response = _GroupClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _GroupClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def ProviderInfo(self):
        from foundry.v2.admin.group_provider_info import GroupProviderInfoClient

        return GroupProviderInfoClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def GroupMember(self):
        from foundry.v2.admin.group_member import GroupMemberClient

        return GroupMemberClient(
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
        attributes: typing.Dict[admin_models.AttributeName, admin_models.AttributeValues],
        name: admin_models.GroupName,
        organizations: typing.List[core_models.OrganizationRid],
        description: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.Group:
        """
        Creates a new Group.
        :param attributes: A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change.
        :type attributes: Dict[AttributeName, AttributeValues]
        :param name: The name of the Group.
        :type name: GroupName
        :param organizations: The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.
        :type organizations: List[OrganizationRid]
        :param description: A description of the Group.
        :type description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Group

        :raises CreateGroupPermissionDenied: Could not create the Group.
        :raises CreateGroupPermissionDenied: Could not create the Group.
        :raises GroupNameAlreadyExists: A group with this name already exists
        :raises InvalidGroupOrganizations: At least one Organization RID must be provided for a group
        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "organizations": organizations,
                    "description": description,
                    "attributes": attributes,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.GroupName,
                        "organizations": typing.List[core_models.OrganizationRid],
                        "description": typing.Optional[str],
                        "attributes": typing.Dict[
                            admin_models.AttributeName, admin_models.AttributeValues
                        ],
                    },
                ),
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateGroupPermissionDenied": admin_errors.CreateGroupPermissionDenied,
                    "CreateGroupPermissionDenied": admin_errors.CreateGroupPermissionDenied,
                    "GroupNameAlreadyExists": admin_errors.GroupNameAlreadyExists,
                    "InvalidGroupOrganizations": admin_errors.InvalidGroupOrganizations,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        group_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Delete the Group with the specified id.
        :param group_id:
        :type group_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteGroupPermissionDenied: Could not delete the Group.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteGroupPermissionDenied": admin_errors.DeleteGroupPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        group_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.Group:
        """
        Get the Group with the specified id.
        :param group_id:
        :type group_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Group

        :raises GroupNotFound: The given Group could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupNotFound": admin_errors.GroupNotFound,
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
                    admin_models.GetGroupsBatchRequestElement,
                    admin_models.GetGroupsBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.GetGroupsBatchResponse:
        """
        Execute multiple get requests on Group.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[Union[GetGroupsBatchRequestElement, GetGroupsBatchRequestElementDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.GetGroupsBatchResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/getBatch",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[admin_models.GetGroupsBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=admin_models.GetGroupsBatchResponse,
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[admin_models.Group]:
        """
        Lists all Groups.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[admin_models.Group]
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListGroupsResponse,
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.ListGroupsResponse:
        """
        Lists all Groups.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.ListGroupsResponse
        """

        warnings.warn(
            "The client.admin.Group.page(...) method has been deprecated. Please use client.admin.Group.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: typing.Union[admin_models.GroupSearchFilter, admin_models.GroupSearchFilterDict],
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.SearchGroupsResponse:
        """
        Perform a case-insensitive prefix search for groups based on group name.

        :param where:
        :type where: Union[GroupSearchFilter, GroupSearchFilterDict]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.SearchGroupsResponse

        :raises SearchGroupsPermissionDenied: Could not search the Group.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/search",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "where": where,
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Union[
                            admin_models.GroupSearchFilter, admin_models.GroupSearchFilterDict
                        ],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                    },
                ),
                response_type=admin_models.SearchGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchGroupsPermissionDenied": admin_errors.SearchGroupsPermissionDenied,
                },
            ),
        ).decode()


class _GroupClientRaw:
    """
    The API client for the Group Resource.

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
        attributes: typing.Dict[admin_models.AttributeName, admin_models.AttributeValues],
        name: admin_models.GroupName,
        organizations: typing.List[core_models.OrganizationRid],
        description: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.Group]:
        """
        Creates a new Group.
        :param attributes: A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change.
        :type attributes: Dict[AttributeName, AttributeValues]
        :param name: The name of the Group.
        :type name: GroupName
        :param organizations: The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.
        :type organizations: List[OrganizationRid]
        :param description: A description of the Group.
        :type description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.Group]

        :raises CreateGroupPermissionDenied: Could not create the Group.
        :raises CreateGroupPermissionDenied: Could not create the Group.
        :raises GroupNameAlreadyExists: A group with this name already exists
        :raises InvalidGroupOrganizations: At least one Organization RID must be provided for a group
        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "organizations": organizations,
                    "description": description,
                    "attributes": attributes,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.GroupName,
                        "organizations": typing.List[core_models.OrganizationRid],
                        "description": typing.Optional[str],
                        "attributes": typing.Dict[
                            admin_models.AttributeName, admin_models.AttributeValues
                        ],
                    },
                ),
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateGroupPermissionDenied": admin_errors.CreateGroupPermissionDenied,
                    "CreateGroupPermissionDenied": admin_errors.CreateGroupPermissionDenied,
                    "GroupNameAlreadyExists": admin_errors.GroupNameAlreadyExists,
                    "InvalidGroupOrganizations": admin_errors.InvalidGroupOrganizations,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        group_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Delete the Group with the specified id.
        :param group_id:
        :type group_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises DeleteGroupPermissionDenied: Could not delete the Group.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteGroupPermissionDenied": admin_errors.DeleteGroupPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        group_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.Group]:
        """
        Get the Group with the specified id.
        :param group_id:
        :type group_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.Group]

        :raises GroupNotFound: The given Group could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupNotFound": admin_errors.GroupNotFound,
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
                    admin_models.GetGroupsBatchRequestElement,
                    admin_models.GetGroupsBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.GetGroupsBatchResponse]:
        """
        Execute multiple get requests on Group.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[Union[GetGroupsBatchRequestElement, GetGroupsBatchRequestElementDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.GetGroupsBatchResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/getBatch",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[admin_models.GetGroupsBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=admin_models.GetGroupsBatchResponse,
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.ListGroupsResponse]:
        """
        Lists all Groups.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.ListGroupsResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListGroupsResponse,
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.ListGroupsResponse]:
        """
        Lists all Groups.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.ListGroupsResponse]
        """

        warnings.warn(
            "The client.admin.Group.page(...) method has been deprecated. Please use client.admin.Group.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: typing.Union[admin_models.GroupSearchFilter, admin_models.GroupSearchFilterDict],
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.SearchGroupsResponse]:
        """
        Perform a case-insensitive prefix search for groups based on group name.

        :param where:
        :type where: Union[GroupSearchFilter, GroupSearchFilterDict]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.SearchGroupsResponse]

        :raises SearchGroupsPermissionDenied: Could not search the Group.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/search",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "where": where,
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Union[
                            admin_models.GroupSearchFilter, admin_models.GroupSearchFilterDict
                        ],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                    },
                ),
                response_type=admin_models.SearchGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchGroupsPermissionDenied": admin_errors.SearchGroupsPermissionDenied,
                },
            ),
        )


class _GroupClientStreaming:
    """
    The API client for the Group Resource.

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
        attributes: typing.Dict[admin_models.AttributeName, admin_models.AttributeValues],
        name: admin_models.GroupName,
        organizations: typing.List[core_models.OrganizationRid],
        description: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.Group]:
        """
        Creates a new Group.
        :param attributes: A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change.
        :type attributes: Dict[AttributeName, AttributeValues]
        :param name: The name of the Group.
        :type name: GroupName
        :param organizations: The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed.
        :type organizations: List[OrganizationRid]
        :param description: A description of the Group.
        :type description: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.Group]

        :raises CreateGroupPermissionDenied: Could not create the Group.
        :raises CreateGroupPermissionDenied: Could not create the Group.
        :raises GroupNameAlreadyExists: A group with this name already exists
        :raises InvalidGroupOrganizations: At least one Organization RID must be provided for a group
        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "organizations": organizations,
                    "description": description,
                    "attributes": attributes,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.GroupName,
                        "organizations": typing.List[core_models.OrganizationRid],
                        "description": typing.Optional[str],
                        "attributes": typing.Dict[
                            admin_models.AttributeName, admin_models.AttributeValues
                        ],
                    },
                ),
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateGroupPermissionDenied": admin_errors.CreateGroupPermissionDenied,
                    "CreateGroupPermissionDenied": admin_errors.CreateGroupPermissionDenied,
                    "GroupNameAlreadyExists": admin_errors.GroupNameAlreadyExists,
                    "InvalidGroupOrganizations": admin_errors.InvalidGroupOrganizations,
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        group_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Delete the Group with the specified id.
        :param group_id:
        :type group_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises DeleteGroupPermissionDenied: Could not delete the Group.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteGroupPermissionDenied": admin_errors.DeleteGroupPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        group_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.Group]:
        """
        Get the Group with the specified id.
        :param group_id:
        :type group_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.Group]

        :raises GroupNotFound: The given Group could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups/{groupId}",
                query_params={},
                path_params={
                    "groupId": group_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.Group,
                request_timeout=request_timeout,
                throwable_errors={
                    "GroupNotFound": admin_errors.GroupNotFound,
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
                    admin_models.GetGroupsBatchRequestElement,
                    admin_models.GetGroupsBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.GetGroupsBatchResponse]:
        """
        Execute multiple get requests on Group.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[Union[GetGroupsBatchRequestElement, GetGroupsBatchRequestElementDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.GetGroupsBatchResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/getBatch",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[admin_models.GetGroupsBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=admin_models.GetGroupsBatchResponse,
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.ListGroupsResponse]:
        """
        Lists all Groups.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.ListGroupsResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListGroupsResponse,
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.ListGroupsResponse]:
        """
        Lists all Groups.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.ListGroupsResponse]
        """

        warnings.warn(
            "The client.admin.Group.page(...) method has been deprecated. Please use client.admin.Group.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/groups",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.ListGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: typing.Union[admin_models.GroupSearchFilter, admin_models.GroupSearchFilterDict],
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.SearchGroupsResponse]:
        """
        Perform a case-insensitive prefix search for groups based on group name.

        :param where:
        :type where: Union[GroupSearchFilter, GroupSearchFilterDict]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.SearchGroupsResponse]

        :raises SearchGroupsPermissionDenied: Could not search the Group.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/groups/search",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "where": where,
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Union[
                            admin_models.GroupSearchFilter, admin_models.GroupSearchFilterDict
                        ],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                    },
                ),
                response_type=admin_models.SearchGroupsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchGroupsPermissionDenied": admin_errors.SearchGroupsPermissionDenied,
                },
            ),
        )
