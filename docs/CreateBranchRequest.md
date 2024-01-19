# CreateBranchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | The identifier (name) of a Branch. Example: \`master\`.  |
**transaction_rid** | **str** | The Resource Identifier (RID) of a Transaction. Example: \`ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4\`.  | \[optional\]

## Example

```python
from foundry.models import CreateBranchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBranchRequest from a JSON string
create_branch_request_instance = CreateBranchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBranchRequest.to_json())

# convert the object into a dict
create_branch_request_dict = create_branch_request_instance.to_dict()
# create an instance of CreateBranchRequest from a dict
create_branch_request_form_dict = create_branch_request.from_dict(create_branch_request_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
