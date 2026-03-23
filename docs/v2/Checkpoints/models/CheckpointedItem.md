# CheckpointedItem

Snapshot of the entity that was captured in a checkpoint.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
CheckpointedIssue | checkpointedIssue
CheckpointedJob | checkpointedJob
CheckpointedSchedule | checkpointedSchedule
CheckpointedResource | checkpointedResource
CheckpointedJobSpecification | checkpointedJobSpecification
CheckpointedLanguageModel | checkpointedLanguageModel
CheckpointedGroup | checkpointedGroup
CheckpointedUserIntakeSubmission | checkpointedUserIntakeSubmission
CheckpointedObjectSet | checkpointedObjectSet
CheckpointedMarking | checkpointedMarking
CheckpointedMarketplaceProduct | checkpointedMarketplaceProduct
CheckpointedPeeringJob | checkpointedPeeringJob
CheckpointedRole | checkpointedRole
CheckpointedIntervention | checkpointedIntervention
CheckpointedLanguageModelSession | checkpointedLanguageModelSession
CheckpointedToken | checkpointedToken
CheckpointedUserIntakeFormInput | checkpointedUserIntakeFormInput
CheckpointedPrincipal | checkpointedPrincipal
CheckpointedActionType | checkpointedActionType


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
