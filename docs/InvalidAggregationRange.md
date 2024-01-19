# InvalidAggregationRange

Aggregation range should include one lt or lte and one gt or gte.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import InvalidAggregationRange

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidAggregationRange from a JSON string
invalid_aggregation_range_instance = InvalidAggregationRange.from_json(json)
# print the JSON string representation of the object
print(InvalidAggregationRange.to_json())

# convert the object into a dict
invalid_aggregation_range_dict = invalid_aggregation_range_instance.to_dict()
# create an instance of InvalidAggregationRange from a dict
invalid_aggregation_range_form_dict = invalid_aggregation_range.from_dict(invalid_aggregation_range_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
