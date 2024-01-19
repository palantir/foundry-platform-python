# InvalidParameterCombination

The given parameters are individually valid but cannot be used in the given combination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidParameterCombinationParameters**](InvalidParameterCombinationParameters.md) |  |

## Example

```python
from foundry.models import InvalidParameterCombination

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidParameterCombination from a JSON string
invalid_parameter_combination_instance = InvalidParameterCombination.from_json(json)
# print the JSON string representation of the object
print(InvalidParameterCombination.to_json())

# convert the object into a dict
invalid_parameter_combination_dict = invalid_parameter_combination_instance.to_dict()
# create an instance of InvalidParameterCombination from a dict
invalid_parameter_combination_form_dict = invalid_parameter_combination.from_dict(invalid_parameter_combination_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
