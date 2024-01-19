# OntologyStructField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_type** | [**OntologyDataType**](OntologyDataType.md) |  |
**name** | **str** | The name of a field in a \`Struct\`.  |
**required** | **bool** |  |

## Example

```python
from foundry.models import OntologyStructField

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyStructField from a JSON string
ontology_struct_field_instance = OntologyStructField.from_json(json)
# print the JSON string representation of the object
print(OntologyStructField.to_json())

# convert the object into a dict
ontology_struct_field_dict = ontology_struct_field_instance.to_dict()
# create an instance of OntologyStructField from a dict
ontology_struct_field_form_dict = ontology_struct_field.from_dict(ontology_struct_field_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
