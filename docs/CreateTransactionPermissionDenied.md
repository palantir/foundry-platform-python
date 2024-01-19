# CreateTransactionPermissionDenied

The provided token does not have permission to create a transaction on this dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**BranchAlreadyExistsParameters**](BranchAlreadyExistsParameters.md) |  |

## Example

```python
from foundry.models import CreateTransactionPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransactionPermissionDenied from a JSON string
create_transaction_permission_denied_instance = CreateTransactionPermissionDenied.from_json(json)
# print the JSON string representation of the object
print(CreateTransactionPermissionDenied.to_json())

# convert the object into a dict
create_transaction_permission_denied_dict = create_transaction_permission_denied_instance.to_dict()
# create an instance of CreateTransactionPermissionDenied from a dict
create_transaction_permission_denied_form_dict = create_transaction_permission_denied.from_dict(create_transaction_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
