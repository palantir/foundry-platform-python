# ReadTablePermissionDenied

The provided token does not have permission to read the given dataset as a table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ColumnTypesNotSupportedParameters**](ColumnTypesNotSupportedParameters.md) |  |

## Example

```python
from foundry.models import ReadTablePermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of ReadTablePermissionDenied from a JSON string
read_table_permission_denied_instance = ReadTablePermissionDenied.from_json(json)
# print the JSON string representation of the object
print(ReadTablePermissionDenied.to_json())

# convert the object into a dict
read_table_permission_denied_dict = read_table_permission_denied_instance.to_dict()
# create an instance of ReadTablePermissionDenied from a dict
read_table_permission_denied_form_dict = read_table_permission_denied.from_dict(read_table_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
