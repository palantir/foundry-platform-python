# LanguageModelSourceNotSupported

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**LanguageModelSourceNotSupportedParameters**](LanguageModelSourceNotSupportedParameters.md) |  |

## Example

```python
from foundry.models import LanguageModelSourceNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageModelSourceNotSupported from a JSON string
language_model_source_not_supported_instance = LanguageModelSourceNotSupported.from_json(json)
# print the JSON string representation of the object
print(LanguageModelSourceNotSupported.to_json())

# convert the object into a dict
language_model_source_not_supported_dict = language_model_source_not_supported_instance.to_dict()
# create an instance of LanguageModelSourceNotSupported from a dict
language_model_source_not_supported_form_dict = language_model_source_not_supported.from_dict(language_model_source_not_supported_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
