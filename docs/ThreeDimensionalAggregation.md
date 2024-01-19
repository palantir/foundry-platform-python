# ThreeDimensionalAggregation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_type** | [**QueryAggregationKeyType**](QueryAggregationKeyType.md) |  |
**type** | **str** |  |
**value_type** | [**TwoDimensionalAggregation**](TwoDimensionalAggregation.md) |  |

## Example

```python
from foundry.models import ThreeDimensionalAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of ThreeDimensionalAggregation from a JSON string
three_dimensional_aggregation_instance = ThreeDimensionalAggregation.from_json(json)
# print the JSON string representation of the object
print(ThreeDimensionalAggregation.to_json())

# convert the object into a dict
three_dimensional_aggregation_dict = three_dimensional_aggregation_instance.to_dict()
# create an instance of ThreeDimensionalAggregation from a dict
three_dimensional_aggregation_form_dict = three_dimensional_aggregation.from_dict(three_dimensional_aggregation_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
