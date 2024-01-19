# ActionType

Represents an action type in the Ontology.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** | The name of the action type in the API. To find the API name for your Action Type, use the \`List action types\` endpoint or check the **Ontology Manager**.  |
**description** | **str** |  | \[optional\]
**display_name** | **str** | The display name of the entity. | \[optional\]
**operations** | [**List\[LogicRule\]**](LogicRule.md) |  | \[optional\]
**parameters** | [**Dict\[str, Parameter\]**](Parameter.md) |  | \[optional\]
**rid** | **str** | The unique resource identifier of an action type, useful for interacting with other Foundry APIs.  |
**status** | [**ReleaseStatus**](ReleaseStatus.md) |  |

## Example

```python
from foundry.models import ActionType

# TODO update the JSON string below
json = "{}"
# create an instance of ActionType from a JSON string
action_type_instance = ActionType.from_json(json)
# print the JSON string representation of the object
print(ActionType.to_json())

# convert the object into a dict
action_type_dict = action_type_instance.to_dict()
# create an instance of ActionType from a dict
action_type_form_dict = action_type.from_dict(action_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
