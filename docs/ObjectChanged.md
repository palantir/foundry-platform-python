# ObjectChanged

An object used by this `Action` was changed by someone else while the `Action` was running.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import ObjectChanged

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectChanged from a JSON string
object_changed_instance = ObjectChanged.from_json(json)
# print the JSON string representation of the object
print(ObjectChanged.to_json())

# convert the object into a dict
object_changed_dict = object_changed_instance.to_dict()
# create an instance of ObjectChanged from a dict
object_changed_form_dict = object_changed.from_dict(object_changed_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
