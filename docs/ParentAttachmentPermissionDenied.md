# ParentAttachmentPermissionDenied

The user does not have permission to parent attachments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import ParentAttachmentPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of ParentAttachmentPermissionDenied from a JSON string
parent_attachment_permission_denied_instance = ParentAttachmentPermissionDenied.from_json(json)
# print the JSON string representation of the object
print(ParentAttachmentPermissionDenied.to_json())

# convert the object into a dict
parent_attachment_permission_denied_dict = parent_attachment_permission_denied_instance.to_dict()
# create an instance of ParentAttachmentPermissionDenied from a dict
parent_attachment_permission_denied_form_dict = parent_attachment_permission_denied.from_dict(parent_attachment_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
