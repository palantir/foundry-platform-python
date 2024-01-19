# MarketplaceObjectMappingNotFound

The given object could not be mapped to a Marketplace installation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**MarketplaceObjectMappingNotFoundParameters**](MarketplaceObjectMappingNotFoundParameters.md) |  |

## Example

```python
from foundry.models import MarketplaceObjectMappingNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceObjectMappingNotFound from a JSON string
marketplace_object_mapping_not_found_instance = MarketplaceObjectMappingNotFound.from_json(json)
# print the JSON string representation of the object
print(MarketplaceObjectMappingNotFound.to_json())

# convert the object into a dict
marketplace_object_mapping_not_found_dict = marketplace_object_mapping_not_found_instance.to_dict()
# create an instance of MarketplaceObjectMappingNotFound from a dict
marketplace_object_mapping_not_found_form_dict = marketplace_object_mapping_not_found.from_dict(marketplace_object_mapping_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
