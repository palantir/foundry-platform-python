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
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.filesystem import errors as filesystem_errors
from foundry_sdk.v2.filesystem import models as filesystem_models


class SpaceClient:
    """
    The API client for the Space Resource.

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

        self.with_streaming_response = _SpaceClientStreaming(self)
        self.with_raw_response = _SpaceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        deletion_policy_organizations: typing.List[core_models.OrganizationRid],
        display_name: filesystem_models.ResourceDisplayName,
        enrollment_rid: core_models.EnrollmentRid,
        organizations: typing.List[core_models.OrganizationRid],
        default_role_set_id: typing.Optional[core_models.RoleSetId] = None,
        description: typing.Optional[str] = None,
        file_system_id: typing.Optional[filesystem_models.FileSystemId] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        usage_account_rid: typing.Optional[filesystem_models.UsageAccountRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Space:
        """
        Creates a new Space.
        :param deletion_policy_organizations: By default, this Space will use a Last Out deletion policy, meaning that this Space and its projects will be deleted when the last Organization listed here is deleted. Only Organizations in the Space's Enrollment can be included here.
        :type deletion_policy_organizations: List[OrganizationRid]
        :param display_name:
        :type display_name: ResourceDisplayName
        :param enrollment_rid: The RID of the Enrollment that this Space belongs to.
        :type enrollment_rid: EnrollmentRid
        :param organizations: The list of Organizations that are provisioned access to this Space. In order to access this Space, a user must be a member of at least one of these Organizations.
        :type organizations: List[OrganizationRid]
        :param default_role_set_id: The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used.
        :type default_role_set_id: Optional[RoleSetId]
        :param description: The description of the Space.
        :type description: Optional[str]
        :param file_system_id: The ID of the Filesystem for this Space, which is where the contents of the Space are stored. If not provided, the default Filesystem for this Enrollment will be used.
        :type file_system_id: Optional[FileSystemId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param usage_account_rid: The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used.
        :type usage_account_rid: Optional[UsageAccountRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Space

        :raises CreateSpacePermissionDenied: Could not create the Space.
        :raises EnrollmentNotFound: An enrollment was not found for the user.
        :raises OrganizationsNotFound: At least one organization RID could not be found.
        :raises RoleSetNotFound: The role set provided in the request to create or replace a space could not be found.
        :raises SpaceInternalError: An internal error occurred when trying to create or replace the space.
        :raises SpaceInvalidArgument: An invalid argument was provided in the request to create or replace a space.
        :raises SpaceNameInvalid: The provided space name is invalid. It may be a reserved name or contain invalid characters.
        :raises SpaceNotFound: The given Space could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/spaces",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "enrollmentRid": enrollment_rid,
                    "usageAccountRid": usage_account_rid,
                    "fileSystemId": file_system_id,
                    "displayName": display_name,
                    "organizations": organizations,
                    "description": description,
                    "deletionPolicyOrganizations": deletion_policy_organizations,
                    "defaultRoleSetId": default_role_set_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "enrollmentRid": core_models.EnrollmentRid,
                        "usageAccountRid": typing.Optional[filesystem_models.UsageAccountRid],
                        "fileSystemId": typing.Optional[filesystem_models.FileSystemId],
                        "displayName": filesystem_models.ResourceDisplayName,
                        "organizations": typing.List[core_models.OrganizationRid],
                        "description": typing.Optional[str],
                        "deletionPolicyOrganizations": typing.List[core_models.OrganizationRid],
                        "defaultRoleSetId": typing.Optional[core_models.RoleSetId],
                    },
                ),
                response_type=filesystem_models.Space,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSpacePermissionDenied": filesystem_errors.CreateSpacePermissionDenied,
                    "EnrollmentNotFound": filesystem_errors.EnrollmentNotFound,
                    "OrganizationsNotFound": filesystem_errors.OrganizationsNotFound,
                    "RoleSetNotFound": filesystem_errors.RoleSetNotFound,
                    "SpaceInternalError": filesystem_errors.SpaceInternalError,
                    "SpaceInvalidArgument": filesystem_errors.SpaceInvalidArgument,
                    "SpaceNameInvalid": filesystem_errors.SpaceNameInvalid,
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        space_rid: filesystem_models.SpaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Delete the space. This will only work if the Space is empty, meaning any Projects or Resources have been deleted first.

        :param space_rid:
        :type space_rid: SpaceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteSpacePermissionDenied: Could not delete the Space.
        :raises SpaceNotEmpty: The space cannot be deleted because it contains resources.
        :raises SpaceNotFound: The given Space could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/filesystem/spaces/{spaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteSpacePermissionDenied": filesystem_errors.DeleteSpacePermissionDenied,
                    "SpaceNotEmpty": filesystem_errors.SpaceNotEmpty,
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        space_rid: filesystem_models.SpaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Space:
        """
        Get the Space with the specified rid.
        :param space_rid:
        :type space_rid: SpaceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Space

        :raises SpaceNotFound: The given Space could not be found.
        :raises SpaceNotFound: The given Space could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/spaces/{spaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=filesystem_models.Space,
                request_timeout=request_timeout,
                throwable_errors={
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                },
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
    ) -> core.ResourceIterator[filesystem_models.Space]:
        """
        Lists all Spaces.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[filesystem_models.Space]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/spaces",
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
                response_type=filesystem_models.ListSpacesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        space_rid: filesystem_models.SpaceRid,
        *,
        display_name: filesystem_models.ResourceDisplayName,
        default_role_set_id: typing.Optional[core_models.RoleSetId] = None,
        description: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        usage_account_rid: typing.Optional[filesystem_models.UsageAccountRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> filesystem_models.Space:
        """
        Replace the Space with the specified rid.
        :param space_rid:
        :type space_rid: SpaceRid
        :param display_name:
        :type display_name: ResourceDisplayName
        :param default_role_set_id: The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used.
        :type default_role_set_id: Optional[RoleSetId]
        :param description: The description of the Space.
        :type description: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param usage_account_rid: The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used.
        :type usage_account_rid: Optional[UsageAccountRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: filesystem_models.Space

        :raises ReplaceSpacePermissionDenied: Could not replace the Space.
        :raises ReservedSpaceCannotBeReplaced: The spaceRid provided is for a reserved space in Foundry which cannot be replaced.
        :raises RoleSetNotFound: The role set provided in the request to create or replace a space could not be found.
        :raises SpaceInvalidArgument: An invalid argument was provided in the request to create or replace a space.
        :raises SpaceNameInvalid: The provided space name is invalid. It may be a reserved name or contain invalid characters.
        :raises SpaceNotFound: The given Space could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/filesystem/spaces/{spaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "usageAccountRid": usage_account_rid,
                    "displayName": display_name,
                    "description": description,
                    "defaultRoleSetId": default_role_set_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "usageAccountRid": typing.Optional[filesystem_models.UsageAccountRid],
                        "displayName": filesystem_models.ResourceDisplayName,
                        "description": typing.Optional[str],
                        "defaultRoleSetId": typing.Optional[core_models.RoleSetId],
                    },
                ),
                response_type=filesystem_models.Space,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceSpacePermissionDenied": filesystem_errors.ReplaceSpacePermissionDenied,
                    "ReservedSpaceCannotBeReplaced": filesystem_errors.ReservedSpaceCannotBeReplaced,
                    "RoleSetNotFound": filesystem_errors.RoleSetNotFound,
                    "SpaceInvalidArgument": filesystem_errors.SpaceInvalidArgument,
                    "SpaceNameInvalid": filesystem_errors.SpaceNameInvalid,
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _SpaceClientRaw:
    def __init__(self, client: SpaceClient) -> None:
        def create(_: filesystem_models.Space): ...
        def delete(_: None): ...
        def get(_: filesystem_models.Space): ...
        def list(_: filesystem_models.ListSpacesResponse): ...
        def replace(_: filesystem_models.Space): ...

        self.create = core.with_raw_response(create, client.create)
        self.delete = core.with_raw_response(delete, client.delete)
        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)
        self.replace = core.with_raw_response(replace, client.replace)


class _SpaceClientStreaming:
    def __init__(self, client: SpaceClient) -> None:
        def create(_: filesystem_models.Space): ...
        def get(_: filesystem_models.Space): ...
        def list(_: filesystem_models.ListSpacesResponse): ...
        def replace(_: filesystem_models.Space): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)
        self.replace = core.with_streaming_response(replace, client.replace)


class AsyncSpaceClient:
    """
    The API client for the Space Resource.

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

        self.with_streaming_response = _AsyncSpaceClientStreaming(self)
        self.with_raw_response = _AsyncSpaceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        deletion_policy_organizations: typing.List[core_models.OrganizationRid],
        display_name: filesystem_models.ResourceDisplayName,
        enrollment_rid: core_models.EnrollmentRid,
        organizations: typing.List[core_models.OrganizationRid],
        default_role_set_id: typing.Optional[core_models.RoleSetId] = None,
        description: typing.Optional[str] = None,
        file_system_id: typing.Optional[filesystem_models.FileSystemId] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        usage_account_rid: typing.Optional[filesystem_models.UsageAccountRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Space]:
        """
        Creates a new Space.
        :param deletion_policy_organizations: By default, this Space will use a Last Out deletion policy, meaning that this Space and its projects will be deleted when the last Organization listed here is deleted. Only Organizations in the Space's Enrollment can be included here.
        :type deletion_policy_organizations: List[OrganizationRid]
        :param display_name:
        :type display_name: ResourceDisplayName
        :param enrollment_rid: The RID of the Enrollment that this Space belongs to.
        :type enrollment_rid: EnrollmentRid
        :param organizations: The list of Organizations that are provisioned access to this Space. In order to access this Space, a user must be a member of at least one of these Organizations.
        :type organizations: List[OrganizationRid]
        :param default_role_set_id: The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used.
        :type default_role_set_id: Optional[RoleSetId]
        :param description: The description of the Space.
        :type description: Optional[str]
        :param file_system_id: The ID of the Filesystem for this Space, which is where the contents of the Space are stored. If not provided, the default Filesystem for this Enrollment will be used.
        :type file_system_id: Optional[FileSystemId]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param usage_account_rid: The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used.
        :type usage_account_rid: Optional[UsageAccountRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Space]

        :raises CreateSpacePermissionDenied: Could not create the Space.
        :raises EnrollmentNotFound: An enrollment was not found for the user.
        :raises OrganizationsNotFound: At least one organization RID could not be found.
        :raises RoleSetNotFound: The role set provided in the request to create or replace a space could not be found.
        :raises SpaceInternalError: An internal error occurred when trying to create or replace the space.
        :raises SpaceInvalidArgument: An invalid argument was provided in the request to create or replace a space.
        :raises SpaceNameInvalid: The provided space name is invalid. It may be a reserved name or contain invalid characters.
        :raises SpaceNotFound: The given Space could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/spaces",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "enrollmentRid": enrollment_rid,
                    "usageAccountRid": usage_account_rid,
                    "fileSystemId": file_system_id,
                    "displayName": display_name,
                    "organizations": organizations,
                    "description": description,
                    "deletionPolicyOrganizations": deletion_policy_organizations,
                    "defaultRoleSetId": default_role_set_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "enrollmentRid": core_models.EnrollmentRid,
                        "usageAccountRid": typing.Optional[filesystem_models.UsageAccountRid],
                        "fileSystemId": typing.Optional[filesystem_models.FileSystemId],
                        "displayName": filesystem_models.ResourceDisplayName,
                        "organizations": typing.List[core_models.OrganizationRid],
                        "description": typing.Optional[str],
                        "deletionPolicyOrganizations": typing.List[core_models.OrganizationRid],
                        "defaultRoleSetId": typing.Optional[core_models.RoleSetId],
                    },
                ),
                response_type=filesystem_models.Space,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSpacePermissionDenied": filesystem_errors.CreateSpacePermissionDenied,
                    "EnrollmentNotFound": filesystem_errors.EnrollmentNotFound,
                    "OrganizationsNotFound": filesystem_errors.OrganizationsNotFound,
                    "RoleSetNotFound": filesystem_errors.RoleSetNotFound,
                    "SpaceInternalError": filesystem_errors.SpaceInternalError,
                    "SpaceInvalidArgument": filesystem_errors.SpaceInvalidArgument,
                    "SpaceNameInvalid": filesystem_errors.SpaceNameInvalid,
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        space_rid: filesystem_models.SpaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Delete the space. This will only work if the Space is empty, meaning any Projects or Resources have been deleted first.

        :param space_rid:
        :type space_rid: SpaceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises DeleteSpacePermissionDenied: Could not delete the Space.
        :raises SpaceNotEmpty: The space cannot be deleted because it contains resources.
        :raises SpaceNotFound: The given Space could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/filesystem/spaces/{spaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteSpacePermissionDenied": filesystem_errors.DeleteSpacePermissionDenied,
                    "SpaceNotEmpty": filesystem_errors.SpaceNotEmpty,
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        space_rid: filesystem_models.SpaceRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Space]:
        """
        Get the Space with the specified rid.
        :param space_rid:
        :type space_rid: SpaceRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Space]

        :raises SpaceNotFound: The given Space could not be found.
        :raises SpaceNotFound: The given Space could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/spaces/{spaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=filesystem_models.Space,
                request_timeout=request_timeout,
                throwable_errors={
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                },
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
    ) -> core.AsyncResourceIterator[filesystem_models.Space]:
        """
        Lists all Spaces.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[filesystem_models.Space]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/spaces",
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
                response_type=filesystem_models.ListSpacesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        space_rid: filesystem_models.SpaceRid,
        *,
        display_name: filesystem_models.ResourceDisplayName,
        default_role_set_id: typing.Optional[core_models.RoleSetId] = None,
        description: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        usage_account_rid: typing.Optional[filesystem_models.UsageAccountRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[filesystem_models.Space]:
        """
        Replace the Space with the specified rid.
        :param space_rid:
        :type space_rid: SpaceRid
        :param display_name:
        :type display_name: ResourceDisplayName
        :param default_role_set_id: The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used.
        :type default_role_set_id: Optional[RoleSetId]
        :param description: The description of the Space.
        :type description: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param usage_account_rid: The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used.
        :type usage_account_rid: Optional[UsageAccountRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[filesystem_models.Space]

        :raises ReplaceSpacePermissionDenied: Could not replace the Space.
        :raises ReservedSpaceCannotBeReplaced: The spaceRid provided is for a reserved space in Foundry which cannot be replaced.
        :raises RoleSetNotFound: The role set provided in the request to create or replace a space could not be found.
        :raises SpaceInvalidArgument: An invalid argument was provided in the request to create or replace a space.
        :raises SpaceNameInvalid: The provided space name is invalid. It may be a reserved name or contain invalid characters.
        :raises SpaceNotFound: The given Space could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/filesystem/spaces/{spaceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "spaceRid": space_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "usageAccountRid": usage_account_rid,
                    "displayName": display_name,
                    "description": description,
                    "defaultRoleSetId": default_role_set_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "usageAccountRid": typing.Optional[filesystem_models.UsageAccountRid],
                        "displayName": filesystem_models.ResourceDisplayName,
                        "description": typing.Optional[str],
                        "defaultRoleSetId": typing.Optional[core_models.RoleSetId],
                    },
                ),
                response_type=filesystem_models.Space,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReplaceSpacePermissionDenied": filesystem_errors.ReplaceSpacePermissionDenied,
                    "ReservedSpaceCannotBeReplaced": filesystem_errors.ReservedSpaceCannotBeReplaced,
                    "RoleSetNotFound": filesystem_errors.RoleSetNotFound,
                    "SpaceInvalidArgument": filesystem_errors.SpaceInvalidArgument,
                    "SpaceNameInvalid": filesystem_errors.SpaceNameInvalid,
                    "SpaceNotFound": filesystem_errors.SpaceNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncSpaceClientRaw:
    def __init__(self, client: AsyncSpaceClient) -> None:
        def create(_: filesystem_models.Space): ...
        def delete(_: None): ...
        def get(_: filesystem_models.Space): ...
        def list(_: filesystem_models.ListSpacesResponse): ...
        def replace(_: filesystem_models.Space): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.delete = core.async_with_raw_response(delete, client.delete)
        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)
        self.replace = core.async_with_raw_response(replace, client.replace)


class _AsyncSpaceClientStreaming:
    def __init__(self, client: AsyncSpaceClient) -> None:
        def create(_: filesystem_models.Space): ...
        def get(_: filesystem_models.Space): ...
        def list(_: filesystem_models.ListSpacesResponse): ...
        def replace(_: filesystem_models.Space): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
        self.replace = core.async_with_streaming_response(replace, client.replace)
