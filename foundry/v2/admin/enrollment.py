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

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.admin import errors as admin_errors
from foundry.v2.admin import models as admin_models
from foundry.v2.core import models as core_models


class EnrollmentClient:
    """
    The API client for the Enrollment Resource.

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
        self.with_streaming_response = _EnrollmentClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _EnrollmentClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def Host(self):
        from foundry.v2.admin.host import HostClient

        return HostClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def AuthenticationProvider(self):
        from foundry.v2.admin.authentication_provider import AuthenticationProviderClient  # NOQA

        return AuthenticationProviderClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        enrollment_rid: core_models.EnrollmentRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.Enrollment:
        """
        Get the Enrollment with the specified rid.
        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Enrollment

        :raises EnrollmentNotFound: The given Enrollment could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}",
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
                response_type=admin_models.Enrollment,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_current(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> admin_models.Enrollment:
        """
        Returns the Enrollment associated with the current User's primary organization.

        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: admin_models.Enrollment

        :raises GetCurrentEnrollmentPermissionDenied: Could not getCurrent the Enrollment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/getCurrent",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.Enrollment,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetCurrentEnrollmentPermissionDenied": admin_errors.GetCurrentEnrollmentPermissionDenied,
                },
            ),
        ).decode()


class _EnrollmentClientRaw:
    """
    The API client for the Enrollment Resource.

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
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.Enrollment]:
        """
        Get the Enrollment with the specified rid.
        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.Enrollment]

        :raises EnrollmentNotFound: The given Enrollment could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}",
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
                response_type=admin_models.Enrollment,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_current(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[admin_models.Enrollment]:
        """
        Returns the Enrollment associated with the current User's primary organization.

        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[admin_models.Enrollment]

        :raises GetCurrentEnrollmentPermissionDenied: Could not getCurrent the Enrollment.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/getCurrent",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.Enrollment,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetCurrentEnrollmentPermissionDenied": admin_errors.GetCurrentEnrollmentPermissionDenied,
                },
            ),
        )


class _EnrollmentClientStreaming:
    """
    The API client for the Enrollment Resource.

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
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.Enrollment]:
        """
        Get the Enrollment with the specified rid.
        :param enrollment_rid:
        :type enrollment_rid: EnrollmentRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.Enrollment]

        :raises EnrollmentNotFound: The given Enrollment could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/{enrollmentRid}",
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
                response_type=admin_models.Enrollment,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_current(
        self,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[admin_models.Enrollment]:
        """
        Returns the Enrollment associated with the current User's primary organization.

        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[admin_models.Enrollment]

        :raises GetCurrentEnrollmentPermissionDenied: Could not getCurrent the Enrollment.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/admin/enrollments/getCurrent",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=admin_models.Enrollment,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetCurrentEnrollmentPermissionDenied": admin_errors.GetCurrentEnrollmentPermissionDenied,
                },
            ),
        )
