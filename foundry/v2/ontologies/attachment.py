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

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.ontologies import models as ontologies_models


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
        self.with_streaming_response = _AttachmentClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _AttachmentClientRaw(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        attachment_rid: ontologies_models.AttachmentRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
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
            ),
        ).decode()

    @typing_extensions.overload
    @typing_extensions.deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def read(
        self,
        attachment_rid: ontologies_models.AttachmentRid,
        *,
        stream: typing.Literal[True],
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.BinaryStream:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.BinaryStream
        """
        ...

    @typing_extensions.overload
    def read(
        self,
        attachment_rid: ontologies_models.AttachmentRid,
        *,
        stream: typing.Literal[False] = False,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> bytes:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """
        ...

    @typing_extensions.overload
    @typing_extensions.deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def read(
        self,
        attachment_rid: ontologies_models.AttachmentRid,
        *,
        stream: bool,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Union[bytes, core.BinaryStream]:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Union[bytes, core.BinaryStream]
        """
        ...

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def read(
        self,
        attachment_rid: ontologies_models.AttachmentRid,
        *,
        stream: bool = False,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Union[bytes, core.BinaryStream]:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Union[bytes, core.BinaryStream]
        """

        if stream:
            warnings.warn(
                f"client.ontologies.Attachment.read(..., stream=True, chunk_size={chunk_size}) is deprecated. Please use:\n\nwith client.ontologies.Attachment.with_streaming_response.read(...) as response:\n    response.iter_bytes(chunk_size={chunk_size})\n",
                DeprecationWarning,
                stacklevel=2,
            )

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
                stream=stream,
                chunk_size=chunk_size,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

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
            ),
        ).decode()


class _AttachmentClientRaw:
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        attachment_rid: ontologies_models.AttachmentRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.AttachmentV2]:
        """
        Get the metadata of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.AttachmentV2]
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
    ) -> core.ApiResponse[bytes]:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[bytes]
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
    ) -> core.ApiResponse[ontologies_models.AttachmentV2]:
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
        :rtype: core.ApiResponse[ontologies_models.AttachmentV2]
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
            ),
        )


class _AttachmentClientStreaming:
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        attachment_rid: ontologies_models.AttachmentRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.AttachmentV2]:
        """
        Get the metadata of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.AttachmentV2]
        """

        return self._api_client.stream_api(
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
    ) -> core.StreamingContextManager[bytes]:
        """
        Get the content of an attachment.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param attachment_rid: The RID of the attachment.
        :type attachment_rid: AttachmentRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[bytes]
        """

        return self._api_client.stream_api(
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
    ) -> core.StreamingContextManager[ontologies_models.AttachmentV2]:
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
        :rtype: core.StreamingContextManager[ontologies_models.AttachmentV2]
        """

        return self._api_client.stream_api(
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
            ),
        )
