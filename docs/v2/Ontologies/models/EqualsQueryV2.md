# EqualsQueryV2

Returns objects where the specified field is equal to a value. Allows you to specify a property to query on
by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.

For string properties, full term matching only works when **Selectable** is enabled for the property in Ontology Manager.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | Optional[PropertyApiName] | No |  |
**property_identifier** | Optional[PropertyIdentifier] | No |  |
**value** | PropertyValue | Yes |  |
**type** | Literal["eq"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
