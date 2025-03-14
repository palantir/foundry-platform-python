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
from datetime import datetime

import pydantic
import typing_extensions

from foundry import _core as core


class AccessRequirements(pydantic.BaseModel):
    """
    Access requirements for a resource are composed of Markings and Organizations. Organizations are disjunctive,
    while Markings are conjunctive.
    """

    organizations: typing.List[Organization]
    markings: typing.List[Marking]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "AccessRequirementsDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AccessRequirementsDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AccessRequirementsDict(typing_extensions.TypedDict):
    """
    Access requirements for a resource are composed of Markings and Organizations. Organizations are disjunctive,
    while Markings are conjunctive.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    organizations: typing.List[OrganizationDict]
    markings: typing.List[MarkingDict]


class Everyone(pydantic.BaseModel):
    """A principal representing all users of the platform."""

    type: typing.Literal["everyone"] = "everyone"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "EveryoneDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(EveryoneDict, self.model_dump(by_alias=True, exclude_none=True))


class EveryoneDict(typing_extensions.TypedDict):
    """A principal representing all users of the platform."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["everyone"]


FileSystemId = str
"""The ID of the filesystem that will be used for all projects in the Space."""


class Folder(pydantic.BaseModel):
    """Folder"""

    rid: core.RID
    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """The description associated with the Folder."""

    documentation: typing.Optional[str] = None
    """The documentation associated with the Folder."""

    path: str
    type: FolderType
    created_by: str = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    updated_by: core.UUID = pydantic.Field(alias=str("updatedBy"))  # type: ignore[literal-required]
    created_time: datetime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    updated_time: datetime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    trash_status: TrashStatus = pydantic.Field(alias=str("trashStatus"))  # type: ignore[literal-required]
    """
    The trash status of the Folder. If trashed, this could either be because the Folder itself has been
    trashed or because one of its ancestors has been trashed.
    """

    parent_folder_rid: core.RID = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    """
    The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces,
    this value will be the root folder (`ri.compass.main.folder.0`).
    """

    project_rid: typing.Optional[ProjectRid] = pydantic.Field(alias=str("projectRid"), default=None)  # type: ignore[literal-required]
    """
    The Project Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will
    not be defined.
    """

    space_rid: core.RID = pydantic.Field(alias=str("spaceRid"))  # type: ignore[literal-required]
    """
    The Space Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will
    be the same as the Folder RID.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "FolderDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(FolderDict, self.model_dump(by_alias=True, exclude_none=True))


class FolderDict(typing_extensions.TypedDict):
    """Folder"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: core.RID
    displayName: str
    description: typing_extensions.NotRequired[str]
    """The description associated with the Folder."""

    documentation: typing_extensions.NotRequired[str]
    """The documentation associated with the Folder."""

    path: str
    type: FolderType
    createdBy: str
    updatedBy: core.UUID
    createdTime: datetime
    updatedTime: datetime
    trashStatus: TrashStatus
    """
    The trash status of the Folder. If trashed, this could either be because the Folder itself has been
    trashed or because one of its ancestors has been trashed.
    """

    parentFolderRid: core.RID
    """
    The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces,
    this value will be the root folder (`ri.compass.main.folder.0`).
    """

    projectRid: typing_extensions.NotRequired[ProjectRid]
    """
    The Project Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will
    not be defined.
    """

    spaceRid: core.RID
    """
    The Space Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will
    be the same as the Folder RID.
    """


FolderRid = core.RID
"""The unique resource identifier (RID) of a Folder."""


FolderType = typing.Literal["FOLDER", "SPACE", "PROJECT"]
"""
A folder can be a regular Folder, a
[Project](/docs/foundry/getting-started/projects-and-resources/#projects) or a
[Space](/docs/foundry/security/orgs-and-spaces/#spaces).
"""


