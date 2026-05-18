# Record

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/checkpoints/records/{recordRid} | Public Beta |
[**get_batch**](#get_batch) | **POST** /v2/checkpoints/records/getBatch | Public Beta |
[**search**](#search) | **POST** /v2/checkpoints/records/search | Public Beta |

# **get**
Retrieve a single checkpoint record by id.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**record_rid** | RecordRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Record**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# RecordRid
record_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.checkpoints.Record.get(record_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Record.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Record  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_batch**
Fetch multiple checkpoint records in a single request. Records not found
or inaccessible to the user will be omitted from the response.


The maximum batch size for this endpoint is 100.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[GetRecordsBatchRequestElement] | Body of the request |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GetRecordsBatchResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[GetRecordsBatchRequestElement] | Body of the request
body = [{"recordRid": "ri.checkpoints.main.checkpoint.a1b2c3d4-e5f6-7890-abcd-ef1234567890"}]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.checkpoints.Record.get_batch(body, preview=preview)
    print("The get_batch response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Record.get_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetRecordsBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **search**
Search for checkpoint records.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**where** | SearchCheckpointRecordsRequest |  |  |
**page_size** | Optional[PageSize] | The page size for the search request. If no value is provided, a default of `100` will be used.  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**sort_direction** | Optional[SortDirection] | Chronological order of creation time for records to be returned in. Defaults to reverse chronological order (DESC).  | [optional] |

### Return type
**SearchCheckpointRecordsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# SearchCheckpointRecordsRequest
where = {"filter": {"type": "eq", "field": "checkpointType", "value": "CONTOUR_EXPORT"}}
# Optional[PageSize] | The page size for the search request. If no value is provided, a default of `100` will be used.
page_size = 100
# Optional[PageToken]
page_token = "v1.QnVpbGQgdGhlIEZ1dHVyZTogaHR0cHM6Ly93d3cucGFsYW50aXIuY29tL2NhcmVlcnMvP2xldmVyLXNvdXJjZSU1YiU1ZD1BUElEb2NzI29wZW4tcG9zaXRpb25z"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[SortDirection] | Chronological order of creation time for records to be returned in. Defaults to reverse chronological order (DESC).
sort_direction = "DESC"


try:
    api_response = client.checkpoints.Record.search(
        where=where,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        sort_direction=sort_direction,
    )
    print("The search response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Record.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchCheckpointRecordsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

