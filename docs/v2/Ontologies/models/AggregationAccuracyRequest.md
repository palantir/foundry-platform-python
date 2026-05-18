# AggregationAccuracyRequest

Specifies the accuracy requirement for aggregation results.

- `REQUIRE_ACCURATE`: Only return results if they are guaranteed to be accurate. If accuracy cannot be
  guaranteed (e.g., due to a low `maxGroupCount` relative to distinct values), the request will fail
  with an `AggregationAccuracyNotSupported` error.
- `ALLOW_APPROXIMATE`: Allow approximate results when exact computation is not feasible. This is the
  default behavior if not specified.


| **Value** |
| --------- |
| `"REQUIRE_ACCURATE"` |
| `"ALLOW_APPROXIMATE"` |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
