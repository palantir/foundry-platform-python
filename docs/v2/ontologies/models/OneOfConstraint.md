# OneOfConstraint

The parameter has a manually predefined set of options.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**options** | List[ParameterOption] | Yes |  |
**other_values_allowed** | pydantic.StrictBool | Yes | A flag denoting whether custom, user provided values will be considered valid. This is configured via the **Allowed "Other" value** toggle in the **Ontology Manager**. |
**type** | Literal["oneOf"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
