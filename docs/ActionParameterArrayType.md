# ActionParameterArrayType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_type** | [**ActionParameterType**](ActionParameterType.md) |  |
**type** | **str** |  |

## Example

```python
from foundry.models import ActionParameterArrayType

# TODO update the JSON string below
json = "{}"
# create an instance of ActionParameterArrayType from a JSON string
action_parameter_array_type_instance = ActionParameterArrayType.from_json(json)
# print the JSON string representation of the object
print(ActionParameterArrayType.to_json())

# convert the object into a dict
action_parameter_array_type_dict = action_parameter_array_type_instance.to_dict()
# create an instance of ActionParameterArrayType from a dict
action_parameter_array_type_form_dict = action_parameter_array_type.from_dict(action_parameter_array_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
