# PropertyBaseTypeNotSupported

The type of the requested property is not currently supported by this API. If you need support for this, please reach out to Palantir Support.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidAggregationRangePropertyTypeParameters**](InvalidAggregationRangePropertyTypeParameters.md) |  |

## Example

```python
from foundry.models import PropertyBaseTypeNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyBaseTypeNotSupported from a JSON string
property_base_type_not_supported_instance = PropertyBaseTypeNotSupported.from_json(json)
# print the JSON string representation of the object
print(PropertyBaseTypeNotSupported.to_json())

# convert the object into a dict
property_base_type_not_supported_dict = property_base_type_not_supported_instance.to_dict()
# create an instance of PropertyBaseTypeNotSupported from a dict
property_base_type_not_supported_form_dict = property_base_type_not_supported.from_dict(property_base_type_not_supported_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
