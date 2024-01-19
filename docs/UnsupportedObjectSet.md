# UnsupportedObjectSet

The requested object set is not supported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import UnsupportedObjectSet

# TODO update the JSON string below
json = "{}"
# create an instance of UnsupportedObjectSet from a JSON string
unsupported_object_set_instance = UnsupportedObjectSet.from_json(json)
# print the JSON string representation of the object
print(UnsupportedObjectSet.to_json())

# convert the object into a dict
unsupported_object_set_dict = unsupported_object_set_instance.to_dict()
# create an instance of UnsupportedObjectSet from a dict
unsupported_object_set_form_dict = unsupported_object_set.from_dict(unsupported_object_set_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
