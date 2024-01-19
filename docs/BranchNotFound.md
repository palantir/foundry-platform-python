# BranchNotFound

The requested branch could not be found, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**BranchAlreadyExistsParameters**](BranchAlreadyExistsParameters.md) |  |

## Example

```python
from foundry.models import BranchNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of BranchNotFound from a JSON string
branch_not_found_instance = BranchNotFound.from_json(json)
# print the JSON string representation of the object
print(BranchNotFound.to_json())

# convert the object into a dict
branch_not_found_dict = branch_not_found_instance.to_dict()
# create an instance of BranchNotFound from a dict
branch_not_found_form_dict = branch_not_found.from_dict(branch_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
