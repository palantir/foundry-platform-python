# Release

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**delete**](#delete) | **DELETE** /v2/widgets/widgetSets/{widgetSetRid}/releases/{releaseVersion} | Private Beta |
[**get**](#get) | **GET** /v2/widgets/widgetSets/{widgetSetRid}/releases/{releaseVersion} | Private Beta |
[**list**](#list) | **GET** /v2/widgets/widgetSets/{widgetSetRid}/releases | Private Beta |

# **delete**
Delete the Release with the specified version.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**widget_set_rid** | WidgetSetRid | A Resource Identifier (RID) identifying a widget set. |  |
**release_version** | ReleaseVersion | The semantic version of the widget set. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# WidgetSetRid | A Resource Identifier (RID) identifying a widget set.
widget_set_rid = "ri.widgetregistry..widget-set.21dt2c42-b7df-4b23-880b-1436a3dred2e"
# ReleaseVersion | The semantic version of the widget set.
release_version = "1.2.0"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.widgets.WidgetSet.Release.delete(
        widget_set_rid, release_version, preview=preview
    )
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Release.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Release with the specified version.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**widget_set_rid** | WidgetSetRid | A Resource Identifier (RID) identifying a widget set. |  |
**release_version** | ReleaseVersion | The semantic version of the widget set. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Release**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# WidgetSetRid | A Resource Identifier (RID) identifying a widget set.
widget_set_rid = "ri.widgetregistry..widget-set.21dt2c42-b7df-4b23-880b-1436a3dred2e"
# ReleaseVersion | The semantic version of the widget set.
release_version = "1.2.0"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.widgets.WidgetSet.Release.get(
        widget_set_rid, release_version, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Release.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Release  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all Releases.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**widget_set_rid** | WidgetSetRid | A Resource Identifier (RID) identifying a widget set. |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListReleasesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# WidgetSetRid | A Resource Identifier (RID) identifying a widget set.
widget_set_rid = "ri.widgetregistry..widget-set.21dt2c42-b7df-4b23-880b-1436a3dred2e"
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for release in client.widgets.WidgetSet.Release.list(
        widget_set_rid, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(release)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Release.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListReleasesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

