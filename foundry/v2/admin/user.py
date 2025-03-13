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


class UserClient:
    """
    The API client for the User Resource.

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
        self.with_streaming_response = _UserClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _UserClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def ProviderInfo(self):
        from foundry.v2.admin.user_provider_info import UserProviderInfoClient

        return UserProviderInfoClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def GroupMembership(self):
        from foundry.v2.admin.group_membership import GroupMembershipClient

        return GroupMembershipClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        user_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Delete the User with the specified id.
        :param user_id:
        :type user_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteUserPermissionDenied: Could not delete the User.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/admin/users/{userId}",
                query_params={},
                path_params={
                    "userId": user_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteUserPermissionDenied": admin_errors.DeleteUserPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        user_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.User:
        """
        Get the User with the specified id.
        :param user_id:
        :type user_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.User

        :raises UserNotFound: The given User could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}",
                query_params={},
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.User,
                request_timeout=request_timeout,
                throwable_errors={
                    "UserNotFound": admin_errors.UserNotFound,
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
                    admin_models.GetUsersBatchRequestElement,
                    admin_models.GetUsersBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.GetUsersBatchResponse:
        """
        Execute multiple get requests on User.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[Union[GetUsersBatchRequestElement, GetUsersBatchRequestElementDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.GetUsersBatchResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/users/getBatch",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[admin_models.GetUsersBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=admin_models.GetUsersBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_current(
        self,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.User:
        """

        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.User

        :raises GetCurrentUserPermissionDenied: Could not getCurrent the User.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/getCurrent",
                query_params={},
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.User,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetCurrentUserPermissionDenied": admin_errors.GetCurrentUserPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_markings(
        self,
        user_id: core_models.PrincipalId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.GetUserMarkingsResponse:
        """
        Retrieve Markings that the user is currently a member of.
        :param user_id:
        :type user_id: PrincipalId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.GetUserMarkingsResponse

        :raises GetMarkingsUserPermissionDenied: Could not getMarkings the User.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/getMarkings",
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
                response_type=admin_models.GetUserMarkingsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetMarkingsUserPermissionDenied": admin_errors.GetMarkingsUserPermissionDenied,
                },
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
    ) -> core.ResourceIterator[admin_models.User]:
        """
        Lists all Users.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[admin_models.User]
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users",
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
                response_type=admin_models.ListUsersResponse,
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
    ) -> admin_models.ListUsersResponse:
        """
        Lists all Users.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.ListUsersResponse
        """

        warnings.warn(
            "The client.admin.User.page(...) method has been deprecated. Please use client.admin.User.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users",
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
                response_type=admin_models.ListUsersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def profile_picture(
        self,
        user_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Optional[bytes]:
        """

        :param user_id:
        :type user_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Optional[bytes]

        :raises GetProfilePictureOfUserPermissionDenied: Could not profilePicture the User.
        :raises InvalidProfilePicture: The user's profile picture is not a valid image
        :raises UserNotFound: The given User could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/profilePicture",
                query_params={},
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=typing.Optional[bytes],
                request_timeout=request_timeout,
                throwable_errors={
                    "GetProfilePictureOfUserPermissionDenied": admin_errors.GetProfilePictureOfUserPermissionDenied,
                    "InvalidProfilePicture": admin_errors.InvalidProfilePicture,
                    "UserNotFound": admin_errors.UserNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: typing.Union[admin_models.UserSearchFilter, admin_models.UserSearchFilterDict],
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.SearchUsersResponse:
        """
        Perform a case-insensitive prefix search for users based on username, given name and family name.

        :param where:
        :type where: Union[UserSearchFilter, UserSearchFilterDict]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.SearchUsersResponse

        :raises SearchUsersPermissionDenied: Could not search the User.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/users/search",
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
                            admin_models.UserSearchFilter, admin_models.UserSearchFilterDict
                        ],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                    },
                ),
                response_type=admin_models.SearchUsersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchUsersPermissionDenied": admin_errors.SearchUsersPermissionDenied,
                },
            ),
        ).decode()


