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

from functools import cached_property
from typing import Any
from typing import Dict
from typing import Optional

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.core.models._build_rid import BuildRid
from foundry.v2.core.models._job_rid import JobRid
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.datasets import errors as datasets_errors
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid
from foundry.v2.datasets.models._transaction import Transaction
from foundry.v2.datasets.models._transaction_rid import TransactionRid
from foundry.v2.datasets.models._transaction_type import TransactionType


class TransactionClient:
    """
    The API client for the Transaction Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _TransactionClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _TransactionClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def abort(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Transaction:
        """
        Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
        not updated.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Transaction

        :raises AbortTransactionPermissionDenied: The provided token does not have permission to abort the given transaction on the given dataset.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/abort",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "AbortTransactionPermissionDenied": datasets_errors.AbortTransactionPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def build(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Optional[BuildRid]:
        """
        Get the [Build](/docs/foundry/data-integration/builds#builds) that computed the
        given Transaction. Not all Transactions have an associated Build. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Build will be tied to the Transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Optional[BuildRid]

        :raises BuildTransactionPermissionDenied: Could not build the Transaction.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/build",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Optional[BuildRid],
                request_timeout=request_timeout,
                throwable_errors={
                    "BuildTransactionPermissionDenied": datasets_errors.BuildTransactionPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def commit(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Transaction:
        """
        Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
        updated to point to the Transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Transaction

        :raises CommitTransactionPermissionDenied: The provided token does not have permission to commit the given transaction on the given dataset.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/commit",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "CommitTransactionPermissionDenied": datasets_errors.CommitTransactionPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        dataset_rid: DatasetRid,
        *,
        transaction_type: TransactionType,
        branch_name: Optional[BranchName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Transaction:
        """
        Creates a Transaction on a Branch of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_type:
        :type transaction_type: TransactionType
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Transaction

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CreateTransactionPermissionDenied: The provided token does not have permission to create a transaction on this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises OpenTransactionAlreadyExists: A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/transactions",
                query_params={
                    "branchName": branch_name,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "transactionType": transaction_type,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "transactionType": TransactionType,
                    },
                ),
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CreateTransactionPermissionDenied": datasets_errors.CreateTransactionPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "OpenTransactionAlreadyExists": datasets_errors.OpenTransactionAlreadyExists,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Transaction:
        """
        Gets a Transaction of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Transaction

        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def job(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Optional[JobRid]:
        """
        Get the [Job](/docs/foundry/data-integration/builds#jobs-and-jobspecs) that computed the
        given Transaction. Not all Transactions have an associated Job. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Job will be tied to the Transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Optional[JobRid]

        :raises JobTransactionPermissionDenied: Could not job the Transaction.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/job",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Optional[JobRid],
                request_timeout=request_timeout,
                throwable_errors={
                    "JobTransactionPermissionDenied": datasets_errors.JobTransactionPermissionDenied,
                },
            ),
        ).decode()


class _TransactionClientRaw:
    """
    The API client for the Transaction Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def abort(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Transaction]:
        """
        Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
        not updated.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Transaction]

        :raises AbortTransactionPermissionDenied: The provided token does not have permission to abort the given transaction on the given dataset.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/abort",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "AbortTransactionPermissionDenied": datasets_errors.AbortTransactionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def build(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Optional[BuildRid]]:
        """
        Get the [Build](/docs/foundry/data-integration/builds#builds) that computed the
        given Transaction. Not all Transactions have an associated Build. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Build will be tied to the Transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Optional[BuildRid]]

        :raises BuildTransactionPermissionDenied: Could not build the Transaction.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/build",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Optional[BuildRid],
                request_timeout=request_timeout,
                throwable_errors={
                    "BuildTransactionPermissionDenied": datasets_errors.BuildTransactionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def commit(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Transaction]:
        """
        Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
        updated to point to the Transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Transaction]

        :raises CommitTransactionPermissionDenied: The provided token does not have permission to commit the given transaction on the given dataset.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/commit",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "CommitTransactionPermissionDenied": datasets_errors.CommitTransactionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        dataset_rid: DatasetRid,
        *,
        transaction_type: TransactionType,
        branch_name: Optional[BranchName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Transaction]:
        """
        Creates a Transaction on a Branch of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_type:
        :type transaction_type: TransactionType
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Transaction]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CreateTransactionPermissionDenied: The provided token does not have permission to create a transaction on this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises OpenTransactionAlreadyExists: A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/transactions",
                query_params={
                    "branchName": branch_name,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "transactionType": transaction_type,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "transactionType": TransactionType,
                    },
                ),
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CreateTransactionPermissionDenied": datasets_errors.CreateTransactionPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "OpenTransactionAlreadyExists": datasets_errors.OpenTransactionAlreadyExists,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Transaction]:
        """
        Gets a Transaction of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Transaction]

        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def job(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Optional[JobRid]]:
        """
        Get the [Job](/docs/foundry/data-integration/builds#jobs-and-jobspecs) that computed the
        given Transaction. Not all Transactions have an associated Job. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Job will be tied to the Transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Optional[JobRid]]

        :raises JobTransactionPermissionDenied: Could not job the Transaction.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/job",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Optional[JobRid],
                request_timeout=request_timeout,
                throwable_errors={
                    "JobTransactionPermissionDenied": datasets_errors.JobTransactionPermissionDenied,
                },
            ),
        )


