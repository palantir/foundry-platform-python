# AnalyzerSelection

Selects the analyzed field variant used for full-text and phrase queries.

The base analyzer searches the field using the analyzer it was indexed with. The base analyzer is used when the
optional `analyzerSelection` is omitted.
The phonetic analyzer searches the field's phonetic indexing to match similar-sounding terms.


| **Value** |
| --------- |
| `"BASE_ANALYZER"` |
| `"PHONETIC_ANALYZER"` |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
