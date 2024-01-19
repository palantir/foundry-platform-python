# QueryStructType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List\[QueryStructField\]**](QueryStructField.md) |  | \[optional\]
**type** | **str** |  |

## Example

```python
from foundry.models import QueryStructType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryStructType from a JSON string
query_struct_type_instance = QueryStructType.from_json(json)
# print the JSON string representation of the object
print(QueryStructType.to_json())

# convert the object into a dict
query_struct_type_dict = query_struct_type_instance.to_dict()
# create an instance of QueryStructType from a dict
query_struct_type_form_dict = query_struct_type.from_dict(query_struct_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
