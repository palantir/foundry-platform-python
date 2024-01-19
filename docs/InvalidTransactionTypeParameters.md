# InvalidTransactionTypeParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_rid** | **str** | The Resource Identifier (RID) of a Dataset. Example: \`ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da\`.  |
**transaction_rid** | **str** | The Resource Identifier (RID) of a Transaction. Example: \`ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4\`.  |
**transaction_type** | [**TransactionType**](TransactionType.md) |  |

## Example

```python
from foundry.models import InvalidTransactionTypeParameters

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidTransactionTypeParameters from a JSON string
invalid_transaction_type_parameters_instance = InvalidTransactionTypeParameters.from_json(json)
# print the JSON string representation of the object
print(InvalidTransactionTypeParameters.to_json())

# convert the object into a dict
invalid_transaction_type_parameters_dict = invalid_transaction_type_parameters_instance.to_dict()
# create an instance of InvalidTransactionTypeParameters from a dict
invalid_transaction_type_parameters_form_dict = invalid_transaction_type_parameters.from_dict(invalid_transaction_type_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
