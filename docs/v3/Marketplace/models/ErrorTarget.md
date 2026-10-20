# ErrorTarget

The proposed job, installation, or input and output references affected by the error.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ErrorTargetInputsAndOutputs | inputsAndOutputs
ErrorTargetInstallation | installation
ErrorTargetJob | job


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
