# DeleteSchemaPermissionDenied

todo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**DeleteSchemaPermissionDeniedParameters**](DeleteSchemaPermissionDeniedParameters.md) |  |

## Example

```python
from foundry.models import DeleteSchemaPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSchemaPermissionDenied from a JSON string
delete_schema_permission_denied_instance = DeleteSchemaPermissionDenied.from_json(json)
# print the JSON string representation of the object
print(DeleteSchemaPermissionDenied.to_json())

# convert the object into a dict
delete_schema_permission_denied_dict = delete_schema_permission_denied_instance.to_dict()
# create an instance of DeleteSchemaPermissionDenied from a dict
delete_schema_permission_denied_form_dict = delete_schema_permission_denied.from_dict(delete_schema_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
