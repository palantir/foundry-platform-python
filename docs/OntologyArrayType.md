# OntologyArrayType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | [**OntologyDataType**](OntologyDataType.md) |  |
**type** | **str** |  |

## Example

```python
from foundry.models import OntologyArrayType

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyArrayType from a JSON string
ontology_array_type_instance = OntologyArrayType.from_json(json)
# print the JSON string representation of the object
print(OntologyArrayType.to_json())

# convert the object into a dict
ontology_array_type_dict = ontology_array_type_instance.to_dict()
# create an instance of OntologyArrayType from a dict
ontology_array_type_form_dict = ontology_array_type.from_dict(ontology_array_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
