# OpenTransactionAlreadyExists

A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**BranchAlreadyExistsParameters**](BranchAlreadyExistsParameters.md) |  |

## Example

```python
from foundry.models import OpenTransactionAlreadyExists

# TODO update the JSON string below
json = "{}"
# create an instance of OpenTransactionAlreadyExists from a JSON string
open_transaction_already_exists_instance = OpenTransactionAlreadyExists.from_json(json)
# print the JSON string representation of the object
print(OpenTransactionAlreadyExists.to_json())

# convert the object into a dict
open_transaction_already_exists_dict = open_transaction_already_exists_instance.to_dict()
# create an instance of OpenTransactionAlreadyExists from a dict
open_transaction_already_exists_form_dict = open_transaction_already_exists.from_dict(open_transaction_already_exists_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
