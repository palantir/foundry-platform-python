# MarketplaceQueryMappingNotFound

The given query could not be mapped to a Marketplace installation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**MarketplaceQueryMappingNotFoundParameters**](MarketplaceQueryMappingNotFoundParameters.md) |  |

## Example

```python
from foundry.models import MarketplaceQueryMappingNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceQueryMappingNotFound from a JSON string
marketplace_query_mapping_not_found_instance = MarketplaceQueryMappingNotFound.from_json(json)
# print the JSON string representation of the object
print(MarketplaceQueryMappingNotFound.to_json())

# convert the object into a dict
marketplace_query_mapping_not_found_dict = marketplace_query_mapping_not_found_instance.to_dict()
# create an instance of MarketplaceQueryMappingNotFound from a dict
marketplace_query_mapping_not_found_form_dict = marketplace_query_mapping_not_found.from_dict(marketplace_query_mapping_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
