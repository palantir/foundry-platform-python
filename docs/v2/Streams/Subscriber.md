# Subscriber

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**commit_offsets**](#commit_offsets) | **POST** /v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/commitOffsets | Private Beta |
[**create**](#create) | **POST** /v2/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers | Private Beta |
[**delete**](#delete) | **DELETE** /v2/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId} | Private Beta |
[**get_read_position**](#get_read_position) | **GET** /v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/getReadPosition | Private Beta |
[**read_records**](#read_records) | **POST** /v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/readRecords | Private Beta |
[**reset_offsets**](#reset_offsets) | **POST** /v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/resetOffsets | Private Beta |

# **commit_offsets**
Explicitly commit offsets for a subscriber. Required when `autoCommit` is false.

Pass the last offset you processed for each partition.

For example, if you processed a record at offset 50, commit `{"0": 50}` and the next
read from partition "0" will start at offset 51.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**stream_branch_name** | BranchName |  |  |
**subscriber_subscriber_id** | SubscriberId |  |  |
**offsets** | PartitionOffsets | The last processed offset for each partition. The server will store these as read positions (offset + 1), so the next read starts after the committed offset.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**view_rid** | Optional[ViewRid] | The view RID to commit offsets for. If not provided, uses the latest view for the dataset/branch.  | [optional] |

### Return type
**PartitionOffsets**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# BranchName
stream_branch_name = None
# SubscriberId
subscriber_subscriber_id = None
# PartitionOffsets | The last processed offset for each partition. The server will store these as read positions (offset + 1), so the next read starts after the committed offset.
offsets = {"0": 50, "1": 75}
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[ViewRid] | The view RID to commit offsets for. If not provided, uses the latest view for the dataset/branch.
view_rid = "ri.foundry-streaming.main.view.ecd4f0f6-8526-4468-9eda-14939449ad79"


try:
    api_response = client.streams.Dataset.Stream.Subscriber.commit_offsets(
        dataset_rid,
        stream_branch_name,
        subscriber_subscriber_id,
        offsets=offsets,
        preview=preview,
        view_rid=view_rid,
    )
    print("The commit_offsets response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Subscriber.commit_offsets: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | PartitionOffsets  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **create**
Register a new subscriber for a stream. Subscribers maintain server-side offset tracking,
allowing reliable consumption without client-side state management.

If a subscriber with the same ID already exists for this stream, the existing registration
is returned. If a subscriber with the same ID exists for a different stream, an error is returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**stream_branch_name** | BranchName |  |  |
**subscriber_id** | SubscriberId |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**read_position** | Optional[ReadPosition] | Where to start reading from. Defaults to `earliest` if not specified.  The `readPosition` determines where the subscriber will start reading: - `earliest`: Start from the beginning of each partition (offset 0). Use this to process   all historical data. - `latest`: Start from the current end of each partition. Use this to skip historical data   and only process new records arriving after registration. - `specific`: Start from explicit offsets for each partition. Use this to resume from a   known checkpoint.  | [optional] |

### Return type
**Subscriber**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# BranchName
stream_branch_name = None
# SubscriberId
subscriber_id = "my-subscriber-001"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[ReadPosition] | Where to start reading from. Defaults to `earliest` if not specified.  The `readPosition` determines where the subscriber will start reading: - `earliest`: Start from the beginning of each partition (offset 0). Use this to process   all historical data. - `latest`: Start from the current end of each partition. Use this to skip historical data   and only process new records arriving after registration. - `specific`: Start from explicit offsets for each partition. Use this to resume from a   known checkpoint.
read_position = None


try:
    api_response = client.streams.Dataset.Stream.Subscriber.create(
        dataset_rid,
        stream_branch_name,
        subscriber_id=subscriber_id,
        preview=preview,
        read_position=read_position,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Subscriber.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Subscriber  | The created Subscriber | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **delete**
Delete a subscriber and all its committed offset state. After deletion, the subscriber ID
can be reused to create a new subscriber.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**stream_branch_name** | BranchName |  |  |
**subscriber_subscriber_id** | SubscriberId |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# BranchName
stream_branch_name = None
# SubscriberId
subscriber_subscriber_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.streams.Dataset.Stream.Subscriber.delete(
        dataset_rid, stream_branch_name, subscriber_subscriber_id, preview=preview
    )
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Subscriber.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_read_position**
Get the current read position for a subscriber. Returns the offset per partition where the next read 
will begin.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**stream_branch_name** | BranchName |  |  |
**subscriber_subscriber_id** | SubscriberId |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**view_rid** | Optional[ViewRid] | The view RID to get positions for. If not provided, uses the latest view for the dataset/branch.  | [optional] |

### Return type
**PartitionOffsets**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# BranchName
stream_branch_name = None
# SubscriberId
subscriber_subscriber_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[ViewRid] | The view RID to get positions for. If not provided, uses the latest view for the dataset/branch.
view_rid = None


try:
    api_response = client.streams.Dataset.Stream.Subscriber.get_read_position(
        dataset_rid,
        stream_branch_name,
        subscriber_subscriber_id,
        preview=preview,
        view_rid=view_rid,
    )
    print("The get_read_position response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Subscriber.get_read_position: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | PartitionOffsets  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **read_records**
Fetch records for a subscriber starting from their committed offset. Returns records
grouped by partition.

If `autoCommit` is true, offsets are automatically committed after the records are
fetched, so the next read will start from where this one left off.

If `autoCommit` is false, you must call `commitOffsets` to update the read position.
Use manual commits for at-least-once processing where you need to ensure records are
processed before acknowledging them.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**stream_branch_name** | BranchName |  |  |
**subscriber_subscriber_id** | SubscriberId |  |  |
**auto_commit** | Optional[bool] | If true, the read position is automatically committed after reading records. The committed position will be the offset after the last record read. If false, you must call the `commitOffsets` endpoint to commit offsets. Defaults to false.  | [optional] |
**limit** | Optional[int] | Maximum number of records to return across all partitions. Defaults to 100, max 1000. If a value  greater than 1000 is requested, only 1000 records will be returned.  | [optional] |
**partition_ids** | Optional[List[PartitionId]] | If specified, only read from these partitions. Otherwise, read from all partitions.  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**view_rid** | Optional[ViewRid] | The view RID to read from. If not provided, reads from the latest view for the dataset/branch.  | [optional] |

### Return type
**ReadSubscriberRecordsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# BranchName
stream_branch_name = None
# SubscriberId
subscriber_subscriber_id = None
# Optional[bool] | If true, the read position is automatically committed after reading records. The committed position will be the offset after the last record read. If false, you must call the `commitOffsets` endpoint to commit offsets. Defaults to false.
auto_commit = None
# Optional[int] | Maximum number of records to return across all partitions. Defaults to 100, max 1000. If a value  greater than 1000 is requested, only 1000 records will be returned.
limit = None
# Optional[List[PartitionId]] | If specified, only read from these partitions. Otherwise, read from all partitions.
partition_ids = ["0"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[ViewRid] | The view RID to read from. If not provided, reads from the latest view for the dataset/branch.
view_rid = "ri.foundry-streaming.main.view.ecd4f0f6-8526-4468-9eda-14939449ad79"


try:
    api_response = client.streams.Dataset.Stream.Subscriber.read_records(
        dataset_rid,
        stream_branch_name,
        subscriber_subscriber_id,
        auto_commit=auto_commit,
        limit=limit,
        partition_ids=partition_ids,
        preview=preview,
        view_rid=view_rid,
    )
    print("The read_records response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Subscriber.read_records: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ReadSubscriberRecordsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **reset_offsets**
Reset subscriber offsets to a specific position. Use this to replay data from the
beginning, skip to the latest records, or jump to specific offsets.

The `position` parameter determines where reading will resume:
- `earliest`: Reset to the beginning of each partition (offset 0)
- `latest`: Reset to the current end of each partition
- `specific`: Reset to explicit offsets for each partition


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid |  |  |
**stream_branch_name** | BranchName |  |  |
**subscriber_subscriber_id** | SubscriberId |  |  |
**position** | ReadPosition | The position to reset offsets to.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**PartitionOffsets**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# BranchName
stream_branch_name = None
# SubscriberId
subscriber_subscriber_id = None
# ReadPosition | The position to reset offsets to.
position = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.streams.Dataset.Stream.Subscriber.reset_offsets(
        dataset_rid,
        stream_branch_name,
        subscriber_subscriber_id,
        position=position,
        preview=preview,
    )
    print("The reset_offsets response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Subscriber.reset_offsets: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | PartitionOffsets  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

