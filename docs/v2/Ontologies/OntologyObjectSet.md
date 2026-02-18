# OntologyObjectSet

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**aggregate**](#aggregate) | **POST** /v2/ontologies/{ontology}/objectSets/aggregate | Stable |
[**create_temporary**](#create_temporary) | **POST** /v2/ontologies/{ontology}/objectSets/createTemporary | Public Beta |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/objectSets/{objectSetRid} | Private Beta |
[**load**](#load) | **POST** /v2/ontologies/{ontology}/objectSets/loadObjects | Stable |
[**load_links**](#load_links) | **POST** /v2/ontologies/{ontology}/objectSets/loadLinks | Private Beta |
[**load_multiple_object_types**](#load_multiple_object_types) | **POST** /v2/ontologies/{ontology}/objectSets/loadObjectsMultipleObjectTypes | Public Beta |
[**load_objects_or_interfaces**](#load_objects_or_interfaces) | **POST** /v2/ontologies/{ontology}/objectSets/loadObjectsOrInterfaces | Public Beta |

# **aggregate**
Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**aggregation** | List[AggregationV2] |  |  |
**group_by** | List[AggregationGroupByV2] |  |  |
**object_set** | ObjectSet |  |  |
**accuracy** | Optional[AggregationAccuracyRequest] |  | [optional] |
**branch** | Optional[FoundryBranch] | The Foundry branch to aggregate the objects from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**include_compute_usage** | Optional[IncludeComputeUsage] |  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The package version of the generated SDK.  | [optional] |
**transaction_id** | Optional[OntologyTransactionId] | The ID of an Ontology transaction to read from. Transactions are an experimental feature and all workflows may not be supported.  | [optional] |

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
# List[AggregationV2]
aggregation = [
    {"field": "tenure", "name": "min_tenure", "type": "min"},
    {"field": "tenure", "name": "avg_tenure", "type": "avg"},
]
# List[AggregationGroupByV2]
group_by = [
    {
        "field": "startDate",
        "ranges": [{"endValue": "2020-06-01", "startValue": "2020-01-01"}],
        "type": "range",
    },
    {"field": "city", "type": "exact"},
]
# ObjectSet
object_set = {"objectType": "Employee", "type": "base"}
# Optional[AggregationAccuracyRequest]
accuracy = None
# Optional[FoundryBranch] | The Foundry branch to aggregate the objects from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[IncludeComputeUsage]
include_compute_usage = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The package version of the generated SDK.
sdk_version = None
# Optional[OntologyTransactionId] | The ID of an Ontology transaction to read from. Transactions are an experimental feature and all workflows may not be supported.
transaction_id = None


try:
    api_response = client.ontologies.OntologyObjectSet.aggregate(
        ontology,
        aggregation=aggregation,
        group_by=group_by,
        object_set=object_set,
        accuracy=accuracy,
        branch=branch,
        include_compute_usage=include_compute_usage,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
        transaction_id=transaction_id,
    )
    print("The aggregate response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.aggregate: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AggregateObjectsResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **create_temporary**
Creates a temporary `ObjectSet` from the given definition. This `ObjectSet` expires after one hour.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_set** | ObjectSet |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to reference. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The package version of the generated SDK.  | [optional] |

### Return type
**CreateTemporaryObjectSetResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectSet
object_set = {"type": "base", "objectType": "Employee"}
# Optional[FoundryBranch] | The Foundry branch to reference. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The package version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.OntologyObjectSet.create_temporary(
        ontology,
        object_set=object_set,
        branch=branch,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
    )
    print("The create_temporary response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.create_temporary: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CreateTemporaryObjectSetResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Gets the definition of the `ObjectSet` with the given RID.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_set_rid** | ObjectSetRid | The RID of the object set.  |  |

### Return type
**ObjectSet**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectSetRid | The RID of the object set.
object_set_rid = "ri.object-set.main.object-set.c32ccba5-1a55-4cfe-ad71-160c4c77a053"


try:
    api_response = client.ontologies.OntologyObjectSet.get(ontology, object_set_rid)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ObjectSet  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **load**
Load the ontology objects present in the `ObjectSet` from the provided object set definition.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Note that null value properties will not be returned.

Vector properties will not be returned unless included in the `select` parameter.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_set** | ObjectSet |  |  |
**select** | List[SelectedPropertyApiName] |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the object set from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**exclude_rid** | Optional[bool] | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.  | [optional] |
**include_compute_usage** | Optional[IncludeComputeUsage] |  | [optional] |
**load_property_securities** | Optional[bool] | A flag to load the securities for all properties. Setting this flag to true will return a list of securities in the `propertySecurities` field of the response. Returned objects will return all properties as Secured Property Values, which provide the property data as well an index into the `propertySecurities` list. This feature is experimental and not yet generally available.  | [optional] |
**order_by** | Optional[SearchOrderByV2] |  | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The package version of the generated SDK.  | [optional] |
**select_v2** | Optional[List[PropertyIdentifier]] | The identifiers of the properties to include in the response. Only selectV2 or select should be populated, but not both.  | [optional] |
**snapshot** | Optional[bool] | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.  | [optional] |
**transaction_id** | Optional[OntologyTransactionId] | The ID of an Ontology transaction to read from. Transactions are an experimental feature and all workflows may not be supported.  | [optional] |

### Return type
**LoadObjectSetResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectSet
object_set = {"type": "base", "objectType": "Employee"}
# List[SelectedPropertyApiName]
select = None
# Optional[FoundryBranch] | The Foundry branch to load the object set from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[bool] | A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[IncludeComputeUsage]
include_compute_usage = None
# Optional[bool] | A flag to load the securities for all properties. Setting this flag to true will return a list of securities in the `propertySecurities` field of the response. Returned objects will return all properties as Secured Property Values, which provide the property data as well an index into the `propertySecurities` list. This feature is experimental and not yet generally available.
load_property_securities = None
# Optional[SearchOrderByV2]
order_by = None
# Optional[PageSize]
page_size = 10000
# Optional[PageToken]
page_token = "v1.QnVpbGQgdGhlIEZ1dHVyZTogaHR0cHM6Ly93d3cucGFsYW50aXIuY29tL2NhcmVlcnMvP2xldmVyLXNvdXJjZSU1YiU1ZD1BUElEb2NzI29wZW4tcG9zaXRpb25z"
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The package version of the generated SDK.
sdk_version = None
# Optional[List[PropertyIdentifier]] | The identifiers of the properties to include in the response. Only selectV2 or select should be populated, but not both.
select_v2 = None
# Optional[bool] | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.
snapshot = None
# Optional[OntologyTransactionId] | The ID of an Ontology transaction to read from. Transactions are an experimental feature and all workflows may not be supported.
transaction_id = None


try:
    api_response = client.ontologies.OntologyObjectSet.load(
        ontology,
        object_set=object_set,
        select=select,
        branch=branch,
        exclude_rid=exclude_rid,
        include_compute_usage=include_compute_usage,
        load_property_securities=load_property_securities,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
        select_v2=select_v2,
        snapshot=snapshot,
        transaction_id=transaction_id,
    )
    print("The load response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.load: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadObjectSetResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **load_links**
Loads the specified links from the defined object set. 

Links are defined as a link type API name and object locators for the source and target objects
where only the `__primaryKey` and `__apiName` properties are loaded.

Links are grouped by source object locator; however, the links for a given source object may be
split over multiple entries with the same source object locator.

Please keep these limitations in mind:
- Links returned may be stale. For example, primary keys returned by this endpoint may not exist anymore.
- This endpoint requests links for 1,000 objects at a time. If, for any page of 1,000 objects, there are more
  than 100,000 links present, results are limited to 100,000 links and should be considered partial.
- This endpoint does not support OSv1 links and will return an error if links provided are backed by OSv1.
- This endpoint currently does not support interface object sets or interface links, but support will be added in the near future.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**links** | List[LinkTypeApiName] |  |  |
**object_set** | ObjectSet |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to aggregate the objects from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**include_compute_usage** | Optional[IncludeComputeUsage] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The package version of the generated SDK.  | [optional] |

### Return type
**LoadObjectSetLinksResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# List[LinkTypeApiName]
links = None
# ObjectSet
object_set = {"objectType": "Employee", "type": "base"}
# Optional[FoundryBranch] | The Foundry branch to aggregate the objects from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[IncludeComputeUsage]
include_compute_usage = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The package version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.OntologyObjectSet.load_links(
        ontology,
        links=links,
        object_set=object_set,
        branch=branch,
        include_compute_usage=include_compute_usage,
        page_token=page_token,
        preview=preview,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
    )
    print("The load_links response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.load_links: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadObjectSetLinksResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **load_multiple_object_types**
Load the ontology objects present in the `ObjectSet` from the provided object set definition. The resulting 
objects may be scoped to an object type, in which all the selected properties on the object type are returned, or scoped 
to an interface, in which only the object type properties that implement the properties of any interfaces in its 
scope are returned. For objects that are scoped to an interface in the result, a mapping from interface to 
object implementation is returned in order to interpret the objects as the interfaces that they implement.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Note that null value properties will not be returned. In addition, property metadata (rid, apiName, and primaryKey)
will be prefixed with '$' instead of '__' as is the case in `loadObjects`.

Vector properties will not be returned unless included in the `select` parameter.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_set** | ObjectSet |  |  |
**select** | List[SelectedPropertyApiName] |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the object set for multiple object types. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**exclude_rid** | Optional[bool] | A flag to exclude the retrieval of the `$rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.  | [optional] |
**include_compute_usage** | Optional[IncludeComputeUsage] |  | [optional] |
**load_property_securities** | Optional[bool] | A flag to load the securities for all properties. Setting this flag to true will return a list of securities in the `propertySecurities` field of the response. Returned objects will return all properties as Secured Property Values, which provide the property data as well an index into the `propertySecurities` list. This feature is experimental and not yet generally available.  | [optional] |
**order_by** | Optional[SearchOrderByV2] |  | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The package version of the generated SDK.  | [optional] |
**select_v2** | Optional[List[PropertyIdentifier]] | The identifiers of the properties to include in the response. Only selectV2 or select should be populated, but not both.  | [optional] |
**snapshot** | Optional[bool] | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.  | [optional] |
**transaction_id** | Optional[OntologyTransactionId] | The ID of an Ontology transaction to read from. Transactions are an experimental feature and all workflows may not be supported.  | [optional] |

### Return type
**LoadObjectSetV2MultipleObjectTypesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectSet
object_set = {"type": "base", "objectType": "Employee"}
# List[SelectedPropertyApiName]
select = None
# Optional[FoundryBranch] | The Foundry branch to load the object set for multiple object types. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[bool] | A flag to exclude the retrieval of the `$rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[IncludeComputeUsage]
include_compute_usage = None
# Optional[bool] | A flag to load the securities for all properties. Setting this flag to true will return a list of securities in the `propertySecurities` field of the response. Returned objects will return all properties as Secured Property Values, which provide the property data as well an index into the `propertySecurities` list. This feature is experimental and not yet generally available.
load_property_securities = None
# Optional[SearchOrderByV2]
order_by = None
# Optional[PageSize]
page_size = 10000
# Optional[PageToken]
page_token = "v1.QnVpbGQgdGhlIEZ1dHVyZTogaHR0cHM6Ly93d3cucGFsYW50aXIuY29tL2NhcmVlcnMvP2xldmVyLXNvdXJjZSU1YiU1ZD1BUElEb2NzI29wZW4tcG9zaXRpb25z"
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The package version of the generated SDK.
sdk_version = None
# Optional[List[PropertyIdentifier]] | The identifiers of the properties to include in the response. Only selectV2 or select should be populated, but not both.
select_v2 = None
# Optional[bool] | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.
snapshot = None
# Optional[OntologyTransactionId] | The ID of an Ontology transaction to read from. Transactions are an experimental feature and all workflows may not be supported.
transaction_id = None


try:
    api_response = client.ontologies.OntologyObjectSet.load_multiple_object_types(
        ontology,
        object_set=object_set,
        select=select,
        branch=branch,
        exclude_rid=exclude_rid,
        include_compute_usage=include_compute_usage,
        load_property_securities=load_property_securities,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
        select_v2=select_v2,
        snapshot=snapshot,
        transaction_id=transaction_id,
    )
    print("The load_multiple_object_types response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.load_multiple_object_types: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadObjectSetV2MultipleObjectTypesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **load_objects_or_interfaces**
Load the ontology objects present in the `ObjectSet` from the provided object set definition. If the requested 
object set contains interfaces and the object can be viewed as an interface, it will contain the properties 
defined by the interface. If not, it will contain the properties defined by its object type. This allows directly
loading all objects of an interface where all objects are viewed as the interface, for example.

Note that the result object set cannot contain a mix of objects with "interface" properties and "object type"
properties. Attempting to load an object set like this will result in an error.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Note that null value properties will not be returned. In addition, property metadata (rid, apiName, and primaryKey)
will be prefixed with '$' instead of '__' as is the case in `/loadObjects`.

Vector properties will not be returned unless included in the `select` parameter.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_set** | ObjectSet |  |  |
**select** | List[SelectedPropertyApiName] |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the objects or interfaces from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**exclude_rid** | Optional[bool] | A flag to exclude the retrieval of the `$rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.  | [optional] |
**order_by** | Optional[SearchOrderByV2] |  | [optional] |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The package version of the generated SDK.  | [optional] |
**select_v2** | Optional[List[PropertyIdentifier]] | The identifiers of the properties to include in the response. Only selectV2 or select should be populated, but not both.  | [optional] |
**snapshot** | Optional[bool] | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.  | [optional] |

### Return type
**LoadObjectSetV2ObjectsOrInterfacesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectSet
object_set = {"type": "interfaceBase", "interfaceType": "Person"}
# List[SelectedPropertyApiName]
select = None
# Optional[FoundryBranch] | The Foundry branch to load the objects or interfaces from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[bool] | A flag to exclude the retrieval of the `$rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
exclude_rid = None
# Optional[SearchOrderByV2]
order_by = None
# Optional[PageSize]
page_size = 10000
# Optional[PageToken]
page_token = "v1.VGhlcmUgaXMgc28gbXVjaCBsZWZ0IHRvIGJ1aWxkIC0gcGFsYW50aXIuY29tL2NhcmVlcnMv"
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The package version of the generated SDK.
sdk_version = None
# Optional[List[PropertyIdentifier]] | The identifiers of the properties to include in the response. Only selectV2 or select should be populated, but not both.
select_v2 = None
# Optional[bool] | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results.
snapshot = None


try:
    api_response = client.ontologies.OntologyObjectSet.load_objects_or_interfaces(
        ontology,
        object_set=object_set,
        select=select,
        branch=branch,
        exclude_rid=exclude_rid,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
        select_v2=select_v2,
        snapshot=snapshot,
    )
    print("The load_objects_or_interfaces response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyObjectSet.load_objects_or_interfaces: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadObjectSetV2ObjectsOrInterfacesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

