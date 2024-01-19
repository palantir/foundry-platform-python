# InvalidPageTokenParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_token** | **str** | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the \`nextPageToken\` field of the previous response and populate the next request's \`pageToken\` field with it.  |

## Example

```python
from foundry.models import InvalidPageTokenParameters

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPageTokenParameters from a JSON string
invalid_page_token_parameters_instance = InvalidPageTokenParameters.from_json(json)
# print the JSON string representation of the object
print(InvalidPageTokenParameters.to_json())

# convert the object into a dict
invalid_page_token_parameters_dict = invalid_page_token_parameters_instance.to_dict()
# create an instance of InvalidPageTokenParameters from a dict
invalid_page_token_parameters_form_dict = invalid_page_token_parameters.from_dict(invalid_page_token_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
