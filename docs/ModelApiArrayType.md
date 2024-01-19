# ModelApiArrayType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_type** | [**ModelApiType**](ModelApiType.md) |  |
**type** | **str** |  |

## Example

```python
from foundry.models import ModelApiArrayType

# TODO update the JSON string below
json = "{}"
# create an instance of ModelApiArrayType from a JSON string
model_api_array_type_instance = ModelApiArrayType.from_json(json)
# print the JSON string representation of the object
print(ModelApiArrayType.to_json())

# convert the object into a dict
model_api_array_type_dict = model_api_array_type_instance.to_dict()
# create an instance of ModelApiArrayType from a dict
model_api_array_type_form_dict = model_api_array_type.from_dict(model_api_array_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
