# ObjectSetAsTypeTypeDict

Casts an object set to a specified object type or interface type API name. Any object whose object type does 
not match the object type provided or implement the interface type provided will be dropped from the resulting 
object set. This is currently unsupported and an exception will be thrown if used.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**entityType** | pydantic.StrictStr | Yes | An object type or interface type API name.  |
**objectSet** | ObjectSetDict | Yes |  |
**type** | Literal["asType"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
