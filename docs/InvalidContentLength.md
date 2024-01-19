# InvalidContentLength

A `Content-Length` header is required for all uploads, but was missing or invalid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import InvalidContentLength

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidContentLength from a JSON string
invalid_content_length_instance = InvalidContentLength.from_json(json)
# print the JSON string representation of the object
print(InvalidContentLength.to_json())

# convert the object into a dict
invalid_content_length_dict = invalid_content_length_instance.to_dict()
# create an instance of InvalidContentLength from a dict
invalid_content_length_form_dict = invalid_content_length.from_dict(invalid_content_length_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
