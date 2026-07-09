# CipherChannelStrategy

Controls which Cipher Channel is used when encrypting a value. If not specified, defaults to `PREFER_EXISTING`.

- `PREFER_EXISTING`: use the Cipher Channel parsed from the existing ciphertext value; fall back to the default channel configured in ontology metadata.
- `PREFER_DEFAULT`: use the default channel configured in ontology metadata; fall back to the channel parsed from the existing ciphertext value.
- `EXISTING_ONLY`: use the channel parsed from the existing ciphertext value only; error if the value is not already encrypted.
- `DEFAULT_ONLY`: use the default channel configured in ontology metadata only; error if none is configured.


| **Value** |
| --------- |
| `"PREFER_EXISTING"` |
| `"PREFER_DEFAULT"` |
| `"EXISTING_ONLY"` |
| `"DEFAULT_ONLY"` |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
