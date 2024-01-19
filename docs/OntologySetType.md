# OntologySetType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | [**OntologyDataType**](OntologyDataType.md) |  |
**type** | **str** |  |

## Example

```python
from foundry.models import OntologySetType

# TODO update the JSON string below
json = "{}"
# create an instance of OntologySetType from a JSON string
ontology_set_type_instance = OntologySetType.from_json(json)
# print the JSON string representation of the object
print(OntologySetType.to_json())

# convert the object into a dict
ontology_set_type_dict = ontology_set_type_instance.to_dict()
# create an instance of OntologySetType from a dict
ontology_set_type_form_dict = ontology_set_type.from_dict(ontology_set_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
