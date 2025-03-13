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
from foundry.v1.core import models as core_models
from foundry.v1.datasets import models as datasets_models


class BranchClient:
    """
    The API client for the Branch Resource.

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
        self.with_streaming_response = _BranchClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _BranchClientRaw(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_id: datasets_models.BranchId,
        transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> datasets_models.Branch:
        """
        Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to create the Branch.
        :type dataset_rid: DatasetRid
        :param branch_id:
        :type branch_id: BranchId
        :param transaction_rid:
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.Branch
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/datasets/{datasetRid}/branches",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branchId": branch_id,
                    "transactionRid": transaction_rid,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branchId": datasets_models.BranchId,
                        "transactionRid": typing.Optional[datasets_models.TransactionRid],
                    },
                ),
                response_type=datasets_models.Branch,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_id: datasets_models.BranchId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Deletes the Branch with the given BranchId.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset that contains the Branch.
        :type dataset_rid: DatasetRid
        :param branch_id: The identifier (name) of the Branch.
        :type branch_id: BranchId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v1/datasets/{datasetRid}/branches/{branchId}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "branchId": branch_id,
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
    def get(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_id: datasets_models.BranchId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> datasets_models.Branch:
        """
        Get a Branch of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset that contains the Branch.
        :type dataset_rid: DatasetRid
        :param branch_id: The identifier (name) of the Branch.
        :type branch_id: BranchId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.Branch
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/branches/{branchId}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "branchId": branch_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.Branch,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[datasets_models.Branch]:
        """
        Lists the Branches of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to list Branches.
        :type dataset_rid: DatasetRid
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[datasets_models.Branch]
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/branches",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> datasets_models.ListBranchesResponse:
        """
        Lists the Branches of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to list Branches.
        :type dataset_rid: DatasetRid
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.ListBranchesResponse
        """

        warnings.warn(
            "The client.datasets.Branch.page(...) method has been deprecated. Please use client.datasets.Branch.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/branches",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()


class _BranchClientRaw:
    """
    The API client for the Branch Resource.

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
    def create(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_id: datasets_models.BranchId,
        transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[datasets_models.Branch]:
        """
        Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to create the Branch.
        :type dataset_rid: DatasetRid
        :param branch_id:
        :type branch_id: BranchId
        :param transaction_rid:
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[datasets_models.Branch]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/datasets/{datasetRid}/branches",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branchId": branch_id,
                    "transactionRid": transaction_rid,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branchId": datasets_models.BranchId,
                        "transactionRid": typing.Optional[datasets_models.TransactionRid],
                    },
                ),
                response_type=datasets_models.Branch,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_id: datasets_models.BranchId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Deletes the Branch with the given BranchId.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset that contains the Branch.
        :type dataset_rid: DatasetRid
        :param branch_id: The identifier (name) of the Branch.
        :type branch_id: BranchId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v1/datasets/{datasetRid}/branches/{branchId}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "branchId": branch_id,
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
    def get(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_id: datasets_models.BranchId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[datasets_models.Branch]:
        """
        Get a Branch of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset that contains the Branch.
        :type dataset_rid: DatasetRid
        :param branch_id: The identifier (name) of the Branch.
        :type branch_id: BranchId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[datasets_models.Branch]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/branches/{branchId}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "branchId": branch_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.Branch,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[datasets_models.ListBranchesResponse]:
        """
        Lists the Branches of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to list Branches.
        :type dataset_rid: DatasetRid
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[datasets_models.ListBranchesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/branches",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[datasets_models.ListBranchesResponse]:
        """
        Lists the Branches of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to list Branches.
        :type dataset_rid: DatasetRid
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[datasets_models.ListBranchesResponse]
        """

        warnings.warn(
            "The client.datasets.Branch.page(...) method has been deprecated. Please use client.datasets.Branch.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/branches",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )


class _BranchClientStreaming:
    """
    The API client for the Branch Resource.

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
    def create(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_id: datasets_models.BranchId,
        transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[datasets_models.Branch]:
        """
        Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to create the Branch.
        :type dataset_rid: DatasetRid
        :param branch_id:
        :type branch_id: BranchId
        :param transaction_rid:
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[datasets_models.Branch]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/datasets/{datasetRid}/branches",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branchId": branch_id,
                    "transactionRid": transaction_rid,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branchId": datasets_models.BranchId,
                        "transactionRid": typing.Optional[datasets_models.TransactionRid],
                    },
                ),
                response_type=datasets_models.Branch,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_id: datasets_models.BranchId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Deletes the Branch with the given BranchId.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset that contains the Branch.
        :type dataset_rid: DatasetRid
        :param branch_id: The identifier (name) of the Branch.
        :type branch_id: BranchId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v1/datasets/{datasetRid}/branches/{branchId}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "branchId": branch_id,
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
    def get(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_id: datasets_models.BranchId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[datasets_models.Branch]:
        """
        Get a Branch of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset that contains the Branch.
        :type dataset_rid: DatasetRid
        :param branch_id: The identifier (name) of the Branch.
        :type branch_id: BranchId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[datasets_models.Branch]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/branches/{branchId}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "branchId": branch_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.Branch,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[datasets_models.ListBranchesResponse]:
        """
        Lists the Branches of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to list Branches.
        :type dataset_rid: DatasetRid
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[datasets_models.ListBranchesResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/branches",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[datasets_models.ListBranchesResponse]:
        """
        Lists the Branches of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to list Branches.
        :type dataset_rid: DatasetRid
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[datasets_models.ListBranchesResponse]
        """

        warnings.warn(
            "The client.datasets.Branch.page(...) method has been deprecated. Please use client.datasets.Branch.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/branches",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
