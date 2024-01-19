# ActionEditedPropertiesNotFound

Actions attempted to edit properties that could not be found on the object type. Please contact the Ontology administrator to resolve this issue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import ActionEditedPropertiesNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ActionEditedPropertiesNotFound from a JSON string
action_edited_properties_not_found_instance = ActionEditedPropertiesNotFound.from_json(json)
# print the JSON string representation of the object
print(ActionEditedPropertiesNotFound.to_json())

# convert the object into a dict
action_edited_properties_not_found_dict = action_edited_properties_not_found_instance.to_dict()
# create an instance of ActionEditedPropertiesNotFound from a dict
action_edited_properties_not_found_form_dict = action_edited_properties_not_found.from_dict(action_edited_properties_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
