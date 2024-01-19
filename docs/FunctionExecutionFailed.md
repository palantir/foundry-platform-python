# FunctionExecutionFailed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**FunctionExecutionFailedParameters**](FunctionExecutionFailedParameters.md) |  |

## Example

```python
from foundry.models import FunctionExecutionFailed

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionExecutionFailed from a JSON string
function_execution_failed_instance = FunctionExecutionFailed.from_json(json)
# print the JSON string representation of the object
print(FunctionExecutionFailed.to_json())

# convert the object into a dict
function_execution_failed_dict = function_execution_failed_instance.to_dict()
# create an instance of FunctionExecutionFailed from a dict
function_execution_failed_form_dict = function_execution_failed.from_dict(function_execution_failed_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
