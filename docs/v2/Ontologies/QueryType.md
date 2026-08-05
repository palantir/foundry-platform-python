# QueryType

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/ontologies/{ontology}/queryTypes/{queryApiName} | Stable |
[**get_by_rid_batch**](#get_by_rid_batch) | **POST** /v2/ontologies/{ontology}/queryTypes/getByRidBatch | Private Beta |
[**list**](#list) | **GET** /v2/ontologies/{ontology}/queryTypes | Stable |

# **get**
Gets a specific query type with the given API name.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**query_api_name** | QueryApiName | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.  |  |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |
**version** | Optional[FunctionVersion] | The version of the Query to get. If not specified, the latest version is used. The latest version is the one that was most recently published, including pre-release versions.  | [optional] |

### Return type
**QueryTypeV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# QueryApiName | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**.
query_api_name = "getEmployeesInCity"
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None
# Optional[FunctionVersion] | The version of the Query to get. If not specified, the latest version is used. The latest version is the one that was most recently published, including pre-release versions.
version = None


try:
    api_response = client.ontologies.Ontology.QueryType.get(
        ontology,
        query_api_name,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
        version=version,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling QueryType.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | QueryTypeV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_by_rid_batch**
Gets a list of query types by RID in bulk.

Query types are filtered from the response if they don't exist or the requesting token lacks the required
permissions.

The maximum batch size for this endpoint is 100.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**requests** | List[GetQueryTypeByRidBatchRequestElement] |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to load the query type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**GetQueryTypeByRidBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# List[GetQueryTypeByRidBatchRequestElement]
requests = None
# Optional[FoundryBranch] | The Foundry branch to load the query type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.Ontology.QueryType.get_by_rid_batch(
        ontology, requests=requests, branch=branch, preview=preview
    )
    print("The get_by_rid_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling QueryType.get_by_rid_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetQueryTypeByRidBatchResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists the query types for the given Ontology.

Each query type is returned at its latest version. The latest version is the one that was most recently
published, which may be a pre-release version.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to list queries from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.  | [optional] |
**page_size** | Optional[PageSize] | The desired size of the page to be returned. Defaults to 100. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**ListQueryTypesResponseV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# Optional[FoundryBranch] | The Foundry branch to list queries from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
branch = None
# Optional[PageSize] | The desired size of the page to be returned. Defaults to 100. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
page_size = None
# Optional[PageToken]
page_token = None


try:
    for query_type in client.ontologies.Ontology.QueryType.list(
        ontology, branch=branch, page_size=page_size, page_token=page_token
    ):
        pprint(query_type)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling QueryType.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListQueryTypesResponseV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

