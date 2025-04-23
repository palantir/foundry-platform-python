# VersionedQueryTypeApiName

The name of the Query in the API and an optional version identifier separated by a colon.
If the API name contains a colon, then a version identifier of either "latest" or a semantic version must
be included.
If the API does not contain a colon, then either the version identifier must be excluded or a version
identifier of a semantic version must be included.
Examples: 'myGroup:myFunction:latest', 'myGroup:myFunction:1.0.0', 'myFunction', 'myFunction:2.0.0'


## Type
```python
str
```


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
