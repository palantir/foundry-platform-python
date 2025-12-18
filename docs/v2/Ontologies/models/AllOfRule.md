# AllOfRule

Matches intervals satisfying all the rules in the query


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rules** | List[IntervalQueryRule] | Yes |  |
**max_gaps** | Optional[int] | No | The maximum gaps between the intervals produced by the sub-rules. If not set, then gaps are not considered.  |
**ordered** | bool | Yes | If true, the matched intervals must occur in order. |
**type** | Literal["allOf"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
