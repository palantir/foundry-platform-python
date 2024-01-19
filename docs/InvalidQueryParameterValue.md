# InvalidQueryParameterValue

The value of the given parameter is invalid. See the documentation of `DataValue` for details on how parameters are represented.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidQueryParameterValueParameters**](InvalidQueryParameterValueParameters.md) |  |

## Example

```python
from foundry.models import InvalidQueryParameterValue

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidQueryParameterValue from a JSON string
invalid_query_parameter_value_instance = InvalidQueryParameterValue.from_json(json)
# print the JSON string representation of the object
print(InvalidQueryParameterValue.to_json())

# convert the object into a dict
invalid_query_parameter_value_dict = invalid_query_parameter_value_instance.to_dict()
# create an instance of InvalidQueryParameterValue from a dict
invalid_query_parameter_value_form_dict = invalid_query_parameter_value.from_dict(invalid_query_parameter_value_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
