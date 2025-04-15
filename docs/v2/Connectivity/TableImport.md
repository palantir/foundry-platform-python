# TableImport

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/connectivity/connections/{connectionRid}/tableImports | Public Beta |
[**delete**](#delete) | **DELETE** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid} | Public Beta |
[**execute**](#execute) | **POST** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}/execute | Public Beta |
[**get**](#get) | **GET** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid} | Public Beta |
[**list**](#list) | **GET** /v2/connectivity/connections/{connectionRid}/tableImports | Public Beta |
[**replace**](#replace) | **PUT** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid} | Private Beta |

# **create**
Creates a new TableImport.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid |  |  |
**config** | CreateTableImportRequestTableImportConfig |  |  |
**dataset_rid** | DatasetRid | The RID of the output dataset. |  |
**display_name** | TableImportDisplayName |  |  |
**import_mode** | TableImportMode |  |  |
**allow_schema_changes** | Optional[TableImportAllowSchemaChanges] | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports. | [optional] |
**branch_name** | Optional[BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**TableImport**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# CreateTableImportRequestTableImportConfig
config = {"type": "jdbcImportConfig", "query": "SELECT * FROM table"}
# DatasetRid | The RID of the output dataset.
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# TableImportDisplayName
display_name = "My table import"
# TableImportMode
import_mode = "SNAPSHOT"
# Optional[TableImportAllowSchemaChanges] | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports.
allow_schema_changes = True
# Optional[BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
branch_name = "master"
# Optional[PreviewMode] | Enables the use of preview functionality.
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
except foundry_sdk.PalantirRPCException as e:
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
**connection_rid** | ConnectionRid |  |  |
**table_import_rid** | TableImportRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# TableImportRid
table_import_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.connectivity.Connection.TableImport.delete(
        connection_rid, table_import_rid, preview=preview
    )
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
Executes the TableImport, which runs asynchronously as a [Foundry Build](https://palantir.com/docs/foundry/data-integration/builds/).
The returned BuildRid can be used to check the status via the Orchestration API.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid |  |  |
**table_import_rid** | TableImportRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**BuildRid**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# TableImportRid
table_import_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.connectivity.Connection.TableImport.execute(
        connection_rid, table_import_rid, preview=preview
    )
    print("The execute response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
**connection_rid** | ConnectionRid |  |  |
**table_import_rid** | TableImportRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**TableImport**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# TableImportRid
table_import_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.connectivity.Connection.TableImport.get(
        connection_rid, table_import_rid, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
**connection_rid** | ConnectionRid |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListTableImportsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for table_import in client.connectivity.Connection.TableImport.list(
        connection_rid, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(table_import)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling TableImport.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListTableImportsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Replace the TableImport with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**connection_rid** | ConnectionRid |  |  |
**table_import_rid** | TableImportRid |  |  |
**config** | ReplaceTableImportRequestTableImportConfig |  |  |
**dataset_rid** | DatasetRid | The RID of the output dataset. |  |
**display_name** | TableImportDisplayName |  |  |
**import_mode** | TableImportMode |  |  |
**allow_schema_changes** | Optional[TableImportAllowSchemaChanges] | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports. | [optional] |
**branch_name** | Optional[BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**TableImport**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ConnectionRid
connection_rid = None
# TableImportRid
table_import_rid = None
# ReplaceTableImportRequestTableImportConfig
config = {"type": "jdbcImportConfig", "query": "SELECT * FROM table"}
# DatasetRid | The RID of the output dataset.
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# TableImportDisplayName
display_name = "My table import"
# TableImportMode
import_mode = "SNAPSHOT"
# Optional[TableImportAllowSchemaChanges] | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports.
allow_schema_changes = True
# Optional[BranchName] | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments.
branch_name = "master"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.connectivity.Connection.TableImport.replace(
        connection_rid,
        table_import_rid,
        config=config,
        dataset_rid=dataset_rid,
        display_name=display_name,
        import_mode=import_mode,
        allow_schema_changes=allow_schema_changes,
        branch_name=branch_name,
        preview=preview,
    )
    print("The replace response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling TableImport.replace: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | TableImport  | The replaced TableImport | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

