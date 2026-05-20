# GeotemporalSeriesProperty

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**load_geotemporal_series_entries**](#load_geotemporal_series_entries) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{property}/loadEntries | Private Beta |

# **load_geotemporal_series_entries**
Load the geotemporal series entries for a given object's geotemporal series reference property within the
specified time range.

Each entry in the response is a map of property names to values, following the same structure as
`OntologyObjectV2`. Use the `additionalProperties` field in the request to control which properties are included
in each entry depending on the underlying geotemporal integration.

Results are paginated. Use the `nextPageToken` from the response to retrieve subsequent pages.

:::callout{theme=warning title=Warning}
  Geotemporal series integrations with only "dataset archive" enabled are not supported.
:::


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object with the geotemporal series property.  |  |
**property** | PropertyApiName | The API name of the geotemporal series property. To find the API name for your property, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**additional_properties** | List[SelectedPropertyApiName] | The additional property API names to include in each entry. The "time" and "position" properties are always included and do not need to be specified here. Use this to request additional geotemporal series metadata properties such as "speed" or "heading". Properties that are not available for the underlying geotemporal integration will be omitted from the response entries.  |  |
**range** | AbsoluteTimeRange |  |  |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package RID of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |

### Return type
**LoadGeotemporalSeriesResponse**

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
property = "locationHistory"
# List[SelectedPropertyApiName] | The additional property API names to include in each entry. The "time" and "position" properties are always included and do not need to be specified here. Use this to request additional geotemporal series metadata properties such as "speed" or "heading". Properties that are not available for the underlying geotemporal integration will be omitted from the response entries.
additional_properties = ["speed", "heading"]
# AbsoluteTimeRange
range = {"startTime": "2020-01-01T00:00:00Z", "endTime": "2020-06-01T00:00:00Z"}
# Optional[PageSize]
page_size = 100
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SdkPackageRid] | The package RID of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.GeotemporalSeriesProperty.load_geotemporal_series_entries(
        ontology,
        object_type,
        primary_key,
        property,
        additional_properties=additional_properties,
        range=range,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
    )
    print("The load_geotemporal_series_entries response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print(
        "HTTP error when calling GeotemporalSeriesProperty.load_geotemporal_series_entries: %s\n"
        % e
    )

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadGeotemporalSeriesResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

