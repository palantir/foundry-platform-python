# AggregationGroupCountExceededLimit

The number of groups in the aggregations grouping exceeded the allowed limit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**AggregationGroupCountExceededLimitParameters**](AggregationGroupCountExceededLimitParameters.md) |  |

## Example

```python
from foundry.models import AggregationGroupCountExceededLimit

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationGroupCountExceededLimit from a JSON string
aggregation_group_count_exceeded_limit_instance = AggregationGroupCountExceededLimit.from_json(json)
# print the JSON string representation of the object
print(AggregationGroupCountExceededLimit.to_json())

# convert the object into a dict
aggregation_group_count_exceeded_limit_dict = aggregation_group_count_exceeded_limit_instance.to_dict()
# create an instance of AggregationGroupCountExceededLimit from a dict
aggregation_group_count_exceeded_limit_form_dict = aggregation_group_count_exceeded_limit.from_dict(aggregation_group_count_exceeded_limit_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
