# TransactionNotFound

The requested transaction could not be found on the dataset, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**AbortTransactionPermissionDeniedParameters**](AbortTransactionPermissionDeniedParameters.md) |  |

## Example

```python
from foundry.models import TransactionNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionNotFound from a JSON string
transaction_not_found_instance = TransactionNotFound.from_json(json)
# print the JSON string representation of the object
print(TransactionNotFound.to_json())

# convert the object into a dict
transaction_not_found_dict = transaction_not_found_instance.to_dict()
# create an instance of TransactionNotFound from a dict
transaction_not_found_form_dict = transaction_not_found.from_dict(transaction_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
