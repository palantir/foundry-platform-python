# TimeSeriesPropertyV2

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get_first_point**](#get_first_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/firstPoint | Stable |
[**get_last_point**](#get_last_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/lastPoint | Stable |
[**stream_points**](#stream_points) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamPoints | Stable |

# **get_first_point**
Get the first point of a time series property.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object with the time series property.  |  |
**property** | PropertyApiName | The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |

### Return type
**Optional[TimeSeriesPoint]**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the object with the time series property.
primary_key = 50030
# PropertyApiName | The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.
property = "performance"
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[SdkPackageName] | The package name of the generated SDK.
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
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling TimeSeriesPropertyV2.get_first_point: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Optional[TimeSeriesPoint]  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_last_point**
Get the last point of a time series property.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object with the time series property.  |  |
**property** | PropertyApiName | The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |

### Return type
**Optional[TimeSeriesPoint]**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the object with the time series property.
primary_key = 50030
# PropertyApiName | The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.
property = "performance"
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[SdkPackageName] | The package name of the generated SDK.
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
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling TimeSeriesPropertyV2.get_last_point: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Optional[TimeSeriesPoint]  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **stream_points**
Stream all of the points of a time series property.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object with the time series property.  |  |
**property** | PropertyApiName | The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**aggregate** | Optional[AggregateTimeSeries] |  | [optional] |
**artifact_repository** | Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.  | [optional] |
**format** | Optional[StreamingOutputFormat] | The output format to serialize the output binary stream in. Default is JSON. ARROW is more efficient than JSON at streaming a large sized response.  | [optional] |
**package_name** | Optional[SdkPackageName] | The package name of the generated SDK.  | [optional] |
**range** | Optional[TimeRange] |  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier | The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the object with the time series property.
primary_key = 50030
# PropertyApiName | The API name of the time series property. To find the API name for your time series property, check the **Ontology Manager** or use the **Get object type** endpoint.
property = None
# Optional[AggregateTimeSeries]
aggregate = None
# Optional[ArtifactRepositoryRid] | The repository associated with a marketplace installation.
artifact_repository = None
# Optional[StreamingOutputFormat] | The output format to serialize the output binary stream in. Default is JSON. ARROW is more efficient than JSON at streaming a large sized response.
format = None
# Optional[SdkPackageName] | The package name of the generated SDK.
package_name = None
# Optional[TimeRange]
range = {
    "type": "relative",
    "startTime": {"when": "BEFORE", "value": 5, "unit": "MONTHS"},
    "endTime": {"when": "BEFORE", "value": 1, "unit": "MONTHS"},
}


try:
    api_response = foundry_client.ontologies.TimeSeriesPropertyV2.stream_points(
        ontology,
        object_type,
        primary_key,
        property,
        aggregate=aggregate,
        artifact_repository=artifact_repository,
        format=format,
        package_name=package_name,
        range=range,
    )
    print("The stream_points response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling TimeSeriesPropertyV2.stream_points: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | Success response. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

