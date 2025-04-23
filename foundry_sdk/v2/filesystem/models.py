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
from foundry_sdk.v2.core import models as core_models


class AccessRequirements(pydantic.BaseModel):
    """
    Access requirements for a resource are composed of Markings and Organizations. Organizations are disjunctive,
    while Markings are conjunctive.
    """

    organizations: typing.List[Organization]
    markings: typing.List[Marking]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Everyone(pydantic.BaseModel):
    """A principal representing all users of the platform."""

    type: typing.Literal["everyone"] = "everyone"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


FileSystemId = str
"""The ID of the filesystem that will be used for all projects in the Space."""


class Folder(pydantic.BaseModel):
    """Folder"""

    rid: FolderRid
    display_name: ResourceDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """The description associated with the Folder."""

    documentation: typing.Optional[str] = None
    """The documentation associated with the Folder."""

    path: ResourcePath
    type: FolderType
    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    updated_by: core_models.UpdatedBy = pydantic.Field(alias=str("updatedBy"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    updated_time: core_models.UpdatedTime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    trash_status: TrashStatus = pydantic.Field(alias=str("trashStatus"))  # type: ignore[literal-required]
    """
    The trash status of the Folder. If trashed, this could either be because the Folder itself has been
    trashed or because one of its ancestors has been trashed.
    """

    parent_folder_rid: FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    """
    The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces,
    this value will be the root folder (`ri.compass.main.folder.0`).
    """

    project_rid: typing.Optional[ProjectRid] = pydantic.Field(alias=str("projectRid"), default=None)  # type: ignore[literal-required]
    """
    The Project Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will
    not be defined.
    """

    space_rid: SpaceRid = pydantic.Field(alias=str("spaceRid"))  # type: ignore[literal-required]
    """
    The Space Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will
    be the same as the Folder RID.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


FolderRid = core.RID
"""The unique resource identifier (RID) of a Folder."""


FolderType = typing.Literal["FOLDER", "SPACE", "PROJECT"]
"""
A folder can be a regular Folder, a
[Project](https://palantir.com/docs/foundry/getting-started/projects-and-resources/#projects) or a
[Space](https://palantir.com/docs/foundry/security/orgs-and-spaces/#spaces).
"""


IsDirectlyApplied = bool
"""
Boolean flag to indicate if the marking is directly applied to the resource, or if it's applied
to a parent resource and inherited by the current resource.
"""


class ListChildrenOfFolderResponse(pydantic.BaseModel):
    """ListChildrenOfFolderResponse"""

    data: typing.List[Resource]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListMarkingsOfResourceResponse(pydantic.BaseModel):
    """ListMarkingsOfResourceResponse"""

    data: typing.List[core_models.MarkingId]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListOrganizationsOfProjectResponse(pydantic.BaseModel):
    """ListOrganizationsOfProjectResponse"""

    data: typing.List[core_models.OrganizationRid]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListResourceRolesResponse(pydantic.BaseModel):
    """ListResourceRolesResponse"""

    data: typing.List[ResourceRole]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListSpacesResponse(pydantic.BaseModel):
    """ListSpacesResponse"""

    data: typing.List[Space]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Marking(pydantic.BaseModel):
    """
    [Markings](https://palantir.com/docs/foundry/security/markings/) provide an additional level of access control for files,
    folders, and Projects within Foundry. Markings define eligibility criteria that restrict visibility
    and actions to users who meet those criteria. To access a resource, a user must be a member of all
    Markings applied to a resource to access it.
    """

    marking_id: core_models.MarkingId = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]
    is_directly_applied: IsDirectlyApplied = pydantic.Field(alias=str("isDirectlyApplied"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Organization(pydantic.BaseModel):
    """
    [Organizations](https://palantir.com/docs/foundry/security/orgs-and-spaces/#organizations) are access requirements applied to
    Projects that enforce strict silos between groups of users and resources. Every user is a member of only
    one Organization, but can be a guest member of multiple Organizations. In order to meet access requirements,
    users must be a member or guest member of at least one Organization applied to a Project.
    Organizations are inherited via the file hierarchy and direct dependencies.
    """

    marking_id: core_models.MarkingId = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]
    organization_rid: core_models.OrganizationRid = pydantic.Field(alias=str("organizationRid"))  # type: ignore[literal-required]
    is_directly_applied: IsDirectlyApplied = pydantic.Field(alias=str("isDirectlyApplied"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class PrincipalWithId(pydantic.BaseModel):
    """Represents a user principal or group principal with an ID."""

    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    type: typing.Literal["principalWithId"] = "principalWithId"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Project(pydantic.BaseModel):
    """Project"""

    rid: ProjectRid
    display_name: ResourceDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the Project. Must be unique and cannot contain a /"""

    description: typing.Optional[str] = None
    """The description associated with the Project."""

    documentation: typing.Optional[str] = None
    """The documentation associated with the Project."""

    path: ResourcePath
    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    updated_by: core_models.UpdatedBy = pydantic.Field(alias=str("updatedBy"))  # type: ignore[literal-required]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    updated_time: core_models.UpdatedTime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    trash_status: TrashStatus = pydantic.Field(alias=str("trashStatus"))  # type: ignore[literal-required]
    """The trash status of the Project."""

    space_rid: SpaceRid = pydantic.Field(alias=str("spaceRid"))  # type: ignore[literal-required]
    """The Space Resource Identifier (RID) that the Project lives in."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ProjectRid = core.RID
"""The unique resource identifier (RID) of a Project."""


ProjectTemplateRid = core.RID
"""The unique resource identifier (RID) of a project template."""


ProjectTemplateVariableId = str
"""An identifier for a variable used in a project template."""


ProjectTemplateVariableValue = str
"""The value assigned to a variable used in a project template."""


class Resource(pydantic.BaseModel):
    """Resource"""

    rid: ResourceRid
    display_name: ResourceDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the Resource"""

    description: typing.Optional[str] = None
    """The description of the Resource"""

    documentation: typing.Optional[str] = None
    """The documentation associated with the Resource"""

    path: ResourcePath
    """The full path to the resource, including the resource name itself"""

    type: ResourceType
    """The type of the Resource derived from the Resource Identifier (RID)."""

    created_by: core_models.CreatedBy = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    """The user that created the Resource."""

    updated_by: core_models.UpdatedBy = pydantic.Field(alias=str("updatedBy"))  # type: ignore[literal-required]
    """The user that last updated the Resource."""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The timestamp that the Resource was last created."""

    updated_time: core_models.UpdatedTime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    """
    The timestamp that the Resource was last modified. For folders, this includes any of its descendants. For
    top level folders (spaces and projects), this is not updated by child updates for performance reasons.
    """

    trash_status: TrashStatus = pydantic.Field(alias=str("trashStatus"))  # type: ignore[literal-required]
    """
    The trash status of the Resource. If trashed, this could either be because the Resource itself has been
    trashed or because one of its ancestors has been trashed.
    """

    parent_folder_rid: FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    """The parent folder Resource Identifier (RID). For projects, this will be the Space RID."""

    project_rid: ProjectRid = pydantic.Field(alias=str("projectRid"))  # type: ignore[literal-required]
    """
    The Project Resource Identifier (RID) that the Resource lives in. If the Resource itself is a
    Project, this value will still be populated with the Project RID.
    """

    space_rid: SpaceRid = pydantic.Field(alias=str("spaceRid"))  # type: ignore[literal-required]
    """The Space Resource Identifier (RID) that the Resource lives in."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ResourceDisplayName = str
"""The display name of the Resource"""


ResourcePath = str
"""The full path to the resource, including the resource name itself"""


ResourceRid = core.RID
"""The unique resource identifier (RID) of a Resource."""


class ResourceRole(pydantic.BaseModel):
    """ResourceRole"""

    resource_role_principal: ResourceRolePrincipal = pydantic.Field(alias=str("resourceRolePrincipal"))  # type: ignore[literal-required]
    role_id: core_models.RoleId = pydantic.Field(alias=str("roleId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ResourceRolePrincipal = typing_extensions.Annotated[
    typing.Union[PrincipalWithId, Everyone], pydantic.Field(discriminator="type")
]
"""ResourceRolePrincipal"""


ResourceType = typing.Literal[
    "AIP_PROFILE",
    "AIP_ASSIST_WALKTHROUGH",
    "ARTIFACTS_REPOSITORY",
    "BELLASO_CIPHER_CHANNEL",
    "BELLASO_CIPHER_LICENSE",
    "BLACKSMITH_DOCUMENT",
    "BLOBSTER_ARCHIVE",
    "BLOBSTER_AUDIO",
    "BLOBSTER_BLOB",
    "BLOBSTER_CODE",
    "BLOBSTER_CONFIGURATION",
    "BLOBSTER_DOCUMENT",
    "BLOBSTER_IMAGE",
    "BLOBSTER_JUPYTERNOTEBOOK",
    "BLOBSTER_PDF",
    "BLOBSTER_PRESENTATION",
    "BLOBSTER_SPREADSHEET",
    "BLOBSTER_VIDEO",
    "BLOBSTER_XML",
    "CARBON_WORKSPACE",
    "COMPASS_FOLDER",
    "COMPASS_WEB_LINK",
    "CONTOUR_ANALYSIS",
    "DATA_HEALTH_MONITORING_VIEW",
    "DECISIONS_EXPLORATION",
    "DREDDIE_PIPELINE",
    "EDDIE_LOGIC",
    "EDDIE_PIPELINE",
    "FFORMS_FORM",
    "FLOW_WORKFLOW",
    "FOUNDRY_DATASET",
    "FOUNDRY_DEPLOYED_APP",
    "FOUNDRY_ACADEMY_TUTORIAL",
    "FOUNDRY_CONTAINER_SERVICE_CONTAINER",
    "FOUNDRY_ML_OBJECTIVE",
    "FOUNDRY_TEMPLATES_TEMPLATE",
    "FUSION_DOCUMENT",
    "GPS_VIEW",
    "HUBBLE_EXPLORATION_LAYOUT",
    "HYPERAUTO_INTEGRATION",
    "LOGIC_FLOWS_CONNECTED_FLOW",
    "MACHINERY_DOCUMENT",
    "MAGRITTE_AGENT",
    "MAGRITTE_SOURCE",
    "MARKETPLACE_BLOCK_SET_INSTALLATION",
    "MARKETPLACE_BLOCK_SET_REPO",
    "MARKETPLACE_LOCAL",
    "MARKETPLACE_REMOTE_STORE",
    "MIO_MEDIA_SET",
    "MODELS_MODEL",
    "MODELS_MODEL_VERSION",
    "MONOCLE_GRAPH",
    "NOTEPAD_NOTEPAD",
    "NOTEPAD_NOTEPAD_TEMPLATE",
    "OBJECT_SENTINEL_MONITOR",
    "OBJECT_SET_VERSIONED_OBJECT_SET",
    "OPUS_GRAPH",
    "OPUS_GRAPH_TEMPLATE",
    "OPUS_MAP",
    "OPUS_MAP_LAYER",
    "OPUS_MAP_TEMPLATE",
    "OPUS_SEARCH_AROUND",
    "QUIVER_ANALYSIS",
    "QUIVER_ARTIFACT",
    "QUIVER_DASHBOARD",
    "REPORT_REPORT",
    "SLATE_DOCUMENT",
    "SOLUTION_DESIGN_DIAGRAM",
    "STEMMA_REPOSITORY",
    "TABLES_TABLE",
    "TAURUS_WORKFLOW",
    "THIRD_PARTY_APPLICATIONS_APPLICATION",
    "TIME_SERIES_CATALOG_SYNC",
    "VECTOR_TEMPLATE",
    "VECTOR_WORKBOOK",
    "WORKSHOP_MODULE",
    "WORKSHOP_STATE",
]
"""The type of the Resource derived from the Resource Identifier (RID)."""


class Space(pydantic.BaseModel):
    """Space"""

    rid: SpaceRid
    display_name: ResourceDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """The description of the Space."""

    path: ResourcePath
    file_system_id: typing.Optional[FileSystemId] = pydantic.Field(alias=str("fileSystemId"), default=None)  # type: ignore[literal-required]
    usage_account_rid: typing.Optional[UsageAccountRid] = pydantic.Field(alias=str("usageAccountRid"), default=None)  # type: ignore[literal-required]
    organizations: typing.List[core_models.OrganizationRid]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


SpaceRid = core.RID
"""The unique resource identifier (RID) of a Space."""


TrashStatus = typing.Literal["DIRECTLY_TRASHED", "ANCESTOR_TRASHED", "NOT_TRASHED"]
"""TrashStatus"""


UsageAccountRid = core.RID
"""The unique resource identifier (RID) of the usage account that will be used as a default on project creation."""


core.resolve_forward_references(ResourceRolePrincipal, globalns=globals(), localns=locals())

__all__ = [
    "AccessRequirements",
    "Everyone",
    "FileSystemId",
    "Folder",
    "FolderRid",
    "FolderType",
    "IsDirectlyApplied",
    "ListChildrenOfFolderResponse",
    "ListMarkingsOfResourceResponse",
    "ListOrganizationsOfProjectResponse",
    "ListResourceRolesResponse",
    "ListSpacesResponse",
    "Marking",
    "Organization",
    "PrincipalWithId",
    "Project",
    "ProjectRid",
    "ProjectTemplateRid",
    "ProjectTemplateVariableId",
    "ProjectTemplateVariableValue",
    "Resource",
    "ResourceDisplayName",
    "ResourcePath",
    "ResourceRid",
    "ResourceRole",
    "ResourceRolePrincipal",
    "ResourceType",
    "Space",
    "SpaceRid",
    "TrashStatus",
    "UsageAccountRid",
]
