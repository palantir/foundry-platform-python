# ObjectsExceededLimit

There are more objects, but they cannot be returned by this API. Only 10,000 objects are available through this API for a given request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import ObjectsExceededLimit

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectsExceededLimit from a JSON string
objects_exceeded_limit_instance = ObjectsExceededLimit.from_json(json)
# print the JSON string representation of the object
print(ObjectsExceededLimit.to_json())

# convert the object into a dict
objects_exceeded_limit_dict = objects_exceeded_limit_instance.to_dict()
# create an instance of ObjectsExceededLimit from a dict
objects_exceeded_limit_form_dict = objects_exceeded_limit.from_dict(objects_exceeded_limit_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
