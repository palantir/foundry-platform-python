# MarketplaceObjectMappingNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_repository** | **str** |  |
**object_type** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**package_name** | **str** |  |

## Example

```python
from foundry.models import MarketplaceObjectMappingNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceObjectMappingNotFoundParameters from a JSON string
marketplace_object_mapping_not_found_parameters_instance = MarketplaceObjectMappingNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(MarketplaceObjectMappingNotFoundParameters.to_json())

# convert the object into a dict
marketplace_object_mapping_not_found_parameters_dict = marketplace_object_mapping_not_found_parameters_instance.to_dict()
# create an instance of MarketplaceObjectMappingNotFoundParameters from a dict
marketplace_object_mapping_not_found_parameters_form_dict = marketplace_object_mapping_not_found_parameters.from_dict(marketplace_object_mapping_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
