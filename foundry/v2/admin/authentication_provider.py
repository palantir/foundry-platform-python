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
from typing import List
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
from foundry.v2.admin.models._attribute_name import AttributeName
from foundry.v2.admin.models._attribute_values import AttributeValues
from foundry.v2.admin.models._authentication_provider import AuthenticationProvider
from foundry.v2.admin.models._authentication_provider_rid import AuthenticationProviderRid  # NOQA
from foundry.v2.admin.models._group_name import GroupName
from foundry.v2.admin.models._list_authentication_providers_response import (
    ListAuthenticationProvidersResponse,
)  # NOQA
from foundry.v2.admin.models._user_username import UserUsername
from foundry.v2.core.models._enrollment_rid import EnrollmentRid
from foundry.v2.core.models._organization_rid import OrganizationRid
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.core.models._principal_id import PrincipalId


class AuthenticationProviderClient:
    """
    The API client for the AuthenticationProvider Resource.

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
        self.with_streaming_response = _AuthenticationProviderClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _AuthenticationProviderClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        enrollment_rid: EnrollmentRid,
        authentication_provider_rid: AuthenticationProviderRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> AuthenticationProvider:
        """
        Get the AuthenticationProvider with the specified rid.
        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid: authenticationProviderRid
        :type authentication_provider_rid: AuthenticationProviderRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AuthenticationProvider

        :raises AuthenticationProviderNotFound: The given AuthenticationProvider could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                    "authenticationProviderRid": authentication_provider_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AuthenticationProvider,
                request_timeout=request_timeout,
                throwable_errors={
                    "AuthenticationProviderNotFound": admin_errors.AuthenticationProviderNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        enrollment_rid: EnrollmentRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListAuthenticationProvidersResponse:
        """
        Lists all AuthenticationProviders.


        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListAuthenticationProvidersResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListAuthenticationProvidersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def preregister_group(
        self,
        enrollment_rid: EnrollmentRid,
        authentication_provider_rid: AuthenticationProviderRid,
        *,
        name: GroupName,
        organizations: List[OrganizationRid],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> PrincipalId:
        """
        Register a Group with a given name before any users with this group log in through this Authentication Provider.
        Preregistered groups can be used anywhere other groups are used in the platform.

        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid: authenticationProviderRid
        :type authentication_provider_rid: AuthenticationProviderRid
        :param name:
        :type name: GroupName
        :param organizations: The RIDs of the Organizations that can view this group.
        :type organizations: List[OrganizationRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: PrincipalId

        :raises PreregisterGroupPermissionDenied: Could not preregisterGroup the AuthenticationProvider.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterGroup",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                    "authenticationProviderRid": authentication_provider_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "organizations": organizations,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": GroupName,
                        "organizations": List[OrganizationRid],
                    },
                ),
                response_type=PrincipalId,
                request_timeout=request_timeout,
                throwable_errors={
                    "PreregisterGroupPermissionDenied": admin_errors.PreregisterGroupPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def preregister_user(
        self,
        enrollment_rid: EnrollmentRid,
        authentication_provider_rid: AuthenticationProviderRid,
        *,
        organization: OrganizationRid,
        username: UserUsername,
        attributes: Optional[Dict[AttributeName, AttributeValues]] = None,
        email: Optional[str] = None,
        family_name: Optional[str] = None,
        given_name: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> PrincipalId:
        """
        Register a User with a given username before they log in to the platform for the first time through this
        Authentication Provider. Preregistered users can be assigned to groups and roles prior to first login.

        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid: authenticationProviderRid
        :type authentication_provider_rid: AuthenticationProviderRid
        :param organization: The RID of the user's primary Organization. This may be changed when the user logs in for the first time depending on any configured Organization assignment rules.
        :type organization: OrganizationRid
        :param username: The new user's username. This must match one of the provider's supported username patterns.
        :type username: UserUsername
        :param attributes:
        :type attributes: Optional[Dict[AttributeName, AttributeValues]]
        :param email:
        :type email: Optional[str]
        :param family_name:
        :type family_name: Optional[str]
        :param given_name:
        :type given_name: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: PrincipalId

        :raises PreregisterUserPermissionDenied: Could not preregisterUser the AuthenticationProvider.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterUser",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                    "authenticationProviderRid": authentication_provider_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "username": username,
                    "organization": organization,
                    "givenName": given_name,
                    "familyName": family_name,
                    "email": email,
                    "attributes": attributes,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "username": UserUsername,
                        "organization": OrganizationRid,
                        "givenName": Optional[str],
                        "familyName": Optional[str],
                        "email": Optional[str],
                        "attributes": Optional[Dict[AttributeName, AttributeValues]],
                    },
                ),
                response_type=PrincipalId,
                request_timeout=request_timeout,
                throwable_errors={
                    "PreregisterUserPermissionDenied": admin_errors.PreregisterUserPermissionDenied,
                },
            ),
        ).decode()


class _AuthenticationProviderClientRaw:
    """
    The API client for the AuthenticationProvider Resource.

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
        enrollment_rid: EnrollmentRid,
        authentication_provider_rid: AuthenticationProviderRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[AuthenticationProvider]:
        """
        Get the AuthenticationProvider with the specified rid.
        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid: authenticationProviderRid
        :type authentication_provider_rid: AuthenticationProviderRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[AuthenticationProvider]

        :raises AuthenticationProviderNotFound: The given AuthenticationProvider could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                    "authenticationProviderRid": authentication_provider_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AuthenticationProvider,
                request_timeout=request_timeout,
                throwable_errors={
                    "AuthenticationProviderNotFound": admin_errors.AuthenticationProviderNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        enrollment_rid: EnrollmentRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListAuthenticationProvidersResponse]:
        """
        Lists all AuthenticationProviders.


        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListAuthenticationProvidersResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListAuthenticationProvidersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def preregister_group(
        self,
        enrollment_rid: EnrollmentRid,
        authentication_provider_rid: AuthenticationProviderRid,
        *,
        name: GroupName,
        organizations: List[OrganizationRid],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[PrincipalId]:
        """
        Register a Group with a given name before any users with this group log in through this Authentication Provider.
        Preregistered groups can be used anywhere other groups are used in the platform.

        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid: authenticationProviderRid
        :type authentication_provider_rid: AuthenticationProviderRid
        :param name:
        :type name: GroupName
        :param organizations: The RIDs of the Organizations that can view this group.
        :type organizations: List[OrganizationRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[PrincipalId]

        :raises PreregisterGroupPermissionDenied: Could not preregisterGroup the AuthenticationProvider.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterGroup",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                    "authenticationProviderRid": authentication_provider_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "organizations": organizations,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": GroupName,
                        "organizations": List[OrganizationRid],
                    },
                ),
                response_type=PrincipalId,
                request_timeout=request_timeout,
                throwable_errors={
                    "PreregisterGroupPermissionDenied": admin_errors.PreregisterGroupPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def preregister_user(
        self,
        enrollment_rid: EnrollmentRid,
        authentication_provider_rid: AuthenticationProviderRid,
        *,
        organization: OrganizationRid,
        username: UserUsername,
        attributes: Optional[Dict[AttributeName, AttributeValues]] = None,
        email: Optional[str] = None,
        family_name: Optional[str] = None,
        given_name: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[PrincipalId]:
        """
        Register a User with a given username before they log in to the platform for the first time through this
        Authentication Provider. Preregistered users can be assigned to groups and roles prior to first login.

        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid: authenticationProviderRid
        :type authentication_provider_rid: AuthenticationProviderRid
        :param organization: The RID of the user's primary Organization. This may be changed when the user logs in for the first time depending on any configured Organization assignment rules.
        :type organization: OrganizationRid
        :param username: The new user's username. This must match one of the provider's supported username patterns.
        :type username: UserUsername
        :param attributes:
        :type attributes: Optional[Dict[AttributeName, AttributeValues]]
        :param email:
        :type email: Optional[str]
        :param family_name:
        :type family_name: Optional[str]
        :param given_name:
        :type given_name: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[PrincipalId]

        :raises PreregisterUserPermissionDenied: Could not preregisterUser the AuthenticationProvider.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterUser",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                    "authenticationProviderRid": authentication_provider_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "username": username,
                    "organization": organization,
                    "givenName": given_name,
                    "familyName": family_name,
                    "email": email,
                    "attributes": attributes,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "username": UserUsername,
                        "organization": OrganizationRid,
                        "givenName": Optional[str],
                        "familyName": Optional[str],
                        "email": Optional[str],
                        "attributes": Optional[Dict[AttributeName, AttributeValues]],
                    },
                ),
                response_type=PrincipalId,
                request_timeout=request_timeout,
                throwable_errors={
                    "PreregisterUserPermissionDenied": admin_errors.PreregisterUserPermissionDenied,
                },
            ),
        )


