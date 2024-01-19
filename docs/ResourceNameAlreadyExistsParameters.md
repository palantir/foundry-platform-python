# ResourceNameAlreadyExistsParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_folder_rid** | **str** |  |
**resource_name** | **str** |  |

## Example

```python
from foundry.models import ResourceNameAlreadyExistsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceNameAlreadyExistsParameters from a JSON string
resource_name_already_exists_parameters_instance = ResourceNameAlreadyExistsParameters.from_json(json)
# print the JSON string representation of the object
print(ResourceNameAlreadyExistsParameters.to_json())

# convert the object into a dict
resource_name_already_exists_parameters_dict = resource_name_already_exists_parameters_instance.to_dict()
# create an instance of ResourceNameAlreadyExistsParameters from a dict
resource_name_already_exists_parameters_form_dict = resource_name_already_exists_parameters.from_dict(resource_name_already_exists_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
