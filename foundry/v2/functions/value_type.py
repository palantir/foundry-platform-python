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
from functools import cached_property

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.functions import errors as functions_errors
from foundry.v2.functions import models as functions_models


class ValueTypeClient:
    """
    The API client for the ValueType Resource.

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
        self.with_streaming_response = _ValueTypeClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _ValueTypeClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def VersionId(self):
        from foundry.v2.functions.version_id import VersionIdClient

        return VersionIdClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        value_type_rid: functions_models.ValueTypeRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> functions_models.ValueType:
        """
        Gets a specific value type with the given RID. The latest version is returned.

        :param value_type_rid:
        :type value_type_rid: ValueTypeRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: functions_models.ValueType

        :raises ValueTypeNotFound: The given ValueType could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/functions/valueTypes/{valueTypeRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "valueTypeRid": value_type_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=functions_models.ValueType,
                request_timeout=request_timeout,
                throwable_errors={
                    "ValueTypeNotFound": functions_errors.ValueTypeNotFound,
                },
            ),
        ).decode()


class _ValueTypeClientRaw:
    """
    The API client for the ValueType Resource.

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
    def get(
        self,
        value_type_rid: functions_models.ValueTypeRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[functions_models.ValueType]:
        """
        Gets a specific value type with the given RID. The latest version is returned.

        :param value_type_rid:
        :type value_type_rid: ValueTypeRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[functions_models.ValueType]

        :raises ValueTypeNotFound: The given ValueType could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/functions/valueTypes/{valueTypeRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "valueTypeRid": value_type_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=functions_models.ValueType,
                request_timeout=request_timeout,
                throwable_errors={
                    "ValueTypeNotFound": functions_errors.ValueTypeNotFound,
                },
            ),
        )


class _ValueTypeClientStreaming:
    """
    The API client for the ValueType Resource.

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
    def get(
        self,
        value_type_rid: functions_models.ValueTypeRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[functions_models.ValueType]:
        """
        Gets a specific value type with the given RID. The latest version is returned.

        :param value_type_rid:
        :type value_type_rid: ValueTypeRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[functions_models.ValueType]

        :raises ValueTypeNotFound: The given ValueType could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/functions/valueTypes/{valueTypeRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "valueTypeRid": value_type_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=functions_models.ValueType,
                request_timeout=request_timeout,
                throwable_errors={
                    "ValueTypeNotFound": functions_errors.ValueTypeNotFound,
                },
            ),
        )
