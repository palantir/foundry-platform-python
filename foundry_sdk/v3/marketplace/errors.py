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
from dataclasses import dataclass

import typing_extensions

from foundry_sdk import _errors as errors
from foundry_sdk.v3.core import models as core_models
from foundry_sdk.v3.marketplace import models as marketplace_models


class AbortInstallationJobPermissionDeniedParameters(typing_extensions.TypedDict):
    """The installation job is visible to the request token, but the request token does not have permission to abort it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationJobRid: marketplace_models.MarketplaceInstallationJobRid


@dataclass
class AbortInstallationJobPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["AbortInstallationJobPermissionDenied"]
    parameters: AbortInstallationJobPermissionDeniedParameters
    error_instance_id: str


class AmbiguousInstallationRecommendationParameters(typing_extensions.TypedDict):
    """A namespace recommendation strategy matches multiple installations of the same linked product. Narrow its suffix filter or use explicit recommendations. Overlapping recommendation inputs or sources are reported separately as `InstallationError` entries in the discovery response."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    productId: marketplace_models.ProductId
    installationRids: typing.List[marketplace_models.MarketplaceInstallationRid]


@dataclass
class AmbiguousInstallationRecommendation(errors.BadRequestError):
    name: typing.Literal["AmbiguousInstallationRecommendation"]
    parameters: AmbiguousInstallationRecommendationParameters
    error_instance_id: str


class ConflictingInstallationInputIntentParameters(typing_extensions.TypedDict):
    """An input name occurs more than once in `explicitlyUnset` or occurs in both `values` and `explicitlyUnset` for the same installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRid: marketplace_models.MarketplaceInstallationRid
    apiName: marketplace_models.InputApiName


@dataclass
class ConflictingInstallationInputIntent(errors.BadRequestError):
    name: typing.Literal["ConflictingInstallationInputIntent"]
    parameters: ConflictingInstallationInputIntentParameters
    error_instance_id: str


class ConflictingInstallationJobParameters(typing_extensions.TypedDict):
    """An installation targeted for submission already has a running job. Draft mode may still prepare a draft."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRids: typing.List[marketplace_models.MarketplaceInstallationRid]


@dataclass
class ConflictingInstallationJob(errors.ConflictError):
    name: typing.Literal["ConflictingInstallationJob"]
    parameters: ConflictingInstallationJobParameters
    error_instance_id: str


class ConflictingInstallationRecommendationParameters(typing_extensions.TypedDict):
    """A recommendation supplies a product that is also included in the requested targets. Remove that recommendation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    recommendationInstallationRid: marketplace_models.MarketplaceInstallationRid
    requestedInstallationRid: marketplace_models.MarketplaceInstallationRid


@dataclass
class ConflictingInstallationRecommendation(errors.BadRequestError):
    name: typing.Literal["ConflictingInstallationRecommendation"]
    parameters: ConflictingInstallationRecommendationParameters
    error_instance_id: str


class CreateInstallationJobPermissionDeniedParameters(typing_extensions.TypedDict):
    """The request token cannot prepare or submit a job for one or more target installations or dependencies."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRids: typing.List[marketplace_models.MarketplaceInstallationRid]


@dataclass
class CreateInstallationJobPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateInstallationJobPermissionDenied"]
    parameters: CreateInstallationJobPermissionDeniedParameters
    error_instance_id: str


class CreateMarketplaceInstallationPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not register the installation due to insufficient permissions on the marketplace, product, or destination project or folder."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    marketplaceRid: marketplace_models.MarketplaceRid
    productId: marketplace_models.ProductId
    parentFolderRid: core_models.FolderRid


@dataclass
class CreateMarketplaceInstallationPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["CreateMarketplaceInstallationPermissionDenied"]
    parameters: CreateMarketplaceInstallationPermissionDeniedParameters
    error_instance_id: str


class DiscoverInstallationJobInputsFailedParameters(typing_extensions.TypedDict):
    """Marketplace could not complete input discovery."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    errorName: marketplace_models.ErrorName
    """The name of the underlying error that prevented input discovery."""

    errorCode: marketplace_models.ErrorCode
    """The code of the underlying error that prevented input discovery."""


@dataclass
class DiscoverInstallationJobInputsFailed(errors.InternalServerError):
    name: typing.Literal["DiscoverInstallationJobInputsFailed"]
    parameters: DiscoverInstallationJobInputsFailedParameters
    error_instance_id: str


class DiscoverInstallationJobInputsPermissionDeniedParameters(typing_extensions.TypedDict):
    """The request token does not have permission to edit one or more target installations and cannot discover their inputs."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRids: typing.List[marketplace_models.MarketplaceInstallationRid]


