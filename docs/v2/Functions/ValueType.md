# ValueType

Method | HTTP request |
------------- | ------------- |

Gets a specific value type with the given RID. The latest version is returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**value_type_rid** | ValueTypeRid | valueTypeRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ValueType**

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
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.functions.ValueType.get(
        value_type_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling ValueType.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ValueType  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

