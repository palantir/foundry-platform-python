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
from foundry_sdk.v2.admin import errors as admin_errors
from foundry_sdk.v2.admin import models as admin_models
from foundry_sdk.v2.core import models as core_models


class EnrollmentRoleAssignmentClient:
    """
    The API client for the EnrollmentRoleAssignment Resource.

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

        self.with_streaming_response = _EnrollmentRoleAssignmentClientStreaming(self)
        self.with_raw_response = _EnrollmentRoleAssignmentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        *,
        role_assignments: typing.List[core_models.RoleAssignmentUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Assign roles to principals for the given Enrollment. At most 100 role assignments can be added in a single request.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param role_assignments:
        :type role_assignments: List[RoleAssignmentUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AddEnrollmentRoleAssignmentsPermissionDenied: Could not add the EnrollmentRoleAssignment.
        :raises EnrollmentNotFound: The given Enrollment could not be found.
        :raises EnrollmentRoleNotFound: One of the provided role IDs was not found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/roleAssignments/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[core_models.RoleAssignmentUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddEnrollmentRoleAssignmentsPermissionDenied": admin_errors.AddEnrollmentRoleAssignmentsPermissionDenied,
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                    "EnrollmentRoleNotFound": admin_errors.EnrollmentRoleNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> admin_models.ListEnrollmentRoleAssignmentsResponse:
        """
        List all principals who are assigned a role for the given Enrollment.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.ListEnrollmentRoleAssignmentsResponse

        :raises EnrollmentNotFound: The given Enrollment could not be found.
        :raises ListEnrollmentRoleAssignmentsPermissionDenied: The provided token does not have permission to list assigned roles for this enrollment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/roleAssignments",
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
                response_type=admin_models.ListEnrollmentRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                    "ListEnrollmentRoleAssignmentsPermissionDenied": admin_errors.ListEnrollmentRoleAssignmentsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        *,
        role_assignments: typing.List[core_models.RoleAssignmentUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Remove roles from principals for the given Enrollment. At most 100 role assignments can be removed in a single request.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param role_assignments:
        :type role_assignments: List[RoleAssignmentUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises EnrollmentNotFound: The given Enrollment could not be found.
        :raises EnrollmentRoleNotFound: One of the provided role IDs was not found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveEnrollmentRoleAssignmentsPermissionDenied: Could not remove the EnrollmentRoleAssignment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/roleAssignments/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[core_models.RoleAssignmentUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                    "EnrollmentRoleNotFound": admin_errors.EnrollmentRoleNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveEnrollmentRoleAssignmentsPermissionDenied": admin_errors.RemoveEnrollmentRoleAssignmentsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _EnrollmentRoleAssignmentClientRaw:
    def __init__(self, client: EnrollmentRoleAssignmentClient) -> None:
        def add(_: None): ...
        def list(_: admin_models.ListEnrollmentRoleAssignmentsResponse): ...
        def remove(_: None): ...

        self.add = core.with_raw_response(add, client.add)
        self.list = core.with_raw_response(list, client.list)
        self.remove = core.with_raw_response(remove, client.remove)


class _EnrollmentRoleAssignmentClientStreaming:
    def __init__(self, client: EnrollmentRoleAssignmentClient) -> None:
        def list(_: admin_models.ListEnrollmentRoleAssignmentsResponse): ...

        self.list = core.with_streaming_response(list, client.list)


class AsyncEnrollmentRoleAssignmentClient:
    """
    The API client for the EnrollmentRoleAssignment Resource.

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

        self.with_streaming_response = _AsyncEnrollmentRoleAssignmentClientStreaming(self)
        self.with_raw_response = _AsyncEnrollmentRoleAssignmentClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        *,
        role_assignments: typing.List[core_models.RoleAssignmentUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Assign roles to principals for the given Enrollment. At most 100 role assignments can be added in a single request.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param role_assignments:
        :type role_assignments: List[RoleAssignmentUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises AddEnrollmentRoleAssignmentsPermissionDenied: Could not add the EnrollmentRoleAssignment.
        :raises EnrollmentNotFound: The given Enrollment could not be found.
        :raises EnrollmentRoleNotFound: One of the provided role IDs was not found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/roleAssignments/add",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[core_models.RoleAssignmentUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AddEnrollmentRoleAssignmentsPermissionDenied": admin_errors.AddEnrollmentRoleAssignmentsPermissionDenied,
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                    "EnrollmentRoleNotFound": admin_errors.EnrollmentRoleNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[admin_models.ListEnrollmentRoleAssignmentsResponse]:
        """
        List all principals who are assigned a role for the given Enrollment.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[admin_models.ListEnrollmentRoleAssignmentsResponse]

        :raises EnrollmentNotFound: The given Enrollment could not be found.
        :raises ListEnrollmentRoleAssignmentsPermissionDenied: The provided token does not have permission to list assigned roles for this enrollment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/roleAssignments",
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
                response_type=admin_models.ListEnrollmentRoleAssignmentsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                    "ListEnrollmentRoleAssignmentsPermissionDenied": admin_errors.ListEnrollmentRoleAssignmentsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        *,
        role_assignments: typing.List[core_models.RoleAssignmentUpdate],
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Remove roles from principals for the given Enrollment. At most 100 role assignments can be removed in a single request.

        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param role_assignments:
        :type role_assignments: List[RoleAssignmentUpdate]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises EnrollmentNotFound: The given Enrollment could not be found.
        :raises EnrollmentRoleNotFound: One of the provided role IDs was not found.
        :raises PrincipalNotFound: A principal (User or Group) with the given PrincipalId could not be found
        :raises RemoveEnrollmentRoleAssignmentsPermissionDenied: Could not remove the EnrollmentRoleAssignment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/admin/enrollments/{enrollmentRid}/roleAssignments/remove",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "enrollmentRid": enrollment_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "roleAssignments": role_assignments,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "roleAssignments": typing.List[core_models.RoleAssignmentUpdate],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                    "EnrollmentRoleNotFound": admin_errors.EnrollmentRoleNotFound,
                    "PrincipalNotFound": admin_errors.PrincipalNotFound,
                    "RemoveEnrollmentRoleAssignmentsPermissionDenied": admin_errors.RemoveEnrollmentRoleAssignmentsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncEnrollmentRoleAssignmentClientRaw:
    def __init__(self, client: AsyncEnrollmentRoleAssignmentClient) -> None:
        def add(_: None): ...
        def list(_: admin_models.ListEnrollmentRoleAssignmentsResponse): ...
        def remove(_: None): ...

        self.add = core.async_with_raw_response(add, client.add)
        self.list = core.async_with_raw_response(list, client.list)
        self.remove = core.async_with_raw_response(remove, client.remove)


class _AsyncEnrollmentRoleAssignmentClientStreaming:
    def __init__(self, client: AsyncEnrollmentRoleAssignmentClient) -> None:
        def list(_: admin_models.ListEnrollmentRoleAssignmentsResponse): ...

        self.list = core.async_with_streaming_response(list, client.list)
