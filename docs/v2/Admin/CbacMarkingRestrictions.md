# CbacMarkingRestrictions

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/admin/cbacMarkingRestrictions | Public Beta |

# **get**
Returns disallowed, implied, and required markings for the given set of marking IDs.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marking_ids** | Optional[List[MarkingId]] | The marking IDs for which to get restrictions. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**CbacMarkingRestrictions**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Optional[List[MarkingId]] | The marking IDs for which to get restrictions.
marking_ids = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.CbacMarkingRestrictions.get(
        marking_ids=marking_ids, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling CbacMarkingRestrictions.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CbacMarkingRestrictions  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

