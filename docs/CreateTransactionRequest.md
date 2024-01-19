# CreateTransactionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_type** | [**TransactionType**](TransactionType.md) |  | \[optional\]

## Example

```python
from foundry.models import CreateTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransactionRequest from a JSON string
create_transaction_request_instance = CreateTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTransactionRequest.to_json())

# convert the object into a dict
create_transaction_request_dict = create_transaction_request_instance.to_dict()
# create an instance of CreateTransactionRequest from a dict
create_transaction_request_form_dict = create_transaction_request.from_dict(create_transaction_request_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
