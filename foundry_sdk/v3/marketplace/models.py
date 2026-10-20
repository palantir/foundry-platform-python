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

import typing

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk.v3.core import models as core_models

CondaPackageExtension: typing_extensions.TypeAlias = typing.Literal["TAR_BZ2", "CONDA"]
"""CondaPackageExtension"""


ConfigurationKey: typing_extensions.TypeAlias = str
"""ConfigurationKey"""


ConfigurationValue: typing_extensions.TypeAlias = typing.Any
"""A JSON configuration value."""


class CreateMarketplaceInstallationJobRequest(core.ModelBase):
    """CreateMarketplaceInstallationJobRequest"""

    installations: typing.List[InstallationJobTarget]
    """Existing installations to upgrade to their target versions, along with their input mappings."""

    recommendations: typing.List[RecommendationStrategy]
    """Strategies for selecting other installations whose outputs can fulfill the targets' inputs. Targets in this request may still supply inputs to one another, independent of recommendation strategy."""

    submission_mode: typing.Optional[InstallationJobSubmissionMode] = pydantic.Field(alias=str("submissionMode"), default=None)  # type: ignore[literal-required]


class CreateMarketplaceInstallationRequest(core.ModelBase):
    """CreateMarketplaceInstallationRequest"""

    installation_suffix: typing.Optional[str] = pydantic.Field(alias=str("installationSuffix"), default=None)  # type: ignore[literal-required]
    """An optional suffix appended to the product title to form the initial display name, for example "Product title - CI staging". If omitted, the display name uses the product title alone."""

    marketplace_rid: MarketplaceRid = pydantic.Field(alias=str("marketplaceRid"))  # type: ignore[literal-required]
    ontology_rid: typing.Optional[core_models.OntologyRid] = pydantic.Field(alias=str("ontologyRid"), default=None)  # type: ignore[literal-required]
    """The ontology where jobs for this installation create or update ontology resources. Omit if the product does not interact with the ontology."""

    parent_folder_rid: core_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    """The RID of the Compass project or folder that currently contains the installation. On creation, this is the destination where the installation is registered and its jobs create resources."""

    product_id: ProductId = pydantic.Field(alias=str("productId"))  # type: ignore[literal-required]
    target_version_hint: typing.Optional[ProductVersionSelector] = pydantic.Field(alias=str("targetVersionHint"), default=None)  # type: ignore[literal-required]
    """
    If provided:
     - validations that are version specific (e.g. singleton validations) are executed assuming
        the installation will later have a job run to transition it to this specific target version.
     - the installation title is resolved from the product title at that version.

    If not provided, the latest released version of the product is used to resolve information for
    the steps above.
    """


CredentialSecrets: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["PlaintextCredentialSecrets", "RedactedCredentialSecrets"],
    pydantic.Field(discriminator="type"),
]
"""
Supply the plaintext variant when configuring an installation job.
Inspection returns the redacted variant, which contains only secret names
and cannot be submitted as credentials for another installation job.
"""


class CurrentInstallationInput(core.ModelBase):
    """A fulfilled input of the installation, including how its current value was supplied."""

    source: InputSource
    """The mechanism that supplied the current value."""

    value: InputValue
    """The current value. Its representation may differ from the one originally supplied. Credentials contain only secret names, with no secret values, and cannot be used as input to another installation job."""


class DiscoverInstallationJobInputsRequest(core.ModelBase):
    """DiscoverInstallationJobInputsRequest"""

    installations: typing.List[InstallationTarget]
    """Between 1 and 10 distinct installations, with at most one installation per product. Targets must share a namespace and marketplace and have at most one resulting ontology after applying overrides."""

    recommendations: typing.List[RecommendationStrategy]
    """An empty list disables recommendations from installations outside the requested targets. Targets in this request may still supply inputs to one another."""

    source_filter: typing.Optional[SourceFilter] = pydantic.Field(alias=str("sourceFilter"), default=None)  # type: ignore[literal-required]
    """When supplied, excludes an input if any of its available sources appears in `excludedSources`. If omitted, returns only inputs whose sole available source is `MANUAL`. Inputs with no available source are always omitted."""


class DiscoverInstallationJobInputsResponse(core.ModelBase):
    """DiscoverInstallationJobInputsResponse"""

    errors: typing.List[InstallationError]
    """Errors encountered during input resolution. Errors for inputs excluded by `sourceFilter` are omitted."""

    inputs: typing.Dict[MarketplaceInstallationRid, DiscoveredInstallationInputs]
    """All matching input requirements for each requested installation after source filtering, without pagination. An installation's input map is empty if no inputs match."""


class DiscoveredInstallationInputs(core.ModelBase):
    """Input requirements keyed by qualified input API name for one proposed installation target."""

    inputs: typing.Dict[InputApiName, InputMetadata]


ErrorCode: typing_extensions.TypeAlias = typing.Literal[
    "UNAUTHORIZED",
    "INTERNAL",
    "PERMISSION_DENIED",
    "INVALID_ARGUMENT",
    "NOT_FOUND",
    "REQUEST_ENTITY_TOO_LARGE",
    "FAILED_PRECONDITION",
    "CUSTOM_CLIENT",
    "CUSTOM_SERVER",
    "CONFLICT",
    "TIMEOUT",
]
"""The source error's broad category. This is response data and does not determine the HTTP status or error severity."""


class ErrorDetails(core.ModelBase):
    """ErrorDetails"""

    error_code: ErrorCode = pydantic.Field(alias=str("errorCode"))  # type: ignore[literal-required]
    error_name: ErrorName = pydantic.Field(alias=str("errorName"))  # type: ignore[literal-required]
    parameters: typing.Dict[ErrorParameterName, ErrorParameterValue]
    """Additional parameters describing the error."""

    type: typing.Literal["other"] = "other"


ErrorName: typing_extensions.TypeAlias = str
"""The source error's namespace-qualified name, for example `Marketplace:IncompatibleDefaultBuildOptions`."""


ErrorParameterName: typing_extensions.TypeAlias = str
"""The name of a parameter describing an installation error."""


ErrorParameterValue: typing_extensions.TypeAlias = typing.Any
"""The value of a parameter describing an installation error."""


ErrorSeverity: typing_extensions.TypeAlias = typing.Literal["BLOCKING", "NON_BLOCKING"]
"""Whether the error blocks proceeding with the proposed installation."""


ErrorTarget: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["ErrorTargetInputsAndOutputs", "ErrorTargetInstallation", "ErrorTargetJob"],
    pydantic.Field(discriminator="type"),
]
"""The proposed job, installation, or input and output references affected by the error."""


class ErrorTargetInputsAndOutputs(core.ModelBase):
    """The inputs and outputs this error applies to. Either or both can be present."""

    inputs: typing.List[InputReference]
    installation_rid: MarketplaceInstallationRid = pydantic.Field(alias=str("installationRid"))  # type: ignore[literal-required]
    outputs: typing.List[OutputReference]
    type: typing.Literal["inputsAndOutputs"] = "inputsAndOutputs"


class ErrorTargetInstallation(core.ModelBase):
    """ErrorTargetInstallation"""

    installation_rid: MarketplaceInstallationRid = pydantic.Field(alias=str("installationRid"))  # type: ignore[literal-required]
    type: typing.Literal["installation"] = "installation"


class ErrorTargetJob(core.ModelBase):
    """Affects the proposed job as a whole."""

    type: typing.Literal["job"] = "job"


FunctionApiStability: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["FunctionApiStabilityDeduplicate", "FunctionApiStabilityStable"],
    pydantic.Field(discriminator="type"),
]
"""How installation selects function versions and API names."""


class FunctionApiStabilityDeduplicate(core.ModelBase):
    """Increment the minor version of an existing function and deduplicate conflicting API names with a numeric suffix. Initial installations use version `0.1.0`."""

    type: typing.Literal["deduplicate"] = "deduplicate"


class FunctionApiStabilityStable(core.ModelBase):
    """Preserve the packaged function version and API name. A version conflict allocates a new function RID; an API name conflict fails installation."""

    type: typing.Literal["stable"] = "stable"


class GeotimeDestination(core.ModelBase):
    """A remote Geotime destination. Its system identifier must differ from the local system identifier."""

    destination_id: core.UUID = pydantic.Field(alias=str("destinationId"))  # type: ignore[literal-required]
    """The destination system's identifier."""

    namespace_rid: typing.Optional[core_models.NamespaceRid] = pydantic.Field(alias=str("namespaceRid"), default=None)  # type: ignore[literal-required]
    """The destination namespace. Omit for a remote system that does not use namespaces."""

    type: typing.Literal["remote"] = "remote"


