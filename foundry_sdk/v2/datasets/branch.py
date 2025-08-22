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
from foundry_sdk.v2.core import errors as core_errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.datasets import errors as datasets_errors
from foundry_sdk.v2.datasets import models as datasets_models


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

        self.with_streaming_response = _BranchClientStreaming(self)
        self.with_raw_response = _BranchClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        name: datasets_models.BranchName,
        transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.Branch:
        """
        Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param name:
        :type name: BranchName
        :param transaction_rid: The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction.
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.Branch

        :raises BranchAlreadyExists: The branch cannot be created because a branch with that name already exists.
        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CreateBranchPermissionDenied: The provided token does not have permission to create a branch of this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises InvalidBranchName: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises TransactionNotCommitted: The given transaction has not been committed.
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/branches",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "transactionRid": transaction_rid,
                    "name": name,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "transactionRid": typing.Optional[datasets_models.TransactionRid],
                        "name": datasets_models.BranchName,
                    },
                ),
                response_type=datasets_models.Branch,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchAlreadyExists": datasets_errors.BranchAlreadyExists,
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CreateBranchPermissionDenied": datasets_errors.CreateBranchPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "InvalidBranchName": datasets_errors.InvalidBranchName,
                    "TransactionNotCommitted": datasets_errors.TransactionNotCommitted,
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_name: datasets_models.BranchName,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Deletes the Branch with the given BranchName.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name:
        :type branch_name: BranchName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DeleteBranchPermissionDenied: The provided token does not have permission to delete the given branch from this dataset.
        :raises InvalidBranchName: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/datasets/{datasetRid}/branches/{branchName}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "branchName": branch_name,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "DeleteBranchPermissionDenied": datasets_errors.DeleteBranchPermissionDenied,
                    "InvalidBranchName": datasets_errors.InvalidBranchName,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_name: datasets_models.BranchName,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.Branch:
        """
        Get a Branch of a Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name:
        :type branch_name: BranchName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.Branch

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/branches/{branchName}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "branchName": branch_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.Branch,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[datasets_models.Branch]:
        """
        Lists the Branches of a Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[datasets_models.Branch]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/branches",
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
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "InvalidPageSize": core_errors.InvalidPageSize,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def transactions(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_name: datasets_models.BranchName,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[datasets_models.Transaction]:
        """
        Get the Transaction history for the given Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name:
        :type branch_name: BranchName
        :param page_size: The default pageSize is 20 transactions and the maximum allowed pageSize is 50 transactions
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[datasets_models.Transaction]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises GetBranchTransactionHistoryPermissionDenied: Could not transactions the Branch.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/branches/{branchName}/transactions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "branchName": branch_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.ListTransactionsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "GetBranchTransactionHistoryPermissionDenied": datasets_errors.GetBranchTransactionHistoryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _BranchClientRaw:
    def __init__(self, client: BranchClient) -> None:
        def create(_: datasets_models.Branch): ...
        def delete(_: None): ...
        def get(_: datasets_models.Branch): ...
        def list(_: datasets_models.ListBranchesResponse): ...
        def transactions(_: datasets_models.ListTransactionsResponse): ...

        self.create = core.with_raw_response(create, client.create)
        self.delete = core.with_raw_response(delete, client.delete)
        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)
        self.transactions = core.with_raw_response(transactions, client.transactions)


class _BranchClientStreaming:
    def __init__(self, client: BranchClient) -> None:
        def create(_: datasets_models.Branch): ...
        def get(_: datasets_models.Branch): ...
        def list(_: datasets_models.ListBranchesResponse): ...
        def transactions(_: datasets_models.ListTransactionsResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)
        self.transactions = core.with_streaming_response(transactions, client.transactions)


class AsyncBranchClient:
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
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncBranchClientStreaming(self)
        self.with_raw_response = _AsyncBranchClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        name: datasets_models.BranchName,
        transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.Branch]:
        """
        Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param name:
        :type name: BranchName
        :param transaction_rid: The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction.
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.Branch]

        :raises BranchAlreadyExists: The branch cannot be created because a branch with that name already exists.
        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CreateBranchPermissionDenied: The provided token does not have permission to create a branch of this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises InvalidBranchName: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises TransactionNotCommitted: The given transaction has not been committed.
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/branches",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "transactionRid": transaction_rid,
                    "name": name,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "transactionRid": typing.Optional[datasets_models.TransactionRid],
                        "name": datasets_models.BranchName,
                    },
                ),
                response_type=datasets_models.Branch,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchAlreadyExists": datasets_errors.BranchAlreadyExists,
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CreateBranchPermissionDenied": datasets_errors.CreateBranchPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "InvalidBranchName": datasets_errors.InvalidBranchName,
                    "TransactionNotCommitted": datasets_errors.TransactionNotCommitted,
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_name: datasets_models.BranchName,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Deletes the Branch with the given BranchName.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name:
        :type branch_name: BranchName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DeleteBranchPermissionDenied: The provided token does not have permission to delete the given branch from this dataset.
        :raises InvalidBranchName: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/datasets/{datasetRid}/branches/{branchName}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "branchName": branch_name,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "DeleteBranchPermissionDenied": datasets_errors.DeleteBranchPermissionDenied,
                    "InvalidBranchName": datasets_errors.InvalidBranchName,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_name: datasets_models.BranchName,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.Branch]:
        """
        Get a Branch of a Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name:
        :type branch_name: BranchName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.Branch]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/branches/{branchName}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "branchName": branch_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.Branch,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[datasets_models.Branch]:
        """
        Lists the Branches of a Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[datasets_models.Branch]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises InvalidPageSize: The provided page size was zero or negative. Page sizes must be greater than zero.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/branches",
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
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "InvalidPageSize": core_errors.InvalidPageSize,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def transactions(
        self,
        dataset_rid: datasets_models.DatasetRid,
        branch_name: datasets_models.BranchName,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[datasets_models.Transaction]:
        """
        Get the Transaction history for the given Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name:
        :type branch_name: BranchName
        :param page_size: The default pageSize is 20 transactions and the maximum allowed pageSize is 50 transactions
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[datasets_models.Transaction]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises GetBranchTransactionHistoryPermissionDenied: Could not transactions the Branch.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/branches/{branchName}/transactions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "branchName": branch_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.ListTransactionsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "GetBranchTransactionHistoryPermissionDenied": datasets_errors.GetBranchTransactionHistoryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncBranchClientRaw:
    def __init__(self, client: AsyncBranchClient) -> None:
        def create(_: datasets_models.Branch): ...
        def delete(_: None): ...
        def get(_: datasets_models.Branch): ...
        def list(_: datasets_models.ListBranchesResponse): ...
        def transactions(_: datasets_models.ListTransactionsResponse): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.delete = core.async_with_raw_response(delete, client.delete)
        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)
        self.transactions = core.async_with_raw_response(transactions, client.transactions)


class _AsyncBranchClientStreaming:
    def __init__(self, client: AsyncBranchClient) -> None:
        def create(_: datasets_models.Branch): ...
        def get(_: datasets_models.Branch): ...
        def list(_: datasets_models.ListBranchesResponse): ...
        def transactions(_: datasets_models.ListTransactionsResponse): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
        self.transactions = core.async_with_streaming_response(transactions, client.transactions)
