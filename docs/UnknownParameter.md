# UnknownParameter

The provided parameters were not found. Please look at the `knownParameters` field to see which ones are available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**UnknownParameterParameters**](UnknownParameterParameters.md) |  |

## Example

```python
from foundry.models import UnknownParameter

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownParameter from a JSON string
unknown_parameter_instance = UnknownParameter.from_json(json)
# print the JSON string representation of the object
print(UnknownParameter.to_json())

# convert the object into a dict
unknown_parameter_dict = unknown_parameter_instance.to_dict()
# create an instance of UnknownParameter from a dict
unknown_parameter_form_dict = unknown_parameter.from_dict(unknown_parameter_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
