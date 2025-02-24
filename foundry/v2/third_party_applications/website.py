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


from __future__ import annotations

from functools import cached_property
from typing import Any
from typing import Dict
from typing import Optional

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.third_party_applications import errors as third_party_applications_errors  # NOQA
from foundry.v2.third_party_applications.models._third_party_application_rid import (
    ThirdPartyApplicationRid,
)  # NOQA
from foundry.v2.third_party_applications.models._version_version import VersionVersion
from foundry.v2.third_party_applications.models._website import Website


class WebsiteClient:
    """
    The API client for the Website Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _WebsiteClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _WebsiteClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def Version(self):
        from foundry.v2.third_party_applications.version import VersionClient

        return VersionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def deploy(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        version: VersionVersion,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Website:
        """
        Deploy a version of the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version:
        :type version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Website

        :raises DeployWebsitePermissionDenied: Could not deploy the Website.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "version": VersionVersion,
                    },
                ),
                response_type=Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeployWebsitePermissionDenied": third_party_applications_errors.DeployWebsitePermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Website:
        """
        Get the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Website

        :raises WebsiteNotFound: The given Website could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "WebsiteNotFound": third_party_applications_errors.WebsiteNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def undeploy(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Website:
        """
        Remove the currently deployed version of the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Website

        :raises UndeployWebsitePermissionDenied: Could not undeploy the Website.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "UndeployWebsitePermissionDenied": third_party_applications_errors.UndeployWebsitePermissionDenied,
                },
            ),
        ).decode()


class _WebsiteClientRaw:
    """
    The API client for the Website Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def deploy(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        version: VersionVersion,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Website]:
        """
        Deploy a version of the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version:
        :type version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Website]

        :raises DeployWebsitePermissionDenied: Could not deploy the Website.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "version": VersionVersion,
                    },
                ),
                response_type=Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeployWebsitePermissionDenied": third_party_applications_errors.DeployWebsitePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Website]:
        """
        Get the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Website]

        :raises WebsiteNotFound: The given Website could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "WebsiteNotFound": third_party_applications_errors.WebsiteNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def undeploy(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Website]:
        """
        Remove the currently deployed version of the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Website]

        :raises UndeployWebsitePermissionDenied: Could not undeploy the Website.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "UndeployWebsitePermissionDenied": third_party_applications_errors.UndeployWebsitePermissionDenied,
                },
            ),
        )


class _WebsiteClientStreaming:
    """
    The API client for the Website Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def deploy(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        version: VersionVersion,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Website]:
        """
        Deploy a version of the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param version:
        :type version: VersionVersion
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Website]

        :raises DeployWebsitePermissionDenied: Could not deploy the Website.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "version": VersionVersion,
                    },
                ),
                response_type=Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeployWebsitePermissionDenied": third_party_applications_errors.DeployWebsitePermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Website]:
        """
        Get the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Website]

        :raises WebsiteNotFound: The given Website could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "WebsiteNotFound": third_party_applications_errors.WebsiteNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def undeploy(
        self,
        third_party_application_rid: ThirdPartyApplicationRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Website]:
        """
        Remove the currently deployed version of the Website.
        :param third_party_application_rid: thirdPartyApplicationRid
        :type third_party_application_rid: ThirdPartyApplicationRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Website]

        :raises UndeployWebsitePermissionDenied: Could not undeploy the Website.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=Website,
                request_timeout=request_timeout,
                throwable_errors={
                    "UndeployWebsitePermissionDenied": third_party_applications_errors.UndeployWebsitePermissionDenied,
                },
            ),
        )
