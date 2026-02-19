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


class ModelStudioTrainerClient:
    """
    The API client for the ModelStudioTrainer Resource.

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

        self.with_streaming_response = _ModelStudioTrainerClientStreaming(self)
        self.with_raw_response = _ModelStudioTrainerClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        model_studio_trainer_trainer_id: models_models.TrainerId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        version: typing.Optional[models_models.TrainerVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ModelStudioTrainer:
        """
        Gets details about a specific trainer by its ID and optional version.
        :param model_studio_trainer_trainer_id:
        :type model_studio_trainer_trainer_id: TrainerId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version: Specific version of the trainer to retrieve. If not specified, returns the latest version.
        :type version: Optional[TrainerVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelStudioTrainer

        :raises ModelStudioTrainerNotFound: The given ModelStudioTrainer could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudioTrainers/{modelStudioTrainerTrainerId}",
                query_params={
                    "preview": preview,
                    "version": version,
                },
                path_params={
                    "modelStudioTrainerTrainerId": model_studio_trainer_trainer_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ModelStudioTrainer,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelStudioTrainerNotFound": models_errors.ModelStudioTrainerNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ListModelStudioTrainersResponse:
        """
        Lists all available trainers for Model Studios.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ListModelStudioTrainersResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudioTrainers",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ListModelStudioTrainersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ModelStudioTrainerClientRaw:
    def __init__(self, client: ModelStudioTrainerClient) -> None:
        def get(_: models_models.ModelStudioTrainer): ...
        def list(_: models_models.ListModelStudioTrainersResponse): ...

        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)


class _ModelStudioTrainerClientStreaming:
    def __init__(self, client: ModelStudioTrainerClient) -> None:
        def get(_: models_models.ModelStudioTrainer): ...
        def list(_: models_models.ListModelStudioTrainersResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)


class AsyncModelStudioTrainerClient:
    """
    The API client for the ModelStudioTrainer Resource.

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

        self.with_streaming_response = _AsyncModelStudioTrainerClientStreaming(self)
        self.with_raw_response = _AsyncModelStudioTrainerClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        model_studio_trainer_trainer_id: models_models.TrainerId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        version: typing.Optional[models_models.TrainerVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ModelStudioTrainer]:
        """
        Gets details about a specific trainer by its ID and optional version.
        :param model_studio_trainer_trainer_id:
        :type model_studio_trainer_trainer_id: TrainerId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version: Specific version of the trainer to retrieve. If not specified, returns the latest version.
        :type version: Optional[TrainerVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelStudioTrainer]

        :raises ModelStudioTrainerNotFound: The given ModelStudioTrainer could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudioTrainers/{modelStudioTrainerTrainerId}",
                query_params={
                    "preview": preview,
                    "version": version,
                },
                path_params={
                    "modelStudioTrainerTrainerId": model_studio_trainer_trainer_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ModelStudioTrainer,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelStudioTrainerNotFound": models_errors.ModelStudioTrainerNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ListModelStudioTrainersResponse]:
        """
        Lists all available trainers for Model Studios.
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ListModelStudioTrainersResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudioTrainers",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ListModelStudioTrainersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncModelStudioTrainerClientRaw:
    def __init__(self, client: AsyncModelStudioTrainerClient) -> None:
        def get(_: models_models.ModelStudioTrainer): ...
        def list(_: models_models.ListModelStudioTrainersResponse): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncModelStudioTrainerClientStreaming:
    def __init__(self, client: AsyncModelStudioTrainerClient) -> None:
        def get(_: models_models.ModelStudioTrainer): ...
        def list(_: models_models.ListModelStudioTrainersResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
