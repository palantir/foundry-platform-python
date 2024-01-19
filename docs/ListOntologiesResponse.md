# ListOntologiesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List\[Ontology\]**](Ontology.md) | The list of Ontologies the user has access to. | \[optional\]

## Example

```python
from foundry.models import ListOntologiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOntologiesResponse from a JSON string
list_ontologies_response_instance = ListOntologiesResponse.from_json(json)
# print the JSON string representation of the object
print(ListOntologiesResponse.to_json())

# convert the object into a dict
list_ontologies_response_dict = list_ontologies_response_instance.to_dict()
# create an instance of ListOntologiesResponse from a dict
list_ontologies_response_form_dict = list_ontologies_response.from_dict(list_ontologies_response_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
