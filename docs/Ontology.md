# Ontology

Metadata about an Ontology.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** |  |
**description** | **str** |  |
**display_name** | **str** | The display name of the entity. |
**rid** | **str** | The unique Resource Identifier (RID) of the Ontology. To look up your Ontology RID, please use the \`List ontologies\` endpoint or check the **Ontology Manager**.  |

## Example

```python
from foundry.models import Ontology

# TODO update the JSON string below
json = "{}"
# create an instance of Ontology from a JSON string
ontology_instance = Ontology.from_json(json)
# print the JSON string representation of the object
print(Ontology.to_json())

# convert the object into a dict
ontology_dict = ontology_instance.to_dict()
# create an instance of Ontology from a dict
ontology_form_dict = ontology.from_dict(ontology_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
