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

import annotated_types
import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.datasets import models as datasets_models
from foundry.v2.orchestration import errors as orchestration_errors
from foundry.v2.orchestration import models as orchestration_models


class BuildClient:
    """
    The API client for the Build Resource.

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
        self.with_streaming_response = _BuildClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _BuildClientRaw(auth=auth, hostname=hostname, config=config)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def cancel(
        self,
        build_rid: core_models.BuildRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> None:
        """
        Request a cancellation for all unfinished jobs in a build. The build's status will not update immediately. This endpoint is asynchronous and a success response indicates that the cancellation request has been acknowledged and the build is expected to be canceled soon. If the build has already finished or finishes shortly after the request and before the cancellation, the build will not change.

        :param build_rid: The RID of a Build.
        :type build_rid: BuildRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises CancelBuildPermissionDenied: Could not cancel the Build.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/{buildRid}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "buildRid": build_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelBuildPermissionDenied": orchestration_errors.CancelBuildPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        fallback_branches: orchestration_models.FallbackBranches,
        target: typing.Union[
            orchestration_models.BuildTarget, orchestration_models.BuildTargetDict
        ],
        abort_on_failure: typing.Optional[orchestration_models.AbortOnFailure] = None,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        force_build: typing.Optional[orchestration_models.ForceBuild] = None,
        notifications_enabled: typing.Optional[orchestration_models.NotificationsEnabled] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        retry_backoff_duration: typing.Optional[
            typing.Union[
                orchestration_models.RetryBackoffDuration,
                orchestration_models.RetryBackoffDurationDict,
            ]
        ] = None,
        retry_count: typing.Optional[orchestration_models.RetryCount] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> orchestration_models.Build:
        """

        :param fallback_branches:
        :type fallback_branches: FallbackBranches
        :param target: The targets of the schedule.
        :type target: Union[BuildTarget, BuildTargetDict]
        :param abort_on_failure:
        :type abort_on_failure: Optional[AbortOnFailure]
        :param branch_name: The target branch the build should run on.
        :type branch_name: Optional[BranchName]
        :param force_build:
        :type force_build: Optional[ForceBuild]
        :param notifications_enabled: The notification will be sent to the user that has most recently edited the schedule. No notification will be sent if the schedule has `scopeMode` set to `ProjectScope`.
        :type notifications_enabled: Optional[NotificationsEnabled]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param retry_backoff_duration:
        :type retry_backoff_duration: Optional[Union[RetryBackoffDuration, RetryBackoffDurationDict]]
        :param retry_count: The number of retry attempts for failed jobs.
        :type retry_count: Optional[RetryCount]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.Build

        :raises CreateBuildPermissionDenied: Could not create the Build.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/create",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "target": target,
                    "branchName": branch_name,
                    "fallbackBranches": fallback_branches,
                    "forceBuild": force_build,
                    "retryCount": retry_count,
                    "retryBackoffDuration": retry_backoff_duration,
                    "abortOnFailure": abort_on_failure,
                    "notificationsEnabled": notifications_enabled,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "target": typing.Union[
                            orchestration_models.BuildTarget, orchestration_models.BuildTargetDict
                        ],
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "fallbackBranches": orchestration_models.FallbackBranches,
                        "forceBuild": typing.Optional[orchestration_models.ForceBuild],
                        "retryCount": typing.Optional[orchestration_models.RetryCount],
                        "retryBackoffDuration": typing.Optional[
                            typing.Union[
                                orchestration_models.RetryBackoffDuration,
                                orchestration_models.RetryBackoffDurationDict,
                            ]
                        ],
                        "abortOnFailure": typing.Optional[orchestration_models.AbortOnFailure],
                        "notificationsEnabled": typing.Optional[
                            orchestration_models.NotificationsEnabled
                        ],
                    },
                ),
                response_type=orchestration_models.Build,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateBuildPermissionDenied": orchestration_errors.CreateBuildPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        build_rid: core_models.BuildRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> orchestration_models.Build:
        """
        Get the Build with the specified rid.
        :param build_rid: The RID of a Build.
        :type build_rid: BuildRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.Build

        :raises BuildNotFound: The given Build could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/builds/{buildRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "buildRid": build_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=orchestration_models.Build,
                request_timeout=request_timeout,
                throwable_errors={
                    "BuildNotFound": orchestration_errors.BuildNotFound,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[
                typing.Union[
                    orchestration_models.GetBuildsBatchRequestElement,
                    orchestration_models.GetBuildsBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> orchestration_models.GetBuildsBatchResponse:
        """
        Execute multiple get requests on Build.

        The maximum batch size for this endpoint is 100.
        :param body: Body of the request
        :type body: List[Union[GetBuildsBatchRequestElement, GetBuildsBatchRequestElementDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.GetBuildsBatchResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[orchestration_models.GetBuildsBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=100),
                ],
                response_type=orchestration_models.GetBuildsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: typing.Union[
            orchestration_models.SearchBuildsFilter, orchestration_models.SearchBuildsFilterDict
        ],
        order_by: typing.Optional[
            typing.Union[
                orchestration_models.SearchBuildsOrderBy,
                orchestration_models.SearchBuildsOrderByDict,
            ]
        ] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> orchestration_models.SearchBuildsResponse:
        """
        Search for Builds.
        :param where:
        :type where: Union[SearchBuildsFilter, SearchBuildsFilterDict]
        :param order_by:
        :type order_by: Optional[Union[SearchBuildsOrderBy, SearchBuildsOrderByDict]]
        :param page_size: The page size for the search request. If no value is provided, a default of `100` will be used.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: orchestration_models.SearchBuildsResponse

        :raises SearchBuildsPermissionDenied: Could not search the Build.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/search",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "where": where,
                    "orderBy": order_by,
                    "pageToken": page_token,
                    "pageSize": page_size,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Union[
                            orchestration_models.SearchBuildsFilter,
                            orchestration_models.SearchBuildsFilterDict,
                        ],
                        "orderBy": typing.Optional[
                            typing.Union[
                                orchestration_models.SearchBuildsOrderBy,
                                orchestration_models.SearchBuildsOrderByDict,
                            ]
                        ],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                    },
                ),
                response_type=orchestration_models.SearchBuildsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchBuildsPermissionDenied": orchestration_errors.SearchBuildsPermissionDenied,
                },
            ),
        ).decode()


