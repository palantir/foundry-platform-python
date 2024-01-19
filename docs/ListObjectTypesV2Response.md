# ListObjectTypesV2Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List\[ObjectTypeV2\]**](ObjectTypeV2.md) | The list of object types in the current page. | \[optional\]
**next_page_token** | **str** | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the \`nextPageToken\` field of the previous response and populate the next request's \`pageToken\` field with it.  | \[optional\]

## Example

```python
from foundry.models import ListObjectTypesV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectTypesV2Response from a JSON string
list_object_types_v2_response_instance = ListObjectTypesV2Response.from_json(json)
# print the JSON string representation of the object
print(ListObjectTypesV2Response.to_json())

# convert the object into a dict
list_object_types_v2_response_dict = list_object_types_v2_response_instance.to_dict()
# create an instance of ListObjectTypesV2Response from a dict
list_object_types_v2_response_form_dict = list_object_types_v2_response.from_dict(list_object_types_v2_response_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
