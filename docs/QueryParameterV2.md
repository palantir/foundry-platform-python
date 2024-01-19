# QueryParameterV2

Details about a parameter of a query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | [**QueryDataType**](QueryDataType.md) |  |
**description** | **str** |  | \[optional\]

## Example

```python
from foundry.models import QueryParameterV2

# TODO update the JSON string below
json = "{}"
# create an instance of QueryParameterV2 from a JSON string
query_parameter_v2_instance = QueryParameterV2.from_json(json)
# print the JSON string representation of the object
print(QueryParameterV2.to_json())

# convert the object into a dict
query_parameter_v2_dict = query_parameter_v2_instance.to_dict()
# create an instance of QueryParameterV2 from a dict
query_parameter_v2_form_dict = query_parameter_v2.from_dict(query_parameter_v2_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