class _BuildClientRaw:
    """
    The API client for the Build Resource.

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
    def cancel(
        self,
        build_rid: core_models.BuildRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[None]:
        """
        Request a cancellation for all unfinished jobs in a build. The build's status will not update immediately. This endpoint is asynchronous and a success response indicates that the cancellation request has been acknowledged and the build is expected to be canceled soon. If the build has already finished or finishes shortly after the request and before the cancellation, the build will not change.

        :param build_rid: The RID of a Build.
        :type build_rid: BuildRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[None]

        :raises CancelBuildPermissionDenied: Could not cancel the Build.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/{buildRid}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "buildRid": build_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelBuildPermissionDenied": orchestration_errors.CancelBuildPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        fallback_branches: orchestration_models.FallbackBranches,
        target: typing.Union[
            orchestration_models.BuildTarget, orchestration_models.BuildTargetDict
        ],
        abort_on_failure: typing.Optional[orchestration_models.AbortOnFailure] = None,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        force_build: typing.Optional[orchestration_models.ForceBuild] = None,
        notifications_enabled: typing.Optional[orchestration_models.NotificationsEnabled] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        retry_backoff_duration: typing.Optional[
            typing.Union[
                orchestration_models.RetryBackoffDuration,
                orchestration_models.RetryBackoffDurationDict,
            ]
        ] = None,
        retry_count: typing.Optional[orchestration_models.RetryCount] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[orchestration_models.Build]:
        """

        :param fallback_branches:
        :type fallback_branches: FallbackBranches
        :param target: The targets of the schedule.
        :type target: Union[BuildTarget, BuildTargetDict]
        :param abort_on_failure:
        :type abort_on_failure: Optional[AbortOnFailure]
        :param branch_name: The target branch the build should run on.
        :type branch_name: Optional[BranchName]
        :param force_build:
        :type force_build: Optional[ForceBuild]
        :param notifications_enabled: The notification will be sent to the user that has most recently edited the schedule. No notification will be sent if the schedule has `scopeMode` set to `ProjectScope`.
        :type notifications_enabled: Optional[NotificationsEnabled]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param retry_backoff_duration:
        :type retry_backoff_duration: Optional[Union[RetryBackoffDuration, RetryBackoffDurationDict]]
        :param retry_count: The number of retry attempts for failed jobs.
        :type retry_count: Optional[RetryCount]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[orchestration_models.Build]

        :raises CreateBuildPermissionDenied: Could not create the Build.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/create",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "target": target,
                    "branchName": branch_name,
                    "fallbackBranches": fallback_branches,
                    "forceBuild": force_build,
                    "retryCount": retry_count,
                    "retryBackoffDuration": retry_backoff_duration,
                    "abortOnFailure": abort_on_failure,
                    "notificationsEnabled": notifications_enabled,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "target": typing.Union[
                            orchestration_models.BuildTarget, orchestration_models.BuildTargetDict
                        ],
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "fallbackBranches": orchestration_models.FallbackBranches,
                        "forceBuild": typing.Optional[orchestration_models.ForceBuild],
                        "retryCount": typing.Optional[orchestration_models.RetryCount],
                        "retryBackoffDuration": typing.Optional[
                            typing.Union[
                                orchestration_models.RetryBackoffDuration,
                                orchestration_models.RetryBackoffDurationDict,
                            ]
                        ],
                        "abortOnFailure": typing.Optional[orchestration_models.AbortOnFailure],
                        "notificationsEnabled": typing.Optional[
                            orchestration_models.NotificationsEnabled
                        ],
                    },
                ),
                response_type=orchestration_models.Build,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateBuildPermissionDenied": orchestration_errors.CreateBuildPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        build_rid: core_models.BuildRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[orchestration_models.Build]:
        """
        Get the Build with the specified rid.
        :param build_rid: The RID of a Build.
        :type build_rid: BuildRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[orchestration_models.Build]

        :raises BuildNotFound: The given Build could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/builds/{buildRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "buildRid": build_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=orchestration_models.Build,
                request_timeout=request_timeout,
                throwable_errors={
                    "BuildNotFound": orchestration_errors.BuildNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[
                typing.Union[
                    orchestration_models.GetBuildsBatchRequestElement,
                    orchestration_models.GetBuildsBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[orchestration_models.GetBuildsBatchResponse]:
        """
        Execute multiple get requests on Build.

        The maximum batch size for this endpoint is 100.
        :param body: Body of the request
        :type body: List[Union[GetBuildsBatchRequestElement, GetBuildsBatchRequestElementDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[orchestration_models.GetBuildsBatchResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[orchestration_models.GetBuildsBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=100),
                ],
                response_type=orchestration_models.GetBuildsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: typing.Union[
            orchestration_models.SearchBuildsFilter, orchestration_models.SearchBuildsFilterDict
        ],
        order_by: typing.Optional[
            typing.Union[
                orchestration_models.SearchBuildsOrderBy,
                orchestration_models.SearchBuildsOrderByDict,
            ]
        ] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[orchestration_models.SearchBuildsResponse]:
        """
        Search for Builds.
        :param where:
        :type where: Union[SearchBuildsFilter, SearchBuildsFilterDict]
        :param order_by:
        :type order_by: Optional[Union[SearchBuildsOrderBy, SearchBuildsOrderByDict]]
        :param page_size: The page size for the search request. If no value is provided, a default of `100` will be used.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[orchestration_models.SearchBuildsResponse]

        :raises SearchBuildsPermissionDenied: Could not search the Build.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/search",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "where": where,
                    "orderBy": order_by,
                    "pageToken": page_token,
                    "pageSize": page_size,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Union[
                            orchestration_models.SearchBuildsFilter,
                            orchestration_models.SearchBuildsFilterDict,
                        ],
                        "orderBy": typing.Optional[
                            typing.Union[
                                orchestration_models.SearchBuildsOrderBy,
                                orchestration_models.SearchBuildsOrderByDict,
                            ]
                        ],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                    },
                ),
                response_type=orchestration_models.SearchBuildsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchBuildsPermissionDenied": orchestration_errors.SearchBuildsPermissionDenied,
                },
            ),
        )


