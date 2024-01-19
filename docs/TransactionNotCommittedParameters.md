# TransactionNotCommittedParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_rid** | **str** | The Resource Identifier (RID) of a Dataset. Example: \`ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da\`.  |
**transaction_rid** | **str** | The Resource Identifier (RID) of a Transaction. Example: \`ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4\`.  |
**transaction_status** | [**TransactionStatus**](TransactionStatus.md) |  |

## Example

```python
from foundry.models import TransactionNotCommittedParameters

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionNotCommittedParameters from a JSON string
transaction_not_committed_parameters_instance = TransactionNotCommittedParameters.from_json(json)
# print the JSON string representation of the object
print(TransactionNotCommittedParameters.to_json())

# convert the object into a dict
transaction_not_committed_parameters_dict = transaction_not_committed_parameters_instance.to_dict()
# create an instance of TransactionNotCommittedParameters from a dict
transaction_not_committed_parameters_form_dict = transaction_not_committed_parameters.from_dict(transaction_not_committed_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
