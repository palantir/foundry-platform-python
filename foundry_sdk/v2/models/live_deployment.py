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
from foundry_sdk.v2.models import errors as models_errors
from foundry_sdk.v2.models import models as models_models


class LiveDeploymentClient:
    """
    The API client for the LiveDeployment Resource.

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

        self.with_streaming_response = _LiveDeploymentClientStreaming(self)
        self.with_raw_response = _LiveDeploymentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def transform_json(
        self,
        live_deployment_rid: models_models.LiveDeploymentRid,
        *,
        input: typing.Dict[str, typing.Any],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.TransformLiveDeploymentResponse:
        """
        Performs inference on the live deployment.

        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param input: The input data for the model inference. The structure should match the model's transform API specification, where each key is an input name and the value is the corresponding input data.
        :type input: Dict[str, Any]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.TransformLiveDeploymentResponse

        :raises TransformJsonLiveDeploymentPermissionDenied: Could not transformJson the LiveDeployment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}/transformJson",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "liveDeploymentRid": live_deployment_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.TransformJsonLiveDeploymentRequest(
                    input=input,
                ),
                response_type=models_models.TransformLiveDeploymentResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "TransformJsonLiveDeploymentPermissionDenied": models_errors.TransformJsonLiveDeploymentPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _LiveDeploymentClientRaw:
    def __init__(self, client: LiveDeploymentClient) -> None:
        def transform_json(_: models_models.TransformLiveDeploymentResponse): ...

        self.transform_json = core.with_raw_response(transform_json, client.transform_json)


class _LiveDeploymentClientStreaming:
    def __init__(self, client: LiveDeploymentClient) -> None:
        def transform_json(_: models_models.TransformLiveDeploymentResponse): ...

        self.transform_json = core.with_streaming_response(transform_json, client.transform_json)


class AsyncLiveDeploymentClient:
    """
    The API client for the LiveDeployment Resource.

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

        self.with_streaming_response = _AsyncLiveDeploymentClientStreaming(self)
        self.with_raw_response = _AsyncLiveDeploymentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def transform_json(
        self,
        live_deployment_rid: models_models.LiveDeploymentRid,
        *,
        input: typing.Dict[str, typing.Any],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.TransformLiveDeploymentResponse]:
        """
        Performs inference on the live deployment.

        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param input: The input data for the model inference. The structure should match the model's transform API specification, where each key is an input name and the value is the corresponding input data.
        :type input: Dict[str, Any]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.TransformLiveDeploymentResponse]

        :raises TransformJsonLiveDeploymentPermissionDenied: Could not transformJson the LiveDeployment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}/transformJson",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "liveDeploymentRid": live_deployment_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.TransformJsonLiveDeploymentRequest(
                    input=input,
                ),
                response_type=models_models.TransformLiveDeploymentResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "TransformJsonLiveDeploymentPermissionDenied": models_errors.TransformJsonLiveDeploymentPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncLiveDeploymentClientRaw:
    def __init__(self, client: AsyncLiveDeploymentClient) -> None:
        def transform_json(_: models_models.TransformLiveDeploymentResponse): ...

        self.transform_json = core.async_with_raw_response(transform_json, client.transform_json)


class _AsyncLiveDeploymentClientStreaming:
    def __init__(self, client: AsyncLiveDeploymentClient) -> None:
        def transform_json(_: models_models.TransformLiveDeploymentResponse): ...

        self.transform_json = core.async_with_streaming_response(
            transform_json, client.transform_json
        )
