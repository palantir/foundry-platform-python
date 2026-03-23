# ModelVersionSource

The source from which this model version was created.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ModelVersionContainerizedSource | importedContainerizedModel
ModelVersionExternalSource | external
ModelVersionCodeWorkspaceSource | codeWorkspace
ModelVersionModelStudioSource | modelStudio
ModelVersionCodeRepositorySource | codeRepository
ModelVersionSdkSource | sdk
ModelVersionPromotedSource | promoted


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
