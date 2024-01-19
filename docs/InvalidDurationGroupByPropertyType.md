# InvalidDurationGroupByPropertyType

Invalid property type for duration groupBy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidAggregationRangePropertyTypeParameters**](InvalidAggregationRangePropertyTypeParameters.md) |  |

## Example

```python
from foundry.models import InvalidDurationGroupByPropertyType

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDurationGroupByPropertyType from a JSON string
invalid_duration_group_by_property_type_instance = InvalidDurationGroupByPropertyType.from_json(json)
# print the JSON string representation of the object
print(InvalidDurationGroupByPropertyType.to_json())

# convert the object into a dict
invalid_duration_group_by_property_type_dict = invalid_duration_group_by_property_type_instance.to_dict()
# create an instance of InvalidDurationGroupByPropertyType from a dict
invalid_duration_group_by_property_type_form_dict = invalid_duration_group_by_property_type.from_dict(invalid_duration_group_by_property_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
