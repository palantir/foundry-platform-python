# CreateDatasetPermissionDeniedParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**parent_folder_rid** | **str** |  |

## Example

```python
from foundry.models import CreateDatasetPermissionDeniedParameters

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDatasetPermissionDeniedParameters from a JSON string
create_dataset_permission_denied_parameters_instance = CreateDatasetPermissionDeniedParameters.from_json(json)
# print the JSON string representation of the object
print(CreateDatasetPermissionDeniedParameters.to_json())

# convert the object into a dict
create_dataset_permission_denied_parameters_dict = create_dataset_permission_denied_parameters_instance.to_dict()
# create an instance of CreateDatasetPermissionDeniedParameters from a dict
create_dataset_permission_denied_parameters_form_dict = create_dataset_permission_denied_parameters.from_dict(create_dataset_permission_denied_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
