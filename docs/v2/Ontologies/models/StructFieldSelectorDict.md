# StructFieldSelectorDict

A combination of a struct property api name and a struct field api name. This is used to select struct fields 
to query on. Note that you can still select struct properties with only a 'PropertyApiNameSelector'; the queries 
will then become 'OR' queries across the fields of the struct property.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**propertyApiName** | PropertyApiName | Yes |  |
**structFieldApiName** | StructFieldApiName | Yes |  |
**type** | Literal["structField"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
