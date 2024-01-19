# ActionValidationFailedParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | The name of the action type in the API. To find the API name for your Action Type, use the \`List action types\` endpoint or check the **Ontology Manager**.  |

## Example

```python
from foundry.models import ActionValidationFailedParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ActionValidationFailedParameters from a JSON string
action_validation_failed_parameters_instance = ActionValidationFailedParameters.from_json(json)
# print the JSON string representation of the object
print(ActionValidationFailedParameters.to_json())

# convert the object into a dict
action_validation_failed_parameters_dict = action_validation_failed_parameters_instance.to_dict()
# create an instance of ActionValidationFailedParameters from a dict
action_validation_failed_parameters_form_dict = action_validation_failed_parameters.from_dict(action_validation_failed_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
