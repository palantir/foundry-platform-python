# InvalidSortOrder

The requested sort order of one or more properties is invalid. Valid sort orders are 'asc' or 'desc'. Sort order can also be omitted, and defaults to 'asc'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidSortOrderParameters**](InvalidSortOrderParameters.md) |  |

## Example

```python
from foundry.models import InvalidSortOrder

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidSortOrder from a JSON string
invalid_sort_order_instance = InvalidSortOrder.from_json(json)
# print the JSON string representation of the object
print(InvalidSortOrder.to_json())

# convert the object into a dict
invalid_sort_order_dict = invalid_sort_order_instance.to_dict()
# create an instance of InvalidSortOrder from a dict
invalid_sort_order_form_dict = invalid_sort_order.from_dict(invalid_sort_order_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
