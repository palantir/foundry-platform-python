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
from foundry_sdk.v2.ontologies import models as ontologies_models


class AttachmentClient:
    """
    The API client for the Attachment Resource.

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

        self.with_streaming_response = _AttachmentClientStreaming(self)
        self.with_raw_response = _AttachmentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        attachment_rid: ontologies_models.AttachmentRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.AttachmentV2:
        """
        Get the metadata of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.AttachmentV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/attachments/{attachmentRid}",
                query_params={},
                path_params={
                    "attachmentRid": attachment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.AttachmentV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def read(
        self,
        attachment_rid: ontologies_models.AttachmentRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/attachments/{attachmentRid}/content",
                query_params={},
                path_params={
                    "attachmentRid": attachment_rid,
                },
                header_params={
                    "Accept": "*/*",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload(
        self,
        body: bytes,
        *,
        content_length: core_models.ContentLength,
        content_type: core_models.ContentType,
        filename: core_models.Filename,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.AttachmentV2:
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
        :param content_length: The size in bytes of the file content being uploaded.
        :type content_length: ContentLength
        :param content_type: The media type of the file being uploaded.
        :type content_type: ContentType
        :param filename: The name of the file being uploaded.
        :type filename: Filename
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.AttachmentV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/attachments/upload",
                query_params={
                    "filename": filename,
                },
                path_params={},
                header_params={
                    "Content-Length": content_length,
                    "Content-Type": content_type,
                    "Content-Type": "*/*",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=ontologies_models.AttachmentV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AttachmentClientRaw:
    def __init__(self, client: AttachmentClient) -> None:
        def get(_: ontologies_models.AttachmentV2): ...
        def read(_: bytes): ...
        def upload(_: ontologies_models.AttachmentV2): ...

        self.get = core.with_raw_response(get, client.get)
        self.read = core.with_raw_response(read, client.read)
        self.upload = core.with_raw_response(upload, client.upload)


class _AttachmentClientStreaming:
    def __init__(self, client: AttachmentClient) -> None:
        def get(_: ontologies_models.AttachmentV2): ...
        def read(_: bytes): ...
        def upload(_: ontologies_models.AttachmentV2): ...

        self.get = core.with_streaming_response(get, client.get)
        self.read = core.with_streaming_response(read, client.read)
        self.upload = core.with_streaming_response(upload, client.upload)


class AsyncAttachmentClient:
    """
    The API client for the Attachment Resource.

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

        self.with_streaming_response = _AsyncAttachmentClientStreaming(self)
        self.with_raw_response = _AsyncAttachmentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        attachment_rid: ontologies_models.AttachmentRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.AttachmentV2]:
        """
        Get the metadata of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.AttachmentV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/attachments/{attachmentRid}",
                query_params={},
                path_params={
                    "attachmentRid": attachment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.AttachmentV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def read(
        self,
        attachment_rid: ontologies_models.AttachmentRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/attachments/{attachmentRid}/content",
                query_params={},
                path_params={
                    "attachmentRid": attachment_rid,
                },
                header_params={
                    "Accept": "*/*",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload(
        self,
        body: bytes,
        *,
        content_length: core_models.ContentLength,
        content_type: core_models.ContentType,
        filename: core_models.Filename,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.AttachmentV2]:
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
        :param content_length: The size in bytes of the file content being uploaded.
        :type content_length: ContentLength
        :param content_type: The media type of the file being uploaded.
        :type content_type: ContentType
        :param filename: The name of the file being uploaded.
        :type filename: Filename
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.AttachmentV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/attachments/upload",
                query_params={
                    "filename": filename,
                },
                path_params={},
                header_params={
                    "Content-Length": content_length,
                    "Content-Type": content_type,
                    "Content-Type": "*/*",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=ontologies_models.AttachmentV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncAttachmentClientRaw:
    def __init__(self, client: AsyncAttachmentClient) -> None:
        def get(_: ontologies_models.AttachmentV2): ...
        def read(_: bytes): ...
        def upload(_: ontologies_models.AttachmentV2): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.read = core.async_with_raw_response(read, client.read)
        self.upload = core.async_with_raw_response(upload, client.upload)


class _AsyncAttachmentClientStreaming:
    def __init__(self, client: AsyncAttachmentClient) -> None:
        def get(_: ontologies_models.AttachmentV2): ...
        def read(_: bytes): ...
        def upload(_: ontologies_models.AttachmentV2): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.read = core.async_with_streaming_response(read, client.read)
        self.upload = core.async_with_streaming_response(upload, client.upload)
