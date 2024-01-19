# OntologyNotFound

The requested Ontology is not found, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**OntologyNotFoundParameters**](OntologyNotFoundParameters.md) |  |

## Example

```python
from foundry.models import OntologyNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyNotFound from a JSON string
ontology_not_found_instance = OntologyNotFound.from_json(json)
# print the JSON string representation of the object
print(OntologyNotFound.to_json())

# convert the object into a dict
ontology_not_found_dict = ontology_not_found_instance.to_dict()
# create an instance of OntologyNotFound from a dict
ontology_not_found_form_dict = ontology_not_found.from_dict(ontology_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
