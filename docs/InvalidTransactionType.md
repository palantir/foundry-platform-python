# InvalidTransactionType

The given transaction type is not valid. Valid transaction types are `SNAPSHOT`, `UPDATE`, `APPEND`, and `DELETE`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidTransactionTypeParameters**](InvalidTransactionTypeParameters.md) |  |

## Example

```python
from foundry.models import InvalidTransactionType

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidTransactionType from a JSON string
invalid_transaction_type_instance = InvalidTransactionType.from_json(json)
# print the JSON string representation of the object
print(InvalidTransactionType.to_json())

# convert the object into a dict
invalid_transaction_type_dict = invalid_transaction_type_instance.to_dict()
# create an instance of InvalidTransactionType from a dict
invalid_transaction_type_form_dict = invalid_transaction_type.from_dict(invalid_transaction_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
