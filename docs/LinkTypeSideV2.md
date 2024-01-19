# LinkTypeSideV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** | The name of the link type in the API. To find the API name for your Link Type, check the **Ontology Manager** application.  |
**cardinality** | [**LinkTypeSideCardinality**](LinkTypeSideCardinality.md) |  |
**display_name** | **str** | The display name of the entity. |
**foreign_key_property_api_name** | **str** | The name of the property in the API. To find the API name for your property, use the \`Get object type\` endpoint or check the **Ontology Manager**.  | \[optional\]
**object_type_api_name** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**status** | [**ReleaseStatus**](ReleaseStatus.md) |  |

## Example

```python
from foundry.models import LinkTypeSideV2

# TODO update the JSON string below
json = "{}"
# create an instance of LinkTypeSideV2 from a JSON string
link_type_side_v2_instance = LinkTypeSideV2.from_json(json)
# print the JSON string representation of the object
print(LinkTypeSideV2.to_json())

# convert the object into a dict
link_type_side_v2_dict = link_type_side_v2_instance.to_dict()
# create an instance of LinkTypeSideV2 from a dict
link_type_side_v2_form_dict = link_type_side_v2.from_dict(link_type_side_v2_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