GeotimeDestinations: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["LocalGeotimeDestination", "PeeredGeotimeDestinations", "GeotimeDestination"],
    pydantic.Field(discriminator="type"),
]
"""Where the installed pipeline writes Geotime data."""


InputApiName: typing_extensions.TypeAlias = str
"""The dot-separated API name of an input, including its ancestors, for example `myDataset.address`."""


InputId: typing_extensions.TypeAlias = core.UUID
"""The UUID of an input in the product definition."""


class InputMetadata(core.ModelBase):
    """An input of the target product as it applies to a proposed installation or upgrade."""

    input_id: InputId = pydantic.Field(alias=str("inputId"))  # type: ignore[literal-required]
    input_type: InputType = pydantic.Field(alias=str("inputType"))  # type: ignore[literal-required]
    optional: bool
    """Whether the product allows this input to be left unfulfilled. Non-optional inputs may be fulfilled automatically, thus still not requiring manual user intervention."""

    sources: typing.List[InputSource]
    """Available sources to fulfill the value of the input."""

    supported_types: typing.List[SupportedInputType] = pydantic.Field(alias=str("supportedTypes"))  # type: ignore[literal-required]
    """Accepted representations for supplied values, most preferred first."""


class InputReference(core.ModelBase):
    """InputReference"""

    api_name: InputApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    input_id: InputId = pydantic.Field(alias=str("inputId"))  # type: ignore[literal-required]


InputSource: typing_extensions.TypeAlias = typing.Literal[
    "MANUAL", "AUTO_MAPPED", "AUTO_MAPPED_FROM_PARENT", "DEFAULT", "EXTERNAL_RECOMMENDATION"
]
"""
An available mechanism for fulfilling an installation input.

Values:
- **AUTO_MAPPED**: A value can be supplied by an automatic mapping.
- **AUTO_MAPPED_FROM_PARENT**: Supports deriving its value from the parent input.
- **DEFAULT**: A successfully resolved product default.
- **EXTERNAL_RECOMMENDATION**: A value can be supplied by an output from a recommended installation.
- **MANUAL**: A value can be supplied manually. Available only when `supportedTypes` is nonempty.
"""


InputType: typing_extensions.TypeAlias = typing.Literal[
    "ACTION",
    "ACTION_PARAMETER",
    "AGENT_BUILDER_AGENT",
    "AGENT_DEFINITION",
    "ONTOLOGY_SCHEMA_MIGRATION_POLICY",
    "AIP_AGENT",
    "ARTIFACTS_REPOSITORY",
    "LIBRARY",
    "CODE_REPOSITORY",
    "AUTOMATION",
    "AUTOPILOT_WORKBENCH",
    "BLOBSTER_RESOURCE",
    "CARBON_WORKSPACE",
    "CIPHER_CHANNEL",
    "CIPHER_LICENSE",
    "CODE_WORKSPACE",
    "CODE_WORKSPACE_LICENSE",
    "COMPASS_RESOURCE",
    "CONTOUR_ANALYSIS",
    "CONTOUR_REF",
    "DATA_HEALTH_CHECK",
    "DATA_HEALTH_CHECK_GROUP",
    "DATA_SOURCE_COLUMN",
    "DEPLOYED_APP",
    "PIPELINE_BUILDER_PARAMETER",
    "PIPELINE_BUILDER_PIPELINE",
    "PIPELINE_BUILDER_REPLAY_OPTION",
    "PIPELINE_BUILDER_GEOTIME_CONFIGURATION",
    "EDGE_PIPELINE_PARAMETER",
    "EDGE_PIPELINE_SOURCE_CONFIGURATION",
    "EVALUATION_SUITE",
    "FILES_DATA_SOURCE",
    "FLINK_PROFILE",
    "FUNCTION",
    "FUNCTION_CONTRACT",
    "FUNCTION_API_STABILITY",
    "FUSION_DOCUMENT",
    "GEOTIME_SERIES_INTEGRATION",
    "INTERFACE_TYPE",
    "INTERFACE_LINK_TYPE",
    "INTERFACE_PROPERTY_TYPE",
    "INTERFACE_ACTION_TYPE_CONSTRAINT",
    "INTERFACE_PARAMETER_CONSTRAINT",
    "INSTALLATION_PREFIX",
    "LANGUAGE_MODEL",
    "LANGUAGE_MODEL_V2",
    "LINK_TYPE",
    "LIVE_DEPLOYMENT",
    "LOGIC",
    "LOGIC_FUNCTION",
    "MACHINERY",
    "DATA_CONNECTION",
    "DATA_CONNECTION_EXPORT",
    "DATA_CONNECTION_SOURCE",
    "CONNECTION_CONFIGURATION_OVERRIDES",
    "STREAMING_SYNC_CONFIGURATION_OVERRIDES",
    "MAP_RENDERING_SYMBOL_TYPE",
    "MARKINGS",
    "MODEL_STUDIO",
    "MODEL",
    "DATA_LINEAGE_GRAPH",
    "USER_ATTRIBUTE",
    "GROUP",
    "NAMED_CREDENTIAL",
    "NETWORK_EGRESS_POLICY",
    "NOTEPAD_DOCUMENT",
    "NOTEPAD_TEMPLATE",
    "NOTEPAD_TEMPLATE_PARAMETER",
    "OBJECT_INSTANCE",
    "OBJECT_SET",
    "OBJECT_TYPE",
    "OBJECT_VIEW",
    "OBJECT_VIEW_TAB",
    "ONTOLOGY_DATA_SOURCE",
    "ONTOLOGY_DATA_SOURCE_RETENTION",
    "ONTOLOGY_SCHEMA_MIGRATION_VALUES",
    "ONTOLOGY_SDK",
    "OVERRIDE_ONTOLOGY_ENTITY_API_NAMES",
    "PARAMETER",
    "PEER_PRODUCER_PROFILE",
    "PEER_PROFILE",
    "PEER_PROFILE_REMOTE_STRATEGY",
    "PROPERTY",
    "QUIVER_DASHBOARD",
    "SAVED_SEARCH_AROUND",
    "SCHEDULE",
    "SHARED_PROPERTY_TYPE",
    "SLATE_APPLICATION",
    "STORED_PROCEDURE",
    "SOLUTION_DESIGN",
    "SPARK_PROFILE",
    "TABULAR_DATA_SOURCE",
    "TAURUS_WORKFLOW",
    "THIRD_PARTY_APPLICATION",
    "TIME_SERIES_SYNC",
    "VALUE_TYPE",
    "CODE_WORKBOOK",
    "VERSIONED_OBJECT_SET",
    "VERTEX_TEMPLATE",
    "VORTEX_TEMPLATE",
    "WALKTHROUGH",
    "WEBHOOK",
    "WIDGET",
    "WIDGET_SET",
    "WORKBENCH_TEMPLATE",
    "WORKFLOW_BUILDER_GRAPH",
    "WORKFLOW_GRAPH",
    "SQL_WORKSHEET",
    "WORKSHOP_APPLICATION",
    "WORKSHOP_APPLICATION_SAVE_LOCATION",
    "OTHER",
]
"""
The kind of resource or configuration requested by a product input. Use `supportedTypes` to determine accepted value representations. `OTHER` covers input kinds that do not have a named value here.

Values:
- **OTHER**: A legacy or newly introduced input kind without a named value in this API.
"""


InputValue: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "InputValueApiName",
        "InputValueBoolean",
        "InputValueCredential",
        "InputValueCron",
        "InputValueInteger",
        "InputValueResolved",
        "InputValueRid",
        "InputValueRidWithVersion",
        "InputValueString",
        "InputValueStrings",
    ],
    pydantic.Field(discriminator="type"),
]
"""A value fulfilling a product input. Use a representation advertised by the input's `supportedTypes`, preferring the first applicable representation. Structured values use the `resolved` variant."""


class InputValueApiName(core.ModelBase):
    """InputValueApiName"""

    api_name: str = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    """The API name of the referenced entity. This is not related to the qualified name identifying the product input."""

    type: typing.Literal["apiName"] = "apiName"


class InputValueBoolean(core.ModelBase):
    """InputValueBoolean"""

    value: bool
    type: typing.Literal["boolean"] = "boolean"


class InputValueCredential(core.ModelBase):
    """InputValueCredential"""

    secrets: CredentialSecrets
    type: typing.Literal["credential"] = "credential"


class InputValueCron(core.ModelBase):
    """InputValueCron"""

    cron_expression: str = pydantic.Field(alias=str("cronExpression"))  # type: ignore[literal-required]
    time_zone: str = pydantic.Field(alias=str("timeZone"))  # type: ignore[literal-required]
    """The time zone used to evaluate the cron expression, for example `Europe/London`."""

    type: typing.Literal["cron"] = "cron"


