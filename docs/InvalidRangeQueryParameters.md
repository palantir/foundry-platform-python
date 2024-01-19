# InvalidRangeQueryParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** |  |
**gt** | **object** | Greater than | \[optional\]
**gte** | **object** | Greater than or equal | \[optional\]
**lt** | **object** | Less than | \[optional\]
**lte** | **object** | Less than or equal | \[optional\]

## Example

```python
from foundry.models import InvalidRangeQueryParameters

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidRangeQueryParameters from a JSON string
invalid_range_query_parameters_instance = InvalidRangeQueryParameters.from_json(json)
# print the JSON string representation of the object
print(InvalidRangeQueryParameters.to_json())

# convert the object into a dict
invalid_range_query_parameters_dict = invalid_range_query_parameters_instance.to_dict()
# create an instance of InvalidRangeQueryParameters from a dict
invalid_range_query_parameters_form_dict = invalid_range_query_parameters.from_dict(invalid_range_query_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
