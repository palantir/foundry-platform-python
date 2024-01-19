# BranchAlreadyExistsParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | The identifier (name) of a Branch. Example: \`master\`.  |
**dataset_rid** | **str** | The Resource Identifier (RID) of a Dataset. Example: \`ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da\`.  |

## Example

```python
from foundry.models import BranchAlreadyExistsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of BranchAlreadyExistsParameters from a JSON string
branch_already_exists_parameters_instance = BranchAlreadyExistsParameters.from_json(json)
# print the JSON string representation of the object
print(BranchAlreadyExistsParameters.to_json())

# convert the object into a dict
branch_already_exists_parameters_dict = branch_already_exists_parameters_instance.to_dict()
# create an instance of BranchAlreadyExistsParameters from a dict
branch_already_exists_parameters_form_dict = branch_already_exists_parameters.from_dict(branch_already_exists_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
