# OntologyV2

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
from foundry.models import OntologyV2

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyV2 from a JSON string
ontology_v2_instance = OntologyV2.from_json(json)
# print the JSON string representation of the object
print(OntologyV2.to_json())

# convert the object into a dict
ontology_v2_dict = ontology_v2_instance.to_dict()
# create an instance of OntologyV2 from a dict
ontology_v2_form_dict = ontology_v2.from_dict(ontology_v2_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
