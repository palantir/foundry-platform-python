# DeleteLinkRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_side_object_type_api_name** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**b_side_object_type_api_name** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**link_type_api_name_ato_b** | **str** | The name of the link type in the API. To find the API name for your Link Type, check the **Ontology Manager** application.  |
**link_type_api_name_bto_a** | **str** | The name of the link type in the API. To find the API name for your Link Type, check the **Ontology Manager** application.  |
**type** | **str** |  |

## Example

```python
from foundry.models import DeleteLinkRule

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteLinkRule from a JSON string
delete_link_rule_instance = DeleteLinkRule.from_json(json)
# print the JSON string representation of the object
print(DeleteLinkRule.to_json())

# convert the object into a dict
delete_link_rule_dict = delete_link_rule_instance.to_dict()
# create an instance of DeleteLinkRule from a dict
delete_link_rule_form_dict = delete_link_rule.from_dict(delete_link_rule_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
