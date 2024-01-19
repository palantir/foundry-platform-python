# CompositePrimaryKeyNotSupportedParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**primary_key** | **List\[str\]** |  | \[optional\]

## Example

```python
from foundry.models import CompositePrimaryKeyNotSupportedParameters

# TODO update the JSON string below
json = "{}"
# create an instance of CompositePrimaryKeyNotSupportedParameters from a JSON string
composite_primary_key_not_supported_parameters_instance = CompositePrimaryKeyNotSupportedParameters.from_json(json)
# print the JSON string representation of the object
print(CompositePrimaryKeyNotSupportedParameters.to_json())

# convert the object into a dict
composite_primary_key_not_supported_parameters_dict = composite_primary_key_not_supported_parameters_instance.to_dict()
# create an instance of CompositePrimaryKeyNotSupportedParameters from a dict
composite_primary_key_not_supported_parameters_form_dict = composite_primary_key_not_supported_parameters.from_dict(composite_primary_key_not_supported_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
