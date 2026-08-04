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
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

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
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def calculate(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> media_sets_models.TrackedTransformationResponse:
        """
        Starts calculation of a thumbnail for a given image.

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
        :rtype: media_sets_models.TrackedTransformationResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform/imagery/thumbnail/calculate",
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
                response_type=media_sets_models.TrackedTransformationResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def clear(
        self,
        media_set_rid: core_models.MediaSetRid,
        *,
        media_item_path: core_models.MediaItemPath,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        branch_rid: typing.Optional[media_sets_models.BranchRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        transaction_id: typing.Optional[media_sets_models.TransactionId] = None,
        view_rid: typing.Optional[core_models.MediaSetViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Clears (soft-deletes) the media item at the specified path within a media set, making it and all older
        media items at that path un-retrievable.

        A branch name, branch RID, or view RID may optionally be specified. If none is specified,
        the item will be cleared from the default branch. If more than one is specified, an error is thrown.

        For transactional media sets, a transaction ID must be provided. The deletion will not be
        visible until the transaction is committed.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_path: The path of the media item to clear.
        :type media_item_path: MediaItemPath
        :param branch_name: Specifies the specific branch by name from which this media item will be cleared. May not be provided if branch rid or view rid are provided.
        :type branch_name: Optional[BranchName]
        :param branch_rid: Specifies the specific branch by rid from which this media item will be cleared. May not be provided if branch name or view rid are provided.
        :type branch_rid: Optional[BranchRid]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param transaction_id: The ID of the transaction associated with this request. Required if this is a transactional media set.
        :type transaction_id: Optional[TransactionId]
        :param view_rid: Specifies the specific view by rid from which this media item will be cleared. May not be provided if branch name or branch rid are provided.
        :type view_rid: Optional[MediaSetViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/mediasets/{mediaSetRid}/items/clearAtPath",
                query_params={
                    "mediaItemPath": media_item_path,
                    "branchName": branch_name,
                    "branchRid": branch_rid,
                    "preview": preview,
                    "transactionId": transaction_id,
                    "viewRid": view_rid,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={},
                body=None,
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
                response_type=media_sets_models.TransactionId,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        media_set_rid: core_models.MediaSetRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> media_sets_models.GetMediaSetResponse:
        """
        Gets information about the media set.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: media_sets_models.GetMediaSetResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=media_sets_models.GetMediaSetResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_result(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        transformation_job_id: media_sets_models.TransformationJobId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Gets the result of a completed transformation job. Returns the transformed media content as binary data.
        This endpoint will return an error if the transformation job has not completed successfully.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param transformation_job_id: The ID of the transformation job.
        :type transformation_job_id: TransformationJobId
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param token:
        :type token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transformationJobs/{transformationJobId}/result",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                    "transformationJobId": transformation_job_id,
                },
                header_params={
                    "Token": token,
                    "Accept": "*/*",
                },
                body=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_rid_by_path(
        self,
        media_set_rid: core_models.MediaSetRid,
        *,
        media_item_path: core_models.MediaItemPath,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        branch_rid: typing.Optional[media_sets_models.BranchRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[core_models.MediaSetViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> media_sets_models.GetMediaItemRidByPathResponse:
        """
        Returns the media item RID for the media item with the specified path.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_path: The path of the media item.
        :type media_item_path: MediaItemPath
        :param branch_name: Specifies the specific branch by name in which to search for this media item. May not be provided if branch rid or view rid are provided.
        :type branch_name: Optional[BranchName]
        :param branch_rid: Specifies the specific branch by rid in which to search for this media item. May not be provided if branch name or view rid are provided.
        :type branch_rid: Optional[BranchRid]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param view_rid: Specifies the specific view by rid in which to search for this media item. May not be provided if branch name or branch rid are provided.
        :type view_rid: Optional[MediaSetViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: media_sets_models.GetMediaItemRidByPathResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/getRidByPath",
                query_params={
                    "mediaItemPath": media_item_path,
                    "branchName": branch_name,
                    "branchRid": branch_rid,
                    "preview": preview,
                    "viewRid": view_rid,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=media_sets_models.GetMediaItemRidByPathResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_status(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        transformation_job_id: media_sets_models.TransformationJobId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> media_sets_models.GetTransformationJobStatusResponse:
        """
        Gets the status of a transformation job.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param transformation_job_id: The ID of the transformation job.
        :type transformation_job_id: TransformationJobId
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param token:
        :type token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: media_sets_models.GetTransformationJobStatusResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transformationJobs/{transformationJobId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                    "transformationJobId": transformation_job_id,
                },
                header_params={
                    "Token": token,
                    "Accept": "application/json",
                },
                body=None,
                response_type=media_sets_models.GetTransformationJobStatusResponse,
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
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> media_sets_models.GetMediaItemInfoResponse:
        """
        Gets information about the media item.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
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
                query_params={},
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "application/json",
                },
                body=None,
                response_type=media_sets_models.GetMediaItemInfoResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def metadata(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> media_sets_models.MediaItemMetadata:
        """
        Gets detailed metadata about the media item, including type-specific information
        such as dimensions for images, duration for audio/video, page count for documents, etc.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: media_sets_models.MediaItemMetadata
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/metadata",
                query_params={},
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "application/json",
                },
                body=None,
                response_type=media_sets_models.MediaItemMetadata,
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
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Gets the content of a media item.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
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
                query_params={},
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "*/*",
                },
                body=None,
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
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Gets the content of an original file uploaded to the media item, even if it was transformed on upload due to being an additional input format.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
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
                query_params={},
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "*/*",
                },
                body=None,
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
                response_type=core_models.MediaReference,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def register(
        self,
        media_set_rid: core_models.MediaSetRid,
        *,
        physical_item_name: str,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        media_item_path: typing.Optional[core_models.MediaItemPath] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        transaction_id: typing.Optional[media_sets_models.TransactionId] = None,
        view_rid: typing.Optional[core_models.MediaSetViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> media_sets_models.RegisterMediaItemResponse:
        """
        Registers a media item that currently resides in a federated media store. Registration will validate the item
        against the media set's schema and perform initial metadata extraction.
        This endpoint is only applicable for federated media sets.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param physical_item_name: The relative path within the federated media store where the media item exists.
        :type physical_item_name: str
        :param branch_name: Specifies the specific branch by name to which this media item will be registered.
        :type branch_name: Optional[BranchName]
        :param media_item_path:
        :type media_item_path: Optional[MediaItemPath]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param transaction_id: The id of the transaction associated with this request. Required for transactional media sets.
        :type transaction_id: Optional[TransactionId]
        :param view_rid: Specifies the specific view by rid to which this media item will be registered.
        :type view_rid: Optional[MediaSetViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: media_sets_models.RegisterMediaItemResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/items/register",
                query_params={
                    "branchName": branch_name,
                    "preview": preview,
                    "transactionId": transaction_id,
                    "viewRid": view_rid,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=media_sets_models.RegisterMediaItemRequest(
                    physical_item_name=physical_item_name,
                    media_item_path=media_item_path,
                ),
                response_type=media_sets_models.RegisterMediaItemResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def retrieve(
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
        Retrieves a successfully calculated thumbnail for a given image.

        Thumbnails are 200px wide in the format of `image/webp`

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
        :rtype: bytes
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform/imagery/thumbnail/retrieve",
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
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def transform(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        transformation: media_sets_models.Transformation,
        attribution: typing.Optional[core_models.Attribution] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> media_sets_models.TransformMediaItemResponse:
        """
        Initiates a transformation on a media item. Returns a job ID that can be used to check the status and retrieve
        the result of the transformation.

        Transforming a media item requires that you are able to read the media item, either via `api:mediasets-read` or
        via a `MediaItemReadToken`

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param transformation:
        :type transformation: Transformation
        :param attribution: Optional resource to attribute LLM calls on behalf of.
        :type attribution: Optional[Attribution]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param token:
        :type token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: media_sets_models.TransformMediaItemResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "Attribution": attribution,
                    "Token": token,
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=media_sets_models.TransformMediaItemRequest(
                    transformation=transformation,
                ),
                response_type=media_sets_models.TransformMediaItemResponse,
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
        media_item_rid: typing.Optional[core_models.MediaItemRid] = None,
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
        :param media_item_rid: An optional RID to use for the media item to create. If omitted, the server will automatically generate a RID. In most cases, the server-generated RID should be preferred; only specify a custom RID if your workflow strictly requires deterministic or client-controlled identifiers. The RID must be in the format of `ri.mio.<instance>.media-item.<UUID>`, where `<instance>` is the same as  the instance part of the media set RID, and `<UUID>` is a UUID. An `InvalidMediaItemRid` error will be thrown if the RID is not in the expected format. A `MediaItemRidAlreadyExists` error will be thrown if the media set already contains a media item with the same RID.
        :type media_item_rid: Optional[MediaItemRid]
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
                    "mediaItemRid": media_item_rid,
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
                response_type=media_sets_models.PutMediaItemResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload_media(
        self,
        body: bytes,
        *,
        filename: core_models.MediaItemPath,
        attribution: typing.Optional[core_models.Attribution] = None,
        media_item_rid: typing.Optional[core_models.MediaItemRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core_models.MediaReference:
        """
        Uploads a temporary media item. If the media item isn't persisted within 1 hour, the item will be deleted.

        If multiple resources are attributed to, usage will be attributed to the first one in the list.

        The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
        Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param body: Body of the request
        :type body: bytes
        :param filename: A user-defined label for a media item within a media set. Required if the backing media set requires paths.  Uploading multiple files to the same path will result in only the most recent file being associated with the  path.
        :type filename: MediaItemPath
        :param attribution: used for passing through usage attribution
        :type attribution: Optional[Attribution]
        :param media_item_rid: An optional RID to use for the media item to create. If omitted, the server will automatically generate a RID. In most cases, the server-generated RID should be preferred; only specify a custom RID if your workflow strictly requires deterministic or client-controlled identifiers. The RID must be in the format of `ri.mio.<instance>.media-item.<UUID>`, where `<instance>` is the same as  the instance part of the media set RID, and `<UUID>` is a UUID. An `InvalidMediaItemRid` error will be thrown if the RID is not in the expected format. A `MediaItemRidAlreadyExists` error will be thrown if the media set already contains a media item with the same RID.
        :type media_item_rid: Optional[MediaItemRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core_models.MediaReference
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/mediasets/media/upload",
                query_params={
                    "filename": filename,
                    "mediaItemRid": media_item_rid,
                },
                path_params={},
                header_params={
                    "attribution": attribution,
                    "Content-Type": "*/*",
                    "Accept": "application/json",
                },
                body=body,
                response_type=core_models.MediaReference,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MediaSetClientRaw:
    def __init__(self, client: MediaSetClient) -> None:
        def abort(_: None): ...
        def calculate(_: media_sets_models.TrackedTransformationResponse): ...
        def clear(_: None): ...
        def commit(_: None): ...
        def create(_: media_sets_models.TransactionId): ...
        def get(_: media_sets_models.GetMediaSetResponse): ...
        def get_result(_: bytes): ...
        def get_rid_by_path(_: media_sets_models.GetMediaItemRidByPathResponse): ...
        def get_status(_: media_sets_models.GetTransformationJobStatusResponse): ...
        def info(_: media_sets_models.GetMediaItemInfoResponse): ...
        def metadata(_: media_sets_models.MediaItemMetadata): ...
        def read(_: bytes): ...
        def read_original(_: bytes): ...
        def reference(_: core_models.MediaReference): ...
        def register(_: media_sets_models.RegisterMediaItemResponse): ...
        def retrieve(_: bytes): ...
        def transform(_: media_sets_models.TransformMediaItemResponse): ...
        def upload(_: media_sets_models.PutMediaItemResponse): ...
        def upload_media(_: core_models.MediaReference): ...

        self.abort = core.with_raw_response(abort, client.abort)
        self.calculate = core.with_raw_response(calculate, client.calculate)
        self.clear = core.with_raw_response(clear, client.clear)
        self.commit = core.with_raw_response(commit, client.commit)
        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.get_result = core.with_raw_response(get_result, client.get_result)
        self.get_rid_by_path = core.with_raw_response(get_rid_by_path, client.get_rid_by_path)
        self.get_status = core.with_raw_response(get_status, client.get_status)
        self.info = core.with_raw_response(info, client.info)
        self.metadata = core.with_raw_response(metadata, client.metadata)
        self.read = core.with_raw_response(read, client.read)
        self.read_original = core.with_raw_response(read_original, client.read_original)
        self.reference = core.with_raw_response(reference, client.reference)
        self.register = core.with_raw_response(register, client.register)
        self.retrieve = core.with_raw_response(retrieve, client.retrieve)
        self.transform = core.with_raw_response(transform, client.transform)
        self.upload = core.with_raw_response(upload, client.upload)
        self.upload_media = core.with_raw_response(upload_media, client.upload_media)


class _MediaSetClientStreaming:
    def __init__(self, client: MediaSetClient) -> None:
        def calculate(_: media_sets_models.TrackedTransformationResponse): ...
        def create(_: media_sets_models.TransactionId): ...
        def get(_: media_sets_models.GetMediaSetResponse): ...
        def get_result(_: bytes): ...
        def get_rid_by_path(_: media_sets_models.GetMediaItemRidByPathResponse): ...
        def get_status(_: media_sets_models.GetTransformationJobStatusResponse): ...
        def info(_: media_sets_models.GetMediaItemInfoResponse): ...
        def metadata(_: media_sets_models.MediaItemMetadata): ...
        def read(_: bytes): ...
        def read_original(_: bytes): ...
        def reference(_: core_models.MediaReference): ...
        def register(_: media_sets_models.RegisterMediaItemResponse): ...
        def retrieve(_: bytes): ...
        def transform(_: media_sets_models.TransformMediaItemResponse): ...
        def upload(_: media_sets_models.PutMediaItemResponse): ...
        def upload_media(_: core_models.MediaReference): ...

        self.calculate = core.with_streaming_response(calculate, client.calculate)
        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.get_result = core.with_streaming_response(get_result, client.get_result)
        self.get_rid_by_path = core.with_streaming_response(get_rid_by_path, client.get_rid_by_path)
        self.get_status = core.with_streaming_response(get_status, client.get_status)
        self.info = core.with_streaming_response(info, client.info)
        self.metadata = core.with_streaming_response(metadata, client.metadata)
        self.read = core.with_streaming_response(read, client.read)
        self.read_original = core.with_streaming_response(read_original, client.read_original)
        self.reference = core.with_streaming_response(reference, client.reference)
        self.register = core.with_streaming_response(register, client.register)
        self.retrieve = core.with_streaming_response(retrieve, client.retrieve)
        self.transform = core.with_streaming_response(transform, client.transform)
        self.upload = core.with_streaming_response(upload, client.upload)
        self.upload_media = core.with_streaming_response(upload_media, client.upload_media)


class AsyncMediaSetClient:
    """
    The API client for the MediaSet Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

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
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def calculate(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[media_sets_models.TrackedTransformationResponse]:
        """
        Starts calculation of a thumbnail for a given image.

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
        :rtype: typing.Awaitable[media_sets_models.TrackedTransformationResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform/imagery/thumbnail/calculate",
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
                response_type=media_sets_models.TrackedTransformationResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def clear(
        self,
        media_set_rid: core_models.MediaSetRid,
        *,
        media_item_path: core_models.MediaItemPath,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        branch_rid: typing.Optional[media_sets_models.BranchRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        transaction_id: typing.Optional[media_sets_models.TransactionId] = None,
        view_rid: typing.Optional[core_models.MediaSetViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Clears (soft-deletes) the media item at the specified path within a media set, making it and all older
        media items at that path un-retrievable.

        A branch name, branch RID, or view RID may optionally be specified. If none is specified,
        the item will be cleared from the default branch. If more than one is specified, an error is thrown.

        For transactional media sets, a transaction ID must be provided. The deletion will not be
        visible until the transaction is committed.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_path: The path of the media item to clear.
        :type media_item_path: MediaItemPath
        :param branch_name: Specifies the specific branch by name from which this media item will be cleared. May not be provided if branch rid or view rid are provided.
        :type branch_name: Optional[BranchName]
        :param branch_rid: Specifies the specific branch by rid from which this media item will be cleared. May not be provided if branch name or view rid are provided.
        :type branch_rid: Optional[BranchRid]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param transaction_id: The ID of the transaction associated with this request. Required if this is a transactional media set.
        :type transaction_id: Optional[TransactionId]
        :param view_rid: Specifies the specific view by rid from which this media item will be cleared. May not be provided if branch name or branch rid are provided.
        :type view_rid: Optional[MediaSetViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/mediasets/{mediaSetRid}/items/clearAtPath",
                query_params={
                    "mediaItemPath": media_item_path,
                    "branchName": branch_name,
                    "branchRid": branch_rid,
                    "preview": preview,
                    "transactionId": transaction_id,
                    "viewRid": view_rid,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={},
                body=None,
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
                response_type=media_sets_models.TransactionId,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        media_set_rid: core_models.MediaSetRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[media_sets_models.GetMediaSetResponse]:
        """
        Gets information about the media set.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[media_sets_models.GetMediaSetResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=media_sets_models.GetMediaSetResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_result(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        transformation_job_id: media_sets_models.TransformationJobId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Gets the result of a completed transformation job. Returns the transformed media content as binary data.
        This endpoint will return an error if the transformation job has not completed successfully.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param transformation_job_id: The ID of the transformation job.
        :type transformation_job_id: TransformationJobId
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param token:
        :type token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transformationJobs/{transformationJobId}/result",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                    "transformationJobId": transformation_job_id,
                },
                header_params={
                    "Token": token,
                    "Accept": "*/*",
                },
                body=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_rid_by_path(
        self,
        media_set_rid: core_models.MediaSetRid,
        *,
        media_item_path: core_models.MediaItemPath,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        branch_rid: typing.Optional[media_sets_models.BranchRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[core_models.MediaSetViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[media_sets_models.GetMediaItemRidByPathResponse]:
        """
        Returns the media item RID for the media item with the specified path.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_path: The path of the media item.
        :type media_item_path: MediaItemPath
        :param branch_name: Specifies the specific branch by name in which to search for this media item. May not be provided if branch rid or view rid are provided.
        :type branch_name: Optional[BranchName]
        :param branch_rid: Specifies the specific branch by rid in which to search for this media item. May not be provided if branch name or view rid are provided.
        :type branch_rid: Optional[BranchRid]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param view_rid: Specifies the specific view by rid in which to search for this media item. May not be provided if branch name or branch rid are provided.
        :type view_rid: Optional[MediaSetViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[media_sets_models.GetMediaItemRidByPathResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/getRidByPath",
                query_params={
                    "mediaItemPath": media_item_path,
                    "branchName": branch_name,
                    "branchRid": branch_rid,
                    "preview": preview,
                    "viewRid": view_rid,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=media_sets_models.GetMediaItemRidByPathResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_status(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        transformation_job_id: media_sets_models.TransformationJobId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[media_sets_models.GetTransformationJobStatusResponse]:
        """
        Gets the status of a transformation job.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param transformation_job_id: The ID of the transformation job.
        :type transformation_job_id: TransformationJobId
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param token:
        :type token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[media_sets_models.GetTransformationJobStatusResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transformationJobs/{transformationJobId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                    "transformationJobId": transformation_job_id,
                },
                header_params={
                    "Token": token,
                    "Accept": "application/json",
                },
                body=None,
                response_type=media_sets_models.GetTransformationJobStatusResponse,
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
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[media_sets_models.GetMediaItemInfoResponse]:
        """
        Gets information about the media item.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
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
                query_params={},
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "application/json",
                },
                body=None,
                response_type=media_sets_models.GetMediaItemInfoResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def metadata(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[media_sets_models.MediaItemMetadata]:
        """
        Gets detailed metadata about the media item, including type-specific information
        such as dimensions for images, duration for audio/video, page count for documents, etc.

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param read_token:
        :type read_token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[media_sets_models.MediaItemMetadata]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/metadata",
                query_params={},
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "application/json",
                },
                body=None,
                response_type=media_sets_models.MediaItemMetadata,
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
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Gets the content of a media item.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
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
                query_params={},
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "*/*",
                },
                body=None,
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
        read_token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Gets the content of an original file uploaded to the media item, even if it was transformed on upload due to being an additional input format.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param media_item_rid:
        :type media_item_rid: MediaItemRid
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
                query_params={},
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "ReadToken": read_token,
                    "Accept": "*/*",
                },
                body=None,
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
                response_type=core_models.MediaReference,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def register(
        self,
        media_set_rid: core_models.MediaSetRid,
        *,
        physical_item_name: str,
        branch_name: typing.Optional[media_sets_models.BranchName] = None,
        media_item_path: typing.Optional[core_models.MediaItemPath] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        transaction_id: typing.Optional[media_sets_models.TransactionId] = None,
        view_rid: typing.Optional[core_models.MediaSetViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[media_sets_models.RegisterMediaItemResponse]:
        """
        Registers a media item that currently resides in a federated media store. Registration will validate the item
        against the media set's schema and perform initial metadata extraction.
        This endpoint is only applicable for federated media sets.

        :param media_set_rid:
        :type media_set_rid: MediaSetRid
        :param physical_item_name: The relative path within the federated media store where the media item exists.
        :type physical_item_name: str
        :param branch_name: Specifies the specific branch by name to which this media item will be registered.
        :type branch_name: Optional[BranchName]
        :param media_item_path:
        :type media_item_path: Optional[MediaItemPath]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param transaction_id: The id of the transaction associated with this request. Required for transactional media sets.
        :type transaction_id: Optional[TransactionId]
        :param view_rid: Specifies the specific view by rid to which this media item will be registered.
        :type view_rid: Optional[MediaSetViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[media_sets_models.RegisterMediaItemResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/items/register",
                query_params={
                    "branchName": branch_name,
                    "preview": preview,
                    "transactionId": transaction_id,
                    "viewRid": view_rid,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=media_sets_models.RegisterMediaItemRequest(
                    physical_item_name=physical_item_name,
                    media_item_path=media_item_path,
                ),
                response_type=media_sets_models.RegisterMediaItemResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def retrieve(
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
        Retrieves a successfully calculated thumbnail for a given image.

        Thumbnails are 200px wide in the format of `image/webp`

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
        :rtype: typing.Awaitable[bytes]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform/imagery/thumbnail/retrieve",
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
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def transform(
        self,
        media_set_rid: core_models.MediaSetRid,
        media_item_rid: core_models.MediaItemRid,
        *,
        transformation: media_sets_models.Transformation,
        attribution: typing.Optional[core_models.Attribution] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        token: typing.Optional[core_models.MediaItemReadToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[media_sets_models.TransformMediaItemResponse]:
        """
        Initiates a transformation on a media item. Returns a job ID that can be used to check the status and retrieve
        the result of the transformation.

        Transforming a media item requires that you are able to read the media item, either via `api:mediasets-read` or
        via a `MediaItemReadToken`

        :param media_set_rid: The RID of the media set.
        :type media_set_rid: MediaSetRid
        :param media_item_rid: The RID of the media item.
        :type media_item_rid: MediaItemRid
        :param transformation:
        :type transformation: Transformation
        :param attribution: Optional resource to attribute LLM calls on behalf of.
        :type attribution: Optional[Attribution]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param token:
        :type token: Optional[MediaItemReadToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[media_sets_models.TransformMediaItemResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mediaSetRid": media_set_rid,
                    "mediaItemRid": media_item_rid,
                },
                header_params={
                    "Attribution": attribution,
                    "Token": token,
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=media_sets_models.TransformMediaItemRequest(
                    transformation=transformation,
                ),
                response_type=media_sets_models.TransformMediaItemResponse,
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
        media_item_rid: typing.Optional[core_models.MediaItemRid] = None,
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
        :param media_item_rid: An optional RID to use for the media item to create. If omitted, the server will automatically generate a RID. In most cases, the server-generated RID should be preferred; only specify a custom RID if your workflow strictly requires deterministic or client-controlled identifiers. The RID must be in the format of `ri.mio.<instance>.media-item.<UUID>`, where `<instance>` is the same as  the instance part of the media set RID, and `<UUID>` is a UUID. An `InvalidMediaItemRid` error will be thrown if the RID is not in the expected format. A `MediaItemRidAlreadyExists` error will be thrown if the media set already contains a media item with the same RID.
        :type media_item_rid: Optional[MediaItemRid]
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
                    "mediaItemRid": media_item_rid,
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
                response_type=media_sets_models.PutMediaItemResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload_media(
        self,
        body: bytes,
        *,
        filename: core_models.MediaItemPath,
        attribution: typing.Optional[core_models.Attribution] = None,
        media_item_rid: typing.Optional[core_models.MediaItemRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[core_models.MediaReference]:
        """
        Uploads a temporary media item. If the media item isn't persisted within 1 hour, the item will be deleted.

        If multiple resources are attributed to, usage will be attributed to the first one in the list.

        The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
        Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param body: Body of the request
        :type body: bytes
        :param filename: A user-defined label for a media item within a media set. Required if the backing media set requires paths.  Uploading multiple files to the same path will result in only the most recent file being associated with the  path.
        :type filename: MediaItemPath
        :param attribution: used for passing through usage attribution
        :type attribution: Optional[Attribution]
        :param media_item_rid: An optional RID to use for the media item to create. If omitted, the server will automatically generate a RID. In most cases, the server-generated RID should be preferred; only specify a custom RID if your workflow strictly requires deterministic or client-controlled identifiers. The RID must be in the format of `ri.mio.<instance>.media-item.<UUID>`, where `<instance>` is the same as  the instance part of the media set RID, and `<UUID>` is a UUID. An `InvalidMediaItemRid` error will be thrown if the RID is not in the expected format. A `MediaItemRidAlreadyExists` error will be thrown if the media set already contains a media item with the same RID.
        :type media_item_rid: Optional[MediaItemRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[core_models.MediaReference]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/mediasets/media/upload",
                query_params={
                    "filename": filename,
                    "mediaItemRid": media_item_rid,
                },
                path_params={},
                header_params={
                    "attribution": attribution,
                    "Content-Type": "*/*",
                    "Accept": "application/json",
                },
                body=body,
                response_type=core_models.MediaReference,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncMediaSetClientRaw:
    def __init__(self, client: AsyncMediaSetClient) -> None:
        def abort(_: None): ...
        def calculate(_: media_sets_models.TrackedTransformationResponse): ...
        def clear(_: None): ...
        def commit(_: None): ...
        def create(_: media_sets_models.TransactionId): ...
        def get(_: media_sets_models.GetMediaSetResponse): ...
        def get_result(_: bytes): ...
        def get_rid_by_path(_: media_sets_models.GetMediaItemRidByPathResponse): ...
        def get_status(_: media_sets_models.GetTransformationJobStatusResponse): ...
        def info(_: media_sets_models.GetMediaItemInfoResponse): ...
        def metadata(_: media_sets_models.MediaItemMetadata): ...
        def read(_: bytes): ...
        def read_original(_: bytes): ...
        def reference(_: core_models.MediaReference): ...
        def register(_: media_sets_models.RegisterMediaItemResponse): ...
        def retrieve(_: bytes): ...
        def transform(_: media_sets_models.TransformMediaItemResponse): ...
        def upload(_: media_sets_models.PutMediaItemResponse): ...
        def upload_media(_: core_models.MediaReference): ...

        self.abort = core.async_with_raw_response(abort, client.abort)
        self.calculate = core.async_with_raw_response(calculate, client.calculate)
        self.clear = core.async_with_raw_response(clear, client.clear)
        self.commit = core.async_with_raw_response(commit, client.commit)
        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_result = core.async_with_raw_response(get_result, client.get_result)
        self.get_rid_by_path = core.async_with_raw_response(get_rid_by_path, client.get_rid_by_path)
        self.get_status = core.async_with_raw_response(get_status, client.get_status)
        self.info = core.async_with_raw_response(info, client.info)
        self.metadata = core.async_with_raw_response(metadata, client.metadata)
        self.read = core.async_with_raw_response(read, client.read)
        self.read_original = core.async_with_raw_response(read_original, client.read_original)
        self.reference = core.async_with_raw_response(reference, client.reference)
        self.register = core.async_with_raw_response(register, client.register)
        self.retrieve = core.async_with_raw_response(retrieve, client.retrieve)
        self.transform = core.async_with_raw_response(transform, client.transform)
        self.upload = core.async_with_raw_response(upload, client.upload)
        self.upload_media = core.async_with_raw_response(upload_media, client.upload_media)


class _AsyncMediaSetClientStreaming:
    def __init__(self, client: AsyncMediaSetClient) -> None:
        def calculate(_: media_sets_models.TrackedTransformationResponse): ...
        def create(_: media_sets_models.TransactionId): ...
        def get(_: media_sets_models.GetMediaSetResponse): ...
        def get_result(_: bytes): ...
        def get_rid_by_path(_: media_sets_models.GetMediaItemRidByPathResponse): ...
        def get_status(_: media_sets_models.GetTransformationJobStatusResponse): ...
        def info(_: media_sets_models.GetMediaItemInfoResponse): ...
        def metadata(_: media_sets_models.MediaItemMetadata): ...
        def read(_: bytes): ...
        def read_original(_: bytes): ...
        def reference(_: core_models.MediaReference): ...
        def register(_: media_sets_models.RegisterMediaItemResponse): ...
        def retrieve(_: bytes): ...
        def transform(_: media_sets_models.TransformMediaItemResponse): ...
        def upload(_: media_sets_models.PutMediaItemResponse): ...
        def upload_media(_: core_models.MediaReference): ...

        self.calculate = core.async_with_streaming_response(calculate, client.calculate)
        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_result = core.async_with_streaming_response(get_result, client.get_result)
        self.get_rid_by_path = core.async_with_streaming_response(
            get_rid_by_path, client.get_rid_by_path
        )
        self.get_status = core.async_with_streaming_response(get_status, client.get_status)
        self.info = core.async_with_streaming_response(info, client.info)
        self.metadata = core.async_with_streaming_response(metadata, client.metadata)
        self.read = core.async_with_streaming_response(read, client.read)
        self.read_original = core.async_with_streaming_response(read_original, client.read_original)
        self.reference = core.async_with_streaming_response(reference, client.reference)
        self.register = core.async_with_streaming_response(register, client.register)
        self.retrieve = core.async_with_streaming_response(retrieve, client.retrieve)
        self.transform = core.async_with_streaming_response(transform, client.transform)
        self.upload = core.async_with_streaming_response(upload, client.upload)
        self.upload_media = core.async_with_streaming_response(upload_media, client.upload_media)
