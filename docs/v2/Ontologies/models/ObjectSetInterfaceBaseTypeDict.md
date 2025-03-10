# ObjectSetInterfaceBaseTypeDict

ObjectSetInterfaceBaseType

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**interfaceType** | str | Yes | An object set with objects that implement the interface with the given interface API name. The objects in  the object set will only have properties that implement properties of the given interface, unless you set the includeAllBaseObjectProperties flag.  |
**includeAllBaseObjectProperties** | typing_extensions.NotRequired[bool] | No | A flag that will return all of the underlying object properties for the objects that implement the interface.  This includes properties that don't explicitly implement an SPT on the interface.  |
**type** | typing.Literal["interfaceBase"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
