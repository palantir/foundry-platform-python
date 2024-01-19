# QueryTimeExceededLimit

Time limits were exceeded for the `Query` execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**FunctionExecutionFailedParameters**](FunctionExecutionFailedParameters.md) |  |

## Example

```python
from foundry.models import QueryTimeExceededLimit

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTimeExceededLimit from a JSON string
query_time_exceeded_limit_instance = QueryTimeExceededLimit.from_json(json)
# print the JSON string representation of the object
print(QueryTimeExceededLimit.to_json())

# convert the object into a dict
query_time_exceeded_limit_dict = query_time_exceeded_limit_instance.to_dict()
# create an instance of QueryTimeExceededLimit from a dict
query_time_exceeded_limit_form_dict = query_time_exceeded_limit.from_dict(query_time_exceeded_limit_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
