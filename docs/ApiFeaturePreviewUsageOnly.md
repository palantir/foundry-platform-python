# ApiFeaturePreviewUsageOnly

This feature is only supported in preview mode. Please use `preview=true` in the query parameters to call this endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import ApiFeaturePreviewUsageOnly

# TODO update the JSON string below
json = "{}"
# create an instance of ApiFeaturePreviewUsageOnly from a JSON string
api_feature_preview_usage_only_instance = ApiFeaturePreviewUsageOnly.from_json(json)
# print the JSON string representation of the object
print(ApiFeaturePreviewUsageOnly.to_json())

# convert the object into a dict
api_feature_preview_usage_only_dict = api_feature_preview_usage_only_instance.to_dict()
# create an instance of ApiFeaturePreviewUsageOnly from a dict
api_feature_preview_usage_only_form_dict = api_feature_preview_usage_only.from_dict(api_feature_preview_usage_only_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
