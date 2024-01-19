# OntologyStructType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List\[OntologyStructField\]**](OntologyStructField.md) |  | \[optional\]
**type** | **str** |  |

## Example

```python
from foundry.models import OntologyStructType

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyStructType from a JSON string
ontology_struct_type_instance = OntologyStructType.from_json(json)
# print the JSON string representation of the object
print(OntologyStructType.to_json())

# convert the object into a dict
ontology_struct_type_dict = ontology_struct_type_instance.to_dict()
# create an instance of OntologyStructType from a dict
ontology_struct_type_form_dict = ontology_struct_type.from_dict(ontology_struct_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
