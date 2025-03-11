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
from foundry.v2.media_sets import models as media_sets_models


class MediaSetClient:
    """
    The API client for the MediaSet Resource.

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
        self.with_streaming_response = _MediaSetClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _MediaSetClientRaw(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def abort(
        self,
        media_set_rid: core_models.MediaSetRid,
        transaction_id: media_sets_models.TransactionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Aborts an open transaction. Items uploaded to the media set during this transaction will be deleted.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param transaction_id:
        :type transaction_id: TransactionId
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/transactions/{transactionId}/abort",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "transactionId": transaction_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def commit(
        self,
        media_set_rid: core_models.MediaSetRid,
        transaction_id: media_sets_models.TransactionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Commits an open transaction. On success, items uploaded to the media set during this transaction will become available.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param transaction_id:
        :type transaction_id: TransactionId
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/transactions/{transactionId}/commit",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "transactionId": transaction_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        media_set_rid: core_models.MediaSetRid,
        *,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> media_sets_models.TransactionId:
        """
        Creates a new transaction. Items uploaded to the media set while this transaction is open will not be reflected until the transaction is committed.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param branch_name: The branch on which to open the transaction. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: media_sets_models.TransactionId
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/transactions",
                query_params={
                    "branchName": branch_name,
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=media_sets_models.TransactionId,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def info(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> media_sets_models.GetMediaItemInfoResponse:
        """
        Gets information about the media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: media_sets_models.GetMediaItemInfoResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=media_sets_models.GetMediaItemInfoResponse,
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
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        stream: typing.Literal[True],
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.BinaryStream:
        """
        Gets the content of a media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
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
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        stream: typing.Literal[False] = False,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> bytes:
        """
        Gets the content of a media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
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
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        stream: bool,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Union[bytes, core.BinaryStream]:
        """
        Gets the content of a media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
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
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        stream: bool = False,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Union[bytes, core.BinaryStream]:
        """
        Gets the content of a media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
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
                f"client.media_sets.MediaSet.read(..., stream=True, chunk_size={chunk_size}) is deprecated. Please use:\n\nwith client.media_sets.MediaSet.with_streaming_response.read(...) as response:\n    response.iter_bytes(chunk_size={chunk_size})\n",
                DeprecationWarning,
                stacklevel=2,
            )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/content",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
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

    @typing_extensions.overload
    @typing_extensions.deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def read_original(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        stream: typing.Literal[True],
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.BinaryStream:
        """
        Gets the content of an original file uploaded to the media item, even if it was transformed on upload due to being an additional input format.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
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
    def read_original(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        stream: typing.Literal[False] = False,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> bytes:
        """
        Gets the content of an original file uploaded to the media item, even if it was transformed on upload due to being an additional input format.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
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
    def read_original(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        stream: bool,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Union[bytes, core.BinaryStream]:
        """
        Gets the content of an original file uploaded to the media item, even if it was transformed on upload due to being an additional input format.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
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
    def read_original(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        stream: bool = False,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Union[bytes, core.BinaryStream]:
        """
        Gets the content of an original file uploaded to the media item, even if it was transformed on upload due to being an additional input format.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
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
                f"client.media_sets.MediaSet.read_original(..., stream=True, chunk_size={chunk_size}) is deprecated. Please use:\n\nwith client.media_sets.MediaSet.with_streaming_response.read_original(...) as response:\n    response.iter_bytes(chunk_size={chunk_size})\n",
                DeprecationWarning,
                stacklevel=2,
            )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/original",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
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
    def reference(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core_models.MediaReference:
        """
        Gets the [media reference](/docs/foundry/data-integration/media-sets/#media-references) for this media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core_models.MediaReference
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/reference",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=core_models.MediaReference,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload(
        self,
        media_set_rid: core_models.MediaSetRid,
        body: bytes,
        *,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        branch_rid: typing.Optional[media_sets_models.BranchRid] = None,
        media_item_path: typing.Optional[core_models.MediaItemPath] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        transaction_id: typing.Optional[media_sets_models.TransactionId] = None,
        view_rid: typing.Optional[core_models.MediaSetViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> media_sets_models.PutMediaItemResponse:
        """
        Uploads a media item to an existing media set.
        The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
        A branch name, or branch rid, or view rid may optionally be specified.  If none is specified, the item will be uploaded to the default branch. If more than one is specified, an error is thrown.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param body: Body of the request
        :type body: bytes
        :param branch_name: Specifies the specific branch by name to which this media item will be uploaded. May not be provided if branch rid or view rid are provided.
        :type branch_name: Optional[BranchName]
        :param branch_rid: Specifies the specific branch by rid to which this media item will be uploaded. May not be provided if branch name or view rid are provided.
        :type branch_rid: Optional[BranchRid]
        :param media_item_path: An identifier for a media item within a media set. Necessary if the backing media set requires paths.
        :type media_item_path: Optional[MediaItemPath]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param transaction_id: The id of the transaction associated with this request.  Required if this is a transactional media set.
        :type transaction_id: Optional[TransactionId]
        :param view_rid: Specifies the specific view by rid to which this media item will be uploaded. May not be provided if branch name or branch rid are provided.
        :type view_rid: Optional[MediaSetViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: media_sets_models.PutMediaItemResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/items",
                query_params={
                    "branchName": branch_name,
                    "branchRid": branch_rid,
                    "mediaItemPath": media_item_path,
                    "preview": preview,
                    "transactionId": transaction_id,
                    "viewRid": view_rid,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Content-Type": "*/*",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=media_sets_models.PutMediaItemResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()


class _MediaSetClientRaw:
    """
    The API client for the MediaSet Resource.

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
    def abort(
        self,
        media_set_rid: core_models.MediaSetRid,
        transaction_id: media_sets_models.TransactionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Aborts an open transaction. Items uploaded to the media set during this transaction will be deleted.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param transaction_id:
        :type transaction_id: TransactionId
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/transactions/{transactionId}/abort",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "transactionId": transaction_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def commit(
        self,
        media_set_rid: core_models.MediaSetRid,
        transaction_id: media_sets_models.TransactionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Commits an open transaction. On success, items uploaded to the media set during this transaction will become available.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param transaction_id:
        :type transaction_id: TransactionId
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/transactions/{transactionId}/commit",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "transactionId": transaction_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        media_set_rid: core_models.MediaSetRid,
        *,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[media_sets_models.TransactionId]:
        """
        Creates a new transaction. Items uploaded to the media set while this transaction is open will not be reflected until the transaction is committed.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param branch_name: The branch on which to open the transaction. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[media_sets_models.TransactionId]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/transactions",
                query_params={
                    "branchName": branch_name,
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=media_sets_models.TransactionId,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def info(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[media_sets_models.GetMediaItemInfoResponse]:
        """
        Gets information about the media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[media_sets_models.GetMediaItemInfoResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=media_sets_models.GetMediaItemInfoResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def read(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[bytes]:
        """
        Gets the content of a media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[bytes]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/content",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
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
    def read_original(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[bytes]:
        """
        Gets the content of an original file uploaded to the media item, even if it was transformed on upload due to being an additional input format.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[bytes]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/original",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
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
    def reference(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[core_models.MediaReference]:
        """
        Gets the [media reference](/docs/foundry/data-integration/media-sets/#media-references) for this media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[core_models.MediaReference]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/reference",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=core_models.MediaReference,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload(
        self,
        media_set_rid: core_models.MediaSetRid,
        body: bytes,
        *,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        branch_rid: typing.Optional[media_sets_models.BranchRid] = None,
        media_item_path: typing.Optional[core_models.MediaItemPath] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        transaction_id: typing.Optional[media_sets_models.TransactionId] = None,
        view_rid: typing.Optional[core_models.MediaSetViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[media_sets_models.PutMediaItemResponse]:
        """
        Uploads a media item to an existing media set.
        The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
        A branch name, or branch rid, or view rid may optionally be specified.  If none is specified, the item will be uploaded to the default branch. If more than one is specified, an error is thrown.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param body: Body of the request
        :type body: bytes
        :param branch_name: Specifies the specific branch by name to which this media item will be uploaded. May not be provided if branch rid or view rid are provided.
        :type branch_name: Optional[BranchName]
        :param branch_rid: Specifies the specific branch by rid to which this media item will be uploaded. May not be provided if branch name or view rid are provided.
        :type branch_rid: Optional[BranchRid]
        :param media_item_path: An identifier for a media item within a media set. Necessary if the backing media set requires paths.
        :type media_item_path: Optional[MediaItemPath]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param transaction_id: The id of the transaction associated with this request.  Required if this is a transactional media set.
        :type transaction_id: Optional[TransactionId]
        :param view_rid: Specifies the specific view by rid to which this media item will be uploaded. May not be provided if branch name or branch rid are provided.
        :type view_rid: Optional[MediaSetViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[media_sets_models.PutMediaItemResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/items",
                query_params={
                    "branchName": branch_name,
                    "branchRid": branch_rid,
                    "mediaItemPath": media_item_path,
                    "preview": preview,
                    "transactionId": transaction_id,
                    "viewRid": view_rid,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Content-Type": "*/*",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=media_sets_models.PutMediaItemResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )


class _MediaSetClientStreaming:
    """
    The API client for the MediaSet Resource.

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
    def abort(
        self,
        media_set_rid: core_models.MediaSetRid,
        transaction_id: media_sets_models.TransactionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Aborts an open transaction. Items uploaded to the media set during this transaction will be deleted.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param transaction_id:
        :type transaction_id: TransactionId
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/transactions/{transactionId}/abort",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "transactionId": transaction_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def commit(
        self,
        media_set_rid: core_models.MediaSetRid,
        transaction_id: media_sets_models.TransactionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Commits an open transaction. On success, items uploaded to the media set during this transaction will become available.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param transaction_id:
        :type transaction_id: TransactionId
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/transactions/{transactionId}/commit",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "transactionId": transaction_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        media_set_rid: core_models.MediaSetRid,
        *,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[media_sets_models.TransactionId]:
        """
        Creates a new transaction. Items uploaded to the media set while this transaction is open will not be reflected until the transaction is committed.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param branch_name: The branch on which to open the transaction. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[media_sets_models.TransactionId]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/transactions",
                query_params={
                    "branchName": branch_name,
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=media_sets_models.TransactionId,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def info(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[media_sets_models.GetMediaItemInfoResponse]:
        """
        Gets information about the media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[media_sets_models.GetMediaItemInfoResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=media_sets_models.GetMediaItemInfoResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def read(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[bytes]:
        """
        Gets the content of a media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[bytes]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/content",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
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
    def read_original(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[bytes]:
        """
        Gets the content of an original file uploaded to the media item, even if it was transformed on upload due to being an additional input format.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[bytes]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/original",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
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
    def reference(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[core_models.MediaReference]:
        """
        Gets the [media reference](/docs/foundry/data-integration/media-sets/#media-references) for this media item.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[core_models.MediaReference]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/reference",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=core_models.MediaReference,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload(
        self,
        media_set_rid: core_models.MediaSetRid,
        body: bytes,
        *,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        branch_rid: typing.Optional[media_sets_models.BranchRid] = None,
        media_item_path: typing.Optional[core_models.MediaItemPath] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        transaction_id: typing.Optional[media_sets_models.TransactionId] = None,
        view_rid: typing.Optional[core_models.MediaSetViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[media_sets_models.PutMediaItemResponse]:
        """
        Uploads a media item to an existing media set.
        The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
        A branch name, or branch rid, or view rid may optionally be specified.  If none is specified, the item will be uploaded to the default branch. If more than one is specified, an error is thrown.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param body: Body of the request
        :type body: bytes
        :param branch_name: Specifies the specific branch by name to which this media item will be uploaded. May not be provided if branch rid or view rid are provided.
        :type branch_name: Optional[BranchName]
        :param branch_rid: Specifies the specific branch by rid to which this media item will be uploaded. May not be provided if branch name or view rid are provided.
        :type branch_rid: Optional[BranchRid]
        :param media_item_path: An identifier for a media item within a media set. Necessary if the backing media set requires paths.
        :type media_item_path: Optional[MediaItemPath]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param transaction_id: The id of the transaction associated with this request.  Required if this is a transactional media set.
        :type transaction_id: Optional[TransactionId]
        :param view_rid: Specifies the specific view by rid to which this media item will be uploaded. May not be provided if branch name or branch rid are provided.
        :type view_rid: Optional[MediaSetViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[media_sets_models.PutMediaItemResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/items",
                query_params={
                    "branchName": branch_name,
                    "branchRid": branch_rid,
                    "mediaItemPath": media_item_path,
                    "preview": preview,
                    "transactionId": transaction_id,
                    "viewRid": view_rid,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Content-Type": "*/*",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=media_sets_models.PutMediaItemResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
