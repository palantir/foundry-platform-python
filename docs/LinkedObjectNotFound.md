# LinkedObjectNotFound

The linked object with the given primary key is not found, or the user does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**LinkedObjectNotFoundParameters**](LinkedObjectNotFoundParameters.md) |  |

## Example

```python
from foundry.models import LinkedObjectNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedObjectNotFound from a JSON string
linked_object_not_found_instance = LinkedObjectNotFound.from_json(json)
# print the JSON string representation of the object
print(LinkedObjectNotFound.to_json())

# convert the object into a dict
linked_object_not_found_dict = linked_object_not_found_instance.to_dict()
# create an instance of LinkedObjectNotFound from a dict
linked_object_not_found_form_dict = linked_object_not_found.from_dict(linked_object_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
