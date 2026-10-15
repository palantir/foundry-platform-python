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

AdditionalField: typing_extensions.TypeAlias = typing.Literal[
    "CONTACT_INFORMATION",
    "DEFAULT_BRANCH",
    "DESCRIPTION",
    "DOCUMENTATION",
    "NAMED_ANCESTORS",
    "PATH",
    "SPACE_RID",
    "TRASH_STATUS",
]
"""An optional field that can be requested for a resource."""


class AdditionalFields(core.ModelBase):
    """
    Optional properties of a resource. An additional field is returned if and only if it was explicitly
    requested by the caller.
    """

    contact_information: typing.Optional[ContactInformationField] = pydantic.Field(alias=str("contactInformation"), default=None)  # type: ignore[literal-required]
    """Empty if the `CONTACT_INFORMATION` additional field was not requested."""

    default_branch: typing.Optional[DefaultBranchField] = pydantic.Field(alias=str("defaultBranch"), default=None)  # type: ignore[literal-required]
    """Empty if the `DEFAULT_BRANCH` additional field was not requested."""

    description: typing.Optional[DescriptionField] = None
    """Empty if the `DESCRIPTION` additional field was not requested."""

    documentation: typing.Optional[DocumentationField] = None
    """Empty if the `DOCUMENTATION` additional field was not requested."""

    named_ancestors: typing.Optional[NamedAncestorsField] = pydantic.Field(alias=str("namedAncestors"), default=None)  # type: ignore[literal-required]
    """Empty if the `NAMED_ANCESTORS` additional field was not requested."""

    path: typing.Optional[PathField] = None
    """Empty if the `PATH` additional field was not requested."""

    space_rid: typing.Optional[SpaceRidField] = pydantic.Field(alias=str("spaceRid"), default=None)  # type: ignore[literal-required]
    """Empty if the `SPACE_RID` additional field was not requested."""

    trash_status: typing.Optional[TrashStatusField] = pydantic.Field(alias=str("trashStatus"), default=None)  # type: ignore[literal-required]
    """Empty if the `TRASH_STATUS` additional field was not requested."""


class Branch(core.ModelBase):
    """An independently addressable version of a resource."""

    name: BranchName
    """The name of the branch."""

    rid: BranchRid
    """The RID of the branch."""


BranchName: typing_extensions.TypeAlias = str
"""The name of a branch."""


BranchRid: typing_extensions.TypeAlias = core.RID
"""The unique resource identifier (RID) of a branch."""


class Contact(core.ModelBase):
    """Contact"""

    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]


class ContactInformation(core.ModelBase):
    """The principals to contact with questions about a resource."""

    primary_contact: Contact = pydantic.Field(alias=str("primaryContact"))  # type: ignore[literal-required]


class ContactInformationField(core.ModelBase):
    """Holds the contacts of a resource, if any are configured."""

    value: typing.Optional[ContactInformation] = None
    """
    The contacts for the resource. Empty if no contacts are configured, or the caller does not have
    permission to view them.
    """