class InputValueInteger(core.ModelBase):
    """InputValueInteger"""

    value: int
    type: typing.Literal["integer"] = "integer"


class InputValueResolved(core.ModelBase):
    """InputValueResolved"""

    value: ResolvedInput
    type: typing.Literal["resolved"] = "resolved"


class InputValueRid(core.ModelBase):
    """InputValueRid"""

    rid: core.RID
    type: typing.Literal["rid"] = "rid"


class InputValueRidWithVersion(core.ModelBase):
    """InputValueRidWithVersion"""

    rid: core.RID
    version: str
    """The resource version, in the format accepted by this input."""

    type: typing.Literal["ridWithVersion"] = "ridWithVersion"


class InputValueString(core.ModelBase):
    """InputValueString"""

    value: str
    type: typing.Literal["string"] = "string"


class InputValueStrings(core.ModelBase):
    """InputValueStrings"""

    values: typing.List[str]
    type: typing.Literal["strings"] = "strings"


class InstallationError(core.ModelBase):
    """A resolution or validation error. Resource references are included only when visible to the request token."""

    error_value: ErrorValue = pydantic.Field(alias=str("errorValue"))  # type: ignore[literal-required]
    severity: ErrorSeverity
    target: ErrorTarget


InstallationInputSelection: typing_extensions.TypeAlias = typing.Literal["MANUAL_ONLY", "ALL"]
"""
Which fulfilled installation inputs to return based on their source.

Values:
- **ALL**: Include inputs from every stored source.
- **MANUAL_ONLY**: Include manually fulfilled inputs only.
"""


class InstallationJobDraftMode(core.ModelBase):
    """Prepare and validate the job draft without submitting a job. The draft remains available for later action."""

    type: typing.Literal["draft"] = "draft"


class InstallationJobDraftPreparationFailure(core.ModelBase):
    """An error prevented draft preparation from reaching a consistent state."""

    error: ErrorValue
    """The error encountered while preparing the draft. The resolved state may be incomplete."""

    type: typing.Literal["draftPreparation"] = "draftPreparation"


InstallationJobErrorHandling: typing_extensions.TypeAlias = typing.Literal["IDLE", "ABORT"]
"""
What to do with a draft if preparation fails or submission is prevented.

Values:
- **ABORT**: Abort and clean up the draft.
- **IDLE**: Retain the draft for inspection or continuation in Marketplace.
"""


class InstallationJobExecutionFailure(core.ModelBase):
    """Errors from a submitted installation job."""

    errors: typing.List[ErrorValue]
    """
    Errors recorded during job, integration, and build execution. Each error has an `errorType` parameter containing
    `kind` (`installJob`, `integration`, or `build`) and, for integration and build errors, `integrationType`.
    """

    stage: InstallationJobFailureStage
    type: typing.Literal["execution"] = "execution"


InstallationJobFailure: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["InstallationJobDraftPreparationFailure", "InstallationJobExecutionFailure"],
    pydantic.Field(discriminator="type"),
]
"""Failure diagnostics grouped by the phase in which the failure occurred."""


InstallationJobFailureStage: typing_extensions.TypeAlias = typing.Literal[
    "IN_PROGRESS_ERROR", "BUILD_ERRORED", "BUILD_TIMED_OUT"
]
"""The stage and cause of a submitted installation job's failure."""


class InstallationJobInputs(core.ModelBase):
    """Input values and explicitly unset inputs for a target installation. Inputs absent from both fields may be fulfilled by defaults, automatic mapping, or recommendations. Use `discoverInputs` to inspect available sources."""

    explicitly_unset: typing.List[InputApiName] = pydantic.Field(alias=str("explicitlyUnset"))  # type: ignore[literal-required]
    """Names deliberately left unfulfilled. An unset suppresses automatic fulfillment. Names must not also occur in `values`. An unset child does not require an explicitly supplied parent."""

    values: typing.Dict[InputApiName, InputValue]
    """Manually supplied values keyed by qualified input API name. A child with a value requires its parent to have a value in this map, recursively through the ancestor chain."""


InstallationJobSubmissionMode: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["InstallationJobDraftMode", "InstallationJobSubmitMode"],
    pydantic.Field(discriminator="type"),
]
"""If omitted, submit with `NON_BLOCKING_ERRORS` tolerance and `ABORT` handling."""


class InstallationJobSubmitMode(core.ModelBase):
    """Submit the job after draft preparation and validation if errors fall within the selected tolerance."""

    error_handling: typing.Optional[InstallationJobErrorHandling] = pydantic.Field(alias=str("errorHandling"), default=None)  # type: ignore[literal-required]
    """If omitted, uses `ABORT`."""

    error_tolerance: typing.Optional[InstallationJobValidationErrorTolerance] = pydantic.Field(alias=str("errorTolerance"), default=None)  # type: ignore[literal-required]
    """If omitted, uses `NON_BLOCKING_ERRORS`."""

    type: typing.Literal["submit"] = "submit"


class InstallationJobTarget(core.ModelBase):
    """An existing installation to upgrade, its target version, and its input selections."""

    inputs: InstallationJobInputs
    installation_rid: MarketplaceInstallationRid = pydantic.Field(alias=str("installationRid"))  # type: ignore[literal-required]
    overrides: typing.Optional[InstallationOverrides] = None
    """If omitted, preserve the existing settings."""

    target_version: TargetVersion = pydantic.Field(alias=str("targetVersion"))  # type: ignore[literal-required]


InstallationJobValidation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["InstallationJobValidationErrors", "InstallationJobValidationSummary"],
    pydantic.Field(discriminator="type"),
]
"""Validation results available to the viewer."""


InstallationJobValidationErrorTolerance: typing_extensions.TypeAlias = typing.Literal[
    "NONE", "NON_BLOCKING_ERRORS"
]
"""
Which validation errors may be tolerated when deciding whether to submit the job.

Values:
- **NONE**: Any validation error prevents submission.
- **NON_BLOCKING_ERRORS**: Only blocking validation errors prevent submission.
"""


class InstallationJobValidationErrors(core.ModelBase):
    """Validation errors visible to the job owner."""

    errors: typing.List[InstallationError]
    type: typing.Literal["errors"] = "errors"


class InstallationJobValidationSummary(core.ModelBase):
    """A validation error count visible to authorized viewers other than the job owner."""

    total_blocking_errors: int = pydantic.Field(alias=str("totalBlockingErrors"))  # type: ignore[literal-required]
    type: typing.Literal["summary"] = "summary"


class InstallationOverrides(core.ModelBase):
    """Changes to the installation's location for the proposed job. The destination folder is unchanged."""

    ontology: typing.Optional[OntologyOverride] = None
    """If omitted, preserve the existing ontology location."""


InstallationPrefixConfiguration: typing_extensions.TypeAlias = typing.Literal[
    "DISPLAY_NAME_ONLY", "DISPLAY_NAME_AND_API_NAME"
]
"""
Values:
- **DISPLAY_NAME_AND_API_NAME**: Prefix Ontology entity display names and API names.
- **DISPLAY_NAME_ONLY**: Prefix Ontology entity display names only.
"""


class InstallationTarget(core.ModelBase):
    """An existing installation and its target product version."""

    installation_rid: MarketplaceInstallationRid = pydantic.Field(alias=str("installationRid"))  # type: ignore[literal-required]
    overrides: typing.Optional[InstallationOverrides] = None
    """If omitted, preserve the existing ontology location."""

    target_version: TargetVersion = pydantic.Field(alias=str("targetVersion"))  # type: ignore[literal-required]


InvalidInstallationInputReason: typing_extensions.TypeAlias = typing.Literal[
    "MISSING_VERSION",
    "INVALID_VERSION",
    "UNSUPPORTED_TYPE",
    "RESOURCE_UNAVAILABLE",
    "INVALID_PARENT_INPUT",
]
"""
Why a supplied input value cannot be used.

Values:
- **INVALID_PARENT_INPUT**: A supplied parent input did not resolve to the type required by the child input.
- **INVALID_VERSION**: The supplied version could not be parsed in the format required by this input.
- **MISSING_VERSION**: This input requires a resource version. Supply it using the `ridWithVersion` value variant.
- **RESOURCE_UNAVAILABLE**: The referenced resource or a required version could not be found or resolved.
- **UNSUPPORTED_TYPE**: The supplied value variant is not supported for this input. Use one of the input's `supportedTypes`.
"""


LibraryLocator: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["LibraryLocatorConda", "LibraryLocatorPath"], pydantic.Field(discriminator="type")
]
"""The library's location within an artifacts repository."""


class LibraryLocatorConda(core.ModelBase):
    """LibraryLocatorConda"""

    build_string: str = pydantic.Field(alias=str("buildString"))  # type: ignore[literal-required]
    extension: CondaPackageExtension
    name: str
    platform: str
    version: str
    type: typing.Literal["conda"] = "conda"


