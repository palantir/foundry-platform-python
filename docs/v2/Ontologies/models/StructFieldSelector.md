# StructFieldSelector

A combination of a property API name and a struct field API name used to select struct fields. Note that you can
still select struct properties with only a 'PropertyApiNameSelector'; the queries will then become 'OR' queries
across the fields of the struct property, and derived property expressions will operate on the whole struct
where applicable.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**property_api_name** | str | Yes |  |
**struct_field_api_name** | str | Yes |  |
**type** | Literal["structField"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
