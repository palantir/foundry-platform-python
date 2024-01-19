# InvalidRangeQuery

The specified query range filter is invalid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidRangeQueryParameters**](InvalidRangeQueryParameters.md) |  |

## Example

```python
from foundry.models import InvalidRangeQuery

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidRangeQuery from a JSON string
invalid_range_query_instance = InvalidRangeQuery.from_json(json)
# print the JSON string representation of the object
print(InvalidRangeQuery.to_json())

# convert the object into a dict
invalid_range_query_dict = invalid_range_query_instance.to_dict()
# create an instance of InvalidRangeQuery from a dict
invalid_range_query_form_dict = invalid_range_query.from_dict(invalid_range_query_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
