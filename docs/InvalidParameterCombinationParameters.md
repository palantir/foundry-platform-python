# InvalidParameterCombinationParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provided_parameters** | **List\[str\]** |  | \[optional\]
**valid_combinations** | **List\[List\[str\]\]** |  | \[optional\]

## Example

```python
from foundry.models import InvalidParameterCombinationParameters

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidParameterCombinationParameters from a JSON string
invalid_parameter_combination_parameters_instance = InvalidParameterCombinationParameters.from_json(json)
# print the JSON string representation of the object
print(InvalidParameterCombinationParameters.to_json())

# convert the object into a dict
invalid_parameter_combination_parameters_dict = invalid_parameter_combination_parameters_instance.to_dict()
# create an instance of InvalidParameterCombinationParameters from a dict
invalid_parameter_combination_parameters_form_dict = invalid_parameter_combination_parameters.from_dict(invalid_parameter_combination_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
