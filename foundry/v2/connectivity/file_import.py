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

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call
from typing_extensions import Annotated

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._errors import handle_unexpected
from foundry.v2.connectivity.models._file_import import FileImport
from foundry.v2.connectivity.models._file_import_rid import FileImportRid
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.orchestration.models._build_rid import BuildRid


class FileImportClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def get(
        self,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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

    @validate_call
    @handle_unexpected
    def trigger(
        self,
        file_import_rid: FileImportRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> BuildRid:
        """
        Triggers the FileImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
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
                resource_path="/v2/connectivity/fileImports/{fileImportRid}/trigger",
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
