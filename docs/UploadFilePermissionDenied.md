# UploadFilePermissionDenied

The provided token does not have permission to upload the given file to the given dataset and transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**FileAlreadyExistsParameters**](FileAlreadyExistsParameters.md) |  |

## Example

```python
from foundry.models import UploadFilePermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of UploadFilePermissionDenied from a JSON string
upload_file_permission_denied_instance = UploadFilePermissionDenied.from_json(json)
# print the JSON string representation of the object
print(UploadFilePermissionDenied.to_json())

# convert the object into a dict
upload_file_permission_denied_dict = upload_file_permission_denied_instance.to_dict()
# create an instance of UploadFilePermissionDenied from a dict
upload_file_permission_denied_form_dict = upload_file_permission_denied.from_dict(upload_file_permission_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
