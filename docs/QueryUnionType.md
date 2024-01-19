# QueryUnionType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |
**union_types** | [**List\[QueryDataType\]**](QueryDataType.md) |  | \[optional\]

## Example

```python
from foundry.models import QueryUnionType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryUnionType from a JSON string
query_union_type_instance = QueryUnionType.from_json(json)
# print the JSON string representation of the object
print(QueryUnionType.to_json())

# convert the object into a dict
query_union_type_dict = query_union_type_instance.to_dict()
# create an instance of QueryUnionType from a dict
query_union_type_form_dict = query_union_type.from_dict(query_union_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
