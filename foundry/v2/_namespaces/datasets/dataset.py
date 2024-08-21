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
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.v2._namespaces.datasets.branch import BranchResource
from foundry.v2._namespaces.datasets.file import FileResource
from foundry.v2._namespaces.datasets.transaction import TransactionResource
from foundry.v2.models._branch_name import BranchName
from foundry.v2.models._create_dataset_request import CreateDatasetRequest
from foundry.v2.models._create_dataset_request_dict import CreateDatasetRequestDict
from foundry.v2.models._dataset import Dataset
from foundry.v2.models._dataset_rid import DatasetRid
from foundry.v2.models._preview_mode import PreviewMode
from foundry.v2.models._table_export_format import TableExportFormat
from foundry.v2.models._transaction_rid import TransactionRid


class DatasetResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

        self.Branch = BranchResource(api_client=api_client)
        self.Transaction = TransactionResource(api_client=api_client)
        self.File = FileResource(api_client=api_client)

    @validate_call
    @handle_unexpected
    def create(
        self,
        create_dataset_request: Union[CreateDatasetRequest, CreateDatasetRequestDict],
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        :param create_dataset_request: Body of the request
        :type create_dataset_request: Union[CreateDatasetRequest, CreateDatasetRequestDict]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = create_dataset_request
        _query_params["preview"] = preview

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets",
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
    def get(
        self,
        dataset_rid: DatasetRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Get the Dataset with the specified rid.
        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["preview"] = preview

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}",
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
    def read_table(
        self,
        dataset_rid: DatasetRid,
        *,
        format: TableExportFormat,
        branch_name: Optional[BranchName] = None,
        columns: Optional[List[StrictStr]] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        preview: Optional[PreviewMode] = None,
        row_limit: Optional[StrictInt] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> bytes:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (Virtual datasets composed of other datasets).

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param format: format
        :type format: TableExportFormat
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param columns: columns
        :type columns: Optional[List[StrictStr]]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
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
        _query_params["format"] = format

        _query_params["branchName"] = branch_name

        _query_params["columns"] = columns

        _query_params["endTransactionRid"] = end_transaction_rid

        _query_params["preview"] = preview

        _query_params["rowLimit"] = row_limit

        _query_params["startTransactionRid"] = start_transaction_rid

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "application/octet-stream"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/readTable",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
            ),
        )
