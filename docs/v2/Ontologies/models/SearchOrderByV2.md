# SearchOrderByV2

Specifies the ordering of search results by a field and an ordering direction, or by relevance.
If the `fields` array is provided, `orderType` is automatically set to `fields`.
If this object is omitted entirely, the ordering is unspecified.

Setting `orderType` to `relevance` requests that results are sorted by decreasing relevance score.
For queries that include text search filters (e.g. `containsAllTerms`, `containsAnyTerm`,
`containsAllTermsInOrder`, `containsAllTermsInOrderPrefixLastTerm`) or `nearestNeighbors`, the
relevance score reflects how well each object matches the query. For other queries, the ordering
is unspecified.

When paging through results ordered by relevance, ordering is not guaranteed to be consistent
across pages: an object may appear on multiple pages or be skipped entirely. Use a single page
when result completeness is required.

Relevance ordering can be expensive and should only be used when required.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**order_type** | Optional[SearchOrderByType] | No |  |
**fields** | List[SearchOrderingV2] | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
