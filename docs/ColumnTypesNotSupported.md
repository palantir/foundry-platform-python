# ColumnTypesNotSupported

The dataset contains column types that are not supported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ColumnTypesNotSupportedParameters**](ColumnTypesNotSupportedParameters.md) |  |

## Example

```python
from foundry.models import ColumnTypesNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnTypesNotSupported from a JSON string
column_types_not_supported_instance = ColumnTypesNotSupported.from_json(json)
# print the JSON string representation of the object
print(ColumnTypesNotSupported.to_json())

# convert the object into a dict
column_types_not_supported_dict = column_types_not_supported_instance.to_dict()
# create an instance of ColumnTypesNotSupported from a dict
column_types_not_supported_form_dict = column_types_not_supported.from_dict(column_types_not_supported_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