class _TransactionClientStreaming:
    """
    The API client for the Transaction Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def abort(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Transaction]:
        """
        Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
        not updated.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Transaction]

        :raises AbortTransactionPermissionDenied: The provided token does not have permission to abort the given transaction on the given dataset.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/abort",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "AbortTransactionPermissionDenied": datasets_errors.AbortTransactionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def build(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Optional[BuildRid]]:
        """
        Get the [Build](/docs/foundry/data-integration/builds#builds) that computed the
        given Transaction. Not all Transactions have an associated Build. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Build will be tied to the Transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Optional[BuildRid]]

        :raises BuildTransactionPermissionDenied: Could not build the Transaction.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/build",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Optional[BuildRid],
                request_timeout=request_timeout,
                throwable_errors={
                    "BuildTransactionPermissionDenied": datasets_errors.BuildTransactionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def commit(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Transaction]:
        """
        Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
        updated to point to the Transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Transaction]

        :raises CommitTransactionPermissionDenied: The provided token does not have permission to commit the given transaction on the given dataset.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/commit",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "CommitTransactionPermissionDenied": datasets_errors.CommitTransactionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        dataset_rid: DatasetRid,
        *,
        transaction_type: TransactionType,
        branch_name: Optional[BranchName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Transaction]:
        """
        Creates a Transaction on a Branch of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_type:
        :type transaction_type: TransactionType
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Transaction]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CreateTransactionPermissionDenied: The provided token does not have permission to create a transaction on this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises OpenTransactionAlreadyExists: A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/transactions",
                query_params={
                    "branchName": branch_name,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "transactionType": transaction_type,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "transactionType": TransactionType,
                    },
                ),
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CreateTransactionPermissionDenied": datasets_errors.CreateTransactionPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "OpenTransactionAlreadyExists": datasets_errors.OpenTransactionAlreadyExists,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Transaction]:
        """
        Gets a Transaction of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Transaction]

        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def job(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Optional[JobRid]]:
        """
        Get the [Job](/docs/foundry/data-integration/builds#jobs-and-jobspecs) that computed the
        given Transaction. Not all Transactions have an associated Job. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Job will be tied to the Transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Optional[JobRid]]

        :raises JobTransactionPermissionDenied: Could not job the Transaction.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/transactions/{transactionRid}/job",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "transactionRid": transaction_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Optional[JobRid],
                request_timeout=request_timeout,
                throwable_errors={
                    "JobTransactionPermissionDenied": datasets_errors.JobTransactionPermissionDenied,
                },
            ),
        )
