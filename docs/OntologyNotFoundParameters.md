# OntologyNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** |  | \[optional\]
**ontology_rid** | **str** | The unique Resource Identifier (RID) of the Ontology. To look up your Ontology RID, please use the \`List ontologies\` endpoint or check the **Ontology Manager**.  | \[optional\]

## Example

```python
from foundry.models import OntologyNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyNotFoundParameters from a JSON string
ontology_not_found_parameters_instance = OntologyNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(OntologyNotFoundParameters.to_json())

# convert the object into a dict
ontology_not_found_parameters_dict = ontology_not_found_parameters_instance.to_dict()
# create an instance of OntologyNotFoundParameters from a dict
ontology_not_found_parameters_form_dict = ontology_not_found_parameters.from_dict(ontology_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
