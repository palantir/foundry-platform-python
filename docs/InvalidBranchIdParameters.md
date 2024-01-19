# InvalidBranchIdParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | The identifier (name) of a Branch. Example: \`master\`.  |

## Example

```python
from foundry.models import InvalidBranchIdParameters

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidBranchIdParameters from a JSON string
invalid_branch_id_parameters_instance = InvalidBranchIdParameters.from_json(json)
# print the JSON string representation of the object
print(InvalidBranchIdParameters.to_json())

# convert the object into a dict
invalid_branch_id_parameters_dict = invalid_branch_id_parameters_instance.to_dict()
# create an instance of InvalidBranchIdParameters from a dict
invalid_branch_id_parameters_form_dict = invalid_branch_id_parameters.from_dict(invalid_branch_id_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
