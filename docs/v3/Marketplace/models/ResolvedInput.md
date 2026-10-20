# ResolvedInput

A structured input value. Use the variant advertised by the input's `supportedTypes`. Prefer a direct scalar or resource reference when the input supports one.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ResolvedInputConnectionConfigurationOverrides | connectionConfigurationOverrides
ResolvedInputFunctionApiStability | functionApiStability
ResolvedInputGroup | group
ResolvedInputInstallationPrefix | installationPrefix
ResolvedInputLibrary | library
ResolvedInputOntologyDataSource | ontologyDataSource
ResolvedInputOntologyDataSourceRetention | ontologyDataSourceRetention
ResolvedInputOntologySchemaMigrationPolicy | ontologySchemaMigrationPolicy
ResolvedInputOntologySchemaMigrationValues | ontologySchemaMigrationValues
ResolvedInputPeerProducerProfile | peerProducerProfile
ResolvedInputPeerProfileRemoteStrategy | peerProfileRemoteStrategy
ResolvedInputPipelineBuilderGeotimeConfiguration | pipelineBuilderGeotimeConfiguration
ResolvedInputPipelineBuilderParameter | pipelineBuilderParameter
ResolvedInputPipelineBuilderReplayOption | pipelineBuilderReplayOption
ResolvedInputStreamingSyncConfigurationOverrides | streamingSyncConfigurationOverrides
ResolvedInputWorkshopSavedStateConfiguration | workshopSavedStateConfiguration


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
