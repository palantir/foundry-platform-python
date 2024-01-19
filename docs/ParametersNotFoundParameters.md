# ParametersNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | The name of the action type in the API. To find the API name for your Action Type, use the \`List action types\` endpoint or check the **Ontology Manager**.  |
**configured_parameter_ids** | **List\[str\]** |  | \[optional\]
**unknown_parameter_ids** | **List\[str\]** |  | \[optional\]

## Example

```python
from foundry.models import ParametersNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ParametersNotFoundParameters from a JSON string
parameters_not_found_parameters_instance = ParametersNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(ParametersNotFoundParameters.to_json())

# convert the object into a dict
parameters_not_found_parameters_dict = parameters_not_found_parameters_instance.to_dict()
# create an instance of ParametersNotFoundParameters from a dict
parameters_not_found_parameters_form_dict = parameters_not_found_parameters.from_dict(parameters_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
