# TransactionNotCommitted

The given transaction has not been committed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**TransactionNotCommittedParameters**](TransactionNotCommittedParameters.md) |  |

## Example

```python
from foundry.models import TransactionNotCommitted

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionNotCommitted from a JSON string
transaction_not_committed_instance = TransactionNotCommitted.from_json(json)
# print the JSON string representation of the object
print(TransactionNotCommitted.to_json())

# convert the object into a dict
transaction_not_committed_dict = transaction_not_committed_instance.to_dict()
# create an instance of TransactionNotCommitted from a dict
transaction_not_committed_form_dict = transaction_not_committed.from_dict(transaction_not_committed_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
