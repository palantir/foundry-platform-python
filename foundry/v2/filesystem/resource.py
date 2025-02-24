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

import warnings
from functools import cached_property
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.core.models._marking_id import MarkingId
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.filesystem import errors as filesystem_errors
from foundry.v2.filesystem.models._access_requirements import AccessRequirements
from foundry.v2.filesystem.models._list_markings_of_resource_response import (
    ListMarkingsOfResourceResponse,
)  # NOQA
from foundry.v2.filesystem.models._resource import Resource
from foundry.v2.filesystem.models._resource_path import ResourcePath
from foundry.v2.filesystem.models._resource_rid import ResourceRid


class ResourceClient:
    """
    The API client for the Resource Resource.

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
        self.with_streaming_response = _ResourceClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ResourceClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def Role(self):
        from foundry.v2.filesystem.resource_role import ResourceRoleClient

        return ResourceRoleClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def add_markings(
        self,
        resource_rid: ResourceRid,
        *,
        marking_ids: List[MarkingId],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Adds a list of Markings to a resource.
        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddMarkingsPermissionDenied: Could not addMarkings the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/addMarkings",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "markingIds": marking_ids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": List[MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingsPermissionDenied": filesystem_errors.AddMarkingsPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Move the given resource to the trash. Following this operation, the resource can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteResourcePermissionDenied: Could not delete the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteResourcePermissionDenied": filesystem_errors.DeleteResourcePermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Resource:
        """
        Get the Resource with the specified rid.
        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Resource

        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_access_requirements(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> AccessRequirements:
        """
        Returns a list of access requirements a user needs in order to view a resource. Access requirements are
        composed of Organizations and Markings, and can either be applied directly to the resource or inherited.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AccessRequirements

        :raises GetAccessRequirementsPermissionDenied: Could not getAccessRequirements the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/getAccessRequirements",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AccessRequirements,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetAccessRequirementsPermissionDenied": filesystem_errors.GetAccessRequirementsPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_by_path(
        self,
        *,
        path: ResourcePath,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Resource:
        """
        Get a Resource by its absolute path.
        :param path: path
        :type path: ResourcePath
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Resource

        :raises GetByPathPermissionDenied: Could not getByPath the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/getByPath",
                query_params={
                    "path": path,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByPathPermissionDenied": filesystem_errors.GetByPathPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def markings(
        self,
        resource_rid: ResourceRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[MarkingId]:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[MarkingId]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def markings_page(
        self,
        resource_rid: ResourceRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListMarkingsOfResourceResponse:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListMarkingsOfResourceResponse
        """

        warnings.warn(
            "The client.filesystem.Resource.markings_page(...) method has been deprecated. Please use client.filesystem.Resource.markings(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def permanently_delete(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Permanently delete the given resource from the trash. If the Resource is not directly trashed, a
        `ResourceNotTrashed` error will be thrown.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises PermanentlyDeleteResourcePermissionDenied: Could not permanentlyDelete the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/permanentlyDelete",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PermanentlyDeleteResourcePermissionDenied": filesystem_errors.PermanentlyDeleteResourcePermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove_markings(
        self,
        resource_rid: ResourceRid,
        *,
        marking_ids: List[MarkingId],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Removes Markings from a resource.
        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises RemoveMarkingsPermissionDenied: Could not removeMarkings the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/removeMarkings",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "markingIds": marking_ids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": List[MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveMarkingsPermissionDenied": filesystem_errors.RemoveMarkingsPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def restore(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
        trashed, this operation will be ignored.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises RestoreResourcePermissionDenied: Could not restore the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
            ),
        ).decode()


class _ResourceClientRaw:
    """
    The API client for the Resource Resource.

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
    def add_markings(
        self,
        resource_rid: ResourceRid,
        *,
        marking_ids: List[MarkingId],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Adds a list of Markings to a resource.
        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises AddMarkingsPermissionDenied: Could not addMarkings the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/addMarkings",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "markingIds": marking_ids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": List[MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingsPermissionDenied": filesystem_errors.AddMarkingsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Move the given resource to the trash. Following this operation, the resource can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises DeleteResourcePermissionDenied: Could not delete the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteResourcePermissionDenied": filesystem_errors.DeleteResourcePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Resource]:
        """
        Get the Resource with the specified rid.
        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Resource]

        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_access_requirements(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[AccessRequirements]:
        """
        Returns a list of access requirements a user needs in order to view a resource. Access requirements are
        composed of Organizations and Markings, and can either be applied directly to the resource or inherited.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[AccessRequirements]

        :raises GetAccessRequirementsPermissionDenied: Could not getAccessRequirements the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/getAccessRequirements",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AccessRequirements,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetAccessRequirementsPermissionDenied": filesystem_errors.GetAccessRequirementsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_by_path(
        self,
        *,
        path: ResourcePath,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Resource]:
        """
        Get a Resource by its absolute path.
        :param path: path
        :type path: ResourcePath
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Resource]

        :raises GetByPathPermissionDenied: Could not getByPath the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/getByPath",
                query_params={
                    "path": path,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByPathPermissionDenied": filesystem_errors.GetByPathPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def markings(
        self,
        resource_rid: ResourceRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListMarkingsOfResourceResponse]:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListMarkingsOfResourceResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def markings_page(
        self,
        resource_rid: ResourceRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListMarkingsOfResourceResponse]:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListMarkingsOfResourceResponse]
        """

        warnings.warn(
            "The client.filesystem.Resource.markings_page(...) method has been deprecated. Please use client.filesystem.Resource.markings(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def permanently_delete(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Permanently delete the given resource from the trash. If the Resource is not directly trashed, a
        `ResourceNotTrashed` error will be thrown.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises PermanentlyDeleteResourcePermissionDenied: Could not permanentlyDelete the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/permanentlyDelete",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PermanentlyDeleteResourcePermissionDenied": filesystem_errors.PermanentlyDeleteResourcePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove_markings(
        self,
        resource_rid: ResourceRid,
        *,
        marking_ids: List[MarkingId],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Removes Markings from a resource.
        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises RemoveMarkingsPermissionDenied: Could not removeMarkings the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/removeMarkings",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "markingIds": marking_ids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": List[MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveMarkingsPermissionDenied": filesystem_errors.RemoveMarkingsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def restore(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
        trashed, this operation will be ignored.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises RestoreResourcePermissionDenied: Could not restore the Resource.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
            ),
        )


class _ResourceClientStreaming:
    """
    The API client for the Resource Resource.

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
    def add_markings(
        self,
        resource_rid: ResourceRid,
        *,
        marking_ids: List[MarkingId],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Adds a list of Markings to a resource.
        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises AddMarkingsPermissionDenied: Could not addMarkings the Resource.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/addMarkings",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "markingIds": marking_ids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": List[MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddMarkingsPermissionDenied": filesystem_errors.AddMarkingsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Move the given resource to the trash. Following this operation, the resource can be restored, using the
        `restore` operation, or permanently deleted using the `permanentlyDelete` operation.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises DeleteResourcePermissionDenied: Could not delete the Resource.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteResourcePermissionDenied": filesystem_errors.DeleteResourcePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Resource]:
        """
        Get the Resource with the specified rid.
        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Resource]

        :raises ResourceNotFound: The given Resource could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "ResourceNotFound": filesystem_errors.ResourceNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_access_requirements(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[AccessRequirements]:
        """
        Returns a list of access requirements a user needs in order to view a resource. Access requirements are
        composed of Organizations and Markings, and can either be applied directly to the resource or inherited.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[AccessRequirements]

        :raises GetAccessRequirementsPermissionDenied: Could not getAccessRequirements the Resource.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/getAccessRequirements",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AccessRequirements,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetAccessRequirementsPermissionDenied": filesystem_errors.GetAccessRequirementsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_by_path(
        self,
        *,
        path: ResourcePath,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Resource]:
        """
        Get a Resource by its absolute path.
        :param path: path
        :type path: ResourcePath
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Resource]

        :raises GetByPathPermissionDenied: Could not getByPath the Resource.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/getByPath",
                query_params={
                    "path": path,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Resource,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByPathPermissionDenied": filesystem_errors.GetByPathPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def markings(
        self,
        resource_rid: ResourceRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListMarkingsOfResourceResponse]:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListMarkingsOfResourceResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def markings_page(
        self,
        resource_rid: ResourceRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListMarkingsOfResourceResponse]:
        """
        List of Markings directly applied to a resource. The number of Markings on a resource is typically small
        so the `pageSize` and `pageToken` parameters are not required.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListMarkingsOfResourceResponse]
        """

        warnings.warn(
            "The client.filesystem.Resource.markings_page(...) method has been deprecated. Please use client.filesystem.Resource.markings(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/filesystem/resources/{resourceRid}/markings",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListMarkingsOfResourceResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def permanently_delete(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Permanently delete the given resource from the trash. If the Resource is not directly trashed, a
        `ResourceNotTrashed` error will be thrown.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises PermanentlyDeleteResourcePermissionDenied: Could not permanentlyDelete the Resource.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/permanentlyDelete",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PermanentlyDeleteResourcePermissionDenied": filesystem_errors.PermanentlyDeleteResourcePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def remove_markings(
        self,
        resource_rid: ResourceRid,
        *,
        marking_ids: List[MarkingId],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Removes Markings from a resource.
        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param marking_ids:
        :type marking_ids: List[MarkingId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises RemoveMarkingsPermissionDenied: Could not removeMarkings the Resource.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/removeMarkings",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "markingIds": marking_ids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "markingIds": List[MarkingId],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RemoveMarkingsPermissionDenied": filesystem_errors.RemoveMarkingsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def restore(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
        trashed, this operation will be ignored.

        :param resource_rid: resourceRid
        :type resource_rid: ResourceRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises RestoreResourcePermissionDenied: Could not restore the Resource.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/filesystem/resources/{resourceRid}/restore",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "resourceRid": resource_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "RestoreResourcePermissionDenied": filesystem_errors.RestoreResourcePermissionDenied,
                },
            ),
        )
