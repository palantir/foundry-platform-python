# View

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add_backing_datasets**](#add_backing_datasets) | **POST** /v2/datasets/views/{viewDatasetRid}/addBackingDatasets | Stable |
[**add_primary_key**](#add_primary_key) | **POST** /v2/datasets/views/{viewDatasetRid}/addPrimaryKey | Stable |
[**create**](#create) | **POST** /v2/datasets/views | Stable |
[**get**](#get) | **GET** /v2/datasets/views/{viewDatasetRid} | Stable |
[**remove_backing_datasets**](#remove_backing_datasets) | **POST** /v2/datasets/views/{viewDatasetRid}/removeBackingDatasets | Stable |
[**replace_backing_datasets**](#replace_backing_datasets) | **PUT** /v2/datasets/views/{viewDatasetRid}/replaceBackingDatasets | Stable |

# **add_backing_datasets**
Adds one or more backing datasets to a View. Any duplicates with the same dataset RID and branch name are 
ignored.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**view_dataset_rid** | DatasetRid | The rid of the View. |  |
**backing_datasets** | List[ViewBackingDataset] |  |  |
**branch** | Optional[BranchName] |  | [optional] |

### Return type
**View**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | The rid of the View.
view_dataset_rid = None
# List[ViewBackingDataset]
backing_datasets = [
    {
        "datasetRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
        "stopPropagatingMarkingIds": ["18212f9a-0e63-4b79-96a0-aae04df23336"],
        "branch": "master",
    }
]
# Optional[BranchName]
branch = "master"


try:
    api_response = client.datasets.View.add_backing_datasets(
        view_dataset_rid, backing_datasets=backing_datasets, branch=branch
    )
    print("The add_backing_datasets response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling View.add_backing_datasets: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | View  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **add_primary_key**
Adds a primary key to a View that does not already have one. Primary keys are treated as 
guarantees provided by the creator of the dataset.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**view_dataset_rid** | DatasetRid | The rid of the View. |  |
**primary_key** | ViewPrimaryKey |  |  |
**branch** | Optional[BranchName] |  | [optional] |

### Return type
**View**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | The rid of the View.
view_dataset_rid = None
# ViewPrimaryKey
primary_key = {
    "columns": ["colA"],
    "resolution": {
        "type": "duplicate",
        "deletionColumn": "deletionCol",
        "resolutionStrategy": {"type": "latestWins", "columns": ["colB", "colC"]},
    },
}
# Optional[BranchName]
branch = "master"


try:
    api_response = client.datasets.View.add_primary_key(
        view_dataset_rid, primary_key=primary_key, branch=branch
    )
    print("The add_primary_key response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling View.add_primary_key: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | View  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **create**
Create a new View.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**backing_datasets** | List[ViewBackingDataset] |  |  |
**parent_folder_rid** | FolderRid |  |  |
**view_name** | DatasetName |  |  |
**branch** | Optional[BranchName] | The branch name of the View. If not specified, defaults to `master` for most enrollments. | [optional] |
**primary_key** | Optional[ViewPrimaryKey] |  | [optional] |

### Return type
**View**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[ViewBackingDataset]
backing_datasets = [
    {
        "datasetRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
        "stopPropagatingMarkingIds": ["18212f9a-0e63-4b79-96a0-aae04df23336"],
        "branch": "master",
    }
]
# FolderRid
parent_folder_rid = "ri.compass.main.folder.c410f510-2937-420e-8ea3-8c9bcb3c1791"
# DatasetName
view_name = "My Dataset"
# Optional[BranchName] | The branch name of the View. If not specified, defaults to `master` for most enrollments.
branch = "master"
# Optional[ViewPrimaryKey]
primary_key = {"columns": ["order_id"]}


try:
    api_response = client.datasets.View.create(
        backing_datasets=backing_datasets,
        parent_folder_rid=parent_folder_rid,
        view_name=view_name,
        branch=branch,
        primary_key=primary_key,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling View.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | View  | The created View | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get metadata for a View.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**view_dataset_rid** | DatasetRid | The rid of the View. |  |
**branch** | Optional[BranchName] |  | [optional] |

### Return type
**View**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | The rid of the View.
view_dataset_rid = None
# Optional[BranchName]
branch = None


try:
    api_response = client.datasets.View.get(view_dataset_rid, branch=branch)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling View.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | View  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **remove_backing_datasets**
Removes specified backing datasets from a View. Removing a dataset triggers a 
[SNAPSHOT](https://palantir.com/docs/foundry/data-integration/datasets#snapshot) transaction on the next update. If a 
specified dataset does not exist, no error is thrown.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**view_dataset_rid** | DatasetRid | The rid of the View. |  |
**backing_datasets** | List[ViewBackingDataset] |  |  |
**branch** | Optional[BranchName] |  | [optional] |

### Return type
**View**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | The rid of the View.
view_dataset_rid = None
# List[ViewBackingDataset]
backing_datasets = [
    {
        "datasetRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
        "stopPropagatingMarkingIds": ["18212f9a-0e63-4b79-96a0-aae04df23336"],
        "branch": "master",
    }
]
# Optional[BranchName]
branch = "master"


try:
    api_response = client.datasets.View.remove_backing_datasets(
        view_dataset_rid, backing_datasets=backing_datasets, branch=branch
    )
    print("The remove_backing_datasets response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling View.remove_backing_datasets: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | View  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace_backing_datasets**
Replaces the backing datasets for a View. Removing any backing dataset triggers a
[SNAPSHOT](https://palantir.com/docs/foundry/data-integration/datasets#snapshot) transaction the next time the View is updated.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**view_dataset_rid** | DatasetRid | The rid of the View. |  |
**backing_datasets** | List[ViewBackingDataset] |  |  |
**branch** | Optional[BranchName] |  | [optional] |

### Return type
**View**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid | The rid of the View.
view_dataset_rid = None
# List[ViewBackingDataset]
backing_datasets = [
    {
        "datasetRid": "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
        "stopPropagatingMarkingIds": ["18212f9a-0e63-4b79-96a0-aae04df23336"],
        "branch": "master",
    }
]
# Optional[BranchName]
branch = "master"


try:
    api_response = client.datasets.View.replace_backing_datasets(
        view_dataset_rid, backing_datasets=backing_datasets, branch=branch
    )
    print("The replace_backing_datasets response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling View.replace_backing_datasets: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | View  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

