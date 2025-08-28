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


class AuthenticationProvider(core.ModelBase):
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


AuthenticationProviderEnabled = bool
"""Whether users can log in using this provider."""


AuthenticationProviderName = str
"""AuthenticationProviderName"""


AuthenticationProviderRid = core.RID
"""AuthenticationProviderRid"""


class CertificateInfo(core.ModelBase):
    """CertificateInfo"""

    pem_certificate: str = pydantic.Field(alias=str("pemCertificate"))  # type: ignore[literal-required]
    """The certificate, in PEM format."""

    common_name: typing.Optional[str] = pydantic.Field(alias=str("commonName"), default=None)  # type: ignore[literal-required]
    expiry_date: core.AwareDatetime = pydantic.Field(alias=str("expiryDate"))  # type: ignore[literal-required]
    usage_type: CertificateUsageType = pydantic.Field(alias=str("usageType"))  # type: ignore[literal-required]


CertificateUsageType = typing.Literal["ENCRYPTION", "SIGNING", "UNSPECIFIED"]
"""CertificateUsageType"""


class Enrollment(core.ModelBase):
    """Enrollment"""

    rid: core_models.EnrollmentRid
    name: EnrollmentName
    created_time: typing.Optional[core_models.CreatedTime] = pydantic.Field(alias=str("createdTime"), default=None)  # type: ignore[literal-required]


EnrollmentName = str
"""EnrollmentName"""


class EnrollmentRoleAssignment(core.ModelBase):
    """EnrollmentRoleAssignment"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    role_id: core_models.RoleId = pydantic.Field(alias=str("roleId"))  # type: ignore[literal-required]


class GetGroupsBatchRequestElement(core.ModelBase):
    """GetGroupsBatchRequestElement"""

    group_id: core_models.GroupId = pydantic.Field(alias=str("groupId"))  # type: ignore[literal-required]


class GetGroupsBatchResponse(core.ModelBase):
    """GetGroupsBatchResponse"""

    data: typing.Dict[core_models.GroupId, Group]


class GetMarkingsBatchRequestElement(core.ModelBase):
    """GetMarkingsBatchRequestElement"""

    marking_id: core_models.MarkingId = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]


class GetMarkingsBatchResponse(core.ModelBase):
    """GetMarkingsBatchResponse"""

    data: typing.Dict[core_models.MarkingId, Marking]


class GetRolesBatchRequestElement(core.ModelBase):
    """GetRolesBatchRequestElement"""

    role_id: core_models.RoleId = pydantic.Field(alias=str("roleId"))  # type: ignore[literal-required]


class GetRolesBatchResponse(core.ModelBase):
    """GetRolesBatchResponse"""

    data: typing.Dict[core_models.RoleId, Role]


class GetUserMarkingsResponse(core.ModelBase):
    """GetUserMarkingsResponse"""

    view: typing.List[core_models.MarkingId]
    """
    The markings that the user has access to. The user will be able to access resources protected with these
    markings. This includes organization markings for organizations in which the user is a guest member.
    """


class GetUsersBatchRequestElement(core.ModelBase):
    """GetUsersBatchRequestElement"""

    user_id: core_models.UserId = pydantic.Field(alias=str("userId"))  # type: ignore[literal-required]


class GetUsersBatchResponse(core.ModelBase):
    """GetUsersBatchResponse"""

    data: typing.Dict[core_models.UserId, User]


class Group(core.ModelBase):
    """Group"""

    id: core_models.GroupId
    name: GroupName
    """The name of the Group."""

    description: typing.Optional[str] = None
    """A description of the Group."""

    realm: core_models.Realm
    organizations: typing.List[core_models.OrganizationRid]
    """The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed."""

    attributes: typing.Dict[AttributeName, AttributeValues]
    """A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change."""


class GroupMember(core.ModelBase):
    """GroupMember"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]


class GroupMembership(core.ModelBase):
    """GroupMembership"""

    group_id: core_models.GroupId = pydantic.Field(alias=str("groupId"))  # type: ignore[literal-required]


GroupMembershipExpiration = core.AwareDatetime
"""GroupMembershipExpiration"""


