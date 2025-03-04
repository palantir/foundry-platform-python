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

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.admin import errors as admin_errors
from foundry.v2.admin.models._enrollment import Enrollment
from foundry.v2.core.models._enrollment_rid import EnrollmentRid
from foundry.v2.core.models._preview_mode import PreviewMode


class EnrollmentClient:
    """
    The API client for the Enrollment Resource.

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

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        enrollment_rid: EnrollmentRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Enrollment:
        """
        Get the Enrollment with the specified rid.
        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Enrollment

        :raises EnrollmentNotFound: The given Enrollment could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Enrollment,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_current(
        self,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Enrollment:
        """
        Returns the Enrollment associated with the current User's primary organization.

        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Enrollment

        :raises GetCurrentEnrollmentPermissionDenied: Could not getCurrent the Enrollment.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Enrollment,
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
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Enrollment]:
        """
        Get the Enrollment with the specified rid.
        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Enrollment]

        :raises EnrollmentNotFound: The given Enrollment could not be found.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Enrollment,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_current(
        self,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Enrollment]:
        """
        Returns the Enrollment associated with the current User's primary organization.

        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Enrollment]

        :raises GetCurrentEnrollmentPermissionDenied: Could not getCurrent the Enrollment.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Enrollment,
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
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Enrollment]:
        """
        Get the Enrollment with the specified rid.
        :param enrollment_rid: enrollmentRid
        :type enrollment_rid: EnrollmentRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Enrollment]

        :raises EnrollmentNotFound: The given Enrollment could not be found.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=Enrollment,
                request_timeout=request_timeout,
                throwable_errors={
                    "EnrollmentNotFound": admin_errors.EnrollmentNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_current(
        self,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Enrollment]:
        """
        Returns the Enrollment associated with the current User's primary organization.

        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Enrollment]

        :raises GetCurrentEnrollmentPermissionDenied: Could not getCurrent the Enrollment.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=Enrollment,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetCurrentEnrollmentPermissionDenied": admin_errors.GetCurrentEnrollmentPermissionDenied,
                },
            ),
        )
