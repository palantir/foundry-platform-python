# IntervalQuery

Returns objects where the specified field matches the sub-rule provided. This applies to the analyzed form of 
text fields. Either `field` or `propertyIdentifier` can be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | Optional[PropertyApiName] | No |  |
**property_identifier** | Optional[PropertyIdentifier] | No |  |
**rule** | IntervalQueryRule | Yes |  |
**type** | Literal["interval"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
