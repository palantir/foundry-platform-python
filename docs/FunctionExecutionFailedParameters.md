# FunctionExecutionFailedParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_rid** | **str** | The unique resource identifier of a Function, useful for interacting with other Foundry APIs.  |
**function_version** | **str** | The version of the given Function, written \`\<major>.\<minor>.\<patch>-\<tag>\`, where \`-\<tag>\` is optional. Examples: \`1.2.3\`, \`1.2.3-rc1\`.  |

## Example

```python
from foundry.models import FunctionExecutionFailedParameters

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionExecutionFailedParameters from a JSON string
function_execution_failed_parameters_instance = FunctionExecutionFailedParameters.from_json(json)
# print the JSON string representation of the object
print(FunctionExecutionFailedParameters.to_json())

# convert the object into a dict
function_execution_failed_parameters_dict = function_execution_failed_parameters_instance.to_dict()
# create an instance of FunctionExecutionFailedParameters from a dict
function_execution_failed_parameters_form_dict = function_execution_failed_parameters.from_dict(function_execution_failed_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
