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

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.filesystem import errors as filesystem_errors
from foundry_sdk.v2.filesystem import models as filesystem_models
from foundry_sdk.v2.models import errors as models_errors
from foundry_sdk.v2.models import models as models_models


class ModelStudioClient:
    """
    The API client for the ModelStudio Resource.

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

        self.with_streaming_response = _ModelStudioClientStreaming(self)
        self.with_raw_response = _ModelStudioClientRaw(self)

    @cached_property
    def Run(self):
        from foundry_sdk.v2.models.model_studio_run import ModelStudioRunClient

        return ModelStudioRunClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def ConfigVersion(self):
        from foundry_sdk.v2.models.model_studio_config_version import (
            ModelStudioConfigVersionClient,
        )  # NOQA

        return ModelStudioConfigVersionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        name: str,
        parent_folder_rid: filesystem_models.FolderRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ModelStudio:
        """
        Creates a new Model Studio.
        :param name: The name of the Model Studio.
        :type name: str
        :param parent_folder_rid: The RID of the parent folder where the studio will be created.
        :type parent_folder_rid: FolderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelStudio

        :raises CreateModelStudioPermissionDenied: Permission denied to create a Model Studio.
        :raises InvalidDisplayName: The display name of a Resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/modelStudios",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.CreateModelStudioRequest(
                    name=name,
                    parent_folder_rid=parent_folder_rid,
                ),
                response_type=models_models.ModelStudio,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateModelStudioPermissionDenied": models_errors.CreateModelStudioPermissionDenied,
                    "InvalidDisplayName": filesystem_errors.InvalidDisplayName,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
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
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ModelStudio:
        """
        Gets details about a Model Studio by its RID.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelStudio

        :raises ModelStudioNotFound: The requested Model Studio was not found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudios/{modelStudioRid}",
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
                response_type=models_models.ModelStudio,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelStudioNotFound": models_errors.ModelStudioNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def launch(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ModelStudioRun:
        """
        Launches a new training run for the Model Studio using the latest configuration version.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelStudioRun

        :raises LaunchModelStudioPermissionDenied: Permission denied to launch a Model Studio run.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/launch",
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
                response_type=models_models.ModelStudioRun,
                request_timeout=request_timeout,
                throwable_errors={
                    "LaunchModelStudioPermissionDenied": models_errors.LaunchModelStudioPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ModelStudioClientRaw:
    def __init__(self, client: ModelStudioClient) -> None:
        def create(_: models_models.ModelStudio): ...
        def get(_: models_models.ModelStudio): ...
        def launch(_: models_models.ModelStudioRun): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.launch = core.with_raw_response(launch, client.launch)


class _ModelStudioClientStreaming:
    def __init__(self, client: ModelStudioClient) -> None:
        def create(_: models_models.ModelStudio): ...
        def get(_: models_models.ModelStudio): ...
        def launch(_: models_models.ModelStudioRun): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.launch = core.with_streaming_response(launch, client.launch)


class AsyncModelStudioClient:
    """
    The API client for the ModelStudio Resource.

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

        self.with_streaming_response = _AsyncModelStudioClientStreaming(self)
        self.with_raw_response = _AsyncModelStudioClientRaw(self)

    @cached_property
    def Run(self):
        from foundry_sdk.v2.models.model_studio_run import AsyncModelStudioRunClient

        return AsyncModelStudioRunClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def ConfigVersion(self):
        from foundry_sdk.v2.models.model_studio_config_version import (
            AsyncModelStudioConfigVersionClient,
        )  # NOQA

        return AsyncModelStudioConfigVersionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        name: str,
        parent_folder_rid: filesystem_models.FolderRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ModelStudio]:
        """
        Creates a new Model Studio.
        :param name: The name of the Model Studio.
        :type name: str
        :param parent_folder_rid: The RID of the parent folder where the studio will be created.
        :type parent_folder_rid: FolderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelStudio]

        :raises CreateModelStudioPermissionDenied: Permission denied to create a Model Studio.
        :raises InvalidDisplayName: The display name of a Resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/modelStudios",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.CreateModelStudioRequest(
                    name=name,
                    parent_folder_rid=parent_folder_rid,
                ),
                response_type=models_models.ModelStudio,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateModelStudioPermissionDenied": models_errors.CreateModelStudioPermissionDenied,
                    "InvalidDisplayName": filesystem_errors.InvalidDisplayName,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
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
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ModelStudio]:
        """
        Gets details about a Model Studio by its RID.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelStudio]

        :raises ModelStudioNotFound: The requested Model Studio was not found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/modelStudios/{modelStudioRid}",
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
                response_type=models_models.ModelStudio,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelStudioNotFound": models_errors.ModelStudioNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def launch(
        self,
        model_studio_rid: models_models.ModelStudioRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ModelStudioRun]:
        """
        Launches a new training run for the Model Studio using the latest configuration version.
        :param model_studio_rid:
        :type model_studio_rid: ModelStudioRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelStudioRun]

        :raises LaunchModelStudioPermissionDenied: Permission denied to launch a Model Studio run.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/modelStudios/{modelStudioRid}/launch",
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
                response_type=models_models.ModelStudioRun,
                request_timeout=request_timeout,
                throwable_errors={
                    "LaunchModelStudioPermissionDenied": models_errors.LaunchModelStudioPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncModelStudioClientRaw:
    def __init__(self, client: AsyncModelStudioClient) -> None:
        def create(_: models_models.ModelStudio): ...
        def get(_: models_models.ModelStudio): ...
        def launch(_: models_models.ModelStudioRun): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.launch = core.async_with_raw_response(launch, client.launch)


class _AsyncModelStudioClientStreaming:
    def __init__(self, client: AsyncModelStudioClient) -> None:
        def create(_: models_models.ModelStudio): ...
        def get(_: models_models.ModelStudio): ...
        def launch(_: models_models.ModelStudioRun): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.launch = core.async_with_streaming_response(launch, client.launch)
