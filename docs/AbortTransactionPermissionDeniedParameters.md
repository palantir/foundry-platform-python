# AbortTransactionPermissionDeniedParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_rid** | **str** | The Resource Identifier (RID) of a Dataset. Example: \`ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da\`.  |
**transaction_rid** | **str** | The Resource Identifier (RID) of a Transaction. Example: \`ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4\`.  |

## Example

```python
from foundry.models import AbortTransactionPermissionDeniedParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AbortTransactionPermissionDeniedParameters from a JSON string
abort_transaction_permission_denied_parameters_instance = AbortTransactionPermissionDeniedParameters.from_json(json)
# print the JSON string representation of the object
print(AbortTransactionPermissionDeniedParameters.to_json())

# convert the object into a dict
abort_transaction_permission_denied_parameters_dict = abort_transaction_permission_denied_parameters_instance.to_dict()
# create an instance of AbortTransactionPermissionDeniedParameters from a dict
abort_transaction_permission_denied_parameters_form_dict = abort_transaction_permission_denied_parameters.from_dict(abort_transaction_permission_denied_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
