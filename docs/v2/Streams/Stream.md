# Stream

Method | HTTP request |
------------- | ------------- |

Get a stream by its branch name. If the branch does not exist, there is no stream on that branch, or the
user does not have permission to access the stream, a 404 error will be returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**stream_branch_name** | BranchName | streamBranchName |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Stream**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = None
# BranchName | streamBranchName
stream_branch_name = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.streams.Dataset.Stream.get(
        dataset_rid,
        stream_branch_name,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Stream.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Stream  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Publish a single record to the stream. The record will be validated against the stream's schema, and
rejected if it is invalid.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**stream_branch_name** | BranchName | streamBranchName |  |
**record** | Record | The record to publish to the stream  |  |
**preview** | Optional[PreviewMode] | preview | [optional] |
**view_rid** | Optional[ViewRid] | If provided, this endpoint will only write to the stream corresponding to the specified view rid. If not provided, this endpoint will write the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.  | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = None
# BranchName | streamBranchName
stream_branch_name = None
# Record | The record to publish to the stream
record = None
# Optional[PreviewMode] | preview
preview = None
# Optional[ViewRid] | If provided, this endpoint will only write to the stream corresponding to the specified view rid. If not provided, this endpoint will write the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.
view_rid = None


try:
    api_response = foundry_client.streams.Dataset.Stream.publish_record(
        dataset_rid,
        stream_branch_name,
        record=record,
        preview=preview,
        view_rid=view_rid,
    )
    print("The publish_record response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Stream.publish_record: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Publish a batch of records to the stream. The records will be validated against the stream's schema, and
the batch will be rejected if one or more of the records are invalid.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**stream_branch_name** | BranchName | streamBranchName |  |
**records** | List[Record] | The records to publish to the stream  |  |
**preview** | Optional[PreviewMode] | preview | [optional] |
**view_rid** | Optional[ViewRid] | If provided, this endpoint will only write to the stream corresponding to the specified view rid. If not provided, this endpoint will write to the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.  | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = None
# BranchName | streamBranchName
stream_branch_name = None
# List[Record] | The records to publish to the stream
records = None
# Optional[PreviewMode] | preview
preview = None
# Optional[ViewRid] | If provided, this endpoint will only write to the stream corresponding to the specified view rid. If not provided, this endpoint will write to the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.
view_rid = None


try:
    api_response = foundry_client.streams.Dataset.Stream.publish_records(
        dataset_rid,
        stream_branch_name,
        records=records,
        preview=preview,
        view_rid=view_rid,
    )
    print("The publish_records response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Stream.publish_records: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

