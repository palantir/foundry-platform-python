# ActionParameterObjectNotFound

The parameter object reference or parameter default value is not found, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ActionParameterObjectNotFoundParameters**](ActionParameterObjectNotFoundParameters.md) |  |

## Example

```python
from foundry.models import ActionParameterObjectNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ActionParameterObjectNotFound from a JSON string
action_parameter_object_not_found_instance = ActionParameterObjectNotFound.from_json(json)
# print the JSON string representation of the object
print(ActionParameterObjectNotFound.to_json())

# convert the object into a dict
action_parameter_object_not_found_dict = action_parameter_object_not_found_instance.to_dict()
# create an instance of ActionParameterObjectNotFound from a dict
action_parameter_object_not_found_form_dict = action_parameter_object_not_found.from_dict(action_parameter_object_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
