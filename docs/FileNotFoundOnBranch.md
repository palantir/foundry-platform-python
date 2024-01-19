# FileNotFoundOnBranch

The requested file could not be found on the given branch, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**FileNotFoundOnBranchParameters**](FileNotFoundOnBranchParameters.md) |  |

## Example

```python
from foundry.models import FileNotFoundOnBranch

# TODO update the JSON string below
json = "{}"
# create an instance of FileNotFoundOnBranch from a JSON string
file_not_found_on_branch_instance = FileNotFoundOnBranch.from_json(json)
# print the JSON string representation of the object
print(FileNotFoundOnBranch.to_json())

# convert the object into a dict
file_not_found_on_branch_dict = file_not_found_on_branch_instance.to_dict()
# create an instance of FileNotFoundOnBranch from a dict
file_not_found_on_branch_form_dict = file_not_found_on_branch.from_dict(file_not_found_on_branch_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
