# Dataset

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/streams/datasets/create | Public Beta |

# **create**
Creates a streaming dataset with a stream on the specified branch, or if no branch is specified, on the
default branch ('master' for most enrollments). For more information on streaming datasets, refer to the
[streams](/docs/foundry/data-integration/streams/) user documentation.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**name** | datasets_models.DatasetName |  |  |
**parent_folder_rid** | filesystem_models.FolderRid |  |  |
**schema** | typing.Union[core_models.StreamSchema, core_models.StreamSchemaDict] | The Foundry schema to apply to the new stream.  |  |
**branch_name** | typing.Optional[datasets_models.BranchName] | The branch to create the initial stream on. If not specified, the default branch will be used ('master' for most enrollments).  | [optional] |
**compressed** | typing.Optional[Compressed] | Whether or not compression is enabled for the stream. Defaults to false.  | [optional] |
**partitions_count** | typing.Optional[PartitionsCount] | The number of partitions for the Foundry stream.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If not specified, 1 partition is used.  This value cannot be changed later.  | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |
**stream_type** | typing.Optional[StreamType] | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.  | [optional] |

### Return type
**Dataset**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# datasets_models.DatasetName |
name = "My Dataset"
# filesystem_models.FolderRid |
parent_folder_rid = "ri.compass.main.folder.c410f510-2937-420e-8ea3-8c9bcb3c1791"
# typing.Union[core_models.StreamSchema, core_models.StreamSchemaDict] | The Foundry schema to apply to the new stream.
schema = None
# typing.Optional[datasets_models.BranchName] | The branch to create the initial stream on. If not specified, the default branch will be used ('master' for most enrollments).
branch_name = "master"
# typing.Optional[Compressed] | Whether or not compression is enabled for the stream. Defaults to false.
compressed = False
# typing.Optional[PartitionsCount] | The number of partitions for the Foundry stream.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If not specified, 1 partition is used.  This value cannot be changed later.
partitions_count = 1
# typing.Optional[core_models.PreviewMode] | preview
preview = None
# typing.Optional[StreamType] | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
stream_type = "LOW_LATENCY"


try:
    api_response = foundry_client.streams.Dataset.create(
        name=name,
        parent_folder_rid=parent_folder_rid,
        schema=schema,
        branch_name=branch_name,
        compressed=compressed,
        partitions_count=partitions_count,
        preview=preview,
        stream_type=stream_type,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Dataset.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Dataset  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

