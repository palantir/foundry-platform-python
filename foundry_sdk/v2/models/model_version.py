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


class ModelVersionClient:
    """
    The API client for the ModelVersion Resource.

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

        self.with_streaming_response = _ModelVersionClientStreaming(self)
        self.with_raw_response = _ModelVersionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        model_rid: models_models.ModelRid,
        *,
        backing_repositories: typing.List[core.RID],
        conda_requirements: typing.List[str],
        model_api: models_models.ModelApi,
        model_files: models_models.ModelFiles,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ModelVersion:
        """
        Creates a new Model Version on an existing model.
        :param model_rid:
        :type model_rid: ModelRid
        :param backing_repositories:
        :type backing_repositories: List[RID]
        :param conda_requirements:
        :type conda_requirements: List[str]
        :param model_api:
        :type model_api: ModelApi
        :param model_files:
        :type model_files: ModelFiles
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelVersion

        :raises CreateModelVersionPermissionDenied: Could not create the ModelVersion.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/{modelRid}/versions",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.CreateModelVersionRequest(
                    model_files=model_files,
                    backing_repositories=backing_repositories,
                    conda_requirements=conda_requirements,
                    model_api=model_api,
                ),
                response_type=models_models.ModelVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateModelVersionPermissionDenied": models_errors.CreateModelVersionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        model_rid: models_models.ModelRid,
        model_version_rid: models_models.ModelVersionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ModelVersion:
        """
        Retrieves a Model Version by its Resource Identifier (RID).
        :param model_rid:
        :type model_rid: ModelRid
        :param model_version_rid:
        :type model_version_rid: ModelVersionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelVersion

        :raises ModelVersionNotFound: The given ModelVersion could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/versions/{modelVersionRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "modelVersionRid": model_version_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ModelVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelVersionNotFound": models_errors.ModelVersionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        model_rid: models_models.ModelRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[models_models.ModelVersion]:
        """
        Lists all Model Versions for a given Model.
        :param model_rid:
        :type model_rid: ModelRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[models_models.ModelVersion]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/versions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ListModelVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _ModelVersionClientRaw:
    def __init__(self, client: ModelVersionClient) -> None:
        def create(_: models_models.ModelVersion): ...
        def get(_: models_models.ModelVersion): ...
        def list(_: models_models.ListModelVersionsResponse): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)


class _ModelVersionClientStreaming:
    def __init__(self, client: ModelVersionClient) -> None:
        def create(_: models_models.ModelVersion): ...
        def get(_: models_models.ModelVersion): ...
        def list(_: models_models.ListModelVersionsResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)


class AsyncModelVersionClient:
    """
    The API client for the ModelVersion Resource.

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

        self.with_streaming_response = _AsyncModelVersionClientStreaming(self)
        self.with_raw_response = _AsyncModelVersionClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        model_rid: models_models.ModelRid,
        *,
        backing_repositories: typing.List[core.RID],
        conda_requirements: typing.List[str],
        model_api: models_models.ModelApi,
        model_files: models_models.ModelFiles,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ModelVersion]:
        """
        Creates a new Model Version on an existing model.
        :param model_rid:
        :type model_rid: ModelRid
        :param backing_repositories:
        :type backing_repositories: List[RID]
        :param conda_requirements:
        :type conda_requirements: List[str]
        :param model_api:
        :type model_api: ModelApi
        :param model_files:
        :type model_files: ModelFiles
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelVersion]

        :raises CreateModelVersionPermissionDenied: Could not create the ModelVersion.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/{modelRid}/versions",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.CreateModelVersionRequest(
                    model_files=model_files,
                    backing_repositories=backing_repositories,
                    conda_requirements=conda_requirements,
                    model_api=model_api,
                ),
                response_type=models_models.ModelVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateModelVersionPermissionDenied": models_errors.CreateModelVersionPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        model_rid: models_models.ModelRid,
        model_version_rid: models_models.ModelVersionRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ModelVersion]:
        """
        Retrieves a Model Version by its Resource Identifier (RID).
        :param model_rid:
        :type model_rid: ModelRid
        :param model_version_rid:
        :type model_version_rid: ModelVersionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelVersion]

        :raises ModelVersionNotFound: The given ModelVersion could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/versions/{modelVersionRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                    "modelVersionRid": model_version_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ModelVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelVersionNotFound": models_errors.ModelVersionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        model_rid: models_models.ModelRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[models_models.ModelVersion]:
        """
        Lists all Model Versions for a given Model.
        :param model_rid:
        :type model_rid: ModelRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[models_models.ModelVersion]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}/versions",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.ListModelVersionsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncModelVersionClientRaw:
    def __init__(self, client: AsyncModelVersionClient) -> None:
        def create(_: models_models.ModelVersion): ...
        def get(_: models_models.ModelVersion): ...
        def list(_: models_models.ListModelVersionsResponse): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncModelVersionClientStreaming:
    def __init__(self, client: AsyncModelVersionClient) -> None:
        def create(_: models_models.ModelVersion): ...
        def get(_: models_models.ModelVersion): ...
        def list(_: models_models.ListModelVersionsResponse): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
