# CreateConnectionRequestEncryptedProperty

When reading an encrypted property, the secret name representing the encrypted value will be returned.
When writing to an encrypted property:
- If a plaintext value is passed as an input, the plaintext value will be encrypted and saved to the property.
- If a secret name is passed as an input, the secret name must match the existing secret name of the property
  and the property will retain its previously encrypted value.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
CreateConnectionRequestAsSecretName | asSecretName
CreateConnectionRequestAsPlaintextValue | asPlaintextValue


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
