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

from typing import Any
from typing import Dict
from typing import Optional

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call
from typing_extensions import Annotated

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.filesystem.models._resource import Resource
from foundry.v2.filesystem.models._resource_rid import ResourceRid


class ResourceClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def delete(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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
            ),
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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
            ),
        )

    @validate_call
    @handle_unexpected
    def permanently_delete(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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
            ),
        )

    @validate_call
    @handle_unexpected
    def restore(
        self,
        resource_rid: ResourceRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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
            ),
        )
