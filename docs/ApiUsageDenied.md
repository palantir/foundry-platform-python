# ApiUsageDenied

You are not allowed to use Palantir APIs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import ApiUsageDenied

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsageDenied from a JSON string
api_usage_denied_instance = ApiUsageDenied.from_json(json)
# print the JSON string representation of the object
print(ApiUsageDenied.to_json())

# convert the object into a dict
api_usage_denied_dict = api_usage_denied_instance.to_dict()
# create an instance of ApiUsageDenied from a dict
api_usage_denied_form_dict = api_usage_denied.from_dict(api_usage_denied_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
