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
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _LiveDeploymentClientStreaming(self)
        self.with_raw_response = _LiveDeploymentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        deployment_type: models_models.CreateLiveDeploymentTarget,
        runtime_configuration: models_models.LiveDeploymentRuntimeConfiguration,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.LiveDeployment:
        """
        Creates a new live deployment for a model version with the specified runtime configuration. The deployment will begin provisioning compute resources and deploying the target model version.

        :param deployment_type: The target model source for the live deployment. Determines which model and version selection strategy to use when creating the deployment.
        :type deployment_type: CreateLiveDeploymentTarget
        :param runtime_configuration: The compute resource configuration for the deployment.
        :type runtime_configuration: LiveDeploymentRuntimeConfiguration
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.LiveDeployment

        :raises CreateLiveDeploymentPermissionDenied: Could not create the LiveDeployment.
        :raises GpuTypeNotAvailable: The requested GPU type is not available. Use a GPU type that is available in the deployment's resource queue.
        :raises InvalidGpuCount: The GPU count is invalid. The GPU count must be between 1 and the maximum allowed for the requested GPU type.
        :raises ModelNotFound: The given Model could not be found.
        :raises ThreadCountTooHigh: The specified thread count exceeds the maximum allowed value.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/liveDeployments",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.CreateLiveDeploymentRequest(
                    deployment_type=deployment_type,
                    runtime_configuration=runtime_configuration,
                ),
                response_type=models_models.LiveDeployment,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateLiveDeploymentPermissionDenied": models_errors.CreateLiveDeploymentPermissionDenied,
                    "GpuTypeNotAvailable": models_errors.GpuTypeNotAvailable,
                    "InvalidGpuCount": models_errors.InvalidGpuCount,
                    "ModelNotFound": models_errors.ModelNotFound,
                    "ThreadCountTooHigh": models_errors.ThreadCountTooHigh,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        live_deployment_rid: models_models.LiveDeploymentRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.LiveDeployment:
        """
        Retrieves a live deployment by its Resource Identifier (RID), including its deployed model version and runtime configuration.

        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.LiveDeployment

        :raises LiveDeploymentNotFound: The specified live deployment was not found.
        :raises UnsupportedLiveDeployment: The Live Deployment type is not supported by the API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "liveDeploymentRid": live_deployment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.LiveDeployment,
                request_timeout=request_timeout,
                throwable_errors={
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "UnsupportedLiveDeployment": models_errors.UnsupportedLiveDeployment,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        live_deployment_rid: models_models.LiveDeploymentRid,
        *,
        runtime_configuration: models_models.LiveDeploymentRuntimeConfiguration,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.LiveDeployment:
        """
        Updates the runtime configuration of the live deployment. The deployment will apply the new configuration to the running replicas.

        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param runtime_configuration: The compute resource configuration for the deployment.
        :type runtime_configuration: LiveDeploymentRuntimeConfiguration
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.LiveDeployment

        :raises GpuTypeNotAvailable: The requested GPU type is not available. Use a GPU type that is available in the deployment's resource queue.
        :raises InvalidGpuCount: The GPU count is invalid. The GPU count must be between 1 and the maximum allowed for the requested GPU type.
        :raises LiveDeploymentNotFound: The specified live deployment was not found.
        :raises ReplaceLiveDeploymentPermissionDenied: Could not replace the LiveDeployment.
        :raises ThreadCountTooHigh: The specified thread count exceeds the maximum allowed value.
        :raises UnsupportedLiveDeployment: The Live Deployment type is not supported by the API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}",
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
                body=models_models.ReplaceLiveDeploymentRequest(
                    runtime_configuration=runtime_configuration,
                ),
                response_type=models_models.LiveDeployment,
                request_timeout=request_timeout,
                throwable_errors={
                    "GpuTypeNotAvailable": models_errors.GpuTypeNotAvailable,
                    "InvalidGpuCount": models_errors.InvalidGpuCount,
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "ReplaceLiveDeploymentPermissionDenied": models_errors.ReplaceLiveDeploymentPermissionDenied,
                    "ThreadCountTooHigh": models_errors.ThreadCountTooHigh,
                    "UnsupportedLiveDeployment": models_errors.UnsupportedLiveDeployment,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

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

        :raises InferenceFailure: The inference request failed due to a model execution error or unexpected internal issue. This typically indicates a problem with the model itself rather than the input data.
        :raises InferenceInvalidInput: The inference request contains invalid input data that does not match the model's API specification. Check the error type for specific validation failure details.
        :raises InferenceTimeout: The live deployment took longer than 5 minutes to respond to the inference request. This typically indicates the model execution is taking too long or the deployment is under heavy load.
        :raises LiveDeploymentNotFound: The specified live deployment was not found.
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
                    "InferenceFailure": models_errors.InferenceFailure,
                    "InferenceInvalidInput": models_errors.InferenceInvalidInput,
                    "InferenceTimeout": models_errors.InferenceTimeout,
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "TransformJsonLiveDeploymentPermissionDenied": models_errors.TransformJsonLiveDeploymentPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _LiveDeploymentClientRaw:
    def __init__(self, client: LiveDeploymentClient) -> None:
        def create(_: models_models.LiveDeployment): ...
        def get(_: models_models.LiveDeployment): ...
        def replace(_: models_models.LiveDeployment): ...
        def transform_json(_: models_models.TransformLiveDeploymentResponse): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.replace = core.with_raw_response(replace, client.replace)
        self.transform_json = core.with_raw_response(transform_json, client.transform_json)


class _LiveDeploymentClientStreaming:
    def __init__(self, client: LiveDeploymentClient) -> None:
        def create(_: models_models.LiveDeployment): ...
        def get(_: models_models.LiveDeployment): ...
        def replace(_: models_models.LiveDeployment): ...
        def transform_json(_: models_models.TransformLiveDeploymentResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.replace = core.with_streaming_response(replace, client.replace)
        self.transform_json = core.with_streaming_response(transform_json, client.transform_json)


class AsyncLiveDeploymentClient:
    """
    The API client for the LiveDeployment Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncLiveDeploymentClientStreaming(self)
        self.with_raw_response = _AsyncLiveDeploymentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        deployment_type: models_models.CreateLiveDeploymentTarget,
        runtime_configuration: models_models.LiveDeploymentRuntimeConfiguration,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.LiveDeployment]:
        """
        Creates a new live deployment for a model version with the specified runtime configuration. The deployment will begin provisioning compute resources and deploying the target model version.

        :param deployment_type: The target model source for the live deployment. Determines which model and version selection strategy to use when creating the deployment.
        :type deployment_type: CreateLiveDeploymentTarget
        :param runtime_configuration: The compute resource configuration for the deployment.
        :type runtime_configuration: LiveDeploymentRuntimeConfiguration
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.LiveDeployment]

        :raises CreateLiveDeploymentPermissionDenied: Could not create the LiveDeployment.
        :raises GpuTypeNotAvailable: The requested GPU type is not available. Use a GPU type that is available in the deployment's resource queue.
        :raises InvalidGpuCount: The GPU count is invalid. The GPU count must be between 1 and the maximum allowed for the requested GPU type.
        :raises ModelNotFound: The given Model could not be found.
        :raises ThreadCountTooHigh: The specified thread count exceeds the maximum allowed value.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/liveDeployments",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.CreateLiveDeploymentRequest(
                    deployment_type=deployment_type,
                    runtime_configuration=runtime_configuration,
                ),
                response_type=models_models.LiveDeployment,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateLiveDeploymentPermissionDenied": models_errors.CreateLiveDeploymentPermissionDenied,
                    "GpuTypeNotAvailable": models_errors.GpuTypeNotAvailable,
                    "InvalidGpuCount": models_errors.InvalidGpuCount,
                    "ModelNotFound": models_errors.ModelNotFound,
                    "ThreadCountTooHigh": models_errors.ThreadCountTooHigh,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        live_deployment_rid: models_models.LiveDeploymentRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.LiveDeployment]:
        """
        Retrieves a live deployment by its Resource Identifier (RID), including its deployed model version and runtime configuration.

        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.LiveDeployment]

        :raises LiveDeploymentNotFound: The specified live deployment was not found.
        :raises UnsupportedLiveDeployment: The Live Deployment type is not supported by the API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "liveDeploymentRid": live_deployment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.LiveDeployment,
                request_timeout=request_timeout,
                throwable_errors={
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "UnsupportedLiveDeployment": models_errors.UnsupportedLiveDeployment,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace(
        self,
        live_deployment_rid: models_models.LiveDeploymentRid,
        *,
        runtime_configuration: models_models.LiveDeploymentRuntimeConfiguration,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.LiveDeployment]:
        """
        Updates the runtime configuration of the live deployment. The deployment will apply the new configuration to the running replicas.

        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param runtime_configuration: The compute resource configuration for the deployment.
        :type runtime_configuration: LiveDeploymentRuntimeConfiguration
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.LiveDeployment]

        :raises GpuTypeNotAvailable: The requested GPU type is not available. Use a GPU type that is available in the deployment's resource queue.
        :raises InvalidGpuCount: The GPU count is invalid. The GPU count must be between 1 and the maximum allowed for the requested GPU type.
        :raises LiveDeploymentNotFound: The specified live deployment was not found.
        :raises ReplaceLiveDeploymentPermissionDenied: Could not replace the LiveDeployment.
        :raises ThreadCountTooHigh: The specified thread count exceeds the maximum allowed value.
        :raises UnsupportedLiveDeployment: The Live Deployment type is not supported by the API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}",
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
                body=models_models.ReplaceLiveDeploymentRequest(
                    runtime_configuration=runtime_configuration,
                ),
                response_type=models_models.LiveDeployment,
                request_timeout=request_timeout,
                throwable_errors={
                    "GpuTypeNotAvailable": models_errors.GpuTypeNotAvailable,
                    "InvalidGpuCount": models_errors.InvalidGpuCount,
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "ReplaceLiveDeploymentPermissionDenied": models_errors.ReplaceLiveDeploymentPermissionDenied,
                    "ThreadCountTooHigh": models_errors.ThreadCountTooHigh,
                    "UnsupportedLiveDeployment": models_errors.UnsupportedLiveDeployment,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

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

        :raises InferenceFailure: The inference request failed due to a model execution error or unexpected internal issue. This typically indicates a problem with the model itself rather than the input data.
        :raises InferenceInvalidInput: The inference request contains invalid input data that does not match the model's API specification. Check the error type for specific validation failure details.
        :raises InferenceTimeout: The live deployment took longer than 5 minutes to respond to the inference request. This typically indicates the model execution is taking too long or the deployment is under heavy load.
        :raises LiveDeploymentNotFound: The specified live deployment was not found.
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
                    "InferenceFailure": models_errors.InferenceFailure,
                    "InferenceInvalidInput": models_errors.InferenceInvalidInput,
                    "InferenceTimeout": models_errors.InferenceTimeout,
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "TransformJsonLiveDeploymentPermissionDenied": models_errors.TransformJsonLiveDeploymentPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncLiveDeploymentClientRaw:
    def __init__(self, client: AsyncLiveDeploymentClient) -> None:
        def create(_: models_models.LiveDeployment): ...
        def get(_: models_models.LiveDeployment): ...
        def replace(_: models_models.LiveDeployment): ...
        def transform_json(_: models_models.TransformLiveDeploymentResponse): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.replace = core.async_with_raw_response(replace, client.replace)
        self.transform_json = core.async_with_raw_response(transform_json, client.transform_json)


class _AsyncLiveDeploymentClientStreaming:
    def __init__(self, client: AsyncLiveDeploymentClient) -> None:
        def create(_: models_models.LiveDeployment): ...
        def get(_: models_models.LiveDeployment): ...
        def replace(_: models_models.LiveDeployment): ...
        def transform_json(_: models_models.TransformLiveDeploymentResponse): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.replace = core.async_with_streaming_response(replace, client.replace)
        self.transform_json = core.async_with_streaming_response(
            transform_json, client.transform_json
        )
