# InvalidDurationGroupByValue

Duration groupBy value is invalid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import InvalidDurationGroupByValue

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDurationGroupByValue from a JSON string
invalid_duration_group_by_value_instance = InvalidDurationGroupByValue.from_json(json)
# print the JSON string representation of the object
print(InvalidDurationGroupByValue.to_json())

# convert the object into a dict
invalid_duration_group_by_value_dict = invalid_duration_group_by_value_instance.to_dict()
# create an instance of InvalidDurationGroupByValue from a dict
invalid_duration_group_by_value_form_dict = invalid_duration_group_by_value.from_dict(invalid_duration_group_by_value_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
