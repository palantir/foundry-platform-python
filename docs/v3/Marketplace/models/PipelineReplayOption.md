# PipelineReplayOption

How a pipeline handles a state break during upgrade.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
PipelineReplayOptionAcknowledgeStateBreaks | acknowledgeStateBreaks
PipelineReplayOptionReset | reset
PipelineReplayOptionResetAndReplayFromOffset | resetAndReplayFromOffset


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
