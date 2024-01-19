# AttachmentNotFound

The requested attachment is not found, or the client token does not have access to it.  Attachments that are not attached to any objects are deleted after two weeks. Attachments that have not been attached to an object can only be viewed by the user who uploaded them. Attachments that have been attached to an object can be viewed by users who can view the object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**AttachmentNotFoundParameters**](AttachmentNotFoundParameters.md) |  |

## Example

```python
from foundry.models import AttachmentNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentNotFound from a JSON string
attachment_not_found_instance = AttachmentNotFound.from_json(json)
# print the JSON string representation of the object
print(AttachmentNotFound.to_json())

# convert the object into a dict
attachment_not_found_dict = attachment_not_found_instance.to_dict()
# create an instance of AttachmentNotFound from a dict
attachment_not_found_form_dict = attachment_not_found.from_dict(attachment_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
