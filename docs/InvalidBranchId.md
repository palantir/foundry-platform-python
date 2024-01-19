# InvalidBranchId

The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidBranchIdParameters**](InvalidBranchIdParameters.md) |  |

## Example

```python
from foundry.models import InvalidBranchId

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidBranchId from a JSON string
invalid_branch_id_instance = InvalidBranchId.from_json(json)
# print the JSON string representation of the object
print(InvalidBranchId.to_json())

# convert the object into a dict
invalid_branch_id_dict = invalid_branch_id_instance.to_dict()
# create an instance of InvalidBranchId from a dict
invalid_branch_id_form_dict = invalid_branch_id.from_dict(invalid_branch_id_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
