# InvalidUserId

The provided value for a user id must be a UUID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidUserIdParameters**](InvalidUserIdParameters.md) |  |

## Example

```python
from foundry.models import InvalidUserId

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidUserId from a JSON string
invalid_user_id_instance = InvalidUserId.from_json(json)
# print the JSON string representation of the object
print(InvalidUserId.to_json())

# convert the object into a dict
invalid_user_id_dict = invalid_user_id_instance.to_dict()
# create an instance of InvalidUserId from a dict
invalid_user_id_form_dict = invalid_user_id.from_dict(invalid_user_id_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
