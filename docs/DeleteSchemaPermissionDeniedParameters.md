# DeleteSchemaPermissionDeniedParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | The identifier (name) of a Branch. Example: \`master\`.  |
**dataset_rid** | **str** | The Resource Identifier (RID) of a Dataset. Example: \`ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da\`.  |
**transaction_rid** | **str** | The Resource Identifier (RID) of a Transaction. Example: \`ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4\`.  | \[optional\]

## Example

```python
from foundry.models import DeleteSchemaPermissionDeniedParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSchemaPermissionDeniedParameters from a JSON string
delete_schema_permission_denied_parameters_instance = DeleteSchemaPermissionDeniedParameters.from_json(json)
# print the JSON string representation of the object
print(DeleteSchemaPermissionDeniedParameters.to_json())

# convert the object into a dict
delete_schema_permission_denied_parameters_dict = delete_schema_permission_denied_parameters_instance.to_dict()
# create an instance of DeleteSchemaPermissionDeniedParameters from a dict
delete_schema_permission_denied_parameters_form_dict = delete_schema_permission_denied_parameters.from_dict(delete_schema_permission_denied_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
