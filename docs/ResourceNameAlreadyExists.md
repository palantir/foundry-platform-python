# ResourceNameAlreadyExists

The provided resource name is already in use by another resource in the same folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ResourceNameAlreadyExistsParameters**](ResourceNameAlreadyExistsParameters.md) |  |

## Example

```python
from foundry.models import ResourceNameAlreadyExists

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceNameAlreadyExists from a JSON string
resource_name_already_exists_instance = ResourceNameAlreadyExists.from_json(json)
# print the JSON string representation of the object
print(ResourceNameAlreadyExists.to_json())

# convert the object into a dict
resource_name_already_exists_dict = resource_name_already_exists_instance.to_dict()
# create an instance of ResourceNameAlreadyExists from a dict
resource_name_already_exists_form_dict = resource_name_already_exists.from_dict(resource_name_already_exists_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
