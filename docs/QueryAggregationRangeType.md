# QueryAggregationRangeType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_type** | [**QueryAggregationRangeSubType**](QueryAggregationRangeSubType.md) |  |
**type** | **str** |  |

## Example

```python
from foundry.models import QueryAggregationRangeType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAggregationRangeType from a JSON string
query_aggregation_range_type_instance = QueryAggregationRangeType.from_json(json)
# print the JSON string representation of the object
print(QueryAggregationRangeType.to_json())

# convert the object into a dict
query_aggregation_range_type_dict = query_aggregation_range_type_instance.to_dict()
# create an instance of QueryAggregationRangeType from a dict
query_aggregation_range_type_form_dict = query_aggregation_range_type.from_dict(query_aggregation_range_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
