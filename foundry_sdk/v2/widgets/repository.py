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
from foundry_sdk.v2.widgets import errors as widgets_errors
from foundry_sdk.v2.widgets import models as widgets_models


class RepositoryClient:
    """
    The API client for the Repository Resource.

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

        self.with_streaming_response = _RepositoryClientStreaming(self)
        self.with_raw_response = _RepositoryClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        repository_rid: widgets_models.RepositoryRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.Repository:
        """
        Get the Repository with the specified rid.
        :param repository_rid: A Resource Identifier (RID) identifying a repository.
        :type repository_rid: RepositoryRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.Repository

        :raises RepositoryNotFound: The given Repository could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/widgets/repositories/{repositoryRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "repositoryRid": repository_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.Repository,
                request_timeout=request_timeout,
                throwable_errors={
                    "RepositoryNotFound": widgets_errors.RepositoryNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def publish(
        self,
        repository_rid: widgets_models.RepositoryRid,
        body: bytes,
        *,
        repository_version: widgets_models.RepositoryVersion,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> widgets_models.Release:
        """
        Publish a new release of a widget set.
        :param repository_rid: A Resource Identifier (RID) identifying a repository.
        :type repository_rid: RepositoryRid
        :param body: The zip file that contains the contents of your widget set. It must include a valid manifest file at the path `.palantir/widgets.config.json`.
        :type body: bytes
        :param repository_version:
        :type repository_version: RepositoryVersion
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: widgets_models.Release

        :raises PublishReleasePermissionDenied: Could not publish the Repository.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/repositories/{repositoryRid}/publish",
                query_params={
                    "repositoryVersion": repository_version,
                    "preview": preview,
                },
                path_params={
                    "repositoryRid": repository_rid,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=widgets_models.Release,
                request_timeout=request_timeout,
                throwable_errors={
                    "PublishReleasePermissionDenied": widgets_errors.PublishReleasePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _RepositoryClientRaw:
    def __init__(self, client: RepositoryClient) -> None:
        def get(_: widgets_models.Repository): ...
        def publish(_: widgets_models.Release): ...

        self.get = core.with_raw_response(get, client.get)
        self.publish = core.with_raw_response(publish, client.publish)


class _RepositoryClientStreaming:
    def __init__(self, client: RepositoryClient) -> None:
        def get(_: widgets_models.Repository): ...
        def publish(_: widgets_models.Release): ...

        self.get = core.with_streaming_response(get, client.get)
        self.publish = core.with_streaming_response(publish, client.publish)


class AsyncRepositoryClient:
    """
    The API client for the Repository Resource.

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

        self.with_streaming_response = _AsyncRepositoryClientStreaming(self)
        self.with_raw_response = _AsyncRepositoryClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        repository_rid: widgets_models.RepositoryRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.Repository]:
        """
        Get the Repository with the specified rid.
        :param repository_rid: A Resource Identifier (RID) identifying a repository.
        :type repository_rid: RepositoryRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.Repository]

        :raises RepositoryNotFound: The given Repository could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/widgets/repositories/{repositoryRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "repositoryRid": repository_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=widgets_models.Repository,
                request_timeout=request_timeout,
                throwable_errors={
                    "RepositoryNotFound": widgets_errors.RepositoryNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def publish(
        self,
        repository_rid: widgets_models.RepositoryRid,
        body: bytes,
        *,
        repository_version: widgets_models.RepositoryVersion,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[widgets_models.Release]:
        """
        Publish a new release of a widget set.
        :param repository_rid: A Resource Identifier (RID) identifying a repository.
        :type repository_rid: RepositoryRid
        :param body: The zip file that contains the contents of your widget set. It must include a valid manifest file at the path `.palantir/widgets.config.json`.
        :type body: bytes
        :param repository_version:
        :type repository_version: RepositoryVersion
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[widgets_models.Release]

        :raises PublishReleasePermissionDenied: Could not publish the Repository.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/widgets/repositories/{repositoryRid}/publish",
                query_params={
                    "repositoryVersion": repository_version,
                    "preview": preview,
                },
                path_params={
                    "repositoryRid": repository_rid,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=widgets_models.Release,
                request_timeout=request_timeout,
                throwable_errors={
                    "PublishReleasePermissionDenied": widgets_errors.PublishReleasePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncRepositoryClientRaw:
    def __init__(self, client: AsyncRepositoryClient) -> None:
        def get(_: widgets_models.Repository): ...
        def publish(_: widgets_models.Release): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.publish = core.async_with_raw_response(publish, client.publish)


class _AsyncRepositoryClientStreaming:
    def __init__(self, client: AsyncRepositoryClient) -> None:
        def get(_: widgets_models.Repository): ...
        def publish(_: widgets_models.Release): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.publish = core.async_with_streaming_response(publish, client.publish)
