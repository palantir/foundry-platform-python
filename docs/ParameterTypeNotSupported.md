# ParameterTypeNotSupported

The type of the requested parameter is not currently supported by this API. If you need support for this, please reach out to Palantir Support.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ParameterTypeNotSupportedParameters**](ParameterTypeNotSupportedParameters.md) |  |

## Example

```python
from foundry.models import ParameterTypeNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterTypeNotSupported from a JSON string
parameter_type_not_supported_instance = ParameterTypeNotSupported.from_json(json)
# print the JSON string representation of the object
print(ParameterTypeNotSupported.to_json())

# convert the object into a dict
parameter_type_not_supported_dict = parameter_type_not_supported_instance.to_dict()
# create an instance of ParameterTypeNotSupported from a dict
parameter_type_not_supported_form_dict = parameter_type_not_supported.from_dict(parameter_type_not_supported_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
