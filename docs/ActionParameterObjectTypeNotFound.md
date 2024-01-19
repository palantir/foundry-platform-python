# ActionParameterObjectTypeNotFound

The parameter references an object type that could not be found, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ActionParameterObjectNotFoundParameters**](ActionParameterObjectNotFoundParameters.md) |  |

## Example

```python
from foundry.models import ActionParameterObjectTypeNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ActionParameterObjectTypeNotFound from a JSON string
action_parameter_object_type_not_found_instance = ActionParameterObjectTypeNotFound.from_json(json)
# print the JSON string representation of the object
print(ActionParameterObjectTypeNotFound.to_json())

# convert the object into a dict
action_parameter_object_type_not_found_dict = action_parameter_object_type_not_found_instance.to_dict()
# create an instance of ActionParameterObjectTypeNotFound from a dict
action_parameter_object_type_not_found_form_dict = action_parameter_object_type_not_found.from_dict(action_parameter_object_type_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
