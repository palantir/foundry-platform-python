# ModifyObjectRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type_api_name** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**type** | **str** |  |

## Example

```python
from foundry.models import ModifyObjectRule

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyObjectRule from a JSON string
modify_object_rule_instance = ModifyObjectRule.from_json(json)
# print the JSON string representation of the object
print(ModifyObjectRule.to_json())

# convert the object into a dict
modify_object_rule_dict = modify_object_rule_instance.to_dict()
# create an instance of ModifyObjectRule from a dict
modify_object_rule_form_dict = modify_object_rule.from_dict(modify_object_rule_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
