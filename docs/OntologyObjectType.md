# OntologyObjectType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_api_name** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**object_type_api_name** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**type** | **str** |  |

## Example

```python
from foundry.models import OntologyObjectType

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyObjectType from a JSON string
ontology_object_type_instance = OntologyObjectType.from_json(json)
# print the JSON string representation of the object
print(OntologyObjectType.to_json())

# convert the object into a dict
ontology_object_type_dict = ontology_object_type_instance.to_dict()
# create an instance of OntologyObjectType from a dict
ontology_object_type_form_dict = ontology_object_type.from_dict(ontology_object_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
