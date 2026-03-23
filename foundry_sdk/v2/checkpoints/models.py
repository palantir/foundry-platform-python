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


class AcknowledgementJustification(core.ModelBase):
    """Checkpoint justification that requires the user to mark a checkbox."""

    prompt: str
    """Prompt acknowledged by the user."""

    description: typing.Optional[str] = None
    """Supplemental information that helps users understand the prompt."""

    title: str
    """Title of the checkpoint the user is acknowledging."""

    type: typing.Literal["acknowledgementJustification"] = "acknowledgementJustification"


class ActingUser(core.ModelBase):
    """User that performed the checkpoint action."""

    user_id: core_models.UserId = pydantic.Field(alias=str("userId"))  # type: ignore[literal-required]
    username: RedactableString
    organization_rid: typing.Optional[OrganizationRid] = pydantic.Field(alias=str("organizationRid"), default=None)  # type: ignore[literal-required]


class ApprovalsMetadata(core.ModelBase):
    """Metadata linking a checkpoint record to an Approvals workflow."""

    approvals_task_id: ApprovalsTaskId = pydantic.Field(alias=str("approvalsTaskId"))  # type: ignore[literal-required]
    approvals_subtask_ids: typing.List[ApprovalsSubtaskId] = pydantic.Field(alias=str("approvalsSubtaskIds"))  # type: ignore[literal-required]


ApprovalsSubtaskId = str
"""Identifier of an Approvals subtask tied to the checkpoint."""


ApprovalsTaskId = str
"""Identifier of an Approvals task tied to the checkpoint."""


CheckpointType = typing.Literal[
    "CONTOUR_CREATE",
    "CONTOUR_EXPORT",
    "HUBBLE_EXPORT",
    "COMPASS_IMPORT",
    "COMPASS_EXPORT",
    "COMPASS_ADD_REFERENCE",
    "COMPASS_AUTHORIZE_MARKING_ON_PROJECT",
    "COMPASS_ADD_ROLE_GRANT",
    "COMPASS_REMOVE_REFERENCE",
    "COMPASS_REMOVE_AUTHORIZED_MARKING_FROM_PROJECT",
    "COMPASS_REMOVE_ROLE_GRANT",
    "DATA_CONNECTION_SYNC_CREATE",
    "DATA_CONNECTION_SYNC_BULK_CREATE",
    "DATA_CONNECTION_SYNC_EDIT",
    "DATA_CONNECTION_SOURCE_SHARE",
    "LOGIN",
    "REPORT_EXPORT",
    "CIPHER_ENCRYPT",
    "CIPHER_DECRYPT",
    "ATTACHMENT_IMPORT",
    "ATTACHMENT_EXPORT",
    "SLATE_EXPORT",
    "NOTEPAD_EXPORT",
    "QUIVER_EXPORT",
    "DATA_LIFETIME_APPLY_RETENTION_POLICY",
    "FRONTEND_EXPORT",
    "BUILD_LOG_EXPORT",
    "CODE_REPOSITORY_LOG_EXPORT",
    "CODE_REPOSITORY_MODIFY_APPROVAL_POLICY",
    "CODE_REPOSITORY_MERGE_PULL_REQUEST",
    "CODE_REPOSITORY_BUILD",
    "CODE_WORKBOOK_BUILD",
    "SCHEDULE_CREATE",
    "SCHEDULE_MODIFY",
    "SCHEDULE_RUN",
    "SCHEDULE_DELETE",
    "RUN_BUILD",
    "MULTIPASS_TOKEN_CREATE",
    "MULTIPASS_ADD_GROUP_MEMBER",
    "MULTIPASS_ADD_MARKING_MEMBER",
    "MULTIPASS_REMOVE_GROUP_MEMBER",
    "MULTIPASS_REMOVE_MARKING_MEMBER",
    "MULTIPASS_UPDATE_GROUP_MEMBERSHIP_EXPIRATION_CONFIG",
    "MULTIPASS_UPDATE_GROUP_MEMBER_EXPIRY",
    "SCOPED_SESSION_SELECT",
    "CODE_WORKSPACE_LOG_EXPORT",
    "CODE_WORKSPACE_MOVE_DATA_FROM_FOUNDRY",
    "CODE_WORKSPACE_MOVE_DATA_TO_FOUNDRY",
    "MANAGE_CODE_WORKSPACE_DASHBOARD_DOWNLOADS",
    "NOTEPAD_MEDIA_IMPORT",
    "CONTOUR_DASHBOARD_EXPORT",
    "PACKAGE_PRODUCT",
    "NOTEPAD_WIDGET_SNAPSHOT",
    "MEDIA_SET_IMPORT",
    "MEDIA_SET_EXPORT",
    "UPGRADE_ASSISTANT_SUMMARY_EXPORT",
    "TABLES_REGISTRATION_AUTOMATIC",
    "TABLES_REGISTRATION_MANUAL",
    "DEV_CONSOLE_OPENAPI_SPECIFICATION_EXPORT",
    "DEV_CONSOLE_USAGE_EXPORT",
    "DEPLOY_PIPELINE",
    "PIPELINE_BUILDER_MERGE_PROPOSAL",
    "PIPELINE_BUILDER_MODIFY_APPROVAL_POLICY",
    "PIPELINE_BUILDER_ARCHIVE_BRANCHES",
    "PIPELINE_BUILDER_MODIFY_FALLBACK_BRANCHES",
    "MODEL_EXPORT",
    "THREADS_SESSION_EXPORT",
    "AGENT_SESSION_EXPORT",
    "USER_INTAKE_SUBMISSION_EXPORT",
    "FUNCTION_BACKED_EXPORT",
    "SUBMIT_ACTION",
    "START_WALKTHROUGH",
    "OBJECT_SET_EXPORT",
    "RESET_MFA_METHOD",
    "ISSUE_CREATE",
    "RECORD_FLOW_CAPTURE",
    "UPLOAD_DATA_TO_FLOW_CAPTURE",
    "EXPORT_FLOW_CAPTURE_ZIP",
    "INSIGHT_LOAD",
    "AIP_ANALYST_APP_LOAD",
    "PEER_MANAGER_CDS_PAYLOAD_EXPORT",
    "PEER_MANAGER_OBJECT_TYPE_SCHEMAS_EXPORT",
    "AIP_ANALYST_EXPORT",
]
"""
Checkpoint type identifier. See the [Checkpoints documentation](https://palantir.com/docs/foundry/checkpoints/overview)
for more details.
"""


