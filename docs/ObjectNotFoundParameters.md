# ObjectNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  | \[optional\]
**primary_key** | **Dict\[str, object\]** |  | \[optional\]

## Example

```python
from foundry.models import ObjectNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectNotFoundParameters from a JSON string
object_not_found_parameters_instance = ObjectNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(ObjectNotFoundParameters.to_json())

# convert the object into a dict
object_not_found_parameters_dict = object_not_found_parameters_instance.to_dict()
# create an instance of ObjectNotFoundParameters from a dict
object_not_found_parameters_form_dict = object_not_found_parameters.from_dict(object_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
