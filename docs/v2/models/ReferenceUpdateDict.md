# ReferenceUpdateDict

The updated data value associated with an object instance's external reference. The object instance
is uniquely identified by an object type and a primary key. Note that the value of the property
field returns a dereferenced value rather than the reference itself.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | ObjectTypeApiName | Yes |  |
**primaryKey** | ObjectPrimaryKey | Yes |  |
**propertyApiName** | PropertyApiName | Yes |  |
**value** | ReferenceValueDict | Yes |  |
**type** | Literal["reference"] | Yes | None |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)
