# TargetVersion

Select the latest released version, an exact semantic version, or a version UUID within the installation's product and marketplace.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
TargetVersionLatest | latest
ProductVersionBySemanticVersion | semanticVersion
ProductVersionById | versionId


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
