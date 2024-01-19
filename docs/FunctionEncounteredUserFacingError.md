# FunctionEncounteredUserFacingError

The authored function failed to execute because of a user induced error. The message argument is meant to be displayed to the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**FunctionEncounteredUserFacingErrorParameters**](FunctionEncounteredUserFacingErrorParameters.md) |  |

## Example

```python
from foundry.models import FunctionEncounteredUserFacingError

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionEncounteredUserFacingError from a JSON string
function_encountered_user_facing_error_instance = FunctionEncounteredUserFacingError.from_json(json)
# print the JSON string representation of the object
print(FunctionEncounteredUserFacingError.to_json())

# convert the object into a dict
function_encountered_user_facing_error_dict = function_encountered_user_facing_error_instance.to_dict()
# create an instance of FunctionEncounteredUserFacingError from a dict
function_encountered_user_facing_error_form_dict = function_encountered_user_facing_error.from_dict(function_encountered_user_facing_error_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
