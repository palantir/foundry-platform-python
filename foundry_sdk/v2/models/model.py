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


class ModelClient:
    """
    The API client for the Model Resource.

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

        self.with_streaming_response = _ModelClientStreaming(self)
        self.with_raw_response = _ModelClientRaw(self)

    @cached_property
    def Experiment(self):
        from foundry_sdk.v2.models.experiment import ExperimentClient

        return ExperimentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Version(self):
        from foundry_sdk.v2.models.model_version import ModelVersionClient

        return ModelVersionClient(
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
        name: models_models.ModelName,
        parent_folder_rid: filesystem_models.FolderRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.Model:
        """
        Creates a new Model with no versions.
        :param name:
        :type name: ModelName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.Model

        :raises CreateModelPermissionDenied: Could not create the Model.
        :raises InvalidDisplayName: The display name of a Resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.CreateModelRequest(
                    name=name,
                    parent_folder_rid=parent_folder_rid,
                ),
                response_type=models_models.Model,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateModelPermissionDenied": models_errors.CreateModelPermissionDenied,
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
        model_rid: models_models.ModelRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.Model:
        """
        Retrieves a Model by its Resource Identifier (RID).
        :param model_rid:
        :type model_rid: ModelRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.Model

        :raises ModelNotFound: The given Model could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.Model,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelNotFound": models_errors.ModelNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def promote_version(
        self,
        model_rid: models_models.ModelRid,
        *,
        source_model_version_rid: models_models.ModelVersionRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> models_models.ModelVersion:
        """
        Promotes an existing Model Version to the target Model. The promoted Model Version will be copied to the target Model as the latest version on the master branch, but will have a new Model Version RID.

        :param model_rid:
        :type model_rid: ModelRid
        :param source_model_version_rid:
        :type source_model_version_rid: ModelVersionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: models_models.ModelVersion

        :raises ModelNotFound: The given Model could not be found.
        :raises ModelVersionNotFound: The given ModelVersion could not be found.
        :raises PromoteVersionModelPermissionDenied: Could not promoteVersion the Model.
        :raises UnsupportedModelSource: The Model Version has a source type that is not supported by the API. This can occur when the model was created through a legacy or internal workflow that is not exposed through the public API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/{modelRid}/promoteVersion",
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
                body=models_models.PromoteVersionModelRequest(
                    source_model_version_rid=source_model_version_rid,
                ),
                response_type=models_models.ModelVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelNotFound": models_errors.ModelNotFound,
                    "ModelVersionNotFound": models_errors.ModelVersionNotFound,
                    "PromoteVersionModelPermissionDenied": models_errors.PromoteVersionModelPermissionDenied,
                    "UnsupportedModelSource": models_errors.UnsupportedModelSource,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _ModelClientRaw:
    def __init__(self, client: ModelClient) -> None:
        def create(_: models_models.Model): ...
        def get(_: models_models.Model): ...
        def promote_version(_: models_models.ModelVersion): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.promote_version = core.with_raw_response(promote_version, client.promote_version)


class _ModelClientStreaming:
    def __init__(self, client: ModelClient) -> None:
        def create(_: models_models.Model): ...
        def get(_: models_models.Model): ...
        def promote_version(_: models_models.ModelVersion): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.promote_version = core.with_streaming_response(promote_version, client.promote_version)


class AsyncModelClient:
    """
    The API client for the Model Resource.

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

        self.with_streaming_response = _AsyncModelClientStreaming(self)
        self.with_raw_response = _AsyncModelClientRaw(self)

    @cached_property
    def Experiment(self):
        from foundry_sdk.v2.models.experiment import AsyncExperimentClient

        return AsyncExperimentClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Version(self):
        from foundry_sdk.v2.models.model_version import AsyncModelVersionClient

        return AsyncModelVersionClient(
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
        name: models_models.ModelName,
        parent_folder_rid: filesystem_models.FolderRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.Model]:
        """
        Creates a new Model with no versions.
        :param name:
        :type name: ModelName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.Model]

        :raises CreateModelPermissionDenied: Could not create the Model.
        :raises InvalidDisplayName: The display name of a Resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=models_models.CreateModelRequest(
                    name=name,
                    parent_folder_rid=parent_folder_rid,
                ),
                response_type=models_models.Model,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateModelPermissionDenied": models_errors.CreateModelPermissionDenied,
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
        model_rid: models_models.ModelRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.Model]:
        """
        Retrieves a Model by its Resource Identifier (RID).
        :param model_rid:
        :type model_rid: ModelRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.Model]

        :raises ModelNotFound: The given Model could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/models/{modelRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "modelRid": model_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=models_models.Model,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelNotFound": models_errors.ModelNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def promote_version(
        self,
        model_rid: models_models.ModelRid,
        *,
        source_model_version_rid: models_models.ModelVersionRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[models_models.ModelVersion]:
        """
        Promotes an existing Model Version to the target Model. The promoted Model Version will be copied to the target Model as the latest version on the master branch, but will have a new Model Version RID.

        :param model_rid:
        :type model_rid: ModelRid
        :param source_model_version_rid:
        :type source_model_version_rid: ModelVersionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[models_models.ModelVersion]

        :raises ModelNotFound: The given Model could not be found.
        :raises ModelVersionNotFound: The given ModelVersion could not be found.
        :raises PromoteVersionModelPermissionDenied: Could not promoteVersion the Model.
        :raises UnsupportedModelSource: The Model Version has a source type that is not supported by the API. This can occur when the model was created through a legacy or internal workflow that is not exposed through the public API.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/models/{modelRid}/promoteVersion",
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
                body=models_models.PromoteVersionModelRequest(
                    source_model_version_rid=source_model_version_rid,
                ),
                response_type=models_models.ModelVersion,
                request_timeout=request_timeout,
                throwable_errors={
                    "ModelNotFound": models_errors.ModelNotFound,
                    "ModelVersionNotFound": models_errors.ModelVersionNotFound,
                    "PromoteVersionModelPermissionDenied": models_errors.PromoteVersionModelPermissionDenied,
                    "UnsupportedModelSource": models_errors.UnsupportedModelSource,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncModelClientRaw:
    def __init__(self, client: AsyncModelClient) -> None:
        def create(_: models_models.Model): ...
        def get(_: models_models.Model): ...
        def promote_version(_: models_models.ModelVersion): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.promote_version = core.async_with_raw_response(promote_version, client.promote_version)


class _AsyncModelClientStreaming:
    def __init__(self, client: AsyncModelClient) -> None:
        def create(_: models_models.Model): ...
        def get(_: models_models.Model): ...
        def promote_version(_: models_models.ModelVersion): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.promote_version = core.async_with_streaming_response(
            promote_version, client.promote_version
        )
