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
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.third_party_applications import errors as third_party_applications_errors  # NOQA
from foundry.v2.third_party_applications.models._list_versions_response import (
    ListVersionsResponse,
)  # NOQA
from foundry.v2.third_party_applications.models._third_party_application_rid import (
    ThirdPartyApplicationRid,
)  # NOQA
from foundry.v2.third_party_applications.models._version import Version
from foundry.v2.third_party_applications.models._version_version import VersionVersion


class VersionClient:
    """
    The API client for the Version Resource.

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
        self.with_streaming_response = _VersionClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _VersionClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        version_version: VersionVersion,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Delete the Version with the specified version.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: versionVersion
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteVersionPermissionDenied: Could not delete the Version.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion}",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                    "versionVersion": version_version,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteVersionPermissionDenied": third_party_applications_errors.DeleteVersionPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        version_version: VersionVersion,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Version:
        """
        Get the Version with the specified version.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: versionVersion
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Version

        :raises VersionNotFound: The given Version could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion}",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                    "versionVersion": version_version,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "VersionNotFound": third_party_applications_errors.VersionNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[Version]:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[Version]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListVersionsResponse:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListVersionsResponse
        """

        warnings.warn(
            "The client.third_party_applications.Version.page(...) method has been deprecated. Please use client.third_party_applications.Version.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def upload(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: VersionVersion,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Version:
        """
        Upload a new version of the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version: version
        :type version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Version

        :raises UploadVersionPermissionDenied: Could not upload the Version.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/upload",
                query_params={
                    "version": version,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "UploadVersionPermissionDenied": third_party_applications_errors.UploadVersionPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def upload_snapshot(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: VersionVersion,
        preview: Optional[PreviewMode] = None,
        snapshot_identifier: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Version:
        """
        Upload a snapshot version of the Website. Snapshot versions are automatically deleted after two days.

        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version: version
        :type version: VersionVersion
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param snapshot_identifier: snapshotIdentifier
        :type snapshot_identifier: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Version

        :raises UploadSnapshotVersionPermissionDenied: Could not uploadSnapshot the Version.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/uploadSnapshot",
                query_params={
                    "version": version,
                    "preview": preview,
                    "snapshotIdentifier": snapshot_identifier,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "UploadSnapshotVersionPermissionDenied": third_party_applications_errors.UploadSnapshotVersionPermissionDenied,
                },
            ),
        ).decode()


class _VersionClientRaw:
    """
    The API client for the Version Resource.

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
    def delete(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        version_version: VersionVersion,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Delete the Version with the specified version.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: versionVersion
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises DeleteVersionPermissionDenied: Could not delete the Version.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion}",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                    "versionVersion": version_version,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteVersionPermissionDenied": third_party_applications_errors.DeleteVersionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        version_version: VersionVersion,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Version]:
        """
        Get the Version with the specified version.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: versionVersion
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Version]

        :raises VersionNotFound: The given Version could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion}",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                    "versionVersion": version_version,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "VersionNotFound": third_party_applications_errors.VersionNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListVersionsResponse]:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListVersionsResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListVersionsResponse]:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListVersionsResponse]
        """

        warnings.warn(
            "The client.third_party_applications.Version.page(...) method has been deprecated. Please use client.third_party_applications.Version.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def upload(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: VersionVersion,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Version]:
        """
        Upload a new version of the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version: version
        :type version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Version]

        :raises UploadVersionPermissionDenied: Could not upload the Version.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/upload",
                query_params={
                    "version": version,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "UploadVersionPermissionDenied": third_party_applications_errors.UploadVersionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def upload_snapshot(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: VersionVersion,
        preview: Optional[PreviewMode] = None,
        snapshot_identifier: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Version]:
        """
        Upload a snapshot version of the Website. Snapshot versions are automatically deleted after two days.

        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version: version
        :type version: VersionVersion
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param snapshot_identifier: snapshotIdentifier
        :type snapshot_identifier: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Version]

        :raises UploadSnapshotVersionPermissionDenied: Could not uploadSnapshot the Version.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/uploadSnapshot",
                query_params={
                    "version": version,
                    "preview": preview,
                    "snapshotIdentifier": snapshot_identifier,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "UploadSnapshotVersionPermissionDenied": third_party_applications_errors.UploadSnapshotVersionPermissionDenied,
                },
            ),
        )


class _VersionClientStreaming:
    """
    The API client for the Version Resource.

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
    def delete(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        version_version: VersionVersion,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Delete the Version with the specified version.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: versionVersion
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises DeleteVersionPermissionDenied: Could not delete the Version.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion}",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                    "versionVersion": version_version,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteVersionPermissionDenied": third_party_applications_errors.DeleteVersionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        version_version: VersionVersion,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Version]:
        """
        Get the Version with the specified version.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: versionVersion
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Version]

        :raises VersionNotFound: The given Version could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion}",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                    "versionVersion": version_version,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "VersionNotFound": third_party_applications_errors.VersionNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListVersionsResponse]:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListVersionsResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListVersionsResponse]:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListVersionsResponse]
        """

        warnings.warn(
            "The client.third_party_applications.Version.page(...) method has been deprecated. Please use client.third_party_applications.Version.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def upload(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: VersionVersion,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Version]:
        """
        Upload a new version of the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version: version
        :type version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Version]

        :raises UploadVersionPermissionDenied: Could not upload the Version.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/upload",
                query_params={
                    "version": version,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "UploadVersionPermissionDenied": third_party_applications_errors.UploadVersionPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def upload_snapshot(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: VersionVersion,
        preview: Optional[PreviewMode] = None,
        snapshot_identifier: Optional[str] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Version]:
        """
        Upload a snapshot version of the Website. Snapshot versions are automatically deleted after two days.

        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version: version
        :type version: VersionVersion
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param snapshot_identifier: snapshotIdentifier
        :type snapshot_identifier: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Version]

        :raises UploadSnapshotVersionPermissionDenied: Could not uploadSnapshot the Version.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/uploadSnapshot",
                query_params={
                    "version": version,
                    "preview": preview,
                    "snapshotIdentifier": snapshot_identifier,
                },
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "UploadSnapshotVersionPermissionDenied": third_party_applications_errors.UploadSnapshotVersionPermissionDenied,
                },
            ),
        )
