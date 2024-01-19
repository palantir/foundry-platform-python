# ViewObjectPermissionDenied

The user does not have permission to view objects of this `ObjectType`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ObjectTypeNotSyncedParameters**](ObjectTypeNotSyncedParameters.md) |  |

## Example

```python
from foundry.models import ViewObjectPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of ViewObjectPermissionDenied from a JSON string
view_object_permission_denied_instance = ViewObjectPermissionDenied.from_json(json)
# print the JSON string representation of the object
print(ViewObjectPermissionDenied.to_json())

# convert the object into a dict
view_object_permission_denied_dict = view_object_permission_denied_instance.to_dict()
# create an instance of ViewObjectPermissionDenied from a dict
view_object_permission_denied_form_dict = view_object_permission_denied.from_dict(view_object_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
