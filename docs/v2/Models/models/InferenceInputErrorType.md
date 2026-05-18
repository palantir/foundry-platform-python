# InferenceInputErrorType

The specific type and details of an input validation error for inference requests.
Each variant carries parameters relevant to that specific error category.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
InvalidArrayShapeError | invalidArrayShape
TypeMismatchError | typeMismatch
UnsupportedTypeError | unsupportedType
UnknownInputNameError | unknownInputName
InvalidTabularFormatError | invalidTabularFormat
InconsistentArrayDimensionsError | inconsistentArrayDimensions
RequiredValueMissingError | requiredValueMissing
InvalidMapFormatError | invalidMapFormat


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
