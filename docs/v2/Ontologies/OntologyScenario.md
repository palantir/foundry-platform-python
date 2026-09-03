# OntologyScenario

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create_scenario**](#create_scenario) | **POST** /v2/ontologies/{ontology}/scenarios/create | Private Beta |
[**list_scenario_conflicting_objects**](#list_scenario_conflicting_objects) | **GET** /v2/ontologies/{ontology}/scenarios/{scenarioRid}/objects/{objectType}/conflicting | Private Beta |
[**list_scenario_edited_entity_types**](#list_scenario_edited_entity_types) | **GET** /v2/ontologies/{ontology}/scenarios/{scenarioRid}/editedEntityTypes | Private Beta |
[**list_scenario_edited_link_types**](#list_scenario_edited_link_types) | **GET** /v2/ontologies/{ontology}/scenarios/{scenarioRid}/objectTypes/{objectType}/outgoingLinkTypes/edited | Private Beta |
[**list_scenario_edited_links**](#list_scenario_edited_links) | **GET** /v2/ontologies/{ontology}/scenarios/{scenarioRid}/objects/{objectType}/links/{linkType}/edited | Private Beta |
[**list_scenario_edited_object_types**](#list_scenario_edited_object_types) | **GET** /v2/ontologies/{ontology}/scenarios/{scenarioRid}/objectTypes/edited | Private Beta |
[**list_scenario_edited_objects**](#list_scenario_edited_objects) | **GET** /v2/ontologies/{ontology}/scenarios/{scenarioRid}/objects/{objectType}/edited | Private Beta |

# **create_scenario**
Creates an ontology scenario.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**base** | Optional[OntologyBase] |  | [optional] |
**expire_after** | Optional[datetime] | The date after which the scenario expires and is automatically cleaned up. Defaults to 31 days after creation. Must be after creation and no later than 31 days after creation.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**CreateOntologyScenarioResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# Optional[OntologyBase]
base = {"type": "branch", "branch": "my-branch"}
# Optional[datetime] | The date after which the scenario expires and is automatically cleaned up. Defaults to 31 days after creation. Must be after creation and no later than 31 days after creation.
expire_after = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.OntologyScenario.create_scenario(
        ontology, base=base, expire_after=expire_after, preview=preview
    )
    print("The create_scenario response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyScenario.create_scenario: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CreateOntologyScenarioResponse  | Successfully created a scenario. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_scenario_conflicting_objects**
Returns the list of objects with edits that conflict with edits to the scenario's base for a specific object
type. A conflict occurs when an object has been edited both within the scenario and on the scenario's base
after the scenario was created. Only objects that the user has permission to view are returned.

Conflict detection takes into account changes that are not reflected in the user-visible object data.
As a result, this endpoint may report false positives. An object may be returned as conflicting even if
its data has not actually changed on the scenario's base.

Each page may be smaller than the requested page size.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**scenario_rid** | OntologyScenarioRid | The unique resource identifier of the scenario.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type.  |  |
**page_size** | Optional[PageSize] | The maximum number of objects to examine when searching for conflicts. This bounds the work performed per call; it is not a guarantee on the number of conflicting objects returned, which may be smaller. Each page may be smaller than this value.  | [optional] |
**page_token** | Optional[PageToken] | The page token to use for pagination.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListScenarioConflictingObjectsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# OntologyScenarioRid | The unique resource identifier of the scenario.
scenario_rid = "ri.actions..scenario.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | The API name of the object type.
object_type = "employee"
# Optional[PageSize] | The maximum number of objects to examine when searching for conflicts. This bounds the work performed per call; it is not a guarantee on the number of conflicting objects returned, which may be smaller. Each page may be smaller than this value.
page_size = None
# Optional[PageToken] | The page token to use for pagination.
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    for ontology_scenario in client.ontologies.OntologyScenario.list_scenario_conflicting_objects(
        ontology,
        scenario_rid,
        object_type,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(ontology_scenario)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyScenario.list_scenario_conflicting_objects: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListScenarioConflictingObjectsResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_scenario_edited_entity_types**
Returns the object types and link types that have been modified within a given scenario.

The response contains the list of object type API names that have been modified, and the list of
many-to-many link types that have been modified, grouped by their source object type. One-to-many
link type edits are surfaced as object edits on the object type that owns the foreign key property.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**scenario_rid** | OntologyScenarioRid | The unique resource identifier of the scenario.  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListScenarioEditedEntityTypesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# OntologyScenarioRid | The unique resource identifier of the scenario.
scenario_rid = "ri.actions..scenario.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.OntologyScenario.list_scenario_edited_entity_types(
        ontology, scenario_rid, preview=preview
    )
    print("The list_scenario_edited_entity_types response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyScenario.list_scenario_edited_entity_types: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListScenarioEditedEntityTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_scenario_edited_link_types**
Returns the list of outgoing links that have been modified within a given scenario for an object type.

Note that only many-to-many link type are returned by this endpoint. One-to-many link type edits are
surfaced as object edits on the object type that owns the foreign key property.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**scenario_rid** | OntologyScenarioRid | The unique resource identifier of the scenario.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListScenarioEditedLinkTypesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# OntologyScenarioRid | The unique resource identifier of the scenario.
scenario_rid = "ri.actions..scenario.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
object_type = "Flight"
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.OntologyScenario.list_scenario_edited_link_types(
        ontology, scenario_rid, object_type, preview=preview
    )
    print("The list_scenario_edited_link_types response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyScenario.list_scenario_edited_link_types: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListScenarioEditedLinkTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_scenario_edited_links**
Returns the list of edited links within a given scenario for a specific object type and link type, grouped
by source object. Only works for many-to-many link types. Only links where the user has permission to view
both objects are returned.

Each page may be smaller than the requested page size.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**scenario_rid** | OntologyScenarioRid | The unique resource identifier of the scenario.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type.  |  |
**link_type** | LinkTypeApiName | The API name of the link type.  |  |
**page_size** | Optional[PageSize] | The maximum number of links to return per page.  | [optional] |
**page_token** | Optional[PageToken] | The page token to use for pagination.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListScenarioEditedLinksResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# OntologyScenarioRid | The unique resource identifier of the scenario.
scenario_rid = "ri.actions..scenario.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | The API name of the object type.
object_type = "employee"
# LinkTypeApiName | The API name of the link type.
link_type = "employeeReportsTo"
# Optional[PageSize] | The maximum number of links to return per page.
page_size = None
# Optional[PageToken] | The page token to use for pagination.
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    for ontology_scenario in client.ontologies.OntologyScenario.list_scenario_edited_links(
        ontology,
        scenario_rid,
        object_type,
        link_type,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(ontology_scenario)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyScenario.list_scenario_edited_links: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListScenarioEditedLinksResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_scenario_edited_object_types**
Returns the list of object type API names that have been modified within a given scenario.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**scenario_rid** | OntologyScenarioRid | The unique resource identifier of the scenario.  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListScenarioEditedObjectTypesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# OntologyScenarioRid | The unique resource identifier of the scenario.
scenario_rid = "ri.actions..scenario.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.OntologyScenario.list_scenario_edited_object_types(
        ontology, scenario_rid, preview=preview
    )
    print("The list_scenario_edited_object_types response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyScenario.list_scenario_edited_object_types: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListScenarioEditedObjectTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_scenario_edited_objects**
Returns the list of objects that have been edited within a given scenario for a specific object type.
Only objects that the user has permission to view are returned.

Each page may be smaller than the requested page size.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**scenario_rid** | OntologyScenarioRid | The unique resource identifier of the scenario.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type.  |  |
**page_size** | Optional[PageSize] | The maximum number of objects to return per page.  | [optional] |
**page_token** | Optional[PageToken] | The page token to use for pagination.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListScenarioEditedObjectsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# OntologyScenarioRid | The unique resource identifier of the scenario.
scenario_rid = "ri.actions..scenario.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"
# ObjectTypeApiName | The API name of the object type.
object_type = "employee"
# Optional[PageSize] | The maximum number of objects to return per page.
page_size = None
# Optional[PageToken] | The page token to use for pagination.
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    for ontology_scenario in client.ontologies.OntologyScenario.list_scenario_edited_objects(
        ontology,
        scenario_rid,
        object_type,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(ontology_scenario)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyScenario.list_scenario_edited_objects: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListScenarioEditedObjectsResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

