# DuplicateOrderBy

The requested sort order includes duplicate properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**DuplicateOrderByParameters**](DuplicateOrderByParameters.md) |  |

## Example

```python
from foundry.models import DuplicateOrderBy

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateOrderBy from a JSON string
duplicate_order_by_instance = DuplicateOrderBy.from_json(json)
# print the JSON string representation of the object
print(DuplicateOrderBy.to_json())

# convert the object into a dict
duplicate_order_by_dict = duplicate_order_by_instance.to_dict()
# create an instance of DuplicateOrderBy from a dict
duplicate_order_by_form_dict = duplicate_order_by.from_dict(duplicate_order_by_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