class _UserClientRaw:
    """
    The API client for the User Resource.

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
    def delete(
        self,
        user_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Delete the User with the specified id.
        :param user_id:
        :type user_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises DeleteUserPermissionDenied: Could not delete the User.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/admin/users/{userId}",
                query_params={},
                path_params={
                    "userId": user_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteUserPermissionDenied": admin_errors.DeleteUserPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        user_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.User]:
        """
        Get the User with the specified id.
        :param user_id:
        :type user_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.User]

        :raises UserNotFound: The given User could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}",
                query_params={},
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.User,
                request_timeout=request_timeout,
                throwable_errors={
                    "UserNotFound": admin_errors.UserNotFound,
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
                    admin_models.GetUsersBatchRequestElement,
                    admin_models.GetUsersBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.GetUsersBatchResponse]:
        """
        Execute multiple get requests on User.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[Union[GetUsersBatchRequestElement, GetUsersBatchRequestElementDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.GetUsersBatchResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/users/getBatch",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[admin_models.GetUsersBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=admin_models.GetUsersBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_current(
        self,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.User]:
        """

        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.User]

        :raises GetCurrentUserPermissionDenied: Could not getCurrent the User.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/getCurrent",
                query_params={},
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.User,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetCurrentUserPermissionDenied": admin_errors.GetCurrentUserPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_markings(
        self,
        user_id: core_models.PrincipalId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.GetUserMarkingsResponse]:
        """
        Retrieve Markings that the user is currently a member of.
        :param user_id:
        :type user_id: PrincipalId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.GetUserMarkingsResponse]

        :raises GetMarkingsUserPermissionDenied: Could not getMarkings the User.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/getMarkings",
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
                response_type=admin_models.GetUserMarkingsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetMarkingsUserPermissionDenied": admin_errors.GetMarkingsUserPermissionDenied,
                },
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
    ) -> core.ApiResponse[admin_models.ListUsersResponse]:
        """
        Lists all Users.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.ListUsersResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users",
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
                response_type=admin_models.ListUsersResponse,
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
    ) -> core.ApiResponse[admin_models.ListUsersResponse]:
        """
        Lists all Users.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.ListUsersResponse]
        """

        warnings.warn(
            "The client.admin.User.page(...) method has been deprecated. Please use client.admin.User.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users",
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
                response_type=admin_models.ListUsersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def profile_picture(
        self,
        user_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[typing.Optional[bytes]]:
        """

        :param user_id:
        :type user_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[typing.Optional[bytes]]

        :raises GetProfilePictureOfUserPermissionDenied: Could not profilePicture the User.
        :raises InvalidProfilePicture: The user's profile picture is not a valid image
        :raises UserNotFound: The given User could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/profilePicture",
                query_params={},
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=typing.Optional[bytes],
                request_timeout=request_timeout,
                throwable_errors={
                    "GetProfilePictureOfUserPermissionDenied": admin_errors.GetProfilePictureOfUserPermissionDenied,
                    "InvalidProfilePicture": admin_errors.InvalidProfilePicture,
                    "UserNotFound": admin_errors.UserNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: typing.Union[admin_models.UserSearchFilter, admin_models.UserSearchFilterDict],
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.SearchUsersResponse]:
        """
        Perform a case-insensitive prefix search for users based on username, given name and family name.

        :param where:
        :type where: Union[UserSearchFilter, UserSearchFilterDict]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.SearchUsersResponse]

        :raises SearchUsersPermissionDenied: Could not search the User.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/users/search",
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
                            admin_models.UserSearchFilter, admin_models.UserSearchFilterDict
                        ],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                    },
                ),
                response_type=admin_models.SearchUsersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchUsersPermissionDenied": admin_errors.SearchUsersPermissionDenied,
                },
            ),
        )


