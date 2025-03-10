# FileImport

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/connectivity/connections/{connectionRid}/fileImports | Public Beta |
[**delete**](#delete) | **DELETE** /v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid} | Public Beta |
[**execute**](#execute) | **POST** /v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}/execute | Public Beta |
[**get**](#get) | **GET** /v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid} | Public Beta |
[**list**](#list) | **GET** /v2/connectivity/connections/{connectionRid}/fileImports | Public Beta |
[**page**](#page) | **GET** /v2/connectivity/connections/{connectionRid}/fileImports | Public Beta |
[**replace**](#replace) | **PUT** /v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid} | Private Beta |

# **create**
Creates a new FileImport.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**dataset_rid** | datasets_models.DatasetRid | The RID of the output dataset. |  |
**display_name** | FileImportDisplayName |  |  |
**file_import_filters** | typing.List[typing.Union[FileImportFilter, FileImportFilterDict]] | Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs) |  |
**import_mode** | FileImportMode |  |  |
**branch_name** | typing.Optional[datasets_models.BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |
**subfolder** | typing.Optional[str] | A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system. | [optional] |

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

# ConnectionRid | connectionRid
connection_rid = None
# datasets_models.DatasetRid | The RID of the output dataset.
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# FileImportDisplayName |
display_name = "My file import"
# typing.List[typing.Union[FileImportFilter, FileImportFilterDict]] | Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)
file_import_filters = None
# FileImportMode |
import_mode = "SNAPSHOT"
# typing.Optional[datasets_models.BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
branch_name = "master"
# typing.Optional[core_models.PreviewMode] | preview
preview = None
# typing.Optional[str] | A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
subfolder = "subfolder1/subfolder2"


try:
    api_response = foundry_client.connectivity.Connection.FileImport.create(
        connection_rid,
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

# **delete**
Delete the FileImport with the specified RID.
Deleting the file import does not delete the destination dataset but the dataset will no longer
be updated by this import.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**file_import_rid** | FileImportRid | fileImportRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

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

# ConnectionRid | connectionRid
connection_rid = None
# FileImportRid | fileImportRid
file_import_rid = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.FileImport.delete(
        connection_rid,
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

# **execute**
Executes the FileImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
The returned BuildRid can be used to check the status via the Orchestration API.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**file_import_rid** | FileImportRid | fileImportRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**core_models.BuildRid**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ConnectionRid | connectionRid
connection_rid = None
# FileImportRid | fileImportRid
file_import_rid = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.FileImport.execute(
        connection_rid,
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
**200** | core_models.BuildRid  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the FileImport with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**file_import_rid** | FileImportRid | fileImportRid |  |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

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

# ConnectionRid | connectionRid
connection_rid = None
# FileImportRid | fileImportRid
file_import_rid = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.FileImport.get(
        connection_rid,
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

# **list**
Lists all file imports defined for this connection.
Only file imports that the user has permissions to view will be returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**ListFileImportsResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ConnectionRid | connectionRid
connection_rid = None
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    for file_import in foundry_client.connectivity.Connection.FileImport.list(
        connection_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(file_import)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling FileImport.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListFileImportsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
Lists all file imports defined for this connection.
Only file imports that the user has permissions to view will be returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**page_size** | typing.Optional[core_models.PageSize] | pageSize | [optional] |
**page_token** | typing.Optional[core_models.PageToken] | pageToken | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |

### Return type
**ListFileImportsResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ConnectionRid | connectionRid
connection_rid = None
# typing.Optional[core_models.PageSize] | pageSize
page_size = None
# typing.Optional[core_models.PageToken] | pageToken
page_token = None
# typing.Optional[core_models.PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.FileImport.page(
        connection_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling FileImport.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListFileImportsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Replace the FileImport with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**file_import_rid** | FileImportRid | fileImportRid |  |
**dataset_rid** | datasets_models.DatasetRid | The RID of the output dataset. |  |
**display_name** | FileImportDisplayName |  |  |
**file_import_filters** | typing.List[typing.Union[FileImportFilter, FileImportFilterDict]] | Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs) |  |
**import_mode** | FileImportMode |  |  |
**branch_name** | typing.Optional[datasets_models.BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. | [optional] |
**preview** | typing.Optional[core_models.PreviewMode] | preview | [optional] |
**subfolder** | typing.Optional[str] | A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system. | [optional] |

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

# ConnectionRid | connectionRid
connection_rid = None
# FileImportRid | fileImportRid
file_import_rid = None
# datasets_models.DatasetRid | The RID of the output dataset.
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# FileImportDisplayName |
display_name = "My file import"
# typing.List[typing.Union[FileImportFilter, FileImportFilterDict]] | Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](/docs/foundry/data-connection/file-based-syncs/#optimize-file-based-syncs)
file_import_filters = None
# FileImportMode |
import_mode = "SNAPSHOT"
# typing.Optional[datasets_models.BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
branch_name = "master"
# typing.Optional[core_models.PreviewMode] | preview
preview = None
# typing.Optional[str] | A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system.
subfolder = "subfolder1/subfolder2"


try:
    api_response = foundry_client.connectivity.Connection.FileImport.replace(
        connection_rid,
        file_import_rid,
        dataset_rid=dataset_rid,
        display_name=display_name,
        file_import_filters=file_import_filters,
        import_mode=import_mode,
        branch_name=branch_name,
        preview=preview,
        subfolder=subfolder,
    )
    print("The replace response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling FileImport.replace: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | FileImport  | The replaced FileImport | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

