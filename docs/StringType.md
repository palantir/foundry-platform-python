# StringType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |

## Example

```python
from foundry.models import StringType

# TODO update the JSON string below
json = "{}"
# create an instance of StringType from a JSON string
string_type_instance = StringType.from_json(json)
# print the JSON string representation of the object
print(StringType.to_json())

# convert the object into a dict
string_type_dict = string_type_instance.to_dict()
# create an instance of StringType from a dict
string_type_form_dict = string_type.from_dict(string_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
