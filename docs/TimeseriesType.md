# TimeseriesType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | [**TimeSeriesItemType**](TimeSeriesItemType.md) |  |
**type** | **str** |  |

## Example

```python
from foundry.models import TimeseriesType

# TODO update the JSON string below
json = "{}"
# create an instance of TimeseriesType from a JSON string
timeseries_type_instance = TimeseriesType.from_json(json)
# print the JSON string representation of the object
print(TimeseriesType.to_json())

# convert the object into a dict
timeseries_type_dict = timeseries_type_instance.to_dict()
# create an instance of TimeseriesType from a dict
timeseries_type_form_dict = timeseries_type.from_dict(timeseries_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
