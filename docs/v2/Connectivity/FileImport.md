# FileImport

Method | HTTP request |
------------- | ------------- |

Delete the FileImport with the specified RID.
Deleting the file import does not delete the destination dataset but the dataset will no longer
be updated by this import.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**file_import_rid** | FileImportRid | fileImportRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**None**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# FileImportRid | fileImportRid
file_import_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.FileImport.delete(
        file_import_rid,
        preview=preview,
    )
    print("The delete response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling FileImport.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Executes the FileImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
The returned BuildRid can be used to check the status via the Orchestration API.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**file_import_rid** | FileImportRid | fileImportRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**BuildRid**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# FileImportRid | fileImportRid
file_import_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.FileImport.execute(
        file_import_rid,
        preview=preview,
    )
    print("The execute response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling FileImport.execute: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | BuildRid  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

Get the FileImport with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**file_import_rid** | FileImportRid | fileImportRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**FileImport**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# FileImportRid | fileImportRid
file_import_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.FileImport.get(
        file_import_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling FileImport.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | FileImport  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

