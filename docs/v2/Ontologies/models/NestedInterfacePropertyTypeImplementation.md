# NestedInterfacePropertyTypeImplementation

Describes how an object type implements an interface property when a reducer is applied to it. Is missing a
reduced property implementation to prevent arbitrarily nested implementations.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
InterfacePropertyStructFieldImplementation | structFieldImplementation
InterfacePropertyStructImplementation | structImplementation
InterfacePropertyLocalPropertyImplementation | localPropertyImplementation


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
