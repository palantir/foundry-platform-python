# QueryNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The name of the Query in the API.  |

## Example

```python
from foundry.models import QueryNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNotFoundParameters from a JSON string
query_not_found_parameters_instance = QueryNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(QueryNotFoundParameters.to_json())

# convert the object into a dict
query_not_found_parameters_dict = query_not_found_parameters_instance.to_dict()
# create an instance of QueryNotFoundParameters from a dict
query_not_found_parameters_form_dict = query_not_found_parameters.from_dict(query_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
