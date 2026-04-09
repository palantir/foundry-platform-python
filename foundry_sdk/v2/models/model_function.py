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
from foundry_sdk.v2.ontologies import models as ontologies_models


class ModelFunctionClient:
    """
    The API client for the ModelFunction Resource.

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

        self.with_streaming_response = _ModelFunctionClientStreaming(self)
        self.with_raw_response = _ModelFunctionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        live_deployment_rid: models_models.LiveDeploymentRid,
        *,
        api_name: models_models.ModelFunctionApiName,
        display_name: models_models.ModelFunctionDisplayName,
        is_row_wise: models_models.ModelFunctionIsRowWise,
        ontology_binding: typing.Optional[ontologies_models.OntologyRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ModelFunction:
        """
        Creates a function for the live deployment.
        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param api_name:
        :type api_name: ModelFunctionApiName
        :param display_name:
        :type display_name: ModelFunctionDisplayName
        :param is_row_wise:
        :type is_row_wise: ModelFunctionIsRowWise
        :param ontology_binding:
        :type ontology_binding: Optional[OntologyRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelFunction

        :raises CreateModelFunctionPermissionDenied: Could not create the ModelFunction.
        :raises FunctionAlreadyExists: A function already exists for this live deployment.
        :raises InvalidFunctionApiName: The provided API name for the function is invalid.
        :raises LiveDeploymentNotFound: The specified live deployment was not found.
        :raises ModelApiTypeUnsupportedForFunction: The model API contains a data type that is not supported for Ontology function creation.
        :raises OntologyNotFound: The specified ontology was not found.
        :raises UnsupportedLiveDeployment: The Live Deployment type is not supported by the API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}/function",
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
                body=models_models.CreateModelFunctionRequest(
                    api_name=api_name,
                    ontology_binding=ontology_binding,
                    is_row_wise=is_row_wise,
                    display_name=display_name,
                ),
                response_type=models_models.ModelFunction,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateModelFunctionPermissionDenied": models_errors.CreateModelFunctionPermissionDenied,
                    "FunctionAlreadyExists": models_errors.FunctionAlreadyExists,
                    "InvalidFunctionApiName": models_errors.InvalidFunctionApiName,
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "ModelApiTypeUnsupportedForFunction": models_errors.ModelApiTypeUnsupportedForFunction,
                    "OntologyNotFound": models_errors.OntologyNotFound,
                    "UnsupportedLiveDeployment": models_errors.UnsupportedLiveDeployment,
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
    ) -> models_models.ModelFunction:
        """
        Gets the function for the live deployment.
        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelFunction

        :raises LiveDeploymentNotFound: The specified live deployment was not found.
        :raises ModelFunctionNotFound: The given ModelFunction could not be found.
        :raises UnsupportedLiveDeployment: The Live Deployment type is not supported by the API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}/function",
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
                response_type=models_models.ModelFunction,
                request_timeout=request_timeout,
                throwable_errors={
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "ModelFunctionNotFound": models_errors.ModelFunctionNotFound,
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
        api_name: models_models.ModelFunctionApiName,
        is_row_wise: models_models.ModelFunctionIsRowWise,
        ontology_binding: typing.Optional[ontologies_models.OntologyRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ModelFunction:
        """
        Replaces the function for the live deployment.
        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param api_name:
        :type api_name: ModelFunctionApiName
        :param is_row_wise:
        :type is_row_wise: ModelFunctionIsRowWise
        :param ontology_binding:
        :type ontology_binding: Optional[OntologyRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelFunction

        :raises InvalidFunctionApiName: The provided API name for the function is invalid.
        :raises LiveDeploymentNotFound: The specified live deployment was not found.
        :raises ModelApiTypeUnsupportedForFunction: The model API contains a data type that is not supported for Ontology function creation.
        :raises ModelFunctionNotFound: The given ModelFunction could not be found.
        :raises OntologyNotFound: The specified ontology was not found.
        :raises ReplaceModelFunctionPermissionDenied: Could not replace the ModelFunction.
        :raises UnsupportedLiveDeployment: The Live Deployment type is not supported by the API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}/function",
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
                body=models_models.ReplaceModelFunctionRequest(
                    api_name=api_name,
                    ontology_binding=ontology_binding,
                    is_row_wise=is_row_wise,
                ),
                response_type=models_models.ModelFunction,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidFunctionApiName": models_errors.InvalidFunctionApiName,
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "ModelApiTypeUnsupportedForFunction": models_errors.ModelApiTypeUnsupportedForFunction,
                    "ModelFunctionNotFound": models_errors.ModelFunctionNotFound,
                    "OntologyNotFound": models_errors.OntologyNotFound,
                    "ReplaceModelFunctionPermissionDenied": models_errors.ReplaceModelFunctionPermissionDenied,
                    "UnsupportedLiveDeployment": models_errors.UnsupportedLiveDeployment,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ModelFunctionClientRaw:
    def __init__(self, client: ModelFunctionClient) -> None:
        def create(_: models_models.ModelFunction): ...
        def get(_: models_models.ModelFunction): ...
        def replace(_: models_models.ModelFunction): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.replace = core.with_raw_response(replace, client.replace)


class _ModelFunctionClientStreaming:
    def __init__(self, client: ModelFunctionClient) -> None:
        def create(_: models_models.ModelFunction): ...
        def get(_: models_models.ModelFunction): ...
        def replace(_: models_models.ModelFunction): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.replace = core.with_streaming_response(replace, client.replace)


