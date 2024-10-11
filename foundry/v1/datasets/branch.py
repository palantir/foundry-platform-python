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

from typing import Any
from typing import Dict
from typing import Optional

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.v1.core.models._page_size import PageSize
from foundry.v1.core.models._page_token import PageToken
from foundry.v1.datasets.models._branch import Branch
from foundry.v1.datasets.models._branch_id import BranchId
from foundry.v1.datasets.models._dataset_rid import DatasetRid
from foundry.v1.datasets.models._list_branches_response import ListBranchesResponse
from foundry.v1.datasets.models._transaction_rid import TransactionRid


class BranchClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        dataset_rid: DatasetRid,
        *,
        branch_id: BranchId,
        transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Branch:
        """
        Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_id:
        :type branch_id: BranchId
        :param transaction_rid:
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Branch
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "branchId": BranchId,
                        "transactionRid": Optional[TransactionRid],
                    },
                ),
                response_type=Branch,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        dataset_rid: DatasetRid,
        branch_id: BranchId,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Deletes the Branch with the given BranchId.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_id: branchId
        :type branch_id: BranchId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            RequestInfo(
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
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        branch_id: BranchId,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Branch:
        """
        Get a Branch of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_id: branchId
        :type branch_id: BranchId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Branch
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Branch,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        dataset_rid: DatasetRid,
        *,
        page_size: Optional[PageSize] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[Branch]:
        """
        Lists the Branches of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[Branch]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/branches",
                query_params={
                    "pageSize": page_size,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListBranchesResponse,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        dataset_rid: DatasetRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListBranchesResponse:
        """
        Lists the Branches of a Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListBranchesResponse
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListBranchesResponse,
                request_timeout=request_timeout,
            ),
        )
