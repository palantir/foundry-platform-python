# DeleteBranchPermissionDenied

The provided token does not have permission to delete the given branch from this dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**BranchAlreadyExistsParameters**](BranchAlreadyExistsParameters.md) |  |

## Example

```python
from foundry.models import DeleteBranchPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBranchPermissionDenied from a JSON string
delete_branch_permission_denied_instance = DeleteBranchPermissionDenied.from_json(json)
# print the JSON string representation of the object
print(DeleteBranchPermissionDenied.to_json())

# convert the object into a dict
delete_branch_permission_denied_dict = delete_branch_permission_denied_instance.to_dict()
# create an instance of DeleteBranchPermissionDenied from a dict
delete_branch_permission_denied_form_dict = delete_branch_permission_denied.from_dict(delete_branch_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
