# ParseClassificationsResponse

ParseClassificationsResponse

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**parsed** | Dict[str, List[MarkingId]] | Yes | Map of valid classification strings to their component marking IDs. Strings that could not be parsed are absent from this map and appear in 'errors' instead. |
**errors** | Dict[str, str] | Yes | Map of classification strings that could not be parsed to a human-readable error message. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
