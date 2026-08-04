# MediaSet

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**abort**](#abort) | **POST** /v2/mediasets/{mediaSetRid}/transactions/{transactionId}/abort | Public Beta |
[**calculate**](#calculate) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform/imagery/thumbnail/calculate | Private Beta |
[**clear**](#clear) | **DELETE** /v2/mediasets/{mediaSetRid}/items/clearAtPath | Public Beta |
[**commit**](#commit) | **POST** /v2/mediasets/{mediaSetRid}/transactions/{transactionId}/commit | Public Beta |
[**create**](#create) | **POST** /v2/mediasets/{mediaSetRid}/transactions | Public Beta |
[**get**](#get) | **GET** /v2/mediasets/{mediaSetRid} | Public Beta |
[**get_result**](#get_result) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transformationJobs/{transformationJobId}/result | Public Beta |
[**get_rid_by_path**](#get_rid_by_path) | **GET** /v2/mediasets/{mediaSetRid}/items/getRidByPath | Public Beta |
[**get_status**](#get_status) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transformationJobs/{transformationJobId} | Public Beta |
[**info**](#info) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid} | Stable |
[**metadata**](#metadata) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/metadata | Stable |
[**read**](#read) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/content | Stable |
[**read_original**](#read_original) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/original | Stable |
[**reference**](#reference) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/reference | Public Beta |
[**register**](#register) | **POST** /v2/mediasets/{mediaSetRid}/items/register | Public Beta |
[**retrieve**](#retrieve) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform/imagery/thumbnail/retrieve | Private Beta |
[**transform**](#transform) | **POST** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform | Public Beta |
[**upload**](#upload) | **POST** /v2/mediasets/{mediaSetRid}/items | Public Beta |
[**upload_media**](#upload_media) | **PUT** /v2/mediasets/media/upload | Stable |

# **abort**
Aborts an open transaction. Items uploaded to the media set during this transaction will be deleted.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid |  |  |
**transaction_id** | TransactionId |  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# TransactionId
transaction_id = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.media_sets.MediaSet.abort(media_set_rid, transaction_id, preview=preview)
    print("The abort response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.abort: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **calculate**
Starts calculation of a thumbnail for a given image.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | The RID of the media set.  |  |
**media_item_rid** | MediaItemRid | The RID of the media item.  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**read_token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**TrackedTransformationResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemRid | The RID of the media item.
media_item_rid = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[MediaItemReadToken]
read_token = None


try:
    api_response = client.media_sets.MediaSet.calculate(
        media_set_rid, media_item_rid, preview=preview, read_token=read_token
    )
    print("The calculate response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.calculate: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | TrackedTransformationResponse  | Status of the thumbnail calculation. Type will be 'successful' if the thumbnail is available,  'pending' if the thumbnail is being calculated, and 'failed' if there was an error.  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **clear**
Clears (soft-deletes) the media item at the specified path within a media set, making it and all older
media items at that path un-retrievable.

A branch name, branch RID, or view RID may optionally be specified. If none is specified,
the item will be cleared from the default branch. If more than one is specified, an error is thrown.

For transactional media sets, a transaction ID must be provided. The deletion will not be
visible until the transaction is committed.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | The RID of the media set.  |  |
**media_item_path** | MediaItemPath | The path of the media item to clear.  |  |
**branch_name** | Optional[BranchName] | Specifies the specific branch by name from which this media item will be cleared. May not be provided if branch rid or view rid are provided. | [optional] |
**branch_rid** | Optional[BranchRid] | Specifies the specific branch by rid from which this media item will be cleared. May not be provided if branch name or view rid are provided. | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**transaction_id** | Optional[TransactionId] | The ID of the transaction associated with this request. Required if this is a transactional media set.  | [optional] |
**view_rid** | Optional[MediaSetViewRid] | Specifies the specific view by rid from which this media item will be cleared. May not be provided if branch name or branch rid are provided. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemPath | The path of the media item to clear.
media_item_path = "q3-data%2fmy-file.png"
# Optional[BranchName] | Specifies the specific branch by name from which this media item will be cleared. May not be provided if branch rid or view rid are provided.
branch_name = None
# Optional[BranchRid] | Specifies the specific branch by rid from which this media item will be cleared. May not be provided if branch name or view rid are provided.
branch_rid = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[TransactionId] | The ID of the transaction associated with this request. Required if this is a transactional media set.
transaction_id = None
# Optional[MediaSetViewRid] | Specifies the specific view by rid from which this media item will be cleared. May not be provided if branch name or branch rid are provided.
view_rid = None


try:
    api_response = client.media_sets.MediaSet.clear(
        media_set_rid,
        media_item_path=media_item_path,
        branch_name=branch_name,
        branch_rid=branch_rid,
        preview=preview,
        transaction_id=transaction_id,
        view_rid=view_rid,
    )
    print("The clear response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.clear: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  | Media item cleared successfully. | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **commit**
Commits an open transaction. On success, items uploaded to the media set during this transaction will become available.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid |  |  |
**transaction_id** | TransactionId |  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# TransactionId
transaction_id = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.media_sets.MediaSet.commit(media_set_rid, transaction_id, preview=preview)
    print("The commit response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.commit: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **create**
Creates a new transaction. Items uploaded to the media set while this transaction is open will not be reflected until the transaction is committed.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid |  |  |
**branch_name** | Optional[BranchName] | The branch on which to open the transaction. Defaults to `master` for most enrollments.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**TransactionId**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# Optional[BranchName] | The branch on which to open the transaction. Defaults to `master` for most enrollments.
branch_name = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.media_sets.MediaSet.create(
        media_set_rid, branch_name=branch_name, preview=preview
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | TransactionId  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Gets information about the media set.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid |  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**GetMediaSetResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.media_sets.MediaSet.get(media_set_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetMediaSetResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_result**
Gets the result of a completed transformation job. Returns the transformed media content as binary data.
This endpoint will return an error if the transformation job has not completed successfully.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | The RID of the media set.  |  |
**media_item_rid** | MediaItemRid | The RID of the media item.  |  |
**transformation_job_id** | TransformationJobId | The ID of the transformation job.  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemRid | The RID of the media item.
media_item_rid = None
# TransformationJobId | The ID of the transformation job.
transformation_job_id = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[MediaItemReadToken]
token = None


try:
    api_response = client.media_sets.MediaSet.get_result(
        media_set_rid, media_item_rid, transformation_job_id, preview=preview, token=token
    )
    print("The get_result response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.get_result: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | The transformed media content. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_rid_by_path**
Returns the media item RID for the media item with the specified path.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | The RID of the media set.  |  |
**media_item_path** | MediaItemPath | The path of the media item.  |  |
**branch_name** | Optional[BranchName] | Specifies the specific branch by name in which to search for this media item. May not be provided if branch rid or view rid are provided. | [optional] |
**branch_rid** | Optional[BranchRid] | Specifies the specific branch by rid in which to search for this media item. May not be provided if branch name or view rid are provided. | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**view_rid** | Optional[MediaSetViewRid] | Specifies the specific view by rid in which to search for this media item. May not be provided if branch name or branch rid are provided. | [optional] |

### Return type
**GetMediaItemRidByPathResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemPath | The path of the media item.
media_item_path = None
# Optional[BranchName] | Specifies the specific branch by name in which to search for this media item. May not be provided if branch rid or view rid are provided.
branch_name = None
# Optional[BranchRid] | Specifies the specific branch by rid in which to search for this media item. May not be provided if branch name or view rid are provided.
branch_rid = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[MediaSetViewRid] | Specifies the specific view by rid in which to search for this media item. May not be provided if branch name or branch rid are provided.
view_rid = None


try:
    api_response = client.media_sets.MediaSet.get_rid_by_path(
        media_set_rid,
        media_item_path=media_item_path,
        branch_name=branch_name,
        branch_rid=branch_rid,
        preview=preview,
        view_rid=view_rid,
    )
    print("The get_rid_by_path response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.get_rid_by_path: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetMediaItemRidByPathResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_status**
Gets the status of a transformation job.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | The RID of the media set.  |  |
**media_item_rid** | MediaItemRid | The RID of the media item.  |  |
**transformation_job_id** | TransformationJobId | The ID of the transformation job.  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**GetTransformationJobStatusResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemRid | The RID of the media item.
media_item_rid = None
# TransformationJobId | The ID of the transformation job.
transformation_job_id = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[MediaItemReadToken]
token = None


try:
    api_response = client.media_sets.MediaSet.get_status(
        media_set_rid, media_item_rid, transformation_job_id, preview=preview, token=token
    )
    print("The get_status response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.get_status: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetTransformationJobStatusResponse  | The status of the transformation job. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **info**
Gets information about the media item.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | The RID of the media set.  |  |
**media_item_rid** | MediaItemRid | The RID of the media item.  |  |
**read_token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**GetMediaItemInfoResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemRid | The RID of the media item.
media_item_rid = None
# Optional[MediaItemReadToken]
read_token = None


try:
    api_response = client.media_sets.MediaSet.info(
        media_set_rid, media_item_rid, read_token=read_token
    )
    print("The info response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.info: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetMediaItemInfoResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **metadata**
Gets detailed metadata about the media item, including type-specific information
such as dimensions for images, duration for audio/video, page count for documents, etc.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | The RID of the media set.  |  |
**media_item_rid** | MediaItemRid | The RID of the media item.  |  |
**read_token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**MediaItemMetadata**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemRid | The RID of the media item.
media_item_rid = None
# Optional[MediaItemReadToken]
read_token = None


try:
    api_response = client.media_sets.MediaSet.metadata(
        media_set_rid, media_item_rid, read_token=read_token
    )
    print("The metadata response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.metadata: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MediaItemMetadata  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **read**
Gets the content of a media item.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid |  |  |
**media_item_rid** | MediaItemRid |  |  |
**read_token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# MediaItemRid
media_item_rid = None
# Optional[MediaItemReadToken]
read_token = None


try:
    api_response = client.media_sets.MediaSet.read(
        media_set_rid, media_item_rid, read_token=read_token
    )
    print("The read response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.read: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | The content stream. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **read_original**
Gets the content of an original file uploaded to the media item, even if it was transformed on upload due to being an additional input format.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid |  |  |
**media_item_rid** | MediaItemRid |  |  |
**read_token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# MediaItemRid
media_item_rid = None
# Optional[MediaItemReadToken]
read_token = None


try:
    api_response = client.media_sets.MediaSet.read_original(
        media_set_rid, media_item_rid, read_token=read_token
    )
    print("The read_original response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.read_original: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | The content stream. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **reference**
Gets the [media reference](https://palantir.com/docs/foundry/data-integration/media-sets/#media-references) for this media item.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | The RID of the media set.  |  |
**media_item_rid** | MediaItemRid | The RID of the media item.  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**read_token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**MediaReference**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemRid | The RID of the media item.
media_item_rid = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[MediaItemReadToken]
read_token = None


try:
    api_response = client.media_sets.MediaSet.reference(
        media_set_rid, media_item_rid, preview=preview, read_token=read_token
    )
    print("The reference response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.reference: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MediaReference  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **register**
Registers a media item that currently resides in a federated media store. Registration will validate the item
against the media set's schema and perform initial metadata extraction.
This endpoint is only applicable for federated media sets.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid |  |  |
**physical_item_name** | str | The relative path within the federated media store where the media item exists. |  |
**branch_name** | Optional[BranchName] | Specifies the specific branch by name to which this media item will be registered. | [optional] |
**media_item_path** | Optional[MediaItemPath] |  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode. | [optional] |
**transaction_id** | Optional[TransactionId] | The id of the transaction associated with this request. Required for transactional media sets. | [optional] |
**view_rid** | Optional[MediaSetViewRid] | Specifies the specific view by rid to which this media item will be registered. | [optional] |

### Return type
**RegisterMediaItemResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# str | The relative path within the federated media store where the media item exists.
physical_item_name = None
# Optional[BranchName] | Specifies the specific branch by name to which this media item will be registered.
branch_name = None
# Optional[MediaItemPath]
media_item_path = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[TransactionId] | The id of the transaction associated with this request. Required for transactional media sets.
transaction_id = None
# Optional[MediaSetViewRid] | Specifies the specific view by rid to which this media item will be registered.
view_rid = None


try:
    api_response = client.media_sets.MediaSet.register(
        media_set_rid,
        physical_item_name=physical_item_name,
        branch_name=branch_name,
        media_item_path=media_item_path,
        preview=preview,
        transaction_id=transaction_id,
        view_rid=view_rid,
    )
    print("The register response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.register: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | RegisterMediaItemResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **retrieve**
Retrieves a successfully calculated thumbnail for a given image.

Thumbnails are 200px wide in the format of `image/webp`


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | The RID of the media set.  |  |
**media_item_rid** | MediaItemRid | The RID of the media item.  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**read_token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemRid | The RID of the media item.
media_item_rid = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[MediaItemReadToken]
read_token = None


try:
    api_response = client.media_sets.MediaSet.retrieve(
        media_set_rid, media_item_rid, preview=preview, read_token=read_token
    )
    print("The retrieve response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.retrieve: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | Retrieves the thumbnail of an image (if available).  | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **transform**
Initiates a transformation on a media item. Returns a job ID that can be used to check the status and retrieve 
the result of the transformation.

Transforming a media item requires that you are able to read the media item, either via `api:mediasets-read` or
via a `MediaItemReadToken`


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | The RID of the media set.  |  |
**media_item_rid** | MediaItemRid | The RID of the media item.  |  |
**transformation** | Transformation |  |  |
**attribution** | Optional[Attribution] | Optional resource to attribute LLM calls on behalf of. | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**TransformMediaItemResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemRid | The RID of the media item.
media_item_rid = None
# Transformation
transformation = {
    "type": "image",
    "encoding": {"type": "webp"},
    "operations": [{"type": "resize", "width": 800, "height": 600}],
}
# Optional[Attribution] | Optional resource to attribute LLM calls on behalf of.
attribution = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[MediaItemReadToken]
token = None


try:
    api_response = client.media_sets.MediaSet.transform(
        media_set_rid,
        media_item_rid,
        transformation=transformation,
        attribution=attribution,
        preview=preview,
        token=token,
    )
    print("The transform response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.transform: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | TransformMediaItemResponse  | The transformation was initiated successfully. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **upload**
Uploads a media item to an existing media set.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
A branch name, or branch rid, or view rid may optionally be specified.  If none is specified, the item will be uploaded to the default branch. If more than one is specified, an error is thrown.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid |  |  |
**body** | bytes | Body of the request |  |
**branch_name** | Optional[BranchName] | Specifies the specific branch by name to which this media item will be uploaded. May not be provided if branch rid or view rid are provided. | [optional] |
**branch_rid** | Optional[BranchRid] | Specifies the specific branch by rid to which this media item will be uploaded. May not be provided if branch name or view rid are provided. | [optional] |
**media_item_path** | Optional[MediaItemPath] | An identifier for a media item within a media set. Necessary if the backing media set requires paths. | [optional] |
**media_item_rid** | Optional[MediaItemRid] | An optional RID to use for the media item to create. If omitted, the server will automatically generate a RID. In most cases, the server-generated RID should be preferred; only specify a custom RID if your workflow strictly requires deterministic or client-controlled identifiers. The RID must be in the format of `ri.mio.<instance>.media-item.<UUID>`, where `<instance>` is the same as  the instance part of the media set RID, and `<UUID>` is a UUID. An `InvalidMediaItemRid` error will be thrown if the RID is not in the expected format. A `MediaItemRidAlreadyExists` error will be thrown if the media set already contains a media item with the same RID.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**transaction_id** | Optional[TransactionId] | The id of the transaction associated with this request.  Required if this is a transactional media set.  | [optional] |
**view_rid** | Optional[MediaSetViewRid] | Specifies the specific view by rid to which this media item will be uploaded. May not be provided if branch name or branch rid are provided. | [optional] |

### Return type
**PutMediaItemResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# bytes | Body of the request
body = None
# Optional[BranchName] | Specifies the specific branch by name to which this media item will be uploaded. May not be provided if branch rid or view rid are provided.
branch_name = None
# Optional[BranchRid] | Specifies the specific branch by rid to which this media item will be uploaded. May not be provided if branch name or view rid are provided.
branch_rid = None
# Optional[MediaItemPath] | An identifier for a media item within a media set. Necessary if the backing media set requires paths.
media_item_path = "q3-data%2fmy-file.png"
# Optional[MediaItemRid] | An optional RID to use for the media item to create. If omitted, the server will automatically generate a RID. In most cases, the server-generated RID should be preferred; only specify a custom RID if your workflow strictly requires deterministic or client-controlled identifiers. The RID must be in the format of `ri.mio.<instance>.media-item.<UUID>`, where `<instance>` is the same as  the instance part of the media set RID, and `<UUID>` is a UUID. An `InvalidMediaItemRid` error will be thrown if the RID is not in the expected format. A `MediaItemRidAlreadyExists` error will be thrown if the media set already contains a media item with the same RID.
media_item_rid = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[TransactionId] | The id of the transaction associated with this request.  Required if this is a transactional media set.
transaction_id = None
# Optional[MediaSetViewRid] | Specifies the specific view by rid to which this media item will be uploaded. May not be provided if branch name or branch rid are provided.
view_rid = None


try:
    api_response = client.media_sets.MediaSet.upload(
        media_set_rid,
        body,
        branch_name=branch_name,
        branch_rid=branch_rid,
        media_item_path=media_item_path,
        media_item_rid=media_item_rid,
        preview=preview,
        transaction_id=transaction_id,
        view_rid=view_rid,
    )
    print("The upload response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.upload: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | PutMediaItemResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **upload_media**
Uploads a temporary media item. If the media item isn't persisted within 1 hour, the item will be deleted. 

If multiple resources are attributed to, usage will be attributed to the first one in the list.

The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:ontologies-read api:ontologies-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | bytes | Body of the request |  |
**filename** | MediaItemPath | A user-defined label for a media item within a media set. Required if the backing media set requires paths.  Uploading multiple files to the same path will result in only the most recent file being associated with the  path.  |  |
**attribution** | Optional[Attribution] | used for passing through usage attribution | [optional] |
**media_item_rid** | Optional[MediaItemRid] | An optional RID to use for the media item to create. If omitted, the server will automatically generate a RID. In most cases, the server-generated RID should be preferred; only specify a custom RID if your workflow strictly requires deterministic or client-controlled identifiers. The RID must be in the format of `ri.mio.<instance>.media-item.<UUID>`, where `<instance>` is the same as  the instance part of the media set RID, and `<UUID>` is a UUID. An `InvalidMediaItemRid` error will be thrown if the RID is not in the expected format. A `MediaItemRidAlreadyExists` error will be thrown if the media set already contains a media item with the same RID.  | [optional] |

### Return type
**MediaReference**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# bytes | Body of the request
body = None
# MediaItemPath | A user-defined label for a media item within a media set. Required if the backing media set requires paths.  Uploading multiple files to the same path will result in only the most recent file being associated with the  path.
filename = "my-file.png"
# Optional[Attribution] | used for passing through usage attribution
attribution = None
# Optional[MediaItemRid] | An optional RID to use for the media item to create. If omitted, the server will automatically generate a RID. In most cases, the server-generated RID should be preferred; only specify a custom RID if your workflow strictly requires deterministic or client-controlled identifiers. The RID must be in the format of `ri.mio.<instance>.media-item.<UUID>`, where `<instance>` is the same as  the instance part of the media set RID, and `<UUID>` is a UUID. An `InvalidMediaItemRid` error will be thrown if the RID is not in the expected format. A `MediaItemRidAlreadyExists` error will be thrown if the media set already contains a media item with the same RID.
media_item_rid = None


try:
    api_response = client.media_sets.MediaSet.upload_media(
        body, filename=filename, attribution=attribution, media_item_rid=media_item_rid
    )
    print("The upload_media response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.upload_media: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MediaReference  | The media reference for the uploaded media. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

