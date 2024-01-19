# AttachmentSizeExceededLimit

The file is too large to be uploaded as an attachment. The maximum attachment size is 200MB.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**AttachmentSizeExceededLimitParameters**](AttachmentSizeExceededLimitParameters.md) |  |

## Example

```python
from foundry.models import AttachmentSizeExceededLimit

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentSizeExceededLimit from a JSON string
attachment_size_exceeded_limit_instance = AttachmentSizeExceededLimit.from_json(json)
# print the JSON string representation of the object
print(AttachmentSizeExceededLimit.to_json())

# convert the object into a dict
attachment_size_exceeded_limit_dict = attachment_size_exceeded_limit_instance.to_dict()
# create an instance of AttachmentSizeExceededLimit from a dict
attachment_size_exceeded_limit_form_dict = attachment_size_exceeded_limit.from_dict(attachment_size_exceeded_limit_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
