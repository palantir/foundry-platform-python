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

AttributeName = str
"""AttributeName"""


AttributeValue = str
"""AttributeValue"""


AttributeValues = typing.List[AttributeValue]
"""AttributeValues"""


AuthenticationProtocol = typing_extensions.Annotated[
    typing.Union["SamlAuthenticationProtocol", "OidcAuthenticationProtocol"],
    pydantic.Field(discriminator="type"),
]
"""AuthenticationProtocol"""


class AuthenticationProvider(pydantic.BaseModel):
    """AuthenticationProvider"""

    rid: AuthenticationProviderRid
    name: AuthenticationProviderName
    realm: core_models.Realm
    enabled: AuthenticationProviderEnabled
    """Whether users can log in using this provider."""

    supported_hosts: typing.List[HostName] = pydantic.Field(alias=str("supportedHosts"))  # type: ignore[literal-required]
    """This provider can only be utilized from these hosts."""

    supported_username_patterns: typing.List[str] = pydantic.Field(alias=str("supportedUsernamePatterns"))  # type: ignore[literal-required]
    """Users who enter usernames that match these patterns will be redirected to this authentication provider."""

    protocol: AuthenticationProtocol
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


AuthenticationProviderEnabled = bool
"""Whether users can log in using this provider."""


AuthenticationProviderName = str
"""AuthenticationProviderName"""


AuthenticationProviderRid = core.RID
"""AuthenticationProviderRid"""


