# ApplyActionFailed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import ApplyActionFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyActionFailed from a JSON string
apply_action_failed_instance = ApplyActionFailed.from_json(json)
# print the JSON string representation of the object
print(ApplyActionFailed.to_json())

# convert the object into a dict
apply_action_failed_dict = apply_action_failed_instance.to_dict()
# create an instance of ApplyActionFailed from a dict
apply_action_failed_form_dict = apply_action_failed.from_dict(apply_action_failed_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
