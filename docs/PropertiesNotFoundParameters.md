# PropertiesNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**properties** | **List\[str\]** |  | \[optional\]

## Example

```python
from foundry.models import PropertiesNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of PropertiesNotFoundParameters from a JSON string
properties_not_found_parameters_instance = PropertiesNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(PropertiesNotFoundParameters.to_json())

# convert the object into a dict
properties_not_found_parameters_dict = properties_not_found_parameters_instance.to_dict()
# create an instance of PropertiesNotFoundParameters from a dict
properties_not_found_parameters_form_dict = properties_not_found_parameters.from_dict(properties_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
