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
from typing import Union

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call

from foundry._errors import handle_unexpected
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.v1.models._branch_id import BranchId
from foundry.v1.models._create_transaction_request import CreateTransactionRequest
from foundry.v1.models._create_transaction_request_dict import CreateTransactionRequestDict  # NOQA
from foundry.v1.models._dataset_rid import DatasetRid
from foundry.v1.models._transaction import Transaction
from foundry.v1.models._transaction_rid import TransactionRid


class TransactionResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def abort(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Transaction:
        """
        Aborts an open Transaction. File modifications made on this Transaction are not preserved and the Branch is
        not updated.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Transaction
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None

        _path_params["datasetRid"] = dataset_rid

        _path_params["transactionRid"] = transaction_rid

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v1/datasets/{datasetRid}/transactions/{transactionRid}/abort",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def commit(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Transaction:
        """
        Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
        updated to point to the Transaction.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Transaction
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None

        _path_params["datasetRid"] = dataset_rid

        _path_params["transactionRid"] = transaction_rid

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v1/datasets/{datasetRid}/transactions/{transactionRid}/commit",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def create(
        self,
        dataset_rid: DatasetRid,
        create_transaction_request: Union[CreateTransactionRequest, CreateTransactionRequestDict],
        *,
        branch_id: Optional[BranchId] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Transaction:
        """
        Creates a Transaction on a Branch of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param create_transaction_request: Body of the request
        :type create_transaction_request: Union[CreateTransactionRequest, CreateTransactionRequestDict]
        :param branch_id: branchId
        :type branch_id: Optional[BranchId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Transaction
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = create_transaction_request
        _query_params["branchId"] = branch_id

        _path_params["datasetRid"] = dataset_rid

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v1/datasets/{datasetRid}/transactions",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[CreateTransactionRequest, CreateTransactionRequestDict],
                response_type=Transaction,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        transaction_rid: TransactionRid,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Transaction:
        """
        Gets a Transaction of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param transaction_rid: transactionRid
        :type transaction_rid: TransactionRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Transaction
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None

        _path_params["datasetRid"] = dataset_rid

        _path_params["transactionRid"] = transaction_rid

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/transactions/{transactionRid}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=Transaction,
                request_timeout=request_timeout,
            ),
        )