class LibraryLocatorPath(core.ModelBase):
    """LibraryLocatorPath"""

    path: str
    """The path to the library file in the repository's Conda layout."""

    type: typing.Literal["path"] = "path"


class LocalGeotimeDestination(core.ModelBase):
    """Write to the local Geotime. Omit `namespaceRid` to use the default local destination."""

    namespace_rid: typing.Optional[core_models.NamespaceRid] = pydantic.Field(alias=str("namespaceRid"), default=None)  # type: ignore[literal-required]
    """The namespace of a specific local destination."""

    type: typing.Literal["local"] = "local"


class MarketplaceInstallation(core.ModelBase):
    """A registered product installation and Compass resource. Its latest target version is absent until an installation job runs."""

    description: typing.Optional[str] = None
    """The current description of the installation in Compass. Absent if no description is set."""

    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The current display name of the installation in Compass."""

    latest_target_version: typing.Optional[ProductVersion] = pydantic.Field(alias=str("latestTargetVersion"), default=None)  # type: ignore[literal-required]
    """The product version targeted by the latest submitted installation job. This may differ from the currently installed version. Absent if no installation job has run."""

    marketplace_rid: MarketplaceRid = pydantic.Field(alias=str("marketplaceRid"))  # type: ignore[literal-required]
    namespace_rid: core_models.NamespaceRid = pydantic.Field(alias=str("namespaceRid"))  # type: ignore[literal-required]
    """The RID of the namespace that the installation currently belongs to in Compass."""

    ontology_rid: typing.Optional[core_models.OntologyRid] = pydantic.Field(alias=str("ontologyRid"), default=None)  # type: ignore[literal-required]
    """The ontology where jobs for this installation create or update ontology resources. Omit if the product does not interact with the ontology."""

    parent_folder_rid: core_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    """The RID of the Compass project or folder that currently contains the installation. On creation, this is the destination where the installation is registered and its jobs create resources."""

    product_id: ProductId = pydantic.Field(alias=str("productId"))  # type: ignore[literal-required]
    rid: MarketplaceInstallationRid


class MarketplaceInstallationInputs(core.ModelBase):
    """The current fulfilled inputs and inputs explicitly left unfulfilled by the last job of a registered Marketplace installation."""

    explicitly_unset: typing.List[InputApiName] = pydantic.Field(alias=str("explicitlyUnset"))  # type: ignore[literal-required]
    """Qualified API names explicitly left unfulfilled by the last job that modified the installation. Optional inputs that were neither fulfilled nor explicitly unset are absent from both fields."""

    inputs: typing.Dict[InputApiName, CurrentInstallationInput]
    """Fulfilled values keyed by qualified input API name. Optional inputs without a current value are absent."""


class MarketplaceInstallationJob(core.ModelBase):
    """An attempt to upgrade one or more existing product installations. The same RID identifies the draft and its submitted job."""

    rid: MarketplaceInstallationJobRid
    status: MarketplaceInstallationJobStatus


class MarketplaceInstallationJobDetails(core.ModelBase):
    """Available validation and failure diagnostics for an installation job or draft."""

    failure: typing.Optional[InstallationJobFailure] = None
    """
    Diagnostics for a draft preparation or submitted-job execution failure, when available. A draft preparation
    failure can appear alongside validation. Absence does not mean the job succeeded; for example, an explicitly
    aborted job may have no failure diagnostics. Check the job's `status` for its outcome.
    """

    validation: typing.Optional[InstallationJobValidation] = None
    """
    Draft validation results, when available. The draft owner receives the full list of errors; other authorized
    viewers receive a summary of blocking errors. An empty error list or a summary count of zero is a validation
    result, not an absence of validation. This field is absent when no draft validation result is available.
    """


MarketplaceInstallationJobRid: typing_extensions.TypeAlias = core.RID
"""The RID of a Marketplace installation job or its draft."""


MarketplaceInstallationJobStatus: typing_extensions.TypeAlias = typing.Literal[
    "PREPARING",
    "IDLE_DRAFT",
    "ABORTING",
    "IN_PROGRESS",
    "BUILDING",
    "ABORTED",
    "SUCCEEDED",
    "FAILED",
]
"""
Values:
- **ABORTED**: The draft or running job was aborted. This can happen either via an explicit abort call or from a job submission failure. An aborted draft remains queryable until automatic cleanup, after which it is no longer found. Terminal status.
- **ABORTING**: Cancellation has been requested for the submitted installation job, but it has not yet reached a terminal state. Continue polling.
- **BUILDING**: Resources have been installed and dataset builds are being submitted or awaited. Continue polling.
- **FAILED**: The installation job failed. Terminal.
- **IDLE_DRAFT**: The draft is retained without running an installation job, either by request or because submission was prevented. Further action is required to submit it; polling alone will not advance it.
- **IN_PROGRESS**: The installation job is executing. Continue polling.
- **PREPARING**: The draft is resolving inputs, validating, or being submitted. Continue polling.
- **SUCCEEDED**: The installation job completed successfully. Terminal.
"""


MarketplaceInstallationRid: typing_extensions.TypeAlias = core.RID
"""MarketplaceInstallationRid"""


MarketplaceRid: typing_extensions.TypeAlias = core.RID
"""MarketplaceRid"""


MigrationCandidateId: typing_extensions.TypeAlias = str
"""A stable identifier for a potential Ontology schema migration in the product definition."""


OntologyLiteral: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "OntologyLiteralArray",
        "OntologyLiteralBoolean",
        "OntologyLiteralByte",
        "OntologyLiteralDate",
        "OntologyLiteralDecimal",
        "OntologyLiteralDouble",
        "OntologyLiteralFloat",
        "OntologyLiteralGeohash",
        "OntologyLiteralInteger",
        "OntologyLiteralLong",
        "OntologyLiteralShort",
        "OntologyLiteralString",
        "OntologyLiteralTimestamp",
    ],
    pydantic.Field(discriminator="type"),
]
"""A typed Ontology property literal."""


class OntologyLiteralArray(core.ModelBase):
    """OntologyLiteralArray"""

    values: typing.List[OntologyLiteralJson]
    type: typing.Literal["array"] = "array"


class OntologyLiteralBoolean(core.ModelBase):
    """OntologyLiteralBoolean"""

    value: bool
    type: typing.Literal["boolean"] = "boolean"


class OntologyLiteralByte(core.ModelBase):
    """OntologyLiteralByte"""

    value: int
    """A signed 8-bit integer, between -128 and 127, inclusive."""

    type: typing.Literal["byte"] = "byte"


class OntologyLiteralDate(core.ModelBase):
    """OntologyLiteralDate"""

    value: str
    """An ISO-8601 date without a time component, for example `2026-09-25`."""

    type: typing.Literal["date"] = "date"


class OntologyLiteralDecimal(core.ModelBase):
    """OntologyLiteralDecimal"""

    value: str
    """A decimal encoded as a string to preserve its exact value and scale, for example `1.2300`."""

    type: typing.Literal["decimal"] = "decimal"


class OntologyLiteralDouble(core.ModelBase):
    """OntologyLiteralDouble"""

    value: float
    type: typing.Literal["double"] = "double"


class OntologyLiteralFloat(core.ModelBase):
    """OntologyLiteralFloat"""

    value: float
    """A 32-bit floating-point value."""

    type: typing.Literal["float"] = "float"


class OntologyLiteralGeohash(core.ModelBase):
    """OntologyLiteralGeohash"""

    value: str
    """A geohash or a `latitude,longitude` pair using WGS-84 coordinates."""

    type: typing.Literal["geohash"] = "geohash"


class OntologyLiteralInteger(core.ModelBase):
    """OntologyLiteralInteger"""

    value: int
    type: typing.Literal["integer"] = "integer"


OntologyLiteralJson: typing_extensions.TypeAlias = typing.Any
"""
A tagged JSON object with the same structure and constraints as `OntologyLiteral`, used for an array element.
Scalar variants contain `type` and `value`; the `array` variant contains `values` with further tagged literals.
For example, `{"type":"array","values":[{"type":"long","value":"1234"}]}`.

