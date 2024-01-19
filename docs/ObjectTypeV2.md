# ObjectTypeV2

Represents an object type in the Ontology.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**description** | **str** | The description of the object type. | \[optional\]
**display_name** | **str** | The display name of the entity. | \[optional\]
**primary_key** | **str** | The name of the property in the API. To find the API name for your property, use the \`Get object type\` endpoint or check the **Ontology Manager**.  |
**properties** | [**Dict\[str, PropertyV2\]**](PropertyV2.md) | A map of the properties of the object type. | \[optional\]
**rid** | **str** | The unique resource identifier of an object type, useful for interacting with other Foundry APIs. |
**status** | [**ReleaseStatus**](ReleaseStatus.md) |  |
**visibility** | [**ObjectTypeVisibility**](ObjectTypeVisibility.md) |  | \[optional\]

## Example

```python
from foundry.models import ObjectTypeV2

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectTypeV2 from a JSON string
object_type_v2_instance = ObjectTypeV2.from_json(json)
# print the JSON string representation of the object
print(ObjectTypeV2.to_json())

# convert the object into a dict
object_type_v2_dict = object_type_v2_instance.to_dict()
# create an instance of ObjectTypeV2 from a dict
object_type_v2_form_dict = object_type_v2.from_dict(object_type_v2_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
