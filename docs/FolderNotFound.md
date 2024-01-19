# FolderNotFound

The requested folder could not be found, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**FolderNotFoundParameters**](FolderNotFoundParameters.md) |  |

## Example

```python
from foundry.models import FolderNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of FolderNotFound from a JSON string
folder_not_found_instance = FolderNotFound.from_json(json)
# print the JSON string representation of the object
print(FolderNotFound.to_json())

# convert the object into a dict
folder_not_found_dict = folder_not_found_instance.to_dict()
# create an instance of FolderNotFound from a dict
folder_not_found_form_dict = folder_not_found.from_dict(folder_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
