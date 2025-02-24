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

import warnings
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
from foundry._core import ResourceIterator
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.datasets import errors as datasets_errors
from foundry.v2.datasets.models._branch import Branch
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid
from foundry.v2.datasets.models._list_branches_response import ListBranchesResponse
from foundry.v2.datasets.models._transaction_rid import TransactionRid


class BranchClient:
    """
    The API client for the Branch Resource.

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
        self.with_streaming_response = _BranchClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _BranchClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        dataset_rid: DatasetRid,
        *,
        name: BranchName,
        transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Branch:
        """
        Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param name:
        :type name: BranchName
        :param transaction_rid: The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction.
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Branch

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CreateBranchPermissionDenied: The provided token does not have permission to create a branch of this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "transactionRid": Optional[TransactionRid],
                        "name": BranchName,
                    },
                ),
                response_type=Branch,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CreateBranchPermissionDenied": datasets_errors.CreateBranchPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        dataset_rid: DatasetRid,
        branch_name: BranchName,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Deletes the Branch with the given BranchName.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_name: branchName
        :type branch_name: BranchName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DeleteBranchPermissionDenied: The provided token does not have permission to delete the given branch from this dataset.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        branch_name: BranchName,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Branch:
        """
        Get a Branch of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_name: branchName
        :type branch_name: BranchName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Branch

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Branch,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        dataset_rid: DatasetRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[Branch]:
        """
        Lists the Branches of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[Branch]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.iterate_api(
            RequestInfo(
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
                response_type=ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
            ),
        )

    @maybe_ignore_preview
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

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        warnings.warn(
            "The client.datasets.Branch.page(...) method has been deprecated. Please use client.datasets.Branch.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
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
    def create(
        self,
        dataset_rid: DatasetRid,
        *,
        name: BranchName,
        transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Branch]:
        """
        Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param name:
        :type name: BranchName
        :param transaction_rid: The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction.
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Branch]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CreateBranchPermissionDenied: The provided token does not have permission to create a branch of this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "transactionRid": Optional[TransactionRid],
                        "name": BranchName,
                    },
                ),
                response_type=Branch,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CreateBranchPermissionDenied": datasets_errors.CreateBranchPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        dataset_rid: DatasetRid,
        branch_name: BranchName,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Deletes the Branch with the given BranchName.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_name: branchName
        :type branch_name: BranchName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DeleteBranchPermissionDenied: The provided token does not have permission to delete the given branch from this dataset.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        branch_name: BranchName,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Branch]:
        """
        Get a Branch of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_name: branchName
        :type branch_name: BranchName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Branch]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Branch,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        dataset_rid: DatasetRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListBranchesResponse]:
        """
        Lists the Branches of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListBranchesResponse]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        dataset_rid: DatasetRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListBranchesResponse]:
        """
        Lists the Branches of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListBranchesResponse]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        warnings.warn(
            "The client.datasets.Branch.page(...) method has been deprecated. Please use client.datasets.Branch.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
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
    def create(
        self,
        dataset_rid: DatasetRid,
        *,
        name: BranchName,
        transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Branch]:
        """
        Creates a branch on an existing dataset. A branch may optionally point to a (committed) transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param name:
        :type name: BranchName
        :param transaction_rid: The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction.
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Branch]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CreateBranchPermissionDenied: The provided token does not have permission to create a branch of this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "transactionRid": Optional[TransactionRid],
                        "name": BranchName,
                    },
                ),
                response_type=Branch,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CreateBranchPermissionDenied": datasets_errors.CreateBranchPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        dataset_rid: DatasetRid,
        branch_name: BranchName,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Deletes the Branch with the given BranchName.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_name: branchName
        :type branch_name: BranchName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DeleteBranchPermissionDenied: The provided token does not have permission to delete the given branch from this dataset.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        branch_name: BranchName,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Branch]:
        """
        Get a Branch of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_name: branchName
        :type branch_name: BranchName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Branch]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=Branch,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        dataset_rid: DatasetRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListBranchesResponse]:
        """
        Lists the Branches of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListBranchesResponse]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        dataset_rid: DatasetRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListBranchesResponse]:
        """
        Lists the Branches of a Dataset.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListBranchesResponse]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        warnings.warn(
            "The client.datasets.Branch.page(...) method has been deprecated. Please use client.datasets.Branch.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListBranchesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
            ),
        )
