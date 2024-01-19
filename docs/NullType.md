# NullType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |

## Example

```python
from foundry.models import NullType

# TODO update the JSON string below
json = "{}"
# create an instance of NullType from a JSON string
null_type_instance = NullType.from_json(json)
# print the JSON string representation of the object
print(NullType.to_json())

# convert the object into a dict
null_type_dict = null_type_instance.to_dict()
# create an instance of NullType from a dict
null_type_form_dict = null_type.from_dict(null_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