class CreateFolderRequest(core.ModelBase):
    """CreateFolderRequest"""

    display_name: DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the folder."""

    parent_folder_rid: core_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    """The RID of the existing project or folder in which to create the new folder. The parent must be inside a project."""


class DefaultBranchField(core.ModelBase):
    """Holds the default branch of a resource, if it can be branched."""

    value: typing.Optional[Branch] = None
    """The default branch of the resource. Empty if no default branch is configured."""


class DeleteFoldersBatchRequestElement(core.ModelBase):
    """DeleteFoldersBatchRequestElement"""

    rid: core_models.FolderRid


class DeleteProjectsBatchRequestElement(core.ModelBase):
    """DeleteProjectsBatchRequestElement"""

    rid: ProjectRid


class DeleteResourcesBatchRequestElement(core.ModelBase):
    """DeleteResourcesBatchRequestElement"""

    rid: ResourceRid


class DeleteSpacesBatchRequestElement(core.ModelBase):
    """DeleteSpacesBatchRequestElement"""

    rid: SpaceRid


class DescriptionField(core.ModelBase):
    """Holds the short description of a resource, if it has one."""

    value: typing.Optional[str] = None
    """The description of the resource. Empty if no description is configured."""


DisplayName: typing_extensions.TypeAlias = str
"""The display name of a resource."""


class DocumentationField(core.ModelBase):
    """Holds the long-form documentation of a resource, if it has any."""

    value: typing.Optional[str] = None
    """
    The documentation associated with the resource. Empty if no documentation is configured,
    or the caller does not have permission to view it.
    """


FileSystemId: typing_extensions.TypeAlias = str
"""The ID of a filesystem."""


class Folder(core.ModelBase):
    """A Foundry folder within a project."""

    additional_fields: AdditionalFields = pydantic.Field(alias=str("additionalFields"))  # type: ignore[literal-required]
    """Optional properties. Only the additional fields explicitly requested by the caller are populated."""

    created_time: typing.Optional[core_models.CreatedTime] = pydantic.Field(alias=str("createdTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the folder was created. This field may be absent for legacy folders."""

    created_user_id: typing.Optional[UserId] = pydantic.Field(alias=str("createdUserId"), default=None)  # type: ignore[literal-required]
    """The ID of the user that created the folder. This field may be absent for legacy folders."""

    display_name: DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the folder."""

    rid: core_models.FolderRid
    updated_time: typing.Optional[core_models.UpdatedTime] = pydantic.Field(alias=str("updatedTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the folder was last modified. This field may be absent for legacy folders."""

    updated_user_id: typing.Optional[UserId] = pydantic.Field(alias=str("updatedUserId"), default=None)  # type: ignore[literal-required]
    """The ID of the user that last modified the folder. This field may be absent for legacy folders."""

    type: typing.Literal["value"] = "value"


FolderBatchResult: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["FolderNotFoundError", "Folder"], pydantic.Field(discriminator="type")
]
"""FolderBatchResult"""


class FolderNotFoundError(core.ModelBase):
    """FolderNotFoundError"""

    rid: core_models.FolderRid
    type: typing.Literal["notFound"] = "notFound"


class GetFoldersBatchRequestElement(core.ModelBase):
    """GetFoldersBatchRequestElement"""

    include: typing.List[AdditionalField]
    """The additional fields to include in the response `additionalFields` field."""

    rid: core_models.FolderRid


class GetFoldersBatchResponse(core.ModelBase):
    """GetFoldersBatchResponse"""

    data: typing.List[FolderBatchResult]


class GetProjectsBatchRequestElement(core.ModelBase):
    """GetProjectsBatchRequestElement"""

    rid: ProjectRid


class GetProjectsBatchResponse(core.ModelBase):
    """GetProjectsBatchResponse"""

    data: typing.List[ProjectBatchResult]


class GetResourcesBatchRequestElement(core.ModelBase):
    """GetResourcesBatchRequestElement"""

    include: typing.List[AdditionalField]
    """The additional fields to include in the response `additionalFields` field."""

    rid: ResourceRid


class GetResourcesBatchResponse(core.ModelBase):
    """GetResourcesBatchResponse"""

    data: typing.List[ResourceBatchResult]


class GetSpacesBatchRequestElement(core.ModelBase):
    """GetSpacesBatchRequestElement"""

    rid: SpaceRid


class GetSpacesBatchResponse(core.ModelBase):
    """GetSpacesBatchResponse"""

    data: typing.List[SpaceBatchResult]


class ListSpacesResponse(core.ModelBase):
    """ListSpacesResponse"""

    data: typing.List[Space]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


MavenIdentifier: typing_extensions.TypeAlias = str
"""The prefix of the Maven coordinate that uniquely identifies resources published from a space."""


class NamedAncestorsField(core.ModelBase):
    """Holds the chain of ancestors of a resource, from the root resource down to the resource itself."""

    value: typing.List[NamedResourceIdentifier]
    """
    The RIDs and names of all ancestors of the resource, starting from and including the root resource, and
    ending at and including the resource itself.
    """


class NamedResourceIdentifier(core.ModelBase):
    """A representation of a resource containing a resource identifier and a name."""

    name: str
    """Human-readable name."""

    rid: ResourceRid
    """RID of the resource."""


OrganizationRid: typing_extensions.TypeAlias = core.RID
"""The unique resource identifier (RID) of an organization."""


class PathField(core.ModelBase):
    """Holds the location of a resource in the filesystem hierarchy."""

    value: ResourcePath
    """The full path to the resource, including the resource name itself."""