class _AuthenticationProviderClientStreaming:
    """
    The API client for the AuthenticationProvider Resource.

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
        enrollment_rid: EnrollmentRid,
        authentication_provider_rid: AuthenticationProviderRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[AuthenticationProvider]:
        """
        Get the AuthenticationProvider with the specified rid.
        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid: authenticationProviderRid
        :type authentication_provider_rid: AuthenticationProviderRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[AuthenticationProvider]

        :raises AuthenticationProviderNotFound: The given AuthenticationProvider could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                    "authenticationProviderRid": authentication_provider_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=AuthenticationProvider,
                request_timeout=request_timeout,
                throwable_errors={
                    "AuthenticationProviderNotFound": admin_errors.AuthenticationProviderNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        enrollment_rid: EnrollmentRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListAuthenticationProvidersResponse]:
        """
        Lists all AuthenticationProviders.


        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListAuthenticationProvidersResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListAuthenticationProvidersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def preregister_group(
        self,
        enrollment_rid: EnrollmentRid,
        authentication_provider_rid: AuthenticationProviderRid,
        *,
        name: GroupName,
        organizations: List[OrganizationRid],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[PrincipalId]:
        """
        Register a Group with a given name before any users with this group log in through this Authentication Provider.
        Preregistered groups can be used anywhere other groups are used in the platform.

        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid: authenticationProviderRid
        :type authentication_provider_rid: AuthenticationProviderRid
        :param name:
        :type name: GroupName
        :param organizations: The RIDs of the Organizations that can view this group.
        :type organizations: List[OrganizationRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[PrincipalId]

        :raises PreregisterGroupPermissionDenied: Could not preregisterGroup the AuthenticationProvider.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterGroup",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                    "authenticationProviderRid": authentication_provider_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "organizations": organizations,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": GroupName,
                        "organizations": List[OrganizationRid],
                    },
                ),
                response_type=PrincipalId,
                request_timeout=request_timeout,
                throwable_errors={
                    "PreregisterGroupPermissionDenied": admin_errors.PreregisterGroupPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def preregister_user(
        self,
        enrollment_rid: EnrollmentRid,
        authentication_provider_rid: AuthenticationProviderRid,
        *,
        organization: OrganizationRid,
        username: UserUsername,
        attributes: Optional[Dict[AttributeName, AttributeValues]] = None,
        email: Optional[str] = None,
        family_name: Optional[str] = None,
        given_name: Optional[str] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[PrincipalId]:
        """
        Register a User with a given username before they log in to the platform for the first time through this
        Authentication Provider. Preregistered users can be assigned to groups and roles prior to first login.

        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid: authenticationProviderRid
        :type authentication_provider_rid: AuthenticationProviderRid
        :param organization: The RID of the user's primary Organization. This may be changed when the user logs in for the first time depending on any configured Organization assignment rules.
        :type organization: OrganizationRid
        :param username: The new user's username. This must match one of the provider's supported username patterns.
        :type username: UserUsername
        :param attributes:
        :type attributes: Optional[Dict[AttributeName, AttributeValues]]
        :param email:
        :type email: Optional[str]
        :param family_name:
        :type family_name: Optional[str]
        :param given_name:
        :type given_name: Optional[str]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[PrincipalId]

        :raises PreregisterUserPermissionDenied: Could not preregisterUser the AuthenticationProvider.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterUser",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                    "authenticationProviderRid": authentication_provider_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "username": username,
                    "organization": organization,
                    "givenName": given_name,
                    "familyName": family_name,
                    "email": email,
                    "attributes": attributes,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "username": UserUsername,
                        "organization": OrganizationRid,
                        "givenName": Optional[str],
                        "familyName": Optional[str],
                        "email": Optional[str],
                        "attributes": Optional[Dict[AttributeName, AttributeValues]],
                    },
                ),
                response_type=PrincipalId,
                request_timeout=request_timeout,
                throwable_errors={
                    "PreregisterUserPermissionDenied": admin_errors.PreregisterUserPermissionDenied,
                },
            ),
        )
