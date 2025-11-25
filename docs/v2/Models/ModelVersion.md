# ModelVersion

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/models/{modelRid}/versions | Private Beta |
[**get**](#get) | **GET** /v2/models/{modelRid}/versions/{modelVersionRid} | Private Beta |
[**list**](#list) | **GET** /v2/models/{modelRid}/versions | Private Beta |

# **create**
Creates a new Model Version on an existing model.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**backing_repositories** | List[RID] |  |  |
**conda_requirements** | List[str] |  |  |
**model_api** | ModelApi |  |  |
**model_files** | ModelFiles |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ModelVersion**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelRid
model_rid = None
# List[RID]
backing_repositories = None
# List[str]
conda_requirements = None
# ModelApi
model_api = {
    "inputs": [
        {
            "name": "input_df",
            "required": True,
            "type": "tabular",
            "columns": [
                {"name": "feature_1", "required": True, "dataType": {"type": "double"}},
                {"name": "feature_2", "required": True, "dataType": {"type": "integer"}},
            ],
            "format": "PANDAS",
        }
    ],
    "outputs": [
        {
            "name": "output_df",
            "required": True,
            "type": "tabular",
            "columns": [{"name": "prediction", "required": True, "dataType": {"type": "double"}}],
            "format": "SPARK",
        }
    ],
}
# ModelFiles
model_files = {
    "type": "dill",
    "serializedModelFunction": "base64-encoded string for a dill-serialize model function",
}
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.Model.Version.create(
        model_rid,
        backing_repositories=backing_repositories,
        conda_requirements=conda_requirements,
        model_api=model_api,
        model_files=model_files,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Version.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ModelVersion  | The created ModelVersion | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Retrieves a Model Version by its Resource Identifier (RID).

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**model_version_rid** | ModelVersionRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ModelVersion**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelRid
model_rid = None
# ModelVersionRid
model_version_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.Model.Version.get(model_rid, model_version_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Version.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ModelVersion  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all Model Versions for a given Model.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**ListModelVersionsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelRid
model_rid = None
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    for model_version in client.models.Model.Version.list(
        model_rid, page_size=page_size, page_token=page_token, preview=preview
    ):
        pprint(model_version)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Version.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListModelVersionsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

