# InvalidPageSizeParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** | The page size to use for the endpoint. |

## Example

```python
from foundry.models import InvalidPageSizeParameters

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPageSizeParameters from a JSON string
invalid_page_size_parameters_instance = InvalidPageSizeParameters.from_json(json)
# print the JSON string representation of the object
print(InvalidPageSizeParameters.to_json())

# convert the object into a dict
invalid_page_size_parameters_dict = invalid_page_size_parameters_instance.to_dict()
# create an instance of InvalidPageSizeParameters from a dict
invalid_page_size_parameters_form_dict = invalid_page_size_parameters.from_dict(invalid_page_size_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
