# AggregationGroupCountExceededLimitParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups_count** | **int** |  |
**groups_limit** | **int** |  |

## Example

```python
from foundry.models import AggregationGroupCountExceededLimitParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationGroupCountExceededLimitParameters from a JSON string
aggregation_group_count_exceeded_limit_parameters_instance = AggregationGroupCountExceededLimitParameters.from_json(json)
# print the JSON string representation of the object
print(AggregationGroupCountExceededLimitParameters.to_json())

# convert the object into a dict
aggregation_group_count_exceeded_limit_parameters_dict = aggregation_group_count_exceeded_limit_parameters_instance.to_dict()
# create an instance of AggregationGroupCountExceededLimitParameters from a dict
aggregation_group_count_exceeded_limit_parameters_form_dict = aggregation_group_count_exceeded_limit_parameters.from_dict(aggregation_group_count_exceeded_limit_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
