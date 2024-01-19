# InvalidPropertyType

The given property type is not of the expected type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidPropertyTypeParameters**](InvalidPropertyTypeParameters.md) |  |

## Example

```python
from foundry.models import InvalidPropertyType

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPropertyType from a JSON string
invalid_property_type_instance = InvalidPropertyType.from_json(json)
# print the JSON string representation of the object
print(InvalidPropertyType.to_json())

# convert the object into a dict
invalid_property_type_dict = invalid_property_type_instance.to_dict()
# create an instance of InvalidPropertyType from a dict
invalid_property_type_form_dict = invalid_property_type.from_dict(invalid_property_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
