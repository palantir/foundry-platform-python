# MarketplaceInstallationNotFound

The given marketplace installation could not be found or the user does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**MarketplaceInstallationNotFoundParameters**](MarketplaceInstallationNotFoundParameters.md) |  |

## Example

```python
from foundry.models import MarketplaceInstallationNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceInstallationNotFound from a JSON string
marketplace_installation_not_found_instance = MarketplaceInstallationNotFound.from_json(json)
# print the JSON string representation of the object
print(MarketplaceInstallationNotFound.to_json())

# convert the object into a dict
marketplace_installation_not_found_dict = marketplace_installation_not_found_instance.to_dict()
# create an instance of MarketplaceInstallationNotFound from a dict
marketplace_installation_not_found_form_dict = marketplace_installation_not_found.from_dict(marketplace_installation_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
