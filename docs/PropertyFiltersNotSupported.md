# PropertyFiltersNotSupported

At least one of the requested property filters are not supported. See the documentation of `PropertyFilter` for a list of supported property filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidPropertyFiltersCombinationParameters**](InvalidPropertyFiltersCombinationParameters.md) |  |

## Example

```python
from foundry.models import PropertyFiltersNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyFiltersNotSupported from a JSON string
property_filters_not_supported_instance = PropertyFiltersNotSupported.from_json(json)
# print the JSON string representation of the object
print(PropertyFiltersNotSupported.to_json())

# convert the object into a dict
property_filters_not_supported_dict = property_filters_not_supported_instance.to_dict()
# create an instance of PropertyFiltersNotSupported from a dict
property_filters_not_supported_form_dict = property_filters_not_supported.from_dict(property_filters_not_supported_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
