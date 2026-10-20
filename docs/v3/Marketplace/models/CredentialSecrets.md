# CredentialSecrets

Supply the plaintext variant when configuring an installation job.
Inspection returns the redacted variant, which contains only secret names
and cannot be submitted as credentials for another installation job.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
PlaintextCredentialSecrets | plaintext
RedactedCredentialSecrets | redacted


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