Every nested literal must use a supported tag and its corresponding value format. Untagged objects, JSON null,
unknown tags, and values outside the selected type's range are invalid.
"""


class OntologyLiteralLong(core.ModelBase):
    """OntologyLiteralLong"""

    value: core.Long
    """A signed 64-bit integer."""

    type: typing.Literal["long"] = "long"


class OntologyLiteralShort(core.ModelBase):
    """OntologyLiteralShort"""

    value: int
    """A signed 16-bit integer, between -32768 and 32767, inclusive."""

    type: typing.Literal["short"] = "short"


class OntologyLiteralString(core.ModelBase):
    """OntologyLiteralString"""

    value: str
    type: typing.Literal["string"] = "string"


class OntologyLiteralTimestamp(core.ModelBase):
    """OntologyLiteralTimestamp"""

    value: core.AwareDatetime
    type: typing.Literal["timestamp"] = "timestamp"


OntologyOverride: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["OntologyOverrideRemove", "OntologyOverrideSet"],
    pydantic.Field(discriminator="type"),
]
"""Change the ontology location for the proposed job."""


class OntologyOverrideRemove(core.ModelBase):
    """Remove the installation's ontology location for the proposed job."""

    type: typing.Literal["remove"] = "remove"


class OntologyOverrideSet(core.ModelBase):
    """Use the specified ontology for the proposed job."""

    ontology_rid: core_models.OntologyRid = pydantic.Field(alias=str("ontologyRid"))  # type: ignore[literal-required]
    type: typing.Literal["set"] = "set"


class OntologyPropertyValueLiteral(core.ModelBase):
    """OntologyPropertyValueLiteral"""

    value: OntologyLiteral
    type: typing.Literal["literal"] = "literal"


class OntologySchemaMigrationSetPropertyValueIfUnset(core.ModelBase):
    """OntologySchemaMigrationSetPropertyValueIfUnset"""

    value: OntologyPropertyValue
    type: typing.Literal["setPropertyValueIfUnset"] = "setPropertyValueIfUnset"


OutputId: typing_extensions.TypeAlias = core.UUID
"""The UUID of an output in the product definition."""


class OutputReference(core.ModelBase):
    """OutputReference"""

    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    output_id: OutputId = pydantic.Field(alias=str("outputId"))  # type: ignore[literal-required]


PeerRemoteStrategy: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "PeerRemoteStrategyMeshId",
        "PeerRemoteStrategyMeshNodeLabel",
        "PeerRemoteStrategySpecificRemote",
    ],
    pydantic.Field(discriminator="type"),
]
"""Which remote systems and namespaces a peer profile governs."""


class PeerRemoteStrategyMeshId(core.ModelBase):
    """Select all members of the specified mesh."""

    mesh_id: core.UUID = pydantic.Field(alias=str("meshId"))  # type: ignore[literal-required]
    type: typing.Literal["meshId"] = "meshId"


class PeerRemoteStrategyMeshNodeLabel(core.ModelBase):
    """Select members of the specified mesh with the given labels."""

    mesh_id: core.UUID = pydantic.Field(alias=str("meshId"))  # type: ignore[literal-required]
    mesh_node_labels: typing.List[str] = pydantic.Field(alias=str("meshNodeLabels"))  # type: ignore[literal-required]
    """Labels identifying mesh members. Entries must be unique."""

    type: typing.Literal["meshNodeLabel"] = "meshNodeLabel"


class PeerRemoteStrategySpecificRemote(core.ModelBase):
    """PeerRemoteStrategySpecificRemote"""

    remote_namespace: core_models.NamespaceRid = pydantic.Field(alias=str("remoteNamespace"))  # type: ignore[literal-required]
    remote_system: core.UUID = pydantic.Field(alias=str("remoteSystem"))  # type: ignore[literal-required]
    type: typing.Literal["specificRemote"] = "specificRemote"


class PeeredGeotimeDestination(core.ModelBase):
    """PeeredGeotimeDestination"""

    destination_id: core.UUID = pydantic.Field(alias=str("destinationId"))  # type: ignore[literal-required]
    """The destination system's identifier."""

    namespace_rid: core_models.NamespaceRid = pydantic.Field(alias=str("namespaceRid"))  # type: ignore[literal-required]


class PeeredGeotimeDestinations(core.ModelBase):
    """Write to the local Geotime and peer to the specified destinations."""

    destinations: typing.List[PeeredGeotimeDestination]
    """At least one destination is required. Entries must be unique."""

    type: typing.Literal["peered"] = "peered"


PipelineBuilderLiteral: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "PipelineBuilderLiteralArray",
        "PipelineBuilderLiteralBinary",
        "PipelineBuilderLiteralBoolean",
        "PipelineBuilderLiteralDate",
        "PipelineBuilderLiteralDatetime",
        "PipelineBuilderLiteralDecimal",
        "PipelineBuilderLiteralDouble",
        "PipelineBuilderLiteralEmpty",
        "PipelineBuilderLiteralInteger",
        "PipelineBuilderLiteralLong",
        "PipelineBuilderLiteralMap",
        "PipelineBuilderLiteralString",
    ],
    pydantic.Field(discriminator="type"),
]
"""A typed pipeline parameter literal. Arrays and maps contain tagged literal JSON with the same variants and value formats, recursively. A null literal uses the `empty` variant rather than a JSON null value."""


class PipelineBuilderLiteralArray(core.ModelBase):
    """PipelineBuilderLiteralArray"""

    values: typing.List[PipelineBuilderLiteralJson]
    type: typing.Literal["array"] = "array"


class PipelineBuilderLiteralBinary(core.ModelBase):
    """PipelineBuilderLiteralBinary"""

    value: str
    """Binary data encoded as a Base64 string."""

    type: typing.Literal["binary"] = "binary"


class PipelineBuilderLiteralBoolean(core.ModelBase):
    """PipelineBuilderLiteralBoolean"""

    value: bool
    type: typing.Literal["boolean"] = "boolean"


class PipelineBuilderLiteralDate(core.ModelBase):
    """PipelineBuilderLiteralDate"""

    value: core.AwareDatetime
    """The date literal's ISO-8601 timestamp, preserving the pipeline parameter's timestamp representation."""

    type: typing.Literal["date"] = "date"


class PipelineBuilderLiteralDatetime(core.ModelBase):
    """PipelineBuilderLiteralDatetime"""

    value: core.AwareDatetime
    type: typing.Literal["datetime"] = "datetime"


class PipelineBuilderLiteralDecimal(core.ModelBase):
    """PipelineBuilderLiteralDecimal"""

    value: str
    """A decimal encoded as a string to preserve its exact value and scale, for example `1.2300`."""

    type: typing.Literal["decimal"] = "decimal"


class PipelineBuilderLiteralDouble(core.ModelBase):
    """PipelineBuilderLiteralDouble"""

    value: float
    type: typing.Literal["double"] = "double"


class PipelineBuilderLiteralEmpty(core.ModelBase):
    """A null literal."""

    type: typing.Literal["empty"] = "empty"


class PipelineBuilderLiteralInteger(core.ModelBase):
    """PipelineBuilderLiteralInteger"""

    value: int
    type: typing.Literal["integer"] = "integer"


PipelineBuilderLiteralJson: typing_extensions.TypeAlias = typing.Any
"""
A tagged JSON object with the same structure and constraints as `PipelineBuilderLiteral`, used for nested literals.
Scalar variants contain `type` and `value`; `array` contains `values`; `map` contains `entries` with `key` and `value`
literals; `empty` contains only `type`. Arrays and maps can contain further literals recursively. For example,
`{"type":"array","values":[{"type":"long","value":"42"},{"type":"empty"}]}`.

Every nested literal must use a supported tag and its corresponding value format. Untagged objects, JSON null,
unknown tags, and values outside the selected type's range are invalid.
"""


class PipelineBuilderLiteralLong(core.ModelBase):
    """PipelineBuilderLiteralLong"""

    value: core.Long
    """An integer encoded as a decimal-integer string. Must be between -9007199254740991 and 9007199254740991, inclusive."""

    type: typing.Literal["long"] = "long"


class PipelineBuilderLiteralMap(core.ModelBase):
    """PipelineBuilderLiteralMap"""

    entries: typing.List[PipelineBuilderLiteralMapEntry]
    """Typed map entries. Entries must be unique."""

    type: typing.Literal["map"] = "map"


class PipelineBuilderLiteralMapEntry(core.ModelBase):
    """PipelineBuilderLiteralMapEntry"""

    key: PipelineBuilderLiteralJson
    value: PipelineBuilderLiteralJson


class PipelineBuilderLiteralString(core.ModelBase):
    """PipelineBuilderLiteralString"""

    value: str
    type: typing.Literal["string"] = "string"


PipelineBuilderParameter: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "PipelineBuilderParameterEnum",
        "PipelineBuilderParameterLiteral",
        "PipelineBuilderParameterRegex",
    ],
    pydantic.Field(discriminator="type"),
]
"""A literal, regular expression, or enum value matching the parameter requested by the product."""


class PipelineBuilderParameterEnum(core.ModelBase):
    """PipelineBuilderParameterEnum"""

    value: str
    """One of the enum values accepted by the product's parameter."""

    type: typing.Literal["enum"] = "enum"


