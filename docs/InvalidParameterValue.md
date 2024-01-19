# InvalidParameterValue

The value of the given parameter is invalid. See the documentation of `DataValue` for details on how parameters are represented.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidParameterValueParameters**](InvalidParameterValueParameters.md) |  |

## Example

```python
from foundry.models import InvalidParameterValue

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidParameterValue from a JSON string
invalid_parameter_value_instance = InvalidParameterValue.from_json(json)
# print the JSON string representation of the object
print(InvalidParameterValue.to_json())

# convert the object into a dict
invalid_parameter_value_dict = invalid_parameter_value_instance.to_dict()
# create an instance of InvalidParameterValue from a dict
invalid_parameter_value_form_dict = invalid_parameter_value.from_dict(invalid_parameter_value_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
