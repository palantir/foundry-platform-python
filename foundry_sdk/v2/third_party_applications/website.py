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
from foundry_sdk.v2.third_party_applications import (
    errors as third_party_applications_errors,
)  # NOQA
from foundry_sdk.v2.third_party_applications import (
    models as third_party_applications_models,
)  # NOQA


class WebsiteClient:
    """
    The API client for the Website Resource.

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

        self.with_streaming_response = _WebsiteClientStreaming(self)
        self.with_raw_response = _WebsiteClientRaw(self)

    @cached_property
    def Version(self):
        from foundry_sdk.v2.third_party_applications.version import VersionClient

        return VersionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def deploy(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        version: third_party_applications_models.VersionVersion,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> third_party_applications_models.Website:
        """
        Deploy a version of the Website.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version:
        :type version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: third_party_applications_models.Website

        :raises DeployWebsitePermissionDenied: Could not deploy the Website.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/deploy",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "version": version,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "version": third_party_applications_models.VersionVersion,
                    },
                ),
                response_type=third_party_applications_models.Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeployWebsitePermissionDenied": third_party_applications_errors.DeployWebsitePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> third_party_applications_models.Website:
        """
        Get the Website.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: third_party_applications_models.Website

        :raises WebsiteNotFound: The given Website could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=third_party_applications_models.Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "WebsiteNotFound": third_party_applications_errors.WebsiteNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def undeploy(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> third_party_applications_models.Website:
        """
        Remove the currently deployed version of the Website.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: third_party_applications_models.Website

        :raises UndeployWebsitePermissionDenied: Could not undeploy the Website.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/undeploy",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=third_party_applications_models.Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "UndeployWebsitePermissionDenied": third_party_applications_errors.UndeployWebsitePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _WebsiteClientRaw:
    def __init__(self, client: WebsiteClient) -> None:
        def deploy(_: third_party_applications_models.Website): ...
        def get(_: third_party_applications_models.Website): ...
        def undeploy(_: third_party_applications_models.Website): ...

        self.deploy = core.with_raw_response(deploy, client.deploy)
        self.get = core.with_raw_response(get, client.get)
        self.undeploy = core.with_raw_response(undeploy, client.undeploy)


class _WebsiteClientStreaming:
    def __init__(self, client: WebsiteClient) -> None:
        def deploy(_: third_party_applications_models.Website): ...
        def get(_: third_party_applications_models.Website): ...
        def undeploy(_: third_party_applications_models.Website): ...

        self.deploy = core.with_streaming_response(deploy, client.deploy)
        self.get = core.with_streaming_response(get, client.get)
        self.undeploy = core.with_streaming_response(undeploy, client.undeploy)


class AsyncWebsiteClient:
    """
    The API client for the Website Resource.

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

        self.with_streaming_response = _AsyncWebsiteClientStreaming(self)
        self.with_raw_response = _AsyncWebsiteClientRaw(self)

    @cached_property
    def Version(self):
        from foundry_sdk.v2.third_party_applications.version import AsyncVersionClient

        return AsyncVersionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def deploy(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        version: third_party_applications_models.VersionVersion,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[third_party_applications_models.Website]:
        """
        Deploy a version of the Website.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version:
        :type version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[third_party_applications_models.Website]

        :raises DeployWebsitePermissionDenied: Could not deploy the Website.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/deploy",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "version": version,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "version": third_party_applications_models.VersionVersion,
                    },
                ),
                response_type=third_party_applications_models.Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeployWebsitePermissionDenied": third_party_applications_errors.DeployWebsitePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[third_party_applications_models.Website]:
        """
        Get the Website.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[third_party_applications_models.Website]

        :raises WebsiteNotFound: The given Website could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=third_party_applications_models.Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "WebsiteNotFound": third_party_applications_errors.WebsiteNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def undeploy(
        self,
        third_party_application_rid: third_party_applications_models.ThirdPartyApplicationRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[third_party_applications_models.Website]:
        """
        Remove the currently deployed version of the Website.
        :param third_party_application_rid: An RID identifying a third-party application created in Developer Console.
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[third_party_applications_models.Website]

        :raises UndeployWebsitePermissionDenied: Could not undeploy the Website.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/undeploy",
                query_params={},
                path_params={
                    "thirdPartyApplicationRid": third_party_application_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=third_party_applications_models.Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "UndeployWebsitePermissionDenied": third_party_applications_errors.UndeployWebsitePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncWebsiteClientRaw:
    def __init__(self, client: AsyncWebsiteClient) -> None:
        def deploy(_: third_party_applications_models.Website): ...
        def get(_: third_party_applications_models.Website): ...
        def undeploy(_: third_party_applications_models.Website): ...

        self.deploy = core.async_with_raw_response(deploy, client.deploy)
        self.get = core.async_with_raw_response(get, client.get)
        self.undeploy = core.async_with_raw_response(undeploy, client.undeploy)


class _AsyncWebsiteClientStreaming:
    def __init__(self, client: AsyncWebsiteClient) -> None:
        def deploy(_: third_party_applications_models.Website): ...
        def get(_: third_party_applications_models.Website): ...
        def undeploy(_: third_party_applications_models.Website): ...

        self.deploy = core.async_with_streaming_response(deploy, client.deploy)
        self.get = core.async_with_streaming_response(get, client.get)
        self.undeploy = core.async_with_streaming_response(undeploy, client.undeploy)
