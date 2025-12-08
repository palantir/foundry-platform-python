# PropertyLoadLevel

The load level of the property:
- APPLY_REDUCERS: Returns a single value of an array as configured in the ontology.
- EXTRACT_MAIN_VALUE: Returns the main value of a struct as configured in the ontology.
- APPLY_REDUCERS_AND_EXTRACT_MAIN_VALUE: Performs both to return the reduced main value.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ApplyReducersAndExtractMainValueLoadLevel | applyReducersAndExtractMainValue
ApplyReducersLoadLevel | applyReducers
ExtractMainValueLoadLevel | extractMainValue


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
