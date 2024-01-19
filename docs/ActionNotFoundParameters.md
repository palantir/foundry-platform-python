# ActionNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_rid** | **str** | The unique resource identifier for an action. |

## Example

```python
from foundry.models import ActionNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ActionNotFoundParameters from a JSON string
action_not_found_parameters_instance = ActionNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(ActionNotFoundParameters.to_json())

# convert the object into a dict
action_not_found_parameters_dict = action_not_found_parameters_instance.to_dict()
# create an instance of ActionNotFoundParameters from a dict
action_not_found_parameters_form_dict = action_not_found_parameters.from_dict(action_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
