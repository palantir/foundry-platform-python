# InvalidFields

TBD

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidFieldsParameters**](InvalidFieldsParameters.md) |  |

## Example

```python
from foundry.models import InvalidFields

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidFields from a JSON string
invalid_fields_instance = InvalidFields.from_json(json)
# print the JSON string representation of the object
print(InvalidFields.to_json())

# convert the object into a dict
invalid_fields_dict = invalid_fields_instance.to_dict()
# create an instance of InvalidFields from a dict
invalid_fields_form_dict = invalid_fields.from_dict(invalid_fields_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
