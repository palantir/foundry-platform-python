# QueryStructField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_type** | [**QueryDataType**](QueryDataType.md) |  |
**name** | **str** | The name of a field in a \`Struct\`.  |

## Example

```python
from foundry.models import QueryStructField

# TODO update the JSON string below
json = "{}"
# create an instance of QueryStructField from a JSON string
query_struct_field_instance = QueryStructField.from_json(json)
# print the JSON string representation of the object
print(QueryStructField.to_json())

# convert the object into a dict
query_struct_field_dict = query_struct_field_instance.to_dict()
# create an instance of QueryStructField from a dict
query_struct_field_form_dict = query_struct_field.from_dict(query_struct_field_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
