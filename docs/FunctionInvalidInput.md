# FunctionInvalidInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**FunctionExecutionFailedParameters**](FunctionExecutionFailedParameters.md) |  |

## Example

```python
from foundry.models import FunctionInvalidInput

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionInvalidInput from a JSON string
function_invalid_input_instance = FunctionInvalidInput.from_json(json)
# print the JSON string representation of the object
print(FunctionInvalidInput.to_json())

# convert the object into a dict
function_invalid_input_dict = function_invalid_input_instance.to_dict()
# create an instance of FunctionInvalidInput from a dict
function_invalid_input_form_dict = function_invalid_input.from_dict(function_invalid_input_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
