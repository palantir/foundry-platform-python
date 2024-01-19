# QueryType

Represents a query type in the Ontology.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** | The name of the Query in the API.  |
**description** | **str** |  | \[optional\]
**display_name** | **str** | The display name of the entity. | \[optional\]
**output** | [**OntologyDataType**](OntologyDataType.md) |  | \[optional\]
**parameters** | [**Dict\[str, Parameter\]**](Parameter.md) |  | \[optional\]
**rid** | **str** | The unique resource identifier of a Function, useful for interacting with other Foundry APIs.  |
**version** | **str** | The version of the given Function, written \`\<major>.\<minor>.\<patch>-\<tag>\`, where \`-\<tag>\` is optional. Examples: \`1.2.3\`, \`1.2.3-rc1\`.  |

## Example

```python
from foundry.models import QueryType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryType from a JSON string
query_type_instance = QueryType.from_json(json)
# print the JSON string representation of the object
print(QueryType.to_json())

# convert the object into a dict
query_type_dict = query_type_instance.to_dict()
# create an instance of QueryType from a dict
query_type_form_dict = query_type.from_dict(query_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
