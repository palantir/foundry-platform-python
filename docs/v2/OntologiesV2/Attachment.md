# Attachment

Method | HTTP request |
------------- | ------------- |
[**read**](#read) | **GET** /v2/ontologies/attachments/{attachmentRid}/content |
[**upload**](#upload) | **POST** /v2/ontologies/attachments/upload |

# **read**
Get the content of an attachment.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**attachment_rid** | AttachmentRid | attachmentRid |  |

### Return type
**bytes**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# AttachmentRid | attachmentRid
attachment_rid = "ri.attachments.main.attachment.bb32154e-e043-4b00-9461-93136ca96b6f"


try:
    api_response = foundry_client.ontologies.Attachment.read(
        attachment_rid,
    )
    print("The read response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Attachment.read: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | Success response. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **upload**
Upload an attachment to use in an action. Any attachment which has not been linked to an object via
an action within one hour after upload will be removed.
Previously mapped attachments which are not connected to any object anymore are also removed on
a biweekly basis.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | bytes | Body of the request |  |
**content_length** | ContentLength | Content-Length |  |
**content_type** | ContentType | Content-Type |  |
**filename** | Filename | filename |  |

### Return type
**AttachmentV2**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# bytes | Body of the request
body = None
# ContentLength | Content-Length
content_length = None
# ContentType | Content-Type
content_type = None
# Filename | filename
filename = "My Image.jpeg"


try:
    api_response = foundry_client.ontologies.Attachment.upload(
        body,
        content_length=content_length,
        content_type=content_type,
        filename=filename,
    )
    print("The upload response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Attachment.upload: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AttachmentV2  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

