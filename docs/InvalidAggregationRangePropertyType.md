# InvalidAggregationRangePropertyType

Range group by is not supported by property type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidAggregationRangePropertyTypeParameters**](InvalidAggregationRangePropertyTypeParameters.md) |  |

## Example

```python
from foundry.models import InvalidAggregationRangePropertyType

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidAggregationRangePropertyType from a JSON string
invalid_aggregation_range_property_type_instance = InvalidAggregationRangePropertyType.from_json(json)
# print the JSON string representation of the object
print(InvalidAggregationRangePropertyType.to_json())

# convert the object into a dict
invalid_aggregation_range_property_type_dict = invalid_aggregation_range_property_type_instance.to_dict()
# create an instance of InvalidAggregationRangePropertyType from a dict
invalid_aggregation_range_property_type_form_dict = invalid_aggregation_range_property_type.from_dict(invalid_aggregation_range_property_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
