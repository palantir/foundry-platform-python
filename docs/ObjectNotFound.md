# ObjectNotFound

The requested object is not found, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ObjectNotFoundParameters**](ObjectNotFoundParameters.md) |  |

## Example

```python
from foundry.models import ObjectNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectNotFound from a JSON string
object_not_found_instance = ObjectNotFound.from_json(json)
# print the JSON string representation of the object
print(ObjectNotFound.to_json())

# convert the object into a dict
object_not_found_dict = object_not_found_instance.to_dict()
# create an instance of ObjectNotFound from a dict
object_not_found_form_dict = object_not_found.from_dict(object_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
