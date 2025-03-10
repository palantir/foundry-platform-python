# ObjectSetNearestNeighborsTypeDict

ObjectSet containing the top `numNeighbors` objects with `propertyIdentifier` nearest to the input vector or
text. This can only be performed on a property with type vector that has been configured to be searched with
approximate nearest neighbors using a similarity function configured in the Ontology.

A non-zero score for each resulting object is returned when the `orderType` in the `orderBy` field is set to
`relevance`. Note that:
  - Scores will not be returned if a nearestNeighbors object set is composed through union, subtraction 
    or intersection with non-nearestNeighbors object sets.
  - If results have scores, the order of the scores will be decreasing (duplicate scores are possible).


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**objectSet** | ObjectSetDict | Yes |  |
**propertyIdentifier** | PropertyIdentifierDict | Yes |  |
**numNeighbors** | int | Yes | The number of objects to return. If the number of documents in the objectType is less than the provided value, all objects will be returned. This value is limited to 1 &lt;= numNeighbors &lt;= 500.  |
**query** | NearestNeighborsQueryDict | Yes |  |
**type** | typing.Literal["nearestNeighbors"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
