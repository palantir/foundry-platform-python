# InvalidPropertyValue

The value of the given property is invalid. See the documentation of `PropertyValue` for details on how properties are represented.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidPropertyValueParameters**](InvalidPropertyValueParameters.md) |  |

## Example

```python
from foundry.models import InvalidPropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPropertyValue from a JSON string
invalid_property_value_instance = InvalidPropertyValue.from_json(json)
# print the JSON string representation of the object
print(InvalidPropertyValue.to_json())

# convert the object into a dict
invalid_property_value_dict = invalid_property_value_instance.to_dict()
# create an instance of InvalidPropertyValue from a dict
invalid_property_value_form_dict = invalid_property_value.from_dict(invalid_property_value_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
