# FunctionExecutionTimedOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**FunctionExecutionFailedParameters**](FunctionExecutionFailedParameters.md) |  |

## Example

```python
from foundry.models import FunctionExecutionTimedOut

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionExecutionTimedOut from a JSON string
function_execution_timed_out_instance = FunctionExecutionTimedOut.from_json(json)
# print the JSON string representation of the object
print(FunctionExecutionTimedOut.to_json())

# convert the object into a dict
function_execution_timed_out_dict = function_execution_timed_out_instance.to_dict()
# create an instance of FunctionExecutionTimedOut from a dict
function_execution_timed_out_form_dict = function_execution_timed_out.from_dict(function_execution_timed_out_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
