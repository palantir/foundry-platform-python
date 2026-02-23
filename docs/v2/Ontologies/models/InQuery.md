# InQuery

Returns objects where the specified field equals any of the provided values. Allows you to
specify a property to query on by a variety of means. If an empty array is provided as the value, then the filter will match all objects
in the object set. Either `field` or `propertyIdentifier` must be supplied, but not both.

For string properties, full term matching only works when **Selectable** is enabled for the property in Ontology Manager.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | Optional[PropertyApiName] | No |  |
**property_identifier** | Optional[PropertyIdentifier] | No |  |
**value** | List[PropertyValue] | Yes |  |
**type** | Literal["in"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
