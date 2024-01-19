# InvalidPropertyFiltersCombination

The provided filters cannot be used together.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidPropertyFiltersCombinationParameters**](InvalidPropertyFiltersCombinationParameters.md) |  |

## Example

```python
from foundry.models import InvalidPropertyFiltersCombination

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPropertyFiltersCombination from a JSON string
invalid_property_filters_combination_instance = InvalidPropertyFiltersCombination.from_json(json)
# print the JSON string representation of the object
print(InvalidPropertyFiltersCombination.to_json())

# convert the object into a dict
invalid_property_filters_combination_dict = invalid_property_filters_combination_instance.to_dict()
# create an instance of InvalidPropertyFiltersCombination from a dict
invalid_property_filters_combination_form_dict = invalid_property_filters_combination.from_dict(invalid_property_filters_combination_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
