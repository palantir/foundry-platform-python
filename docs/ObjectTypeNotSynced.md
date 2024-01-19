# ObjectTypeNotSynced

The requested object types are not synced into the ontology. Please reach out to your Ontology Administrator to re-index the object type in Ontology Management Application.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**ObjectTypeNotSyncedParameters**](ObjectTypeNotSyncedParameters.md) |  |

## Example

```python
from foundry.models import ObjectTypeNotSynced

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectTypeNotSynced from a JSON string
object_type_not_synced_instance = ObjectTypeNotSynced.from_json(json)
# print the JSON string representation of the object
print(ObjectTypeNotSynced.to_json())

# convert the object into a dict
object_type_not_synced_dict = object_type_not_synced_instance.to_dict()
# create an instance of ObjectTypeNotSynced from a dict
object_type_not_synced_form_dict = object_type_not_synced.from_dict(object_type_not_synced_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