class _UserClientStreaming:
    """
    The API client for the User Resource.

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
    def delete(
        self,
        user_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Delete the User with the specified id.
        :param user_id:
        :type user_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises DeleteUserPermissionDenied: Could not delete the User.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/admin/users/{userId}",
                query_params={},
                path_params={
                    "userId": user_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteUserPermissionDenied": admin_errors.DeleteUserPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        user_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.User]:
        """
        Get the User with the specified id.
        :param user_id:
        :type user_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.User]

        :raises UserNotFound: The given User could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}",
                query_params={},
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.User,
                request_timeout=request_timeout,
                throwable_errors={
                    "UserNotFound": admin_errors.UserNotFound,
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
                    admin_models.GetUsersBatchRequestElement,
                    admin_models.GetUsersBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=500),
        ],
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.GetUsersBatchResponse]:
        """
        Execute multiple get requests on User.

        The maximum batch size for this endpoint is 500.
        :param body: Body of the request
        :type body: List[Union[GetUsersBatchRequestElement, GetUsersBatchRequestElementDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.GetUsersBatchResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/users/getBatch",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[admin_models.GetUsersBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=500),
                ],
                response_type=admin_models.GetUsersBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_current(
        self,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.User]:
        """

        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.User]

        :raises GetCurrentUserPermissionDenied: Could not getCurrent the User.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/getCurrent",
                query_params={},
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.User,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetCurrentUserPermissionDenied": admin_errors.GetCurrentUserPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_markings(
        self,
        user_id: core_models.PrincipalId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.GetUserMarkingsResponse]:
        """
        Retrieve Markings that the user is currently a member of.
        :param user_id:
        :type user_id: PrincipalId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.GetUserMarkingsResponse]

        :raises GetMarkingsUserPermissionDenied: Could not getMarkings the User.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/getMarkings",
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
                response_type=admin_models.GetUserMarkingsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetMarkingsUserPermissionDenied": admin_errors.GetMarkingsUserPermissionDenied,
                },
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
    ) -> core.StreamingContextManager[admin_models.ListUsersResponse]:
        """
        Lists all Users.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.ListUsersResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users",
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
                response_type=admin_models.ListUsersResponse,
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
    ) -> core.StreamingContextManager[admin_models.ListUsersResponse]:
        """
        Lists all Users.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.ListUsersResponse]
        """

        warnings.warn(
            "The client.admin.User.page(...) method has been deprecated. Please use client.admin.User.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users",
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
                response_type=admin_models.ListUsersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def profile_picture(
        self,
        user_id: core_models.PrincipalId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[typing.Optional[bytes]]:
        """

        :param user_id:
        :type user_id: PrincipalId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[typing.Optional[bytes]]

        :raises GetProfilePictureOfUserPermissionDenied: Could not profilePicture the User.
        :raises InvalidProfilePicture: The user's profile picture is not a valid image
        :raises UserNotFound: The given User could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/users/{userId}/profilePicture",
                query_params={},
                path_params={
                    "userId": user_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=typing.Optional[bytes],
                request_timeout=request_timeout,
                throwable_errors={
                    "GetProfilePictureOfUserPermissionDenied": admin_errors.GetProfilePictureOfUserPermissionDenied,
                    "InvalidProfilePicture": admin_errors.InvalidProfilePicture,
                    "UserNotFound": admin_errors.UserNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: typing.Union[admin_models.UserSearchFilter, admin_models.UserSearchFilterDict],
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.SearchUsersResponse]:
        """
        Perform a case-insensitive prefix search for users based on username, given name and family name.

        :param where:
        :type where: Union[UserSearchFilter, UserSearchFilterDict]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.SearchUsersResponse]

        :raises SearchUsersPermissionDenied: Could not search the User.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/users/search",
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
                            admin_models.UserSearchFilter, admin_models.UserSearchFilterDict
                        ],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                    },
                ),
                response_type=admin_models.SearchUsersResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchUsersPermissionDenied": admin_errors.SearchUsersPermissionDenied,
                },
            ),
        )
