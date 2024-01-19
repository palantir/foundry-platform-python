# ActionContainsDuplicateEdits

The given action request has multiple edits on the same object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import ActionContainsDuplicateEdits

# TODO update the JSON string below
json = "{}"
# create an instance of ActionContainsDuplicateEdits from a JSON string
action_contains_duplicate_edits_instance = ActionContainsDuplicateEdits.from_json(json)
# print the JSON string representation of the object
print(ActionContainsDuplicateEdits.to_json())

# convert the object into a dict
action_contains_duplicate_edits_dict = action_contains_duplicate_edits_instance.to_dict()
# create an instance of ActionContainsDuplicateEdits from a dict
action_contains_duplicate_edits_form_dict = action_contains_duplicate_edits.from_dict(action_contains_duplicate_edits_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
