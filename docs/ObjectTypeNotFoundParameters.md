# ObjectTypeNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  | \[optional\]
**object_type_rid** | **str** | The unique resource identifier of an object type, useful for interacting with other Foundry APIs. | \[optional\]

## Example

```python
from foundry.models import ObjectTypeNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectTypeNotFoundParameters from a JSON string
object_type_not_found_parameters_instance = ObjectTypeNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(ObjectTypeNotFoundParameters.to_json())

# convert the object into a dict
object_type_not_found_parameters_dict = object_type_not_found_parameters_instance.to_dict()
# create an instance of ObjectTypeNotFoundParameters from a dict
object_type_not_found_parameters_form_dict = object_type_not_found_parameters.from_dict(object_type_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
