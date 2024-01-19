# OntologyMapType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_type** | [**OntologyDataType**](OntologyDataType.md) |  |
**type** | **str** |  |
**value_type** | [**OntologyDataType**](OntologyDataType.md) |  |

## Example

```python
from foundry.models import OntologyMapType

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyMapType from a JSON string
ontology_map_type_instance = OntologyMapType.from_json(json)
# print the JSON string representation of the object
print(OntologyMapType.to_json())

# convert the object into a dict
ontology_map_type_dict = ontology_map_type_instance.to_dict()
# create an instance of OntologyMapType from a dict
ontology_map_type_form_dict = ontology_map_type.from_dict(ontology_map_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
