# FileNotFoundOnBranchParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | The identifier (name) of a Branch. Example: \`master\`.  |
**dataset_rid** | **str** | The Resource Identifier (RID) of a Dataset. Example: \`ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da\`.  |
**path** | **str** | The path to a File within Foundry. Examples: \`my-file.txt\`, \`path/to/my-file.jpg\`, \`dataframe.snappy.parquet\`.  |

## Example

```python
from foundry.models import FileNotFoundOnBranchParameters

# TODO update the JSON string below
json = "{}"
# create an instance of FileNotFoundOnBranchParameters from a JSON string
file_not_found_on_branch_parameters_instance = FileNotFoundOnBranchParameters.from_json(json)
# print the JSON string representation of the object
print(FileNotFoundOnBranchParameters.to_json())

# convert the object into a dict
file_not_found_on_branch_parameters_dict = file_not_found_on_branch_parameters_instance.to_dict()
# create an instance of FileNotFoundOnBranchParameters from a dict
file_not_found_on_branch_parameters_form_dict = file_not_found_on_branch_parameters.from_dict(file_not_found_on_branch_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