class PipelineBuilderParameterLiteral(core.ModelBase):
    """PipelineBuilderParameterLiteral"""

    value: PipelineBuilderLiteral
    type: typing.Literal["literal"] = "literal"


class PipelineBuilderParameterRegex(core.ModelBase):
    """PipelineBuilderParameterRegex"""

    pattern: str
    type: typing.Literal["regex"] = "regex"


PipelineReplayOption: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "PipelineReplayOptionAcknowledgeStateBreaks",
        "PipelineReplayOptionReset",
        "PipelineReplayOptionResetAndReplayFromOffset",
    ],
    pydantic.Field(discriminator="type"),
]
"""How a pipeline handles a state break during upgrade."""


class PipelineReplayOptionAcknowledgeStateBreaks(core.ModelBase):
    """Ignore state breaks and continue reading data where possible."""

    acknowledgement: typing.Optional[ReplayAcknowledgement] = None
    """Confirms the replay choice. If omitted, this choice is unacknowledged and will not be applied."""

    type: typing.Literal["acknowledgeStateBreaks"] = "acknowledgeStateBreaks"


class PipelineReplayOptionReset(core.ModelBase):
    """Reset the pipeline with all data."""

    acknowledgement: typing.Optional[ReplayAcknowledgement] = None
    """Confirms the replay choice. If omitted, this choice is unacknowledged and will not be applied."""

    type: typing.Literal["reset"] = "reset"


class PipelineReplayOptionResetAndReplayFromOffset(core.ModelBase):
    """Reset the pipeline with data received before the specified offset time."""

    acknowledgement: typing.Optional[ReplayAcknowledgement] = None
    """Confirms the replay choice. If omitted, this choice is unacknowledged and will not be applied."""

    offset_millis: core.Long = pydantic.Field(alias=str("offsetMillis"))  # type: ignore[literal-required]
    """The replay offset time in milliseconds. Encoded as a decimal-integer string; must be between -9007199254740991 and 9007199254740991, inclusive."""

    type: typing.Literal["resetAndReplayFromOffset"] = "resetAndReplayFromOffset"


class PlaintextCredentialSecrets(core.ModelBase):
    """PlaintextCredentialSecrets"""

    values: typing.Dict[SecretName, SecretValue]
    """Secret names and actual values to use when creating a credential."""

    type: typing.Literal["plaintext"] = "plaintext"


ProductId: typing_extensions.TypeAlias = core.UUID
"""ProductId"""


ProductSemanticVersion: typing_extensions.TypeAlias = str
"""The semantic version of a product, for example 1.2.3."""


class ProductVersion(core.ModelBase):
    """ProductVersion"""

    semantic_version: ProductSemanticVersion = pydantic.Field(alias=str("semanticVersion"))  # type: ignore[literal-required]
    version_id: ProductVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]


class ProductVersionById(core.ModelBase):
    """ProductVersionById"""

    version_id: ProductVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    type: typing.Literal["versionId"] = "versionId"


class ProductVersionBySemanticVersion(core.ModelBase):
    """ProductVersionBySemanticVersion"""

    version: ProductSemanticVersion
    """An exact major.minor.patch version, for example 1.2.3. Each component must be a non-negative integer without leading zeros. Version ranges, wildcards, prerelease identifiers, and build metadata are not supported."""

    type: typing.Literal["semanticVersion"] = "semanticVersion"


ProductVersionId: typing_extensions.TypeAlias = core.UUID
"""ProductVersionId"""


ProductVersionSelector: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["ProductVersionBySemanticVersion", "ProductVersionById"],
    pydantic.Field(discriminator="type"),
]
"""Select a product version by its UUID or an exact semantic version within the specified product and marketplace."""


RecommendationStrategy: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["RecommendationStrategyExplicit", "RecommendationStrategySameNamespace"],
    pydantic.Field(discriminator="type"),
]
"""Select other installations whose outputs may fulfill the target inputs. Recommendations are automatically applied when preparing an installation job."""


class RecommendationStrategyExplicit(core.ModelBase):
    """Consider the specified installations as input recommendations. The request token must be able to view each installation, and none may have a product targeted by the job."""

    installation_rids: typing.List[MarketplaceInstallationRid] = pydantic.Field(alias=str("installationRids"))  # type: ignore[literal-required]
    type: typing.Literal["explicit"] = "explicit"


class RecommendationStrategySameNamespace(core.ModelBase):
    """Consider visible installations outside the trash in the targets' namespace. Multiple matches for one linked product are ambiguous, even if only one has a compatible version."""

    suffix_filter: typing.Optional[str] = pydantic.Field(alias=str("suffixFilter"), default=None)  # type: ignore[literal-required]
    """Include only installations whose titles end with ` - ` followed by this suffix. The separator is added automatically. If omitted, do not filter by title."""

    type: typing.Literal["sameNamespace"] = "sameNamespace"


class RedactedCredentialSecrets(core.ModelBase):
    """Inspection data only. These names cannot be submitted as credentials for installation."""

    secret_names: typing.List[SecretName] = pydantic.Field(alias=str("secretNames"))  # type: ignore[literal-required]
    """Names of the secrets whose values have been withheld."""

    type: typing.Literal["redacted"] = "redacted"


class ReplayAcknowledgement(core.ModelBase):
    """ReplayAcknowledgement"""

    marketplace_upgrade_version: int = pydantic.Field(alias=str("marketplaceUpgradeVersion"))  # type: ignore[literal-required]
    """The installed pipeline's Marketplace upgrade version at the moment of acknowledgement."""


ResolvedInput: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ResolvedInputConnectionConfigurationOverrides",
        "ResolvedInputFunctionApiStability",
        "ResolvedInputGroup",
        "ResolvedInputInstallationPrefix",
        "ResolvedInputLibrary",
        "ResolvedInputOntologyDataSource",
        "ResolvedInputOntologyDataSourceRetention",
        "ResolvedInputOntologySchemaMigrationPolicy",
        "ResolvedInputOntologySchemaMigrationValues",
        "ResolvedInputPeerProducerProfile",
        "ResolvedInputPeerProfileRemoteStrategy",
        "ResolvedInputPipelineBuilderGeotimeConfiguration",
        "ResolvedInputPipelineBuilderParameter",
        "ResolvedInputPipelineBuilderReplayOption",
        "ResolvedInputStreamingSyncConfigurationOverrides",
        "ResolvedInputWorkshopSavedStateConfiguration",
    ],
    pydantic.Field(discriminator="type"),
]
"""A structured input value. Use the variant advertised by the input's `supportedTypes`. Prefer a direct scalar or resource reference when the input supports one."""


class ResolvedInputConnectionConfigurationOverrides(core.ModelBase):
    """ResolvedInputConnectionConfigurationOverrides"""

    config_overrides: typing.Dict[ConfigurationKey, ConfigurationValue] = pydantic.Field(alias=str("configOverrides"))  # type: ignore[literal-required]
    """Configuration overrides for a data connection source."""

    type: typing.Literal["connectionConfigurationOverrides"] = "connectionConfigurationOverrides"


class ResolvedInputFunctionApiStability(core.ModelBase):
    """ResolvedInputFunctionApiStability"""

    configuration: FunctionApiStability
    type: typing.Literal["functionApiStability"] = "functionApiStability"


class ResolvedInputGroup(core.ModelBase):
    """ResolvedInputGroup"""

    name: str
    realm: str
    type: typing.Literal["group"] = "group"


class ResolvedInputInstallationPrefix(core.ModelBase):
    """ResolvedInputInstallationPrefix"""

    prefix: str
    """A prefix for installed resources. Use an empty string for no prefix. Otherwise, use lowercase kebab-case containing only `a-z`, `0-9`, and hyphens, at most 16 characters, without a leading number."""

    prefix_configuration: typing.Optional[InstallationPrefixConfiguration] = pydantic.Field(alias=str("prefixConfiguration"), default=None)  # type: ignore[literal-required]
    """Controls prefixing of Ontology entity names. Defaults to `DISPLAY_NAME_AND_API_NAME` when omitted."""

    type: typing.Literal["installationPrefix"] = "installationPrefix"


class ResolvedInputLibrary(core.ModelBase):
    """ResolvedInputLibrary"""

    locator: LibraryLocator
    repository_rid: ResourceRid = pydantic.Field(alias=str("repositoryRid"))  # type: ignore[literal-required]
    """The artifacts repository containing the library."""

    type: typing.Literal["library"] = "library"


class ResolvedInputOntologyDataSource(core.ModelBase):
    """ResolvedInputOntologyDataSource"""

    data_source_rid: ResourceRid = pydantic.Field(alias=str("dataSourceRid"))  # type: ignore[literal-required]
    ontology_entity_rid: ResourceRid = pydantic.Field(alias=str("ontologyEntityRid"))  # type: ignore[literal-required]
    """The Ontology entity associated with the data source."""

    type: typing.Literal["ontologyDataSource"] = "ontologyDataSource"


