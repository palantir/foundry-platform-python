# ObjectType

Represents an object type in the Ontology.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**description** | **str** | The description of the object type. | \[optional\]
**display_name** | **str** | The display name of the entity. | \[optional\]
**primary_key** | **List\[str\]** | The primary key of the object. This is a list of properties that can be used to uniquely identify the object. | \[optional\]
**properties** | [**Dict\[str, ModelProperty\]**](ModelProperty.md) | A map of the properties of the object type. | \[optional\]
**rid** | **str** | The unique resource identifier of an object type, useful for interacting with other Foundry APIs. |
**status** | [**ReleaseStatus**](ReleaseStatus.md) |  |
**visibility** | [**ObjectTypeVisibility**](ObjectTypeVisibility.md) |  | \[optional\]

## Example

```python
from foundry.models import ObjectType

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectType from a JSON string
object_type_instance = ObjectType.from_json(json)
# print the JSON string representation of the object
print(ObjectType.to_json())

# convert the object into a dict
object_type_dict = object_type_instance.to_dict()
# create an instance of ObjectType from a dict
object_type_form_dict = object_type.from_dict(object_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
