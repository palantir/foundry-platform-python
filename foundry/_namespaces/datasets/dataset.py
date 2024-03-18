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
from pydantic import StrictInt
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

from foundry._errors.sdk_internal_error import handle_unexpected
from foundry.api_client import ApiClient

from foundry.models._branch_id import BranchId
from foundry.models._create_dataset_request import CreateDatasetRequest
from foundry.models._dataset import Dataset
from foundry.models._dataset_rid import DatasetRid
from foundry.models._preview_mode import PreviewMode
from foundry.models._table_export_format import TableExportFormat
from foundry.models._transaction_rid import TransactionRid


class DatasetResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def create(
        self,
        *,
        create_dataset_request: CreateDatasetRequest,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param create_dataset_request: CreateDatasetRequest
        :type create_dataset_request: CreateDatasetRequest
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = create_dataset_request

        _header_params["Accept"] = "application/json"

        _header_params["Content-Type"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: Dataset,
        }

        return self._api_client.call_api(
            method="POST",
            resource_path="/v1/datasets",
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
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

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: Dataset,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/datasets/{datasetRid}".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def read_table(
        self,
        dataset_rid: DatasetRid,
        *,
        format: TableExportFormat,
        branch_id: Optional[BranchId] = None,
        columns: Optional[List[StrictStr]] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        preview: Optional[PreviewMode] = None,
        row_limit: Optional[StrictInt] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> bytes:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
          Furthermore, this endpoint currently does not support views (Virtual datasets composed of other datasets).
        :::

        Gets the content of a dataset as a table in the specified format.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The RID of the Dataset.
        :type dataset_rid: DatasetRid
        :param branch_id: The identifier (name) of the Branch.
        :type branch_id: Optional[BranchId]
        :param start_transaction_rid: The Resource Identifier (RID) of the start Transaction.
        :type start_transaction_rid: Optional[TransactionRid]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction.
        :type end_transaction_rid: Optional[TransactionRid]
        :param format: The export format. Must be `ARROW` or `CSV`.
        :type format: TableExportFormat
        :param columns: A subset of the dataset columns to include in the result. Defaults to all columns.
        :type columns: Optional[List[StrictStr]]
        :param row_limit: A limit on the number of rows to return. Note that row ordering is non-deterministic.
        :type row_limit: Optional[StrictInt]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None
        _query_params["branchId"] = branch_id

        _query_params["startTransactionRid"] = start_transaction_rid

        _query_params["endTransactionRid"] = end_transaction_rid

        _query_params["format"] = format

        _query_params["columns"] = columns

        _query_params["rowLimit"] = row_limit

        _query_params["preview"] = preview

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "*/*"

        _response_types_map: Dict[int, Any] = {
            200: bytes,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/datasets/{datasetRid}/readTable".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def put_schema(
        self,
        dataset_rid: DatasetRid,
        *,
        body: object,
        branch_id: Optional[BranchId] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """
        Puts a Schema on an existing Dataset and Branch.

        :param dataset_rid: The RID of the Dataset on which to put the Schema.
        :type dataset_rid: DatasetRid
        :param branch_id: The ID of the Branch on which to put the Schema.
        :type branch_id: Optional[BranchId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param body: Body of the request
        :type body: object
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = body
        _query_params["branchId"] = branch_id

        _query_params["preview"] = preview

        _path_params["datasetRid"] = dataset_rid

        _header_params["Content-Type"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            204: None,
        }

        return self._api_client.call_api(
            method="PUT",
            resource_path="/v1/datasets/{datasetRid}/schema".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
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
    ) -> Union[object, None]:
        """
        Retrieves the Schema for a Dataset and Branch, if it exists.

        :param dataset_rid: The RID of the Dataset.
        :type dataset_rid: DatasetRid
        :param branch_id: The ID of the Branch.
        :type branch_id: Optional[BranchId]
        :param transaction_rid: The TransactionRid that contains the Schema.
        :type transaction_rid: Optional[TransactionRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Union[object, None]
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None
        _query_params["branchId"] = branch_id

        _query_params["transactionRid"] = transaction_rid

        _query_params["preview"] = preview

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: object,
            204: None,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/datasets/{datasetRid}/schema".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
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

        :param dataset_rid: The RID of the Dataset on which to delete the schema.
        :type dataset_rid: DatasetRid
        :param branch_id: The ID of the Branch on which to delete the schema.
        :type branch_id: Optional[BranchId]
        :param transaction_rid: The RID of the Transaction on which to delete the schema.
        :type transaction_rid: Optional[TransactionRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None
        _query_params["branchId"] = branch_id

        _query_params["transactionRid"] = transaction_rid

        _query_params["preview"] = preview

        _path_params["datasetRid"] = dataset_rid

        _response_types_map: Dict[int, Any] = {
            204: None,
        }

        return self._api_client.call_api(
            method="DELETE",
            resource_path="/v1/datasets/{datasetRid}/schema".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )
