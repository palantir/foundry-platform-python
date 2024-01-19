# ActionTypeV2

Represents an action type in the Ontology.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** | The name of the action type in the API. To find the API name for your Action Type, use the \`List action types\` endpoint or check the **Ontology Manager**.  |
**description** | **str** |  | \[optional\]
**display_name** | **str** | The display name of the entity. | \[optional\]
**operations** | [**List\[LogicRule\]**](LogicRule.md) |  | \[optional\]
**parameters** | [**Dict\[str, ActionParameterV2\]**](ActionParameterV2.md) |  | \[optional\]
**rid** | **str** | The unique resource identifier of an action type, useful for interacting with other Foundry APIs.  |
**status** | [**ReleaseStatus**](ReleaseStatus.md) |  |

## Example

```python
from foundry.models import ActionTypeV2

# TODO update the JSON string below
json = "{}"
# create an instance of ActionTypeV2 from a JSON string
action_type_v2_instance = ActionTypeV2.from_json(json)
# print the JSON string representation of the object
print(ActionTypeV2.to_json())

# convert the object into a dict
action_type_v2_dict = action_type_v2_instance.to_dict()
# create an instance of ActionTypeV2 from a dict
action_type_v2_form_dict = action_type_v2.from_dict(action_type_v2_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
