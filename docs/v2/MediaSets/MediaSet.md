# MediaSet

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**abort**](#abort) | **POST** /v2/mediasets/{mediaSetRid}/transactions/{transactionId}/abort | Public Beta |
[**commit**](#commit) | **POST** /v2/mediasets/{mediaSetRid}/transactions/{transactionId}/commit | Public Beta |
[**create**](#create) | **POST** /v2/mediasets/{mediaSetRid}/transactions | Public Beta |
[**info**](#info) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid} | Public Beta |
[**read**](#read) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/content | Public Beta |
[**read_original**](#read_original) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/original | Public Beta |
[**reference**](#reference) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/reference | Public Beta |
[**upload**](#upload) | **POST** /v2/mediasets/{mediaSetRid}/items | Public Beta |

# **abort**
Aborts an open transaction. Items uploaded to the media set during this transaction will be deleted.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.


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
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# TransactionId
transaction_id = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = foundry_client.media_sets.MediaSet.abort(
        media_set_rid, transaction_id, preview=preview
    )
    print("The abort response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.abort: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **commit**
Commits an open transaction. On success, items uploaded to the media set during this transaction will become available.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.


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
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# TransactionId
transaction_id = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = foundry_client.media_sets.MediaSet.commit(
        media_set_rid, transaction_id, preview=preview
    )
    print("The commit response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.


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
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# Optional[BranchName] | The branch on which to open the transaction. Defaults to `master` for most enrollments.
branch_name = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = foundry_client.media_sets.MediaSet.create(
        media_set_rid, branch_name=branch_name, preview=preview
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | TransactionId  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **info**
Gets information about the media item.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid | The RID of the media set.  |  |
**media_item_rid** | MediaItemRid | The RID of the media item.  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**read_token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**GetMediaItemInfoResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemRid | The RID of the media item.
media_item_rid = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[MediaItemReadToken]
read_token = None


try:
    api_response = foundry_client.media_sets.MediaSet.info(
        media_set_rid, media_item_rid, preview=preview, read_token=read_token
    )
    print("The info response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.info: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetMediaItemInfoResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **read**
Gets the content of a media item.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid |  |  |
**media_item_rid** | MediaItemRid |  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**read_token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# MediaItemRid
media_item_rid = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[MediaItemReadToken]
read_token = None


try:
    api_response = foundry_client.media_sets.MediaSet.read(
        media_set_rid, media_item_rid, preview=preview, read_token=read_token
    )
    print("The read response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid |  |  |
**media_item_rid** | MediaItemRid |  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**read_token** | Optional[MediaItemReadToken] |  | [optional] |

### Return type
**bytes**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid
media_set_rid = None
# MediaItemRid
media_item_rid = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[MediaItemReadToken]
read_token = None


try:
    api_response = foundry_client.media_sets.MediaSet.read_original(
        media_set_rid, media_item_rid, preview=preview, read_token=read_token
    )
    print("The read_original response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
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
Gets the [media reference](/docs/foundry/data-integration/media-sets/#media-references) for this media item.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-read`.


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
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaSetRid | The RID of the media set.
media_set_rid = None
# MediaItemRid | The RID of the media item.
media_item_rid = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[MediaItemReadToken]
read_token = None


try:
    api_response = foundry_client.media_sets.MediaSet.reference(
        media_set_rid, media_item_rid, preview=preview, read_token=read_token
    )
    print("The reference response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.reference: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MediaReference  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **upload**
Uploads a media item to an existing media set.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
A branch name, or branch rid, or view rid may optionally be specified.  If none is specified, the item will be uploaded to the default branch. If more than one is specified, an error is thrown.

Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:mediasets-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_set_rid** | MediaSetRid |  |  |
**body** | bytes | Body of the request |  |
**branch_name** | Optional[BranchName] | Specifies the specific branch by name to which this media item will be uploaded. May not be provided if branch rid or view rid are provided. | [optional] |
**branch_rid** | Optional[BranchRid] | Specifies the specific branch by rid to which this media item will be uploaded. May not be provided if branch name or view rid are provided. | [optional] |
**media_item_path** | Optional[MediaItemPath] | An identifier for a media item within a media set. Necessary if the backing media set requires paths. | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**transaction_id** | Optional[TransactionId] | The id of the transaction associated with this request.  Required if this is a transactional media set.  | [optional] |
**view_rid** | Optional[MediaSetViewRid] | Specifies the specific view by rid to which this media item will be uploaded. May not be provided if branch name or branch rid are provided. | [optional] |

### Return type
**PutMediaItemResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

client = FoundryClient(auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com")

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
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[TransactionId] | The id of the transaction associated with this request.  Required if this is a transactional media set.
transaction_id = None
# Optional[MediaSetViewRid] | Specifies the specific view by rid to which this media item will be uploaded. May not be provided if branch name or branch rid are provided.
view_rid = None


try:
    api_response = foundry_client.media_sets.MediaSet.upload(
        media_set_rid,
        body,
        branch_name=branch_name,
        branch_rid=branch_rid,
        media_item_path=media_item_path,
        preview=preview,
        transaction_id=transaction_id,
        view_rid=view_rid,
    )
    print("The upload response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling MediaSet.upload: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | PutMediaItemResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

