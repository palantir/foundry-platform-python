# InvalidPropertyFiltersCombinationParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | The name of the property in the API. To find the API name for your property, use the \`Get object type\` endpoint or check the **Ontology Manager**.  |
**property_filters** | **List\[str\]** |  | \[optional\]

## Example

```python
from foundry.models import InvalidPropertyFiltersCombinationParameters

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPropertyFiltersCombinationParameters from a JSON string
invalid_property_filters_combination_parameters_instance = InvalidPropertyFiltersCombinationParameters.from_json(json)
# print the JSON string representation of the object
print(InvalidPropertyFiltersCombinationParameters.to_json())

# convert the object into a dict
invalid_property_filters_combination_parameters_dict = invalid_property_filters_combination_parameters_instance.to_dict()
# create an instance of InvalidPropertyFiltersCombinationParameters from a dict
invalid_property_filters_combination_parameters_form_dict = invalid_property_filters_combination_parameters.from_dict(invalid_property_filters_combination_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
