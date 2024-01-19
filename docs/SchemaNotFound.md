# SchemaNotFound

A schema could not be found for the given dataset and branch, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**DeleteSchemaPermissionDeniedParameters**](DeleteSchemaPermissionDeniedParameters.md) |  |

## Example

```python
from foundry.models import SchemaNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaNotFound from a JSON string
schema_not_found_instance = SchemaNotFound.from_json(json)
# print the JSON string representation of the object
print(SchemaNotFound.to_json())

# convert the object into a dict
schema_not_found_dict = schema_not_found_instance.to_dict()
# create an instance of SchemaNotFound from a dict
schema_not_found_form_dict = schema_not_found.from_dict(schema_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
