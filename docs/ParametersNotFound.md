# ParametersNotFound

The provided parameter ID was not found for the action. Please look at the `configuredParameterIds` field to see which ones are available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ParametersNotFoundParameters**](ParametersNotFoundParameters.md) |  |

## Example

```python
from foundry.models import ParametersNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ParametersNotFound from a JSON string
parameters_not_found_instance = ParametersNotFound.from_json(json)
# print the JSON string representation of the object
print(ParametersNotFound.to_json())

# convert the object into a dict
parameters_not_found_dict = parameters_not_found_instance.to_dict()
# create an instance of ParametersNotFound from a dict
parameters_not_found_form_dict = parameters_not_found.from_dict(parameters_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
