# CreateObjectRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type_api_name** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**type** | **str** |  |

## Example

```python
from foundry.models import CreateObjectRule

# TODO update the JSON string below
json = "{}"
# create an instance of CreateObjectRule from a JSON string
create_object_rule_instance = CreateObjectRule.from_json(json)
# print the JSON string representation of the object
print(CreateObjectRule.to_json())

# convert the object into a dict
create_object_rule_dict = create_object_rule_instance.to_dict()
# create an instance of CreateObjectRule from a dict
create_object_rule_form_dict = create_object_rule.from_dict(create_object_rule_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
