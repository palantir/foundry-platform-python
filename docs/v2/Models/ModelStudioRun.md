# ModelStudioRun

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**list**](#list) | **GET** /v2/models/modelStudios/{modelStudioRid}/runs | Private Beta |

# **list**
Lists all runs for a Model Studio.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_studio_rid** | ModelStudioRid |  |  |
**config_version** | Optional[ModelStudioConfigVersionNumber] | Filter runs by configuration version. | [optional] |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListModelStudioRunsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelStudioRid
model_studio_rid = None
# Optional[ModelStudioConfigVersionNumber] | Filter runs by configuration version.
config_version = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for model_studio_run in client.models.ModelStudio.Run.list(
        model_studio_rid,
        config_version=config_version,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(model_studio_run)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Run.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListModelStudioRunsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

