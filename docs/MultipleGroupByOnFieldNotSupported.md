# MultipleGroupByOnFieldNotSupported

Aggregation cannot group by on the same field multiple times.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**MultipleGroupByOnFieldNotSupportedParameters**](MultipleGroupByOnFieldNotSupportedParameters.md) |  |

## Example

```python
from foundry.models import MultipleGroupByOnFieldNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleGroupByOnFieldNotSupported from a JSON string
multiple_group_by_on_field_not_supported_instance = MultipleGroupByOnFieldNotSupported.from_json(json)
# print the JSON string representation of the object
print(MultipleGroupByOnFieldNotSupported.to_json())

# convert the object into a dict
multiple_group_by_on_field_not_supported_dict = multiple_group_by_on_field_not_supported_instance.to_dict()
# create an instance of MultipleGroupByOnFieldNotSupported from a dict
multiple_group_by_on_field_not_supported_form_dict = multiple_group_by_on_field_not_supported.from_dict(multiple_group_by_on_field_not_supported_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
