# FilePathMatchesFilterDict

Only import files whose path (relative to the root of the source) matches the regular expression.

**Example**
Suppose we are importing files from `relative/subfolder`.
`relative/subfolder` contains:
- `relative/subfolder/include-file.txt`
- `relative/subfolder/exclude-file.txt`
- `relative/subfolder/other-file.txt`

With the `relative/subfolder/include-.*.txt` regex, only `relative/subfolder/include-file.txt` will be imported.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**regex** | pydantic.StrictStr | Yes | Must be written to match the paths relative to the root of the source, even if a subfolder is specified.  |
**type** | Literal["pathMatchesFilter"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
