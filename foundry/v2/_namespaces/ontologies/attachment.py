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
from foundry.v2.models._attachment_rid import AttachmentRid
from foundry.v2.models._attachment_v2 import AttachmentV2
from foundry.v2.models._content_length import ContentLength
from foundry.v2.models._content_type import ContentType
from foundry.v2.models._filename import Filename


class AttachmentResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def get(
        self,
        attachment_rid: AttachmentRid,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> AttachmentV2:
        """
        Get the metadata of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: attachmentRid
        :type attachment_rid: AttachmentRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AttachmentV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None

        _path_params["attachmentRid"] = attachment_rid

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/attachments/{attachmentRid}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=AttachmentV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def read(
        self,
        attachment_rid: AttachmentRid,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> bytes:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: attachmentRid
        :type attachment_rid: AttachmentRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None

        _path_params["attachmentRid"] = attachment_rid

        _header_params["Accept"] = "*/*"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/attachments/{attachmentRid}/content",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def upload(
        self,
        body: bytes,
        *,
        content_length: ContentLength,
        content_type: ContentType,
        filename: Filename,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> AttachmentV2:
        """
        Upload an attachment to use in an action. Any attachment which has not been linked to an object via
        an action within one hour after upload will be removed.
        Previously mapped attachments which are not connected to any object anymore are also removed on
        a biweekly basis.
        The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-write`.

        :param body: Body of the request
        :type body: bytes
        :param content_length: Content-Length
        :type content_length: ContentLength
        :param content_type: Content-Type
        :type content_type: ContentType
        :param filename: filename
        :type filename: Filename
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AttachmentV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = body
        _query_params["filename"] = filename

        _header_params["Content-Length"] = content_length

        _header_params["Content-Type"] = content_type

        _header_params["Content-Type"] = "*/*"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/attachments/upload",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=bytes,
                response_type=AttachmentV2,
                request_timeout=request_timeout,
            ),
        )