class _BuildClientStreaming:
    """
    The API client for the Build Resource.

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
    def cancel(
        self,
        build_rid: core_models.BuildRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[None]:
        """
        Request a cancellation for all unfinished jobs in a build. The build's status will not update immediately. This endpoint is asynchronous and a success response indicates that the cancellation request has been acknowledged and the build is expected to be canceled soon. If the build has already finished or finishes shortly after the request and before the cancellation, the build will not change.

        :param build_rid: The RID of a Build.
        :type build_rid: BuildRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[None]

        :raises CancelBuildPermissionDenied: Could not cancel the Build.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/{buildRid}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "buildRid": build_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelBuildPermissionDenied": orchestration_errors.CancelBuildPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        fallback_branches: orchestration_models.FallbackBranches,
        target: typing.Union[
            orchestration_models.BuildTarget, orchestration_models.BuildTargetDict
        ],
        abort_on_failure: typing.Optional[orchestration_models.AbortOnFailure] = None,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        force_build: typing.Optional[orchestration_models.ForceBuild] = None,
        notifications_enabled: typing.Optional[orchestration_models.NotificationsEnabled] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        retry_backoff_duration: typing.Optional[
            typing.Union[
                orchestration_models.RetryBackoffDuration,
                orchestration_models.RetryBackoffDurationDict,
            ]
        ] = None,
        retry_count: typing.Optional[orchestration_models.RetryCount] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[orchestration_models.Build]:
        """

        :param fallback_branches:
        :type fallback_branches: FallbackBranches
        :param target: The targets of the schedule.
        :type target: Union[BuildTarget, BuildTargetDict]
        :param abort_on_failure:
        :type abort_on_failure: Optional[AbortOnFailure]
        :param branch_name: The target branch the build should run on.
        :type branch_name: Optional[BranchName]
        :param force_build:
        :type force_build: Optional[ForceBuild]
        :param notifications_enabled: The notification will be sent to the user that has most recently edited the schedule. No notification will be sent if the schedule has `scopeMode` set to `ProjectScope`.
        :type notifications_enabled: Optional[NotificationsEnabled]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param retry_backoff_duration:
        :type retry_backoff_duration: Optional[Union[RetryBackoffDuration, RetryBackoffDurationDict]]
        :param retry_count: The number of retry attempts for failed jobs.
        :type retry_count: Optional[RetryCount]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[orchestration_models.Build]

        :raises CreateBuildPermissionDenied: Could not create the Build.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/create",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "target": target,
                    "branchName": branch_name,
                    "fallbackBranches": fallback_branches,
                    "forceBuild": force_build,
                    "retryCount": retry_count,
                    "retryBackoffDuration": retry_backoff_duration,
                    "abortOnFailure": abort_on_failure,
                    "notificationsEnabled": notifications_enabled,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "target": typing.Union[
                            orchestration_models.BuildTarget, orchestration_models.BuildTargetDict
                        ],
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "fallbackBranches": orchestration_models.FallbackBranches,
                        "forceBuild": typing.Optional[orchestration_models.ForceBuild],
                        "retryCount": typing.Optional[orchestration_models.RetryCount],
                        "retryBackoffDuration": typing.Optional[
                            typing.Union[
                                orchestration_models.RetryBackoffDuration,
                                orchestration_models.RetryBackoffDurationDict,
                            ]
                        ],
                        "abortOnFailure": typing.Optional[orchestration_models.AbortOnFailure],
                        "notificationsEnabled": typing.Optional[
                            orchestration_models.NotificationsEnabled
                        ],
                    },
                ),
                response_type=orchestration_models.Build,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateBuildPermissionDenied": orchestration_errors.CreateBuildPermissionDenied,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        build_rid: core_models.BuildRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[orchestration_models.Build]:
        """
        Get the Build with the specified rid.
        :param build_rid: The RID of a Build.
        :type build_rid: BuildRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[orchestration_models.Build]

        :raises BuildNotFound: The given Build could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/orchestration/builds/{buildRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "buildRid": build_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=orchestration_models.Build,
                request_timeout=request_timeout,
                throwable_errors={
                    "BuildNotFound": orchestration_errors.BuildNotFound,
                },
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[
                typing.Union[
                    orchestration_models.GetBuildsBatchRequestElement,
                    orchestration_models.GetBuildsBatchRequestElementDict,
                ]
            ],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[orchestration_models.GetBuildsBatchResponse]:
        """
        Execute multiple get requests on Build.

        The maximum batch size for this endpoint is 100.
        :param body: Body of the request
        :type body: List[Union[GetBuildsBatchRequestElement, GetBuildsBatchRequestElementDict]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[orchestration_models.GetBuildsBatchResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/getBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                body_type=typing_extensions.Annotated[
                    typing.List[orchestration_models.GetBuildsBatchRequestElementDict],
                    annotated_types.Len(min_length=1, max_length=100),
                ],
                response_type=orchestration_models.GetBuildsBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        where: typing.Union[
            orchestration_models.SearchBuildsFilter, orchestration_models.SearchBuildsFilterDict
        ],
        order_by: typing.Optional[
            typing.Union[
                orchestration_models.SearchBuildsOrderBy,
                orchestration_models.SearchBuildsOrderByDict,
            ]
        ] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[orchestration_models.SearchBuildsResponse]:
        """
        Search for Builds.
        :param where:
        :type where: Union[SearchBuildsFilter, SearchBuildsFilterDict]
        :param order_by:
        :type order_by: Optional[Union[SearchBuildsOrderBy, SearchBuildsOrderByDict]]
        :param page_size: The page size for the search request. If no value is provided, a default of `100` will be used.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[orchestration_models.SearchBuildsResponse]

        :raises SearchBuildsPermissionDenied: Could not search the Build.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/orchestration/builds/search",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "where": where,
                    "orderBy": order_by,
                    "pageToken": page_token,
                    "pageSize": page_size,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Union[
                            orchestration_models.SearchBuildsFilter,
                            orchestration_models.SearchBuildsFilterDict,
                        ],
                        "orderBy": typing.Optional[
                            typing.Union[
                                orchestration_models.SearchBuildsOrderBy,
                                orchestration_models.SearchBuildsOrderByDict,
                            ]
                        ],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "pageSize": typing.Optional[core_models.PageSize],
                    },
                ),
                response_type=orchestration_models.SearchBuildsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "SearchBuildsPermissionDenied": orchestration_errors.SearchBuildsPermissionDenied,
                },
            ),
        )
