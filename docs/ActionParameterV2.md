# ActionParameterV2

Details about a parameter of an action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | [**ActionParameterType**](ActionParameterType.md) |  |
**description** | **str** |  | \[optional\]
**required** | **bool** |  |

## Example

```python
from foundry.models import ActionParameterV2

# TODO update the JSON string below
json = "{}"
# create an instance of ActionParameterV2 from a JSON string
action_parameter_v2_instance = ActionParameterV2.from_json(json)
# print the JSON string representation of the object
print(ActionParameterV2.to_json())

# convert the object into a dict
action_parameter_v2_dict = action_parameter_v2_instance.to_dict()
# create an instance of ActionParameterV2 from a dict
action_parameter_v2_form_dict = action_parameter_v2.from_dict(action_parameter_v2_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
