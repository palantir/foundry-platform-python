# User

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**delete**](#delete) | **DELETE** /v2/admin/users/{userId} | Stable |
[**get**](#get) | **GET** /v2/admin/users/{userId} | Stable |
[**get_batch**](#get_batch) | **POST** /v2/admin/users/getBatch | Stable |
[**get_current**](#get_current) | **GET** /v2/admin/users/getCurrent | Stable |
[**get_markings**](#get_markings) | **GET** /v2/admin/users/{userId}/getMarkings | Public Beta |
[**list**](#list) | **GET** /v2/admin/users | Stable |
[**page**](#page) | **GET** /v2/admin/users | Stable |
[**profile_picture**](#profile_picture) | **GET** /v2/admin/users/{userId}/profilePicture | Stable |
[**search**](#search) | **POST** /v2/admin/users/search | Stable |

# **delete**
Delete the User with the specified id.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | str |  |  |

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

# str
user_id = None


try:
    api_response = foundry_client.admin.User.delete(
        user_id,
    )
    print("The delete response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling User.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the User with the specified id.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | str |  |  |

### Return type
**User**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# str
user_id = None


try:
    api_response = foundry_client.admin.User.get(
        user_id,
    )
    print("The get response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling User.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | User  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_batch**
Execute multiple get requests on User.

The maximum batch size for this endpoint is 500.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**body** | List[Union[GetUsersBatchRequestElement, GetUsersBatchRequestElementDict]] | Body of the request |  |

### Return type
**GetUsersBatchResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# List[Union[GetUsersBatchRequestElement, GetUsersBatchRequestElementDict]] | Body of the request
body = [{"userId": "f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]


try:
    api_response = foundry_client.admin.User.get_batch(
        body,
    )
    print("The get_batch response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling User.get_batch: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetUsersBatchResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_current**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |

### Return type
**User**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)


try:
    api_response = foundry_client.admin.User.get_current()
    print("The get_current response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling User.get_current: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | User  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_markings**
Retrieve Markings that the user is currently a member of.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | str |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**GetUserMarkingsResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# str
user_id = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = foundry_client.admin.User.get_markings(
        user_id,
        preview=preview,
    )
    print("The get_markings response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling User.get_markings: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetUserMarkingsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **list**
Lists all Users.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |

### Return type
**ListUsersResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None


try:
    for user in foundry_client.admin.User.list(
        page_size=page_size,
        page_token=page_token,
    ):
        pprint(user)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling User.list: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListUsersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **page**
Lists all Users.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**page_size** | Optional[PageSize] | The page size to use for the endpoint. | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. | [optional] |

### Return type
**ListUsersResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Optional[PageSize] | The page size to use for the endpoint.
page_size = None
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
page_token = None


try:
    api_response = foundry_client.admin.User.page(
        page_size=page_size,
        page_token=page_token,
    )
    print("The page response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling User.page: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ListUsersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **profile_picture**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**user_id** | str |  |  |

### Return type
**Optional[bytes]**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# str
user_id = None


try:
    api_response = foundry_client.admin.User.profile_picture(
        user_id,
    )
    print("The profile_picture response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling User.profile_picture: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Optional[bytes]  | The user's profile picture in binary format. The format is the original format uploaded by the user.  The response will contain a `Content-Type` header that can be used to identify the media type.  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **search**
Perform a case-insensitive prefix search for users based on username, given name and family name.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**where** | Union[UserSearchFilter, UserSearchFilterDict] |  |  |
**page_size** | Optional[PageSize] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |

### Return type
**SearchUsersResponse**

### Example

```python
from foundry.v2 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# Union[UserSearchFilter, UserSearchFilterDict]
where = {"type": "queryString"}
# Optional[PageSize]
page_size = 100
# Optional[PageToken]
page_token = "v1.QnVpbGQgdGhlIEZ1dHVyZTogaHR0cHM6Ly93d3cucGFsYW50aXIuY29tL2NhcmVlcnMvP2xldmVyLXNvdXJjZSU1YiU1ZD1BUElEb2NzI29wZW4tcG9zaXRpb25z"


try:
    api_response = foundry_client.admin.User.search(
        where=where,
        page_size=page_size,
        page_token=page_token,
    )
    print("The search response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling User.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchUsersResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

