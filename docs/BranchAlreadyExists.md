# BranchAlreadyExists

The branch cannot be created because a branch with that name already exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**BranchAlreadyExistsParameters**](BranchAlreadyExistsParameters.md) |  |

## Example

```python
from foundry.models import BranchAlreadyExists

# TODO update the JSON string below
json = "{}"
# create an instance of BranchAlreadyExists from a JSON string
branch_already_exists_instance = BranchAlreadyExists.from_json(json)
# print the JSON string representation of the object
print(BranchAlreadyExists.to_json())

# convert the object into a dict
branch_already_exists_dict = branch_already_exists_instance.to_dict()
# create an instance of BranchAlreadyExists from a dict
branch_already_exists_form_dict = branch_already_exists.from_dict(branch_already_exists_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
