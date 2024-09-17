# Website

Method | HTTP request |
------------- | ------------- |
[**deploy**](#deploy) | **POST** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/deploy |
[**get**](#get) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website |
[**undeploy**](#undeploy) | **POST** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/undeploy |

# **deploy**
Deploy a version of the Website.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | thirdPartyApplicationRid |  |
**version** | VersionVersion |  |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Website**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ThirdPartyApplicationRid | thirdPartyApplicationRid
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# VersionVersion |
version = "1.2.0"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.third_party_applications.ThirdPartyApplication.Website.deploy(
        third_party_application_rid,
        version=version,
        preview=preview,
    )
    print("The deploy response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Website.deploy: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Website  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Website.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | thirdPartyApplicationRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Website**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ThirdPartyApplicationRid | thirdPartyApplicationRid
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.third_party_applications.ThirdPartyApplication.Website.get(
        third_party_application_rid,
        preview=preview,
    )
    print("The get response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Website.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Website  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **undeploy**
Remove the currently deployed version of the Website.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | thirdPartyApplicationRid |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Website**

### Example

```python
from foundry.v2 import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ThirdPartyApplicationRid | thirdPartyApplicationRid
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = foundry_client.third_party_applications.ThirdPartyApplication.Website.undeploy(
        third_party_application_rid,
        preview=preview,
    )
    print("The undeploy response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Website.undeploy: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Website  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

