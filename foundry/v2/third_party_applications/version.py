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


import typing
import warnings

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.third_party_applications import errors as third_party_applications_errors  # NOQA
from foundry.v2.third_party_applications import models as third_party_applications_models  # NOQA


class VersionClient:
    """
    The API client for the Version Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _VersionClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _VersionClientRaw(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        version_version: third_party_applications_models.VersionVersion,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Delete the Version with the specified version.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: The semantic version of the Website.
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteVersionPermissionDenied: Could not delete the Version.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        version_version: third_party_applications_models.VersionVersion,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> third_party_applications_models.Version:
        """
        Get the Version with the specified version.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: The semantic version of the Website.
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: third_party_applications_models.Version

        :raises VersionNotFound: The given Version could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "VersionNotFound": third_party_applications_errors.VersionNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[third_party_applications_models.Version]:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[third_party_applications_models.Version]
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> third_party_applications_models.ListVersionsResponse:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: third_party_applications_models.ListVersionsResponse
        """

        warnings.warn(
            "The client.third_party_applications.Version.page(...) method has been deprecated. Please use client.third_party_applications.Version.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: third_party_applications_models.VersionVersion,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> third_party_applications_models.Version:
        """
        Upload a new version of the Website.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version:
        :type version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: third_party_applications_models.Version

        :raises UploadVersionPermissionDenied: Could not upload the Version.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "UploadVersionPermissionDenied": third_party_applications_errors.UploadVersionPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload_snapshot(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: third_party_applications_models.VersionVersion,
        preview: typing.Optional[core_models.PreviewMode] = None,
        snapshot_identifier: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> third_party_applications_models.Version:
        """
        Upload a snapshot version of the Website. Snapshot versions are automatically deleted after two days.

        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version:
        :type version: VersionVersion
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param snapshot_identifier: The identifier of the snapshot. If the identifier follows the format `foundry.v1@<repositoryRid>@<pullRequestRid>@<commitHash>`, PR preview for such identifier will be accessible from foundry code repositories.
        :type snapshot_identifier: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: third_party_applications_models.Version

        :raises UploadSnapshotVersionPermissionDenied: Could not uploadSnapshot the Version.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.Version,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        version_version: third_party_applications_models.VersionVersion,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Delete the Version with the specified version.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: The semantic version of the Website.
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises DeleteVersionPermissionDenied: Could not delete the Version.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        version_version: third_party_applications_models.VersionVersion,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[third_party_applications_models.Version]:
        """
        Get the Version with the specified version.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: The semantic version of the Website.
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[third_party_applications_models.Version]

        :raises VersionNotFound: The given Version could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "VersionNotFound": third_party_applications_errors.VersionNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[third_party_applications_models.ListVersionsResponse]:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[third_party_applications_models.ListVersionsResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[third_party_applications_models.ListVersionsResponse]:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[third_party_applications_models.ListVersionsResponse]
        """

        warnings.warn(
            "The client.third_party_applications.Version.page(...) method has been deprecated. Please use client.third_party_applications.Version.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: third_party_applications_models.VersionVersion,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[third_party_applications_models.Version]:
        """
        Upload a new version of the Website.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version:
        :type version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[third_party_applications_models.Version]

        :raises UploadVersionPermissionDenied: Could not upload the Version.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "UploadVersionPermissionDenied": third_party_applications_errors.UploadVersionPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload_snapshot(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: third_party_applications_models.VersionVersion,
        preview: typing.Optional[core_models.PreviewMode] = None,
        snapshot_identifier: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[third_party_applications_models.Version]:
        """
        Upload a snapshot version of the Website. Snapshot versions are automatically deleted after two days.

        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version:
        :type version: VersionVersion
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param snapshot_identifier: The identifier of the snapshot. If the identifier follows the format `foundry.v1@<repositoryRid>@<pullRequestRid>@<commitHash>`, PR preview for such identifier will be accessible from foundry code repositories.
        :type snapshot_identifier: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[third_party_applications_models.Version]

        :raises UploadSnapshotVersionPermissionDenied: Could not uploadSnapshot the Version.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.Version,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        version_version: third_party_applications_models.VersionVersion,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Delete the Version with the specified version.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: The semantic version of the Website.
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises DeleteVersionPermissionDenied: Could not delete the Version.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        version_version: third_party_applications_models.VersionVersion,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[third_party_applications_models.Version]:
        """
        Get the Version with the specified version.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version_version: The semantic version of the Website.
        :type version_version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[third_party_applications_models.Version]

        :raises VersionNotFound: The given Version could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "VersionNotFound": third_party_applications_errors.VersionNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[third_party_applications_models.ListVersionsResponse]:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[third_party_applications_models.ListVersionsResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[third_party_applications_models.ListVersionsResponse]:
        """
        Lists all Versions.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[third_party_applications_models.ListVersionsResponse]
        """

        warnings.warn(
            "The client.third_party_applications.Version.page(...) method has been deprecated. Please use client.third_party_applications.Version.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.ListVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: third_party_applications_models.VersionVersion,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[third_party_applications_models.Version]:
        """
        Upload a new version of the Website.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version:
        :type version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[third_party_applications_models.Version]

        :raises UploadVersionPermissionDenied: Could not upload the Version.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "UploadVersionPermissionDenied": third_party_applications_errors.UploadVersionPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload_snapshot(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        body: bytes,
        *,
        version: third_party_applications_models.VersionVersion,
        preview: typing.Optional[core_models.PreviewMode] = None,
        snapshot_identifier: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[third_party_applications_models.Version]:
        """
        Upload a snapshot version of the Website. Snapshot versions are automatically deleted after two days.

        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param body: The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
        :type body: bytes
        :param version:
        :type version: VersionVersion
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param snapshot_identifier: The identifier of the snapshot. If the identifier follows the format `foundry.v1@<repositoryRid>@<pullRequestRid>@<commitHash>`, PR preview for such identifier will be accessible from foundry code repositories.
        :type snapshot_identifier: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[third_party_applications_models.Version]

        :raises UploadSnapshotVersionPermissionDenied: Could not uploadSnapshot the Version.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=third_party_applications_models.Version,
                request_timeout=request_timeout,
                throwable_errors={
                    "UploadSnapshotVersionPermissionDenied": third_party_applications_errors.UploadSnapshotVersionPermissionDenied,
                },
            ),
        )
