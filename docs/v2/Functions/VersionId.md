# VersionId

Method | HTTP request |
------------- | ------------- |

Gets a specific value type with the given RID. The specified version is returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**value_type_rid** | ValueTypeRid | valueTypeRid |  |
**version_id_version_id** | ValueTypeVersionId | versionIdVersionId |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**VersionId**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ValueTypeRid | valueTypeRid
value_type_rid = None
# ValueTypeVersionId | versionIdVersionId
version_id_version_id = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.functions.ValueType.VersionId.get(
        value_type_rid,
        version_id_version_id,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling VersionId.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | VersionId  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

