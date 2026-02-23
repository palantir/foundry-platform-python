# FuzzyRule

Matches intervals containing terms that are similar to the provided term, within an edit distance
defined by fuzziness. An edit is a single character change needed to make a term match, including
character insertion, deletion, substitution, or transposition of two adjacent characters.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**term** | str | Yes | The term to match. |
**fuzziness** | Optional[int] | No | Maximum edit distance allowed for matching. Valid values are 0, 1, or 2. Defaults to 2.  |
**type** | Literal["fuzzy"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
