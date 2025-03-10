# DeprecatedPropertyTypeStatusDict

This status indicates that the PropertyType is reaching the end of its life and will be removed as per the
deadline specified.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**message** | str | Yes |  |
**deadline** | datetime | Yes |  |
**replacedBy** | typing_extensions.NotRequired[PropertyTypeRid] | No |  |
**type** | typing.Literal["deprecated"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
