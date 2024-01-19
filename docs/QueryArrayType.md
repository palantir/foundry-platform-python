# QueryArrayType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_type** | [**QueryDataType**](QueryDataType.md) |  |
**type** | **str** |  |

## Example

```python
from foundry.models import QueryArrayType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryArrayType from a JSON string
query_array_type_instance = QueryArrayType.from_json(json)
# print the JSON string representation of the object
print(QueryArrayType.to_json())

# convert the object into a dict
query_array_type_dict = query_array_type_instance.to_dict()
# create an instance of QueryArrayType from a dict
query_array_type_form_dict = query_array_type.from_dict(query_array_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
