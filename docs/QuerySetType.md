# QuerySetType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_type** | [**QueryDataType**](QueryDataType.md) |  |
**type** | **str** |  |

## Example

```python
from foundry.models import QuerySetType

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySetType from a JSON string
query_set_type_instance = QuerySetType.from_json(json)
# print the JSON string representation of the object
print(QuerySetType.to_json())

# convert the object into a dict
query_set_type_dict = query_set_type_instance.to_dict()
# create an instance of QuerySetType from a dict
query_set_type_form_dict = query_set_type.from_dict(query_set_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
