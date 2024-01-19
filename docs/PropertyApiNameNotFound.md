# PropertyApiNameNotFound

A property that was required to have an API name, such as a primary key, is missing one. You can set an API name for it using the **Ontology Manager**.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**PropertyApiNameNotFoundParameters**](PropertyApiNameNotFoundParameters.md) |  |

## Example

```python
from foundry.models import PropertyApiNameNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyApiNameNotFound from a JSON string
property_api_name_not_found_instance = PropertyApiNameNotFound.from_json(json)
# print the JSON string representation of the object
print(PropertyApiNameNotFound.to_json())

# convert the object into a dict
property_api_name_not_found_dict = property_api_name_not_found_instance.to_dict()
# create an instance of PropertyApiNameNotFound from a dict
property_api_name_not_found_form_dict = property_api_name_not_found.from_dict(property_api_name_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
