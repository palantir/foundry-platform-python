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
from typing import Optional

from pydantic import Field
from pydantic import validate_call

from foundry._errors.sdk_internal_error import handle_unexpected
from foundry.api_client import ApiClient

from foundry.models._branch import Branch
from foundry.models._branch_id import BranchId
from foundry.models._create_branch_request import CreateBranchRequest
from foundry.models._dataset_rid import DatasetRid
from foundry.models._list_branches_response import ListBranchesResponse
from foundry.models._page_size import PageSize
from foundry.models._page_token import PageToken


class BranchResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def create(
        self,
        dataset_rid: DatasetRid,
        *,
        create_branch_request: CreateBranchRequest,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Branch:
        """
        Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to create the Branch.
        :type dataset_rid: DatasetRid
        :param create_branch_request: CreateBranchRequest
        :type create_branch_request: CreateBranchRequest
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Branch
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = create_branch_request

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "application/json"

        _header_params["Content-Type"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: Branch,
        }

        return self._api_client.call_api(
            method="POST",
            resource_path="/v1/datasets/{datasetRid}/branches".format(**_path_params),
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
        branch_id: BranchId,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Branch:
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
        :rtype: Branch
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None

        _path_params["datasetRid"] = dataset_rid

        _path_params["branchId"] = branch_id

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: Branch,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/datasets/{datasetRid}/branches/{branchId}".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def delete(
        self,
        dataset_rid: DatasetRid,
        branch_id: BranchId,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None

        _path_params["datasetRid"] = dataset_rid

        _path_params["branchId"] = branch_id

        _response_types_map: Dict[int, Any] = {
            204: None,
        }

        return self._api_client.call_api(
            method="DELETE",
            resource_path="/v1/datasets/{datasetRid}/branches/{branchId}".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def iterator(
        self,
        dataset_rid: DatasetRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListBranchesResponse:
        """
        Lists the Branches of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to list Branches.
        :type dataset_rid: DatasetRid
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListBranchesResponse
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None
        _query_params["pageSize"] = page_size

        _query_params["pageToken"] = page_token

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: ListBranchesResponse,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/datasets/{datasetRid}/branches".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )