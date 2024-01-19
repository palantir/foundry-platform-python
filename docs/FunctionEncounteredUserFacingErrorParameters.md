# FunctionEncounteredUserFacingErrorParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_rid** | **str** | The unique resource identifier of a Function, useful for interacting with other Foundry APIs.  |
**function_version** | **str** | The version of the given Function, written \`\<major>.\<minor>.\<patch>-\<tag>\`, where \`-\<tag>\` is optional. Examples: \`1.2.3\`, \`1.2.3-rc1\`.  |
**message** | **str** |  |

## Example

```python
from foundry.models import FunctionEncounteredUserFacingErrorParameters

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionEncounteredUserFacingErrorParameters from a JSON string
function_encountered_user_facing_error_parameters_instance = FunctionEncounteredUserFacingErrorParameters.from_json(json)
# print the JSON string representation of the object
print(FunctionEncounteredUserFacingErrorParameters.to_json())

# convert the object into a dict
function_encountered_user_facing_error_parameters_dict = function_encountered_user_facing_error_parameters_instance.to_dict()
# create an instance of FunctionEncounteredUserFacingErrorParameters from a dict
function_encountered_user_facing_error_parameters_form_dict = function_encountered_user_facing_error_parameters.from_dict(function_encountered_user_facing_error_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
