# OntologySyncing

The requested object type has been changed in the **Ontology Manager** and changes are currently being applied. Wait a few seconds and try again.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ObjectTypeNotSyncedParameters**](ObjectTypeNotSyncedParameters.md) |  |

## Example

```python
from foundry.models import OntologySyncing

# TODO update the JSON string below
json = "{}"
# create an instance of OntologySyncing from a JSON string
ontology_syncing_instance = OntologySyncing.from_json(json)
# print the JSON string representation of the object
print(OntologySyncing.to_json())

# convert the object into a dict
ontology_syncing_dict = ontology_syncing_instance.to_dict()
# create an instance of OntologySyncing from a dict
ontology_syncing_form_dict = ontology_syncing.from_dict(ontology_syncing_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
