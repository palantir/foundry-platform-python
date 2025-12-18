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
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.data_health import errors as data_health_errors
from foundry_sdk.v2.data_health import models as data_health_models


class CheckReportClient:
    """
    The API client for the CheckReport Resource.

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

        self.with_streaming_response = _CheckReportClientStreaming(self)
        self.with_raw_response = _CheckReportClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        check_report_rid: core_models.CheckReportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> data_health_models.CheckReport:
        """
        Get the CheckReport with the specified rid.
        :param check_report_rid:
        :type check_report_rid: CheckReportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: data_health_models.CheckReport

        :raises CheckReportNotFound: The given CheckReport could not be found.
        :raises CheckTypeNotSupported: The type of the requested check is not yet supported in the Platform API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/dataHealth/checkReports/{checkReportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "checkReportRid": check_report_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=data_health_models.CheckReport,
                request_timeout=request_timeout,
                throwable_errors={
                    "CheckReportNotFound": data_health_errors.CheckReportNotFound,
                    "CheckTypeNotSupported": data_health_errors.CheckTypeNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _CheckReportClientRaw:
    def __init__(self, client: CheckReportClient) -> None:
        def get(_: data_health_models.CheckReport): ...

        self.get = core.with_raw_response(get, client.get)


class _CheckReportClientStreaming:
    def __init__(self, client: CheckReportClient) -> None:
        def get(_: data_health_models.CheckReport): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncCheckReportClient:
    """
    The API client for the CheckReport Resource.

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

        self.with_streaming_response = _AsyncCheckReportClientStreaming(self)
        self.with_raw_response = _AsyncCheckReportClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        check_report_rid: core_models.CheckReportRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[data_health_models.CheckReport]:
        """
        Get the CheckReport with the specified rid.
        :param check_report_rid:
        :type check_report_rid: CheckReportRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[data_health_models.CheckReport]

        :raises CheckReportNotFound: The given CheckReport could not be found.
        :raises CheckTypeNotSupported: The type of the requested check is not yet supported in the Platform API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/dataHealth/checkReports/{checkReportRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "checkReportRid": check_report_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=data_health_models.CheckReport,
                request_timeout=request_timeout,
                throwable_errors={
                    "CheckReportNotFound": data_health_errors.CheckReportNotFound,
                    "CheckTypeNotSupported": data_health_errors.CheckTypeNotSupported,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncCheckReportClientRaw:
    def __init__(self, client: AsyncCheckReportClient) -> None:
        def get(_: data_health_models.CheckReport): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncCheckReportClientStreaming:
    def __init__(self, client: AsyncCheckReportClient) -> None:
        def get(_: data_health_models.CheckReport): ...

        self.get = core.async_with_streaming_response(get, client.get)
