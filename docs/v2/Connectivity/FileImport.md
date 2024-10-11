# FileImport

Method | HTTP request |
------------- | ------------- |

Creates a new FileImport.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | The RID of the Connection (formerly known as a source) that the File Import uses to import data. |  |
**dataset_rid** | DatasetRid | The RID of the output dataset. |  |
**display_name** | FileImportDisplayName |  |  |
**file_import_filters** | List[FileImportFilterDict] | Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs) |  |
**import_mode** | FileImportMode |  |  |
**branch_name** | Optional[BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |
**subfolder** | Optional[pydantic.StrictStr] | A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system. | [optional] |

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

# ConnectionRid | The RID of the Connection (formerly known as a source) that the File Import uses to import data.
connection_rid = "ri.magritte..source.c078b71b-92f9-41b6-b0df-3760f411120b"
# DatasetRid | The RID of the output dataset.
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# FileImportDisplayName |
display_name = None
# List[FileImportFilterDict] | Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)
file_import_filters = None
# FileImportMode |
import_mode = "SNAPSHOT"
# Optional[BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
branch_name = "master"
# Optional[PreviewMode] | preview
preview = None
# Optional[pydantic.StrictStr] | A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
subfolder = "subfolder1/subfolder2"


try:
    api_response = foundry_client.connectivity.FileImport.create(
        connection_rid=connection_rid,
        dataset_rid=dataset_rid,
        display_name=display_name,
        file_import_filters=file_import_filters,
        import_mode=import_mode,
        branch_name=branch_name,
        preview=preview,
        subfolder=subfolder,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling FileImport.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | FileImport  | The created FileImport | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

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

