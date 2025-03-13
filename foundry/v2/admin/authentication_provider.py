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

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.admin import errors as admin_errors
from foundry.v2.admin import models as admin_models
from foundry.v2.core import models as core_models


class AuthenticationProviderClient:
    """
    The API client for the AuthenticationProvider Resource.

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
        self.with_streaming_response = _AuthenticationProviderClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _AuthenticationProviderClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        authentication_provider_rid: admin_models.AuthenticationProviderRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.AuthenticationProvider:
        """
        Get the AuthenticationProvider with the specified rid.
        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid:
        :type authentication_provider_rid: AuthenticationProviderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.AuthenticationProvider

        :raises AuthenticationProviderNotFound: The given AuthenticationProvider could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=admin_models.AuthenticationProvider,
                request_timeout=request_timeout,
                throwable_errors={
                    "AuthenticationProviderNotFound": admin_errors.AuthenticationProviderNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.ListAuthenticationProvidersResponse:
        """
        Lists all AuthenticationProviders.


        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.ListAuthenticationProvidersResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=admin_models.ListAuthenticationProvidersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def preregister_group(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        authentication_provider_rid: admin_models.AuthenticationProviderRid,
        *,
        name: admin_models.GroupName,
        organizations: typing.List[core_models.OrganizationRid],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core_models.PrincipalId:
        """
        Register a Group with a given name before any users with this group log in through this Authentication Provider.
        Preregistered groups can be used anywhere other groups are used in the platform.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid:
        :type authentication_provider_rid: AuthenticationProviderRid
        :param name:
        :type name: GroupName
        :param organizations: The RIDs of the Organizations that can view this group.
        :type organizations: List[OrganizationRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core_models.PrincipalId

        :raises PreregisterGroupPermissionDenied: Could not preregisterGroup the AuthenticationProvider.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.GroupName,
                        "organizations": typing.List[core_models.OrganizationRid],
                    },
                ),
                response_type=core_models.PrincipalId,
                request_timeout=request_timeout,
                throwable_errors={
                    "PreregisterGroupPermissionDenied": admin_errors.PreregisterGroupPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def preregister_user(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        authentication_provider_rid: admin_models.AuthenticationProviderRid,
        *,
        organization: core_models.OrganizationRid,
        username: admin_models.UserUsername,
        attributes: typing.Optional[
            typing.Dict[admin_models.AttributeName, admin_models.AttributeValues]
        ] = None,
        email: typing.Optional[str] = None,
        family_name: typing.Optional[str] = None,
        given_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core_models.PrincipalId:
        """
        Register a User with a given username before they log in to the platform for the first time through this
        Authentication Provider. Preregistered users can be assigned to groups and roles prior to first login.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid:
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
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core_models.PrincipalId

        :raises PreregisterUserPermissionDenied: Could not preregisterUser the AuthenticationProvider.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "username": admin_models.UserUsername,
                        "organization": core_models.OrganizationRid,
                        "givenName": typing.Optional[str],
                        "familyName": typing.Optional[str],
                        "email": typing.Optional[str],
                        "attributes": typing.Optional[
                            typing.Dict[admin_models.AttributeName, admin_models.AttributeValues]
                        ],
                    },
                ),
                response_type=core_models.PrincipalId,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        authentication_provider_rid: admin_models.AuthenticationProviderRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.AuthenticationProvider]:
        """
        Get the AuthenticationProvider with the specified rid.
        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid:
        :type authentication_provider_rid: AuthenticationProviderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.AuthenticationProvider]

        :raises AuthenticationProviderNotFound: The given AuthenticationProvider could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=admin_models.AuthenticationProvider,
                request_timeout=request_timeout,
                throwable_errors={
                    "AuthenticationProviderNotFound": admin_errors.AuthenticationProviderNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.ListAuthenticationProvidersResponse]:
        """
        Lists all AuthenticationProviders.


        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.ListAuthenticationProvidersResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=admin_models.ListAuthenticationProvidersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def preregister_group(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        authentication_provider_rid: admin_models.AuthenticationProviderRid,
        *,
        name: admin_models.GroupName,
        organizations: typing.List[core_models.OrganizationRid],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[core_models.PrincipalId]:
        """
        Register a Group with a given name before any users with this group log in through this Authentication Provider.
        Preregistered groups can be used anywhere other groups are used in the platform.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid:
        :type authentication_provider_rid: AuthenticationProviderRid
        :param name:
        :type name: GroupName
        :param organizations: The RIDs of the Organizations that can view this group.
        :type organizations: List[OrganizationRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[core_models.PrincipalId]

        :raises PreregisterGroupPermissionDenied: Could not preregisterGroup the AuthenticationProvider.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.GroupName,
                        "organizations": typing.List[core_models.OrganizationRid],
                    },
                ),
                response_type=core_models.PrincipalId,
                request_timeout=request_timeout,
                throwable_errors={
                    "PreregisterGroupPermissionDenied": admin_errors.PreregisterGroupPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def preregister_user(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        authentication_provider_rid: admin_models.AuthenticationProviderRid,
        *,
        organization: core_models.OrganizationRid,
        username: admin_models.UserUsername,
        attributes: typing.Optional[
            typing.Dict[admin_models.AttributeName, admin_models.AttributeValues]
        ] = None,
        email: typing.Optional[str] = None,
        family_name: typing.Optional[str] = None,
        given_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[core_models.PrincipalId]:
        """
        Register a User with a given username before they log in to the platform for the first time through this
        Authentication Provider. Preregistered users can be assigned to groups and roles prior to first login.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid:
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
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[core_models.PrincipalId]

        :raises PreregisterUserPermissionDenied: Could not preregisterUser the AuthenticationProvider.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "username": admin_models.UserUsername,
                        "organization": core_models.OrganizationRid,
                        "givenName": typing.Optional[str],
                        "familyName": typing.Optional[str],
                        "email": typing.Optional[str],
                        "attributes": typing.Optional[
                            typing.Dict[admin_models.AttributeName, admin_models.AttributeValues]
                        ],
                    },
                ),
                response_type=core_models.PrincipalId,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        authentication_provider_rid: admin_models.AuthenticationProviderRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.AuthenticationProvider]:
        """
        Get the AuthenticationProvider with the specified rid.
        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid:
        :type authentication_provider_rid: AuthenticationProviderRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.AuthenticationProvider]

        :raises AuthenticationProviderNotFound: The given AuthenticationProvider could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=admin_models.AuthenticationProvider,
                request_timeout=request_timeout,
                throwable_errors={
                    "AuthenticationProviderNotFound": admin_errors.AuthenticationProviderNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.ListAuthenticationProvidersResponse]:
        """
        Lists all AuthenticationProviders.


        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.ListAuthenticationProvidersResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=admin_models.ListAuthenticationProvidersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def preregister_group(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        authentication_provider_rid: admin_models.AuthenticationProviderRid,
        *,
        name: admin_models.GroupName,
        organizations: typing.List[core_models.OrganizationRid],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[core_models.PrincipalId]:
        """
        Register a Group with a given name before any users with this group log in through this Authentication Provider.
        Preregistered groups can be used anywhere other groups are used in the platform.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid:
        :type authentication_provider_rid: AuthenticationProviderRid
        :param name:
        :type name: GroupName
        :param organizations: The RIDs of the Organizations that can view this group.
        :type organizations: List[OrganizationRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[core_models.PrincipalId]

        :raises PreregisterGroupPermissionDenied: Could not preregisterGroup the AuthenticationProvider.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": admin_models.GroupName,
                        "organizations": typing.List[core_models.OrganizationRid],
                    },
                ),
                response_type=core_models.PrincipalId,
                request_timeout=request_timeout,
                throwable_errors={
                    "PreregisterGroupPermissionDenied": admin_errors.PreregisterGroupPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def preregister_user(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        authentication_provider_rid: admin_models.AuthenticationProviderRid,
        *,
        organization: core_models.OrganizationRid,
        username: admin_models.UserUsername,
        attributes: typing.Optional[
            typing.Dict[admin_models.AttributeName, admin_models.AttributeValues]
        ] = None,
        email: typing.Optional[str] = None,
        family_name: typing.Optional[str] = None,
        given_name: typing.Optional[str] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[core_models.PrincipalId]:
        """
        Register a User with a given username before they log in to the platform for the first time through this
        Authentication Provider. Preregistered users can be assigned to groups and roles prior to first login.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param authentication_provider_rid:
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
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[core_models.PrincipalId]

        :raises PreregisterUserPermissionDenied: Could not preregisterUser the AuthenticationProvider.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "username": admin_models.UserUsername,
                        "organization": core_models.OrganizationRid,
                        "givenName": typing.Optional[str],
                        "familyName": typing.Optional[str],
                        "email": typing.Optional[str],
                        "attributes": typing.Optional[
                            typing.Dict[admin_models.AttributeName, admin_models.AttributeValues]
                        ],
                    },
                ),
                response_type=core_models.PrincipalId,
                request_timeout=request_timeout,
                throwable_errors={
                    "PreregisterUserPermissionDenied": admin_errors.PreregisterUserPermissionDenied,
                },
            ),
        )
