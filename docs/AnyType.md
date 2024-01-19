# AnyType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |

## Example

```python
from foundry.models import AnyType

# TODO update the JSON string below
json = "{}"
# create an instance of AnyType from a JSON string
any_type_instance = AnyType.from_json(json)
# print the JSON string representation of the object
print(AnyType.to_json())

# convert the object into a dict
any_type_dict = any_type_instance.to_dict()
# create an instance of AnyType from a dict
any_type_form_dict = any_type.from_dict(any_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
