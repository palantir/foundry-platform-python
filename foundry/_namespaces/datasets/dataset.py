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
from typing import List
from typing import Optional
from typing import Union

from pydantic import Field
from pydantic import StrictInt
from pydantic import StrictStr
from pydantic import validate_call

from foundry._errors import handle_unexpected
from foundry._namespaces.datasets.branch import BranchResource
from foundry._namespaces.datasets.file import FileResource
from foundry._namespaces.datasets.transaction import TransactionResource
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.models._branch_id import BranchId
from foundry.models._create_dataset_request import CreateDatasetRequest
from foundry.models._create_dataset_request_dict import CreateDatasetRequestDict
from foundry.models._dataset import Dataset
from foundry.models._dataset_rid import DatasetRid
from foundry.models._preview_mode import PreviewMode
from foundry.models._table_export_format import TableExportFormat
from foundry.models._transaction_rid import TransactionRid


class DatasetResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

        self.Branch = BranchResource(api_client=api_client)
        self.File = FileResource(api_client=api_client)
        self.Transaction = TransactionResource(api_client=api_client)

    @validate_call
    @handle_unexpected
    def create(
        self,
        create_dataset_request: Union[CreateDatasetRequest, CreateDatasetRequestDict],
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param create_dataset_request: Body of the request
        :type create_dataset_request: Union[CreateDatasetRequest, CreateDatasetRequestDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = create_dataset_request

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v1/datasets",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[CreateDatasetRequest, CreateDatasetRequestDict],
                response_type=Dataset,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def delete_schema(
        self,
        dataset_rid: DatasetRid,
        *,
        branch_id: Optional[BranchId] = None,
        preview: Optional[PreviewMode] = None,
        transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """
        Deletes the Schema from a Dataset and Branch.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_id: branchId
        :type branch_id: Optional[BranchId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param transaction_rid: transactionRid
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["branchId"] = branch_id

        _query_params["preview"] = preview

        _query_params["transactionRid"] = transaction_rid

        _path_params["datasetRid"] = dataset_rid

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v1/datasets/{datasetRid}/schema",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Gets the Dataset with the given DatasetRid.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=Dataset,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get_schema(
        self,
        dataset_rid: DatasetRid,
        *,
        branch_id: Optional[BranchId] = None,
        preview: Optional[PreviewMode] = None,
        transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Any:
        """
        Retrieves the Schema for a Dataset and Branch, if it exists.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_id: branchId
        :type branch_id: Optional[BranchId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param transaction_rid: transactionRid
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Any
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["branchId"] = branch_id

        _query_params["preview"] = preview

        _query_params["transactionRid"] = transaction_rid

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/schema",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=Any,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def read(
        self,
        dataset_rid: DatasetRid,
        *,
        columns: List[StrictStr],
        format: TableExportFormat,
        branch_id: Optional[BranchId] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        row_limit: Optional[StrictInt] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> bytes:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (Virtual datasets composed of other datasets).

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param columns: columns
        :type columns: List[StrictStr]
        :param format: format
        :type format: TableExportFormat
        :param branch_id: branchId
        :type branch_id: Optional[BranchId]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param row_limit: rowLimit
        :type row_limit: Optional[StrictInt]
        :param start_transaction_rid: startTransactionRid
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["columns"] = columns

        _query_params["format"] = format

        _query_params["branchId"] = branch_id

        _query_params["endTransactionRid"] = end_transaction_rid

        _query_params["rowLimit"] = row_limit

        _query_params["startTransactionRid"] = start_transaction_rid

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "*/*"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/readTable",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def replace_schema(
        self,
        dataset_rid: DatasetRid,
        body: Any,
        *,
        branch_id: Optional[BranchId] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """
        Puts a Schema on an existing Dataset and Branch.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param body: Body of the request
        :type body: Any
        :param branch_id: branchId
        :type branch_id: Optional[BranchId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = body
        _query_params["branchId"] = branch_id

        _query_params["preview"] = preview

        _path_params["datasetRid"] = dataset_rid

        _header_params["Content-Type"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v1/datasets/{datasetRid}/schema",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Any,
                response_type=None,
                request_timeout=request_timeout,
            ),
        )
