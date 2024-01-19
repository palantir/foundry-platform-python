# PutSchemaPermissionDenied

todo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**BranchAlreadyExistsParameters**](BranchAlreadyExistsParameters.md) |  |

## Example

```python
from foundry.models import PutSchemaPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of PutSchemaPermissionDenied from a JSON string
put_schema_permission_denied_instance = PutSchemaPermissionDenied.from_json(json)
# print the JSON string representation of the object
print(PutSchemaPermissionDenied.to_json())

# convert the object into a dict
put_schema_permission_denied_dict = put_schema_permission_denied_instance.to_dict()
# create an instance of PutSchemaPermissionDenied from a dict
put_schema_permission_denied_form_dict = put_schema_permission_denied.from_dict(put_schema_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
