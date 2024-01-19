# PropertiesNotFilterable

Results could not be filtered by the requested properties. Please mark the properties as *Searchable* and *Selectable* in the **Ontology Manager** to be able to filter on those properties. There may be a short delay between the time a property is marked *Searchable* and *Selectable* and when it can be used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**DuplicateOrderByParameters**](DuplicateOrderByParameters.md) |  |

## Example

```python
from foundry.models import PropertiesNotFilterable

# TODO update the JSON string below
json = "{}"
# create an instance of PropertiesNotFilterable from a JSON string
properties_not_filterable_instance = PropertiesNotFilterable.from_json(json)
# print the JSON string representation of the object
print(PropertiesNotFilterable.to_json())

# convert the object into a dict
properties_not_filterable_dict = properties_not_filterable_instance.to_dict()
# create an instance of PropertiesNotFilterable from a dict
properties_not_filterable_form_dict = properties_not_filterable.from_dict(properties_not_filterable_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
