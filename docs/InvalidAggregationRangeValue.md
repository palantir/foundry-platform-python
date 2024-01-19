# InvalidAggregationRangeValue

Aggregation value does not conform to the expected underlying type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidAggregationRangePropertyTypeParameters**](InvalidAggregationRangePropertyTypeParameters.md) |  |

## Example

```python
from foundry.models import InvalidAggregationRangeValue

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidAggregationRangeValue from a JSON string
invalid_aggregation_range_value_instance = InvalidAggregationRangeValue.from_json(json)
# print the JSON string representation of the object
print(InvalidAggregationRangeValue.to_json())

# convert the object into a dict
invalid_aggregation_range_value_dict = invalid_aggregation_range_value_instance.to_dict()
# create an instance of InvalidAggregationRangeValue from a dict
invalid_aggregation_range_value_form_dict = invalid_aggregation_range_value.from_dict(invalid_aggregation_range_value_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
