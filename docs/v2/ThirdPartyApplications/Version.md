# Version

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**delete**](#delete) | **DELETE** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion} | Stable |
[**get**](#get) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion} | Stable |
[**list**](#list) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions | Stable |
[**upload**](#upload) | **POST** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/upload | Stable |
[**upload_snapshot**](#upload_snapshot) | **POST** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/uploadSnapshot | Private Beta |

# **delete**
Delete the Version with the specified version.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | An RID identifying a third-party application created in Developer Console. |  |
**version_version** | VersionVersion | The semantic version of the Website. |  |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ThirdPartyApplicationRid | An RID identifying a third-party application created in Developer Console.
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# VersionVersion | The semantic version of the Website.
version_version = "1.2.0"


try:
    api_response = client.third_party_applications.ThirdPartyApplication.Website.Version.delete(
        third_party_application_rid, version_version
    )
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
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
**third_party_application_rid** | ThirdPartyApplicationRid | An RID identifying a third-party application created in Developer Console. |  |
**version_version** | VersionVersion | The semantic version of the Website. |  |

### Return type
**Version**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ThirdPartyApplicationRid | An RID identifying a third-party application created in Developer Console.
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# VersionVersion | The semantic version of the Website.
version_version = "1.2.0"


try:
    api_response = client.third_party_applications.ThirdPartyApplication.Website.Version.get(
        third_party_application_rid, version_version
    )
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
**200** | Version  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all Versions.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | An RID identifying a third-party application created in Developer Console. |  |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |

### Return type
**ListVersionsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ThirdPartyApplicationRid | An RID identifying a third-party application created in Developer Console.
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None


try:
    for version in client.third_party_applications.ThirdPartyApplication.Website.Version.list(
        third_party_application_rid, page_size=page_size, page_token=page_token
    ):
        pprint(version)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Version.list: %s\n" % e)

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
**third_party_application_rid** | ThirdPartyApplicationRid | An RID identifying a third-party application created in Developer Console. |  |
**body** | bytes | The zip file that contains the contents of your application. For more information,  refer to the [documentation](https://palantir.com/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.  |  |
**version** | VersionVersion |  |  |

### Return type
**Version**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ThirdPartyApplicationRid | An RID identifying a third-party application created in Developer Console.
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# bytes | The zip file that contains the contents of your application. For more information,  refer to the [documentation](https://palantir.com/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
body = None
# VersionVersion
version = None


try:
    api_response = client.third_party_applications.ThirdPartyApplication.Website.Version.upload(
        third_party_application_rid, body, version=version
    )
    print("The upload response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Version.upload: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Version  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **upload_snapshot**
Upload a snapshot version of the Website. Snapshot versions are automatically deleted after two days.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**third_party_application_rid** | ThirdPartyApplicationRid | An RID identifying a third-party application created in Developer Console. |  |
**body** | bytes | The zip file that contains the contents of your application. For more information,  refer to the [documentation](https://palantir.com/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.  |  |
**version** | VersionVersion |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**snapshot_identifier** | Optional[str] | The identifier of the snapshot. If the identifier follows the format `foundry.v1@<repositoryRid>@<pullRequestRid>@<commitHash>`, PR preview for such identifier will be accessible from foundry code repositories.  | [optional] |

### Return type
**Version**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ThirdPartyApplicationRid | An RID identifying a third-party application created in Developer Console.
third_party_application_rid = (
    "ri.third-party-applications.main.application.292db3b2-b653-4de6-971c-7e97a7b881d6"
)
# bytes | The zip file that contains the contents of your application. For more information,  refer to the [documentation](https://palantir.com/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/) user documentation.
body = None
# VersionVersion
version = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[str] | The identifier of the snapshot. If the identifier follows the format `foundry.v1@<repositoryRid>@<pullRequestRid>@<commitHash>`, PR preview for such identifier will be accessible from foundry code repositories.
snapshot_identifier = (
    "foundry.v1@ri.stemma.main.repository.a@ri.pull-request.main.pull-request.a@hash"
)


try:
    api_response = (
        client.third_party_applications.ThirdPartyApplication.Website.Version.upload_snapshot(
            third_party_application_rid,
            body,
            version=version,
            preview=preview,
            snapshot_identifier=snapshot_identifier,
        )
    )
    print("The upload_snapshot response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Version.upload_snapshot: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Version  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

