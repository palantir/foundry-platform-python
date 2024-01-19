# PropertyTypesSearchNotSupported

The search on the property types are not supported. See the `Search Objects` documentation for a list of supported search queries on different property types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**PropertyTypesSearchNotSupportedParameters**](PropertyTypesSearchNotSupportedParameters.md) |  |

## Example

```python
from foundry.models import PropertyTypesSearchNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyTypesSearchNotSupported from a JSON string
property_types_search_not_supported_instance = PropertyTypesSearchNotSupported.from_json(json)
# print the JSON string representation of the object
print(PropertyTypesSearchNotSupported.to_json())

# convert the object into a dict
property_types_search_not_supported_dict = property_types_search_not_supported_instance.to_dict()
# create an instance of PropertyTypesSearchNotSupported from a dict
property_types_search_not_supported_form_dict = property_types_search_not_supported.from_dict(property_types_search_not_supported_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
