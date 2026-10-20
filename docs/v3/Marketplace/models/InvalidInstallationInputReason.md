# InvalidInstallationInputReason

Why a supplied input value cannot be used.

Values:
- **INVALID_PARENT_INPUT**: A supplied parent input did not resolve to the type required by the child input.
- **INVALID_VERSION**: The supplied version could not be parsed in the format required by this input.
- **MISSING_VERSION**: This input requires a resource version. Supply it using the `ridWithVersion` value variant.
- **RESOURCE_UNAVAILABLE**: The referenced resource or a required version could not be found or resolved.
- **UNSUPPORTED_TYPE**: The supplied value variant is not supported for this input. Use one of the input's `supportedTypes`.

| **Value** |
| --------- |
| `"MISSING_VERSION"` |
| `"INVALID_VERSION"` |
| `"UNSUPPORTED_TYPE"` |
| `"RESOURCE_UNAVAILABLE"` |
| `"INVALID_PARENT_INPUT"` |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
