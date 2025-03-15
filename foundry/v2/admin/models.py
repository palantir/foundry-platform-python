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

AttributeName = str
"""AttributeName"""


AttributeValue = str
"""AttributeValue"""


AttributeValues = typing.List["AttributeValue"]
"""AttributeValues"""


AuthenticationProtocol = typing_extensions.Annotated[
    typing.Union["SamlAuthenticationProtocol", "OidcAuthenticationProtocol"],
    pydantic.Field(discriminator="type"),
]
"""AuthenticationProtocol"""


AuthenticationProtocolDict = typing_extensions.Annotated[
    typing.Union["SamlAuthenticationProtocolDict", "OidcAuthenticationProtocolDict"],
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

    def to_dict(self) -> "AuthenticationProviderDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            AuthenticationProviderDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class AuthenticationProviderDict(typing_extensions.TypedDict):
    """AuthenticationProvider"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: AuthenticationProviderRid
    name: AuthenticationProviderName
    realm: core_models.Realm
    enabled: AuthenticationProviderEnabled
    """Whether users can log in using this provider."""

    supportedHosts: typing.List[HostName]
    """This provider can only be utilized from these hosts."""

    supportedUsernamePatterns: typing.List[str]
    """Users who enter usernames that match these patterns will be redirected to this authentication provider."""

    protocol: AuthenticationProtocolDict


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
    expiry_date: datetime = pydantic.Field(alias=str("expiryDate"))  # type: ignore[literal-required]
    usage_type: CertificateUsageType = pydantic.Field(alias=str("usageType"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "CertificateInfoDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(CertificateInfoDict, self.model_dump(by_alias=True, exclude_none=True))


class CertificateInfoDict(typing_extensions.TypedDict):
    """CertificateInfo"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    pemCertificate: str
    """The certificate, in PEM format."""

    commonName: typing_extensions.NotRequired[str]
    expiryDate: datetime
    usageType: CertificateUsageType


CertificateUsageType = typing.Literal["ENCRYPTION", "SIGNING", "UNSPECIFIED"]
"""CertificateUsageType"""


class Enrollment(pydantic.BaseModel):
    """Enrollment"""

    rid: core_models.EnrollmentRid
    name: EnrollmentName
    created_time: typing.Optional[core_models.CreatedTime] = pydantic.Field(alias=str("createdTime"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "EnrollmentDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(EnrollmentDict, self.model_dump(by_alias=True, exclude_none=True))


class EnrollmentDict(typing_extensions.TypedDict):
    """Enrollment"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: core_models.EnrollmentRid
    name: EnrollmentName
    createdTime: typing_extensions.NotRequired[core_models.CreatedTime]


EnrollmentName = str
"""EnrollmentName"""


class GetGroupsBatchRequestElement(pydantic.BaseModel):
    """GetGroupsBatchRequestElement"""

    group_id: core_models.PrincipalId = pydantic.Field(alias=str("groupId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GetGroupsBatchRequestElementDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GetGroupsBatchRequestElementDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GetGroupsBatchRequestElementDict(typing_extensions.TypedDict):
    """GetGroupsBatchRequestElement"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.PrincipalId


class GetGroupsBatchResponse(pydantic.BaseModel):
    """GetGroupsBatchResponse"""

    data: typing.Dict[core_models.PrincipalId, Group]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GetGroupsBatchResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GetGroupsBatchResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GetGroupsBatchResponseDict(typing_extensions.TypedDict):
    """GetGroupsBatchResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.Dict[core_models.PrincipalId, GroupDict]


class GetMarkingsBatchRequestElement(pydantic.BaseModel):
    """GetMarkingsBatchRequestElement"""

    marking_id: core_models.MarkingId = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GetMarkingsBatchRequestElementDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GetMarkingsBatchRequestElementDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GetMarkingsBatchRequestElementDict(typing_extensions.TypedDict):
    """GetMarkingsBatchRequestElement"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingId: core_models.MarkingId


class GetMarkingsBatchResponse(pydantic.BaseModel):
    """GetMarkingsBatchResponse"""

    data: typing.Dict[core_models.MarkingId, Marking]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GetMarkingsBatchResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GetMarkingsBatchResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GetMarkingsBatchResponseDict(typing_extensions.TypedDict):
    """GetMarkingsBatchResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.Dict[core_models.MarkingId, MarkingDict]


class GetUserMarkingsResponse(pydantic.BaseModel):
    """GetUserMarkingsResponse"""

    view: typing.List[core_models.MarkingId]
    """
    The markings that the user has access to. The user will be able to access resources protected with these
    markings. This includes organization markings for organizations in which the user is a guest member.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GetUserMarkingsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GetUserMarkingsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GetUserMarkingsResponseDict(typing_extensions.TypedDict):
    """GetUserMarkingsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    view: typing.List[core_models.MarkingId]
    """
    The markings that the user has access to. The user will be able to access resources protected with these
    markings. This includes organization markings for organizations in which the user is a guest member.
    """


class GetUsersBatchRequestElement(pydantic.BaseModel):
    """GetUsersBatchRequestElement"""

    user_id: core_models.PrincipalId = pydantic.Field(alias=str("userId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GetUsersBatchRequestElementDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GetUsersBatchRequestElementDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GetUsersBatchRequestElementDict(typing_extensions.TypedDict):
    """GetUsersBatchRequestElement"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    userId: core_models.PrincipalId


class GetUsersBatchResponse(pydantic.BaseModel):
    """GetUsersBatchResponse"""

    data: typing.Dict[core_models.PrincipalId, User]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GetUsersBatchResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            GetUsersBatchResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class GetUsersBatchResponseDict(typing_extensions.TypedDict):
    """GetUsersBatchResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.Dict[core_models.PrincipalId, UserDict]


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

    def to_dict(self) -> "GroupDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GroupDict, self.model_dump(by_alias=True, exclude_none=True))


class GroupDict(typing_extensions.TypedDict):
    """Group"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    id: core_models.PrincipalId
    name: GroupName
    """The name of the Group."""

    description: typing_extensions.NotRequired[str]
    """A description of the Group."""

    realm: core_models.Realm
    organizations: typing.List[core_models.OrganizationRid]
    """The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed."""

    attributes: typing.Dict[AttributeName, AttributeValues]
    """A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change."""


class GroupMember(pydantic.BaseModel):
    """GroupMember"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GroupMemberDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GroupMemberDict, self.model_dump(by_alias=True, exclude_none=True))


class GroupMemberDict(typing_extensions.TypedDict):
    """GroupMember"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    principalType: core_models.PrincipalType
    principalId: core_models.PrincipalId


class GroupMembership(pydantic.BaseModel):
    """GroupMembership"""

    group_id: core_models.PrincipalId = pydantic.Field(alias=str("groupId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GroupMembershipDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GroupMembershipDict, self.model_dump(by_alias=True, exclude_none=True))


class GroupMembershipDict(typing_extensions.TypedDict):
    """GroupMembership"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.PrincipalId


GroupMembershipExpiration = datetime
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

    def to_dict(self) -> "GroupProviderInfoDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GroupProviderInfoDict, self.model_dump(by_alias=True, exclude_none=True))


class GroupProviderInfoDict(typing_extensions.TypedDict):
    """GroupProviderInfo"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    providerId: ProviderId
    """
    The ID of the Group in the external authentication provider. This value is determined by the authentication provider.
    At most one Group can have a given provider ID in a given Realm.
    """


class GroupSearchFilter(pydantic.BaseModel):
    """GroupSearchFilter"""

    type: PrincipalFilterType
    value: str
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "GroupSearchFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(GroupSearchFilterDict, self.model_dump(by_alias=True, exclude_none=True))


class GroupSearchFilterDict(typing_extensions.TypedDict):
    """GroupSearchFilter"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: PrincipalFilterType
    value: str


class Host(pydantic.BaseModel):
    """Host"""

    host_name: HostName = pydantic.Field(alias=str("hostName"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "HostDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(HostDict, self.model_dump(by_alias=True, exclude_none=True))


class HostDict(typing_extensions.TypedDict):
    """Host"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    hostName: HostName


HostName = str
"""HostName"""


class ListAuthenticationProvidersResponse(pydantic.BaseModel):
    """ListAuthenticationProvidersResponse"""

    data: typing.List[AuthenticationProvider]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListAuthenticationProvidersResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListAuthenticationProvidersResponseDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class ListAuthenticationProvidersResponseDict(typing_extensions.TypedDict):
    """ListAuthenticationProvidersResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[AuthenticationProviderDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListGroupMembersResponse(pydantic.BaseModel):
    """ListGroupMembersResponse"""

    data: typing.List[GroupMember]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListGroupMembersResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListGroupMembersResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListGroupMembersResponseDict(typing_extensions.TypedDict):
    """ListGroupMembersResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[GroupMemberDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListGroupMembershipsResponse(pydantic.BaseModel):
    """ListGroupMembershipsResponse"""

    data: typing.List[GroupMembership]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListGroupMembershipsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListGroupMembershipsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListGroupMembershipsResponseDict(typing_extensions.TypedDict):
    """ListGroupMembershipsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[GroupMembershipDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListGroupsResponse(pydantic.BaseModel):
    """ListGroupsResponse"""

    data: typing.List[Group]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListGroupsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListGroupsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListGroupsResponseDict(typing_extensions.TypedDict):
    """ListGroupsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[GroupDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListHostsResponse(pydantic.BaseModel):
    """ListHostsResponse"""

    data: typing.List[Host]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListHostsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ListHostsResponseDict, self.model_dump(by_alias=True, exclude_none=True))


class ListHostsResponseDict(typing_extensions.TypedDict):
    """ListHostsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[HostDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListMarkingCategoriesResponse(pydantic.BaseModel):
    """ListMarkingCategoriesResponse"""

    data: typing.List[MarkingCategory]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListMarkingCategoriesResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListMarkingCategoriesResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListMarkingCategoriesResponseDict(typing_extensions.TypedDict):
    """ListMarkingCategoriesResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[MarkingCategoryDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListMarkingMembersResponse(pydantic.BaseModel):
    """ListMarkingMembersResponse"""

    data: typing.List[MarkingMember]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListMarkingMembersResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListMarkingMembersResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListMarkingMembersResponseDict(typing_extensions.TypedDict):
    """ListMarkingMembersResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[MarkingMemberDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListMarkingRoleAssignmentsResponse(pydantic.BaseModel):
    """ListMarkingRoleAssignmentsResponse"""

    data: typing.List[MarkingRoleAssignment]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListMarkingRoleAssignmentsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListMarkingRoleAssignmentsResponseDict,
            self.model_dump(by_alias=True, exclude_none=True),
        )


class ListMarkingRoleAssignmentsResponseDict(typing_extensions.TypedDict):
    """ListMarkingRoleAssignmentsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[MarkingRoleAssignmentDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListMarkingsResponse(pydantic.BaseModel):
    """ListMarkingsResponse"""

    data: typing.List[Marking]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListMarkingsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            ListMarkingsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class ListMarkingsResponseDict(typing_extensions.TypedDict):
    """ListMarkingsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[MarkingDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class ListUsersResponse(pydantic.BaseModel):
    """ListUsersResponse"""

    data: typing.List[User]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "ListUsersResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(ListUsersResponseDict, self.model_dump(by_alias=True, exclude_none=True))


class ListUsersResponseDict(typing_extensions.TypedDict):
    """ListUsersResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[UserDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


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

    def to_dict(self) -> "MarkingDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MarkingDict, self.model_dump(by_alias=True, exclude_none=True))


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

    def to_dict(self) -> "MarkingCategoryDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MarkingCategoryDict, self.model_dump(by_alias=True, exclude_none=True))


class MarkingCategoryDict(typing_extensions.TypedDict):
    """MarkingCategory"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    id: MarkingCategoryId
    name: MarkingCategoryName
    description: typing_extensions.NotRequired[str]
    categoryType: MarkingCategoryType
    markingType: MarkingType
    markings: typing.List[core_models.MarkingId]
    createdTime: core_models.CreatedTime
    createdBy: typing_extensions.NotRequired[core_models.CreatedBy]


MarkingCategoryId = str
"""
The ID of a marking category. For user-created categories, this will be a UUID. Markings associated with
Organizations are placed in a category with ID "Organization".
"""


MarkingCategoryName = str
"""MarkingCategoryName"""


MarkingCategoryType = typing.Literal["CONJUNCTIVE", "DISJUNCTIVE"]
"""MarkingCategoryType"""


class MarkingDict(typing_extensions.TypedDict):
    """Marking"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    id: core_models.MarkingId
    categoryId: MarkingCategoryId
    name: MarkingName
    description: typing_extensions.NotRequired[str]
    organization: typing_extensions.NotRequired[core_models.OrganizationRid]
    """If this marking is associated with an Organization, its RID will be populated here."""

    createdTime: core_models.CreatedTime
    createdBy: typing_extensions.NotRequired[core_models.CreatedBy]


class MarkingMember(pydantic.BaseModel):
    """MarkingMember"""

    principal_type: core_models.PrincipalType = pydantic.Field(alias=str("principalType"))  # type: ignore[literal-required]
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MarkingMemberDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MarkingMemberDict, self.model_dump(by_alias=True, exclude_none=True))


class MarkingMemberDict(typing_extensions.TypedDict):
    """MarkingMember"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    principalType: core_models.PrincipalType
    principalId: core_models.PrincipalId


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

    def to_dict(self) -> "MarkingRoleAssignmentDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            MarkingRoleAssignmentDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class MarkingRoleAssignmentDict(typing_extensions.TypedDict):
    """MarkingRoleAssignment"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    principalType: core_models.PrincipalType
    principalId: core_models.PrincipalId
    role: MarkingRole


class MarkingRoleUpdate(pydantic.BaseModel):
    """MarkingRoleUpdate"""

    role: MarkingRole
    principal_id: core_models.PrincipalId = pydantic.Field(alias=str("principalId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "MarkingRoleUpdateDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(MarkingRoleUpdateDict, self.model_dump(by_alias=True, exclude_none=True))


class MarkingRoleUpdateDict(typing_extensions.TypedDict):
    """MarkingRoleUpdate"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    role: MarkingRole
    principalId: core_models.PrincipalId


MarkingType = typing.Literal["MANDATORY", "CBAC"]
"""MarkingType"""


class OidcAuthenticationProtocol(pydantic.BaseModel):
    """OidcAuthenticationProtocol"""

    type: typing.Literal["oidc"] = "oidc"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "OidcAuthenticationProtocolDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            OidcAuthenticationProtocolDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class OidcAuthenticationProtocolDict(typing_extensions.TypedDict):
    """OidcAuthenticationProtocol"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: typing.Literal["oidc"]


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

    def to_dict(self) -> "OrganizationDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(OrganizationDict, self.model_dump(by_alias=True, exclude_none=True))


class OrganizationDict(typing_extensions.TypedDict):
    """Organization"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: core_models.OrganizationRid
    name: OrganizationName
    description: typing_extensions.NotRequired[str]
    markingId: core_models.MarkingId
    """
    The ID of this Organization's underlying marking. Organization guest access can be managed
    by updating the membership of this Marking.
    """

    host: typing_extensions.NotRequired[HostName]
    """
    The primary host name of the Organization. This should be used when constructing URLs for users of this
    Organization.
    """


OrganizationName = str
"""OrganizationName"""


PrincipalFilterType = typing.Literal["queryString"]
"""PrincipalFilterType"""


ProviderId = str
"""A value that uniquely identifies a User or Group in an external authentication provider. This value is determined by the external authentication provider and must be unique per Realm."""


class SamlAuthenticationProtocol(pydantic.BaseModel):
    """SamlAuthenticationProtocol"""

    service_provider_metadata: SamlServiceProviderMetadata = pydantic.Field(alias=str("serviceProviderMetadata"))  # type: ignore[literal-required]
    type: typing.Literal["saml"] = "saml"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SamlAuthenticationProtocolDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SamlAuthenticationProtocolDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SamlAuthenticationProtocolDict(typing_extensions.TypedDict):
    """SamlAuthenticationProtocol"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    serviceProviderMetadata: SamlServiceProviderMetadataDict
    type: typing.Literal["saml"]


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

    def to_dict(self) -> "SamlServiceProviderMetadataDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SamlServiceProviderMetadataDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SamlServiceProviderMetadataDict(typing_extensions.TypedDict):
    """Information that describes a Foundry Authentication Provider as a SAML service provider. All information listed here is generated by Foundry."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    entityId: str
    """The static SAML entity ID that represents this service provider."""

    metadataUrl: str
    """A public URL from which this service provider metadata can be downloaded as XML."""

    acsUrls: typing.List[str]
    """
    The Assertion Consumer Service (ACS) URLs for this service provider, to which the SAML identity provider
    redirects authentication responses.
    """

    logoutUrls: typing.List[str]
    """The URLs for this service provider to which the SAML identity provider sends logout requests."""

    certificates: typing.List[CertificateInfoDict]


class SearchGroupsResponse(pydantic.BaseModel):
    """SearchGroupsResponse"""

    data: typing.List[Group]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchGroupsResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchGroupsResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchGroupsResponseDict(typing_extensions.TypedDict):
    """SearchGroupsResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[GroupDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


class SearchUsersResponse(pydantic.BaseModel):
    """SearchUsersResponse"""

    data: typing.List[User]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "SearchUsersResponseDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(
            SearchUsersResponseDict, self.model_dump(by_alias=True, exclude_none=True)
        )


class SearchUsersResponseDict(typing_extensions.TypedDict):
    """SearchUsersResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    data: typing.List[UserDict]
    nextPageToken: typing_extensions.NotRequired[core_models.PageToken]


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

    def to_dict(self) -> "UserDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(UserDict, self.model_dump(by_alias=True, exclude_none=True))


class UserDict(typing_extensions.TypedDict):
    """User"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    id: core_models.PrincipalId
    username: UserUsername
    """The Foundry username of the User. This is unique within the realm."""

    givenName: typing_extensions.NotRequired[str]
    """The given name of the User."""

    familyName: typing_extensions.NotRequired[str]
    """The family name (last name) of the User."""

    email: typing_extensions.NotRequired[str]
    """The email at which to contact a User. Multiple users may have the same email address."""

    realm: core_models.Realm
    organization: typing_extensions.NotRequired[core_models.OrganizationRid]
    """The RID of the user's primary Organization. This will be blank for third-party application service users."""

    attributes: typing.Dict[AttributeName, AttributeValues]
    """
    A map of the User's attributes. Attributes prefixed with "multipass:" are reserved for internal use by
    Foundry and are subject to change. Additional attributes may be configured by Foundry administrators in 
    Control Panel and populated by the User's SSO provider upon login.
    """


class UserProviderInfo(pydantic.BaseModel):
    """UserProviderInfo"""

    provider_id: ProviderId = pydantic.Field(alias=str("providerId"))  # type: ignore[literal-required]
    """
    The ID of the User in the external authentication provider. This value is determined by the authentication provider.
    At most one User can have a given provider ID in a given Realm.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "UserProviderInfoDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(UserProviderInfoDict, self.model_dump(by_alias=True, exclude_none=True))


class UserProviderInfoDict(typing_extensions.TypedDict):
    """UserProviderInfo"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    providerId: ProviderId
    """
    The ID of the User in the external authentication provider. This value is determined by the authentication provider.
    At most one User can have a given provider ID in a given Realm.
    """


class UserSearchFilter(pydantic.BaseModel):
    """UserSearchFilter"""

    type: PrincipalFilterType
    value: str
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> "UserSearchFilterDict":
        """Return the dictionary representation of the model using the field aliases."""
        return typing.cast(UserSearchFilterDict, self.model_dump(by_alias=True, exclude_none=True))


class UserSearchFilterDict(typing_extensions.TypedDict):
    """UserSearchFilter"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    type: PrincipalFilterType
    value: str


UserUsername = str
"""The Foundry username of the User. This is unique within the realm."""


from foundry.v2.core import models as core_models  # noqa: E402

__all__ = [
    "AttributeName",
    "AttributeValue",
    "AttributeValues",
    "AuthenticationProtocol",
    "AuthenticationProtocolDict",
    "AuthenticationProvider",
    "AuthenticationProviderDict",
    "AuthenticationProviderEnabled",
    "AuthenticationProviderName",
    "AuthenticationProviderRid",
    "CertificateInfo",
    "CertificateInfoDict",
    "CertificateUsageType",
    "Enrollment",
    "EnrollmentDict",
    "EnrollmentName",
    "GetGroupsBatchRequestElement",
    "GetGroupsBatchRequestElementDict",
    "GetGroupsBatchResponse",
    "GetGroupsBatchResponseDict",
    "GetMarkingsBatchRequestElement",
    "GetMarkingsBatchRequestElementDict",
    "GetMarkingsBatchResponse",
    "GetMarkingsBatchResponseDict",
    "GetUserMarkingsResponse",
    "GetUserMarkingsResponseDict",
    "GetUsersBatchRequestElement",
    "GetUsersBatchRequestElementDict",
    "GetUsersBatchResponse",
    "GetUsersBatchResponseDict",
    "Group",
    "GroupDict",
    "GroupMember",
    "GroupMemberDict",
    "GroupMembership",
    "GroupMembershipDict",
    "GroupMembershipExpiration",
    "GroupName",
    "GroupProviderInfo",
    "GroupProviderInfoDict",
    "GroupSearchFilter",
    "GroupSearchFilterDict",
    "Host",
    "HostDict",
    "HostName",
    "ListAuthenticationProvidersResponse",
    "ListAuthenticationProvidersResponseDict",
    "ListGroupMembersResponse",
    "ListGroupMembersResponseDict",
    "ListGroupMembershipsResponse",
    "ListGroupMembershipsResponseDict",
    "ListGroupsResponse",
    "ListGroupsResponseDict",
    "ListHostsResponse",
    "ListHostsResponseDict",
    "ListMarkingCategoriesResponse",
    "ListMarkingCategoriesResponseDict",
    "ListMarkingMembersResponse",
    "ListMarkingMembersResponseDict",
    "ListMarkingRoleAssignmentsResponse",
    "ListMarkingRoleAssignmentsResponseDict",
    "ListMarkingsResponse",
    "ListMarkingsResponseDict",
    "ListUsersResponse",
    "ListUsersResponseDict",
    "Marking",
    "MarkingCategory",
    "MarkingCategoryDict",
    "MarkingCategoryId",
    "MarkingCategoryName",
    "MarkingCategoryType",
    "MarkingDict",
    "MarkingMember",
    "MarkingMemberDict",
    "MarkingName",
    "MarkingRole",
    "MarkingRoleAssignment",
    "MarkingRoleAssignmentDict",
    "MarkingRoleUpdate",
    "MarkingRoleUpdateDict",
    "MarkingType",
    "OidcAuthenticationProtocol",
    "OidcAuthenticationProtocolDict",
    "Organization",
    "OrganizationDict",
    "OrganizationName",
    "PrincipalFilterType",
    "ProviderId",
    "SamlAuthenticationProtocol",
    "SamlAuthenticationProtocolDict",
    "SamlServiceProviderMetadata",
    "SamlServiceProviderMetadataDict",
    "SearchGroupsResponse",
    "SearchGroupsResponseDict",
    "SearchUsersResponse",
    "SearchUsersResponseDict",
    "User",
    "UserDict",
    "UserProviderInfo",
    "UserProviderInfoDict",
    "UserSearchFilter",
    "UserSearchFilterDict",
    "UserUsername",
]
