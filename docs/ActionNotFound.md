# ActionNotFound

The action is not found, or the user does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ActionNotFoundParameters**](ActionNotFoundParameters.md) |  |

## Example

```python
from foundry.models import ActionNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ActionNotFound from a JSON string
action_not_found_instance = ActionNotFound.from_json(json)
# print the JSON string representation of the object
print(ActionNotFound.to_json())

# convert the object into a dict
action_not_found_dict = action_not_found_instance.to_dict()
# create an instance of ActionNotFound from a dict
action_not_found_form_dict = action_not_found.from_dict(action_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
