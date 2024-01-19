# ModelApiMapType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_type** | [**ModelApiType**](ModelApiType.md) |  |
**type** | **str** |  |
**value_type** | [**ModelApiType**](ModelApiType.md) |  |

## Example

```python
from foundry.models import ModelApiMapType

# TODO update the JSON string below
json = "{}"
# create an instance of ModelApiMapType from a JSON string
model_api_map_type_instance = ModelApiMapType.from_json(json)
# print the JSON string representation of the object
print(ModelApiMapType.to_json())

# convert the object into a dict
model_api_map_type_dict = model_api_map_type_instance.to_dict()
# create an instance of ModelApiMapType from a dict
model_api_map_type_form_dict = model_api_map_type.from_dict(model_api_map_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
