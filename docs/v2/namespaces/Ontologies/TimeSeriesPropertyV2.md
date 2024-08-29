# TimeSeriesPropertyV2

Method | HTTP request |
------------- | ------------- |
[**get_first_point**](#get_first_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/firstPoint |
[**get_last_point**](#get_last_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/lastPoint |
[**stream_points**](#stream_points) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamPoints |

# **get_first_point**
Get the first point of a time series property.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**property** | PropertyApiName | property |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**TimeSeriesPoint**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"

# ObjectTypeApiName | objectType
object_type = "employee"

# PropertyValueEscapedString | primaryKey
primary_key = 50030

# PropertyApiName | property
property = "performance"

# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None

# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.TimeSeriesPropertyV2.get_first_point(
        ontology,
        object_type,
        primary_key,
        property,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The get_first_point response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling TimeSeriesPropertyV2.get_first_point: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | TimeSeriesPoint  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **get_last_point**
Get the last point of a time series property.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**property** | PropertyApiName | property |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**TimeSeriesPoint**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"

# ObjectTypeApiName | objectType
object_type = "employee"

# PropertyValueEscapedString | primaryKey
primary_key = 50030

# PropertyApiName | property
property = "performance"

# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None

# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.TimeSeriesPropertyV2.get_last_point(
        ontology,
        object_type,
        primary_key,
        property,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The get_last_point response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling TimeSeriesPropertyV2.get_last_point: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | TimeSeriesPoint  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

# **stream_points**
Stream all of the points of a time series property.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | ontology |  |
**object_type** | ObjectTypeApiName | objectType |  |
**primary_key** | PropertyValueEscapedString | primaryKey |  |
**property** | PropertyApiName | property |  |
**stream_time_series_points_request** | Union[StreamTimeSeriesPointsRequest, StreamTimeSeriesPointsRequestDict] | Body of the request |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | artifactRepository | [optional] |
**package_name** | Optional[SdkPackageName] | packageName | [optional] |

### Return type
**bytes**

### Example

```python
from foundry.v2 import FoundryV2Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV2Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyIdentifier | ontology
ontology = "palantir"

# ObjectTypeApiName | objectType
object_type = "employee"

# PropertyValueEscapedString | primaryKey
primary_key = 50030

# PropertyApiName | property
property = None

# Union[StreamTimeSeriesPointsRequest, StreamTimeSeriesPointsRequestDict] | Body of the request
stream_time_series_points_request = {
    "range": {
        "type": "relative",
        "startTime": {"when": "BEFORE", "value": 5, "unit": "MONTHS"},
        "endTime": {"when": "BEFORE", "value": 1, "unit": "MONTHS"},
    }
}

# Optional[ArtifactRepositoryRid] | artifactRepository
artifact_repository = None

# Optional[SdkPackageName] | packageName
package_name = None


try:
    api_response = foundry_client.ontologies.TimeSeriesPropertyV2.stream_points(
        ontology,
        object_type,
        primary_key,
        property,
        stream_time_series_points_request,
        artifact_repository=artifact_repository,
        package_name=package_name,
    )
    print("The stream_points response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling TimeSeriesPropertyV2.stream_points: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | Success response. | */* |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v2-link) [[Back to README]](../../../../README.md)

