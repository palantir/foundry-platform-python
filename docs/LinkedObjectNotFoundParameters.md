# LinkedObjectNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_type** | **str** | The name of the link type in the API. To find the API name for your Link Type, check the **Ontology Manager** application.  |
**linked_object_primary_key** | **Dict\[str, object\]** |  | \[optional\]
**linked_object_type** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |

## Example

```python
from foundry.models import LinkedObjectNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedObjectNotFoundParameters from a JSON string
linked_object_not_found_parameters_instance = LinkedObjectNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(LinkedObjectNotFoundParameters.to_json())

# convert the object into a dict
linked_object_not_found_parameters_dict = linked_object_not_found_parameters_instance.to_dict()
# create an instance of LinkedObjectNotFoundParameters from a dict
linked_object_not_found_parameters_form_dict = linked_object_not_found_parameters.from_dict(linked_object_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
