# ModelApiStructField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_type** | [**ModelApiType**](ModelApiType.md) |  |
**name** | **str** |  |

## Example

```python
from foundry.models import ModelApiStructField

# TODO update the JSON string below
json = "{}"
# create an instance of ModelApiStructField from a JSON string
model_api_struct_field_instance = ModelApiStructField.from_json(json)
# print the JSON string representation of the object
print(ModelApiStructField.to_json())

# convert the object into a dict
model_api_struct_field_dict = model_api_struct_field_instance.to_dict()
# create an instance of ModelApiStructField from a dict
model_api_struct_field_form_dict = model_api_struct_field.from_dict(model_api_struct_field_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
