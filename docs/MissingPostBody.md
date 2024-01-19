# MissingPostBody

A post body is required for this endpoint, but was not found in the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | **object** |  |

## Example

```python
from foundry.models import MissingPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of MissingPostBody from a JSON string
missing_post_body_instance = MissingPostBody.from_json(json)
# print the JSON string representation of the object
print(MissingPostBody.to_json())

# convert the object into a dict
missing_post_body_dict = missing_post_body_instance.to_dict()
# create an instance of MissingPostBody from a dict
missing_post_body_form_dict = missing_post_body.from_dict(missing_post_body_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