class GroupMembershipExpirationPolicy(core.ModelBase):
    """GroupMembershipExpirationPolicy"""

    maximum_value: typing.Optional[GroupMembershipExpiration] = pydantic.Field(alias=str("maximumValue"), default=None)  # type: ignore[literal-required]
    """Members in this group must be added with expiration times that occur before this value."""

    maximum_duration: typing.Optional[core_models.DurationSeconds] = pydantic.Field(alias=str("maximumDuration"), default=None)  # type: ignore[literal-required]
    """Members in this group must be added with expirations that are less than this duration in seconds into the future from the time they are added."""


GroupName = str
"""The name of the Group."""


class GroupProviderInfo(core.ModelBase):
    """GroupProviderInfo"""

    provider_id: ProviderId = pydantic.Field(alias=str("providerId"))  # type: ignore[literal-required]
    """
    The ID of the Group in the external authentication provider. This value is determined by the authentication provider.
    At most one Group can have a given provider ID in a given Realm.
    """


class GroupSearchFilter(core.ModelBase):
    """GroupSearchFilter"""

    type: PrincipalFilterType
    value: str


class Host(core.ModelBase):
    """Host"""

    host_name: HostName = pydantic.Field(alias=str("hostName"))  # type: ignore[literal-required]


HostName = str
"""HostName"""


class ListAuthenticationProvidersResponse(core.ModelBase):
    """ListAuthenticationProvidersResponse"""

    data: typing.List[AuthenticationProvider]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListAvailableOrganizationRolesResponse(core.ModelBase):
    """ListAvailableOrganizationRolesResponse"""

    data: typing.List[core_models.Role]


class ListEnrollmentRoleAssignmentsResponse(core.ModelBase):
    """ListEnrollmentRoleAssignmentsResponse"""

    data: typing.List[EnrollmentRoleAssignment]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListGroupMembersResponse(core.ModelBase):
    """ListGroupMembersResponse"""

    data: typing.List[GroupMember]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListGroupMembershipsResponse(core.ModelBase):
    """ListGroupMembershipsResponse"""

    data: typing.List[GroupMembership]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListGroupsResponse(core.ModelBase):
    """ListGroupsResponse"""

    data: typing.List[Group]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListHostsResponse(core.ModelBase):
    """ListHostsResponse"""

    data: typing.List[Host]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListMarkingCategoriesResponse(core.ModelBase):
    """ListMarkingCategoriesResponse"""

    data: typing.List[MarkingCategory]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListMarkingMembersResponse(core.ModelBase):
    """ListMarkingMembersResponse"""

    data: typing.List[MarkingMember]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListMarkingRoleAssignmentsResponse(core.ModelBase):
    """ListMarkingRoleAssignmentsResponse"""

    data: typing.List[MarkingRoleAssignment]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListMarkingsResponse(core.ModelBase):
    """ListMarkingsResponse"""

    data: typing.List[Marking]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListOrganizationRoleAssignmentsResponse(core.ModelBase):
    """ListOrganizationRoleAssignmentsResponse"""

    data: typing.List[OrganizationRoleAssignment]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListUsersResponse(core.ModelBase):
    """ListUsersResponse"""

    data: typing.List[User]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class Marking(core.ModelBase):
    """Marking"""

    id: core_models.MarkingId
    category_id: MarkingCategoryId = pydantic.Field(alias=str("categoryId"))  # type: ignore[literal-required]
    name: MarkingName
    description: typing.Optional[str] = None
    organization: typing.Optional[core_models.OrganizationRid] = None
    """If this marking is associated with an Organization, its RID will be populated here."""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    created_by: typing.Optional[core_models.CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)  # type: ignore[literal-required]


class MarkingCategory(core.ModelBase):
    """MarkingCategory"""

    id: MarkingCategoryId
    name: MarkingCategoryName
    description: typing.Optional[str] = None
    category_type: MarkingCategoryType = pydantic.Field(alias=str("categoryType"))  # type: ignore[literal-required]
    marking_type: MarkingType = pydantic.Field(alias=str("markingType"))  # type: ignore[literal-required]
    markings: typing.List[core_models.MarkingId]
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    created_by: typing.Optional[core_models.CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)  # type: ignore[literal-required]


