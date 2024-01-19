# AbortTransactionPermissionDenied

The provided token does not have permission to abort the given treansaction on the given dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**AbortTransactionPermissionDeniedParameters**](AbortTransactionPermissionDeniedParameters.md) |  |

## Example

```python
from foundry.models import AbortTransactionPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of AbortTransactionPermissionDenied from a JSON string
abort_transaction_permission_denied_instance = AbortTransactionPermissionDenied.from_json(json)
# print the JSON string representation of the object
print(AbortTransactionPermissionDenied.to_json())

# convert the object into a dict
abort_transaction_permission_denied_dict = abort_transaction_permission_denied_instance.to_dict()
# create an instance of AbortTransactionPermissionDenied from a dict
abort_transaction_permission_denied_form_dict = abort_transaction_permission_denied.from_dict(abort_transaction_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
