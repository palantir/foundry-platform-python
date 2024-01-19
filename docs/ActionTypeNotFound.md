# ActionTypeNotFound

The action type is not found, or the user does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ActionTypeNotFoundParameters**](ActionTypeNotFoundParameters.md) |  |

## Example

```python
from foundry.models import ActionTypeNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ActionTypeNotFound from a JSON string
action_type_not_found_instance = ActionTypeNotFound.from_json(json)
# print the JSON string representation of the object
print(ActionTypeNotFound.to_json())

# convert the object into a dict
action_type_not_found_dict = action_type_not_found_instance.to_dict()
# create an instance of ActionTypeNotFound from a dict
action_type_not_found_form_dict = action_type_not_found.from_dict(action_type_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
