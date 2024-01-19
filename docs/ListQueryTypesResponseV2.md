# ListQueryTypesResponseV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List\[QueryTypeV2\]**](QueryTypeV2.md) |  | \[optional\]
**next_page_token** | **str** | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the \`nextPageToken\` field of the previous response and populate the next request's \`pageToken\` field with it.  | \[optional\]

## Example

```python
from foundry.models import ListQueryTypesResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of ListQueryTypesResponseV2 from a JSON string
list_query_types_response_v2_instance = ListQueryTypesResponseV2.from_json(json)
# print the JSON string representation of the object
print(ListQueryTypesResponseV2.to_json())

# convert the object into a dict
list_query_types_response_v2_dict = list_query_types_response_v2_instance.to_dict()
# create an instance of ListQueryTypesResponseV2 from a dict
list_query_types_response_v2_form_dict = list_query_types_response_v2.from_dict(list_query_types_response_v2_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
