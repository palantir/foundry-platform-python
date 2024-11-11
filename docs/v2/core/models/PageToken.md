# PageToken

The page token indicates where to start paging. This should be omitted from the first page's request.
To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response
and use it to populate the `pageToken` field of the next request.

## Type
```python
pydantic.StrictStr
```


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
