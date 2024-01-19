# MalformedPropertyFilters

At least one of requested filters are malformed. Please look at the documentation of `PropertyFilter`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**MalformedPropertyFiltersParameters**](MalformedPropertyFiltersParameters.md) |  |

## Example

```python
from foundry.models import MalformedPropertyFilters

# TODO update the JSON string below
json = "{}"
# create an instance of MalformedPropertyFilters from a JSON string
malformed_property_filters_instance = MalformedPropertyFilters.from_json(json)
# print the JSON string representation of the object
print(MalformedPropertyFilters.to_json())

# convert the object into a dict
malformed_property_filters_dict = malformed_property_filters_instance.to_dict()
# create an instance of MalformedPropertyFilters from a dict
malformed_property_filters_form_dict = malformed_property_filters.from_dict(malformed_property_filters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
