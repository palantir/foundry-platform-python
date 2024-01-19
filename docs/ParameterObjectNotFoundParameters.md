# ParameterObjectNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**primary_key** | **Dict\[str, object\]** |  | \[optional\]

## Example

```python
from foundry.models import ParameterObjectNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterObjectNotFoundParameters from a JSON string
parameter_object_not_found_parameters_instance = ParameterObjectNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(ParameterObjectNotFoundParameters.to_json())

# convert the object into a dict
parameter_object_not_found_parameters_dict = parameter_object_not_found_parameters_instance.to_dict()
# create an instance of ParameterObjectNotFoundParameters from a dict
parameter_object_not_found_parameters_form_dict = parameter_object_not_found_parameters.from_dict(parameter_object_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
