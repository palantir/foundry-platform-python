# UnknownParameterParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_parameters** | **List\[str\]** |  | \[optional\]
**unknown_parameters** | **List\[str\]** |  | \[optional\]

## Example

```python
from foundry.models import UnknownParameterParameters

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownParameterParameters from a JSON string
unknown_parameter_parameters_instance = UnknownParameterParameters.from_json(json)
# print the JSON string representation of the object
print(UnknownParameterParameters.to_json())

# convert the object into a dict
unknown_parameter_parameters_dict = unknown_parameter_parameters_instance.to_dict()
# create an instance of UnknownParameterParameters from a dict
unknown_parameter_parameters_form_dict = unknown_parameter_parameters.from_dict(unknown_parameter_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
