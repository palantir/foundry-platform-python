# AsyncOperationError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **Dict\[str, object\]** |  | \[optional\]
**type** | **str** |  |

## Example

```python
from foundry.models import AsyncOperationError

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncOperationError from a JSON string
async_operation_error_instance = AsyncOperationError.from_json(json)
# print the JSON string representation of the object
print(AsyncOperationError.to_json())

# convert the object into a dict
async_operation_error_dict = async_operation_error_instance.to_dict()
# create an instance of AsyncOperationError from a dict
async_operation_error_form_dict = async_operation_error.from_dict(async_operation_error_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
