# ModelApiStructType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List\[ModelApiStructField\]**](ModelApiStructField.md) |  | \[optional\]
**type** | **str** |  |

## Example

```python
from foundry.models import ModelApiStructType

# TODO update the JSON string below
json = "{}"
# create an instance of ModelApiStructType from a JSON string
model_api_struct_type_instance = ModelApiStructType.from_json(json)
# print the JSON string representation of the object
print(ModelApiStructType.to_json())

# convert the object into a dict
model_api_struct_type_dict = model_api_struct_type_instance.to_dict()
# create an instance of ModelApiStructType from a dict
model_api_struct_type_form_dict = model_api_struct_type.from_dict(model_api_struct_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