class CertificateInfo(pydantic.BaseModel):
    """CertificateInfo"""

    pem_certificate: str = pydantic.Field(alias=str("pemCertificate"))  # type: ignore[literal-required]
    """The certificate, in PEM format."""

    common_name: typing.Optional[str] = pydantic.Field(alias=str("commonName"), default=None)  # type: ignore[literal-required]
    expiry_date: core.AwareDatetime = pydantic.Field(alias=str("expiryDate"))  # type: ignore[literal-required]
    usage_type: CertificateUsageType = pydantic.Field(alias=str("usageType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


CertificateUsageType = typing.Literal["ENCRYPTION", "SIGNING", "UNSPECIFIED"]
"""CertificateUsageType"""


class Enrollment(pydantic.BaseModel):
    """Enrollment"""

    rid: core_models.EnrollmentRid
    name: EnrollmentName
    created_time: typing.Optional[core_models.CreatedTime] = pydantic.Field(alias=str("createdTime"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


EnrollmentName = str
"""EnrollmentName"""


class GetGroupsBatchRequestElement(pydantic.BaseModel):
    """GetGroupsBatchRequestElement"""

    group_id: core_models.PrincipalId = pydantic.Field(alias=str("groupId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GetGroupsBatchResponse(pydantic.BaseModel):
    """GetGroupsBatchResponse"""

    data: typing.Dict[core_models.PrincipalId, Group]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GetMarkingsBatchRequestElement(pydantic.BaseModel):
    """GetMarkingsBatchRequestElement"""

    marking_id: core_models.MarkingId = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GetMarkingsBatchResponse(pydantic.BaseModel):
    """GetMarkingsBatchResponse"""

    data: typing.Dict[core_models.MarkingId, Marking]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GetRolesBatchRequestElement(pydantic.BaseModel):
    """GetRolesBatchRequestElement"""

    role_id: core_models.RoleId = pydantic.Field(alias=str("roleId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GetRolesBatchResponse(pydantic.BaseModel):
    """GetRolesBatchResponse"""

    data: typing.Dict[core_models.RoleId, Role]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GetUserMarkingsResponse(pydantic.BaseModel):
    """GetUserMarkingsResponse"""

    view: typing.List[core_models.MarkingId]
    """
    The markings that the user has access to. The user will be able to access resources protected with these
    markings. This includes organization markings for organizations in which the user is a guest member.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GetUsersBatchRequestElement(pydantic.BaseModel):
    """GetUsersBatchRequestElement"""

    user_id: core_models.PrincipalId = pydantic.Field(alias=str("userId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GetUsersBatchResponse(pydantic.BaseModel):
    """GetUsersBatchResponse"""

    data: typing.Dict[core_models.PrincipalId, User]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Group(pydantic.BaseModel):
    """Group"""

    id: core_models.PrincipalId
    name: GroupName
    """The name of the Group."""

    description: typing.Optional[str] = None
    """A description of the Group."""

    realm: core_models.Realm
    organizations: typing.List[core_models.OrganizationRid]
    """The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed."""

    attributes: typing.Dict[AttributeName, AttributeValues]
    """A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GroupMember(pydantic.BaseModel):
    """GroupMember"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GroupMembership(pydantic.BaseModel):
    """GroupMembership"""

    group_id: core_models.PrincipalId = pydantic.Field(alias=str("groupId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


GroupMembershipExpiration = core.AwareDatetime
"""GroupMembershipExpiration"""


GroupName = str
"""The name of the Group."""


class GroupProviderInfo(pydantic.BaseModel):
    """GroupProviderInfo"""

    provider_id: ProviderId = pydantic.Field(alias=str("providerId"))  # type: ignore[literal-required]
    """
    The ID of the Group in the external authentication provider. This value is determined by the authentication provider.
    At most one Group can have a given provider ID in a given Realm.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GroupSearchFilter(pydantic.BaseModel):
    """GroupSearchFilter"""

    type: PrincipalFilterType
    value: str
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Host(pydantic.BaseModel):
    """Host"""

    host_name: HostName = pydantic.Field(alias=str("hostName"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


HostName = str
"""HostName"""


class ListAuthenticationProvidersResponse(pydantic.BaseModel):
    """ListAuthenticationProvidersResponse"""

    data: typing.List[AuthenticationProvider]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListAvailableOrganizationRolesResponse(pydantic.BaseModel):
    """ListAvailableOrganizationRolesResponse"""

    data: typing.List[core_models.Role]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListGroupMembersResponse(pydantic.BaseModel):
    """ListGroupMembersResponse"""

    data: typing.List[GroupMember]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListGroupMembershipsResponse(pydantic.BaseModel):
    """ListGroupMembershipsResponse"""

    data: typing.List[GroupMembership]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListGroupsResponse(pydantic.BaseModel):
    """ListGroupsResponse"""

    data: typing.List[Group]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListHostsResponse(pydantic.BaseModel):
    """ListHostsResponse"""

    data: typing.List[Host]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListMarkingCategoriesResponse(pydantic.BaseModel):
    """ListMarkingCategoriesResponse"""

    data: typing.List[MarkingCategory]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListMarkingMembersResponse(pydantic.BaseModel):
    """ListMarkingMembersResponse"""

    data: typing.List[MarkingMember]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListMarkingRoleAssignmentsResponse(pydantic.BaseModel):
    """ListMarkingRoleAssignmentsResponse"""

    data: typing.List[MarkingRoleAssignment]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListMarkingsResponse(pydantic.BaseModel):
    """ListMarkingsResponse"""

    data: typing.List[Marking]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListOrganizationRoleAssignmentsResponse(pydantic.BaseModel):
    """ListOrganizationRoleAssignmentsResponse"""

    data: typing.List[OrganizationRoleAssignment]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ListUsersResponse(pydantic.BaseModel):
    """ListUsersResponse"""

    data: typing.List[User]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Marking(pydantic.BaseModel):
    """Marking"""

    id: core_models.MarkingId
    category_id: MarkingCategoryId = pydantic.Field(alias=str("categoryId"))  # type: ignore[literal-required]
    name: MarkingName
    description: typing.Optional[str] = None
    organization: typing.Optional[core_models.OrganizationRid] = None
    """If this marking is associated with an Organization, its RID will be populated here."""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    created_by: typing.Optional[core_models.CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MarkingCategory(pydantic.BaseModel):
    """MarkingCategory"""

    id: MarkingCategoryId
    name: MarkingCategoryName
    description: typing.Optional[str] = None
    category_type: MarkingCategoryType = pydantic.Field(alias=str("categoryType"))  # type: ignore[literal-required]
    marking_type: MarkingType = pydantic.Field(alias=str("markingType"))  # type: ignore[literal-required]
    markings: typing.List[core_models.MarkingId]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    created_by: typing.Optional[core_models.CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


MarkingCategoryId = str
"""
The ID of a marking category. For user-created categories, this will be a UUID. Markings associated with
Organizations are placed in a category with ID "Organization".
"""


MarkingCategoryName = str
"""MarkingCategoryName"""


MarkingCategoryType = typing.Literal["CONJUNCTIVE", "DISJUNCTIVE"]
"""MarkingCategoryType"""


class MarkingMember(pydantic.BaseModel):
    """MarkingMember"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


MarkingName = str
"""MarkingName"""


MarkingRole = typing.Literal["ADMINISTER", "DECLASSIFY", "USE"]
"""
Represents the operations that a user can perform with regards to a Marking.
  * ADMINISTER: The user can add and remove members from the Marking, update Marking Role Assignments, and change Marking metadata.
  * DECLASSIFY: The user can remove the Marking from resources in the platform and stop the propagation of the Marking during a transform.
  * USE: The user can apply the marking to resources in the platform.
"""


class MarkingRoleAssignment(pydantic.BaseModel):
    """MarkingRoleAssignment"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    role: MarkingRole
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MarkingRoleUpdate(pydantic.BaseModel):
    """MarkingRoleUpdate"""

    role: MarkingRole
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


MarkingType = typing.Literal["MANDATORY", "CBAC"]
"""MarkingType"""


class OidcAuthenticationProtocol(pydantic.BaseModel):
    """OidcAuthenticationProtocol"""

    type: typing.Literal["oidc"] = "oidc"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Organization(pydantic.BaseModel):
    """Organization"""

    rid: core_models.OrganizationRid
    name: OrganizationName
    description: typing.Optional[str] = None
    marking_id: core_models.MarkingId = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]
    """
    The ID of this Organization's underlying marking. Organization guest access can be managed
    by updating the membership of this Marking.
    """

    host: typing.Optional[HostName] = None
    """
    The primary host name of the Organization. This should be used when constructing URLs for users of this
    Organization.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


OrganizationName = str
"""OrganizationName"""


class OrganizationRoleAssignment(pydantic.BaseModel):
    """OrganizationRoleAssignment"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    role_id: core_models.RoleId = pydantic.Field(alias=str("roleId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


PrincipalFilterType = typing.Literal["queryString"]
"""PrincipalFilterType"""


ProviderId = str
"""A value that uniquely identifies a User or Group in an external authentication provider. This value is determined by the external authentication provider and must be unique per Realm."""


class Role(pydantic.BaseModel):
    """Role"""

    id: core_models.RoleId
    display_name: RoleDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: RoleDescription
    operations: typing.List[str]
    """A list of permissions that this role has."""

    can_assigns: typing.List[core_models.RoleId] = pydantic.Field(alias=str("canAssigns"))  # type: ignore[literal-required]
    """A list of roles that this role inherits."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


RoleDescription = str
"""RoleDescription"""


RoleDisplayName = str
"""RoleDisplayName"""


class SamlAuthenticationProtocol(pydantic.BaseModel):
    """SamlAuthenticationProtocol"""

    service_provider_metadata: SamlServiceProviderMetadata = pydantic.Field(alias=str("serviceProviderMetadata"))  # type: ignore[literal-required]
    type: typing.Literal["saml"] = "saml"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SamlServiceProviderMetadata(pydantic.BaseModel):
    """Information that describes a Foundry Authentication Provider as a SAML service provider. All information listed here is generated by Foundry."""

    entity_id: str = pydantic.Field(alias=str("entityId"))  # type: ignore[literal-required]
    """The static SAML entity ID that represents this service provider."""

    metadata_url: str = pydantic.Field(alias=str("metadataUrl"))  # type: ignore[literal-required]
    """A public URL from which this service provider metadata can be downloaded as XML."""

    acs_urls: typing.List[str] = pydantic.Field(alias=str("acsUrls"))  # type: ignore[literal-required]
    """
    The Assertion Consumer Service (ACS) URLs for this service provider, to which the SAML identity provider
    redirects authentication responses.
    """

    logout_urls: typing.List[str] = pydantic.Field(alias=str("logoutUrls"))  # type: ignore[literal-required]
    """The URLs for this service provider to which the SAML identity provider sends logout requests."""

    certificates: typing.List[CertificateInfo]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SearchGroupsResponse(pydantic.BaseModel):
    """SearchGroupsResponse"""

    data: typing.List[Group]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SearchUsersResponse(pydantic.BaseModel):
    """SearchUsersResponse"""

    data: typing.List[User]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class User(pydantic.BaseModel):
    """User"""

    id: core_models.PrincipalId
    username: UserUsername
    """The Foundry username of the User. This is unique within the realm."""

    given_name: typing.Optional[str] = pydantic.Field(alias=str("givenName"), default=None)  # type: ignore[literal-required]
    """The given name of the User."""

    family_name: typing.Optional[str] = pydantic.Field(alias=str("familyName"), default=None)  # type: ignore[literal-required]
    """The family name (last name) of the User."""

    email: typing.Optional[str] = None
    """The email at which to contact a User. Multiple users may have the same email address."""

    realm: core_models.Realm
    organization: typing.Optional[core_models.OrganizationRid] = None
    """The RID of the user's primary Organization. This will be blank for third-party application service users."""

    attributes: typing.Dict[AttributeName, AttributeValues]
    """
    A map of the User's attributes. Attributes prefixed with "multipass:" are reserved for internal use by
    Foundry and are subject to change. Additional attributes may be configured by Foundry administrators in 
    Control Panel and populated by the User's SSO provider upon login.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class UserProviderInfo(pydantic.BaseModel):
    """UserProviderInfo"""

    provider_id: ProviderId = pydantic.Field(alias=str("providerId"))  # type: ignore[literal-required]
    """
    The ID of the User in the external authentication provider. This value is determined by the authentication provider.
    At most one User can have a given provider ID in a given Realm.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class UserSearchFilter(pydantic.BaseModel):
    """UserSearchFilter"""

    type: PrincipalFilterType
    value: str
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


UserUsername = str
"""The Foundry username of the User. This is unique within the realm."""


core.resolve_forward_references(AttributeValues, globalns=globals(), localns=locals())
core.resolve_forward_references(AuthenticationProtocol, globalns=globals(), localns=locals())

__all__ = [
    "AttributeName",
    "AttributeValue",
    "AttributeValues",
    "AuthenticationProtocol",
    "AuthenticationProvider",
    "AuthenticationProviderEnabled",
    "AuthenticationProviderName",
    "AuthenticationProviderRid",
    "CertificateInfo",
    "CertificateUsageType",
    "Enrollment",
    "EnrollmentName",
    "GetGroupsBatchRequestElement",
    "GetGroupsBatchResponse",
    "GetMarkingsBatchRequestElement",
    "GetMarkingsBatchResponse",
    "GetRolesBatchRequestElement",
    "GetRolesBatchResponse",
    "GetUserMarkingsResponse",
    "GetUsersBatchRequestElement",
    "GetUsersBatchResponse",
    "Group",
    "GroupMember",
    "GroupMembership",
    "GroupMembershipExpiration",
    "GroupName",
    "GroupProviderInfo",
    "GroupSearchFilter",
    "Host",
    "HostName",
    "ListAuthenticationProvidersResponse",
    "ListAvailableOrganizationRolesResponse",
    "ListGroupMembersResponse",
    "ListGroupMembershipsResponse",
    "ListGroupsResponse",
    "ListHostsResponse",
    "ListMarkingCategoriesResponse",
    "ListMarkingMembersResponse",
    "ListMarkingRoleAssignmentsResponse",
    "ListMarkingsResponse",
    "ListOrganizationRoleAssignmentsResponse",
    "ListUsersResponse",
    "Marking",
    "MarkingCategory",
    "MarkingCategoryId",
    "MarkingCategoryName",
    "MarkingCategoryType",
    "MarkingMember",
    "MarkingName",
    "MarkingRole",
    "MarkingRoleAssignment",
    "MarkingRoleUpdate",
    "MarkingType",
    "OidcAuthenticationProtocol",
    "Organization",
    "OrganizationName",
    "OrganizationRoleAssignment",
    "PrincipalFilterType",
    "ProviderId",
    "Role",
    "RoleDescription",
    "RoleDisplayName",
    "SamlAuthenticationProtocol",
    "SamlServiceProviderMetadata",
    "SearchGroupsResponse",
    "SearchUsersResponse",
    "User",
    "UserProviderInfo",
    "UserSearchFilter",
    "UserUsername",
]
