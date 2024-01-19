# ParameterObjectNotFound

The parameter object reference or parameter default value is not found, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ParameterObjectNotFoundParameters**](ParameterObjectNotFoundParameters.md) |  |

## Example

```python
from foundry.models import ParameterObjectNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterObjectNotFound from a JSON string
parameter_object_not_found_instance = ParameterObjectNotFound.from_json(json)
# print the JSON string representation of the object
print(ParameterObjectNotFound.to_json())

# convert the object into a dict
parameter_object_not_found_dict = parameter_object_not_found_instance.to_dict()
# create an instance of ParameterObjectNotFound from a dict
parameter_object_not_found_form_dict = parameter_object_not_found.from_dict(parameter_object_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
