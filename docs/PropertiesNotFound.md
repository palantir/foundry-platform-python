# PropertiesNotFound

The requested properties are not found on the object type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**PropertiesNotFoundParameters**](PropertiesNotFoundParameters.md) |  |

## Example

```python
from foundry.models import PropertiesNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of PropertiesNotFound from a JSON string
properties_not_found_instance = PropertiesNotFound.from_json(json)
# print the JSON string representation of the object
print(PropertiesNotFound.to_json())

# convert the object into a dict
properties_not_found_dict = properties_not_found_instance.to_dict()
# create an instance of PropertiesNotFound from a dict
properties_not_found_form_dict = properties_not_found.from_dict(properties_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