MarkingCategoryId = str
"""
The ID of a marking category. For user-created categories, this will be a UUID. Markings associated with
Organizations are placed in a category with ID "Organization".
"""


MarkingCategoryName = str
"""MarkingCategoryName"""


MarkingCategoryType = typing.Literal["CONJUNCTIVE", "DISJUNCTIVE"]
"""MarkingCategoryType"""


class MarkingMember(core.ModelBase):
    """MarkingMember"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]


MarkingName = str
"""MarkingName"""


MarkingRole = typing.Literal["ADMINISTER", "DECLASSIFY", "USE"]
"""
Represents the operations that a user can perform with regards to a Marking.
  * ADMINISTER: The user can add and remove members from the Marking, update Marking Role Assignments, and change Marking metadata.
  * DECLASSIFY: The user can remove the Marking from resources in the platform and stop the propagation of the Marking during a transform.
  * USE: The user can apply the marking to resources in the platform.
"""


class MarkingRoleAssignment(core.ModelBase):
    """MarkingRoleAssignment"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    role: MarkingRole


class MarkingRoleUpdate(core.ModelBase):
    """MarkingRoleUpdate"""

    role: MarkingRole
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]


MarkingType = typing.Literal["MANDATORY", "CBAC"]
"""MarkingType"""


class OidcAuthenticationProtocol(core.ModelBase):
    """OidcAuthenticationProtocol"""

    type: typing.Literal["oidc"] = "oidc"


class Organization(core.ModelBase):
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


OrganizationName = str
"""OrganizationName"""


class OrganizationRoleAssignment(core.ModelBase):
    """OrganizationRoleAssignment"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    role_id: core_models.RoleId = pydantic.Field(alias=str("roleId"))  # type: ignore[literal-required]


PrincipalFilterType = typing.Literal["queryString"]
"""PrincipalFilterType"""


ProviderId = str
"""A value that uniquely identifies a User or Group in an external authentication provider. This value is determined by the external authentication provider and must be unique per Realm."""


class Role(core.ModelBase):
    """Role"""

    id: core_models.RoleId
    display_name: RoleDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: RoleDescription
    operations: typing.List[str]
    """A list of permissions that this role has."""

    can_assigns: typing.List[core_models.RoleId] = pydantic.Field(alias=str("canAssigns"))  # type: ignore[literal-required]
    """A list of roles that this role inherits."""


RoleDescription = str
"""RoleDescription"""


RoleDisplayName = str
"""RoleDisplayName"""


class SamlAuthenticationProtocol(core.ModelBase):
    """SamlAuthenticationProtocol"""

    service_provider_metadata: SamlServiceProviderMetadata = pydantic.Field(alias=str("serviceProviderMetadata"))  # type: ignore[literal-required]
    type: typing.Literal["saml"] = "saml"


class SamlServiceProviderMetadata(core.ModelBase):
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


class SearchGroupsResponse(core.ModelBase):
    """SearchGroupsResponse"""

    data: typing.List[Group]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class SearchUsersResponse(core.ModelBase):
    """SearchUsersResponse"""

    data: typing.List[User]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class User(core.ModelBase):
    """User"""

    id: core_models.UserId
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


class UserProviderInfo(core.ModelBase):
    """UserProviderInfo"""

    provider_id: ProviderId = pydantic.Field(alias=str("providerId"))  # type: ignore[literal-required]
    """
    The ID of the User in the external authentication provider. This value is determined by the authentication provider.
    At most one User can have a given provider ID in a given Realm.
    """


class UserSearchFilter(core.ModelBase):
    """UserSearchFilter"""

    type: PrincipalFilterType
    value: str


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
    "EnrollmentRoleAssignment",
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
    "GroupMembershipExpirationPolicy",
    "GroupName",
    "GroupProviderInfo",
    "GroupSearchFilter",
    "Host",
    "HostName",
    "ListAuthenticationProvidersResponse",
    "ListAvailableOrganizationRolesResponse",
    "ListEnrollmentRoleAssignmentsResponse",
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
