# Stream

Method | HTTP request |
------------- | ------------- |

Creates a new branch on the backing streaming dataset, and creates a new stream on that branch.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**branch_name** | BranchName |  |  |
**schema** | CreateStreamRequestStreamSchemaDict | The Foundry schema for this stream. |  |
**compressed** | Optional[Compressed] | Whether or not compression is enabled for the stream. Defaults to false.  | [optional] |
**partitions_count** | Optional[PartitionsCount] | The number of partitions for the Foundry stream. Defaults to 1.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**stream_type** | Optional[StreamType] | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.  | [optional] |

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
# BranchName |
branch_name = "master"
# CreateStreamRequestStreamSchemaDict | The Foundry schema for this stream.
schema = None
# Optional[Compressed] | Whether or not compression is enabled for the stream. Defaults to false.
compressed = None
# Optional[PartitionsCount] | The number of partitions for the Foundry stream. Defaults to 1.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.
partitions_count = 1
# Optional[PreviewMode] | preview
preview = None
# Optional[StreamType] | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
stream_type = "LOW_LATENCY"


try:
    api_response = foundry_client.streams.Dataset.Stream.create(
        dataset_rid,
        branch_name=branch_name,
        schema=schema,
        compressed=compressed,
        partitions_count=partitions_count,
        preview=preview,
        stream_type=stream_type,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Stream.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Stream  | The created Stream | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

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

Publish a single binary record to the stream. The stream's schema must be a single binary field.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**stream_branch_name** | BranchName | streamBranchName |  |
**body** | bytes | The binary record to publish to the stream  |  |
**preview** | Optional[PreviewMode] | preview | [optional] |
**view_rid** | Optional[ViewRid] | viewRid | [optional] |

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
# bytes | The binary record to publish to the stream
body = None
# Optional[PreviewMode] | preview
preview = None
# Optional[ViewRid] | viewRid
view_rid = None


try:
    api_response = foundry_client.streams.Dataset.Stream.publish_binary_record(
        dataset_rid,
        stream_branch_name,
        body,
        preview=preview,
        view_rid=view_rid,
    )
    print("The publish_binary_record response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Stream.publish_binary_record: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

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

Reset the stream on the given dataset branch, clearing the existing records and allowing new configurations
to be applied.

To change the stream settings without clearing the records, update the stream settings in-platform.

This will create a new stream view (as seen by the change of the `viewRid` on the branch),
which will be the new stream view that will be written to for the branch.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | datasetRid |  |
**stream_branch_name** | BranchName | streamBranchName |  |
**compressed** | Optional[Compressed] | Whether or not compression is enabled for the stream.  If omitted, the compression setting of the existing stream on the branch will be used.  | [optional] |
**partitions_count** | Optional[PartitionsCount] | The number of partitions for the Foundry stream. Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If omitted, the partitions count of the existing stream on the branch will be used.  | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**schema** | Optional[StreamSchemaDict] | The Foundry schema to apply to the new stream.   If omitted, the schema of the existing stream on the branch will be used.  | [optional] |
**stream_type** | Optional[StreamType] | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.  If omitted, the stream type of the existing stream on the branch will be used.  | [optional] |

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
# Optional[Compressed] | Whether or not compression is enabled for the stream.  If omitted, the compression setting of the existing stream on the branch will be used.
compressed = None
# Optional[PartitionsCount] | The number of partitions for the Foundry stream. Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If omitted, the partitions count of the existing stream on the branch will be used.
partitions_count = None
# Optional[PreviewMode] | preview
preview = None
# Optional[StreamSchemaDict] | The Foundry schema to apply to the new stream.   If omitted, the schema of the existing stream on the branch will be used.
schema = None
# Optional[StreamType] | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.  If omitted, the stream type of the existing stream on the branch will be used.
stream_type = "LOW_LATENCY"


try:
    api_response = foundry_client.streams.Dataset.Stream.reset(
        dataset_rid,
        stream_branch_name,
        compressed=compressed,
        partitions_count=partitions_count,
        preview=preview,
        schema=schema,
        stream_type=stream_type,
    )
    print("The reset response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Stream.reset: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Stream  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

