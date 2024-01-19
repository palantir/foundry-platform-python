# OntologyObjectSetType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_api_name** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  | \[optional\]
**object_type_api_name** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  | \[optional\]
**type** | **str** |  |

## Example

```python
from foundry.models import OntologyObjectSetType

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyObjectSetType from a JSON string
ontology_object_set_type_instance = OntologyObjectSetType.from_json(json)
# print the JSON string representation of the object
print(OntologyObjectSetType.to_json())

# convert the object into a dict
ontology_object_set_type_dict = ontology_object_set_type_instance.to_dict()
# create an instance of OntologyObjectSetType from a dict
ontology_object_set_type_form_dict = ontology_object_set_type.from_dict(ontology_object_set_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
