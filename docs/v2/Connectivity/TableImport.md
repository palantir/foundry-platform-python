# TableImport

Method | HTTP request |
------------- | ------------- |
[**create**](#create) | **POST** /v2/connectivity/connections/{connectionRid}/tableImports |
[**delete**](#delete) | **DELETE** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid} |
[**execute**](#execute) | **POST** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}/execute |
[**get**](#get) | **GET** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid} |
[**list**](#list) | **GET** /v2/connectivity/connections/{connectionRid}/tableImports |
[**page**](#page) | **GET** /v2/connectivity/connections/{connectionRid}/tableImports |

# **create**
Creates a new TableImport.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**config** | CreateTableImportRequestTableImportConfigDict |  |  |
**dataset_rid** | DatasetRid | The RID of the output dataset. |  |
**display_name** | TableImportDisplayName |  |  |
**import_mode** | TableImportMode |  |  |
**allow_schema_changes** | Optional[TableImportAllowSchemaChanges] | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports. | [optional] |
**branch_name** | Optional[BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**TableImport**

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
# CreateTableImportRequestTableImportConfigDict |
config = None
# DatasetRid | The RID of the output dataset.
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# TableImportDisplayName |
display_name = "My table import"
# TableImportMode |
import_mode = "SNAPSHOT"
# Optional[TableImportAllowSchemaChanges] | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports.
allow_schema_changes = True
# Optional[BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
branch_name = "master"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.TableImport.create(
        connection_rid,
        config=config,
        dataset_rid=dataset_rid,
        display_name=display_name,
        import_mode=import_mode,
        allow_schema_changes=allow_schema_changes,
        branch_name=branch_name,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling TableImport.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | TableImport  | The created TableImport | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **delete**
Delete the TableImport with the specified RID.
Deleting the table import does not delete the destination dataset but the dataset will no longer
be updated by this import.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**table_import_rid** | TableImportRid | tableImportRid |  |
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

# ConnectionRid | connectionRid
connection_rid = None
# TableImportRid | tableImportRid
table_import_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.TableImport.delete(
        connection_rid,
        table_import_rid,
        preview=preview,
    )
    print("The delete response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling TableImport.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **execute**
Executes the TableImport, which runs asynchronously as a [Foundry Build](/docs/foundry/data-integration/builds/).
The returned BuildRid can be used to check the status via the Orchestration API.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**table_import_rid** | TableImportRid | tableImportRid |  |
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

# ConnectionRid | connectionRid
connection_rid = None
# TableImportRid | tableImportRid
table_import_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.TableImport.execute(
        connection_rid,
        table_import_rid,
        preview=preview,
    )
    print("The execute response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling TableImport.execute: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | BuildRid  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the TableImport with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**table_import_rid** | TableImportRid | tableImportRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**TableImport**

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
# TableImportRid | tableImportRid
table_import_rid = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.TableImport.get(
        connection_rid,
        table_import_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling TableImport.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | TableImport  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all table imports defined for this connection.
Only table imports that the user has permissions to view will be returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ResourceIterator[TableImport]**

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
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None


try:
    for table_import in foundry_client.connectivity.Connection.TableImport.list(
        connection_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    ):
        pprint(table_import)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling TableImport.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListTableImportsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
Lists all table imports defined for this connection.
Only table imports that the user has permissions to view will be returned.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid | connectionRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ListTableImportsResponse**

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
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.connectivity.Connection.TableImport.page(
        connection_rid,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling TableImport.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListTableImportsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

