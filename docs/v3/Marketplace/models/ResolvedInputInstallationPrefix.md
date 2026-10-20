# ResolvedInputInstallationPrefix

ResolvedInputInstallationPrefix

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**prefix** | str | Yes | A prefix for installed resources. Use an empty string for no prefix. Otherwise, use lowercase kebab-case containing only `a-z`, `0-9`, and hyphens, at most 16 characters, without a leading number. |
**prefix_configuration** | Optional[InstallationPrefixConfiguration] | No | Controls prefixing of Ontology entity names. Defaults to `DISPLAY_NAME_AND_API_NAME` when omitted. |
**type** | Literal["installationPrefix"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
