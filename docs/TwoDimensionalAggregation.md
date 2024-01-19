# TwoDimensionalAggregation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_type** | [**QueryAggregationKeyType**](QueryAggregationKeyType.md) |  |
**type** | **str** |  |
**value_type** | [**QueryAggregationValueType**](QueryAggregationValueType.md) |  |

## Example

```python
from foundry.models import TwoDimensionalAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of TwoDimensionalAggregation from a JSON string
two_dimensional_aggregation_instance = TwoDimensionalAggregation.from_json(json)
# print the JSON string representation of the object
print(TwoDimensionalAggregation.to_json())

# convert the object into a dict
two_dimensional_aggregation_dict = two_dimensional_aggregation_instance.to_dict()
# create an instance of TwoDimensionalAggregation from a dict
two_dimensional_aggregation_form_dict = two_dimensional_aggregation.from_dict(two_dimensional_aggregation_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
