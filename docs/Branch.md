# Branch

A Branch of a Dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | The identifier (name) of a Branch. Example: \`master\`.  |
**transaction_rid** | **str** | The Resource Identifier (RID) of a Transaction. Example: \`ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4\`.  | \[optional\]

## Example

```python
from foundry.models import Branch

# TODO update the JSON string below
json = "{}"
# create an instance of Branch from a JSON string
branch_instance = Branch.from_json(json)
# print the JSON string representation of the object
print(Branch.to_json())

# convert the object into a dict
branch_dict = branch_instance.to_dict()
# create an instance of Branch from a dict
branch_form_dict = branch.from_dict(branch_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
