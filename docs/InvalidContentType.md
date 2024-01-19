# InvalidContentType

The `Content-Type` cannot be inferred from the request content and filename. Please check your request content and filename to ensure they are compatible.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import InvalidContentType

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidContentType from a JSON string
invalid_content_type_instance = InvalidContentType.from_json(json)
# print the JSON string representation of the object
print(InvalidContentType.to_json())

# convert the object into a dict
invalid_content_type_dict = invalid_content_type_instance.to_dict()
# create an instance of InvalidContentType from a dict
invalid_content_type_form_dict = invalid_content_type.from_dict(invalid_content_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
