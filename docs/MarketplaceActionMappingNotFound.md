# MarketplaceActionMappingNotFound

The given action could not be mapped to a Marketplace installation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**MarketplaceActionMappingNotFoundParameters**](MarketplaceActionMappingNotFoundParameters.md) |  |

## Example

```python
from foundry.models import MarketplaceActionMappingNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceActionMappingNotFound from a JSON string
marketplace_action_mapping_not_found_instance = MarketplaceActionMappingNotFound.from_json(json)
# print the JSON string representation of the object
print(MarketplaceActionMappingNotFound.to_json())

# convert the object into a dict
marketplace_action_mapping_not_found_dict = marketplace_action_mapping_not_found_instance.to_dict()
# create an instance of MarketplaceActionMappingNotFound from a dict
marketplace_action_mapping_not_found_form_dict = marketplace_action_mapping_not_found.from_dict(marketplace_action_mapping_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
