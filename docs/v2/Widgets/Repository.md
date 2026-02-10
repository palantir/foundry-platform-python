# Repository

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/widgets/repositories/{repositoryRid} | Private Beta |
[**publish**](#publish) | **POST** /v2/widgets/repositories/{repositoryRid}/publish | Private Beta |

# **get**
Get the Repository with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**repository_rid** | RepositoryRid | A Resource Identifier (RID) identifying a repository. |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Repository**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# RepositoryRid | A Resource Identifier (RID) identifying a repository.
repository_rid = "ri.stemma.main.repository.e1r31370-3cf3-4ac4-9269-h1432d7fb0b4"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.widgets.Repository.get(repository_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Repository.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Repository  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **publish**
Publish a new release of a widget set.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**repository_rid** | RepositoryRid | A Resource Identifier (RID) identifying a repository. |  |
**body** | bytes | The zip file that contains the contents of your widget set. It must include a valid manifest file at the path `.palantir/widgets.config.json`.  |  |
**repository_version** | RepositoryVersion |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Release**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# RepositoryRid | A Resource Identifier (RID) identifying a repository.
repository_rid = "ri.stemma.main.repository.e1r31370-3cf3-4ac4-9269-h1432d7fb0b4"
# bytes | The zip file that contains the contents of your widget set. It must include a valid manifest file at the path `.palantir/widgets.config.json`.
body = None
# RepositoryVersion
repository_version = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.widgets.Repository.publish(
        repository_rid, body, repository_version=repository_version, preview=preview
    )
    print("The publish response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Repository.publish: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Release  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