@dataclass
class DiscoverInstallationJobInputsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["DiscoverInstallationJobInputsPermissionDenied"]
    parameters: DiscoverInstallationJobInputsPermissionDeniedParameters
    error_instance_id: str


class DuplicateInstallationJobInstallationsParameters(typing_extensions.TypedDict):
    """An installation occurs more than once in the target list."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRids: typing.List[marketplace_models.MarketplaceInstallationRid]


@dataclass
class DuplicateInstallationJobInstallations(errors.BadRequestError):
    name: typing.Literal["DuplicateInstallationJobInstallations"]
    parameters: DuplicateInstallationJobInstallationsParameters
    error_instance_id: str


class DuplicateInstallationJobProductsParameters(typing_extensions.TypedDict):
    """More than one target installation uses the same product."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    productId: marketplace_models.ProductId
    installationRids: typing.List[marketplace_models.MarketplaceInstallationRid]


@dataclass
class DuplicateInstallationJobProducts(errors.BadRequestError):
    name: typing.Literal["DuplicateInstallationJobProducts"]
    parameters: DuplicateInstallationJobProductsParameters
    error_instance_id: str


class GetMarketplaceInstallationInputsPermissionDeniedParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    marketplaceInstallationRid: marketplace_models.MarketplaceInstallationRid


@dataclass
class GetMarketplaceInstallationInputsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetMarketplaceInstallationInputsPermissionDenied"]
    parameters: GetMarketplaceInstallationInputsPermissionDeniedParameters
    error_instance_id: str


class GetMarketplaceInstallationJobDetailsPermissionDeniedParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    marketplaceInstallationJobRid: marketplace_models.MarketplaceInstallationJobRid


@dataclass
class GetMarketplaceInstallationJobDetailsPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["GetMarketplaceInstallationJobDetailsPermissionDenied"]
    parameters: GetMarketplaceInstallationJobDetailsPermissionDeniedParameters
    error_instance_id: str


class InstallationDraftAlreadyExistsParameters(typing_extensions.TypedDict):
    """The caller already has a preparing or idle draft for a target installation. Complete or abort the existing draft before preparing another job or discovering inputs for that installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRid: marketplace_models.MarketplaceInstallationRid
    existingInstallationJobRid: marketplace_models.MarketplaceInstallationJobRid


@dataclass
class InstallationDraftAlreadyExists(errors.ConflictError):
    name: typing.Literal["InstallationDraftAlreadyExists"]
    parameters: InstallationDraftAlreadyExistsParameters
    error_instance_id: str


class InstallationInputApiNamesNotEnabledParameters(typing_extensions.TypedDict):
    """One or more installations have product inputs without API names. Enable input API name generation for those products before interacting with them."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRids: typing.List[marketplace_models.MarketplaceInstallationRid]


@dataclass
class InstallationInputApiNamesNotEnabled(errors.BadRequestError):
    name: typing.Literal["InstallationInputApiNamesNotEnabled"]
    parameters: InstallationInputApiNamesNotEnabledParameters
    error_instance_id: str


class InstallationInputNotFoundParameters(typing_extensions.TypedDict):
    """An input API name is not present in the selected product version."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRid: marketplace_models.MarketplaceInstallationRid
    apiName: marketplace_models.InputApiName


@dataclass
class InstallationInputNotFound(errors.BadRequestError):
    name: typing.Literal["InstallationInputNotFound"]
    parameters: InstallationInputNotFoundParameters
    error_instance_id: str


class InstallationJobMarketplaceConstraintViolatedParameters(typing_extensions.TypedDict):
    """The target products must belong to a single marketplace."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRids: typing.List[marketplace_models.MarketplaceInstallationRid]


@dataclass
class InstallationJobMarketplaceConstraintViolated(errors.BadRequestError):
    name: typing.Literal["InstallationJobMarketplaceConstraintViolated"]
    parameters: InstallationJobMarketplaceConstraintViolatedParameters
    error_instance_id: str


