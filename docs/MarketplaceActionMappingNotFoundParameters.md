# MarketplaceActionMappingNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | The name of the action type in the API. To find the API name for your Action Type, use the \`List action types\` endpoint or check the **Ontology Manager**.  |
**artifact_repository** | **str** |  |
**package_name** | **str** |  |

## Example

```python
from foundry.models import MarketplaceActionMappingNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceActionMappingNotFoundParameters from a JSON string
marketplace_action_mapping_not_found_parameters_instance = MarketplaceActionMappingNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(MarketplaceActionMappingNotFoundParameters.to_json())

# convert the object into a dict
marketplace_action_mapping_not_found_parameters_dict = marketplace_action_mapping_not_found_parameters_instance.to_dict()
# create an instance of MarketplaceActionMappingNotFoundParameters from a dict
marketplace_action_mapping_not_found_parameters_form_dict = marketplace_action_mapping_not_found_parameters.from_dict(marketplace_action_mapping_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