class ListChildrenOfFolderResponse(pydantic.BaseModel):
    """ListChildrenOfFolderResponse"""

    data: typing.List[Resource]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListChildrenOfFolderResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListChildrenOfFolderResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListChildrenOfFolderResponseDict(typing_extensions.TypedDict):
    """ListChildrenOfFolderResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[ResourceDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListMarkingsOfResourceResponse(pydantic.BaseModel):
    """ListMarkingsOfResourceResponse"""

    data: typing.List[core_models.MarkingId]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListMarkingsOfResourceResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListMarkingsOfResourceResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListMarkingsOfResourceResponseDict(typing_extensions.TypedDict):
    """ListMarkingsOfResourceResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[core_models.MarkingId]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListOrganizationsOfProjectResponse(pydantic.BaseModel):
    """ListOrganizationsOfProjectResponse"""

    data: typing.List[core_models.OrganizationRid]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListOrganizationsOfProjectResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListOrganizationsOfProjectResponseDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class ListOrganizationsOfProjectResponseDict(typing_extensions.TypedDict):
    """ListOrganizationsOfProjectResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[core_models.OrganizationRid]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListResourceRolesResponse(pydantic.BaseModel):
    """ListResourceRolesResponse"""

    data: typing.List[ResourceRole]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListResourceRolesResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListResourceRolesResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListResourceRolesResponseDict(typing_extensions.TypedDict):
    """ListResourceRolesResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[ResourceRoleDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListSpacesResponse(pydantic.BaseModel):
    """ListSpacesResponse"""

    data: typing.List[Space]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListSpacesResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListSpacesResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListSpacesResponseDict(typing_extensions.TypedDict):
    """ListSpacesResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[SpaceDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class Marking(pydantic.BaseModel):
    """
    [Markings](/docs/foundry/security/markings/) provide an additional level of access control for files,
    folders, and Projects within Foundry. Markings define eligibility criteria that restrict visibility
    and actions to users who meet those criteria. To access a resource, a user must be a member of all
    Markings applied to a resource to access it.
    """

    marking_id: core.UUID = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]
    is_directly_applied: bool = pydantic.Field(alias=str("isDirectlyApplied"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MarkingDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MarkingDict, self.model_dump(by_alias=True, exclude_none=True))


class MarkingDict(typing_extensions.TypedDict):
    """
    [Markings](/docs/foundry/security/markings/) provide an additional level of access control for files,
    folders, and Projects within Foundry. Markings define eligibility criteria that restrict visibility
    and actions to users who meet those criteria. To access a resource, a user must be a member of all
    Markings applied to a resource to access it.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core.UUID
    isDirectlyApplied: bool


class Organization(pydantic.BaseModel):
    """
    [Organizations](/docs/foundry/security/orgs-and-spaces/#organizations) are access requirements applied to
    Projects that enforce strict silos between groups of users and resources. Every user is a member of only
    one Organization, but can be a guest member of multiple Organizations. In order to meet access requirements,
    users must be a member or guest member of at least one Organization applied to a Project.
    Organizations are inherited via the file hierarchy and direct dependencies.
    """

    marking_id: core.UUID = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]
    organization_rid: core.RID = pydantic.Field(alias=str("organizationRid"))  # type: ignore[literal-required]
    is_directly_applied: bool = pydantic.Field(alias=str("isDirectlyApplied"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OrganizationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OrganizationDict, self.model_dump(by_alias=True, exclude_none=True))


class OrganizationDict(typing_extensions.TypedDict):
    """
    [Organizations](/docs/foundry/security/orgs-and-spaces/#organizations) are access requirements applied to
    Projects that enforce strict silos between groups of users and resources. Every user is a member of only
    one Organization, but can be a guest member of multiple Organizations. In order to meet access requirements,
    users must be a member or guest member of at least one Organization applied to a Project.
    Organizations are inherited via the file hierarchy and direct dependencies.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core.UUID
    organizationRid: core.RID
    isDirectlyApplied: bool


class PrincipalWithId(pydantic.BaseModel):
    """Represents a user principal or group principal with an ID."""

    principal_id: str = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    type: typing.Literal["principalWithId"] = "principalWithId"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "PrincipalWithIdDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(PrincipalWithIdDict, self.model_dump(by_alias=True, exclude_none=True))


class PrincipalWithIdDict(typing_extensions.TypedDict):
    """Represents a user principal or group principal with an ID."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    principalId: str
    principalType: core_models.PrincipalType
    type: typing.Literal["principalWithId"]


class Project(pydantic.BaseModel):
    """Project"""

    rid: core.RID
    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the Project. Must be unique and cannot contain a /"""

    description: typing.Optional[str] = None
    """The description associated with the Project."""

    documentation: typing.Optional[str] = None
    """The documentation associated with the Project."""

    path: str
    created_by: str = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    updated_by: core.UUID = pydantic.Field(alias=str("updatedBy"))  # type: ignore[literal-required]
    created_time: datetime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    updated_time: datetime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    trash_status: TrashStatus = pydantic.Field(alias=str("trashStatus"))  # type: ignore[literal-required]
    """The trash status of the Project."""

    space_rid: core.RID = pydantic.Field(alias=str("spaceRid"))  # type: ignore[literal-required]
    """The Space Resource Identifier (RID) that the Project lives in."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ProjectDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ProjectDict, self.model_dump(by_alias=True, exclude_none=True))


class ProjectDict(typing_extensions.TypedDict):
    """Project"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: core.RID
    displayName: str
    """The display name of the Project. Must be unique and cannot contain a /"""

    description: typing_extensions.NotRequired[str]
    """The description associated with the Project."""

    documentation: typing_extensions.NotRequired[str]
    """The documentation associated with the Project."""

    path: str
    createdBy: str
    updatedBy: core.UUID
    createdTime: datetime
    updatedTime: datetime
    trashStatus: TrashStatus
    """The trash status of the Project."""

    spaceRid: core.RID
    """The Space Resource Identifier (RID) that the Project lives in."""


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

    rid: core.RID
    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the Resource"""

    description: typing.Optional[str] = None
    """The description of the Resource"""

    documentation: typing.Optional[str] = None
    """The documentation associated with the Resource"""

    path: str
    """The full path to the resource, including the resource name itself"""

    type: ResourceType
    """The type of the Resource derived from the Resource Identifier (RID)."""

    created_by: str = pydantic.Field(alias=str("createdBy"))  # type: ignore[literal-required]
    """The user that created the Resource."""

    updated_by: core.UUID = pydantic.Field(alias=str("updatedBy"))  # type: ignore[literal-required]
    """The user that last updated the Resource."""

    created_time: datetime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The timestamp that the Resource was last created."""

    updated_time: datetime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]
    """
    The timestamp that the Resource was last modified. For folders, this includes any of its descendants. For
    top level folders (spaces and projects), this is not updated by child updates for performance reasons.
    """

    trash_status: TrashStatus = pydantic.Field(alias=str("trashStatus"))  # type: ignore[literal-required]
    """
    The trash status of the Resource. If trashed, this could either be because the Resource itself has been
    trashed or because one of its ancestors has been trashed.
    """

    parent_folder_rid: core.RID = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    """The parent folder Resource Identifier (RID). For projects, this will be the Space RID."""

    project_rid: core.RID = pydantic.Field(alias=str("projectRid"))  # type: ignore[literal-required]
    """
    The Project Resource Identifier (RID) that the Resource lives in. If the Resource itself is a
    Project, this value will still be populated with the Project RID.
    """

    space_rid: core.RID = pydantic.Field(alias=str("spaceRid"))  # type: ignore[literal-required]
    """The Space Resource Identifier (RID) that the Resource lives in."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ResourceDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ResourceDict, self.model_dump(by_alias=True, exclude_none=True))


class ResourceDict(typing_extensions.TypedDict):
    """Resource"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: core.RID
    displayName: str
    """The display name of the Resource"""

    description: typing_extensions.NotRequired[str]
    """The description of the Resource"""

    documentation: typing_extensions.NotRequired[str]
    """The documentation associated with the Resource"""

    path: str
    """The full path to the resource, including the resource name itself"""

    type: ResourceType
    """The type of the Resource derived from the Resource Identifier (RID)."""

    createdBy: str
    """The user that created the Resource."""

    updatedBy: core.UUID
    """The user that last updated the Resource."""

    createdTime: datetime
    """The timestamp that the Resource was last created."""

    updatedTime: datetime
    """
    The timestamp that the Resource was last modified. For folders, this includes any of its descendants. For
    top level folders (spaces and projects), this is not updated by child updates for performance reasons.
    """

    trashStatus: TrashStatus
    """
    The trash status of the Resource. If trashed, this could either be because the Resource itself has been
    trashed or because one of its ancestors has been trashed.
    """

    parentFolderRid: core.RID
    """The parent folder Resource Identifier (RID). For projects, this will be the Space RID."""

    projectRid: core.RID
    """
    The Project Resource Identifier (RID) that the Resource lives in. If the Resource itself is a
    Project, this value will still be populated with the Project RID.
    """

    spaceRid: core.RID
    """The Space Resource Identifier (RID) that the Resource lives in."""


ResourceDisplayName = str
"""The display name of the Resource"""


ResourcePath = str
"""The full path to the resource, including the resource name itself"""


ResourceRid = core.RID
"""The unique resource identifier (RID) of a Resource."""


class ResourceRole(pydantic.BaseModel):
    """ResourceRole"""

    resource_role_principal: ResourceRolePrincipal = pydantic.Field(alias=str("resourceRolePrincipal"))  # type: ignore[literal-required]
    role_id: str = pydantic.Field(alias=str("roleId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ResourceRoleDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ResourceRoleDict, self.model_dump(by_alias=True, exclude_none=True))


class ResourceRoleDict(typing_extensions.TypedDict):
    """ResourceRole"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    resourceRolePrincipal: ResourceRolePrincipalDict
    roleId: str


ResourceRolePrincipal = typing_extensions.Annotated[
    typing.Union["PrincipalWithId", "Everyone"], pydantic.Field(discriminator="type")
]
"""ResourceRolePrincipal"""


ResourceRolePrincipalDict = typing_extensions.Annotated[
    typing.Union["PrincipalWithIdDict", "EveryoneDict"], pydantic.Field(discriminator="type")
]
"""ResourceRolePrincipal"""


ResourceType = typing.Literal[
    "ARTIFACTS_REPOSITORY",
    "BELLASO_CIPHER_CHANNEL",
    "BLOBSTER_CODE",
    "BLOBSTER_DOCUMENT",
    "BLOBSTER_IMAGE",
    "BLOBSTER_SPREADSHEET",
    "CARBON_WORKSPACE",
    "COMPASS_FOLDER",
    "COMPASS_WEB_LINK",
    "CONTOUR_ANALYSIS",
    "DATA_HEALTH_MONITORING_VIEW",
    "EDDIE_LOGIC",
    "EDDIE_PIPELINE",
    "FFORMS_FORM",
    "FOUNDRY_DATASET",
    "FOUNDRY_ACADEMY_TUTORIAL",
    "FOUNDRY_CONTAINER_SERVICE_CONTAINER",
    "FOUNDRY_ML_OBJECTIVE",
    "FOUNDRY_TEMPLATES_TEMPLATE",
    "FUSION_DOCUMENT",
    "HUBBLE_EXPLORATION_LAYOUT",
    "MACHINERY_DOCUMENT",
    "MAGRITTE_AGENT",
    "MAGRITTE_SOURCE",
    "MARKETPLACE_BLOCK_SET_INSTALLATION",
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
    "OPUS_MAP",
    "OPUS_MAP_LAYER",
    "QUIVER_ANALYSIS",
    "REPORT_REPORT",
    "SLATE_DOCUMENT",
    "SOLUTION_DESIGN_DIAGRAM",
    "STEMMA_REPOSITORY",
    "TABLES_TABLE",
    "TAURUS_WORKFLOW",
    "THIRD_PARTY_APPLICATIONS_APPLICATION",
    "VECTOR_WORKBOOK",
    "WORKSHOP_MODULE",
]
"""The type of the Resource derived from the Resource Identifier (RID)."""


class Space(pydantic.BaseModel):
    """Space"""

    rid: core.RID
    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """The description of the Space."""

    path: str
    file_system_id: typing.Optional[FileSystemId] = pydantic.Field(alias=str("fileSystemId"), default=None)  # type: ignore[literal-required]
    usage_account_rid: typing.Optional[UsageAccountRid] = pydantic.Field(alias=str("usageAccountRid"), default=None)  # type: ignore[literal-required]
    organizations: typing.List[core_models.OrganizationRid]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SpaceDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(SpaceDict, self.model_dump(by_alias=True, exclude_none=True))


class SpaceDict(typing_extensions.TypedDict):
    """Space"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: core.RID
    displayName: str
    description: typing_extensions.NotRequired[str]
    """The description of the Space."""

    path: str
    fileSystemId: typing_extensions.NotRequired[FileSystemId]
    usageAccountRid: typing_extensions.NotRequired[UsageAccountRid]
    organizations: typing.List[core_models.OrganizationRid]


SpaceRid = core.RID
"""The unique resource identifier (RID) of a Space."""


TrashStatus = typing.Literal["DIRECTLY_TRASHED", "ANCESTOR_TRASHED", "NOT_TRASHED"]
"""TrashStatus"""


UsageAccountRid = core.RID
"""The unique resource identifier (RID) of the usage account that will be used as a default on project creation."""


from foundry.v2.core import models as core_models  # noqa: E402

__all__ = [
    "AccessRequirements",
    "AccessRequirementsDict",
    "Everyone",
    "EveryoneDict",
    "FileSystemId",
    "Folder",
    "FolderDict",
    "FolderRid",
    "FolderType",
    "ListChildrenOfFolderResponse",
    "ListChildrenOfFolderResponseDict",
    "ListMarkingsOfResourceResponse",
    "ListMarkingsOfResourceResponseDict",
    "ListOrganizationsOfProjectResponse",
    "ListOrganizationsOfProjectResponseDict",
    "ListResourceRolesResponse",
    "ListResourceRolesResponseDict",
    "ListSpacesResponse",
    "ListSpacesResponseDict",
    "Marking",
    "MarkingDict",
    "Organization",
    "OrganizationDict",
    "PrincipalWithId",
    "PrincipalWithIdDict",
    "Project",
    "ProjectDict",
    "ProjectRid",
    "ProjectTemplateRid",
    "ProjectTemplateVariableId",
    "ProjectTemplateVariableValue",
    "Resource",
    "ResourceDict",
    "ResourceDisplayName",
    "ResourcePath",
    "ResourceRid",
    "ResourceRole",
    "ResourceRoleDict",
    "ResourceRolePrincipal",
    "ResourceRolePrincipalDict",
    "ResourceType",
    "Space",
    "SpaceDict",
    "SpaceRid",
    "TrashStatus",
    "UsageAccountRid",
]