class AsyncModelFunctionClient:
    """
    The API client for the ModelFunction Resource.

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

        self.with_streaming_response = _AsyncModelFunctionClientStreaming(self)
        self.with_raw_response = _AsyncModelFunctionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        live_deployment_rid: models_models.LiveDeploymentRid,
        *,
        api_name: models_models.ModelFunctionApiName,
        display_name: models_models.ModelFunctionDisplayName,
        is_row_wise: models_models.ModelFunctionIsRowWise,
        ontology_binding: typing.Optional[ontologies_models.OntologyRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ModelFunction]:
        """
        Creates a function for the live deployment.
        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param api_name:
        :type api_name: ModelFunctionApiName
        :param display_name:
        :type display_name: ModelFunctionDisplayName
        :param is_row_wise:
        :type is_row_wise: ModelFunctionIsRowWise
        :param ontology_binding:
        :type ontology_binding: Optional[OntologyRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelFunction]

        :raises CreateModelFunctionPermissionDenied: Could not create the ModelFunction.
        :raises FunctionAlreadyExists: A function already exists for this live deployment.
        :raises InvalidFunctionApiName: The provided API name for the function is invalid.
        :raises LiveDeploymentNotFound: The specified live deployment was not found.
        :raises ModelApiTypeUnsupportedForFunction: The model API contains a data type that is not supported for Ontology function creation.
        :raises OntologyNotFound: The specified ontology was not found.
        :raises UnsupportedLiveDeployment: The Live Deployment type is not supported by the API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}/function",
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
                body=models_models.CreateModelFunctionRequest(
                    api_name=api_name,
                    ontology_binding=ontology_binding,
                    is_row_wise=is_row_wise,
                    display_name=display_name,
                ),
                response_type=models_models.ModelFunction,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateModelFunctionPermissionDenied": models_errors.CreateModelFunctionPermissionDenied,
                    "FunctionAlreadyExists": models_errors.FunctionAlreadyExists,
                    "InvalidFunctionApiName": models_errors.InvalidFunctionApiName,
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "ModelApiTypeUnsupportedForFunction": models_errors.ModelApiTypeUnsupportedForFunction,
                    "OntologyNotFound": models_errors.OntologyNotFound,
                    "UnsupportedLiveDeployment": models_errors.UnsupportedLiveDeployment,
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
    ) -> typing.Awaitable[models_models.ModelFunction]:
        """
        Gets the function for the live deployment.
        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelFunction]

        :raises LiveDeploymentNotFound: The specified live deployment was not found.
        :raises ModelFunctionNotFound: The given ModelFunction could not be found.
        :raises UnsupportedLiveDeployment: The Live Deployment type is not supported by the API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}/function",
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
                response_type=models_models.ModelFunction,
                request_timeout=request_timeout,
                throwable_errors={
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "ModelFunctionNotFound": models_errors.ModelFunctionNotFound,
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
        api_name: models_models.ModelFunctionApiName,
        is_row_wise: models_models.ModelFunctionIsRowWise,
        ontology_binding: typing.Optional[ontologies_models.OntologyRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ModelFunction]:
        """
        Replaces the function for the live deployment.
        :param live_deployment_rid:
        :type live_deployment_rid: LiveDeploymentRid
        :param api_name:
        :type api_name: ModelFunctionApiName
        :param is_row_wise:
        :type is_row_wise: ModelFunctionIsRowWise
        :param ontology_binding:
        :type ontology_binding: Optional[OntologyRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelFunction]

        :raises InvalidFunctionApiName: The provided API name for the function is invalid.
        :raises LiveDeploymentNotFound: The specified live deployment was not found.
        :raises ModelApiTypeUnsupportedForFunction: The model API contains a data type that is not supported for Ontology function creation.
        :raises ModelFunctionNotFound: The given ModelFunction could not be found.
        :raises OntologyNotFound: The specified ontology was not found.
        :raises ReplaceModelFunctionPermissionDenied: Could not replace the ModelFunction.
        :raises UnsupportedLiveDeployment: The Live Deployment type is not supported by the API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/models/liveDeployments/{liveDeploymentRid}/function",
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
                body=models_models.ReplaceModelFunctionRequest(
                    api_name=api_name,
                    ontology_binding=ontology_binding,
                    is_row_wise=is_row_wise,
                ),
                response_type=models_models.ModelFunction,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidFunctionApiName": models_errors.InvalidFunctionApiName,
                    "LiveDeploymentNotFound": models_errors.LiveDeploymentNotFound,
                    "ModelApiTypeUnsupportedForFunction": models_errors.ModelApiTypeUnsupportedForFunction,
                    "ModelFunctionNotFound": models_errors.ModelFunctionNotFound,
                    "OntologyNotFound": models_errors.OntologyNotFound,
                    "ReplaceModelFunctionPermissionDenied": models_errors.ReplaceModelFunctionPermissionDenied,
                    "UnsupportedLiveDeployment": models_errors.UnsupportedLiveDeployment,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncModelFunctionClientRaw:
    def __init__(self, client: AsyncModelFunctionClient) -> None:
        def create(_: models_models.ModelFunction): ...
        def get(_: models_models.ModelFunction): ...
        def replace(_: models_models.ModelFunction): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.replace = core.async_with_raw_response(replace, client.replace)


class _AsyncModelFunctionClientStreaming:
    def __init__(self, client: AsyncModelFunctionClient) -> None:
        def create(_: models_models.ModelFunction): ...
        def get(_: models_models.ModelFunction): ...
        def replace(_: models_models.ModelFunction): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.replace = core.async_with_streaming_response(replace, client.replace)
