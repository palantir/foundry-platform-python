# PipelineBuilderLiteralJson

A tagged JSON object with the same structure and constraints as `PipelineBuilderLiteral`, used for nested literals.
Scalar variants contain `type` and `value`; `array` contains `values`; `map` contains `entries` with `key` and `value`
literals; `empty` contains only `type`. Arrays and maps can contain further literals recursively. For example,
`{"type":"array","values":[{"type":"long","value":"42"},{"type":"empty"}]}`.

Every nested literal must use a supported tag and its corresponding value format. Untagged objects, JSON null,
unknown tags, and values outside the selected type's range are invalid.

## Type
```python
Any
```


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
