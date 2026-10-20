# InputValue

A value fulfilling a product input. Use a representation advertised by the input's `supportedTypes`, preferring the first applicable representation. Structured values use the `resolved` variant.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
InputValueApiName | apiName
InputValueBoolean | boolean
InputValueCredential | credential
InputValueCron | cron
InputValueInteger | integer
InputValueResolved | resolved
InputValueRid | rid
InputValueRidWithVersion | ridWithVersion
InputValueString | string
InputValueStrings | strings


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
