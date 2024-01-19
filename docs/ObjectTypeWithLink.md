# ObjectTypeWithLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_types** | [**List\[LinkTypeSideV2\]**](LinkTypeSideV2.md) |  | \[optional\]
**object_type** | [**ObjectTypeV2**](ObjectTypeV2.md) |  |

## Example

```python
from foundry.models import ObjectTypeWithLink

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectTypeWithLink from a JSON string
object_type_with_link_instance = ObjectTypeWithLink.from_json(json)
# print the JSON string representation of the object
print(ObjectTypeWithLink.to_json())

# convert the object into a dict
object_type_with_link_dict = object_type_with_link_instance.to_dict()
# create an instance of ObjectTypeWithLink from a dict
object_type_with_link_form_dict = object_type_with_link.from_dict(object_type_with_link_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
