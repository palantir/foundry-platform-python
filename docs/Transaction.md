# Transaction

An operation that modifies the files within a dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_time** | **datetime** | The timestamp when the transaction was closed, in ISO 8601 timestamp format. | \[optional\]
**created_time** | **datetime** | The timestamp when the transaction was created, in ISO 8601 timestamp format. |
**rid** | **str** | The Resource Identifier (RID) of a Transaction. Example: \`ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4\`.  |
**status** | [**TransactionStatus**](TransactionStatus.md) |  |
**transaction_type** | [**TransactionType**](TransactionType.md) |  |

## Example

```python
from foundry.models import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_form_dict = transaction.from_dict(transaction_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
