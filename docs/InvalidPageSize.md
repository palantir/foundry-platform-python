# InvalidPageSize

The provided page size was zero or negative. Page sizes must be greater than zero.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidPageSizeParameters**](InvalidPageSizeParameters.md) |  |

## Example

```python
from foundry.models import InvalidPageSize

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPageSize from a JSON string
invalid_page_size_instance = InvalidPageSize.from_json(json)
# print the JSON string representation of the object
print(InvalidPageSize.to_json())

# convert the object into a dict
invalid_page_size_dict = invalid_page_size_instance.to_dict()
# create an instance of InvalidPageSize from a dict
invalid_page_size_form_dict = invalid_page_size.from_dict(invalid_page_size_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
