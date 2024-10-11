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
from typing import List
from typing import Optional

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._errors import handle_unexpected
from foundry.v2.connectivity.models._connection_rid import ConnectionRid
from foundry.v2.connectivity.models._file_import import FileImport
from foundry.v2.connectivity.models._file_import_display_name import FileImportDisplayName  # NOQA
from foundry.v2.connectivity.models._file_import_filter_dict import FileImportFilterDict
from foundry.v2.connectivity.models._file_import_mode import FileImportMode
from foundry.v2.connectivity.models._file_import_rid import FileImportRid
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid
from foundry.v2.orchestration.models._build_rid import BuildRid


class FileImportClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        connection_rid: ConnectionRid,
        dataset_rid: DatasetRid,
        display_name: FileImportDisplayName,
        file_import_filters: List[FileImportFilterDict],
        import_mode: FileImportMode,
        branch_name: Optional[BranchName] = None,
        preview: Optional[PreviewMode] = None,
        subfolder: Optional[pydantic.StrictStr] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> FileImport:
        """
        Creates a new FileImport.
        :param connection_rid: The RID of the Connection (formerly known as a source) that the File Import uses to import data.
        :type connection_rid: ConnectionRid
        :param dataset_rid: The RID of the output dataset.
        :type dataset_rid: DatasetRid
        :param display_name:
        :type display_name: FileImportDisplayName
        :param file_import_filters: Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)
        :type file_import_filters: List[FileImportFilterDict]
        :param import_mode:
        :type import_mode: FileImportMode
        :param branch_name: The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param subfolder: A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
        :type subfolder: Optional[pydantic.StrictStr]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: FileImport
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/fileImports",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "datasetRid": dataset_rid,
                    "importMode": import_mode,
                    "displayName": display_name,
                    "connectionRid": connection_rid,
                    "branchName": branch_name,
                    "subfolder": subfolder,
                    "fileImportFilters": file_import_filters,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "datasetRid": DatasetRid,
                        "importMode": FileImportMode,
                        "displayName": FileImportDisplayName,
                        "connectionRid": ConnectionRid,
                        "branchName": Optional[BranchName],
                        "subfolder": Optional[pydantic.StrictStr],
                        "fileImportFilters": List[FileImportFilterDict],
                    },
                ),
                response_type=FileImport,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Delete the FileImport with the specified RID.
        Deleting the file import does not delete the destination dataset but the dataset will no longer
        be updated by this import.

        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/connectivity/fileImports/{fileImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "fileImportRid": file_import_rid,
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
    def execute(
        self,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> BuildRid:
        """
        Executes the FileImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
        The returned BuildRid can be used to check the status via the Orchestration API.

        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: BuildRid
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/connectivity/fileImports/{fileImportRid}/execute",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "fileImportRid": file_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=BuildRid,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> FileImport:
        """
        Get the FileImport with the specified rid.
        :param file_import_rid: fileImportRid
        :type file_import_rid: FileImportRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: FileImport
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/connectivity/fileImports/{fileImportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "fileImportRid": file_import_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=FileImport,
                request_timeout=request_timeout,
            ),
        )
