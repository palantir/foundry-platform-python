# QueryNotFound

The query is not found, or the user does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**QueryNotFoundParameters**](QueryNotFoundParameters.md) |  |

## Example

```python
from foundry.models import QueryNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNotFound from a JSON string
query_not_found_instance = QueryNotFound.from_json(json)
# print the JSON string representation of the object
print(QueryNotFound.to_json())

# convert the object into a dict
query_not_found_dict = query_not_found_instance.to_dict()
# create an instance of QueryNotFound from a dict
query_not_found_form_dict = query_not_found.from_dict(query_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
