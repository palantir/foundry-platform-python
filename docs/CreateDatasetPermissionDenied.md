# CreateDatasetPermissionDenied

The provided token does not have permission to create a dataset in this folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**CreateDatasetPermissionDeniedParameters**](CreateDatasetPermissionDeniedParameters.md) |  |

## Example

```python
from foundry.models import CreateDatasetPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDatasetPermissionDenied from a JSON string
create_dataset_permission_denied_instance = CreateDatasetPermissionDenied.from_json(json)
# print the JSON string representation of the object
print(CreateDatasetPermissionDenied.to_json())

# convert the object into a dict
create_dataset_permission_denied_dict = create_dataset_permission_denied_instance.to_dict()
# create an instance of CreateDatasetPermissionDenied from a dict
create_dataset_permission_denied_form_dict = create_dataset_permission_denied.from_dict(create_dataset_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
