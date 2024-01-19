# OntologyFullMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_types** | [**Dict\[str, ActionTypeV2\]**](ActionTypeV2.md) |  | \[optional\]
**object_types** | [**Dict\[str, ObjectTypeWithLink\]**](ObjectTypeWithLink.md) |  | \[optional\]
**ontology** | [**OntologyV2**](OntologyV2.md) |  |
**query_types** | [**Dict\[str, QueryTypeV2\]**](QueryTypeV2.md) |  | \[optional\]

## Example

```python
from foundry.models import OntologyFullMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyFullMetadata from a JSON string
ontology_full_metadata_instance = OntologyFullMetadata.from_json(json)
# print the JSON string representation of the object
print(OntologyFullMetadata.to_json())

# convert the object into a dict
ontology_full_metadata_dict = ontology_full_metadata_instance.to_dict()
# create an instance of OntologyFullMetadata from a dict
ontology_full_metadata_form_dict = ontology_full_metadata.from_dict(ontology_full_metadata_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
