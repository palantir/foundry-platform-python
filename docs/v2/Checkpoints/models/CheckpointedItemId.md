# CheckpointedItemId

Identifier for a checkpointed item. This union type explicitly identifies the type of item
being referenced, eliminating ambiguity between RIDs and string IDs.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
CheckpointedJobRid | checkpointedJobRid
CheckpointedMarkingId | checkpointedMarkingId
CheckpointedTokenId | checkpointedTokenId
CheckpointedGroupId | checkpointedGroupId
CheckpointedObjectSetVersionedRid | checkpointedObjectSetVersionedRid
CheckpointedObjectSetTypesProxyRids | checkpointedObjectSetTypesProxyRids
CheckpointedResourceRid | checkpointedResourceRid
CheckpointedPeeringJobId | checkpointedPeeringJobId
CheckpointedIssueRid | checkpointedIssueRid
CheckpointedInterventionRid | checkpointedInterventionRid
CheckpointedJobSpecRid | checkpointedJobSpecRid
CheckpointedActionTypeRid | checkpointedActionTypeRid
CheckpointedScheduleRid | checkpointedScheduleRid
CheckpointedRoleId | checkpointedRoleId
CheckpointedUserIntakeFormInputId | checkpointedUserIntakeFormInputId
CheckpointedMarketplaceProductId | checkpointedMarketplaceProductId
CheckpointedLanguageModelRid | checkpointedLanguageModelRid
CheckpointedPrincipalId | checkpointedPrincipalId
CheckpointedLanguageModelSessionRid | checkpointedLanguageModelSessionRid
CheckpointedUserIntakeSubmissionRid | checkpointedUserIntakeSubmissionRid


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
