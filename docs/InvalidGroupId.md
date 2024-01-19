# InvalidGroupId

The provided value for a group id must be a UUID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidGroupIdParameters**](InvalidGroupIdParameters.md) |  |

## Example

```python
from foundry.models import InvalidGroupId

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidGroupId from a JSON string
invalid_group_id_instance = InvalidGroupId.from_json(json)
# print the JSON string representation of the object
print(InvalidGroupId.to_json())

# convert the object into a dict
invalid_group_id_dict = invalid_group_id_instance.to_dict()
# create an instance of InvalidGroupId from a dict
invalid_group_id_form_dict = invalid_group_id.from_dict(invalid_group_id_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
