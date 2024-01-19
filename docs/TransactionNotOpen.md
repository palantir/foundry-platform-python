# TransactionNotOpen

The given transaction is not open.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**TransactionNotCommittedParameters**](TransactionNotCommittedParameters.md) |  |

## Example

```python
from foundry.models import TransactionNotOpen

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionNotOpen from a JSON string
transaction_not_open_instance = TransactionNotOpen.from_json(json)
# print the JSON string representation of the object
print(TransactionNotOpen.to_json())

# convert the object into a dict
transaction_not_open_dict = transaction_not_open_instance.to_dict()
# create an instance of TransactionNotOpen from a dict
transaction_not_open_form_dict = transaction_not_open.from_dict(transaction_not_open_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
