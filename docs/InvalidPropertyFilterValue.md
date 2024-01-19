# InvalidPropertyFilterValue

The value of the given property filter is invalid. For instance, 2 is an invalid value for `isNull` in `properties.address.isNull=2` because the `isNull` filter expects a value of boolean type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidPropertyFilterValueParameters**](InvalidPropertyFilterValueParameters.md) |  |

## Example

```python
from foundry.models import InvalidPropertyFilterValue

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPropertyFilterValue from a JSON string
invalid_property_filter_value_instance = InvalidPropertyFilterValue.from_json(json)
# print the JSON string representation of the object
print(InvalidPropertyFilterValue.to_json())

# convert the object into a dict
invalid_property_filter_value_dict = invalid_property_filter_value_instance.to_dict()
# create an instance of InvalidPropertyFilterValue from a dict
invalid_property_filter_value_form_dict = invalid_property_filter_value.from_dict(invalid_property_filter_value_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