class CheckpointedActionType(core.ModelBase):
    """An ontology action type that was captured as part of a checkpoint."""

    action_type_rid: core.RID = pydantic.Field(alias=str("actionTypeRid"))  # type: ignore[literal-required]
    ontology: CheckpointedOntology
    type: typing.Literal["checkpointedActionType"] = "checkpointedActionType"


class CheckpointedActionTypeRid(core.ModelBase):
    """Action type identifier for a checkpointed action type."""

    rid: core.RID
    type: typing.Literal["checkpointedActionTypeRid"] = "checkpointedActionTypeRid"


class CheckpointedGroup(core.ModelBase):
    """A group that was captured as part of a checkpoint."""

    group_id: str = pydantic.Field(alias=str("groupId"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedGroup"] = "checkpointedGroup"


class CheckpointedGroupId(core.ModelBase):
    """Group identifier for a checkpointed group."""

    id: str
    type: typing.Literal["checkpointedGroupId"] = "checkpointedGroupId"


class CheckpointedIntervention(core.ModelBase):
    """An intervention that was captured as part of a checkpoint."""

    intervention_rid: core.RID = pydantic.Field(alias=str("interventionRid"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedIntervention"] = "checkpointedIntervention"


class CheckpointedInterventionRid(core.ModelBase):
    """Intervention identifier for a checkpointed intervention."""

    rid: core.RID
    type: typing.Literal["checkpointedInterventionRid"] = "checkpointedInterventionRid"


class CheckpointedIssue(core.ModelBase):
    """An issue that was captured as part of a checkpoint."""

    issue_rid: core.RID = pydantic.Field(alias=str("issueRid"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedIssue"] = "checkpointedIssue"


class CheckpointedIssueRid(core.ModelBase):
    """Issue identifier for a checkpointed issue."""

    rid: core.RID
    type: typing.Literal["checkpointedIssueRid"] = "checkpointedIssueRid"


CheckpointedItem = typing_extensions.Annotated[
    typing.Union[
        "CheckpointedIssue",
        "CheckpointedJob",
        "CheckpointedSchedule",
        "CheckpointedResource",
        "CheckpointedJobSpecification",
        "CheckpointedLanguageModel",
        "CheckpointedGroup",
        "CheckpointedUserIntakeSubmission",
        "CheckpointedObjectSet",
        "CheckpointedMarking",
        "CheckpointedMarketplaceProduct",
        "CheckpointedPeeringJob",
        "CheckpointedRole",
        "CheckpointedIntervention",
        "CheckpointedLanguageModelSession",
        "CheckpointedToken",
        "CheckpointedUserIntakeFormInput",
        "CheckpointedPrincipal",
        "CheckpointedActionType",
    ],
    pydantic.Field(discriminator="type"),
]
"""Snapshot of the entity that was captured in a checkpoint."""


CheckpointedItemId = typing_extensions.Annotated[
    typing.Union[
        "CheckpointedJobRid",
        "CheckpointedMarkingId",
        "CheckpointedTokenId",
        "CheckpointedGroupId",
        "CheckpointedObjectSetVersionedRid",
        "CheckpointedObjectSetTypesProxyRids",
        "CheckpointedResourceRid",
        "CheckpointedPeeringJobId",
        "CheckpointedIssueRid",
        "CheckpointedInterventionRid",
        "CheckpointedJobSpecRid",
        "CheckpointedActionTypeRid",
        "CheckpointedScheduleRid",
        "CheckpointedRoleId",
        "CheckpointedUserIntakeFormInputId",
        "CheckpointedMarketplaceProductId",
        "CheckpointedLanguageModelRid",
        "CheckpointedPrincipalId",
        "CheckpointedLanguageModelSessionRid",
        "CheckpointedUserIntakeSubmissionRid",
    ],
    pydantic.Field(discriminator="type"),
]
"""
Identifier for a checkpointed item. This union type explicitly identifies the type of item
being referenced, eliminating ambiguity between RIDs and string IDs.
"""


class CheckpointedJob(core.ModelBase):
    """A build job that was captured as part of a checkpoint."""

    job_rid: core.RID = pydantic.Field(alias=str("jobRid"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedJob"] = "checkpointedJob"


class CheckpointedJobRid(core.ModelBase):
    """Job identifier for a checkpointed job."""

    rid: core.RID
    type: typing.Literal["checkpointedJobRid"] = "checkpointedJobRid"


class CheckpointedJobSpecRid(core.ModelBase):
    """Job specification identifier for a checkpointed job spec."""

    rid: core.RID
    type: typing.Literal["checkpointedJobSpecRid"] = "checkpointedJobSpecRid"


class CheckpointedJobSpecification(core.ModelBase):
    """A job specification that was captured as part of a checkpoint."""

    job_spec_rid: core.RID = pydantic.Field(alias=str("jobSpecRid"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedJobSpecification"] = "checkpointedJobSpecification"


class CheckpointedLanguageModel(core.ModelBase):
    """A language model that was captured as part of a checkpoint."""

    model_rid: core.RID = pydantic.Field(alias=str("modelRid"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedLanguageModel"] = "checkpointedLanguageModel"


class CheckpointedLanguageModelRid(core.ModelBase):
    """Language model identifier for a checkpointed language model."""

    rid: core.RID
    type: typing.Literal["checkpointedLanguageModelRid"] = "checkpointedLanguageModelRid"


class CheckpointedLanguageModelSession(core.ModelBase):
    """A language model session that was captured as part of a checkpoint."""

    session_rid: core.RID = pydantic.Field(alias=str("sessionRid"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedLanguageModelSession"] = "checkpointedLanguageModelSession"


class CheckpointedLanguageModelSessionRid(core.ModelBase):
    """Language model session identifier for a checkpointed session."""

    rid: core.RID
    type: typing.Literal["checkpointedLanguageModelSessionRid"] = (
        "checkpointedLanguageModelSessionRid"
    )


class CheckpointedMarketplaceProduct(core.ModelBase):
    """A Marketplace product that was captured as part of a checkpoint."""

    product_id: str = pydantic.Field(alias=str("productId"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedMarketplaceProduct"] = "checkpointedMarketplaceProduct"


class CheckpointedMarketplaceProductId(core.ModelBase):
    """Marketplace product identifier for a checkpointed product."""

    id: str
    type: typing.Literal["checkpointedMarketplaceProductId"] = "checkpointedMarketplaceProductId"


class CheckpointedMarking(core.ModelBase):
    """A marking that was captured as part of a checkpoint."""

    marking_id: str = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedMarking"] = "checkpointedMarking"


class CheckpointedMarkingId(core.ModelBase):
    """Marking identifier for a checkpointed marking."""

    id: str
    type: typing.Literal["checkpointedMarkingId"] = "checkpointedMarkingId"


class CheckpointedObjectSet(core.ModelBase):
    """Represents the object set that was checkpointed."""

    versioned: typing.Optional[CheckpointedVersionedObjectSet] = None
    types_proxy: typing.Optional[CheckpointedObjectSetTypesProxy] = pydantic.Field(alias=str("typesProxy"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["checkpointedObjectSet"] = "checkpointedObjectSet"


class CheckpointedObjectSetTypesProxy(core.ModelBase):
    """A types proxy object set that was captured as part of a checkpoint."""

    object_types: typing.List[CheckpointedOntologyWithObjectTypes] = pydantic.Field(alias=str("objectTypes"))  # type: ignore[literal-required]


class CheckpointedObjectSetTypesProxyRids(core.ModelBase):
    """Object type RIDs for a types proxy object set."""

    rids: typing.List[core.RID]
    type: typing.Literal["checkpointedObjectSetTypesProxyRids"] = (
        "checkpointedObjectSetTypesProxyRids"
    )


class CheckpointedObjectSetVersionedRid(core.ModelBase):
    """Versioned object set RID for a checkpointed object set."""

    rid: core.RID
    type: typing.Literal["checkpointedObjectSetVersionedRid"] = "checkpointedObjectSetVersionedRid"


class CheckpointedOntology(core.ModelBase):
    """An ontology snapshot that was captured as part of a checkpoint."""

    ontology_rid: core.RID = pydantic.Field(alias=str("ontologyRid"))  # type: ignore[literal-required]
    ontology_version: core.UUID = pydantic.Field(alias=str("ontologyVersion"))  # type: ignore[literal-required]
    namespace_rid: typing.Optional[NamespaceRid] = pydantic.Field(alias=str("namespaceRid"), default=None)  # type: ignore[literal-required]


class CheckpointedOntologyWithObjectTypes(core.ModelBase):
    """An ontology with its associated object types that was captured as part of a checkpoint."""

    ontology: CheckpointedOntology
    object_type_rids: typing.List[core.RID] = pydantic.Field(alias=str("objectTypeRids"))  # type: ignore[literal-required]


class CheckpointedPeeringJob(core.ModelBase):
    """A peering job that was captured as part of a checkpoint."""

    job_id: str = pydantic.Field(alias=str("jobId"))  # type: ignore[literal-required]
    """Identifier of the peering job."""

    type: typing.Literal["checkpointedPeeringJob"] = "checkpointedPeeringJob"


class CheckpointedPeeringJobId(core.ModelBase):
    """Peering job identifier for a checkpointed peering job."""

    id: str
    type: typing.Literal["checkpointedPeeringJobId"] = "checkpointedPeeringJobId"


class CheckpointedPrincipal(core.ModelBase):
    """A user or group principal that was captured as part of a checkpoint."""

    id: str
    username: RedactableString
    organization_rid: typing.Optional[OrganizationRid] = pydantic.Field(alias=str("organizationRid"), default=None)  # type: ignore[literal-required]
    role: CheckpointedPrincipalRole
    type: typing.Literal["checkpointedPrincipal"] = "checkpointedPrincipal"


class CheckpointedPrincipalId(core.ModelBase):
    """Principal identifier for a checkpointed principal."""

    id: str
    type: typing.Literal["checkpointedPrincipalId"] = "checkpointedPrincipalId"


CheckpointedPrincipalRole = typing.Literal[
    "SOURCE_SHARE_RECIPIENT",
    "TARGET_GROUP",
    "GROUP_MEMBER",
    "MARKING_MEMBER",
    "ROLE_GRANT_RECIPIENT",
    "MFA_METHOD_RESET_TARGET",
    "ISSUE_ASSIGNEE",
]
"""Role the principal had relative to the checkpointed entity."""


class CheckpointedResource(core.ModelBase):
    """A Foundry resource that was captured as part of a checkpoint."""

    rid: core.RID
    resource_type: CheckpointedResourceType = pydantic.Field(alias=str("resourceType"))  # type: ignore[literal-required]
    name: typing.Optional[RedactableString] = None
    project_rid: typing.Optional[ProjectRid] = pydantic.Field(alias=str("projectRid"), default=None)  # type: ignore[literal-required]
    namespace_rid: typing.Optional[NamespaceRid] = pydantic.Field(alias=str("namespaceRid"), default=None)  # type: ignore[literal-required]
    compass_path: RedactableString = pydantic.Field(alias=str("compassPath"))  # type: ignore[literal-required]
    org_markings: typing.List[str] = pydantic.Field(alias=str("orgMarkings"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedResource"] = "checkpointedResource"


class CheckpointedResourceRid(core.ModelBase):
    """Resource identifier for a checkpointed resource."""

    rid: core.RID
    type: typing.Literal["checkpointedResourceRid"] = "checkpointedResourceRid"


CheckpointedResourceType = typing.Literal[
    "CONTOUR_ANALYSIS",
    "CONTOUR_SOURCE_DATASET",
    "DATA_CONNECTION_SYNC",
    "DATA_CONNECTION_SOURCE",
    "DATA_CONNECTION_SYNC_TARGET_DATASET",
    "HUBBLE_OBJECT_TYPE",
    "EXPORTED_RESOURCE",
    "IMPORTED_RESOURCE",
    "REPORT",
    "CIPHER_CHANNEL",
    "CIPHER_LICENSE",
    "PARENT_RESOURCE",
    "ATTACHMENT",
    "SLATE_APPLICATION",
    "NOTEPAD",
    "DATASET",
    "MEDIA_SET",
    "CODE_REPOSITORY",
    "CODE_WORKBOOK",
    "CODE_WORKSPACE",
    "TELEMETRY_CONTAINER",
    "REFERENCED_RESOURCE",
    "ROLE_GRANT_RESOURCE",
    "PROJECT",
    "STORE",
    "THIRD_PARTY_APPLICATION",
    "BUILDER_PIPELINE",
    "MODEL",
    "MODEL_VERSION",
    "AGENT",
    "WORKSHOP_MODULE",
    "WALKTHROUGH",
    "FLOW_CAPTURE",
    "PEERING_CONNECTION",
]
"""Type of resource that was captured."""


class CheckpointedRole(core.ModelBase):
    """A role that was captured as part of a checkpoint."""

    role_id: str = pydantic.Field(alias=str("roleId"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedRole"] = "checkpointedRole"


class CheckpointedRoleId(core.ModelBase):
    """Role identifier for a checkpointed role."""

    id: str
    type: typing.Literal["checkpointedRoleId"] = "checkpointedRoleId"


class CheckpointedSchedule(core.ModelBase):
    """A schedule that was captured as part of a checkpoint."""

    schedule_rid: core.RID = pydantic.Field(alias=str("scheduleRid"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedSchedule"] = "checkpointedSchedule"


class CheckpointedScheduleRid(core.ModelBase):
    """Schedule identifier for a checkpointed schedule."""

    rid: core.RID
    type: typing.Literal["checkpointedScheduleRid"] = "checkpointedScheduleRid"


class CheckpointedToken(core.ModelBase):
    """An authentication token that was captured as part of a checkpoint."""

    token_id: str = pydantic.Field(alias=str("tokenId"))  # type: ignore[literal-required]
    token_type: CheckpointedTokenType = pydantic.Field(alias=str("tokenType"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedToken"] = "checkpointedToken"


class CheckpointedTokenId(core.ModelBase):
    """Token identifier for a checkpointed token."""

    id: str
    type: typing.Literal["checkpointedTokenId"] = "checkpointedTokenId"


CheckpointedTokenType = typing.Literal["USER_TOKEN"]
"""The type of token that was captured as part of a checkpoint."""


class CheckpointedUserIntakeFormInput(core.ModelBase):
    """A user intake form input that was captured as part of a checkpoint."""

    input_id: str = pydantic.Field(alias=str("inputId"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedUserIntakeFormInput"] = "checkpointedUserIntakeFormInput"


class CheckpointedUserIntakeFormInputId(core.ModelBase):
    """User intake form input identifier for a checkpointed form input."""

    id: str
    type: typing.Literal["checkpointedUserIntakeFormInputId"] = "checkpointedUserIntakeFormInputId"


class CheckpointedUserIntakeSubmission(core.ModelBase):
    """A user intake form submission that was captured as part of a checkpoint."""

    submission_rid: core.RID = pydantic.Field(alias=str("submissionRid"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedUserIntakeSubmission"] = "checkpointedUserIntakeSubmission"


class CheckpointedUserIntakeSubmissionRid(core.ModelBase):
    """User intake submission identifier for a checkpointed submission."""

    rid: core.RID
    type: typing.Literal["checkpointedUserIntakeSubmissionRid"] = (
        "checkpointedUserIntakeSubmissionRid"
    )


class CheckpointedVersionedObjectSet(core.ModelBase):
    """A versioned object set that was captured as part of a checkpoint."""

    versioned_object_set_rid: core.RID = pydantic.Field(alias=str("versionedObjectSetRid"))  # type: ignore[literal-required]
    object_set_version: core.UUID = pydantic.Field(alias=str("objectSetVersion"))  # type: ignore[literal-required]
    object_types: typing.List[CheckpointedOntologyWithObjectTypes] = pydantic.Field(alias=str("objectTypes"))  # type: ignore[literal-required]


ConfigRid = core.RID
"""Identifier of the checkpoint configuration that produced a record."""


class DropdownJustification(core.ModelBase):
    """Checkpoint justification where the user selects one or more options from a dropdown."""

    selected_options: typing.List[DropdownSelection] = pydantic.Field(alias=str("selectedOptions"))  # type: ignore[literal-required]
    """Options the user selected in the dropdown."""

    prompt: str
    """Prompt to which the user-selected options respond."""

    description: typing.Optional[str] = None
    """Supplemental information that helps users understand the prompt."""

    title: str
    """Title of the checkpoint to which the user is responding."""

    type: typing.Literal["dropdownJustification"] = "dropdownJustification"


class DropdownSelection(core.ModelBase):
    """A selection made within a multi-select dropdown justification."""

    selected_option: str = pydantic.Field(alias=str("selectedOption"))  # type: ignore[literal-required]
    """Dropdown option the user selected."""

    additional_response: typing.Optional[str] = pydantic.Field(alias=str("additionalResponse"), default=None)  # type: ignore[literal-required]
    """Extra free-text response submitted alongside the dropdown selection."""


class GetRecordsBatchRequestElement(core.ModelBase):
    """GetRecordsBatchRequestElement"""

    record_rid: RecordRid = pydantic.Field(alias=str("recordRid"))  # type: ignore[literal-required]


class GetRecordsBatchResponse(core.ModelBase):
    """GetRecordsBatchResponse"""

    data: typing.Dict[RecordRid, Record]


InteractionRid = core.RID
"""Identifier of the interaction associated with a record."""


Justification = typing_extensions.Annotated[
    typing.Union[
        "ResponseJustification",
        "DropdownJustification",
        "ReauthenticationJustification",
        "AcknowledgementJustification",
    ],
    pydantic.Field(discriminator="type"),
]
"""Justification submitted by the user to pass a checkpoint."""


JustificationMatchType = typing.Literal["EXACT", "CONTAINS"]
"""Determines how free-text justification input should be matched."""


NamespaceRid = core.RID
"""Identifier of the namespace associated with a checkpoint."""


OrganizationRid = core.RID
"""Identifier of the organization associated with a checkpoint."""


ProjectRid = core.RID
"""Identifier of the project that scoped a checkpoint."""


class ReauthenticationJustification(core.ModelBase):
    """Checkpoint justification that requires the user to reauthenticate with the platform."""

    reauthentication_id: core.UUID = pydantic.Field(alias=str("reauthenticationId"))  # type: ignore[literal-required]
    """Identifier for the reauthentication instance."""

    prompt: str
    """Prompt shown to the user during reauthentication."""

    description: typing.Optional[str] = None
    """Supplemental information that helps users understand the prompt."""

    title: str
    """Title of the checkpoint that the user is acknowledging."""

    type: typing.Literal["reauthenticationJustification"] = "reauthenticationJustification"


class Record(core.ModelBase):
    """Record"""

    rid: RecordRid
    config_rid: typing.Optional[ConfigRid] = pydantic.Field(alias=str("configRid"), default=None)  # type: ignore[literal-required]
    type: CheckpointType
    scope: Scope
    acting_user: ActingUser = pydantic.Field(alias=str("actingUser"))  # type: ignore[literal-required]
    delegate_user_id: typing.Optional[core_models.UserId] = pydantic.Field(alias=str("delegateUserId"), default=None)  # type: ignore[literal-required]
    created_at: RecordCreatedAt = pydantic.Field(alias=str("createdAt"))  # type: ignore[literal-required]
    checkpointed_items: typing.List[CheckpointedItem] = pydantic.Field(alias=str("checkpointedItems"))  # type: ignore[literal-required]
    justification: Justification
    project_rid: typing.Optional[ProjectRid] = pydantic.Field(alias=str("projectRid"), default=None)  # type: ignore[literal-required]
    organization_rid: typing.Optional[OrganizationRid] = pydantic.Field(alias=str("organizationRid"), default=None)  # type: ignore[literal-required]
    namespace_rid: typing.Optional[NamespaceRid] = pydantic.Field(alias=str("namespaceRid"), default=None)  # type: ignore[literal-required]
    interaction_rid: typing.Optional[InteractionRid] = pydantic.Field(alias=str("interactionRid"), default=None)  # type: ignore[literal-required]
    approvals_metadata: typing.Optional[ApprovalsMetadata] = pydantic.Field(alias=str("approvalsMetadata"), default=None)  # type: ignore[literal-required]


RecordCreatedAt = core.AwareDatetime
"""The time at which the checkpoint record was created."""


RecordRid = core.RID
"""Identifier of a checkpoint record."""


class RedactableString(core.ModelBase):
    """A string value that may be redacted for privacy reasons."""

    value: typing.Optional[str] = None
    redaction_type: typing.Optional[RedactionType] = pydantic.Field(alias=str("redactionType"), default=None)  # type: ignore[literal-required]


RedactionType = typing.Literal["USER_REDACTED", "RESOURCE_REDACTED"]
"""Indicates why a string value was redacted."""


class ResponseJustification(core.ModelBase):
    """Checkpoint justification that requires the user to input a free-text response."""

    response: str
    """User-submitted free-text justification."""

    prompt: str
    """Prompt to which the user responds."""

    description: typing.Optional[str] = None
    """Supplemental information that helps users understand the prompt."""

    title: str
    """Title of the checkpoint to which the user is responding."""

    type: typing.Literal["responseJustification"] = "responseJustification"


Scope = typing.Literal["USER_SCOPED", "RESOURCE_SCOPED"]
"""Indicates whether the checkpoint was scoped to a user or resource."""


class SearchCheckpointRecordsAndFilter(core.ModelBase):
    """Logical conjunction of checkpoint record filters."""

    filters: typing.List[SearchCheckpointRecordsFilter]
    type: typing.Literal["and"] = "and"


class SearchCheckpointRecordsCheckpointedItemIdFilter(core.ModelBase):
    """Filter for checkpointed item identifier matches."""

    checkpointed_item_id: CheckpointedItemId = pydantic.Field(alias=str("checkpointedItemId"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedItemId"] = "checkpointedItemId"


class SearchCheckpointRecordsEqualsFilter(core.ModelBase):
    """Filter for exact field value matches."""

    field: SearchCheckpointRecordsEqualsFilterField
    value: str
    type: typing.Literal["eq"] = "eq"


SearchCheckpointRecordsEqualsFilterField = typing.Literal[
    "recordRid",
    "configRid",
    "checkpointType",
    "actingUserId",
    "delegateUserId",
    "organizationRid",
    "namespaceRid",
    "interactionRid",
    "checkpointedItemType",
]
"""Fields that support equality filtering."""


SearchCheckpointRecordsFilter = typing_extensions.Annotated[
    typing.Union[
        "SearchCheckpointRecordsNotFilter",
        "SearchCheckpointRecordsOrFilter",
        "SearchCheckpointRecordsTextSearchFilter",
        "SearchCheckpointRecordsAndFilter",
        "SearchCheckpointRecordsLtFilter",
        "SearchCheckpointRecordsGteFilter",
        "SearchCheckpointRecordsEqualsFilter",
        "SearchCheckpointRecordsCheckpointedItemIdFilter",
    ],
    pydantic.Field(discriminator="type"),
]
"""Search criteria for checkpoint records."""


class SearchCheckpointRecordsGteFilter(core.ModelBase):
    """Filter for greater-than-or-equal comparisons."""

    field: SearchCheckpointRecordsGteFilterField
    value: core.AwareDatetime
    type: typing.Literal["gte"] = "gte"


SearchCheckpointRecordsGteFilterField = typing.Literal["createdAt"]
"""Fields that support greater-than-or-equal filtering."""


class SearchCheckpointRecordsLtFilter(core.ModelBase):
    """Filter for less-than comparisons."""

    field: SearchCheckpointRecordsLtFilterField
    value: core.AwareDatetime
    type: typing.Literal["lt"] = "lt"


SearchCheckpointRecordsLtFilterField = typing.Literal["createdAt"]
"""Fields that support less-than filtering."""


class SearchCheckpointRecordsNotFilter(core.ModelBase):
    """Logical negation of a checkpoint record filter."""

    filter: SearchCheckpointRecordsFilter
    type: typing.Literal["not"] = "not"


class SearchCheckpointRecordsOrFilter(core.ModelBase):
    """Logical disjunction of checkpoint record filters."""

    filters: typing.List[SearchCheckpointRecordsFilter]
    type: typing.Literal["or"] = "or"


class SearchCheckpointRecordsRequest(core.ModelBase):
    """Request payload for searching checkpoint records."""

    filter: SearchCheckpointRecordsFilter


class SearchCheckpointRecordsResponse(core.ModelBase):
    """Response payload for searching checkpoint records."""

    data: typing.List[Record]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class SearchCheckpointRecordsTextSearchFilter(core.ModelBase):
    """Filter for text search on justification fields."""

    field: SearchCheckpointRecordsTextSearchFilterField
    query: str
    match_type: JustificationMatchType = pydantic.Field(alias=str("matchType"))  # type: ignore[literal-required]
    type: typing.Literal["textSearch"] = "textSearch"


SearchCheckpointRecordsTextSearchFilterField = typing.Literal[
    "justificationResponse", "justificationSelectedOption", "justificationAdditionalResponse"
]
"""Fields that support text search filtering."""


class SearchRecordsRequest(core.ModelBase):
    """SearchRecordsRequest"""

    where: SearchCheckpointRecordsRequest
    page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("pageToken"), default=None)  # type: ignore[literal-required]
    page_size: typing.Optional[core_models.PageSize] = pydantic.Field(alias=str("pageSize"), default=None)  # type: ignore[literal-required]
    """The page size for the search request. If no value is provided, a default of `100` will be used."""

    sort_direction: typing.Optional[SortDirection] = pydantic.Field(alias=str("sortDirection"), default=None)  # type: ignore[literal-required]
    """Chronological order of creation time for records to be returned in. Defaults to reverse chronological order (DESC)."""


SortDirection = typing.Literal["ASC", "DESC"]
"""SortDirection"""


core.resolve_forward_references(CheckpointedItem, globalns=globals(), localns=locals())
core.resolve_forward_references(CheckpointedItemId, globalns=globals(), localns=locals())
core.resolve_forward_references(Justification, globalns=globals(), localns=locals())
core.resolve_forward_references(SearchCheckpointRecordsFilter, globalns=globals(), localns=locals())

__all__ = [
    "AcknowledgementJustification",
    "ActingUser",
    "ApprovalsMetadata",
    "ApprovalsSubtaskId",
    "ApprovalsTaskId",
    "CheckpointType",
    "CheckpointedActionType",
    "CheckpointedActionTypeRid",
    "CheckpointedGroup",
    "CheckpointedGroupId",
    "CheckpointedIntervention",
    "CheckpointedInterventionRid",
    "CheckpointedIssue",
    "CheckpointedIssueRid",
    "CheckpointedItem",
    "CheckpointedItemId",
    "CheckpointedJob",
    "CheckpointedJobRid",
    "CheckpointedJobSpecRid",
    "CheckpointedJobSpecification",
    "CheckpointedLanguageModel",
    "CheckpointedLanguageModelRid",
    "CheckpointedLanguageModelSession",
    "CheckpointedLanguageModelSessionRid",
    "CheckpointedMarketplaceProduct",
    "CheckpointedMarketplaceProductId",
    "CheckpointedMarking",
    "CheckpointedMarkingId",
    "CheckpointedObjectSet",
    "CheckpointedObjectSetTypesProxy",
    "CheckpointedObjectSetTypesProxyRids",
    "CheckpointedObjectSetVersionedRid",
    "CheckpointedOntology",
    "CheckpointedOntologyWithObjectTypes",
    "CheckpointedPeeringJob",
    "CheckpointedPeeringJobId",
    "CheckpointedPrincipal",
    "CheckpointedPrincipalId",
    "CheckpointedPrincipalRole",
    "CheckpointedResource",
    "CheckpointedResourceRid",
    "CheckpointedResourceType",
    "CheckpointedRole",
    "CheckpointedRoleId",
    "CheckpointedSchedule",
    "CheckpointedScheduleRid",
    "CheckpointedToken",
    "CheckpointedTokenId",
    "CheckpointedTokenType",
    "CheckpointedUserIntakeFormInput",
    "CheckpointedUserIntakeFormInputId",
    "CheckpointedUserIntakeSubmission",
    "CheckpointedUserIntakeSubmissionRid",
    "CheckpointedVersionedObjectSet",
    "ConfigRid",
    "DropdownJustification",
    "DropdownSelection",
    "GetRecordsBatchRequestElement",
    "GetRecordsBatchResponse",
    "InteractionRid",
    "Justification",
    "JustificationMatchType",
    "NamespaceRid",
    "OrganizationRid",
    "ProjectRid",
    "ReauthenticationJustification",
    "Record",
    "RecordCreatedAt",
    "RecordRid",
    "RedactableString",
    "RedactionType",
    "ResponseJustification",
    "Scope",
    "SearchCheckpointRecordsAndFilter",
    "SearchCheckpointRecordsCheckpointedItemIdFilter",
    "SearchCheckpointRecordsEqualsFilter",
    "SearchCheckpointRecordsEqualsFilterField",
    "SearchCheckpointRecordsFilter",
    "SearchCheckpointRecordsGteFilter",
    "SearchCheckpointRecordsGteFilterField",
    "SearchCheckpointRecordsLtFilter",
    "SearchCheckpointRecordsLtFilterField",
    "SearchCheckpointRecordsNotFilter",
    "SearchCheckpointRecordsOrFilter",
    "SearchCheckpointRecordsRequest",
    "SearchCheckpointRecordsResponse",
    "SearchCheckpointRecordsTextSearchFilter",
    "SearchCheckpointRecordsTextSearchFilterField",
    "SearchRecordsRequest",
    "SortDirection",
]
