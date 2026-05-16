# EditsHistoryFilters

EditsHistoryFilters

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**start_time** | Optional[datetime] | No | Filter edits to only those that occurred after this timestamp (inclusive). ISO 8601 format. Example: "2024-01-01T00:00:00Z"  |
**end_time** | Optional[datetime] | No | Filter edits to only those that occurred before this timestamp (inclusive). ISO 8601 format. Example: "2024-12-31T23:59:59Z"  |
**action_types** | List[ActionTypeApiName] | Yes | Filter edits to only those caused by specific action types. If not specified, edits from all action types are returned.  |
**edit_types** | List[EditTypeFilter] | Yes | Filter edits by operation type (create, modify, or delete). If not specified, all edit types are returned.  |
**user_ids** | List[str] | Yes | Filter edits to only those performed by specific users. If not specified, edits from all users are returned.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
