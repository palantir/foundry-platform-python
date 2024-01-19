# UnknownDistanceUnitParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**known_units** | [**List\[DistanceUnit\]**](DistanceUnit.md) |  | \[optional\]
**unknown_unit** | **str** |  |

## Example

```python
from foundry.models import UnknownDistanceUnitParameters

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownDistanceUnitParameters from a JSON string
unknown_distance_unit_parameters_instance = UnknownDistanceUnitParameters.from_json(json)
# print the JSON string representation of the object
print(UnknownDistanceUnitParameters.to_json())

# convert the object into a dict
unknown_distance_unit_parameters_dict = unknown_distance_unit_parameters_instance.to_dict()
# create an instance of UnknownDistanceUnitParameters from a dict
unknown_distance_unit_parameters_form_dict = unknown_distance_unit_parameters.from_dict(unknown_distance_unit_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
