# ListOntologiesV2Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List\[OntologyV2\]**](OntologyV2.md) | The list of Ontologies the user has access to. | \[optional\]

## Example

```python
from foundry.models import ListOntologiesV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListOntologiesV2Response from a JSON string
list_ontologies_v2_response_instance = ListOntologiesV2Response.from_json(json)
# print the JSON string representation of the object
print(ListOntologiesV2Response.to_json())

# convert the object into a dict
list_ontologies_v2_response_dict = list_ontologies_v2_response_instance.to_dict()
# create an instance of ListOntologiesV2Response from a dict
list_ontologies_v2_response_form_dict = list_ontologies_v2_response.from_dict(list_ontologies_v2_response_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
