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
from foundry_sdk.v2.functions import errors as functions_errors
from foundry_sdk.v2.functions import models as functions_models


class VersionIdClient:
    """
    The API client for the VersionId Resource.

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

        self.with_streaming_response = _VersionIdClientStreaming(self)
        self.with_raw_response = _VersionIdClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        value_type_rid: functions_models.ValueTypeRid,
        version_id_version_id: functions_models.ValueTypeVersionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> functions_models.VersionId:
        """
        Gets a specific value type with the given RID. The specified version is returned.

        :param value_type_rid:
        :type value_type_rid: ValueTypeRid
        :param version_id_version_id:
        :type version_id_version_id: ValueTypeVersionId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: functions_models.VersionId

        :raises VersionIdNotFound: The given VersionId could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/functions/valueTypes/{valueTypeRid}/versionIds/{versionIdVersionId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "valueTypeRid": value_type_rid,
                    "versionIdVersionId": version_id_version_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=functions_models.VersionId,
                request_timeout=request_timeout,
                throwable_errors={
                    "VersionIdNotFound": functions_errors.VersionIdNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _VersionIdClientRaw:
    def __init__(self, client: VersionIdClient) -> None:
        def get(_: functions_models.VersionId): ...

        self.get = core.with_raw_response(get, client.get)


class _VersionIdClientStreaming:
    def __init__(self, client: VersionIdClient) -> None:
        def get(_: functions_models.VersionId): ...

        self.get = core.with_streaming_response(get, client.get)


class AsyncVersionIdClient:
    """
    The API client for the VersionId Resource.

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

        self.with_streaming_response = _AsyncVersionIdClientStreaming(self)
        self.with_raw_response = _AsyncVersionIdClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        value_type_rid: functions_models.ValueTypeRid,
        version_id_version_id: functions_models.ValueTypeVersionId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[functions_models.VersionId]:
        """
        Gets a specific value type with the given RID. The specified version is returned.

        :param value_type_rid:
        :type value_type_rid: ValueTypeRid
        :param version_id_version_id:
        :type version_id_version_id: ValueTypeVersionId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[functions_models.VersionId]

        :raises VersionIdNotFound: The given VersionId could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/functions/valueTypes/{valueTypeRid}/versionIds/{versionIdVersionId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "valueTypeRid": value_type_rid,
                    "versionIdVersionId": version_id_version_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=functions_models.VersionId,
                request_timeout=request_timeout,
                throwable_errors={
                    "VersionIdNotFound": functions_errors.VersionIdNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncVersionIdClientRaw:
    def __init__(self, client: AsyncVersionIdClient) -> None:
        def get(_: functions_models.VersionId): ...

        self.get = core.async_with_raw_response(get, client.get)


class _AsyncVersionIdClientStreaming:
    def __init__(self, client: AsyncVersionIdClient) -> None:
        def get(_: functions_models.VersionId): ...

        self.get = core.async_with_streaming_response(get, client.get)
