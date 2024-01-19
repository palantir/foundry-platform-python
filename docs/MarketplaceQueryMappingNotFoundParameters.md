# MarketplaceQueryMappingNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_repository** | **str** |  |
**package_name** | **str** |  |
**query_type** | **str** | The name of the Query in the API.  |

## Example

```python
from foundry.models import MarketplaceQueryMappingNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceQueryMappingNotFoundParameters from a JSON string
marketplace_query_mapping_not_found_parameters_instance = MarketplaceQueryMappingNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(MarketplaceQueryMappingNotFoundParameters.to_json())

# convert the object into a dict
marketplace_query_mapping_not_found_parameters_dict = marketplace_query_mapping_not_found_parameters_instance.to_dict()
# create an instance of MarketplaceQueryMappingNotFoundParameters from a dict
marketplace_query_mapping_not_found_parameters_form_dict = marketplace_query_mapping_not_found_parameters.from_dict(marketplace_query_mapping_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
