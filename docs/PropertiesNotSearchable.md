# PropertiesNotSearchable

Search is not enabled on the specified properties. Please mark the properties as *Searchable* in the **Ontology Manager** to enable search on them. There may be a short delay between the time a property is marked *Searchable* and when it can be used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**PropertiesNotSearchableParameters**](PropertiesNotSearchableParameters.md) |  |

## Example

```python
from foundry.models import PropertiesNotSearchable

# TODO update the JSON string below
json = "{}"
# create an instance of PropertiesNotSearchable from a JSON string
properties_not_searchable_instance = PropertiesNotSearchable.from_json(json)
# print the JSON string representation of the object
print(PropertiesNotSearchable.to_json())

# convert the object into a dict
properties_not_searchable_dict = properties_not_searchable_instance.to_dict()
# create an instance of PropertiesNotSearchable from a dict
properties_not_searchable_form_dict = properties_not_searchable.from_dict(properties_not_searchable_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
