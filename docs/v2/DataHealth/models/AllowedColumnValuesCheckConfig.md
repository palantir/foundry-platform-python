# AllowedColumnValuesCheckConfig

Checks that values in a column are within an allowed set of values.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**subject** | DatasetSubject | Yes |  |
**column_name** | ColumnName | Yes |  |
**allowed_values** | List[ColumnValue] | Yes |  |
**allow_null** | Optional[bool] | No |  |
**severity** | SeverityLevel | Yes |  |
**type** | Literal["allowedColumnValues"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