class InstallationJobNamespaceConstraintViolatedParameters(typing_extensions.TypedDict):
    """The target installations must belong to a single namespace."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRids: typing.List[marketplace_models.MarketplaceInstallationRid]


@dataclass
class InstallationJobNamespaceConstraintViolated(errors.BadRequestError):
    name: typing.Literal["InstallationJobNamespaceConstraintViolated"]
    parameters: InstallationJobNamespaceConstraintViolatedParameters
    error_instance_id: str


class InstallationJobOntologyConstraintViolatedParameters(typing_extensions.TypedDict):
    """The target installations must have at most one resulting ontology after applying location overrides."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRids: typing.List[marketplace_models.MarketplaceInstallationRid]


@dataclass
class InstallationJobOntologyConstraintViolated(errors.BadRequestError):
    name: typing.Literal["InstallationJobOntologyConstraintViolated"]
    parameters: InstallationJobOntologyConstraintViolatedParameters
    error_instance_id: str


class InstallationTargetVersionNotFoundParameters(typing_extensions.TypedDict):
    """The requested target version could not be found within the installation product and marketplace."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRid: marketplace_models.MarketplaceInstallationRid
    targetVersion: marketplace_models.TargetVersion


@dataclass
class InstallationTargetVersionNotFound(errors.NotFoundError):
    name: typing.Literal["InstallationTargetVersionNotFound"]
    parameters: InstallationTargetVersionNotFoundParameters
    error_instance_id: str


class InstallationUninstallStartedParameters(typing_extensions.TypedDict):
    """Uninstall has begun for the target installation. Create a new installation to install the product again."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRid: marketplace_models.MarketplaceInstallationRid


@dataclass
class InstallationUninstallStarted(errors.ConflictError):
    name: typing.Literal["InstallationUninstallStarted"]
    parameters: InstallationUninstallStartedParameters
    error_instance_id: str


class InvalidInstallationInputParameters(typing_extensions.TypedDict):
    """An input value could not be converted for the selected product version. The error reason does not contain the supplied value."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRid: marketplace_models.MarketplaceInstallationRid
    apiName: marketplace_models.InputApiName
    reason: marketplace_models.InvalidInstallationInputReason


@dataclass
class InvalidInstallationInput(errors.BadRequestError):
    name: typing.Literal["InvalidInstallationInput"]
    parameters: InvalidInstallationInputParameters
    error_instance_id: str


class InvalidInstallationTargetVersionParameters(typing_extensions.TypedDict):
    """The target semantic version must be an exact major.minor.patch version with non-negative integer components and no leading zeros. Each component must be at most 2⁵³ - 2 (9,007,199,254,740,990). Version ranges, wildcards, prerelease identifiers, and build metadata are not supported."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    version: marketplace_models.ProductSemanticVersion


@dataclass
class InvalidInstallationTargetVersion(errors.BadRequestError):
    name: typing.Literal["InvalidInstallationTargetVersion"]
    parameters: InvalidInstallationTargetVersionParameters
    error_instance_id: str


class InvalidInstallationTargetVersionHintParameters(typing_extensions.TypedDict):
    """The semantic version in the hint must be an exact major.minor.patch version with non-negative integer components and no leading zeros. Version ranges, wildcards, prerelease identifiers, and build metadata are not supported."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    targetVersionHint: marketplace_models.ProductSemanticVersion


@dataclass
class InvalidInstallationTargetVersionHint(errors.BadRequestError):
    name: typing.Literal["InvalidInstallationTargetVersionHint"]
    parameters: InvalidInstallationTargetVersionHintParameters
    error_instance_id: str


class MarketplaceInstallationJobNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    marketplaceInstallationJobRid: marketplace_models.MarketplaceInstallationJobRid


@dataclass
class MarketplaceInstallationJobNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceInstallationJobNotFound"]
    parameters: MarketplaceInstallationJobNotFoundParameters
    error_instance_id: str


class MarketplaceInstallationNotFoundParameters(typing_extensions.TypedDict):

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    marketplaceInstallationRid: marketplace_models.MarketplaceInstallationRid


@dataclass
class MarketplaceInstallationNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceInstallationNotFound"]
    parameters: MarketplaceInstallationNotFoundParameters
    error_instance_id: str


class MarketplaceProductNotFoundParameters(typing_extensions.TypedDict):
    """The product could not be found in the specified marketplace or has no released version available for registration."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    marketplaceRid: marketplace_models.MarketplaceRid
    productId: marketplace_models.ProductId


@dataclass
class MarketplaceProductNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceProductNotFound"]
    parameters: MarketplaceProductNotFoundParameters
    error_instance_id: str


