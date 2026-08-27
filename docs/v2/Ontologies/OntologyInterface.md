# OntologyInterface

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**aggregate**](#aggregate) | **POST** /v2/ontologies/{ontology}/interfaces/{interfaceType}/aggregate | Private Beta |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/interfaceTypes/{interfaceType} | Public Beta |
[**get_outgoing_interface_link_type**](#get_outgoing_interface_link_type) | **GET** /v2/ontologies/{ontology}/interfaceTypes/{interfaceType}/outgoingLinkTypes/{interfaceLinkType} | Private Beta |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/interfaceTypes | Public Beta |
[**list_interface_linked_objects**](#list_interface_linked_objects) | **GET** /v2/ontologies/{ontology}/interfaces/{interfaceType}/{objectType}/{primaryKey}/links/{interfaceLinkType} | Private Beta |
[**list_objects_for_interface**](#list_objects_for_interface) | **GET** /v2/ontologies/{ontology}/interfaces/{interfaceType} | Private Beta |
[**list_outgoing_interface_link_types**](#list_outgoing_interface_link_types) | **GET** /v2/ontologies/{ontology}/interfaceTypes/{interfaceType}/outgoingLinkTypes | Private Beta |
[**search**](#search) | **POST** /v2/ontologies/{ontology}/interfaces/{interfaceType}/search | Private Beta |

# **aggregate**
:::callout{theme=warning title=Warning}
This endpoint will be removed once TS OSDK is updated to use `objectSets/aggregate` with interface object
sets.
:::
Perform functions on object fields in the specified ontology and of the specified interface type. Any 
properties specified in the query must be shared property type API names defined on the interface.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**interface_type** | InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.  |  |
**aggregation** | List[AggregationV2] |  |  |
**group_by** | List[AggregationGroupByV2] |  |  |
**accuracy** | Optional[AggregationAccuracyRequest] |  | [optional] |
**branch** | Optional[FoundryBranch] | The Foundry branch to aggregate objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**where** | Optional[SearchJsonQueryV2] |  | [optional] |

### Return type
**AggregateObjectsResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
interface_type = "Employee"
# List[AggregationV2]
aggregation = [
    {"type": "min", "field": "tenure", "name": "min_tenure"},
    {"type": "avg", "field": "tenure", "name": "avg_tenure"},
]
# List[AggregationGroupByV2]
group_by = [
    {
        "field": "startDate",
        "type": "range",
        "ranges": [{"startValue": "2020-01-01", "endValue": "2020-06-01"}],
    },
    {"field": "city", "type": "exact"},
]
# Optional[AggregationAccuracyRequest]
accuracy = None
# Optional[FoundryBranch] | The Foundry branch to aggregate objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SearchJsonQueryV2]
where = {"type": "eq", "field": "name", "value": "john"}


try:
    api_response = client.ontologies.OntologyInterface.aggregate(
        ontology,
        interface_type,
        aggregation=aggregation,
        group_by=group_by,
        accuracy=accuracy,
        branch=branch,
        preview=preview,
        where=where,
    )
    print("The aggregate response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.aggregate: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AggregateObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Gets a specific interface type with the given API name.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**interface_type** | InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the interface type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |

### Return type
**InterfaceType**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
interface_type = "Employee"
# Optional[FoundryBranch] | The Foundry branch to load the interface type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.OntologyInterface.get(
        ontology,
        interface_type,
        branch=branch,
        preview=preview,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | InterfaceType  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_outgoing_interface_link_type**
Get an outgoing interface link type for an interface type.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**interface_type** | InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager** application.  |  |
**interface_link_type** | InterfaceLinkTypeApiName | The API name of the outgoing interface link. To find the API name for your interface link type, check the **Ontology Manager** page for the  parent interface.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**InterfaceLinkType**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager** application.
interface_type = "Employee"
# InterfaceLinkTypeApiName | The API name of the outgoing interface link. To find the API name for your interface link type, check the **Ontology Manager** page for the  parent interface.
interface_link_type = "worksAt"
# Optional[FoundryBranch] | The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.OntologyInterface.get_outgoing_interface_link_type(
        ontology, interface_type, interface_link_type, branch=branch, preview=preview
    )
    print("The get_outgoing_interface_link_type response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.get_outgoing_interface_link_type: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | InterfaceLinkType  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists the interface types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to list the interface types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListInterfaceTypesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# Optional[FoundryBranch] | The Foundry branch to list the interface types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    for ontology_interface in client.ontologies.OntologyInterface.list(
        ontology, branch=branch, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(ontology_interface)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListInterfaceTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_interface_linked_objects**
Lists the linked objects for a specific object and the given interface link type.

Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
repeated objects in the response pages.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Each page may be smaller or larger than the requested page size. However, it
is guaranteed that if there are more results available, at least one result will be present
in the response.

Note that null value properties will not be returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**interface_type** | InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager** application.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object from which to **start** the interface link traversal. To look up the expected  primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.  |  |
**interface_link_type** | InterfaceLinkTypeApiName | The API name of the outgoing interface link. To find the API name for your interface link type, check the **Ontology Manager** page for the  parent interface.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**exclude_rid** | Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.  | [optional] |
**order_by** | Optional[OrderBy] |  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**select** | Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.  | [optional] |
**snapshot** | Optional[bool] | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.  | [optional] |

### Return type
**ListInterfaceLinkedObjectsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager** application.
interface_type = "Employee"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the object from which to **start** the interface link traversal. To look up the expected  primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
primary_key = None
# InterfaceLinkTypeApiName | The API name of the outgoing interface link. To find the API name for your interface link type, check the **Ontology Manager** page for the  parent interface.
interface_link_type = "worksAt"
# Optional[FoundryBranch] | The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[OrderBy]
order_by = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[List[SelectedPropertyApiName]] | The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
select = None
# Optional[bool] | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.
snapshot = None


try:
    for ontology_interface in client.ontologies.OntologyInterface.list_interface_linked_objects(
        ontology,
        interface_type,
        object_type,
        primary_key,
        interface_link_type,
        branch=branch,
        exclude_rid=exclude_rid,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        select=select,
        snapshot=snapshot,
    ):
        pprint(ontology_interface)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.list_interface_linked_objects: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListInterfaceLinkedObjectsResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_objects_for_interface**
Lists the objects for the given Ontology and interface type.

Note that this endpoint does not guarantee consistency, unless you use the snapshot flag specified below. Changes to the data could result in missing or
repeated objects in the response pages.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Each page may be smaller or larger than the requested page size. However, it
is guaranteed that if there are more results available, at least one result will be present
in the response.

Note that null value properties will not be returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**interface_type** | InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to list objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**exclude_rid** | Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.  | [optional] |
**order_by** | Optional[OrderBy] |  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**select** | Optional[List[SelectedPropertyApiName]] | The properties of the interface type that should be included in the response. Omit this parameter to get all the properties.  | [optional] |
**snapshot** | Optional[bool] | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.  | [optional] |

### Return type
**ListObjectsForInterfaceResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
interface_type = "employee"
# Optional[FoundryBranch] | The Foundry branch to list objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[bool] | A flag to exclude the retrieval of the `__rid` property.  Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[OrderBy]
order_by = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[List[SelectedPropertyApiName]] | The properties of the interface type that should be included in the response. Omit this parameter to get all the properties.
select = None
# Optional[bool] | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.
snapshot = None


try:
    for ontology_interface in client.ontologies.OntologyInterface.list_objects_for_interface(
        ontology,
        interface_type,
        branch=branch,
        exclude_rid=exclude_rid,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        select=select,
        snapshot=snapshot,
    ):
        pprint(ontology_interface)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.list_objects_for_interface: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListObjectsForInterfaceResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list_outgoing_interface_link_types**
List the outgoing interface link types for an interface type.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**interface_type** | InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager** application.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to get the outgoing link type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**ListOutgoingInterfaceLinkTypesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager** application.
interface_type = "Employee"
# Optional[FoundryBranch] | The Foundry branch to get the outgoing link type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.OntologyInterface.list_outgoing_interface_link_types(
        ontology, interface_type, branch=branch, preview=preview
    )
    print("The list_outgoing_interface_link_types response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.list_outgoing_interface_link_types: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListOutgoingInterfaceLinkTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **search**
:::callout{theme=warning title=Warning}
  This endpoint will be removed once TS OSDK is updated to use `objectSets/loadObjects` with interface object
  sets.
:::
Search for objects in the specified ontology and interface type. Any properties specified in the "where" or 
"orderBy" parameters must be shared property type API names defined on the interface. The following search 
queries are supported:

| Query type                              | Description                                                                                                       | Supported Types                 |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------|
| lt                                      | The provided property is less than the provided value.                                                            | number, string, date, timestamp |
| gt                                      | The provided property is greater than the provided value.                                                         | number, string, date, timestamp |
| lte                                     | The provided property is less than or equal to the provided value.                                                | number, string, date, timestamp |
| gte                                     | The provided property is greater than or equal to the provided value.                                             | number, string, date, timestamp |
| eq                                      | The provided property is exactly equal to the provided value.                                                     | number, string, date, timestamp |
| isNull                                  | The provided property is (or is not) null.                                                                        | all                             |
| contains                                | The provided property contains the provided value.                                                                | array                           |
| not                                     | The sub-query does not match.                                                                                     | N/A (applied on a query)        |
| and                                     | All the sub-queries match.                                                                                        | N/A (applied on queries)        |
| or                                      | At least one of the sub-queries match.                                                                            | N/A (applied on queries)        |
| startsWith                              | The provided property starts with the provided term.                                                              | string                          |
| containsAllTermsInOrderPrefixLastTerm   | The provided property contains all the terms provided in order. The last term can be a partial prefix match.      | string                          |
| containsAllTermsInOrder                 | The provided property contains the provided terms as a substring.                                                 | string                          |
| containsAnyTerm                         | The provided property contains at least one of the terms separated by whitespace.                                 | string                          |
| containsAllTerms                        | The provided property contains all the terms separated by whitespace.                                             | string                          |

Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
Partial terms are not matched by terms filters except where explicitly noted.

Attempting to use an unsupported query will result in a validation error. Third-party applications using this 
endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

The `pageSize` parameter is a maximum. A page may contain fewer objects than requested if the
objects in the page are large enough to reach an internal memory limit; this does not indicate
that there are no more results. As long as the response contains a `nextPageToken`, the remaining
objects can be retrieved by requesting subsequent pages.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**interface_type** | InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.  |  |
**augmented_interface_property_types** | Dict[InterfaceTypeApiName, List[InterfacePropertyApiName]] | A map from interface type API name to a list of interface property type API names. For each returned object,  if the object implements an interface that is a key in the map, then we augment the response for that object  type with the list of properties specified in the value.  |  |
**augmented_properties** | Dict[ObjectTypeApiName, List[PropertyApiName]] | A map from object type API name to a list of property type API names. For each returned object, if the  object’s object type is a key in the map, then we augment the response for that object type with the list  of properties specified in the value.  |  |
**augmented_shared_property_types** | Dict[InterfaceTypeApiName, List[SharedPropertyTypeApiName]] | A map from interface type API name to a list of shared property type API names. For each returned object, if the object implements an interface that is a key in the map, then we augment the response for that object  type with the list of properties specified in the value.  |  |
**other_interface_types** | List[InterfaceTypeApiName] | A list of interface type API names. Object types must implement all the mentioned interfaces in order to be  included in the response.  |  |
**selected_interface_property_types** | List[InterfacePropertyApiName] | A list of interface property type API names of the interface type that should be included in the response.  Omit this parameter to include all properties of the interface type in the response.  |  |
**selected_object_types** | List[ObjectTypeApiName] | A list of object type API names that should be included in the response. If non-empty, object types that are not mentioned will not be included in the response even if they implement the specified interface. Omit the  parameter to include all object types.  |  |
**selected_shared_property_types** | List[SharedPropertyTypeApiName] | A list of shared property type API names of the interface type that should be included in the response.  Omit this parameter to include all properties of the interface type in the response.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to search objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**order_by** | Optional[SearchOrderByV2] |  | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**where** | Optional[SearchJsonQueryV2] |  | [optional] |

### Return type
**SearchObjectsResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# InterfaceTypeApiName | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
interface_type = "Employee"
# Dict[InterfaceTypeApiName, List[InterfacePropertyApiName]] | A map from interface type API name to a list of interface property type API names. For each returned object,  if the object implements an interface that is a key in the map, then we augment the response for that object  type with the list of properties specified in the value.
augmented_interface_property_types = None
# Dict[ObjectTypeApiName, List[PropertyApiName]] | A map from object type API name to a list of property type API names. For each returned object, if the  object’s object type is a key in the map, then we augment the response for that object type with the list  of properties specified in the value.
augmented_properties = None
# Dict[InterfaceTypeApiName, List[SharedPropertyTypeApiName]] | A map from interface type API name to a list of shared property type API names. For each returned object, if the object implements an interface that is a key in the map, then we augment the response for that object  type with the list of properties specified in the value.
augmented_shared_property_types = None
# List[InterfaceTypeApiName] | A list of interface type API names. Object types must implement all the mentioned interfaces in order to be  included in the response.
other_interface_types = None
# List[InterfacePropertyApiName] | A list of interface property type API names of the interface type that should be included in the response.  Omit this parameter to include all properties of the interface type in the response.
selected_interface_property_types = None
# List[ObjectTypeApiName] | A list of object type API names that should be included in the response. If non-empty, object types that are not mentioned will not be included in the response even if they implement the specified interface. Omit the  parameter to include all object types.
selected_object_types = None
# List[SharedPropertyTypeApiName] | A list of shared property type API names of the interface type that should be included in the response.  Omit this parameter to include all properties of the interface type in the response.
selected_shared_property_types = None
# Optional[FoundryBranch] | The Foundry branch to search objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[SearchOrderByV2]
order_by = None
# Optional[PageSize]
page_size = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SearchJsonQueryV2]
where = None


try:
    api_response = client.ontologies.OntologyInterface.search(
        ontology,
        interface_type,
        augmented_interface_property_types=augmented_interface_property_types,
        augmented_properties=augmented_properties,
        augmented_shared_property_types=augmented_shared_property_types,
        other_interface_types=other_interface_types,
        selected_interface_property_types=selected_interface_property_types,
        selected_object_types=selected_object_types,
        selected_shared_property_types=selected_shared_property_types,
        branch=branch,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        where=where,
    )
    print("The search response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyInterface.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

