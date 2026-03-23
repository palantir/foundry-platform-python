# FieldValidationError

A dataset column type is not compatible with the trainer's supported column types.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**dataset_rid** | RID | Yes | The RID of the dataset containing the invalid field. |
**field_name** | Optional[str] | No | The name of the dataset column or field that failed validation. |
**field_type** | str | Yes | The type of the dataset field. |
**type** | Literal["fieldValidationFailure"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
