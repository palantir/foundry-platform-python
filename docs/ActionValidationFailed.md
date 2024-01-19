# ActionValidationFailed

The validation failed for the given action parameters. Please use the `validateAction` endpoint for more details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ActionValidationFailedParameters**](ActionValidationFailedParameters.md) |  |

## Example

```python
from foundry.models import ActionValidationFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ActionValidationFailed from a JSON string
action_validation_failed_instance = ActionValidationFailed.from_json(json)
# print the JSON string representation of the object
print(ActionValidationFailed.to_json())

# convert the object into a dict
action_validation_failed_dict = action_validation_failed_instance.to_dict()
# create an instance of ActionValidationFailed from a dict
action_validation_failed_form_dict = action_validation_failed.from_dict(action_validation_failed_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
