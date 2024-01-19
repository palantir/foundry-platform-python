# DatasetNotFound

The requested dataset could not be found, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ColumnTypesNotSupportedParameters**](ColumnTypesNotSupportedParameters.md) |  |

## Example

```python
from foundry.models import DatasetNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetNotFound from a JSON string
dataset_not_found_instance = DatasetNotFound.from_json(json)
# print the JSON string representation of the object
print(DatasetNotFound.to_json())

# convert the object into a dict
dataset_not_found_dict = dataset_not_found_instance.to_dict()
# create an instance of DatasetNotFound from a dict
dataset_not_found_form_dict = dataset_not_found.from_dict(dataset_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
