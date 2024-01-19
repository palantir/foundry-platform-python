# OntologyEditsExceededLimit

The number of edits to the Ontology exceeded the allowed limit. This may happen because of the request or because the Action is modifying too many objects. Please change the size of your request or contact the Ontology administrator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**OntologyEditsExceededLimitParameters**](OntologyEditsExceededLimitParameters.md) |  |

## Example

```python
from foundry.models import OntologyEditsExceededLimit

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyEditsExceededLimit from a JSON string
ontology_edits_exceeded_limit_instance = OntologyEditsExceededLimit.from_json(json)
# print the JSON string representation of the object
print(OntologyEditsExceededLimit.to_json())

# convert the object into a dict
ontology_edits_exceeded_limit_dict = ontology_edits_exceeded_limit_instance.to_dict()
# create an instance of OntologyEditsExceededLimit from a dict
ontology_edits_exceeded_limit_form_dict = ontology_edits_exceeded_limit.from_dict(ontology_edits_exceeded_limit_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
