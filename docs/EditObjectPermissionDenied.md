# EditObjectPermissionDenied

The user does not have permission to edit this `ObjectType`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import EditObjectPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of EditObjectPermissionDenied from a JSON string
edit_object_permission_denied_instance = EditObjectPermissionDenied.from_json(json)
# print the JSON string representation of the object
print(EditObjectPermissionDenied.to_json())

# convert the object into a dict
edit_object_permission_denied_dict = edit_object_permission_denied_instance.to_dict()
# create an instance of EditObjectPermissionDenied from a dict
edit_object_permission_denied_form_dict = edit_object_permission_denied.from_dict(edit_object_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
