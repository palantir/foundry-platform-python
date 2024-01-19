# CommitTransactionPermissionDenied

The provided token does not have permission to commit the given treansaction on the given dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**AbortTransactionPermissionDeniedParameters**](AbortTransactionPermissionDeniedParameters.md) |  |

## Example

```python
from foundry.models import CommitTransactionPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of CommitTransactionPermissionDenied from a JSON string
commit_transaction_permission_denied_instance = CommitTransactionPermissionDenied.from_json(json)
# print the JSON string representation of the object
print(CommitTransactionPermissionDenied.to_json())

# convert the object into a dict
commit_transaction_permission_denied_dict = commit_transaction_permission_denied_instance.to_dict()
# create an instance of CommitTransactionPermissionDenied from a dict
commit_transaction_permission_denied_form_dict = commit_transaction_permission_denied.from_dict(commit_transaction_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
