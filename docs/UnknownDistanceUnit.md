# UnknownDistanceUnit

An unknown distance unit was provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**UnknownDistanceUnitParameters**](UnknownDistanceUnitParameters.md) |  |

## Example

```python
from foundry.models import UnknownDistanceUnit

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownDistanceUnit from a JSON string
unknown_distance_unit_instance = UnknownDistanceUnit.from_json(json)
# print the JSON string representation of the object
print(UnknownDistanceUnit.to_json())

# convert the object into a dict
unknown_distance_unit_dict = unknown_distance_unit_instance.to_dict()
# create an instance of UnknownDistanceUnit from a dict
unknown_distance_unit_form_dict = unknown_distance_unit.from_dict(unknown_distance_unit_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
