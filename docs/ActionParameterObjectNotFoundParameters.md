# ActionParameterObjectNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_id** | **str** | The unique identifier of the parameter. Parameters are used as inputs when an action or query is applied. Parameters can be viewed and managed in the **Ontology Manager**.  |

## Example

```python
from foundry.models import ActionParameterObjectNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ActionParameterObjectNotFoundParameters from a JSON string
action_parameter_object_not_found_parameters_instance = ActionParameterObjectNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(ActionParameterObjectNotFoundParameters.to_json())

# convert the object into a dict
action_parameter_object_not_found_parameters_dict = action_parameter_object_not_found_parameters_instance.to_dict()
# create an instance of ActionParameterObjectNotFoundParameters from a dict
action_parameter_object_not_found_parameters_form_dict = action_parameter_object_not_found_parameters.from_dict(action_parameter_object_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
