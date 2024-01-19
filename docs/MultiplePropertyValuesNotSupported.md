# MultiplePropertyValuesNotSupported

One of the requested property filters does not support multiple values. Please include only a single value for it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**MultiplePropertyValuesNotSupportedParameters**](MultiplePropertyValuesNotSupportedParameters.md) |  |

## Example

```python
from foundry.models import MultiplePropertyValuesNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of MultiplePropertyValuesNotSupported from a JSON string
multiple_property_values_not_supported_instance = MultiplePropertyValuesNotSupported.from_json(json)
# print the JSON string representation of the object
print(MultiplePropertyValuesNotSupported.to_json())

# convert the object into a dict
multiple_property_values_not_supported_dict = multiple_property_values_not_supported_instance.to_dict()
# create an instance of MultiplePropertyValuesNotSupported from a dict
multiple_property_values_not_supported_form_dict = multiple_property_values_not_supported.from_dict(multiple_property_values_not_supported_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
