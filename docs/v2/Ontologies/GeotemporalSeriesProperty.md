# GeotemporalSeriesProperty

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get_geotemporal_series_latest_value**](#get_geotemporal_series_latest_value) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{propertyName}/latestValue | Private Beta |
[**stream_geotemporal_series_historic_values**](#stream_geotemporal_series_historic_values) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{propertyName}/streamHistoricValues | Private Beta |

# **get_geotemporal_series_latest_value**
Get the latest recorded location for a geotemporal series reference property.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object with the geotemporal series property.  |  |
**property_name** | PropertyApiName | The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |

### Return type
**Optional[GeotemporalSeriesEntry]**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "airplane"
# PropertyValueEscapedString | The primary key of the object with the geotemporal series property.
primary_key = "XYZ123"
# PropertyApiName | The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint.
property_name = "locationHistory"
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.GeotemporalSeriesProperty.get_geotemporal_series_latest_value(
        ontology,
        object_type,
        primary_key,
        property_name,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
    )
    print("The get_geotemporal_series_latest_value response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print(
        "HTTP error when calling GeotemporalSeriesProperty.get_geotemporal_series_latest_value: %s\n"
        % e
    )

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Optional[GeotemporalSeriesEntry]  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **stream_geotemporal_series_historic_values**
Stream historic points of a geotemporal series reference property.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object with the geotemporal series property.  |  |
**property_name** | PropertyApiName | The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**range** | Optional[TimeRange] |  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "airplane"
# PropertyValueEscapedString | The primary key of the object with the geotemporal series property.
primary_key = "XYZ123"
# PropertyApiName | The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint.
property_name = "locationHistory"
# Optional[TimeRange]
range = {
    "type": "relative",
    "startTime": {"when": "BEFORE", "value": 5, "unit": "MONTHS"},
    "endTime": {"when": "BEFORE", "value": 1, "unit": "MONTHS"},
}
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None


try:
    api_response = (
        client.ontologies.GeotemporalSeriesProperty.stream_geotemporal_series_historic_values(
            ontology,
            object_type,
            primary_key,
            property_name,
            range=range,
            sdk_package_rid=sdk_package_rid,
            sdk_version=sdk_version,
        )
    )
    print("The stream_geotemporal_series_historic_values response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print(
        "HTTP error when calling GeotemporalSeriesProperty.stream_geotemporal_series_historic_values: %s\n"
        % e
    )

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | Success response. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

