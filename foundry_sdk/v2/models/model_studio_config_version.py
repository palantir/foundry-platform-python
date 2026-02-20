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


class ModelStudioConfigVersionClient:
    """
    The API client for the ModelStudioConfigVersion Resource.

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

        self.with_streaming_response = _ModelStudioConfigVersionClientStreaming(self)
        self.with_raw_response = _ModelStudioConfigVersionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        *,
        name: models_models.ModelStudioConfigVersionName,
        resources: models_models.ResourceConfiguration,
        trainer_id: models_models.TrainerId,
        worker_config: models_models.ModelStudioWorkerConfig,
        changelog: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ModelStudioConfigVersion:
        """
        Creates a new Model Studio configuration version.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param name: Human readable name of the configuration version and experiment.
        :type name: ModelStudioConfigVersionName
        :param resources: The compute resources allocated for training runs.
        :type resources: ResourceConfiguration
        :param trainer_id: The identifier of the trainer to use for this configuration.
        :type trainer_id: TrainerId
        :param worker_config: The worker configuration including inputs, outputs, and custom settings.
        :type worker_config: ModelStudioWorkerConfig
        :param changelog: Changelog describing changes in this version.
        :type changelog: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelStudioConfigVersion

        :raises CreateModelStudioConfigVersionPermissionDenied: Could not create the ModelStudioConfigVersion.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/configVersions",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelStudioRid": model_studio_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.CreateModelStudioConfigVersionRequest(
                    name=name,
                    resources=resources,
                    changelog=changelog,
                    worker_config=worker_config,
                    trainer_id=trainer_id,
                ),
                response_type=models_models.ModelStudioConfigVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateModelStudioConfigVersionPermissionDenied": models_errors.CreateModelStudioConfigVersionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        model_studio_config_version_version: models_models.ModelStudioConfigVersionNumber,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ModelStudioConfigVersion:
        """
        Gets a specific Model Studio configuration version.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param model_studio_config_version_version: The version number of this configuration.
        :type model_studio_config_version_version: ModelStudioConfigVersionNumber
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelStudioConfigVersion

        :raises ModelStudioConfigVersionNotFound: The requested Model Studio configuration version was not found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/configVersions/{modelStudioConfigVersionVersion}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelStudioRid": model_studio_rid,
                    "modelStudioConfigVersionVersion": model_studio_config_version_version,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ModelStudioConfigVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelStudioConfigVersionNotFound": models_errors.ModelStudioConfigVersionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def latest(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Optional[models_models.ModelStudioConfigVersion]:
        """
        Gets the latest configuration version for a Model Studio.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Optional[models_models.ModelStudioConfigVersion]

        :raises LatestModelStudioConfigVersionsPermissionDenied: Could not latest the ModelStudioConfigVersion.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/configVersions/latest",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelStudioRid": model_studio_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=typing.Optional[models_models.ModelStudioConfigVersion],
                request_timeout=request_timeout,
                throwable_errors={
                    "LatestModelStudioConfigVersionsPermissionDenied": models_errors.LatestModelStudioConfigVersionsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[models_models.ModelStudioConfigVersion]:
        """
        Lists all configuration versions for a Model Studio.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[models_models.ModelStudioConfigVersion]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/configVersions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "modelStudioRid": model_studio_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ListModelStudioConfigVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _ModelStudioConfigVersionClientRaw:
    def __init__(self, client: ModelStudioConfigVersionClient) -> None:
        def create(_: models_models.ModelStudioConfigVersion): ...
        def get(_: models_models.ModelStudioConfigVersion): ...
        def latest(_: typing.Optional[models_models.ModelStudioConfigVersion]): ...
        def list(_: models_models.ListModelStudioConfigVersionsResponse): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.latest = core.with_raw_response(latest, client.latest)
        self.list = core.with_raw_response(list, client.list)


class _ModelStudioConfigVersionClientStreaming:
    def __init__(self, client: ModelStudioConfigVersionClient) -> None:
        def create(_: models_models.ModelStudioConfigVersion): ...
        def get(_: models_models.ModelStudioConfigVersion): ...
        def latest(_: typing.Optional[models_models.ModelStudioConfigVersion]): ...
        def list(_: models_models.ListModelStudioConfigVersionsResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.latest = core.with_streaming_response(latest, client.latest)
        self.list = core.with_streaming_response(list, client.list)


class AsyncModelStudioConfigVersionClient:
    """
    The API client for the ModelStudioConfigVersion Resource.

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

        self.with_streaming_response = _AsyncModelStudioConfigVersionClientStreaming(self)
        self.with_raw_response = _AsyncModelStudioConfigVersionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        *,
        name: models_models.ModelStudioConfigVersionName,
        resources: models_models.ResourceConfiguration,
        trainer_id: models_models.TrainerId,
        worker_config: models_models.ModelStudioWorkerConfig,
        changelog: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ModelStudioConfigVersion]:
        """
        Creates a new Model Studio configuration version.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param name: Human readable name of the configuration version and experiment.
        :type name: ModelStudioConfigVersionName
        :param resources: The compute resources allocated for training runs.
        :type resources: ResourceConfiguration
        :param trainer_id: The identifier of the trainer to use for this configuration.
        :type trainer_id: TrainerId
        :param worker_config: The worker configuration including inputs, outputs, and custom settings.
        :type worker_config: ModelStudioWorkerConfig
        :param changelog: Changelog describing changes in this version.
        :type changelog: Optional[str]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelStudioConfigVersion]

        :raises CreateModelStudioConfigVersionPermissionDenied: Could not create the ModelStudioConfigVersion.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/configVersions",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelStudioRid": model_studio_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.CreateModelStudioConfigVersionRequest(
                    name=name,
                    resources=resources,
                    changelog=changelog,
                    worker_config=worker_config,
                    trainer_id=trainer_id,
                ),
                response_type=models_models.ModelStudioConfigVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateModelStudioConfigVersionPermissionDenied": models_errors.CreateModelStudioConfigVersionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        model_studio_config_version_version: models_models.ModelStudioConfigVersionNumber,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ModelStudioConfigVersion]:
        """
        Gets a specific Model Studio configuration version.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param model_studio_config_version_version: The version number of this configuration.
        :type model_studio_config_version_version: ModelStudioConfigVersionNumber
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelStudioConfigVersion]

        :raises ModelStudioConfigVersionNotFound: The requested Model Studio configuration version was not found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/configVersions/{modelStudioConfigVersionVersion}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelStudioRid": model_studio_rid,
                    "modelStudioConfigVersionVersion": model_studio_config_version_version,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ModelStudioConfigVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelStudioConfigVersionNotFound": models_errors.ModelStudioConfigVersionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def latest(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[typing.Optional[models_models.ModelStudioConfigVersion]]:
        """
        Gets the latest configuration version for a Model Studio.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[typing.Optional[models_models.ModelStudioConfigVersion]]

        :raises LatestModelStudioConfigVersionsPermissionDenied: Could not latest the ModelStudioConfigVersion.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/configVersions/latest",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelStudioRid": model_studio_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=typing.Optional[models_models.ModelStudioConfigVersion],
                request_timeout=request_timeout,
                throwable_errors={
                    "LatestModelStudioConfigVersionsPermissionDenied": models_errors.LatestModelStudioConfigVersionsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[models_models.ModelStudioConfigVersion]:
        """
        Lists all configuration versions for a Model Studio.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[models_models.ModelStudioConfigVersion]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/configVersions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "modelStudioRid": model_studio_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ListModelStudioConfigVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncModelStudioConfigVersionClientRaw:
    def __init__(self, client: AsyncModelStudioConfigVersionClient) -> None:
        def create(_: models_models.ModelStudioConfigVersion): ...
        def get(_: models_models.ModelStudioConfigVersion): ...
        def latest(_: typing.Optional[models_models.ModelStudioConfigVersion]): ...
        def list(_: models_models.ListModelStudioConfigVersionsResponse): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.latest = core.async_with_raw_response(latest, client.latest)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncModelStudioConfigVersionClientStreaming:
    def __init__(self, client: AsyncModelStudioConfigVersionClient) -> None:
        def create(_: models_models.ModelStudioConfigVersion): ...
        def get(_: models_models.ModelStudioConfigVersion): ...
        def latest(_: typing.Optional[models_models.ModelStudioConfigVersion]): ...
        def list(_: models_models.ListModelStudioConfigVersionsResponse): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.latest = core.async_with_streaming_response(latest, client.latest)
        self.list = core.async_with_streaming_response(list, client.list)
