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
from foundry_sdk.v2.media_sets import models as media_sets_models


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

        self.with_streaming_response = _MediaSetClientStreaming(self)
        self.with_raw_response = _MediaSetClientRaw(self)

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
        _sdk_internal: core.SdkInternal = {},
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
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
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
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
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> core_models.MediaReference:
        """
        Gets the [media reference](https://palantir.com/docs/foundry/data-integration/media-sets/#media-references) for this media item.

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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MediaSetClientRaw:
    def __init__(self, client: MediaSetClient) -> None:
        def abort(_: None): ...
        def commit(_: None): ...
        def create(_: media_sets_models.TransactionId): ...
        def info(_: media_sets_models.GetMediaItemInfoResponse): ...
        def read(_: bytes): ...
        def read_original(_: bytes): ...
        def reference(_: core_models.MediaReference): ...
        def upload(_: media_sets_models.PutMediaItemResponse): ...

        self.abort = core.with_raw_response(abort, client.abort)
        self.commit = core.with_raw_response(commit, client.commit)
        self.create = core.with_raw_response(create, client.create)
        self.info = core.with_raw_response(info, client.info)
        self.read = core.with_raw_response(read, client.read)
        self.read_original = core.with_raw_response(read_original, client.read_original)
        self.reference = core.with_raw_response(reference, client.reference)
        self.upload = core.with_raw_response(upload, client.upload)


class _MediaSetClientStreaming:
    def __init__(self, client: MediaSetClient) -> None:
        def create(_: media_sets_models.TransactionId): ...
        def info(_: media_sets_models.GetMediaItemInfoResponse): ...
        def read(_: bytes): ...
        def read_original(_: bytes): ...
        def reference(_: core_models.MediaReference): ...
        def upload(_: media_sets_models.PutMediaItemResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.info = core.with_streaming_response(info, client.info)
        self.read = core.with_streaming_response(read, client.read)
        self.read_original = core.with_streaming_response(read_original, client.read_original)
        self.reference = core.with_streaming_response(reference, client.reference)
        self.upload = core.with_streaming_response(upload, client.upload)


class AsyncMediaSetClient:
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
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncMediaSetClientStreaming(self)
        self.with_raw_response = _AsyncMediaSetClientRaw(self)

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
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
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
        :rtype: typing.Awaitable[None]
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
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
        :rtype: typing.Awaitable[None]
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[media_sets_models.TransactionId]:
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
        :rtype: typing.Awaitable[media_sets_models.TransactionId]
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[media_sets_models.GetMediaItemInfoResponse]:
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
        :rtype: typing.Awaitable[media_sets_models.GetMediaItemInfoResponse]
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
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
        :rtype: typing.Awaitable[bytes]
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
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
        :rtype: typing.Awaitable[bytes]
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[core_models.MediaReference]:
        """
        Gets the [media reference](https://palantir.com/docs/foundry/data-integration/media-sets/#media-references) for this media item.

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
        :rtype: typing.Awaitable[core_models.MediaReference]
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
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[media_sets_models.PutMediaItemResponse]:
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
        :rtype: typing.Awaitable[media_sets_models.PutMediaItemResponse]
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
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncMediaSetClientRaw:
    def __init__(self, client: AsyncMediaSetClient) -> None:
        def abort(_: None): ...
        def commit(_: None): ...
        def create(_: media_sets_models.TransactionId): ...
        def info(_: media_sets_models.GetMediaItemInfoResponse): ...
        def read(_: bytes): ...
        def read_original(_: bytes): ...
        def reference(_: core_models.MediaReference): ...
        def upload(_: media_sets_models.PutMediaItemResponse): ...

        self.abort = core.async_with_raw_response(abort, client.abort)
        self.commit = core.async_with_raw_response(commit, client.commit)
        self.create = core.async_with_raw_response(create, client.create)
        self.info = core.async_with_raw_response(info, client.info)
        self.read = core.async_with_raw_response(read, client.read)
        self.read_original = core.async_with_raw_response(read_original, client.read_original)
        self.reference = core.async_with_raw_response(reference, client.reference)
        self.upload = core.async_with_raw_response(upload, client.upload)


class _AsyncMediaSetClientStreaming:
    def __init__(self, client: AsyncMediaSetClient) -> None:
        def create(_: media_sets_models.TransactionId): ...
        def info(_: media_sets_models.GetMediaItemInfoResponse): ...
        def read(_: bytes): ...
        def read_original(_: bytes): ...
        def reference(_: core_models.MediaReference): ...
        def upload(_: media_sets_models.PutMediaItemResponse): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.info = core.async_with_streaming_response(info, client.info)
        self.read = core.async_with_streaming_response(read, client.read)
        self.read_original = core.async_with_streaming_response(read_original, client.read_original)
        self.reference = core.async_with_streaming_response(reference, client.reference)
        self.upload = core.async_with_streaming_response(upload, client.upload)