class ResolvedInputOntologyDataSourceRetention(core.ModelBase):
    """Retention thresholds for a direct Ontology data source in an edge environment."""

    target_size_bytes: core.Long = pydantic.Field(alias=str("targetSizeBytes"))  # type: ignore[literal-required]
    """The size in bytes to retain after retention runs. Encoded as a decimal-integer string; must be between 0 and 9007199254740991, inclusive."""

    trigger_size_bytes: core.Long = pydantic.Field(alias=str("triggerSizeBytes"))  # type: ignore[literal-required]
    """The size in bytes that triggers retention. Encoded as a decimal-integer string; must be between 0 and 9007199254740991, inclusive."""

    type: typing.Literal["ontologyDataSourceRetention"] = "ontologyDataSourceRetention"


class ResolvedInputOntologySchemaMigrationPolicy(core.ModelBase):
    """Acknowledgements permitting automatic migrations of Ontology edits during installation or upgrade."""

    allow_cast_migrations: bool = pydantic.Field(alias=str("allowCastMigrations"))  # type: ignore[literal-required]
    """Allow casting property edits, or dropping those edits when a safe cast is unavailable."""

    allow_drop_migrations: bool = pydantic.Field(alias=str("allowDropMigrations"))  # type: ignore[literal-required]
    """Allow dropping property edits."""

    allow_permanently_delete_migrations: typing.Optional[bool] = pydantic.Field(alias=str("allowPermanentlyDeleteMigrations"), default=None)  # type: ignore[literal-required]
    """Allow permanently deleting all edits following a primary key change. Omission does not acknowledge this migration."""

    allow_rename_data_source_migrations: typing.Optional[bool] = pydantic.Field(alias=str("allowRenameDataSourceMigrations"), default=None)  # type: ignore[literal-required]
    """Allow moving data source edits. Omission does not acknowledge this migration."""

    allow_rename_property_migrations: typing.Optional[bool] = pydantic.Field(alias=str("allowRenamePropertyMigrations"), default=None)  # type: ignore[literal-required]
    """Allow moving property edits, or dropping them when the move cannot be applied. Omission does not acknowledge this migration."""

    type: typing.Literal["ontologySchemaMigrationPolicy"] = "ontologySchemaMigrationPolicy"


class ResolvedInputOntologySchemaMigrationValues(core.ModelBase):
    """ResolvedInputOntologySchemaMigrationValues"""

    migrations: typing.Dict[MigrationCandidateId, OntologySchemaMigrationValue]
    """Values for migration candidates requiring a literal during installation."""

    type: typing.Literal["ontologySchemaMigrationValues"] = "ontologySchemaMigrationValues"


class ResolvedInputPeerProducerProfile(core.ModelBase):
    """ResolvedInputPeerProducerProfile"""

    peer_producer_profile_rid: ResourceRid = pydantic.Field(alias=str("peerProducerProfileRid"))  # type: ignore[literal-required]
    peer_producer_uri: str = pydantic.Field(alias=str("peerProducerUri"))  # type: ignore[literal-required]
    """The producer's identifier for the kind of data it supports."""

    peer_profile_rid: ResourceRid = pydantic.Field(alias=str("peerProfileRid"))  # type: ignore[literal-required]
    """The peer profile to which the producer profile belongs."""

    type: typing.Literal["peerProducerProfile"] = "peerProducerProfile"


class ResolvedInputPeerProfileRemoteStrategy(core.ModelBase):
    """ResolvedInputPeerProfileRemoteStrategy"""

    strategy: PeerRemoteStrategy
    type: typing.Literal["peerProfileRemoteStrategy"] = "peerProfileRemoteStrategy"


class ResolvedInputPipelineBuilderGeotimeConfiguration(core.ModelBase):
    """Geotime destinations for an installed pipeline."""

    destinations: GeotimeDestinations
    observation_spec_id: typing.Optional[str] = pydantic.Field(alias=str("observationSpecId"), default=None)  # type: ignore[literal-required]
    source_system_spec_id: typing.Optional[str] = pydantic.Field(alias=str("sourceSystemSpecId"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["pipelineBuilderGeotimeConfiguration"] = (
        "pipelineBuilderGeotimeConfiguration"
    )


class ResolvedInputPipelineBuilderParameter(core.ModelBase):
    """A parameter value for a Pipeline Builder or edge pipeline input."""

    parameter: PipelineBuilderParameter
    type: typing.Literal["pipelineBuilderParameter"] = "pipelineBuilderParameter"


class ResolvedInputPipelineBuilderReplayOption(core.ModelBase):
    """ResolvedInputPipelineBuilderReplayOption"""

    replay_option: PipelineReplayOption = pydantic.Field(alias=str("replayOption"))  # type: ignore[literal-required]
    type: typing.Literal["pipelineBuilderReplayOption"] = "pipelineBuilderReplayOption"


class ResolvedInputStreamingSyncConfigurationOverrides(core.ModelBase):
    """ResolvedInputStreamingSyncConfigurationOverrides"""

    config_overrides: typing.Dict[ConfigurationKey, ConfigurationValue] = pydantic.Field(alias=str("configOverrides"))  # type: ignore[literal-required]
    """Configuration overrides for a streaming sync."""

    type: typing.Literal["streamingSyncConfigurationOverrides"] = (
        "streamingSyncConfigurationOverrides"
    )


ResolvedInputType: typing_extensions.TypeAlias = typing.Literal[
    "ONTOLOGY_SCHEMA_MIGRATION_POLICY",
    "LIBRARY",
    "PIPELINE_BUILDER_GEOTIME_CONFIGURATION",
    "PIPELINE_BUILDER_PARAMETER",
    "PIPELINE_BUILDER_REPLAY_OPTION",
    "FUNCTION_API_STABILITY",
    "INSTALLATION_PREFIX",
    "CONNECTION_CONFIGURATION_OVERRIDES",
    "STREAMING_SYNC_CONFIGURATION_OVERRIDES",
    "GROUP",
    "ONTOLOGY_DATA_SOURCE",
    "ONTOLOGY_DATA_SOURCE_RETENTION",
    "ONTOLOGY_SCHEMA_MIGRATION_VALUES",
    "PEER_PRODUCER_PROFILE",
    "PEER_PROFILE_REMOTE_STRATEGY",
    "WORKSHOP_SAVED_STATE_CONFIGURATION",
]
"""A structured representation supported by an input when a scalar or resource reference is insufficient."""


class ResolvedInputWorkshopSavedStateConfiguration(core.ModelBase):
    """ResolvedInputWorkshopSavedStateConfiguration"""

    enable_folder_selector: bool = pydantic.Field(alias=str("enableFolderSelector"))  # type: ignore[literal-required]
    enable_home_folder_saves: bool = pydantic.Field(alias=str("enableHomeFolderSaves"))  # type: ignore[literal-required]
    hide_inaccessible_locations: bool = pydantic.Field(alias=str("hideInaccessibleLocations"))  # type: ignore[literal-required]
    save_locations: typing.List[WorkshopSaveLocation] = pydantic.Field(alias=str("saveLocations"))  # type: ignore[literal-required]
    stable_identifier: StableIdentifier = pydantic.Field(alias=str("stableIdentifier"))  # type: ignore[literal-required]
    """The saved-state input's stable identifier from the product definition."""

    type: typing.Literal["workshopSavedStateConfiguration"] = "workshopSavedStateConfiguration"


ResourceRid: typing_extensions.TypeAlias = core.RID
"""A resource RID used in a structured input field with a known purpose."""


SecretName: typing_extensions.TypeAlias = str
"""The name of a secret required by a credential input."""


SecretValue: typing_extensions.TypeAlias = str
"""A credential secret supplied when configuring an installation job."""


SimpleInputType: typing_extensions.TypeAlias = typing.Literal[
    "RID",
    "RID_WITH_VERSION",
    "API_NAME",
    "STRING",
    "STRINGS",
    "BOOLEAN",
    "INTEGER",
    "CRON",
    "CREDENTIAL",
]
"""
A standard value representation supported by an input.

Values:
- **CREDENTIAL**: A mapping of secret names to secret values.
- **CRON**: A cron expression with a time zone.
"""


class SourceFilter(core.ModelBase):
    """Filters inputs by the sources that can fulfill them."""

    excluded_sources: typing.List[InputSource] = pydantic.Field(alias=str("excludedSources"))  # type: ignore[literal-required]
    """An empty list excludes no sources."""


StableIdentifier: typing_extensions.TypeAlias = str
"""The stable identifier assigned to an input in the product definition."""


SupportedInputType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["SupportedInputTypeResolved", "SupportedInputTypeSimple"],
    pydantic.Field(discriminator="type"),
]
"""An accepted representation for a supplied input value. Simple representations are preferred to structured resolved representations."""


class SupportedInputTypeResolved(core.ModelBase):
    """SupportedInputTypeResolved"""

    value_type: ResolvedInputType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["resolved"] = "resolved"


class SupportedInputTypeSimple(core.ModelBase):
    """SupportedInputTypeSimple"""

    value_type: SimpleInputType = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["simple"] = "simple"


TargetVersion: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["TargetVersionLatest", "ProductVersionBySemanticVersion", "ProductVersionById"],
    pydantic.Field(discriminator="type"),
]
"""Select the latest released version, an exact semantic version, or a version UUID within the installation's product and marketplace."""


