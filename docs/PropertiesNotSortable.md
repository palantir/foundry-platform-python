# PropertiesNotSortable

Results could not be ordered by the requested properties. Please mark the properties as *Searchable* and *Sortable* in the **Ontology Manager** to enable their use in `orderBy` parameters. There may be a short delay between the time a property is set to *Searchable* and *Sortable* and when it can be used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**DuplicateOrderByParameters**](DuplicateOrderByParameters.md) |  |

## Example

```python
from foundry.models import PropertiesNotSortable

# TODO update the JSON string below
json = "{}"
# create an instance of PropertiesNotSortable from a JSON string
properties_not_sortable_instance = PropertiesNotSortable.from_json(json)
# print the JSON string representation of the object
print(PropertiesNotSortable.to_json())

# convert the object into a dict
properties_not_sortable_dict = properties_not_sortable_instance.to_dict()
# create an instance of PropertiesNotSortable from a dict
properties_not_sortable_form_dict = properties_not_sortable.from_dict(properties_not_sortable_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
