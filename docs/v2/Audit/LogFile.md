# LogFile

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**content**](#content) | **GET** /v2/audit/organizations/{organizationRid}/logFiles/{logFileId}/content | Public Beta |
[**list**](#list) | **GET** /v2/audit/organizations/{organizationRid}/logFiles | Public Beta |

# **content**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**organization_rid** | OrganizationRid |  |  |
**log_file_id** | FileId |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OrganizationRid
organization_rid = None
# FileId
log_file_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.audit.Organization.LogFile.content(
        organization_rid, log_file_id, preview=preview
    )
    print("The content response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling LogFile.content: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all LogFiles.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**organization_rid** | OrganizationRid |  |  |
**end_date** | Optional[datetime] | List log files for audit events up until this date (inclusive). If absent, defaults to no end date. Use the returned `nextPageToken` to continually poll the  `listLogFiles` endpoint to list the latest available logs.  | [optional] |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**start_date** | Optional[datetime] | List log files for audit events starting from this date. If absent, defaults to the current date.  | [optional] |

### Return type
**ListLogFilesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OrganizationRid
organization_rid = None
# Optional[datetime] | List log files for audit events up until this date (inclusive). If absent, defaults to no end date. Use the returned `nextPageToken` to continually poll the  `listLogFiles` endpoint to list the latest available logs.
end_date = "2025-01-01"
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[datetime] | List log files for audit events starting from this date. If absent, defaults to the current date.
start_date = "2024-01-01"


try:
    for log_file in client.audit.Organization.LogFile.list(
        organization_rid,
        end_date=end_date,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        start_date=start_date,
    ):
        pprint(log_file)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling LogFile.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListLogFilesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

