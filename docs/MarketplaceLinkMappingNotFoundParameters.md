# MarketplaceLinkMappingNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_repository** | **str** |  |
**link_type** | **str** | The name of the link type in the API. To find the API name for your Link Type, check the **Ontology Manager** application.  |
**object_type** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**package_name** | **str** |  |

## Example

```python
from foundry.models import MarketplaceLinkMappingNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceLinkMappingNotFoundParameters from a JSON string
marketplace_link_mapping_not_found_parameters_instance = MarketplaceLinkMappingNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(MarketplaceLinkMappingNotFoundParameters.to_json())

# convert the object into a dict
marketplace_link_mapping_not_found_parameters_dict = marketplace_link_mapping_not_found_parameters_instance.to_dict()
# create an instance of MarketplaceLinkMappingNotFoundParameters from a dict
marketplace_link_mapping_not_found_parameters_form_dict = marketplace_link_mapping_not_found_parameters.from_dict(marketplace_link_mapping_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
