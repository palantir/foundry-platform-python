# InvalidPageToken

The provided page token could not be used to retrieve the next page of results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**InvalidPageTokenParameters**](InvalidPageTokenParameters.md) |  |

## Example

```python
from foundry.models import InvalidPageToken

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPageToken from a JSON string
invalid_page_token_instance = InvalidPageToken.from_json(json)
# print the JSON string representation of the object
print(InvalidPageToken.to_json())

# convert the object into a dict
invalid_page_token_dict = invalid_page_token_instance.to_dict()
# create an instance of InvalidPageToken from a dict
invalid_page_token_form_dict = invalid_page_token.from_dict(invalid_page_token_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
