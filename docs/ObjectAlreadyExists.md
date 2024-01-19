# ObjectAlreadyExists

The object the user is attempting to create already exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import ObjectAlreadyExists

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectAlreadyExists from a JSON string
object_already_exists_instance = ObjectAlreadyExists.from_json(json)
# print the JSON string representation of the object
print(ObjectAlreadyExists.to_json())

# convert the object into a dict
object_already_exists_dict = object_already_exists_instance.to_dict()
# create an instance of ObjectAlreadyExists from a dict
object_already_exists_form_dict = object_already_exists.from_dict(object_already_exists_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
