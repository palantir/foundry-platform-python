# PropertyTypeStatusDict

The status to indicate whether the PropertyType is either Experimental, Active, Deprecated, or Example.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
DeprecatedPropertyTypeStatusDict | deprecated
ActivePropertyTypeStatusDict | active
ExperimentalPropertyTypeStatusDict | experimental
ExamplePropertyTypeStatusDict | example


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
