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
from foundry.v2.admin import errors as admin_errors
from foundry.v2.admin.models._host_name import HostName
from foundry.v2.admin.models._organization import Organization
from foundry.v2.admin.models._organization_name import OrganizationName
from foundry.v2.core.models._organization_rid import OrganizationRid
from foundry.v2.core.models._preview_mode import PreviewMode


class OrganizationClient:
    """
    The API client for the Organization Resource.

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
        self.with_streaming_response = _OrganizationClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _OrganizationClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        organization_rid: OrganizationRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Organization:
        """
        Get the Organization with the specified rid.
        :param organization_rid: organizationRid
        :type organization_rid: OrganizationRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Organization

        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/organizations/{organizationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Organization,
                request_timeout=request_timeout,
                throwable_errors={
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        organization_rid: OrganizationRid,
        *,
        name: OrganizationName,
        description: Optional[str] = None,
        host: Optional[HostName] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Organization:
        """
        Replace the Organization with the specified rid.
        :param organization_rid: organizationRid
        :type organization_rid: OrganizationRid
        :param name:
        :type name: OrganizationName
        :param description:
        :type description: Optional[str]
        :param host: The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.
        :type host: Optional[HostName]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Organization

        :raises InvalidHostName: The provided hostname must be a valid domain name. The only allowed characters are letters, numbers, periods, and hyphens.
        :raises ReplaceOrganizationPermissionDenied: Could not replace the Organization.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/admin/organizations/{organizationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "host": host,
                    "description": description,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": OrganizationName,
                        "host": Optional[HostName],
                        "description": Optional[str],
                    },
                ),
                response_type=Organization,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidHostName": admin_errors.InvalidHostName,
                    "ReplaceOrganizationPermissionDenied": admin_errors.ReplaceOrganizationPermissionDenied,
                },
            ),
        ).decode()


class _OrganizationClientRaw:
    """
    The API client for the Organization Resource.

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
    def get(
        self,
        organization_rid: OrganizationRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Organization]:
        """
        Get the Organization with the specified rid.
        :param organization_rid: organizationRid
        :type organization_rid: OrganizationRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Organization]

        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/organizations/{organizationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Organization,
                request_timeout=request_timeout,
                throwable_errors={
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        organization_rid: OrganizationRid,
        *,
        name: OrganizationName,
        description: Optional[str] = None,
        host: Optional[HostName] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Organization]:
        """
        Replace the Organization with the specified rid.
        :param organization_rid: organizationRid
        :type organization_rid: OrganizationRid
        :param name:
        :type name: OrganizationName
        :param description:
        :type description: Optional[str]
        :param host: The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.
        :type host: Optional[HostName]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Organization]

        :raises InvalidHostName: The provided hostname must be a valid domain name. The only allowed characters are letters, numbers, periods, and hyphens.
        :raises ReplaceOrganizationPermissionDenied: Could not replace the Organization.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/admin/organizations/{organizationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "host": host,
                    "description": description,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": OrganizationName,
                        "host": Optional[HostName],
                        "description": Optional[str],
                    },
                ),
                response_type=Organization,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidHostName": admin_errors.InvalidHostName,
                    "ReplaceOrganizationPermissionDenied": admin_errors.ReplaceOrganizationPermissionDenied,
                },
            ),
        )


class _OrganizationClientStreaming:
    """
    The API client for the Organization Resource.

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
    def get(
        self,
        organization_rid: OrganizationRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Organization]:
        """
        Get the Organization with the specified rid.
        :param organization_rid: organizationRid
        :type organization_rid: OrganizationRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Organization]

        :raises OrganizationNotFound: The given Organization could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/organizations/{organizationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Organization,
                request_timeout=request_timeout,
                throwable_errors={
                    "OrganizationNotFound": admin_errors.OrganizationNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def replace(
        self,
        organization_rid: OrganizationRid,
        *,
        name: OrganizationName,
        description: Optional[str] = None,
        host: Optional[HostName] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Organization]:
        """
        Replace the Organization with the specified rid.
        :param organization_rid: organizationRid
        :type organization_rid: OrganizationRid
        :param name:
        :type name: OrganizationName
        :param description:
        :type description: Optional[str]
        :param host: The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.
        :type host: Optional[HostName]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Organization]

        :raises InvalidHostName: The provided hostname must be a valid domain name. The only allowed characters are letters, numbers, periods, and hyphens.
        :raises ReplaceOrganizationPermissionDenied: Could not replace the Organization.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="PUT",
                resource_path="/v2/admin/organizations/{organizationRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "organizationRid": organization_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "host": host,
                    "description": description,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": OrganizationName,
                        "host": Optional[HostName],
                        "description": Optional[str],
                    },
                ),
                response_type=Organization,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidHostName": admin_errors.InvalidHostName,
                    "ReplaceOrganizationPermissionDenied": admin_errors.ReplaceOrganizationPermissionDenied,
                },
            ),
        )
