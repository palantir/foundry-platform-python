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

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.audit import errors as audit_errors
from foundry_sdk.v2.audit import models as audit_models
from foundry_sdk.v2.core import models as core_models


class LogFileClient:
    """
    The API client for the LogFile Resource.

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

        self.with_streaming_response = _LogFileClientStreaming(self)
        self.with_raw_response = _LogFileClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def content(
        self,
        organization_rid: core_models.OrganizationRid,
        log_file_id: audit_models.FileId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param log_file_id:
        :type log_file_id: FileId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

        :raises GetLogFileContentPermissionDenied: Could not content the LogFile.
        :raises GetLogFileContentPermissionDenied: Could not content the LogFile.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/audit/organizations/{organizationRid}/logFiles/{logFileId}/content",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                    "logFileId": log_file_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetLogFileContentPermissionDenied": audit_errors.GetLogFileContentPermissionDenied,
                    "GetLogFileContentPermissionDenied": audit_errors.GetLogFileContentPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        end_date: typing.Optional[core.AwareDatetime] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        start_date: typing.Optional[core.AwareDatetime] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[audit_models.LogFile]:
        """
        Lists all LogFiles.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param end_date: List log files for audit events up until this date (inclusive). If absent, defaults to no end date. Use the returned `nextPageToken` to continually poll the  `listLogFiles` endpoint to list the latest available logs.
        :type end_date: Optional[datetime]
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param start_date: List log files for audit events starting from this date. If absent, defaults to the current date.
        :type start_date: Optional[datetime]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[audit_models.LogFile]

        :raises ListLogFilesPermissionDenied: The provided token does not have permission to list audit log files.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/audit/organizations/{organizationRid}/logFiles",
                query_params={
                    "endDate": end_date,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                    "startDate": start_date,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=audit_models.ListLogFilesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListLogFilesPermissionDenied": audit_errors.ListLogFilesPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _LogFileClientRaw:
    def __init__(self, client: LogFileClient) -> None:
        def content(_: bytes): ...
        def list(_: audit_models.ListLogFilesResponse): ...

        self.content = core.with_raw_response(content, client.content)
        self.list = core.with_raw_response(list, client.list)


class _LogFileClientStreaming:
    def __init__(self, client: LogFileClient) -> None:
        def content(_: bytes): ...
        def list(_: audit_models.ListLogFilesResponse): ...

        self.content = core.with_streaming_response(content, client.content)
        self.list = core.with_streaming_response(list, client.list)


class AsyncLogFileClient:
    """
    The API client for the LogFile Resource.

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
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncLogFileClientStreaming(self)
        self.with_raw_response = _AsyncLogFileClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def content(
        self,
        organization_rid: core_models.OrganizationRid,
        log_file_id: audit_models.FileId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """

        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param log_file_id:
        :type log_file_id: FileId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]

        :raises GetLogFileContentPermissionDenied: Could not content the LogFile.
        :raises GetLogFileContentPermissionDenied: Could not content the LogFile.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/audit/organizations/{organizationRid}/logFiles/{logFileId}/content",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                    "logFileId": log_file_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetLogFileContentPermissionDenied": audit_errors.GetLogFileContentPermissionDenied,
                    "GetLogFileContentPermissionDenied": audit_errors.GetLogFileContentPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        organization_rid: core_models.OrganizationRid,
        *,
        end_date: typing.Optional[core.AwareDatetime] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        start_date: typing.Optional[core.AwareDatetime] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[audit_models.LogFile]:
        """
        Lists all LogFiles.

        This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.
        :param organization_rid:
        :type organization_rid: OrganizationRid
        :param end_date: List log files for audit events up until this date (inclusive). If absent, defaults to no end date. Use the returned `nextPageToken` to continually poll the  `listLogFiles` endpoint to list the latest available logs.
        :type end_date: Optional[datetime]
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param start_date: List log files for audit events starting from this date. If absent, defaults to the current date.
        :type start_date: Optional[datetime]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[audit_models.LogFile]

        :raises ListLogFilesPermissionDenied: The provided token does not have permission to list audit log files.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/audit/organizations/{organizationRid}/logFiles",
                query_params={
                    "endDate": end_date,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                    "startDate": start_date,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=audit_models.ListLogFilesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ListLogFilesPermissionDenied": audit_errors.ListLogFilesPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncLogFileClientRaw:
    def __init__(self, client: AsyncLogFileClient) -> None:
        def content(_: bytes): ...
        def list(_: audit_models.ListLogFilesResponse): ...

        self.content = core.async_with_raw_response(content, client.content)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncLogFileClientStreaming:
    def __init__(self, client: AsyncLogFileClient) -> None:
        def content(_: bytes): ...
        def list(_: audit_models.ListLogFilesResponse): ...

        self.content = core.async_with_streaming_response(content, client.content)
        self.list = core.async_with_streaming_response(list, client.list)
