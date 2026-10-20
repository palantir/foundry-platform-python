# OntologyLiteralJson

A tagged JSON object with the same structure and constraints as `OntologyLiteral`, used for an array element.
Scalar variants contain `type` and `value`; the `array` variant contains `values` with further tagged literals.
For example, `{"type":"array","values":[{"type":"long","value":"1234"}]}`.

Every nested literal must use a supported tag and its corresponding value format. Untagged objects, JSON null,
unknown tags, and values outside the selected type's range are invalid.

## Type
```python
Any
```


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
