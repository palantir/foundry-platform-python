# ActionTypeNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | The name of the action type in the API. To find the API name for your Action Type, use the \`List action types\` endpoint or check the **Ontology Manager**.  | \[optional\]
**rid** | **str** | The unique resource identifier of an action type, useful for interacting with other Foundry APIs.  | \[optional\]

## Example

```python
from foundry.models import ActionTypeNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ActionTypeNotFoundParameters from a JSON string
action_type_not_found_parameters_instance = ActionTypeNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(ActionTypeNotFoundParameters.to_json())

# convert the object into a dict
action_type_not_found_parameters_dict = action_type_not_found_parameters_instance.to_dict()
# create an instance of ActionTypeNotFoundParameters from a dict
action_type_not_found_parameters_form_dict = action_type_not_found_parameters.from_dict(action_type_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
