# ModelApiDataType

An object definition representing an input or an output type for the deployment API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of a field.  | \[optional\]
**property_type** | [**ModelApiType**](ModelApiType.md) |  | \[optional\]
**required** | **bool** |  | \[optional\]

## Example

```python
from foundry.models import ModelApiDataType

# TODO update the JSON string below
json = "{}"
# create an instance of ModelApiDataType from a JSON string
model_api_data_type_instance = ModelApiDataType.from_json(json)
# print the JSON string representation of the object
print(ModelApiDataType.to_json())

# convert the object into a dict
model_api_data_type_dict = model_api_data_type_instance.to_dict()
# create an instance of ModelApiDataType from a dict
model_api_data_type_form_dict = model_api_data_type.from_dict(model_api_data_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
