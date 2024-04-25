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

from typing import Annotated
from typing import Any
from typing import Dict
from typing import Optional

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call

from foundry._errors import handle_unexpected
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.models._preview_mode import PreviewMode
from foundry.models._principal_id import PrincipalId
from foundry.models._user import User


class UserResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def delete(
        self,
        user_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """
        Deletes the given User
        :param user_id: userId
        :type user_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["preview"] = preview

        _path_params["userId"] = user_id

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/security/users/{userId}".format(**_path_params),
                query_params=_query_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        user_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> User:
        """
        Get the User
        :param user_id: userId
        :type user_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: User
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["preview"] = preview

        _path_params["userId"] = user_id

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/security/users/{userId}".format(**_path_params),
                query_params=_query_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=User,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def me(
        self,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> User:
        """

        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: User
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["preview"] = preview

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/security/users/me",
                query_params=_query_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=User,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def profile_picture(
        self,
        user_id: PrincipalId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> bytes:
        """

        :param user_id: userId
        :type user_id: PrincipalId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["preview"] = preview

        _path_params["userId"] = user_id

        _header_params["Accept"] = "application/octet-stream"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/security/users/{userId}/profilePicture".format(**_path_params),
                query_params=_query_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
            ),
        )