class MarketplaceProductVersionNotFoundParameters(typing_extensions.TypedDict):
    """The hinted product version could not be found in the specified product and marketplace."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    marketplaceRid: marketplace_models.MarketplaceRid
    productId: marketplace_models.ProductId
    targetVersionHint: marketplace_models.ProductVersionSelector


@dataclass
class MarketplaceProductVersionNotFound(errors.NotFoundError):
    name: typing.Literal["MarketplaceProductVersionNotFound"]
    parameters: MarketplaceProductVersionNotFoundParameters
    error_instance_id: str


class MaxInstallationJobInstallationsCountExceededParameters(typing_extensions.TypedDict):
    """The number of installation targets exceeds the maximum supported by this operation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationsCount: int
    maxInstallationsCount: int


@dataclass
class MaxInstallationJobInstallationsCountExceeded(errors.BadRequestError):
    name: typing.Literal["MaxInstallationJobInstallationsCountExceeded"]
    parameters: MaxInstallationJobInstallationsCountExceededParameters
    error_instance_id: str


class MissingInstallationInputParentValueParameters(typing_extensions.TypedDict):
    """A child input with a value requires its parent to have a value in `inputs.values` for the same installation."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    installationRid: marketplace_models.MarketplaceInstallationRid
    childApiName: marketplace_models.InputApiName
    parentApiName: marketplace_models.InputApiName


@dataclass
class MissingInstallationInputParentValue(errors.BadRequestError):
    name: typing.Literal["MissingInstallationInputParentValue"]
    parameters: MissingInstallationInputParentValueParameters
    error_instance_id: str


class MissingInstallationJobInstallationsParameters(typing_extensions.TypedDict):
    """At least one installation target must be supplied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class MissingInstallationJobInstallations(errors.BadRequestError):
    name: typing.Literal["MissingInstallationJobInstallations"]
    parameters: MissingInstallationJobInstallationsParameters
    error_instance_id: str


class ParentFolderNotFoundParameters(typing_extensions.TypedDict):
    """The destination project or folder could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parentFolderRid: core_models.FolderRid


@dataclass
class ParentFolderNotFound(errors.NotFoundError):
    name: typing.Literal["ParentFolderNotFound"]
    parameters: ParentFolderNotFoundParameters
    error_instance_id: str


class SingletonMarketplaceInstallationAlreadyExistsParameters(typing_extensions.TypedDict):
    """Another installation of this product already exists in the destination namespace, and the product version used for registration requires a single installation per namespace."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    productId: marketplace_models.ProductId
    namespaceRid: core_models.NamespaceRid


@dataclass
class SingletonMarketplaceInstallationAlreadyExists(errors.ConflictError):
    name: typing.Literal["SingletonMarketplaceInstallationAlreadyExists"]
    parameters: SingletonMarketplaceInstallationAlreadyExistsParameters
    error_instance_id: str


__all__ = [
    "AbortInstallationJobPermissionDenied",
    "AmbiguousInstallationRecommendation",
    "ConflictingInstallationInputIntent",
    "ConflictingInstallationJob",
    "ConflictingInstallationRecommendation",
    "CreateInstallationJobPermissionDenied",
    "CreateMarketplaceInstallationPermissionDenied",
    "DiscoverInstallationJobInputsFailed",
    "DiscoverInstallationJobInputsPermissionDenied",
    "DuplicateInstallationJobInstallations",
    "DuplicateInstallationJobProducts",
    "GetMarketplaceInstallationInputsPermissionDenied",
    "GetMarketplaceInstallationJobDetailsPermissionDenied",
    "InstallationDraftAlreadyExists",
    "InstallationInputApiNamesNotEnabled",
    "InstallationInputNotFound",
    "InstallationJobMarketplaceConstraintViolated",
    "InstallationJobNamespaceConstraintViolated",
    "InstallationJobOntologyConstraintViolated",
    "InstallationTargetVersionNotFound",
    "InstallationUninstallStarted",
    "InvalidInstallationInput",
    "InvalidInstallationTargetVersion",
    "InvalidInstallationTargetVersionHint",
    "MarketplaceInstallationJobNotFound",
    "MarketplaceInstallationNotFound",
    "MarketplaceProductNotFound",
    "MarketplaceProductVersionNotFound",
    "MaxInstallationJobInstallationsCountExceeded",
    "MissingInstallationInputParentValue",
    "MissingInstallationJobInstallations",
    "ParentFolderNotFound",
    "SingletonMarketplaceInstallationAlreadyExists",
]