class TargetVersionLatest(core.ModelBase):
    """Use the latest released version of the product when the request is evaluated. A later request may select a different version."""

    type: typing.Literal["latest"] = "latest"


class WorkshopSaveLocationFolder(core.ModelBase):
    """WorkshopSaveLocationFolder"""

    display_name_override: str = pydantic.Field(alias=str("displayNameOverride"))  # type: ignore[literal-required]
    """The display name for the folder shortcut."""

    folder_rid: core_models.FolderRid = pydantic.Field(alias=str("folderRid"))  # type: ignore[literal-required]
    type: typing.Literal["folder"] = "folder"


ErrorValue: typing_extensions.TypeAlias = ErrorDetails
"""The value describing an encountered error."""


OntologyPropertyValue: typing_extensions.TypeAlias = OntologyPropertyValueLiteral
"""OntologyPropertyValue"""


OntologySchemaMigrationValue: typing_extensions.TypeAlias = (
    OntologySchemaMigrationSetPropertyValueIfUnset
)
"""OntologySchemaMigrationValue"""


WorkshopSaveLocation: typing_extensions.TypeAlias = WorkshopSaveLocationFolder
"""WorkshopSaveLocation"""


core.resolve_forward_references_in_module(__name__)

__all__ = [
    "CondaPackageExtension",
    "ConfigurationKey",
    "ConfigurationValue",
    "CreateMarketplaceInstallationJobRequest",
    "CreateMarketplaceInstallationRequest",
    "CredentialSecrets",
    "CurrentInstallationInput",
    "DiscoverInstallationJobInputsRequest",
    "DiscoverInstallationJobInputsResponse",
    "DiscoveredInstallationInputs",
    "ErrorCode",
    "ErrorDetails",
    "ErrorName",
    "ErrorParameterName",
    "ErrorParameterValue",
    "ErrorSeverity",
    "ErrorTarget",
    "ErrorTargetInputsAndOutputs",
    "ErrorTargetInstallation",
    "ErrorTargetJob",
    "ErrorValue",
    "FunctionApiStability",
    "FunctionApiStabilityDeduplicate",
    "FunctionApiStabilityStable",
    "GeotimeDestination",
    "GeotimeDestinations",
    "InputApiName",
    "InputId",
    "InputMetadata",
    "InputReference",
    "InputSource",
    "InputType",
    "InputValue",
    "InputValueApiName",
    "InputValueBoolean",
    "InputValueCredential",
    "InputValueCron",
    "InputValueInteger",
    "InputValueResolved",
    "InputValueRid",
    "InputValueRidWithVersion",
    "InputValueString",
    "InputValueStrings",
    "InstallationError",
    "InstallationInputSelection",
    "InstallationJobDraftMode",
    "InstallationJobDraftPreparationFailure",
    "InstallationJobErrorHandling",
    "InstallationJobExecutionFailure",
    "InstallationJobFailure",
    "InstallationJobFailureStage",
    "InstallationJobInputs",
    "InstallationJobSubmissionMode",
    "InstallationJobSubmitMode",
    "InstallationJobTarget",
    "InstallationJobValidation",
    "InstallationJobValidationErrorTolerance",
    "InstallationJobValidationErrors",
    "InstallationJobValidationSummary",
    "InstallationOverrides",
    "InstallationPrefixConfiguration",
    "InstallationTarget",
    "InvalidInstallationInputReason",
    "LibraryLocator",
    "LibraryLocatorConda",
    "LibraryLocatorPath",
    "LocalGeotimeDestination",
    "MarketplaceInstallation",
    "MarketplaceInstallationInputs",
    "MarketplaceInstallationJob",
    "MarketplaceInstallationJobDetails",
    "MarketplaceInstallationJobRid",
    "MarketplaceInstallationJobStatus",
    "MarketplaceInstallationRid",
    "MarketplaceRid",
    "MigrationCandidateId",
    "OntologyLiteral",
    "OntologyLiteralArray",
    "OntologyLiteralBoolean",
    "OntologyLiteralByte",
    "OntologyLiteralDate",
    "OntologyLiteralDecimal",
    "OntologyLiteralDouble",
    "OntologyLiteralFloat",
    "OntologyLiteralGeohash",
    "OntologyLiteralInteger",
    "OntologyLiteralJson",
    "OntologyLiteralLong",
    "OntologyLiteralShort",
    "OntologyLiteralString",
    "OntologyLiteralTimestamp",
    "OntologyOverride",
    "OntologyOverrideRemove",
    "OntologyOverrideSet",
    "OntologyPropertyValue",
    "OntologyPropertyValueLiteral",
    "OntologySchemaMigrationSetPropertyValueIfUnset",
    "OntologySchemaMigrationValue",
    "OutputId",
    "OutputReference",
    "PeerRemoteStrategy",
    "PeerRemoteStrategyMeshId",
    "PeerRemoteStrategyMeshNodeLabel",
    "PeerRemoteStrategySpecificRemote",
    "PeeredGeotimeDestination",
    "PeeredGeotimeDestinations",
    "PipelineBuilderLiteral",
    "PipelineBuilderLiteralArray",
    "PipelineBuilderLiteralBinary",
    "PipelineBuilderLiteralBoolean",
    "PipelineBuilderLiteralDate",
    "PipelineBuilderLiteralDatetime",
    "PipelineBuilderLiteralDecimal",
    "PipelineBuilderLiteralDouble",
    "PipelineBuilderLiteralEmpty",
    "PipelineBuilderLiteralInteger",
    "PipelineBuilderLiteralJson",
    "PipelineBuilderLiteralLong",
    "PipelineBuilderLiteralMap",
    "PipelineBuilderLiteralMapEntry",
    "PipelineBuilderLiteralString",
    "PipelineBuilderParameter",
    "PipelineBuilderParameterEnum",
    "PipelineBuilderParameterLiteral",
    "PipelineBuilderParameterRegex",
    "PipelineReplayOption",
    "PipelineReplayOptionAcknowledgeStateBreaks",
    "PipelineReplayOptionReset",
    "PipelineReplayOptionResetAndReplayFromOffset",
    "PlaintextCredentialSecrets",
    "ProductId",
    "ProductSemanticVersion",
    "ProductVersion",
    "ProductVersionById",
    "ProductVersionBySemanticVersion",
    "ProductVersionId",
    "ProductVersionSelector",
    "RecommendationStrategy",
    "RecommendationStrategyExplicit",
    "RecommendationStrategySameNamespace",
    "RedactedCredentialSecrets",
    "ReplayAcknowledgement",
    "ResolvedInput",
    "ResolvedInputConnectionConfigurationOverrides",
    "ResolvedInputFunctionApiStability",
    "ResolvedInputGroup",
    "ResolvedInputInstallationPrefix",
    "ResolvedInputLibrary",
    "ResolvedInputOntologyDataSource",
    "ResolvedInputOntologyDataSourceRetention",
    "ResolvedInputOntologySchemaMigrationPolicy",
    "ResolvedInputOntologySchemaMigrationValues",
    "ResolvedInputPeerProducerProfile",
    "ResolvedInputPeerProfileRemoteStrategy",
    "ResolvedInputPipelineBuilderGeotimeConfiguration",
    "ResolvedInputPipelineBuilderParameter",
    "ResolvedInputPipelineBuilderReplayOption",
    "ResolvedInputStreamingSyncConfigurationOverrides",
    "ResolvedInputType",
    "ResolvedInputWorkshopSavedStateConfiguration",
    "ResourceRid",
    "SecretName",
    "SecretValue",
    "SimpleInputType",
    "SourceFilter",
    "StableIdentifier",
    "SupportedInputType",
    "SupportedInputTypeResolved",
    "SupportedInputTypeSimple",
    "TargetVersion",
    "TargetVersionLatest",
    "WorkshopSaveLocation",
    "WorkshopSaveLocationFolder",
]
