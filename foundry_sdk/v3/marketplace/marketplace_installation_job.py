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
from foundry_sdk.v3.core import models as core_models
from foundry_sdk.v3.marketplace import errors as marketplace_errors
from foundry_sdk.v3.marketplace import models as marketplace_models


class MarketplaceInstallationJobClient:
    """
    The API client for the MarketplaceInstallationJob Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _MarketplaceInstallationJobClientStreaming(self)
        self.with_raw_response = _MarketplaceInstallationJobClientRaw(self)

    @cached_property
    def Details(self):
        from foundry_sdk.v3.marketplace.marketplace_installation_job_details import (
            MarketplaceInstallationJobDetailsClient,
        )  # NOQA

        return MarketplaceInstallationJobDetailsClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def abort(
        self,
        marketplace_installation_job_rid: marketplace_models.MarketplaceInstallationJobRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Abort an installation job draft or request cancellation of a submitted installation job. This operation is
        idempotent while the job remains available. Poll the job with `get` after aborting: submitted jobs may report
        `ABORTING` before reaching `ABORTED`. Aborting a job that has already finished leaves its terminal status
        unchanged.

        A submitted job may already have created resources. Cancelling it can leave the installation in an
        inconsistent state. To recover to a consistent state, attempt a new job to the same target version.

        An aborted draft remains queryable only until automatic cleanup.

        Required scopes: [api:v3:marketplace-installation-job:write:abort]

        :param marketplace_installation_job_rid:
        :type marketplace_installation_job_rid: MarketplaceInstallationJobRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AbortInstallationJobPermissionDenied: The installation job is visible to the request token, but the request token does not have permission to abort it.
        :raises MarketplaceInstallationJobNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/marketplaceInstallationJobs/{marketplaceInstallationJobRid}/abort",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "marketplaceInstallationJobRid": marketplace_installation_job_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AbortInstallationJobPermissionDenied": marketplace_errors.AbortInstallationJobPermissionDenied,
                    "MarketplaceInstallationJobNotFound": marketplace_errors.MarketplaceInstallationJobNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        installations: typing.List[marketplace_models.InstallationJobTarget],
        recommendations: typing.List[marketplace_models.RecommendationStrategy],
        preview: typing.Optional[core_models.PreviewMode] = None,
        submission_mode: typing.Optional[marketplace_models.InstallationJobSubmissionMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> marketplace_models.MarketplaceInstallationJob:
        """
        Create a job to upgrade existing installations to their target versions.

        The operation returns before preparation and validation complete. Poll the job's status to track progress.

        Specify 1 to 10 distinct installations, with at most one installation per product. Targets must share a
        namespace and marketplace and have at most one resulting ontology after applying overrides.

        For each target, `values` and `explicitlyUnset` replace all previously provided values and explicit unsets.

        Inputs omitted from both fields may be fulfilled by defaults, automatic mapping, or recommendations. Use
        `discoverInputs` to inspect available sources.

        This operation is not idempotent. Repeating it may create another draft or return a conflict.

        Required scopes: [api:v3:marketplace-installation-job:write:create]

        :param installations: Existing installations to upgrade to their target versions, along with their input mappings.
        :type installations: List[InstallationJobTarget]
        :param recommendations: Strategies for selecting other installations whose outputs can fulfill the targets' inputs. Targets in this request may still supply inputs to one another, independent of recommendation strategy.
        :type recommendations: List[RecommendationStrategy]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param submission_mode:
        :type submission_mode: Optional[InstallationJobSubmissionMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: marketplace_models.MarketplaceInstallationJob

        :raises AmbiguousInstallationRecommendation: A namespace recommendation strategy matches multiple installations of the same linked product. Narrow its suffix filter or use explicit recommendations. Overlapping recommendation inputs or sources are reported separately as `InstallationError` entries in the discovery response.
        :raises ConflictingInstallationInputIntent: An input name occurs more than once in `explicitlyUnset` or occurs in both `values` and `explicitlyUnset` for the same installation.
        :raises ConflictingInstallationJob: An installation targeted for submission already has a running job. Draft mode may still prepare a draft.
        :raises ConflictingInstallationRecommendation: A recommendation supplies a product that is also included in the requested targets. Remove that recommendation.
        :raises CreateInstallationJobPermissionDenied: The request token cannot prepare or submit a job for one or more target installations or dependencies.
        :raises DuplicateInstallationJobInstallations: An installation occurs more than once in the target list.
        :raises DuplicateInstallationJobProducts: More than one target installation uses the same product.
        :raises InstallationDraftAlreadyExists: The caller already has a preparing or idle draft for a target installation. Complete or abort the existing draft before preparing another job or discovering inputs for that installation.
        :raises InstallationInputApiNamesNotEnabled: One or more installations have product inputs without API names. Enable input API name generation for those products before interacting with them.
        :raises InstallationInputNotFound: An input API name is not present in the selected product version.
        :raises InstallationJobMarketplaceConstraintViolated: The target products must belong to a single marketplace.
        :raises InstallationJobNamespaceConstraintViolated: The target installations must belong to a single namespace.
        :raises InstallationJobOntologyConstraintViolated: The target installations must have at most one resulting ontology after applying location overrides.
        :raises InstallationTargetVersionNotFound: The requested target version could not be found within the installation product and marketplace.
        :raises InstallationUninstallStarted: Uninstall has begun for the target installation. Create a new installation to install the product again.
        :raises InvalidInstallationInput: An input value could not be converted for the selected product version. The error reason does not contain the supplied value.
        :raises InvalidInstallationTargetVersion: The target semantic version must be an exact major.minor.patch version with non-negative integer components and no leading zeros. Each component must be at most 2⁵³ - 2 (9,007,199,254,740,990). Version ranges, wildcards, prerelease identifiers, and build metadata are not supported.
        :raises MarketplaceInstallationNotFound:
        :raises MaxInstallationJobInstallationsCountExceeded: The number of installation targets exceeds the maximum supported by this operation.
        :raises MissingInstallationInputParentValue: A child input with a value requires its parent to have a value in `inputs.values` for the same installation.
        :raises MissingInstallationJobInstallations: At least one installation target must be supplied.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/marketplaceInstallationJobs",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=marketplace_models.CreateMarketplaceInstallationJobRequest(
                    installations=installations,
                    recommendations=recommendations,
                    submission_mode=submission_mode,
                ),
                response_type=marketplace_models.MarketplaceInstallationJob,
                request_timeout=request_timeout,
                throwable_errors={
                    "AmbiguousInstallationRecommendation": marketplace_errors.AmbiguousInstallationRecommendation,
                    "ConflictingInstallationInputIntent": marketplace_errors.ConflictingInstallationInputIntent,
                    "ConflictingInstallationJob": marketplace_errors.ConflictingInstallationJob,
                    "ConflictingInstallationRecommendation": marketplace_errors.ConflictingInstallationRecommendation,
                    "CreateInstallationJobPermissionDenied": marketplace_errors.CreateInstallationJobPermissionDenied,
                    "DuplicateInstallationJobInstallations": marketplace_errors.DuplicateInstallationJobInstallations,
                    "DuplicateInstallationJobProducts": marketplace_errors.DuplicateInstallationJobProducts,
                    "InstallationDraftAlreadyExists": marketplace_errors.InstallationDraftAlreadyExists,
                    "InstallationInputApiNamesNotEnabled": marketplace_errors.InstallationInputApiNamesNotEnabled,
                    "InstallationInputNotFound": marketplace_errors.InstallationInputNotFound,
                    "InstallationJobMarketplaceConstraintViolated": marketplace_errors.InstallationJobMarketplaceConstraintViolated,
                    "InstallationJobNamespaceConstraintViolated": marketplace_errors.InstallationJobNamespaceConstraintViolated,
                    "InstallationJobOntologyConstraintViolated": marketplace_errors.InstallationJobOntologyConstraintViolated,
                    "InstallationTargetVersionNotFound": marketplace_errors.InstallationTargetVersionNotFound,
                    "InstallationUninstallStarted": marketplace_errors.InstallationUninstallStarted,
                    "InvalidInstallationInput": marketplace_errors.InvalidInstallationInput,
                    "InvalidInstallationTargetVersion": marketplace_errors.InvalidInstallationTargetVersion,
                    "MarketplaceInstallationNotFound": marketplace_errors.MarketplaceInstallationNotFound,
                    "MaxInstallationJobInstallationsCountExceeded": marketplace_errors.MaxInstallationJobInstallationsCountExceeded,
                    "MissingInstallationInputParentValue": marketplace_errors.MissingInstallationInputParentValue,
                    "MissingInstallationJobInstallations": marketplace_errors.MissingInstallationJobInstallations,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def discover_inputs(
        self,
        *,
        installations: typing.List[marketplace_models.InstallationTarget],
        recommendations: typing.List[marketplace_models.RecommendationStrategy],
        preview: typing.Optional[core_models.PreviewMode] = None,
        source_filter: typing.Optional[marketplace_models.SourceFilter] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> marketplace_models.DiscoverInstallationJobInputsResponse:
        """
        Discover required and optional inputs for existing installations and their proposed target versions.

        Resolves input requirements and available sources using the requested target versions, location overrides,
        and recommendation strategies.

        The request token must have permission to edit each target. Every input in the target product versions must
        have an API name.

        Required scopes: [api:v3:marketplace-installation-job:read:discover-inputs]

        :param installations: Between 1 and 10 distinct installations, with at most one installation per product. Targets must share a namespace and marketplace and have at most one resulting ontology after applying overrides.
        :type installations: List[InstallationTarget]
        :param recommendations: An empty list disables recommendations from installations outside the requested targets. Targets in this request may still supply inputs to one another.
        :type recommendations: List[RecommendationStrategy]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param source_filter: When supplied, excludes an input if any of its available sources appears in `excludedSources`. If omitted, returns only inputs whose sole available source is `MANUAL`. Inputs with no available source are always omitted.
        :type source_filter: Optional[SourceFilter]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: marketplace_models.DiscoverInstallationJobInputsResponse

        :raises AmbiguousInstallationRecommendation: A namespace recommendation strategy matches multiple installations of the same linked product. Narrow its suffix filter or use explicit recommendations. Overlapping recommendation inputs or sources are reported separately as `InstallationError` entries in the discovery response.
        :raises ConflictingInstallationRecommendation: A recommendation supplies a product that is also included in the requested targets. Remove that recommendation.
        :raises DiscoverInstallationJobInputsFailed: Marketplace could not complete input discovery.
        :raises DiscoverInstallationJobInputsPermissionDenied: The request token does not have permission to edit one or more target installations and cannot discover their inputs.
        :raises DuplicateInstallationJobInstallations: An installation occurs more than once in the target list.
        :raises DuplicateInstallationJobProducts: More than one target installation uses the same product.
        :raises InstallationDraftAlreadyExists: The caller already has a preparing or idle draft for a target installation. Complete or abort the existing draft before preparing another job or discovering inputs for that installation.
        :raises InstallationInputApiNamesNotEnabled: One or more installations have product inputs without API names. Enable input API name generation for those products before interacting with them.
        :raises InstallationJobMarketplaceConstraintViolated: The target products must belong to a single marketplace.
        :raises InstallationJobNamespaceConstraintViolated: The target installations must belong to a single namespace.
        :raises InstallationJobOntologyConstraintViolated: The target installations must have at most one resulting ontology after applying location overrides.
        :raises InstallationTargetVersionNotFound: The requested target version could not be found within the installation product and marketplace.
        :raises InstallationUninstallStarted: Uninstall has begun for the target installation. Create a new installation to install the product again.
        :raises InvalidInstallationTargetVersion: The target semantic version must be an exact major.minor.patch version with non-negative integer components and no leading zeros. Each component must be at most 2⁵³ - 2 (9,007,199,254,740,990). Version ranges, wildcards, prerelease identifiers, and build metadata are not supported.
        :raises MarketplaceInstallationNotFound:
        :raises MaxInstallationJobInstallationsCountExceeded: The number of installation targets exceeds the maximum supported by this operation.
        :raises MissingInstallationJobInstallations: At least one installation target must be supplied.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/marketplaceInstallationJobs/discoverInputs",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=marketplace_models.DiscoverInstallationJobInputsRequest(
                    installations=installations,
                    recommendations=recommendations,
                    source_filter=source_filter,
                ),
                response_type=marketplace_models.DiscoverInstallationJobInputsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AmbiguousInstallationRecommendation": marketplace_errors.AmbiguousInstallationRecommendation,
                    "ConflictingInstallationRecommendation": marketplace_errors.ConflictingInstallationRecommendation,
                    "DiscoverInstallationJobInputsFailed": marketplace_errors.DiscoverInstallationJobInputsFailed,
                    "DiscoverInstallationJobInputsPermissionDenied": marketplace_errors.DiscoverInstallationJobInputsPermissionDenied,
                    "DuplicateInstallationJobInstallations": marketplace_errors.DuplicateInstallationJobInstallations,
                    "DuplicateInstallationJobProducts": marketplace_errors.DuplicateInstallationJobProducts,
                    "InstallationDraftAlreadyExists": marketplace_errors.InstallationDraftAlreadyExists,
                    "InstallationInputApiNamesNotEnabled": marketplace_errors.InstallationInputApiNamesNotEnabled,
                    "InstallationJobMarketplaceConstraintViolated": marketplace_errors.InstallationJobMarketplaceConstraintViolated,
                    "InstallationJobNamespaceConstraintViolated": marketplace_errors.InstallationJobNamespaceConstraintViolated,
                    "InstallationJobOntologyConstraintViolated": marketplace_errors.InstallationJobOntologyConstraintViolated,
                    "InstallationTargetVersionNotFound": marketplace_errors.InstallationTargetVersionNotFound,
                    "InstallationUninstallStarted": marketplace_errors.InstallationUninstallStarted,
                    "InvalidInstallationTargetVersion": marketplace_errors.InvalidInstallationTargetVersion,
                    "MarketplaceInstallationNotFound": marketplace_errors.MarketplaceInstallationNotFound,
                    "MaxInstallationJobInstallationsCountExceeded": marketplace_errors.MaxInstallationJobInstallationsCountExceeded,
                    "MissingInstallationJobInstallations": marketplace_errors.MissingInstallationJobInstallations,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marketplace_installation_job_rid: marketplace_models.MarketplaceInstallationJobRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> marketplace_models.MarketplaceInstallationJob:
        """
        Get the current status of an installation job through draft preparation and execution.

        The request token must have permission to view the draft or submitted job. Missing or inaccessible jobs return
        `MarketplaceInstallationJobNotFound`. A failed or aborted job still returns HTTP 200 with its current status.

        Required scopes: [api:v3:marketplace-installation-job:read:get]

        :param marketplace_installation_job_rid:
        :type marketplace_installation_job_rid: MarketplaceInstallationJobRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: marketplace_models.MarketplaceInstallationJob

        :raises MarketplaceInstallationJobNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/marketplaceInstallationJobs/{marketplaceInstallationJobRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "marketplaceInstallationJobRid": marketplace_installation_job_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=marketplace_models.MarketplaceInstallationJob,
                request_timeout=request_timeout,
                throwable_errors={
                    "MarketplaceInstallationJobNotFound": marketplace_errors.MarketplaceInstallationJobNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MarketplaceInstallationJobClientRaw:
    def __init__(self, client: MarketplaceInstallationJobClient) -> None:
        def abort(_: None): ...
        def create(_: marketplace_models.MarketplaceInstallationJob): ...
        def discover_inputs(_: marketplace_models.DiscoverInstallationJobInputsResponse): ...
        def get(_: marketplace_models.MarketplaceInstallationJob): ...

        self.abort = core.with_raw_response(abort, client.abort)
        self.create = core.with_raw_response(create, client.create)
        self.discover_inputs = core.with_raw_response(discover_inputs, client.discover_inputs)
        self.get = core.with_raw_response(get, client.get)


class _MarketplaceInstallationJobClientStreaming:
    def __init__(self, client: MarketplaceInstallationJobClient) -> None:
        def create(_: marketplace_models.MarketplaceInstallationJob): ...
        def discover_inputs(_: marketplace_models.DiscoverInstallationJobInputsResponse): ...
        def get(_: marketplace_models.MarketplaceInstallationJob): ...

        self.create = core.with_streaming_response(create, client.create)
        self.discover_inputs = core.with_streaming_response(discover_inputs, client.discover_inputs)
        self.get = core.with_streaming_response(get, client.get)


class AsyncMarketplaceInstallationJobClient:
    """
    The API client for the MarketplaceInstallationJob Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncMarketplaceInstallationJobClientStreaming(self)
        self.with_raw_response = _AsyncMarketplaceInstallationJobClientRaw(self)

    @cached_property
    def Details(self):
        from foundry_sdk.v3.marketplace.marketplace_installation_job_details import (
            AsyncMarketplaceInstallationJobDetailsClient,
        )  # NOQA

        return AsyncMarketplaceInstallationJobDetailsClient(
            auth=self._auth,
            hostname=self._hostname_supplier,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def abort(
        self,
        marketplace_installation_job_rid: marketplace_models.MarketplaceInstallationJobRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Abort an installation job draft or request cancellation of a submitted installation job. This operation is
        idempotent while the job remains available. Poll the job with `get` after aborting: submitted jobs may report
        `ABORTING` before reaching `ABORTED`. Aborting a job that has already finished leaves its terminal status
        unchanged.

        A submitted job may already have created resources. Cancelling it can leave the installation in an
        inconsistent state. To recover to a consistent state, attempt a new job to the same target version.

        An aborted draft remains queryable only until automatic cleanup.

        Required scopes: [api:v3:marketplace-installation-job:write:abort]

        :param marketplace_installation_job_rid:
        :type marketplace_installation_job_rid: MarketplaceInstallationJobRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises AbortInstallationJobPermissionDenied: The installation job is visible to the request token, but the request token does not have permission to abort it.
        :raises MarketplaceInstallationJobNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/marketplaceInstallationJobs/{marketplaceInstallationJobRid}/abort",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "marketplaceInstallationJobRid": marketplace_installation_job_rid,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AbortInstallationJobPermissionDenied": marketplace_errors.AbortInstallationJobPermissionDenied,
                    "MarketplaceInstallationJobNotFound": marketplace_errors.MarketplaceInstallationJobNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        installations: typing.List[marketplace_models.InstallationJobTarget],
        recommendations: typing.List[marketplace_models.RecommendationStrategy],
        preview: typing.Optional[core_models.PreviewMode] = None,
        submission_mode: typing.Optional[marketplace_models.InstallationJobSubmissionMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[marketplace_models.MarketplaceInstallationJob]:
        """
        Create a job to upgrade existing installations to their target versions.

        The operation returns before preparation and validation complete. Poll the job's status to track progress.

        Specify 1 to 10 distinct installations, with at most one installation per product. Targets must share a
        namespace and marketplace and have at most one resulting ontology after applying overrides.

        For each target, `values` and `explicitlyUnset` replace all previously provided values and explicit unsets.

        Inputs omitted from both fields may be fulfilled by defaults, automatic mapping, or recommendations. Use
        `discoverInputs` to inspect available sources.

        This operation is not idempotent. Repeating it may create another draft or return a conflict.

        Required scopes: [api:v3:marketplace-installation-job:write:create]

        :param installations: Existing installations to upgrade to their target versions, along with their input mappings.
        :type installations: List[InstallationJobTarget]
        :param recommendations: Strategies for selecting other installations whose outputs can fulfill the targets' inputs. Targets in this request may still supply inputs to one another, independent of recommendation strategy.
        :type recommendations: List[RecommendationStrategy]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param submission_mode:
        :type submission_mode: Optional[InstallationJobSubmissionMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[marketplace_models.MarketplaceInstallationJob]

        :raises AmbiguousInstallationRecommendation: A namespace recommendation strategy matches multiple installations of the same linked product. Narrow its suffix filter or use explicit recommendations. Overlapping recommendation inputs or sources are reported separately as `InstallationError` entries in the discovery response.
        :raises ConflictingInstallationInputIntent: An input name occurs more than once in `explicitlyUnset` or occurs in both `values` and `explicitlyUnset` for the same installation.
        :raises ConflictingInstallationJob: An installation targeted for submission already has a running job. Draft mode may still prepare a draft.
        :raises ConflictingInstallationRecommendation: A recommendation supplies a product that is also included in the requested targets. Remove that recommendation.
        :raises CreateInstallationJobPermissionDenied: The request token cannot prepare or submit a job for one or more target installations or dependencies.
        :raises DuplicateInstallationJobInstallations: An installation occurs more than once in the target list.
        :raises DuplicateInstallationJobProducts: More than one target installation uses the same product.
        :raises InstallationDraftAlreadyExists: The caller already has a preparing or idle draft for a target installation. Complete or abort the existing draft before preparing another job or discovering inputs for that installation.
        :raises InstallationInputApiNamesNotEnabled: One or more installations have product inputs without API names. Enable input API name generation for those products before interacting with them.
        :raises InstallationInputNotFound: An input API name is not present in the selected product version.
        :raises InstallationJobMarketplaceConstraintViolated: The target products must belong to a single marketplace.
        :raises InstallationJobNamespaceConstraintViolated: The target installations must belong to a single namespace.
        :raises InstallationJobOntologyConstraintViolated: The target installations must have at most one resulting ontology after applying location overrides.
        :raises InstallationTargetVersionNotFound: The requested target version could not be found within the installation product and marketplace.
        :raises InstallationUninstallStarted: Uninstall has begun for the target installation. Create a new installation to install the product again.
        :raises InvalidInstallationInput: An input value could not be converted for the selected product version. The error reason does not contain the supplied value.
        :raises InvalidInstallationTargetVersion: The target semantic version must be an exact major.minor.patch version with non-negative integer components and no leading zeros. Each component must be at most 2⁵³ - 2 (9,007,199,254,740,990). Version ranges, wildcards, prerelease identifiers, and build metadata are not supported.
        :raises MarketplaceInstallationNotFound:
        :raises MaxInstallationJobInstallationsCountExceeded: The number of installation targets exceeds the maximum supported by this operation.
        :raises MissingInstallationInputParentValue: A child input with a value requires its parent to have a value in `inputs.values` for the same installation.
        :raises MissingInstallationJobInstallations: At least one installation target must be supplied.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/marketplaceInstallationJobs",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=marketplace_models.CreateMarketplaceInstallationJobRequest(
                    installations=installations,
                    recommendations=recommendations,
                    submission_mode=submission_mode,
                ),
                response_type=marketplace_models.MarketplaceInstallationJob,
                request_timeout=request_timeout,
                throwable_errors={
                    "AmbiguousInstallationRecommendation": marketplace_errors.AmbiguousInstallationRecommendation,
                    "ConflictingInstallationInputIntent": marketplace_errors.ConflictingInstallationInputIntent,
                    "ConflictingInstallationJob": marketplace_errors.ConflictingInstallationJob,
                    "ConflictingInstallationRecommendation": marketplace_errors.ConflictingInstallationRecommendation,
                    "CreateInstallationJobPermissionDenied": marketplace_errors.CreateInstallationJobPermissionDenied,
                    "DuplicateInstallationJobInstallations": marketplace_errors.DuplicateInstallationJobInstallations,
                    "DuplicateInstallationJobProducts": marketplace_errors.DuplicateInstallationJobProducts,
                    "InstallationDraftAlreadyExists": marketplace_errors.InstallationDraftAlreadyExists,
                    "InstallationInputApiNamesNotEnabled": marketplace_errors.InstallationInputApiNamesNotEnabled,
                    "InstallationInputNotFound": marketplace_errors.InstallationInputNotFound,
                    "InstallationJobMarketplaceConstraintViolated": marketplace_errors.InstallationJobMarketplaceConstraintViolated,
                    "InstallationJobNamespaceConstraintViolated": marketplace_errors.InstallationJobNamespaceConstraintViolated,
                    "InstallationJobOntologyConstraintViolated": marketplace_errors.InstallationJobOntologyConstraintViolated,
                    "InstallationTargetVersionNotFound": marketplace_errors.InstallationTargetVersionNotFound,
                    "InstallationUninstallStarted": marketplace_errors.InstallationUninstallStarted,
                    "InvalidInstallationInput": marketplace_errors.InvalidInstallationInput,
                    "InvalidInstallationTargetVersion": marketplace_errors.InvalidInstallationTargetVersion,
                    "MarketplaceInstallationNotFound": marketplace_errors.MarketplaceInstallationNotFound,
                    "MaxInstallationJobInstallationsCountExceeded": marketplace_errors.MaxInstallationJobInstallationsCountExceeded,
                    "MissingInstallationInputParentValue": marketplace_errors.MissingInstallationInputParentValue,
                    "MissingInstallationJobInstallations": marketplace_errors.MissingInstallationJobInstallations,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def discover_inputs(
        self,
        *,
        installations: typing.List[marketplace_models.InstallationTarget],
        recommendations: typing.List[marketplace_models.RecommendationStrategy],
        preview: typing.Optional[core_models.PreviewMode] = None,
        source_filter: typing.Optional[marketplace_models.SourceFilter] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[marketplace_models.DiscoverInstallationJobInputsResponse]:
        """
        Discover required and optional inputs for existing installations and their proposed target versions.

        Resolves input requirements and available sources using the requested target versions, location overrides,
        and recommendation strategies.

        The request token must have permission to edit each target. Every input in the target product versions must
        have an API name.

        Required scopes: [api:v3:marketplace-installation-job:read:discover-inputs]

        :param installations: Between 1 and 10 distinct installations, with at most one installation per product. Targets must share a namespace and marketplace and have at most one resulting ontology after applying overrides.
        :type installations: List[InstallationTarget]
        :param recommendations: An empty list disables recommendations from installations outside the requested targets. Targets in this request may still supply inputs to one another.
        :type recommendations: List[RecommendationStrategy]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param source_filter: When supplied, excludes an input if any of its available sources appears in `excludedSources`. If omitted, returns only inputs whose sole available source is `MANUAL`. Inputs with no available source are always omitted.
        :type source_filter: Optional[SourceFilter]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[marketplace_models.DiscoverInstallationJobInputsResponse]

        :raises AmbiguousInstallationRecommendation: A namespace recommendation strategy matches multiple installations of the same linked product. Narrow its suffix filter or use explicit recommendations. Overlapping recommendation inputs or sources are reported separately as `InstallationError` entries in the discovery response.
        :raises ConflictingInstallationRecommendation: A recommendation supplies a product that is also included in the requested targets. Remove that recommendation.
        :raises DiscoverInstallationJobInputsFailed: Marketplace could not complete input discovery.
        :raises DiscoverInstallationJobInputsPermissionDenied: The request token does not have permission to edit one or more target installations and cannot discover their inputs.
        :raises DuplicateInstallationJobInstallations: An installation occurs more than once in the target list.
        :raises DuplicateInstallationJobProducts: More than one target installation uses the same product.
        :raises InstallationDraftAlreadyExists: The caller already has a preparing or idle draft for a target installation. Complete or abort the existing draft before preparing another job or discovering inputs for that installation.
        :raises InstallationInputApiNamesNotEnabled: One or more installations have product inputs without API names. Enable input API name generation for those products before interacting with them.
        :raises InstallationJobMarketplaceConstraintViolated: The target products must belong to a single marketplace.
        :raises InstallationJobNamespaceConstraintViolated: The target installations must belong to a single namespace.
        :raises InstallationJobOntologyConstraintViolated: The target installations must have at most one resulting ontology after applying location overrides.
        :raises InstallationTargetVersionNotFound: The requested target version could not be found within the installation product and marketplace.
        :raises InstallationUninstallStarted: Uninstall has begun for the target installation. Create a new installation to install the product again.
        :raises InvalidInstallationTargetVersion: The target semantic version must be an exact major.minor.patch version with non-negative integer components and no leading zeros. Each component must be at most 2⁵³ - 2 (9,007,199,254,740,990). Version ranges, wildcards, prerelease identifiers, and build metadata are not supported.
        :raises MarketplaceInstallationNotFound:
        :raises MaxInstallationJobInstallationsCountExceeded: The number of installation targets exceeds the maximum supported by this operation.
        :raises MissingInstallationJobInstallations: At least one installation target must be supplied.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v3/platform/marketplaceInstallationJobs/discoverInputs",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=marketplace_models.DiscoverInstallationJobInputsRequest(
                    installations=installations,
                    recommendations=recommendations,
                    source_filter=source_filter,
                ),
                response_type=marketplace_models.DiscoverInstallationJobInputsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "AmbiguousInstallationRecommendation": marketplace_errors.AmbiguousInstallationRecommendation,
                    "ConflictingInstallationRecommendation": marketplace_errors.ConflictingInstallationRecommendation,
                    "DiscoverInstallationJobInputsFailed": marketplace_errors.DiscoverInstallationJobInputsFailed,
                    "DiscoverInstallationJobInputsPermissionDenied": marketplace_errors.DiscoverInstallationJobInputsPermissionDenied,
                    "DuplicateInstallationJobInstallations": marketplace_errors.DuplicateInstallationJobInstallations,
                    "DuplicateInstallationJobProducts": marketplace_errors.DuplicateInstallationJobProducts,
                    "InstallationDraftAlreadyExists": marketplace_errors.InstallationDraftAlreadyExists,
                    "InstallationInputApiNamesNotEnabled": marketplace_errors.InstallationInputApiNamesNotEnabled,
                    "InstallationJobMarketplaceConstraintViolated": marketplace_errors.InstallationJobMarketplaceConstraintViolated,
                    "InstallationJobNamespaceConstraintViolated": marketplace_errors.InstallationJobNamespaceConstraintViolated,
                    "InstallationJobOntologyConstraintViolated": marketplace_errors.InstallationJobOntologyConstraintViolated,
                    "InstallationTargetVersionNotFound": marketplace_errors.InstallationTargetVersionNotFound,
                    "InstallationUninstallStarted": marketplace_errors.InstallationUninstallStarted,
                    "InvalidInstallationTargetVersion": marketplace_errors.InvalidInstallationTargetVersion,
                    "MarketplaceInstallationNotFound": marketplace_errors.MarketplaceInstallationNotFound,
                    "MaxInstallationJobInstallationsCountExceeded": marketplace_errors.MaxInstallationJobInstallationsCountExceeded,
                    "MissingInstallationJobInstallations": marketplace_errors.MissingInstallationJobInstallations,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        marketplace_installation_job_rid: marketplace_models.MarketplaceInstallationJobRid,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[marketplace_models.MarketplaceInstallationJob]:
        """
        Get the current status of an installation job through draft preparation and execution.

        The request token must have permission to view the draft or submitted job. Missing or inaccessible jobs return
        `MarketplaceInstallationJobNotFound`. A failed or aborted job still returns HTTP 200 with its current status.

        Required scopes: [api:v3:marketplace-installation-job:read:get]

        :param marketplace_installation_job_rid:
        :type marketplace_installation_job_rid: MarketplaceInstallationJobRid
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[marketplace_models.MarketplaceInstallationJob]

        :raises MarketplaceInstallationJobNotFound:
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v3/platform/marketplaceInstallationJobs/{marketplaceInstallationJobRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "marketplaceInstallationJobRid": marketplace_installation_job_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=marketplace_models.MarketplaceInstallationJob,
                request_timeout=request_timeout,
                throwable_errors={
                    "MarketplaceInstallationJobNotFound": marketplace_errors.MarketplaceInstallationJobNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncMarketplaceInstallationJobClientRaw:
    def __init__(self, client: AsyncMarketplaceInstallationJobClient) -> None:
        def abort(_: None): ...
        def create(_: marketplace_models.MarketplaceInstallationJob): ...
        def discover_inputs(_: marketplace_models.DiscoverInstallationJobInputsResponse): ...
        def get(_: marketplace_models.MarketplaceInstallationJob): ...

        self.abort = core.async_with_raw_response(abort, client.abort)
        self.create = core.async_with_raw_response(create, client.create)
        self.discover_inputs = core.async_with_raw_response(discover_inputs, client.discover_inputs)
        self.get = core.async_with_raw_response(get, client.get)


class _AsyncMarketplaceInstallationJobClientStreaming:
    def __init__(self, client: AsyncMarketplaceInstallationJobClient) -> None:
        def create(_: marketplace_models.MarketplaceInstallationJob): ...
        def discover_inputs(_: marketplace_models.DiscoverInstallationJobInputsResponse): ...
        def get(_: marketplace_models.MarketplaceInstallationJob): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.discover_inputs = core.async_with_streaming_response(
            discover_inputs, client.discover_inputs
        )
        self.get = core.async_with_streaming_response(get, client.get)
