# UniqueIdentifierArgument

Represents a unique identifier argument in a logic rule.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**link_id** | Optional[UUID] | No | By default all UniqueIdentifier Logic Rule arguments will generate different UUID.  If the linkId is present all Logic Rules with the same linkId will all have the same uuid generated as the value.  |
**type** | Literal["uniqueIdentifier"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
