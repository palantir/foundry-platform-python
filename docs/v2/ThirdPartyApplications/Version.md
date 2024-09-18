# Version

Method | HTTP request |
------------- | ------------- |
[**delete**](#delete) | **DELETE** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion} |
[**get**](#get) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion} |
[**list**](#list) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions |
[**page**](#page) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions |
[**upload**](#upload) | **POST** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/upload |

# **delete**
Delete the Version with the specified version.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | thirdPartyApplicationRid |  |
**version_version** | VersionVersion | versionVersion |  |
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

# ThirdPartyApplicationRid | thirdPartyApplicationRid
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# VersionVersion | versionVersion
version_version = "1.2.0"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = (
        foundry_client.third_party_applications.ThirdPartyApplication.Website.Version.delete(
            third_party_application_rid,
            version_version,
            preview=preview,
        )
    )
    print("The delete response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Version.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Version with the specified version.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | thirdPartyApplicationRid |  |
**version_version** | VersionVersion | versionVersion |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Version**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ThirdPartyApplicationRid | thirdPartyApplicationRid
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# VersionVersion | versionVersion
version_version = "1.2.0"
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = (
        foundry_client.third_party_applications.ThirdPartyApplication.Website.Version.get(
            third_party_application_rid,
            version_version,
            preview=preview,
        )
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Version.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Version  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all Versions.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | thirdPartyApplicationRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ResourceIterator[Version]**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ThirdPartyApplicationRid | thirdPartyApplicationRid
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# Optional[PageSize] | pageSize
page_size = None
# Optional[PreviewMode] | preview
preview = None


try:
    for (
        version
    ) in foundry_client.third_party_applications.ThirdPartyApplication.Website.Version.list(
        third_party_application_rid,
        page_size=page_size,
        preview=preview,
    ):
        pprint(version)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Version.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListVersionsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
Lists all Versions.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | thirdPartyApplicationRid |  |
**page_size** | Optional[PageSize] | pageSize | [optional] |
**page_token** | Optional[PageToken] | pageToken | [optional] |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**ListVersionsResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ThirdPartyApplicationRid | thirdPartyApplicationRid
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# Optional[PageSize] | pageSize
page_size = None
# Optional[PageToken] | pageToken
page_token = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = (
        foundry_client.third_party_applications.ThirdPartyApplication.Website.Version.page(
            third_party_application_rid,
            page_size=page_size,
            page_token=page_token,
            preview=preview,
        )
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Version.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListVersionsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **upload**
Upload a new version of the Website.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | thirdPartyApplicationRid |  |
**body** | bytes | The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.  |  |
**version** | VersionVersion | version |  |
**preview** | Optional[PreviewMode] | preview | [optional] |

### Return type
**Version**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# ThirdPartyApplicationRid | thirdPartyApplicationRid
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# bytes | The zip file that contains the contents of your application. For more information,  refer to the [documentation](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
body = None
# VersionVersion | version
version = None
# Optional[PreviewMode] | preview
preview = None


try:
    api_response = (
        foundry_client.third_party_applications.ThirdPartyApplication.Website.Version.upload(
            third_party_application_rid,
            body,
            version=version,
            preview=preview,
        )
    )
    print("The upload response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Version.upload: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Version  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

