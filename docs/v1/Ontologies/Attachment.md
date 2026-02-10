# Attachment

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v1/attachments/{attachmentRid} | Stable |
[**read**](#read) | **GET** /v1/attachments/{attachmentRid}/content | Stable |
[**upload**](#upload) | **POST** /v1/attachments/upload | Stable |

# **get**
Get the metadata of an attachment.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**attachment_rid** | AttachmentRid | The RID of the attachment. |  |

### Return type
**Attachment**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AttachmentRid | The RID of the attachment.
attachment_rid = "ri.attachments.main.attachment.bb32154e-e043-4b00-9461-93136ca96b6f"


try:
    api_response = client.ontologies.Attachment.get(attachment_rid)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Attachment.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Attachment  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **read**
Get the content of an attachment.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**attachment_rid** | AttachmentRid | The RID of the attachment. |  |

### Return type
**bytes**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# AttachmentRid | The RID of the attachment.
attachment_rid = "ri.attachments.main.attachment.bb32154e-e043-4b00-9461-93136ca96b6f"


try:
    api_response = client.ontologies.Attachment.read(attachment_rid)
    print("The read response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Attachment.read: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | Success response. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **upload**
Upload an attachment to use in an action. Any attachment which has not been linked to an object via
an action within one hour after upload will be removed.
Previously mapped attachments which are not connected to any object anymore are also removed on
a biweekly basis.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | bytes | Body of the request |  |
**content_length** | ContentLength | The size in bytes of the file content being uploaded. |  |
**content_type** | ContentType | The media type of the file being uploaded. |  |
**filename** | Filename | The name of the file being uploaded. |  |

### Return type
**Attachment**

### Example

```python
from foundry_sdk.v1 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# bytes | Body of the request
body = None
# ContentLength | The size in bytes of the file content being uploaded.
content_length = None
# ContentType | The media type of the file being uploaded.
content_type = None
# Filename | The name of the file being uploaded.
filename = "My Image.jpeg"


try:
    api_response = client.ontologies.Attachment.upload(
        body, content_length=content_length, content_type=content_type, filename=filename
    )
    print("The upload response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Attachment.upload: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Attachment  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

