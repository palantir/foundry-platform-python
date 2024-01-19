# OntologyObjectArrayType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_type** | [**ObjectPropertyType**](ObjectPropertyType.md) |  |
**type** | **str** |  |

## Example

```python
from foundry.models import OntologyObjectArrayType

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyObjectArrayType from a JSON string
ontology_object_array_type_instance = OntologyObjectArrayType.from_json(json)
# print the JSON string representation of the object
print(OntologyObjectArrayType.to_json())

# convert the object into a dict
ontology_object_array_type_dict = ontology_object_array_type_instance.to_dict()
# create an instance of OntologyObjectArrayType from a dict
ontology_object_array_type_form_dict = ontology_object_array_type.from_dict(ontology_object_array_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
