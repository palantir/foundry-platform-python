# InvalidSortType

The requested sort type of one or more clauses is invalid. Valid sort types are 'p' or 'properties'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidSortTypeParameters**](InvalidSortTypeParameters.md) |  |

## Example

```python
from foundry.models import InvalidSortType

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidSortType from a JSON string
invalid_sort_type_instance = InvalidSortType.from_json(json)
# print the JSON string representation of the object
print(InvalidSortType.to_json())

# convert the object into a dict
invalid_sort_type_dict = invalid_sort_type_instance.to_dict()
# create an instance of InvalidSortType from a dict
invalid_sort_type_form_dict = invalid_sort_type.from_dict(invalid_sort_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