class Project(core.ModelBase):
    """A Foundry project."""

    created_time: typing.Optional[core_models.CreatedTime] = pydantic.Field(alias=str("createdTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the project was created. This field may be absent for legacy projects."""

    created_user_id: typing.Optional[UserId] = pydantic.Field(alias=str("createdUserId"), default=None)  # type: ignore[literal-required]
    """The ID of the user that created the project. This field may be absent for legacy projects."""

    description: typing.Optional[str] = None
    """The description of the project. Empty if no description is configured."""

    display_name: DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the project. Must be unique and cannot contain a `/`."""

    documentation: typing.Optional[str] = None
    """
    The long-form, markdown-formatted documentation of the project. Empty if no documentation is configured,
    or the caller does not have permission to view it.
    """

    path: ResourcePath
    """The full path to the project, including the project name itself."""

    resource_level_role_grants_allowed: bool = pydantic.Field(alias=str("resourceLevelRoleGrantsAllowed"))  # type: ignore[literal-required]
    """Whether role grants are allowed on individual resources within the project."""

    rid: ProjectRid
    space_rid: SpaceRid = pydantic.Field(alias=str("spaceRid"))  # type: ignore[literal-required]
    """The RID of the space that contains the project."""

    trash_status: TrashStatus = pydantic.Field(alias=str("trashStatus"))  # type: ignore[literal-required]
    """The trash status of the project."""

    updated_time: typing.Optional[core_models.UpdatedTime] = pydantic.Field(alias=str("updatedTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the project was last modified. This field may be absent for legacy projects."""

    updated_user_id: typing.Optional[UserId] = pydantic.Field(alias=str("updatedUserId"), default=None)  # type: ignore[literal-required]
    """The ID of the user that last modified the project. This field may be absent for legacy projects."""

    type: typing.Literal["value"] = "value"


ProjectBatchResult: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["ProjectNotFoundError", "Project"], pydantic.Field(discriminator="type")
]
"""ProjectBatchResult"""


class ProjectNotFoundError(core.ModelBase):
    """ProjectNotFoundError"""

    rid: ProjectRid
    type: typing.Literal["notFound"] = "notFound"


ProjectRid: typing_extensions.TypeAlias = core.RID
"""The unique resource identifier (RID) of a project."""


class Resource(core.ModelBase):
    """A Foundry resource."""

    additional_fields: AdditionalFields = pydantic.Field(alias=str("additionalFields"))  # type: ignore[literal-required]
    """Optional properties. Only the additional fields explicitly requested by the caller are populated."""

    created_time: typing.Optional[core_models.CreatedTime] = pydantic.Field(alias=str("createdTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the resource was created. This field may be absent for legacy resources."""

    created_user_id: typing.Optional[UserId] = pydantic.Field(alias=str("createdUserId"), default=None)  # type: ignore[literal-required]
    """The ID of the user that created the resource. This field may be absent for legacy resources."""

    display_name: DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the resource."""

    resource_type: ResourceType = pydantic.Field(alias=str("resourceType"))  # type: ignore[literal-required]
    """The type of the resource."""

    rid: ResourceRid
    updated_time: typing.Optional[core_models.UpdatedTime] = pydantic.Field(alias=str("updatedTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the resource was last modified. This field may be absent for legacy resources."""

    updated_user_id: typing.Optional[UserId] = pydantic.Field(alias=str("updatedUserId"), default=None)  # type: ignore[literal-required]
    """The ID of the user that last modified the resource. This field may be absent for legacy resources."""

    type: typing.Literal["value"] = "value"


ResourceBatchResult: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["ResourceNotFoundError", "Resource"], pydantic.Field(discriminator="type")
]
"""ResourceBatchResult"""


class ResourceNotFoundError(core.ModelBase):
    """ResourceNotFoundError"""

    rid: ResourceRid
    type: typing.Literal["notFound"] = "notFound"


ResourcePath: typing_extensions.TypeAlias = str
"""The full path to a resource, including the resource name itself."""


ResourceRid: typing_extensions.TypeAlias = core.RID
"""The unique resource identifier (RID) of a resource."""


ResourceType: typing_extensions.TypeAlias = typing.Literal[
    "FOLDER",
    "SPACE",
    "PROJECT",
    "ACTIONS_ACTION_TYPE",
    "AGENT_BUILDER_AGENT",
    "AGENT_ENGINE_AGENT_DEFINITION",
    "AIP_AGENTS_AGENT",
    "AIP_AGENTS_SESSION",
    "AIP_AGENTS_SKILL",
    "AIP_ANALYST_ANALYSIS",
    "AIP_ASSIST_FLOW_CAPTURE",
    "AIP_ASSIST_WALKTHROUGH",
    "AIP_PROFILE",
    "ARROW_TEMPLATE",
    "ARTIFACTS_REPOSITORY",
    "AUDITEXPORT_ARTIFACTS",
    "AUDIT_EXPORT_ORGANIZATION",
    "AUTOTRAIN_DATASET",
    "AUTOTRAIN_TRAINING_SESSION",
    "BELLASO_CIPHER_CHANNEL",
    "BELLASO_CIPHER_LICENSE",
    "BLACKSMITH_DOCUMENT",
    "BLOBSTER_ARCHIVE",
    "BLOBSTER_AUDIO",
    "BLOBSTER_BLOB",
    "BLOBSTER_CERTIFICATE",
    "BLOBSTER_CERTIFICATE_STORE",
    "BLOBSTER_CODE",
    "BLOBSTER_CONFIGURATION",
    "BLOBSTER_DOCUMENT",
    "BLOBSTER_EXECUTABLE",
    "BLOBSTER_IMAGE",
    "BLOBSTER_JUPYTERNOTEBOOK",
    "BLOBSTER_LOG",
    "BLOBSTER_PDF",
    "BLOBSTER_PRESENTATION",
    "BLOBSTER_SPREADSHEET",
    "BLOBSTER_VIDEO",
    "BLOBSTER_XML",
    "CARBON_WORKSPACE",
    "CHRONOGRAPH_TIMELINE",
    "CODE_ENVIRONMENT_REGISTRY_ENVIRONMENT",
    "COMPASS_WEB_LINK",
    "CONTOUR_ANALYSIS",
    "CREDENTIAL_CREDENTIAL",
    "DATA_HEALTH_MONITORING_VIEW",
    "DECISIONS_EXPLORATION",
    "DREDDIE_PIPELINE",
    "EDDIE_LIBRARY",
    "EDDIE_LOGIC",
    "EDDIE_PIPELINE",
    "EDGE_PIPELINES_MANAGER_EDGE_PIPELINE",
    "EVALS_EVALUATION_SUITE",
    "FFORMS_FORM",
    "FLOW_WORKFLOW",
    "FLOW_WORKFLOW_EDIT",
    "FOUNDRY_ACADEMY_TUTORIAL",
    "FOUNDRY_CONTAINER_SERVICE_CONTAINER",
    "FOUNDRY_DATASET",
    "FOUNDRY_DEPLOYED_APP",
    "FOUNDRY_ML_OBJECTIVE",
    "FOUNDRY_SQL_SERVER_WORKSHEET",
    "FOUNDRY_STREAMING_VIEW",
    "FOUNDRY_TEMPLATES_TEMPLATE",
    "FUNCTION_REGISTRY_FUNCTION",
    "FUNCTION_REGISTRY_REGISTRY",
    "FUSION_DOCUMENT",
    "GEOTIME_CATALOG_INTEGRATION",
    "GOTHAM_ARTIFACT_STENCIL_FORM",
    "GPS_VIEW",
    "HUBBLE_EXPLORATION_LAYOUT",
    "HUBBLE_INSIGHT_WORKBOOK",
    "HYPERAUTO_INTEGRATION",
    "INBOUND_MESSAGE_LISTENER_TARGET",
    "LOGIC_FLOWS_CONNECTED_FLOW",
    "MACHINERY_AUTOPILOT",
    "MACHINERY_DOCUMENT",
    "MAGRITTE_AGENT",
    "MAGRITTE_DRIVER",
    "MAGRITTE_EXPORT",
    "MAGRITTE_EXTERNAL_STACK",
    "MAGRITTE_PLUGIN",
    "MAGRITTE_SOURCE",
    "MAP_RENDERING_SERVICE_SYMBOL_TYPE",
    "MARBLE_SERVER_LAYER",
    "MARKETPLACE_BLOCK_SET_INSTALLATION",
    "MARKETPLACE_BLOCK_SET_REPO",
    "MARKETPLACE_LOCAL",
    "MARKETPLACE_REMOTE_STORE",
    "MATRIX_CASE_STUDY",
    "MIO_MEDIA_SET",
    "MODELS_EXPERIMENT",
    "MODELS_MODEL",
    "MODELS_MODEL_VERSION",
    "MONOCLE_GRAPH",
    "NETWORK_POLICY_POLICY",
    "NOTEPAD_NOTEPAD",
    "NOTEPAD_NOTEPAD_TEMPLATE",
    "OBJECT_SENTINEL_MONITOR",
    "OBJECT_SET_VERSIONED_OBJECT_SET",
    "ONTOLOGY_BRANCH",
    "ONTOLOGY_DIRECT_SOURCE",
    "ONTOLOGY_INTERFACE",
    "ONTOLOGY_OBJECT_TYPE",
    "ONTOLOGY_ONTOLOGY",
    "ONTOLOGY_RELATION",
    "ONTOLOGY_SHARED_PROPERTY",
    "OPUS_GRAPH",
    "OPUS_GRAPH_POINTER",
    "OPUS_GRAPH_TEMPLATE",
    "OPUS_MAP",
    "OPUS_MAP_LAYER",
    "OPUS_MAP_TEMPLATE",
    "OPUS_SEARCH_AROUND",
    "QUBIT_PROJECT",
    "QUIVER_ANALYSIS",
    "QUIVER_ARTIFACT",
    "QUIVER_DASHBOARD",
    "QUIVER_DERIVED_SERIES",
    "QUIVER_FUNCTION",
    "QUIVER_OBJECT_SET_PATH",
    "QUIVER_SINGLE_DERIVED_SERIES",
    "QUIVER_TIME_SERIES_ANALYSIS",
    "RELEASE_MANAGEMENT_APPLICATION_INSTANCE",
    "REPORT_REPORT",
    "SITES_SERVICE_ENDPOINT_SET",
    "SLATE_DOCUMENT",
    "SLATE_VIEW",
    "SOLUTION_DESIGN_DIAGRAM",
    "STEMMA_REPOSITORY",
    "TABLES_TABLE",
    "TAURUS_WORKFLOW",
    "THIRD_PARTY_APPLICATIONS_APPLICATION",
    "TIME_SERIES_CATALOG_SYNC",
    "VECTOR_SHARED_CHANNEL",
    "VECTOR_TEMPLATE",
    "VECTOR_WORKBOOK",
    "WIDGETREGISTRY_WIDGET_SET",
    "WORKFLOW_BUILDER_EDIT",
    "WORKSHOP_MODULE",
    "WORKSHOP_STATE",
]
"""The type of the resource."""


RoleSetId: typing_extensions.TypeAlias = str
"""The ID of a role set."""


class Space(core.ModelBase):
    """A Foundry space."""

    default_role_set_id: RoleSetId = pydantic.Field(alias=str("defaultRoleSetId"))  # type: ignore[literal-required]
    """
    The ID of the default role set for this space, which defines the set of roles that projects in this space
    must use.
    """

    deletion_policy_organization_rids: typing.List[OrganizationRid] = pydantic.Field(alias=str("deletionPolicyOrganizationRids"))  # type: ignore[literal-required]
    """
    By default, this space will use a Last Out deletion policy, meaning that this space and its projects will be
    deleted when the last organization listed here is deleted. Only organizations in the space's enrollment can
    be included here.
    """

    description: typing.Optional[str] = None
    """The description of the space. Empty if no description is configured."""

    display_name: DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the space. Must be unique and cannot contain a `/`."""

    file_system_id: typing.Optional[FileSystemId] = pydantic.Field(alias=str("fileSystemId"), default=None)  # type: ignore[literal-required]
    """
    The ID of the filesystem for this space, which is where the contents of the space are stored.
    This field may be absent for legacy resources.
    """

    maven_identifier: typing.Optional[MavenIdentifier] = pydantic.Field(alias=str("mavenIdentifier"), default=None)  # type: ignore[literal-required]
    """
    The Maven identifier used as the prefix to the maven coordinate that uniquely identifies resources published
    from this space. Only present if previously configured.
    """

    organization_rids: typing.List[OrganizationRid] = pydantic.Field(alias=str("organizationRids"))  # type: ignore[literal-required]
    """
    The list of organizations that are provisioned access to this space. To access this space, a user must be a
    member of at least one of these organizations.
    """

    path: ResourcePath
    """The full path to the resource, including the resource name itself."""

    rid: SpaceRid
    usage_account_rid: typing.Optional[UsageAccountRid] = pydantic.Field(alias=str("usageAccountRid"), default=None)  # type: ignore[literal-required]
    """
    The RID of the usage account for this space. Resource usage for projects in this space will accrue to this
    usage account by default. This field may be absent for legacy resources.
    """

    type: typing.Literal["value"] = "value"


SpaceBatchResult: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["SpaceNotFoundError", "Space"], pydantic.Field(discriminator="type")
]
"""SpaceBatchResult"""


class SpaceNotFoundError(core.ModelBase):
    """SpaceNotFoundError"""

    rid: SpaceRid
    type: typing.Literal["notFound"] = "notFound"


SpaceRid: typing_extensions.TypeAlias = core.RID
"""The unique resource identifier (RID) of a space."""


class SpaceRidField(core.ModelBase):
    """Holds the space that a resource belongs to."""

    value: SpaceRid
    """The RID of the space that contains the resource."""


TrashStatus: typing_extensions.TypeAlias = typing.Literal[
    "NOT_TRASHED", "DIRECTLY_TRASHED", "ANCESTOR_TRASHED"
]
"""
Whether a resource is in the trash, and if so, whether it was trashed directly or through one of its ancestors.


Values:
- **ANCESTOR_TRASHED**: The resource is in the trash because one of its ancestors was trashed. Such a resource cannot be restored
on its own; restoring the trashed ancestor also restores this resource.

- **DIRECTLY_TRASHED**: The resource itself was trashed and can be restored.
- **NOT_TRASHED**: Neither the resource nor any of its ancestors is trashed.
"""


class TrashStatusField(core.ModelBase):
    """Holds whether a resource is in the trash."""

    value: TrashStatus
    """
    The trash status of the resource. If trashed, this could either be because the resource itself has been
    trashed or because one of its ancestors has been trashed.
    """


UsageAccountRid: typing_extensions.TypeAlias = core.RID
"""The unique resource identifier (RID) of a usage account."""


UserId: typing_extensions.TypeAlias = str
"""The ID of a user."""


core.resolve_forward_references_in_module(__name__)

__all__ = [
    "AdditionalField",
    "AdditionalFields",
    "Branch",
    "BranchName",
    "BranchRid",
    "Contact",
    "ContactInformation",
    "ContactInformationField",
    "CreateFolderRequest",
    "DefaultBranchField",
    "DeleteFoldersBatchRequestElement",
    "DeleteProjectsBatchRequestElement",
    "DeleteResourcesBatchRequestElement",
    "DeleteSpacesBatchRequestElement",
    "DescriptionField",
    "DisplayName",
    "DocumentationField",
    "FileSystemId",
    "Folder",
    "FolderBatchResult",
    "FolderNotFoundError",
    "GetFoldersBatchRequestElement",
    "GetFoldersBatchResponse",
    "GetProjectsBatchRequestElement",
    "GetProjectsBatchResponse",
    "GetResourcesBatchRequestElement",
    "GetResourcesBatchResponse",
    "GetSpacesBatchRequestElement",
    "GetSpacesBatchResponse",
    "ListSpacesResponse",
    "MavenIdentifier",
    "NamedAncestorsField",
    "NamedResourceIdentifier",
    "OrganizationRid",
    "PathField",
    "Project",
    "ProjectBatchResult",
    "ProjectNotFoundError",
    "ProjectRid",
    "Resource",
    "ResourceBatchResult",
    "ResourceNotFoundError",
    "ResourcePath",
    "ResourceRid",
    "ResourceType",
    "RoleSetId",
    "Space",
    "SpaceBatchResult",
    "SpaceNotFoundError",
    "SpaceRid",
    "SpaceRidField",
    "TrashStatus",
    "TrashStatusField",
    "UsageAccountRid",
    "UserId",
]
