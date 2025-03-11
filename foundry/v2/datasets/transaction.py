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

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.datasets import errors as datasets_errors
from foundry.v2.datasets import models as datasets_models


class TransactionClient:
    """
    The API client for the Transaction Resource.

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
        self.with_streaming_response = _TransactionClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _TransactionClientRaw(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def abort(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> datasets_models.Transaction:
        """
        Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
        not updated.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.Transaction

        :raises AbortTransactionPermissionDenied: The provided token does not have permission to abort the given transaction on the given dataset.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "AbortTransactionPermissionDenied": datasets_errors.AbortTransactionPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def build(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Optional[core_models.BuildRid]:
        """
        Get the [Build](/docs/foundry/data-integration/builds#builds) that computed the
        given Transaction. Not all Transactions have an associated Build. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Build will be tied to the Transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Optional[core_models.BuildRid]

        :raises BuildTransactionPermissionDenied: Could not build the Transaction.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=typing.Optional[core_models.BuildRid],
                request_timeout=request_timeout,
                throwable_errors={
                    "BuildTransactionPermissionDenied": datasets_errors.BuildTransactionPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def commit(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> datasets_models.Transaction:
        """
        Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
        updated to point to the Transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.Transaction

        :raises CommitTransactionPermissionDenied: The provided token does not have permission to commit the given transaction on the given dataset.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "CommitTransactionPermissionDenied": datasets_errors.CommitTransactionPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        transaction_type: datasets_models.TransactionType,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> datasets_models.Transaction:
        """
        Creates a Transaction on a Branch of a Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_type:
        :type transaction_type: TransactionType
        :param branch_name: The name of the Branch on which to create the Transaction. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.Transaction

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CreateTransactionPermissionDenied: The provided token does not have permission to create a transaction on this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises OpenTransactionAlreadyExists: A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "transactionType": datasets_models.TransactionType,
                    },
                ),
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CreateTransactionPermissionDenied": datasets_errors.CreateTransactionPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "OpenTransactionAlreadyExists": datasets_errors.OpenTransactionAlreadyExists,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> datasets_models.Transaction:
        """
        Gets a Transaction of a Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.Transaction

        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def job(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Optional[core_models.JobRid]:
        """
        Get the [Job](/docs/foundry/data-integration/builds#jobs-and-jobspecs) that computed the
        given Transaction. Not all Transactions have an associated Job. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Job will be tied to the Transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Optional[core_models.JobRid]

        :raises JobTransactionPermissionDenied: Could not job the Transaction.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=typing.Optional[core_models.JobRid],
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
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[datasets_models.Transaction]:
        """
        Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
        not updated.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[datasets_models.Transaction]

        :raises AbortTransactionPermissionDenied: The provided token does not have permission to abort the given transaction on the given dataset.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "AbortTransactionPermissionDenied": datasets_errors.AbortTransactionPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def build(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[typing.Optional[core_models.BuildRid]]:
        """
        Get the [Build](/docs/foundry/data-integration/builds#builds) that computed the
        given Transaction. Not all Transactions have an associated Build. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Build will be tied to the Transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[typing.Optional[core_models.BuildRid]]

        :raises BuildTransactionPermissionDenied: Could not build the Transaction.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=typing.Optional[core_models.BuildRid],
                request_timeout=request_timeout,
                throwable_errors={
                    "BuildTransactionPermissionDenied": datasets_errors.BuildTransactionPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def commit(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[datasets_models.Transaction]:
        """
        Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
        updated to point to the Transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[datasets_models.Transaction]

        :raises CommitTransactionPermissionDenied: The provided token does not have permission to commit the given transaction on the given dataset.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "CommitTransactionPermissionDenied": datasets_errors.CommitTransactionPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        transaction_type: datasets_models.TransactionType,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[datasets_models.Transaction]:
        """
        Creates a Transaction on a Branch of a Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_type:
        :type transaction_type: TransactionType
        :param branch_name: The name of the Branch on which to create the Transaction. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[datasets_models.Transaction]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CreateTransactionPermissionDenied: The provided token does not have permission to create a transaction on this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises OpenTransactionAlreadyExists: A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "transactionType": datasets_models.TransactionType,
                    },
                ),
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CreateTransactionPermissionDenied": datasets_errors.CreateTransactionPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "OpenTransactionAlreadyExists": datasets_errors.OpenTransactionAlreadyExists,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[datasets_models.Transaction]:
        """
        Gets a Transaction of a Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[datasets_models.Transaction]

        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def job(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[typing.Optional[core_models.JobRid]]:
        """
        Get the [Job](/docs/foundry/data-integration/builds#jobs-and-jobspecs) that computed the
        given Transaction. Not all Transactions have an associated Job. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Job will be tied to the Transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[typing.Optional[core_models.JobRid]]

        :raises JobTransactionPermissionDenied: Could not job the Transaction.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=typing.Optional[core_models.JobRid],
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
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[datasets_models.Transaction]:
        """
        Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
        not updated.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[datasets_models.Transaction]

        :raises AbortTransactionPermissionDenied: The provided token does not have permission to abort the given transaction on the given dataset.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "AbortTransactionPermissionDenied": datasets_errors.AbortTransactionPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def build(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[typing.Optional[core_models.BuildRid]]:
        """
        Get the [Build](/docs/foundry/data-integration/builds#builds) that computed the
        given Transaction. Not all Transactions have an associated Build. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Build will be tied to the Transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[typing.Optional[core_models.BuildRid]]

        :raises BuildTransactionPermissionDenied: Could not build the Transaction.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=typing.Optional[core_models.BuildRid],
                request_timeout=request_timeout,
                throwable_errors={
                    "BuildTransactionPermissionDenied": datasets_errors.BuildTransactionPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def commit(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[datasets_models.Transaction]:
        """
        Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
        updated to point to the Transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[datasets_models.Transaction]

        :raises CommitTransactionPermissionDenied: The provided token does not have permission to commit the given transaction on the given dataset.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "CommitTransactionPermissionDenied": datasets_errors.CommitTransactionPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        transaction_type: datasets_models.TransactionType,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[datasets_models.Transaction]:
        """
        Creates a Transaction on a Branch of a Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_type:
        :type transaction_type: TransactionType
        :param branch_name: The name of the Branch on which to create the Transaction. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[datasets_models.Transaction]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CreateTransactionPermissionDenied: The provided token does not have permission to create a transaction on this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises OpenTransactionAlreadyExists: A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "transactionType": datasets_models.TransactionType,
                    },
                ),
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CreateTransactionPermissionDenied": datasets_errors.CreateTransactionPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "OpenTransactionAlreadyExists": datasets_errors.OpenTransactionAlreadyExists,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[datasets_models.Transaction]:
        """
        Gets a Transaction of a Dataset.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[datasets_models.Transaction]

        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=datasets_models.Transaction,
                request_timeout=request_timeout,
                throwable_errors={
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def job(
        self,
        dataset_rid: datasets_models.DatasetRid,
        transaction_rid: datasets_models.TransactionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[typing.Optional[core_models.JobRid]]:
        """
        Get the [Job](/docs/foundry/data-integration/builds#jobs-and-jobspecs) that computed the
        given Transaction. Not all Transactions have an associated Job. For example, if a Dataset
        is updated by a User uploading a CSV file into the browser, no Job will be tied to the Transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param transaction_rid:
        :type transaction_rid: TransactionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[typing.Optional[core_models.JobRid]]

        :raises JobTransactionPermissionDenied: Could not job the Transaction.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=typing.Optional[core_models.JobRid],
                request_timeout=request_timeout,
                throwable_errors={
                    "JobTransactionPermissionDenied": datasets_errors.JobTransactionPermissionDenied,
                },
            ),
        )
