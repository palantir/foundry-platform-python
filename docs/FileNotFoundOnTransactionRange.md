# FileNotFoundOnTransactionRange

The requested file could not be found on the given transaction range, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**FileNotFoundOnTransactionRangeParameters**](FileNotFoundOnTransactionRangeParameters.md) |  |

## Example

```python
from foundry.models import FileNotFoundOnTransactionRange

# TODO update the JSON string below
json = "{}"
# create an instance of FileNotFoundOnTransactionRange from a JSON string
file_not_found_on_transaction_range_instance = FileNotFoundOnTransactionRange.from_json(json)
# print the JSON string representation of the object
print(FileNotFoundOnTransactionRange.to_json())

# convert the object into a dict
file_not_found_on_transaction_range_dict = file_not_found_on_transaction_range_instance.to_dict()
# create an instance of FileNotFoundOnTransactionRange from a dict
file_not_found_on_transaction_range_form_dict = file_not_found_on_transaction_range.from_dict(file_not_found_on_transaction_range_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
