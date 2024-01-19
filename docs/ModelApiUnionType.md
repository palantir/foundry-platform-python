# ModelApiUnionType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |
**union_types** | [**List\[ModelApiType\]**](ModelApiType.md) |  | \[optional\]

## Example

```python
from foundry.models import ModelApiUnionType

# TODO update the JSON string below
json = "{}"
# create an instance of ModelApiUnionType from a JSON string
model_api_union_type_instance = ModelApiUnionType.from_json(json)
# print the JSON string representation of the object
print(ModelApiUnionType.to_json())

# convert the object into a dict
model_api_union_type_dict = model_api_union_type_instance.to_dict()
# create an instance of ModelApiUnionType from a dict
model_api_union_type_form_dict = model_api_union_type.from_dict(model_api_union_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
