# LoadObjectSetV2ObjectsOrInterfacesResponseDict

Represents the API response when loading an `ObjectSet`. Objects in the returned set can either have properties 
defined by an interface that the objects belong to or properties defined by the object type of the object.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**data** | List[OntologyObjectV2] | Yes | The list of objects in the current page. |
**nextPageToken** | NotRequired[PageToken] | No |  |
**totalCount** | TotalCount | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
