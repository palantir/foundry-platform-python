# Enrollment

Method | HTTP request |
------------- | ------------- |

Get the Enrollment with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**enrollment_rid** | EnrollmentRid | enrollmentRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Enrollment**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# EnrollmentRid | enrollmentRid
enrollment_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Enrollment.get(
        enrollment_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Enrollment.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Enrollment  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Returns the Enrollment associated with the current User's primary organization.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Enrollment**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.admin.Enrollment.get_current(
        preview=preview,
    )
    print("The get_current response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Enrollment.get_current: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Enrollment  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

