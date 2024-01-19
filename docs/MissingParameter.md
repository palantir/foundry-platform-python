# MissingParameter

Required parameters are missing. Please look at the `parameters` field to see which required parameters are missing from the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**MissingParameterParameters**](MissingParameterParameters.md) |  |

## Example

```python
from foundry.models import MissingParameter

# TODO update the JSON string below
json = "{}"
# create an instance of MissingParameter from a JSON string
missing_parameter_instance = MissingParameter.from_json(json)
# print the JSON string representation of the object
print(MissingParameter.to_json())

# convert the object into a dict
missing_parameter_dict = missing_parameter_instance.to_dict()
# create an instance of MissingParameter from a dict
missing_parameter_form_dict = missing_parameter.from_dict(missing_parameter_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
