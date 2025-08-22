# SchemaComparisonType

The type of schema comparison to perform:
- EXACT_MATCH_ORDERED_COLUMNS: Schemas must have identical columns in the same order.
- EXACT_MATCH_UNORDERED_COLUMNS: Schemas must have identical columns but order doesn't matter.
- COLUMN_ADDITIONS_ALLOWED: Expected schema columns must be present, additional columns are allowed and 
  missing column types are ignored.
- COLUMN_ADDITIONS_ALLOWED_STRICT: Expected schema columns must be present, additional columns are allowed. 
  Both expected and actual columns must specify types and they must match exactly.

| **Value** |
| --------- |
| `"EXACT_MATCH_ORDERED_COLUMNS"` |
| `"EXACT_MATCH_UNORDERED_COLUMNS"` |
| `"COLUMN_ADDITIONS_ALLOWED"` |
| `"COLUMN_ADDITIONS_ALLOWED_STRICT"` |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
