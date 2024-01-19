# LinkTypeNotFound

The link type is not found, or the user does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**LinkTypeNotFoundParameters**](LinkTypeNotFoundParameters.md) |  |

## Example

```python
from foundry.models import LinkTypeNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of LinkTypeNotFound from a JSON string
link_type_not_found_instance = LinkTypeNotFound.from_json(json)
# print the JSON string representation of the object
print(LinkTypeNotFound.to_json())

# convert the object into a dict
link_type_not_found_dict = link_type_not_found_instance.to_dict()
# create an instance of LinkTypeNotFound from a dict
link_type_not_found_form_dict = link_type_not_found.from_dict(link_type_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
