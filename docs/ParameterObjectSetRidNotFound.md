# ParameterObjectSetRidNotFound

The parameter object set RID is not found, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ParameterObjectSetRidNotFoundParameters**](ParameterObjectSetRidNotFoundParameters.md) |  |

## Example

```python
from foundry.models import ParameterObjectSetRidNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterObjectSetRidNotFound from a JSON string
parameter_object_set_rid_not_found_instance = ParameterObjectSetRidNotFound.from_json(json)
# print the JSON string representation of the object
print(ParameterObjectSetRidNotFound.to_json())

# convert the object into a dict
parameter_object_set_rid_not_found_dict = parameter_object_set_rid_not_found_instance.to_dict()
# create an instance of ParameterObjectSetRidNotFound from a dict
parameter_object_set_rid_not_found_form_dict = parameter_object_set_rid_not_found.from_dict(parameter_object_set_rid_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
