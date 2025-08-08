# Foundry Platform SDK

![Supported Python Versions](https://img.shields.io/pypi/pyversions/foundry-platform-sdk)
[![PyPI Version](https://img.shields.io/pypi/v/foundry-platform-sdk)](https://pypi.org/project/foundry-platform-sdk/)
[![License](https://img.shields.io/badge/License-Apache%202.0-lightgrey.svg)](https://opensource.org/licenses/Apache-2.0)

The Foundry Platform SDK is a Python SDK built on top of the Foundry API.
Review [Foundry API documentation](https://www.palantir.com/docs/foundry/api/) for more details.

> [!NOTE]
> This Python package is automatically generated based on the Foundry API specification.


<a id="sdk-vs-sdk"></a>
## Gotham Platform SDK vs. Foundry Platform SDK vs. Ontology SDK
Palantir provides two platform APIs for interacting with the Gotham and Foundry platforms. Each has a corresponding Software Development Kit (SDK). There is also the OSDK for interacting with Foundry ontologies. Make sure to choose the correct SDK for your use case. As a general rule of thumb, any applications which leverage the Ontology should use the Ontology SDK over the Foundry platform SDK for a superior development experience.

> [!IMPORTANT]
> Make sure to understand the difference between the Foundry, Gotham, and Ontology SDKs. Review this section before continuing with the installation of this library.

### Ontology SDK
The Ontology SDK allows you to access the full power of the Ontology directly from your development environment. You can generate the Ontology SDK using the Developer Console, a portal for creating and managing applications using Palantir APIs. Review the [Ontology SDK documentation](https://www.palantir.com/docs/foundry/ontology-sdk) for more information.

### Foundry Platform SDK
The Foundry Platform Software Development Kit (SDK) is generated from the Foundry API specification
file. The intention of this SDK is to encompass endpoints related to interacting
with the Foundry platform itself. Although there are Ontology services included by this SDK, this SDK surfaces endpoints
for interacting with Ontological resources such as object types, link types, and action types. In contrast, the OSDK allows you to interact with objects, links and Actions (for example, querying your objects, applying an action).

### Gotham Platform SDK
The Gotham Platform Software Development Kit (SDK) is generated from the Gotham API specification
file. The intention of this SDK is to encompass endpoints related to interacting
with the Gotham platform itself. This includes Gotham apps and data, such as Gaia, Target Workbench, and geotemporal data.

<a id="installation"></a>
## Installation
You can install the Python package using `pip`:

```sh
pip install foundry-platform-sdk
```

<a id="major-version-link"></a>
## API Versioning
Every endpoint of the Foundry API is versioned using a version number that appears in the URL. For example,
v1 endpoints look like this:

```
https://<hostname>/api/v1/...
```

This SDK exposes several clients, one for each major version of the API. The latest major version of the
SDK is **v2** and is exposed using the `FoundryClient` located in the
`foundry_sdk` package.

```python
from foundry_sdk import FoundryClient
```

For other major versions, you must import that specific client from a submodule. For example, to
import the **v2** client from a sub-module you would import it like this:

```python
from foundry_sdk.v2 import FoundryClient
```

More information about how the API is versioned can be found [here](https://www.palantir.com/docs/foundry/api/general/overview/versioning/).

<a id="authorization"></a>
## Authorization and client initalization
There are two options for authorizing the SDK.

### User token
> [!WARNING]
> User tokens are associated with your personal user account and must not be used in
> production applications or committed to shared or public code repositories. We recommend
> you store test API tokens as environment variables during development. For authorizing
> production applications, you should register an OAuth2 application (see
> [OAuth2 Client](#oauth2-client) below for more details).

You can pass in a user token as an arguments when initializing the `UserTokenAuth`:

```python
import foundry_sdk

client = foundry_sdk.FoundryClient(
    auth=foundry_sdk.UserTokenAuth(os.environ["BEARER_TOKEN"]),
    hostname="example.palantirfoundry.com",
)

```

For convenience, the auth and hostname can also be set using environmental or context variables.
The `auth` and `hostname` parameters are set (in order of precedence) by:

- The parameters passed to the `FoundryClient` constructor
- Context variables `FOUNDRY_TOKEN` and `FOUNDRY_HOSTNAME`
- Environment variables `FOUNDRY_TOKEN` and `FOUNDRY_HOSTNAME`

The `FOUNDRY_TOKEN` is a string of an users Bearer token, which will create a `UserTokenAuth` for the `auth` parameter.

```python
import foundry_sdk

# The SDK will initialize the following context or environment variables when auth and hostname are not provided:
# FOUNDRY_TOKEN
# FOUNDRY_HOSTNAME
client = foundry_sdk.FoundryClient()
`
```

<a id="oauth2-client"></a>
### OAuth2 Client
OAuth2 clients are the recommended way to connect to Foundry in production applications. Currently, this SDK
natively supports the [client credentials grant flow](https://www.palantir.com/docs/foundry/platform-security-third-party/writing-oauth2-clients/#client-credentials-grant).
The token obtained by this grant can be used to access resources on behalf of the created service user. To use this
authentication method, you will first need to register a third-party application in Foundry by following [the guide on third-party application registration](https://www.palantir.com/docs/foundry/platform-security-third-party/register-3pa).

To use the confidential client functionality, you first need to construct a
`ConfidentialClientAuth` object. As these service user tokens have a short
lifespan (one hour), we automatically retry all operations one time if a `401`
(Unauthorized) error is thrown after refreshing the token.

```python
import foundry_sdk

auth = foundry_sdk.ConfidentialClientAuth(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    scopes=[...],  # optional list of scopes
)

```

> [!IMPORTANT]
> Make sure to select the appropriate scopes when initializating the `ConfidentialClientAuth`. You can find the relevant scopes
> in the [endpoint documentation](#apis-link).

After creating the `ConfidentialClientAuth` object, pass it in to the `FoundryClient`,

```python
import foundry_sdk

client = foundry_sdk.FoundryClient(auth=auth, hostname="example.palantirfoundry.com")

```

> [!TIP]
> If you want to use the `ConfidentialClientAuth` class independently of the `FoundryClient`, you can
> use the `get_token()` method to get the token. You will have to provide a `hostname` when
> instantiating the `ConfidentialClientAuth` object, for example
> `ConfidentialClientAuth(..., hostname="example.palantirfoundry.com")`.

## Quickstart

Follow the [installation procedure](#installation) and determine which [authentication method](#authorization) is
best suited for your instance before following this example. For simplicity, the `UserTokenAuth` class will be used for demonstration
purposes.

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# DatasetRid
dataset_rid = None
# BranchName
name = "master"
# Optional[TransactionRid] | The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction.
transaction_rid = "ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4"


try:
    api_response = client.datasets.Dataset.Branch.create(
        dataset_rid, name=name, transaction_rid=transaction_rid
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Branch.create: %s\n" % e)

```

Want to learn more about this Foundry SDK library? Review the following sections.

↳ [Error handling](#errors): Learn more about HTTP & data validation error handling  
↳ [Pagination](#pagination): Learn how to work with paginated endpoints in the SDK  
↳ [Streaming](#binary-streaming): Learn how to stream binary data from Foundry  
↳ [Static type analysis](#static-types): Learn about the static type analysis capabilities of this library  
↳ [HTTP Session Configuration](#session-config): Learn how to configure the HTTP session.  

<a id="errors"></a>
## Error handling
### Data validation
The SDK employs [Pydantic](https://docs.pydantic.dev/latest/) for runtime validation
of arguments. In the example below, we are passing in a number to `transaction_rid`
which should actually be a string type:

```python
client.datasets.Dataset.Branch.create(
	dataset_rid, 
	name=name, 
	transaction_rid=123)
```

If you did this, you would receive an error that looks something like:

```python
pydantic_core._pydantic_core.ValidationError: 1 validation error for create
transaction_rid
  Input should be a valid string [type=string_type, input_value=123, input_type=int]
    For further information visit https://errors.pydantic.dev/2.5/v/string_type

```

To handle these errors, you can catch `pydantic.ValidationError`. To learn more, see
the [Pydantic error documentation](https://docs.pydantic.dev/latest/errors/errors/).

> [!TIP]
> Pydantic works with static type checkers such as
[pyright](https://github.com/microsoft/pyright) for an improved developer
experience. See [Static Type Analysis](#static-types) below for more information.

### HTTP exceptions
Each operation includes a list of possible exceptions that can be thrown which can be thrown by the server, all of which inherit from `PalantirRPCException`. For example, an operation that interacts with dataset branches might throw a `BranchNotFound` error, which is defined as follows:

```python
class BranchNotFoundParameters(typing_extensions.TypedDict):
    """The requested branch could not be found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    datasetRid: datasets_models.DatasetRid
    branchName: datasets_models.BranchName


@dataclass
class BranchNotFound(errors.NotFoundError):
    name: typing.Literal["BranchNotFound"]
    parameters: BranchNotFoundParameters
    error_instance_id: str

```

As a user, you can catch this exception and handle it accordingly.

```python
from foundry_sdk.v1.datasets.errors import BranchNotFound

try:
    response = client.datasets.Dataset.get(dataset_rid)
    ...
except BranchNotFound as e:
    print("Resource not found", e.parameters[...])

```

You can refer to the method documentation to see which exceptions can be thrown. It is also possible to
catch a generic subclass of `PalantirRPCException` such as `BadRequestError` or `NotFoundError`.


| Status Code | Error Class                  |
| ----------- | ---------------------------- |
| 400         | `BadRequestError`            |
| 401         | `UnauthorizedError`          |
| 403         | `PermissionDeniedError`      |
| 404         | `NotFoundError`              |
| 413         | `RequestEntityTooLargeError` |
| 422         | `UnprocessableEntityError`   |
| 429         | `RateLimitError`             |
| >=500,<600  | `InternalServerError`        |
| Other       | `PalantirRPCException`       |

```python
from foundry_sdk import PalantirRPCException
from foundry_sdk import NotFoundError

try:
    api_response = client.datasets.Dataset.get(dataset_rid)
    ...
except NotFoundError as e:
    print("Resource not found", e)
except PalantirRPCException as e:
    print("Another HTTP exception occurred", e)

```

All HTTP exceptions will have the following properties. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors) for details about the Foundry error information.

| Property          | Type                   | Description                                                                                                                                                       |
| ----------------- | -----------------------| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name              | str                    | The Palantir error name. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors).        |
| error_instance_id | str                    | The Palantir error instance ID. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors). |
| parameters        | Dict[str, Any]         | The Palantir error parameters. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors).  |

### Other exceptions
There are a handful of other exception classes that could be thrown when instantiating or using a client.

| ErrorClass                 | Thrown Directly | Description                                                                                                                       |
| -------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------- |     
| NotAuthenticated           | Yes             | You used either `ConfidentialClientAuth` or `PublicClientAuth` to make an API call without going through the OAuth process first. |           
| ConnectionError            | Yes             | An issue occurred when connecting to the server. This also catches `ProxyError`.                                                  |
| ProxyError                 | Yes             | An issue occurred when connecting to or authenticating with a proxy server.                                                       |
| TimeoutError               | No              | The request timed out. This catches both `ConnectTimeout`, `ReadTimeout` and `WriteTimeout`.                                      |
| ConnectTimeout             | Yes             | The request timed out when attempting to connect to the server.                                                                   |
| ReadTimeout                | Yes             | The server did not send any data in the allotted amount of time.                                                                  |
| WriteTimeout               | Yes             | There was a timeout when writing data to the server.                                                                              |
| StreamConsumedError        | Yes             | The content of the given stream has already been consumed.                                                                        |
| RequestEntityTooLargeError | Yes             | The request entity is too large.                                                                                                  |
| ConflictError              | Yes             | There was a conflict with another request.                                                                                        |
| SDKInternalError           | Yes             | An unexpected issue occurred and should be reported.                                                                              |

<a id="pagination"></a>
## Pagination
When calling any iterator endpoints, we return a `ResourceIterator` class designed to simplify the process of working
with paginated API endpoints. This class provides a convenient way to fetch, iterate over, and manage pages
of data, while handling the underlying pagination logic.

To iterate over all items, you can simply create a `ResourceIterator` instance and use it in a for loop, like this:

```python
for item in client.datasets.Dataset.Branch.list(dataset_rid):
    print(item)

# Or, you can collect all the items in a list
results = list(client.datasets.Dataset.Branch.list(dataset_rid))

```

This will automatically fetch and iterate through all the pages of data from the specified API endpoint. For more granular control, you can manually fetch each page using the `next_page_token`.

```python
next_page_token: Optional[str] = None
while True:
    page = client.datasets.Dataset.Branch.list(
        dataset_rid, page_size=page_size, page_token=next_page_token
    )
    for branch in page.data:
        print(branch)

    if page.next_page_token is None:
        break

    next_page_token = page.next_page_token

```

### Asynchronous Pagination (Beta)

> [!WARNING]
> The asynchronous client is in beta and may change in future releases.

When using the `AsyncFoundryClient` client, pagination works similar to the synchronous client
but you need to use `async for` to iterate over the results. Here's an example:


```python
async for item in client.datasets.Dataset.Branch.list(dataset_rid):
    print(item)

# Or, you can collect all the items in a list
results = [item async for item in client.datasets.Dataset.Branch.list(dataset_rid)]

```

For more control over asynchronous pagination, you can manually handle the pagination
tokens and use the `with_raw_response` utility to fetch each page.


```python
next_page_token: Optional[str] = None
while True:
    response = await client.client.datasets.Dataset.Branch.with_raw_response.list(
        dataset_rid, page_token=next_page_token
    )

    page = response.decode()
    for item in page.data:
        print(item)

    if page.next_page_token is None:
        break

    next_page_token = page.next_page_token

```

<a id="async-client"></a>
### Asynchronous Client (Beta)

> [!WARNING]
> The asynchronous client is in beta and may change in future releases.

This SDK supports creating an asynchronous client, just import and instantiate the
`AsyncFoundryClient` instead of the `FoundryClient`.

```python
from foundry import AsyncFoundryClient
import foundry
import asyncio
from pprint import pprint

async def main():
    client = AsyncFoundryClient(...)
    response = await client.datasets.Dataset.Branch.create(dataset_rid, name=name, transaction_rid=transaction_rid)
    pprint(response)

if __name__ == "__main__":
    asyncio.run(main())
```

When using asynchronous clients, you'll just need to use the `await` keyword when calling APIs. Otherwise, the behaviour
between the `FoundryClient` and `AsyncFoundryClient` is nearly identical.

<a id="binary-streaming"></a>
## Streaming
This SDK supports streaming binary data using a separate streaming client accessible under
`with_streaming_response` on each Resource. To ensure the stream is closed, you need to use a context
manager when making a request with this client.

```python
# Non-streaming response
with open("result.png", "wb") as f:
    f.write(client.admin.User.profile_picture(user_id))

# Streaming response
with open("result.png", "wb") as f:
    with client.admin.User.with_streaming_response.profile_picture(user_id) as response:
        for chunk in response.iter_bytes():
            f.write(chunk)

```

<a id="static-types"></a>
## Static type analysis
This library uses [Pydantic](https://docs.pydantic.dev) for creating and validating data models which you will see in the
method definitions (see [Documentation for Models](#models-link) below for a full list of models).
All request parameters and responses with nested fields are typed using a Pydantic
[`BaseModel`](https://docs.pydantic.dev/latest/api/base_model/) class. For example, here is how
`Group.search` method is defined in the `Admin` namespace:

```python
    @pydantic.validate_call
    @handle_unexpected
    def search(
        self,
        *,
        where: GroupSearchFilter,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[int, pydantic.Field(gt=0)]] = None,
    ) -> SearchGroupsResponse:
        ...

```

```python
import foundry_sdk
from foundry_sdk.v2.admin.models import GroupSearchFilter

client = foundry_sdk.FoundryClient(...)

result = client.admin.Group.search(where=GroupSearchFilter(type="queryString", value="John Doe"))
print(result.data)

```

If you are using a static type checker (for example, [mypy](https://mypy-lang.org), [pyright](https://github.com/microsoft/pyright)), you
get static type analysis for the arguments you provide to the function and with the response. For example, if you pass an `int`
to `name` but `name` expects a string or if you try to access `branchName` on the returned [`Branch`](docs/Branch.md) object (the
property is actually called `name`), you will get the following errors:


```python
branch = client.datasets.Dataset.Branch.create(
    "ri.foundry.main.dataset.abc",
    # ERROR: "Literal[123]" is incompatible with "BranchName"
    name=123,
)
# ERROR: Cannot access member "branchName" for type "Branch"
print(branch.branchName)

```

<a id="session-config"></a>
## HTTP Session Configuration
You can configure various parts of the HTTP session using the `Config` class.

```python
from foundry_sdk import Config
from foundry_sdk import UserTokenAuth
from foundry_sdk import FoundryClient

client = FoundryClient(
    auth=UserTokenAuth(...),
    hostname="example.palantirfoundry.com",
    config=Config(
        # Set the default headers for every request
        default_headers={"Foo": "Bar"},
        # Default to a 60 second timeout
        timeout=60,
        # Create a proxy for the https protocol
        proxies={"https": "https://10.10.1.10:1080"},
    ),
)

```

The full list of options can be found below.

- `default_headers` (dict[str, str]): HTTP headers to include with all requests.
- `proxies` (dict["http" | "https", str]): Proxies to use for HTTP and HTTPS requests.
- `timeout` (int | float): The default timeout for all requests in seconds.
- `verify` (bool | str): SSL verification, can be a boolean or a path to a CA bundle. Defaults to `True`.
- `default_params` (dict[str, Any]): URL query parameters to include with all requests.
- `scheme` ("http" | "https"): URL scheme to use ('http' or 'https'). Defaults to 'https'.

### SSL Certificate Verification

In addition to the `Config` class, the SSL certificate file used for verification can be set using
the following environment variables (in order of precedence):
- **`REQUESTS_CA_BUNDLE`**
- **`SSL_CERT_FILE`**

The SDK will only check for the presence of these environment variables if the `verify` option is set to
`True` (the default value). If `verify` is set to False, the environment variables will be ignored.

> [!IMPORTANT]
> If you are using an HTTPS proxy server, the `verify` value will be passed to the proxy's
> SSL context as well.

## Common errors
This section will document any user-related errors with information on how you may be able to resolve them.

### ApiFeaturePreviewUsageOnly
This error indicates you are trying to use an endpoint in public preview and have not set `preview=True` when
calling the endpoint. Before doing so, note that this endpoint is
in preview state and breaking changes may occur at any time.

During the first phase of an endpoint's lifecycle, it may be in `Public Preview`
state. This indicates that the endpoint is in development and is not intended for
production use. 

## Input should have timezone info

```python
# Example error
pydantic_core._pydantic_core.ValidationError: 1 validation error for Model
datetype
  Input should have timezone info [type=timezone_aware, input_value=datetime.datetime(2025, 2, 5, 20, 57, 57, 511182), input_type=datetime]
```

This error indicates that you are passing a `datetime` object without timezone information to an
endpoint that requires it. To resolve this error, you should pass in a `datetime` object with timezone
information. For example, you can use the `timezone` class in the `datetime` package:

```python
from datetime import datetime
from datetime import timezone

datetime_with_tz = datetime(2025, 2, 5, 20, 57, 57, 511182, tzinfo=timezone.utc)
```

<a id="apis-link"></a>
<a id="apis-v2-link"></a>
## Documentation for V2 API endpoints

Namespace | Resource | Operation | HTTP request |
------------ | ------------- | ------------- | ------------- |
**Admin** | AuthenticationProvider | [**get**](docs/v2/Admin/AuthenticationProvider.md#get) | **GET** /v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid} |
**Admin** | AuthenticationProvider | [**list**](docs/v2/Admin/AuthenticationProvider.md#list) | **GET** /v2/admin/enrollments/{enrollmentRid}/authenticationProviders |
**Admin** | AuthenticationProvider | [**preregister_group**](docs/v2/Admin/AuthenticationProvider.md#preregister_group) | **POST** /v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterGroup |
**Admin** | AuthenticationProvider | [**preregister_user**](docs/v2/Admin/AuthenticationProvider.md#preregister_user) | **POST** /v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterUser |
**Admin** | Group | [**create**](docs/v2/Admin/Group.md#create) | **POST** /v2/admin/groups |
**Admin** | Group | [**delete**](docs/v2/Admin/Group.md#delete) | **DELETE** /v2/admin/groups/{groupId} |
**Admin** | Group | [**get**](docs/v2/Admin/Group.md#get) | **GET** /v2/admin/groups/{groupId} |
**Admin** | Group | [**get_batch**](docs/v2/Admin/Group.md#get_batch) | **POST** /v2/admin/groups/getBatch |
**Admin** | Group | [**list**](docs/v2/Admin/Group.md#list) | **GET** /v2/admin/groups |
**Admin** | Group | [**search**](docs/v2/Admin/Group.md#search) | **POST** /v2/admin/groups/search |
**Admin** | GroupMember | [**add**](docs/v2/Admin/GroupMember.md#add) | **POST** /v2/admin/groups/{groupId}/groupMembers/add |
**Admin** | GroupMember | [**list**](docs/v2/Admin/GroupMember.md#list) | **GET** /v2/admin/groups/{groupId}/groupMembers |
**Admin** | GroupMember | [**remove**](docs/v2/Admin/GroupMember.md#remove) | **POST** /v2/admin/groups/{groupId}/groupMembers/remove |
**Admin** | GroupMembership | [**list**](docs/v2/Admin/GroupMembership.md#list) | **GET** /v2/admin/users/{userId}/groupMemberships |
**Admin** | GroupMembershipExpirationPolicy | [**get**](docs/v2/Admin/GroupMembershipExpirationPolicy.md#get) | **GET** /v2/admin/groups/{groupId}/membershipExpirationPolicy |
**Admin** | GroupMembershipExpirationPolicy | [**replace**](docs/v2/Admin/GroupMembershipExpirationPolicy.md#replace) | **PUT** /v2/admin/groups/{groupId}/membershipExpirationPolicy |
**Admin** | GroupProviderInfo | [**get**](docs/v2/Admin/GroupProviderInfo.md#get) | **GET** /v2/admin/groups/{groupId}/providerInfo |
**Admin** | GroupProviderInfo | [**replace**](docs/v2/Admin/GroupProviderInfo.md#replace) | **PUT** /v2/admin/groups/{groupId}/providerInfo |
**Admin** | Marking | [**create**](docs/v2/Admin/Marking.md#create) | **POST** /v2/admin/markings |
**Admin** | Marking | [**get**](docs/v2/Admin/Marking.md#get) | **GET** /v2/admin/markings/{markingId} |
**Admin** | Marking | [**get_batch**](docs/v2/Admin/Marking.md#get_batch) | **POST** /v2/admin/markings/getBatch |
**Admin** | Marking | [**list**](docs/v2/Admin/Marking.md#list) | **GET** /v2/admin/markings |
**Admin** | Marking | [**replace**](docs/v2/Admin/Marking.md#replace) | **PUT** /v2/admin/markings/{markingId} |
**Admin** | MarkingCategory | [**get**](docs/v2/Admin/MarkingCategory.md#get) | **GET** /v2/admin/markingCategories/{markingCategoryId} |
**Admin** | MarkingCategory | [**list**](docs/v2/Admin/MarkingCategory.md#list) | **GET** /v2/admin/markingCategories |
**Admin** | MarkingMember | [**add**](docs/v2/Admin/MarkingMember.md#add) | **POST** /v2/admin/markings/{markingId}/markingMembers/add |
**Admin** | MarkingMember | [**list**](docs/v2/Admin/MarkingMember.md#list) | **GET** /v2/admin/markings/{markingId}/markingMembers |
**Admin** | MarkingMember | [**remove**](docs/v2/Admin/MarkingMember.md#remove) | **POST** /v2/admin/markings/{markingId}/markingMembers/remove |
**Admin** | MarkingRoleAssignment | [**add**](docs/v2/Admin/MarkingRoleAssignment.md#add) | **POST** /v2/admin/markings/{markingId}/roleAssignments/add |
**Admin** | MarkingRoleAssignment | [**list**](docs/v2/Admin/MarkingRoleAssignment.md#list) | **GET** /v2/admin/markings/{markingId}/roleAssignments |
**Admin** | MarkingRoleAssignment | [**remove**](docs/v2/Admin/MarkingRoleAssignment.md#remove) | **POST** /v2/admin/markings/{markingId}/roleAssignments/remove |
**Admin** | Organization | [**get**](docs/v2/Admin/Organization.md#get) | **GET** /v2/admin/organizations/{organizationRid} |
**Admin** | Organization | [**list_available_roles**](docs/v2/Admin/Organization.md#list_available_roles) | **GET** /v2/admin/organizations/{organizationRid}/listAvailableRoles |
**Admin** | Organization | [**replace**](docs/v2/Admin/Organization.md#replace) | **PUT** /v2/admin/organizations/{organizationRid} |
**Admin** | OrganizationRoleAssignment | [**add**](docs/v2/Admin/OrganizationRoleAssignment.md#add) | **POST** /v2/admin/organizations/{organizationRid}/roleAssignments/add |
**Admin** | OrganizationRoleAssignment | [**list**](docs/v2/Admin/OrganizationRoleAssignment.md#list) | **GET** /v2/admin/organizations/{organizationRid}/roleAssignments |
**Admin** | OrganizationRoleAssignment | [**remove**](docs/v2/Admin/OrganizationRoleAssignment.md#remove) | **POST** /v2/admin/organizations/{organizationRid}/roleAssignments/remove |
**Admin** | User | [**delete**](docs/v2/Admin/User.md#delete) | **DELETE** /v2/admin/users/{userId} |
**Admin** | User | [**get**](docs/v2/Admin/User.md#get) | **GET** /v2/admin/users/{userId} |
**Admin** | User | [**get_batch**](docs/v2/Admin/User.md#get_batch) | **POST** /v2/admin/users/getBatch |
**Admin** | User | [**get_current**](docs/v2/Admin/User.md#get_current) | **GET** /v2/admin/users/getCurrent |
**Admin** | User | [**get_markings**](docs/v2/Admin/User.md#get_markings) | **GET** /v2/admin/users/{userId}/getMarkings |
**Admin** | User | [**list**](docs/v2/Admin/User.md#list) | **GET** /v2/admin/users |
**Admin** | User | [**profile_picture**](docs/v2/Admin/User.md#profile_picture) | **GET** /v2/admin/users/{userId}/profilePicture |
**Admin** | User | [**revoke_all_tokens**](docs/v2/Admin/User.md#revoke_all_tokens) | **POST** /v2/admin/users/{userId}/revokeAllTokens |
**Admin** | User | [**search**](docs/v2/Admin/User.md#search) | **POST** /v2/admin/users/search |
**Admin** | UserProviderInfo | [**get**](docs/v2/Admin/UserProviderInfo.md#get) | **GET** /v2/admin/users/{userId}/providerInfo |
**Admin** | UserProviderInfo | [**replace**](docs/v2/Admin/UserProviderInfo.md#replace) | **PUT** /v2/admin/users/{userId}/providerInfo |
**AipAgents** | Agent | [**all_sessions**](docs/v2/AipAgents/Agent.md#all_sessions) | **GET** /v2/aipAgents/agents/allSessions |
**AipAgents** | Agent | [**get**](docs/v2/AipAgents/Agent.md#get) | **GET** /v2/aipAgents/agents/{agentRid} |
**AipAgents** | AgentVersion | [**get**](docs/v2/AipAgents/AgentVersion.md#get) | **GET** /v2/aipAgents/agents/{agentRid}/agentVersions/{agentVersionString} |
**AipAgents** | AgentVersion | [**list**](docs/v2/AipAgents/AgentVersion.md#list) | **GET** /v2/aipAgents/agents/{agentRid}/agentVersions |
**AipAgents** | Content | [**get**](docs/v2/AipAgents/Content.md#get) | **GET** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/content |
**AipAgents** | Session | [**blocking_continue**](docs/v2/AipAgents/Session.md#blocking_continue) | **POST** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/blockingContinue |
**AipAgents** | Session | [**cancel**](docs/v2/AipAgents/Session.md#cancel) | **POST** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/cancel |
**AipAgents** | Session | [**create**](docs/v2/AipAgents/Session.md#create) | **POST** /v2/aipAgents/agents/{agentRid}/sessions |
**AipAgents** | Session | [**get**](docs/v2/AipAgents/Session.md#get) | **GET** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid} |
**AipAgents** | Session | [**list**](docs/v2/AipAgents/Session.md#list) | **GET** /v2/aipAgents/agents/{agentRid}/sessions |
**AipAgents** | Session | [**rag_context**](docs/v2/AipAgents/Session.md#rag_context) | **PUT** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/ragContext |
**AipAgents** | Session | [**streaming_continue**](docs/v2/AipAgents/Session.md#streaming_continue) | **POST** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/streamingContinue |
**AipAgents** | Session | [**update_title**](docs/v2/AipAgents/Session.md#update_title) | **PUT** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/updateTitle |
**AipAgents** | SessionTrace | [**get**](docs/v2/AipAgents/SessionTrace.md#get) | **GET** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/sessionTraces/{sessionTraceId} |
**Connectivity** | Connection | [**get**](docs/v2/Connectivity/Connection.md#get) | **GET** /v2/connectivity/connections/{connectionRid} |
**Connectivity** | Connection | [**get_configuration**](docs/v2/Connectivity/Connection.md#get_configuration) | **GET** /v2/connectivity/connections/{connectionRid}/getConfiguration |
**Connectivity** | Connection | [**update_secrets**](docs/v2/Connectivity/Connection.md#update_secrets) | **POST** /v2/connectivity/connections/{connectionRid}/updateSecrets |
**Connectivity** | FileImport | [**create**](docs/v2/Connectivity/FileImport.md#create) | **POST** /v2/connectivity/connections/{connectionRid}/fileImports |
**Connectivity** | FileImport | [**delete**](docs/v2/Connectivity/FileImport.md#delete) | **DELETE** /v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid} |
**Connectivity** | FileImport | [**execute**](docs/v2/Connectivity/FileImport.md#execute) | **POST** /v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}/execute |
**Connectivity** | FileImport | [**get**](docs/v2/Connectivity/FileImport.md#get) | **GET** /v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid} |
**Connectivity** | FileImport | [**list**](docs/v2/Connectivity/FileImport.md#list) | **GET** /v2/connectivity/connections/{connectionRid}/fileImports |
**Connectivity** | FileImport | [**replace**](docs/v2/Connectivity/FileImport.md#replace) | **PUT** /v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid} |
**Connectivity** | TableImport | [**create**](docs/v2/Connectivity/TableImport.md#create) | **POST** /v2/connectivity/connections/{connectionRid}/tableImports |
**Connectivity** | TableImport | [**delete**](docs/v2/Connectivity/TableImport.md#delete) | **DELETE** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid} |
**Connectivity** | TableImport | [**execute**](docs/v2/Connectivity/TableImport.md#execute) | **POST** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}/execute |
**Connectivity** | TableImport | [**get**](docs/v2/Connectivity/TableImport.md#get) | **GET** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid} |
**Connectivity** | TableImport | [**list**](docs/v2/Connectivity/TableImport.md#list) | **GET** /v2/connectivity/connections/{connectionRid}/tableImports |
**Connectivity** | TableImport | [**replace**](docs/v2/Connectivity/TableImport.md#replace) | **PUT** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid} |
**Datasets** | Branch | [**create**](docs/v2/Datasets/Branch.md#create) | **POST** /v2/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**delete**](docs/v2/Datasets/Branch.md#delete) | **DELETE** /v2/datasets/{datasetRid}/branches/{branchName} |
**Datasets** | Branch | [**get**](docs/v2/Datasets/Branch.md#get) | **GET** /v2/datasets/{datasetRid}/branches/{branchName} |
**Datasets** | Branch | [**list**](docs/v2/Datasets/Branch.md#list) | **GET** /v2/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**transactions**](docs/v2/Datasets/Branch.md#transactions) | **GET** /v2/datasets/{datasetRid}/branches/{branchName}/transactions |
**Datasets** | Dataset | [**create**](docs/v2/Datasets/Dataset.md#create) | **POST** /v2/datasets |
**Datasets** | Dataset | [**get**](docs/v2/Datasets/Dataset.md#get) | **GET** /v2/datasets/{datasetRid} |
**Datasets** | Dataset | [**get_schedules**](docs/v2/Datasets/Dataset.md#get_schedules) | **GET** /v2/datasets/{datasetRid}/getSchedules |
**Datasets** | Dataset | [**get_schema**](docs/v2/Datasets/Dataset.md#get_schema) | **GET** /v2/datasets/{datasetRid}/getSchema |
**Datasets** | Dataset | [**put_schema**](docs/v2/Datasets/Dataset.md#put_schema) | **PUT** /v2/datasets/{datasetRid}/putSchema |
**Datasets** | Dataset | [**read_table**](docs/v2/Datasets/Dataset.md#read_table) | **GET** /v2/datasets/{datasetRid}/readTable |
**Datasets** | Dataset | [**transactions**](docs/v2/Datasets/Dataset.md#transactions) | **GET** /v2/datasets/{datasetRid}/transactions |
**Datasets** | File | [**content**](docs/v2/Datasets/File.md#content) | **GET** /v2/datasets/{datasetRid}/files/{filePath}/content |
**Datasets** | File | [**delete**](docs/v2/Datasets/File.md#delete) | **DELETE** /v2/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**get**](docs/v2/Datasets/File.md#get) | **GET** /v2/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**list**](docs/v2/Datasets/File.md#list) | **GET** /v2/datasets/{datasetRid}/files |
**Datasets** | File | [**upload**](docs/v2/Datasets/File.md#upload) | **POST** /v2/datasets/{datasetRid}/files/{filePath}/upload |
**Datasets** | Transaction | [**abort**](docs/v2/Datasets/Transaction.md#abort) | **POST** /v2/datasets/{datasetRid}/transactions/{transactionRid}/abort |
**Datasets** | Transaction | [**commit**](docs/v2/Datasets/Transaction.md#commit) | **POST** /v2/datasets/{datasetRid}/transactions/{transactionRid}/commit |
**Datasets** | Transaction | [**create**](docs/v2/Datasets/Transaction.md#create) | **POST** /v2/datasets/{datasetRid}/transactions |
**Datasets** | Transaction | [**get**](docs/v2/Datasets/Transaction.md#get) | **GET** /v2/datasets/{datasetRid}/transactions/{transactionRid} |
**Datasets** | View | [**add_backing_datasets**](docs/v2/Datasets/View.md#add_backing_datasets) | **POST** /v2/datasets/views/{viewDatasetRid}/addBackingDatasets |
**Datasets** | View | [**add_primary_key**](docs/v2/Datasets/View.md#add_primary_key) | **POST** /v2/datasets/views/{viewDatasetRid}/addPrimaryKey |
**Datasets** | View | [**create**](docs/v2/Datasets/View.md#create) | **POST** /v2/datasets/views |
**Datasets** | View | [**get**](docs/v2/Datasets/View.md#get) | **GET** /v2/datasets/views/{viewDatasetRid} |
**Datasets** | View | [**remove_backing_datasets**](docs/v2/Datasets/View.md#remove_backing_datasets) | **POST** /v2/datasets/views/{viewDatasetRid}/removeBackingDatasets |
**Datasets** | View | [**replace_backing_datasets**](docs/v2/Datasets/View.md#replace_backing_datasets) | **PUT** /v2/datasets/views/{viewDatasetRid}/replaceBackingDatasets |
**Filesystem** | Folder | [**children**](docs/v2/Filesystem/Folder.md#children) | **GET** /v2/filesystem/folders/{folderRid}/children |
**Filesystem** | Folder | [**create**](docs/v2/Filesystem/Folder.md#create) | **POST** /v2/filesystem/folders |
**Filesystem** | Folder | [**get**](docs/v2/Filesystem/Folder.md#get) | **GET** /v2/filesystem/folders/{folderRid} |
**Filesystem** | Project | [**add_organizations**](docs/v2/Filesystem/Project.md#add_organizations) | **POST** /v2/filesystem/projects/{projectRid}/addOrganizations |
**Filesystem** | Project | [**create**](docs/v2/Filesystem/Project.md#create) | **POST** /v2/filesystem/projects/create |
**Filesystem** | Project | [**get**](docs/v2/Filesystem/Project.md#get) | **GET** /v2/filesystem/projects/{projectRid} |
**Filesystem** | Project | [**organizations**](docs/v2/Filesystem/Project.md#organizations) | **GET** /v2/filesystem/projects/{projectRid}/organizations |
**Filesystem** | Project | [**remove_organizations**](docs/v2/Filesystem/Project.md#remove_organizations) | **POST** /v2/filesystem/projects/{projectRid}/removeOrganizations |
**Filesystem** | Resource | [**add_markings**](docs/v2/Filesystem/Resource.md#add_markings) | **POST** /v2/filesystem/resources/{resourceRid}/addMarkings |
**Filesystem** | Resource | [**delete**](docs/v2/Filesystem/Resource.md#delete) | **DELETE** /v2/filesystem/resources/{resourceRid} |
**Filesystem** | Resource | [**get**](docs/v2/Filesystem/Resource.md#get) | **GET** /v2/filesystem/resources/{resourceRid} |
**Filesystem** | Resource | [**get_access_requirements**](docs/v2/Filesystem/Resource.md#get_access_requirements) | **GET** /v2/filesystem/resources/{resourceRid}/getAccessRequirements |
**Filesystem** | Resource | [**get_by_path**](docs/v2/Filesystem/Resource.md#get_by_path) | **GET** /v2/filesystem/resources/getByPath |
**Filesystem** | Resource | [**markings**](docs/v2/Filesystem/Resource.md#markings) | **GET** /v2/filesystem/resources/{resourceRid}/markings |
**Filesystem** | Resource | [**permanently_delete**](docs/v2/Filesystem/Resource.md#permanently_delete) | **POST** /v2/filesystem/resources/{resourceRid}/permanentlyDelete |
**Filesystem** | Resource | [**remove_markings**](docs/v2/Filesystem/Resource.md#remove_markings) | **POST** /v2/filesystem/resources/{resourceRid}/removeMarkings |
**Filesystem** | Resource | [**restore**](docs/v2/Filesystem/Resource.md#restore) | **POST** /v2/filesystem/resources/{resourceRid}/restore |
**Filesystem** | ResourceRole | [**add**](docs/v2/Filesystem/ResourceRole.md#add) | **POST** /v2/filesystem/resources/{resourceRid}/roles/add |
**Filesystem** | ResourceRole | [**list**](docs/v2/Filesystem/ResourceRole.md#list) | **GET** /v2/filesystem/resources/{resourceRid}/roles |
**Filesystem** | ResourceRole | [**remove**](docs/v2/Filesystem/ResourceRole.md#remove) | **POST** /v2/filesystem/resources/{resourceRid}/roles/remove |
**Filesystem** | Space | [**list**](docs/v2/Filesystem/Space.md#list) | **GET** /v2/filesystem/spaces |
**MediaSets** | MediaSet | [**abort**](docs/v2/MediaSets/MediaSet.md#abort) | **POST** /v2/mediasets/{mediaSetRid}/transactions/{transactionId}/abort |
**MediaSets** | MediaSet | [**commit**](docs/v2/MediaSets/MediaSet.md#commit) | **POST** /v2/mediasets/{mediaSetRid}/transactions/{transactionId}/commit |
**MediaSets** | MediaSet | [**create**](docs/v2/MediaSets/MediaSet.md#create) | **POST** /v2/mediasets/{mediaSetRid}/transactions |
**MediaSets** | MediaSet | [**get_rid_by_path**](docs/v2/MediaSets/MediaSet.md#get_rid_by_path) | **GET** /v2/mediasets/{mediaSetRid}/items/getRidByPath |
**MediaSets** | MediaSet | [**info**](docs/v2/MediaSets/MediaSet.md#info) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid} |
**MediaSets** | MediaSet | [**read**](docs/v2/MediaSets/MediaSet.md#read) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/content |
**MediaSets** | MediaSet | [**read_original**](docs/v2/MediaSets/MediaSet.md#read_original) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/original |
**MediaSets** | MediaSet | [**reference**](docs/v2/MediaSets/MediaSet.md#reference) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/reference |
**MediaSets** | MediaSet | [**upload**](docs/v2/MediaSets/MediaSet.md#upload) | **POST** /v2/mediasets/{mediaSetRid}/items |
**Ontologies** | Action | [**apply**](docs/v2/Ontologies/Action.md#apply) | **POST** /v2/ontologies/{ontology}/actions/{action}/apply |
**Ontologies** | Action | [**apply_batch**](docs/v2/Ontologies/Action.md#apply_batch) | **POST** /v2/ontologies/{ontology}/actions/{action}/applyBatch |
**Ontologies** | ActionType | [**get**](docs/v2/Ontologies/ActionType.md#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} |
**Ontologies** | ActionType | [**get_by_rid**](docs/v2/Ontologies/ActionType.md#get_by_rid) | **GET** /v2/ontologies/{ontology}/actionTypes/byRid/{actionTypeRid} |
**Ontologies** | ActionType | [**list**](docs/v2/Ontologies/ActionType.md#list) | **GET** /v2/ontologies/{ontology}/actionTypes |
**Ontologies** | Attachment | [**get**](docs/v2/Ontologies/Attachment.md#get) | **GET** /v2/ontologies/attachments/{attachmentRid} |
**Ontologies** | Attachment | [**read**](docs/v2/Ontologies/Attachment.md#read) | **GET** /v2/ontologies/attachments/{attachmentRid}/content |
**Ontologies** | Attachment | [**upload**](docs/v2/Ontologies/Attachment.md#upload) | **POST** /v2/ontologies/attachments/upload |
**Ontologies** | AttachmentProperty | [**get_attachment**](docs/v2/Ontologies/AttachmentProperty.md#get_attachment) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property} |
**Ontologies** | AttachmentProperty | [**get_attachment_by_rid**](docs/v2/Ontologies/AttachmentProperty.md#get_attachment_by_rid) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid} |
**Ontologies** | AttachmentProperty | [**read_attachment**](docs/v2/Ontologies/AttachmentProperty.md#read_attachment) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/content |
**Ontologies** | AttachmentProperty | [**read_attachment_by_rid**](docs/v2/Ontologies/AttachmentProperty.md#read_attachment_by_rid) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}/content |
**Ontologies** | CipherTextProperty | [**decrypt**](docs/v2/Ontologies/CipherTextProperty.md#decrypt) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/decrypt |
**Ontologies** | LinkedObject | [**get_linked_object**](docs/v2/Ontologies/LinkedObject.md#get_linked_object) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey} |
**Ontologies** | LinkedObject | [**list_linked_objects**](docs/v2/Ontologies/LinkedObject.md#list_linked_objects) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType} |
**Ontologies** | MediaReferenceProperty | [**get_media_content**](docs/v2/Ontologies/MediaReferenceProperty.md#get_media_content) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/media/{property}/content |
**Ontologies** | MediaReferenceProperty | [**upload**](docs/v2/Ontologies/MediaReferenceProperty.md#upload) | **POST** /v2/ontologies/{ontology}/objectTypes/{objectType}/media/{property}/upload |
**Ontologies** | ObjectType | [**get**](docs/v2/Ontologies/ObjectType.md#get) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType} |
**Ontologies** | ObjectType | [**get_outgoing_link_type**](docs/v2/Ontologies/ObjectType.md#get_outgoing_link_type) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
**Ontologies** | ObjectType | [**list**](docs/v2/Ontologies/ObjectType.md#list) | **GET** /v2/ontologies/{ontology}/objectTypes |
**Ontologies** | ObjectType | [**list_outgoing_link_types**](docs/v2/Ontologies/ObjectType.md#list_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | Ontology | [**get**](docs/v2/Ontologies/Ontology.md#get) | **GET** /v2/ontologies/{ontology} |
**Ontologies** | Ontology | [**get_full_metadata**](docs/v2/Ontologies/Ontology.md#get_full_metadata) | **GET** /v2/ontologies/{ontology}/fullMetadata |
**Ontologies** | Ontology | [**list**](docs/v2/Ontologies/Ontology.md#list) | **GET** /v2/ontologies |
**Ontologies** | OntologyInterface | [**get**](docs/v2/Ontologies/OntologyInterface.md#get) | **GET** /v2/ontologies/{ontology}/interfaceTypes/{interfaceType} |
**Ontologies** | OntologyInterface | [**list**](docs/v2/Ontologies/OntologyInterface.md#list) | **GET** /v2/ontologies/{ontology}/interfaceTypes |
**Ontologies** | OntologyObject | [**aggregate**](docs/v2/Ontologies/OntologyObject.md#aggregate) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/aggregate |
**Ontologies** | OntologyObject | [**get**](docs/v2/Ontologies/OntologyObject.md#get) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey} |
**Ontologies** | OntologyObject | [**list**](docs/v2/Ontologies/OntologyObject.md#list) | **GET** /v2/ontologies/{ontology}/objects/{objectType} |
**Ontologies** | OntologyObject | [**search**](docs/v2/Ontologies/OntologyObject.md#search) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/search |
**Ontologies** | OntologyObjectSet | [**aggregate**](docs/v2/Ontologies/OntologyObjectSet.md#aggregate) | **POST** /v2/ontologies/{ontology}/objectSets/aggregate |
**Ontologies** | OntologyObjectSet | [**create_temporary**](docs/v2/Ontologies/OntologyObjectSet.md#create_temporary) | **POST** /v2/ontologies/{ontology}/objectSets/createTemporary |
**Ontologies** | OntologyObjectSet | [**load**](docs/v2/Ontologies/OntologyObjectSet.md#load) | **POST** /v2/ontologies/{ontology}/objectSets/loadObjects |
**Ontologies** | OntologyObjectSet | [**load_multiple_object_types**](docs/v2/Ontologies/OntologyObjectSet.md#load_multiple_object_types) | **POST** /v2/ontologies/{ontology}/objectSets/loadObjectsMultipleObjectTypes |
**Ontologies** | OntologyObjectSet | [**load_objects_or_interfaces**](docs/v2/Ontologies/OntologyObjectSet.md#load_objects_or_interfaces) | **POST** /v2/ontologies/{ontology}/objectSets/loadObjectsOrInterfaces |
**Ontologies** | Query | [**execute**](docs/v2/Ontologies/Query.md#execute) | **POST** /v2/ontologies/{ontology}/queries/{queryApiName}/execute |
**Ontologies** | QueryType | [**get**](docs/v2/Ontologies/QueryType.md#get) | **GET** /v2/ontologies/{ontology}/queryTypes/{queryApiName} |
**Ontologies** | QueryType | [**list**](docs/v2/Ontologies/QueryType.md#list) | **GET** /v2/ontologies/{ontology}/queryTypes |
**Ontologies** | TimeSeriesPropertyV2 | [**get_first_point**](docs/v2/Ontologies/TimeSeriesPropertyV2.md#get_first_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/firstPoint |
**Ontologies** | TimeSeriesPropertyV2 | [**get_last_point**](docs/v2/Ontologies/TimeSeriesPropertyV2.md#get_last_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/lastPoint |
**Ontologies** | TimeSeriesPropertyV2 | [**stream_points**](docs/v2/Ontologies/TimeSeriesPropertyV2.md#stream_points) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamPoints |
**Ontologies** | TimeSeriesValueBankProperty | [**get_latest_value**](docs/v2/Ontologies/TimeSeriesValueBankProperty.md#get_latest_value) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{propertyName}/latestValue |
**Ontologies** | TimeSeriesValueBankProperty | [**stream_values**](docs/v2/Ontologies/TimeSeriesValueBankProperty.md#stream_values) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamValues |
**Orchestration** | Build | [**cancel**](docs/v2/Orchestration/Build.md#cancel) | **POST** /v2/orchestration/builds/{buildRid}/cancel |
**Orchestration** | Build | [**create**](docs/v2/Orchestration/Build.md#create) | **POST** /v2/orchestration/builds/create |
**Orchestration** | Build | [**get**](docs/v2/Orchestration/Build.md#get) | **GET** /v2/orchestration/builds/{buildRid} |
**Orchestration** | Build | [**get_batch**](docs/v2/Orchestration/Build.md#get_batch) | **POST** /v2/orchestration/builds/getBatch |
**Orchestration** | Build | [**jobs**](docs/v2/Orchestration/Build.md#jobs) | **GET** /v2/orchestration/builds/{buildRid}/jobs |
**Orchestration** | Job | [**get**](docs/v2/Orchestration/Job.md#get) | **GET** /v2/orchestration/jobs/{jobRid} |
**Orchestration** | Job | [**get_batch**](docs/v2/Orchestration/Job.md#get_batch) | **POST** /v2/orchestration/jobs/getBatch |
**Orchestration** | Schedule | [**create**](docs/v2/Orchestration/Schedule.md#create) | **POST** /v2/orchestration/schedules |
**Orchestration** | Schedule | [**delete**](docs/v2/Orchestration/Schedule.md#delete) | **DELETE** /v2/orchestration/schedules/{scheduleRid} |
**Orchestration** | Schedule | [**get**](docs/v2/Orchestration/Schedule.md#get) | **GET** /v2/orchestration/schedules/{scheduleRid} |
**Orchestration** | Schedule | [**get_batch**](docs/v2/Orchestration/Schedule.md#get_batch) | **POST** /v2/orchestration/schedules/getBatch |
**Orchestration** | Schedule | [**pause**](docs/v2/Orchestration/Schedule.md#pause) | **POST** /v2/orchestration/schedules/{scheduleRid}/pause |
**Orchestration** | Schedule | [**replace**](docs/v2/Orchestration/Schedule.md#replace) | **PUT** /v2/orchestration/schedules/{scheduleRid} |
**Orchestration** | Schedule | [**run**](docs/v2/Orchestration/Schedule.md#run) | **POST** /v2/orchestration/schedules/{scheduleRid}/run |
**Orchestration** | Schedule | [**runs**](docs/v2/Orchestration/Schedule.md#runs) | **GET** /v2/orchestration/schedules/{scheduleRid}/runs |
**Orchestration** | Schedule | [**unpause**](docs/v2/Orchestration/Schedule.md#unpause) | **POST** /v2/orchestration/schedules/{scheduleRid}/unpause |
**Orchestration** | ScheduleVersion | [**get**](docs/v2/Orchestration/ScheduleVersion.md#get) | **GET** /v2/orchestration/scheduleVersions/{scheduleVersionRid} |
**Orchestration** | ScheduleVersion | [**schedule**](docs/v2/Orchestration/ScheduleVersion.md#schedule) | **GET** /v2/orchestration/scheduleVersions/{scheduleVersionRid}/schedule |
**SqlQueries** | SqlQuery | [**cancel**](docs/v2/SqlQueries/SqlQuery.md#cancel) | **POST** /v2/sqlQueries/{sqlQueryId}/cancel |
**SqlQueries** | SqlQuery | [**execute**](docs/v2/SqlQueries/SqlQuery.md#execute) | **POST** /v2/sqlQueries/execute |
**SqlQueries** | SqlQuery | [**get_results**](docs/v2/SqlQueries/SqlQuery.md#get_results) | **GET** /v2/sqlQueries/{sqlQueryId}/getResults |
**SqlQueries** | SqlQuery | [**get_status**](docs/v2/SqlQueries/SqlQuery.md#get_status) | **GET** /v2/sqlQueries/{sqlQueryId}/getStatus |
**Streams** | Dataset | [**create**](docs/v2/Streams/Dataset.md#create) | **POST** /v2/streams/datasets/create |
**Streams** | Stream | [**create**](docs/v2/Streams/Stream.md#create) | **POST** /v2/streams/datasets/{datasetRid}/streams |
**Streams** | Stream | [**get**](docs/v2/Streams/Stream.md#get) | **GET** /v2/streams/datasets/{datasetRid}/streams/{streamBranchName} |
**Streams** | Stream | [**publish_binary_record**](docs/v2/Streams/Stream.md#publish_binary_record) | **POST** /v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/publishBinaryRecord |
**Streams** | Stream | [**publish_record**](docs/v2/Streams/Stream.md#publish_record) | **POST** /v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/publishRecord |
**Streams** | Stream | [**publish_records**](docs/v2/Streams/Stream.md#publish_records) | **POST** /v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/publishRecords |
**Streams** | Stream | [**reset**](docs/v2/Streams/Stream.md#reset) | **POST** /v2/streams/datasets/{datasetRid}/streams/{streamBranchName}/reset |
**ThirdPartyApplications** | Version | [**delete**](docs/v2/ThirdPartyApplications/Version.md#delete) | **DELETE** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion} |
**ThirdPartyApplications** | Version | [**get**](docs/v2/ThirdPartyApplications/Version.md#get) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion} |
**ThirdPartyApplications** | Version | [**list**](docs/v2/ThirdPartyApplications/Version.md#list) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions |
**ThirdPartyApplications** | Version | [**upload**](docs/v2/ThirdPartyApplications/Version.md#upload) | **POST** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/upload |
**ThirdPartyApplications** | Website | [**deploy**](docs/v2/ThirdPartyApplications/Website.md#deploy) | **POST** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/deploy |
**ThirdPartyApplications** | Website | [**get**](docs/v2/ThirdPartyApplications/Website.md#get) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website |
**ThirdPartyApplications** | Website | [**undeploy**](docs/v2/ThirdPartyApplications/Website.md#undeploy) | **POST** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/undeploy |
<a id="apis-v1-link"></a>
## Documentation for V1 API endpoints

Namespace | Resource | Operation | HTTP request |
------------ | ------------- | ------------- | ------------- |
**Datasets** | Branch | [**create**](docs/v1/Datasets/Branch.md#create) | **POST** /v1/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**delete**](docs/v1/Datasets/Branch.md#delete) | **DELETE** /v1/datasets/{datasetRid}/branches/{branchId} |
**Datasets** | Branch | [**get**](docs/v1/Datasets/Branch.md#get) | **GET** /v1/datasets/{datasetRid}/branches/{branchId} |
**Datasets** | Branch | [**list**](docs/v1/Datasets/Branch.md#list) | **GET** /v1/datasets/{datasetRid}/branches |
**Datasets** | Dataset | [**create**](docs/v1/Datasets/Dataset.md#create) | **POST** /v1/datasets |
**Datasets** | Dataset | [**get**](docs/v1/Datasets/Dataset.md#get) | **GET** /v1/datasets/{datasetRid} |
**Datasets** | Dataset | [**read**](docs/v1/Datasets/Dataset.md#read) | **GET** /v1/datasets/{datasetRid}/readTable |
**Datasets** | File | [**delete**](docs/v1/Datasets/File.md#delete) | **DELETE** /v1/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**get**](docs/v1/Datasets/File.md#get) | **GET** /v1/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**list**](docs/v1/Datasets/File.md#list) | **GET** /v1/datasets/{datasetRid}/files |
**Datasets** | File | [**read**](docs/v1/Datasets/File.md#read) | **GET** /v1/datasets/{datasetRid}/files/{filePath}/content |
**Datasets** | File | [**upload**](docs/v1/Datasets/File.md#upload) | **POST** /v1/datasets/{datasetRid}/files:upload |
**Datasets** | Transaction | [**abort**](docs/v1/Datasets/Transaction.md#abort) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/abort |
**Datasets** | Transaction | [**commit**](docs/v1/Datasets/Transaction.md#commit) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/commit |
**Datasets** | Transaction | [**create**](docs/v1/Datasets/Transaction.md#create) | **POST** /v1/datasets/{datasetRid}/transactions |
**Datasets** | Transaction | [**get**](docs/v1/Datasets/Transaction.md#get) | **GET** /v1/datasets/{datasetRid}/transactions/{transactionRid} |
**Ontologies** | Action | [**apply**](docs/v1/Ontologies/Action.md#apply) | **POST** /v1/ontologies/{ontologyRid}/actions/{actionType}/apply |
**Ontologies** | Action | [**apply_batch**](docs/v1/Ontologies/Action.md#apply_batch) | **POST** /v1/ontologies/{ontologyRid}/actions/{actionType}/applyBatch |
**Ontologies** | Action | [**validate**](docs/v1/Ontologies/Action.md#validate) | **POST** /v1/ontologies/{ontologyRid}/actions/{actionType}/validate |
**Ontologies** | ActionType | [**get**](docs/v1/Ontologies/ActionType.md#get) | **GET** /v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName} |
**Ontologies** | ActionType | [**list**](docs/v1/Ontologies/ActionType.md#list) | **GET** /v1/ontologies/{ontologyRid}/actionTypes |
**Ontologies** | Attachment | [**get**](docs/v1/Ontologies/Attachment.md#get) | **GET** /v1/attachments/{attachmentRid} |
**Ontologies** | Attachment | [**read**](docs/v1/Ontologies/Attachment.md#read) | **GET** /v1/attachments/{attachmentRid}/content |
**Ontologies** | Attachment | [**upload**](docs/v1/Ontologies/Attachment.md#upload) | **POST** /v1/attachments/upload |
**Ontologies** | ObjectType | [**get**](docs/v1/Ontologies/ObjectType.md#get) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType} |
**Ontologies** | ObjectType | [**get_outgoing_link_type**](docs/v1/Ontologies/ObjectType.md#get_outgoing_link_type) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
**Ontologies** | ObjectType | [**list**](docs/v1/Ontologies/ObjectType.md#list) | **GET** /v1/ontologies/{ontologyRid}/objectTypes |
**Ontologies** | ObjectType | [**list_outgoing_link_types**](docs/v1/Ontologies/ObjectType.md#list_outgoing_link_types) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | Ontology | [**get**](docs/v1/Ontologies/Ontology.md#get) | **GET** /v1/ontologies/{ontologyRid} |
**Ontologies** | Ontology | [**list**](docs/v1/Ontologies/Ontology.md#list) | **GET** /v1/ontologies |
**Ontologies** | OntologyObject | [**aggregate**](docs/v1/Ontologies/OntologyObject.md#aggregate) | **POST** /v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate |
**Ontologies** | OntologyObject | [**get**](docs/v1/Ontologies/OntologyObject.md#get) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey} |
**Ontologies** | OntologyObject | [**get_linked_object**](docs/v1/Ontologies/OntologyObject.md#get_linked_object) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey} |
**Ontologies** | OntologyObject | [**list**](docs/v1/Ontologies/OntologyObject.md#list) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType} |
**Ontologies** | OntologyObject | [**list_linked_objects**](docs/v1/Ontologies/OntologyObject.md#list_linked_objects) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType} |
**Ontologies** | OntologyObject | [**search**](docs/v1/Ontologies/OntologyObject.md#search) | **POST** /v1/ontologies/{ontologyRid}/objects/{objectType}/search |
**Ontologies** | Query | [**execute**](docs/v1/Ontologies/Query.md#execute) | **POST** /v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute |
**Ontologies** | QueryType | [**get**](docs/v1/Ontologies/QueryType.md#get) | **GET** /v1/ontologies/{ontologyRid}/queryTypes/{queryApiName} |
**Ontologies** | QueryType | [**list**](docs/v1/Ontologies/QueryType.md#list) | **GET** /v1/ontologies/{ontologyRid}/queryTypes |


<a id="models-link"></a>
<a id="models-v2-link"></a>
## Documentation for V2 models

Namespace | Name | Import |
--------- | ---- | ------ |
**Admin** | [AttributeName](docs/v2/Admin/models/AttributeName.md) | `from foundry_sdk.v2.admin.models import AttributeName` |
**Admin** | [AttributeValue](docs/v2/Admin/models/AttributeValue.md) | `from foundry_sdk.v2.admin.models import AttributeValue` |
**Admin** | [AttributeValues](docs/v2/Admin/models/AttributeValues.md) | `from foundry_sdk.v2.admin.models import AttributeValues` |
**Admin** | [AuthenticationProtocol](docs/v2/Admin/models/AuthenticationProtocol.md) | `from foundry_sdk.v2.admin.models import AuthenticationProtocol` |
**Admin** | [AuthenticationProvider](docs/v2/Admin/models/AuthenticationProvider.md) | `from foundry_sdk.v2.admin.models import AuthenticationProvider` |
**Admin** | [AuthenticationProviderEnabled](docs/v2/Admin/models/AuthenticationProviderEnabled.md) | `from foundry_sdk.v2.admin.models import AuthenticationProviderEnabled` |
**Admin** | [AuthenticationProviderName](docs/v2/Admin/models/AuthenticationProviderName.md) | `from foundry_sdk.v2.admin.models import AuthenticationProviderName` |
**Admin** | [AuthenticationProviderRid](docs/v2/Admin/models/AuthenticationProviderRid.md) | `from foundry_sdk.v2.admin.models import AuthenticationProviderRid` |
**Admin** | [CertificateInfo](docs/v2/Admin/models/CertificateInfo.md) | `from foundry_sdk.v2.admin.models import CertificateInfo` |
**Admin** | [CertificateUsageType](docs/v2/Admin/models/CertificateUsageType.md) | `from foundry_sdk.v2.admin.models import CertificateUsageType` |
**Admin** | [Enrollment](docs/v2/Admin/models/Enrollment.md) | `from foundry_sdk.v2.admin.models import Enrollment` |
**Admin** | [EnrollmentName](docs/v2/Admin/models/EnrollmentName.md) | `from foundry_sdk.v2.admin.models import EnrollmentName` |
**Admin** | [EnrollmentRoleAssignment](docs/v2/Admin/models/EnrollmentRoleAssignment.md) | `from foundry_sdk.v2.admin.models import EnrollmentRoleAssignment` |
**Admin** | [GetGroupsBatchRequestElement](docs/v2/Admin/models/GetGroupsBatchRequestElement.md) | `from foundry_sdk.v2.admin.models import GetGroupsBatchRequestElement` |
**Admin** | [GetGroupsBatchResponse](docs/v2/Admin/models/GetGroupsBatchResponse.md) | `from foundry_sdk.v2.admin.models import GetGroupsBatchResponse` |
**Admin** | [GetMarkingsBatchRequestElement](docs/v2/Admin/models/GetMarkingsBatchRequestElement.md) | `from foundry_sdk.v2.admin.models import GetMarkingsBatchRequestElement` |
**Admin** | [GetMarkingsBatchResponse](docs/v2/Admin/models/GetMarkingsBatchResponse.md) | `from foundry_sdk.v2.admin.models import GetMarkingsBatchResponse` |
**Admin** | [GetRolesBatchRequestElement](docs/v2/Admin/models/GetRolesBatchRequestElement.md) | `from foundry_sdk.v2.admin.models import GetRolesBatchRequestElement` |
**Admin** | [GetRolesBatchResponse](docs/v2/Admin/models/GetRolesBatchResponse.md) | `from foundry_sdk.v2.admin.models import GetRolesBatchResponse` |
**Admin** | [GetUserMarkingsResponse](docs/v2/Admin/models/GetUserMarkingsResponse.md) | `from foundry_sdk.v2.admin.models import GetUserMarkingsResponse` |
**Admin** | [GetUsersBatchRequestElement](docs/v2/Admin/models/GetUsersBatchRequestElement.md) | `from foundry_sdk.v2.admin.models import GetUsersBatchRequestElement` |
**Admin** | [GetUsersBatchResponse](docs/v2/Admin/models/GetUsersBatchResponse.md) | `from foundry_sdk.v2.admin.models import GetUsersBatchResponse` |
**Admin** | [Group](docs/v2/Admin/models/Group.md) | `from foundry_sdk.v2.admin.models import Group` |
**Admin** | [GroupMember](docs/v2/Admin/models/GroupMember.md) | `from foundry_sdk.v2.admin.models import GroupMember` |
**Admin** | [GroupMembership](docs/v2/Admin/models/GroupMembership.md) | `from foundry_sdk.v2.admin.models import GroupMembership` |
**Admin** | [GroupMembershipExpiration](docs/v2/Admin/models/GroupMembershipExpiration.md) | `from foundry_sdk.v2.admin.models import GroupMembershipExpiration` |
**Admin** | [GroupMembershipExpirationPolicy](docs/v2/Admin/models/GroupMembershipExpirationPolicy.md) | `from foundry_sdk.v2.admin.models import GroupMembershipExpirationPolicy` |
**Admin** | [GroupName](docs/v2/Admin/models/GroupName.md) | `from foundry_sdk.v2.admin.models import GroupName` |
**Admin** | [GroupProviderInfo](docs/v2/Admin/models/GroupProviderInfo.md) | `from foundry_sdk.v2.admin.models import GroupProviderInfo` |
**Admin** | [GroupSearchFilter](docs/v2/Admin/models/GroupSearchFilter.md) | `from foundry_sdk.v2.admin.models import GroupSearchFilter` |
**Admin** | [Host](docs/v2/Admin/models/Host.md) | `from foundry_sdk.v2.admin.models import Host` |
**Admin** | [HostName](docs/v2/Admin/models/HostName.md) | `from foundry_sdk.v2.admin.models import HostName` |
**Admin** | [ListAuthenticationProvidersResponse](docs/v2/Admin/models/ListAuthenticationProvidersResponse.md) | `from foundry_sdk.v2.admin.models import ListAuthenticationProvidersResponse` |
**Admin** | [ListAvailableOrganizationRolesResponse](docs/v2/Admin/models/ListAvailableOrganizationRolesResponse.md) | `from foundry_sdk.v2.admin.models import ListAvailableOrganizationRolesResponse` |
**Admin** | [ListEnrollmentRoleAssignmentsResponse](docs/v2/Admin/models/ListEnrollmentRoleAssignmentsResponse.md) | `from foundry_sdk.v2.admin.models import ListEnrollmentRoleAssignmentsResponse` |
**Admin** | [ListGroupMembershipsResponse](docs/v2/Admin/models/ListGroupMembershipsResponse.md) | `from foundry_sdk.v2.admin.models import ListGroupMembershipsResponse` |
**Admin** | [ListGroupMembersResponse](docs/v2/Admin/models/ListGroupMembersResponse.md) | `from foundry_sdk.v2.admin.models import ListGroupMembersResponse` |
**Admin** | [ListGroupsResponse](docs/v2/Admin/models/ListGroupsResponse.md) | `from foundry_sdk.v2.admin.models import ListGroupsResponse` |
**Admin** | [ListHostsResponse](docs/v2/Admin/models/ListHostsResponse.md) | `from foundry_sdk.v2.admin.models import ListHostsResponse` |
**Admin** | [ListMarkingCategoriesResponse](docs/v2/Admin/models/ListMarkingCategoriesResponse.md) | `from foundry_sdk.v2.admin.models import ListMarkingCategoriesResponse` |
**Admin** | [ListMarkingMembersResponse](docs/v2/Admin/models/ListMarkingMembersResponse.md) | `from foundry_sdk.v2.admin.models import ListMarkingMembersResponse` |
**Admin** | [ListMarkingRoleAssignmentsResponse](docs/v2/Admin/models/ListMarkingRoleAssignmentsResponse.md) | `from foundry_sdk.v2.admin.models import ListMarkingRoleAssignmentsResponse` |
**Admin** | [ListMarkingsResponse](docs/v2/Admin/models/ListMarkingsResponse.md) | `from foundry_sdk.v2.admin.models import ListMarkingsResponse` |
**Admin** | [ListOrganizationRoleAssignmentsResponse](docs/v2/Admin/models/ListOrganizationRoleAssignmentsResponse.md) | `from foundry_sdk.v2.admin.models import ListOrganizationRoleAssignmentsResponse` |
**Admin** | [ListUsersResponse](docs/v2/Admin/models/ListUsersResponse.md) | `from foundry_sdk.v2.admin.models import ListUsersResponse` |
**Admin** | [Marking](docs/v2/Admin/models/Marking.md) | `from foundry_sdk.v2.admin.models import Marking` |
**Admin** | [MarkingCategory](docs/v2/Admin/models/MarkingCategory.md) | `from foundry_sdk.v2.admin.models import MarkingCategory` |
**Admin** | [MarkingCategoryId](docs/v2/Admin/models/MarkingCategoryId.md) | `from foundry_sdk.v2.admin.models import MarkingCategoryId` |
**Admin** | [MarkingCategoryName](docs/v2/Admin/models/MarkingCategoryName.md) | `from foundry_sdk.v2.admin.models import MarkingCategoryName` |
**Admin** | [MarkingCategoryType](docs/v2/Admin/models/MarkingCategoryType.md) | `from foundry_sdk.v2.admin.models import MarkingCategoryType` |
**Admin** | [MarkingMember](docs/v2/Admin/models/MarkingMember.md) | `from foundry_sdk.v2.admin.models import MarkingMember` |
**Admin** | [MarkingName](docs/v2/Admin/models/MarkingName.md) | `from foundry_sdk.v2.admin.models import MarkingName` |
**Admin** | [MarkingRole](docs/v2/Admin/models/MarkingRole.md) | `from foundry_sdk.v2.admin.models import MarkingRole` |
**Admin** | [MarkingRoleAssignment](docs/v2/Admin/models/MarkingRoleAssignment.md) | `from foundry_sdk.v2.admin.models import MarkingRoleAssignment` |
**Admin** | [MarkingRoleUpdate](docs/v2/Admin/models/MarkingRoleUpdate.md) | `from foundry_sdk.v2.admin.models import MarkingRoleUpdate` |
**Admin** | [MarkingType](docs/v2/Admin/models/MarkingType.md) | `from foundry_sdk.v2.admin.models import MarkingType` |
**Admin** | [OidcAuthenticationProtocol](docs/v2/Admin/models/OidcAuthenticationProtocol.md) | `from foundry_sdk.v2.admin.models import OidcAuthenticationProtocol` |
**Admin** | [Organization](docs/v2/Admin/models/Organization.md) | `from foundry_sdk.v2.admin.models import Organization` |
**Admin** | [OrganizationName](docs/v2/Admin/models/OrganizationName.md) | `from foundry_sdk.v2.admin.models import OrganizationName` |
**Admin** | [OrganizationRoleAssignment](docs/v2/Admin/models/OrganizationRoleAssignment.md) | `from foundry_sdk.v2.admin.models import OrganizationRoleAssignment` |
**Admin** | [PrincipalFilterType](docs/v2/Admin/models/PrincipalFilterType.md) | `from foundry_sdk.v2.admin.models import PrincipalFilterType` |
**Admin** | [ProviderId](docs/v2/Admin/models/ProviderId.md) | `from foundry_sdk.v2.admin.models import ProviderId` |
**Admin** | [Role](docs/v2/Admin/models/Role.md) | `from foundry_sdk.v2.admin.models import Role` |
**Admin** | [RoleDescription](docs/v2/Admin/models/RoleDescription.md) | `from foundry_sdk.v2.admin.models import RoleDescription` |
**Admin** | [RoleDisplayName](docs/v2/Admin/models/RoleDisplayName.md) | `from foundry_sdk.v2.admin.models import RoleDisplayName` |
**Admin** | [SamlAuthenticationProtocol](docs/v2/Admin/models/SamlAuthenticationProtocol.md) | `from foundry_sdk.v2.admin.models import SamlAuthenticationProtocol` |
**Admin** | [SamlServiceProviderMetadata](docs/v2/Admin/models/SamlServiceProviderMetadata.md) | `from foundry_sdk.v2.admin.models import SamlServiceProviderMetadata` |
**Admin** | [SearchGroupsResponse](docs/v2/Admin/models/SearchGroupsResponse.md) | `from foundry_sdk.v2.admin.models import SearchGroupsResponse` |
**Admin** | [SearchUsersResponse](docs/v2/Admin/models/SearchUsersResponse.md) | `from foundry_sdk.v2.admin.models import SearchUsersResponse` |
**Admin** | [User](docs/v2/Admin/models/User.md) | `from foundry_sdk.v2.admin.models import User` |
**Admin** | [UserProviderInfo](docs/v2/Admin/models/UserProviderInfo.md) | `from foundry_sdk.v2.admin.models import UserProviderInfo` |
**Admin** | [UserSearchFilter](docs/v2/Admin/models/UserSearchFilter.md) | `from foundry_sdk.v2.admin.models import UserSearchFilter` |
**Admin** | [UserUsername](docs/v2/Admin/models/UserUsername.md) | `from foundry_sdk.v2.admin.models import UserUsername` |
**AipAgents** | [Agent](docs/v2/AipAgents/models/Agent.md) | `from foundry_sdk.v2.aip_agents.models import Agent` |
**AipAgents** | [AgentMarkdownResponse](docs/v2/AipAgents/models/AgentMarkdownResponse.md) | `from foundry_sdk.v2.aip_agents.models import AgentMarkdownResponse` |
**AipAgents** | [AgentMetadata](docs/v2/AipAgents/models/AgentMetadata.md) | `from foundry_sdk.v2.aip_agents.models import AgentMetadata` |
**AipAgents** | [AgentRid](docs/v2/AipAgents/models/AgentRid.md) | `from foundry_sdk.v2.aip_agents.models import AgentRid` |
**AipAgents** | [AgentSessionRagContextResponse](docs/v2/AipAgents/models/AgentSessionRagContextResponse.md) | `from foundry_sdk.v2.aip_agents.models import AgentSessionRagContextResponse` |
**AipAgents** | [AgentsSessionsPage](docs/v2/AipAgents/models/AgentsSessionsPage.md) | `from foundry_sdk.v2.aip_agents.models import AgentsSessionsPage` |
**AipAgents** | [AgentVersion](docs/v2/AipAgents/models/AgentVersion.md) | `from foundry_sdk.v2.aip_agents.models import AgentVersion` |
**AipAgents** | [AgentVersionDetails](docs/v2/AipAgents/models/AgentVersionDetails.md) | `from foundry_sdk.v2.aip_agents.models import AgentVersionDetails` |
**AipAgents** | [AgentVersionString](docs/v2/AipAgents/models/AgentVersionString.md) | `from foundry_sdk.v2.aip_agents.models import AgentVersionString` |
**AipAgents** | [CancelSessionResponse](docs/v2/AipAgents/models/CancelSessionResponse.md) | `from foundry_sdk.v2.aip_agents.models import CancelSessionResponse` |
**AipAgents** | [Content](docs/v2/AipAgents/models/Content.md) | `from foundry_sdk.v2.aip_agents.models import Content` |
**AipAgents** | [FailureToolCallOutput](docs/v2/AipAgents/models/FailureToolCallOutput.md) | `from foundry_sdk.v2.aip_agents.models import FailureToolCallOutput` |
**AipAgents** | [FunctionRetrievedContext](docs/v2/AipAgents/models/FunctionRetrievedContext.md) | `from foundry_sdk.v2.aip_agents.models import FunctionRetrievedContext` |
**AipAgents** | [InputContext](docs/v2/AipAgents/models/InputContext.md) | `from foundry_sdk.v2.aip_agents.models import InputContext` |
**AipAgents** | [ListAgentVersionsResponse](docs/v2/AipAgents/models/ListAgentVersionsResponse.md) | `from foundry_sdk.v2.aip_agents.models import ListAgentVersionsResponse` |
**AipAgents** | [ListSessionsResponse](docs/v2/AipAgents/models/ListSessionsResponse.md) | `from foundry_sdk.v2.aip_agents.models import ListSessionsResponse` |
**AipAgents** | [MessageId](docs/v2/AipAgents/models/MessageId.md) | `from foundry_sdk.v2.aip_agents.models import MessageId` |
**AipAgents** | [ObjectContext](docs/v2/AipAgents/models/ObjectContext.md) | `from foundry_sdk.v2.aip_agents.models import ObjectContext` |
**AipAgents** | [ObjectSetParameter](docs/v2/AipAgents/models/ObjectSetParameter.md) | `from foundry_sdk.v2.aip_agents.models import ObjectSetParameter` |
**AipAgents** | [ObjectSetParameterValue](docs/v2/AipAgents/models/ObjectSetParameterValue.md) | `from foundry_sdk.v2.aip_agents.models import ObjectSetParameterValue` |
**AipAgents** | [ObjectSetParameterValueUpdate](docs/v2/AipAgents/models/ObjectSetParameterValueUpdate.md) | `from foundry_sdk.v2.aip_agents.models import ObjectSetParameterValueUpdate` |
**AipAgents** | [Parameter](docs/v2/AipAgents/models/Parameter.md) | `from foundry_sdk.v2.aip_agents.models import Parameter` |
**AipAgents** | [ParameterAccessMode](docs/v2/AipAgents/models/ParameterAccessMode.md) | `from foundry_sdk.v2.aip_agents.models import ParameterAccessMode` |
**AipAgents** | [ParameterId](docs/v2/AipAgents/models/ParameterId.md) | `from foundry_sdk.v2.aip_agents.models import ParameterId` |
**AipAgents** | [ParameterType](docs/v2/AipAgents/models/ParameterType.md) | `from foundry_sdk.v2.aip_agents.models import ParameterType` |
**AipAgents** | [ParameterValue](docs/v2/AipAgents/models/ParameterValue.md) | `from foundry_sdk.v2.aip_agents.models import ParameterValue` |
**AipAgents** | [ParameterValueUpdate](docs/v2/AipAgents/models/ParameterValueUpdate.md) | `from foundry_sdk.v2.aip_agents.models import ParameterValueUpdate` |
**AipAgents** | [RidToolInputValue](docs/v2/AipAgents/models/RidToolInputValue.md) | `from foundry_sdk.v2.aip_agents.models import RidToolInputValue` |
**AipAgents** | [RidToolOutputValue](docs/v2/AipAgents/models/RidToolOutputValue.md) | `from foundry_sdk.v2.aip_agents.models import RidToolOutputValue` |
**AipAgents** | [Session](docs/v2/AipAgents/models/Session.md) | `from foundry_sdk.v2.aip_agents.models import Session` |
**AipAgents** | [SessionExchange](docs/v2/AipAgents/models/SessionExchange.md) | `from foundry_sdk.v2.aip_agents.models import SessionExchange` |
**AipAgents** | [SessionExchangeContexts](docs/v2/AipAgents/models/SessionExchangeContexts.md) | `from foundry_sdk.v2.aip_agents.models import SessionExchangeContexts` |
**AipAgents** | [SessionExchangeResult](docs/v2/AipAgents/models/SessionExchangeResult.md) | `from foundry_sdk.v2.aip_agents.models import SessionExchangeResult` |
**AipAgents** | [SessionMetadata](docs/v2/AipAgents/models/SessionMetadata.md) | `from foundry_sdk.v2.aip_agents.models import SessionMetadata` |
**AipAgents** | [SessionRid](docs/v2/AipAgents/models/SessionRid.md) | `from foundry_sdk.v2.aip_agents.models import SessionRid` |
**AipAgents** | [SessionTrace](docs/v2/AipAgents/models/SessionTrace.md) | `from foundry_sdk.v2.aip_agents.models import SessionTrace` |
**AipAgents** | [SessionTraceId](docs/v2/AipAgents/models/SessionTraceId.md) | `from foundry_sdk.v2.aip_agents.models import SessionTraceId` |
**AipAgents** | [SessionTraceStatus](docs/v2/AipAgents/models/SessionTraceStatus.md) | `from foundry_sdk.v2.aip_agents.models import SessionTraceStatus` |
**AipAgents** | [StringParameter](docs/v2/AipAgents/models/StringParameter.md) | `from foundry_sdk.v2.aip_agents.models import StringParameter` |
**AipAgents** | [StringParameterValue](docs/v2/AipAgents/models/StringParameterValue.md) | `from foundry_sdk.v2.aip_agents.models import StringParameterValue` |
**AipAgents** | [StringToolInputValue](docs/v2/AipAgents/models/StringToolInputValue.md) | `from foundry_sdk.v2.aip_agents.models import StringToolInputValue` |
**AipAgents** | [StringToolOutputValue](docs/v2/AipAgents/models/StringToolOutputValue.md) | `from foundry_sdk.v2.aip_agents.models import StringToolOutputValue` |
**AipAgents** | [SuccessToolCallOutput](docs/v2/AipAgents/models/SuccessToolCallOutput.md) | `from foundry_sdk.v2.aip_agents.models import SuccessToolCallOutput` |
**AipAgents** | [ToolCall](docs/v2/AipAgents/models/ToolCall.md) | `from foundry_sdk.v2.aip_agents.models import ToolCall` |
**AipAgents** | [ToolCallGroup](docs/v2/AipAgents/models/ToolCallGroup.md) | `from foundry_sdk.v2.aip_agents.models import ToolCallGroup` |
**AipAgents** | [ToolCallInput](docs/v2/AipAgents/models/ToolCallInput.md) | `from foundry_sdk.v2.aip_agents.models import ToolCallInput` |
**AipAgents** | [ToolCallOutput](docs/v2/AipAgents/models/ToolCallOutput.md) | `from foundry_sdk.v2.aip_agents.models import ToolCallOutput` |
**AipAgents** | [ToolInputName](docs/v2/AipAgents/models/ToolInputName.md) | `from foundry_sdk.v2.aip_agents.models import ToolInputName` |
**AipAgents** | [ToolInputValue](docs/v2/AipAgents/models/ToolInputValue.md) | `from foundry_sdk.v2.aip_agents.models import ToolInputValue` |
**AipAgents** | [ToolMetadata](docs/v2/AipAgents/models/ToolMetadata.md) | `from foundry_sdk.v2.aip_agents.models import ToolMetadata` |
**AipAgents** | [ToolOutputValue](docs/v2/AipAgents/models/ToolOutputValue.md) | `from foundry_sdk.v2.aip_agents.models import ToolOutputValue` |
**AipAgents** | [ToolType](docs/v2/AipAgents/models/ToolType.md) | `from foundry_sdk.v2.aip_agents.models import ToolType` |
**AipAgents** | [UserTextInput](docs/v2/AipAgents/models/UserTextInput.md) | `from foundry_sdk.v2.aip_agents.models import UserTextInput` |
**Connectivity** | [ApiKeyAuthentication](docs/v2/Connectivity/models/ApiKeyAuthentication.md) | `from foundry_sdk.v2.connectivity.models import ApiKeyAuthentication` |
**Connectivity** | [AsPlaintextValue](docs/v2/Connectivity/models/AsPlaintextValue.md) | `from foundry_sdk.v2.connectivity.models import AsPlaintextValue` |
**Connectivity** | [AsSecretName](docs/v2/Connectivity/models/AsSecretName.md) | `from foundry_sdk.v2.connectivity.models import AsSecretName` |
**Connectivity** | [AwsAccessKey](docs/v2/Connectivity/models/AwsAccessKey.md) | `from foundry_sdk.v2.connectivity.models import AwsAccessKey` |
**Connectivity** | [AwsOidcAuthentication](docs/v2/Connectivity/models/AwsOidcAuthentication.md) | `from foundry_sdk.v2.connectivity.models import AwsOidcAuthentication` |
**Connectivity** | [BasicCredentials](docs/v2/Connectivity/models/BasicCredentials.md) | `from foundry_sdk.v2.connectivity.models import BasicCredentials` |
**Connectivity** | [BearerToken](docs/v2/Connectivity/models/BearerToken.md) | `from foundry_sdk.v2.connectivity.models import BearerToken` |
**Connectivity** | [CloudIdentity](docs/v2/Connectivity/models/CloudIdentity.md) | `from foundry_sdk.v2.connectivity.models import CloudIdentity` |
**Connectivity** | [CloudIdentityRid](docs/v2/Connectivity/models/CloudIdentityRid.md) | `from foundry_sdk.v2.connectivity.models import CloudIdentityRid` |
**Connectivity** | [Connection](docs/v2/Connectivity/models/Connection.md) | `from foundry_sdk.v2.connectivity.models import Connection` |
**Connectivity** | [ConnectionConfiguration](docs/v2/Connectivity/models/ConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import ConnectionConfiguration` |
**Connectivity** | [ConnectionDisplayName](docs/v2/Connectivity/models/ConnectionDisplayName.md) | `from foundry_sdk.v2.connectivity.models import ConnectionDisplayName` |
**Connectivity** | [ConnectionExportSettings](docs/v2/Connectivity/models/ConnectionExportSettings.md) | `from foundry_sdk.v2.connectivity.models import ConnectionExportSettings` |
**Connectivity** | [ConnectionRid](docs/v2/Connectivity/models/ConnectionRid.md) | `from foundry_sdk.v2.connectivity.models import ConnectionRid` |
**Connectivity** | [CreateConnectionRequestAsPlaintextValue](docs/v2/Connectivity/models/CreateConnectionRequestAsPlaintextValue.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestAsPlaintextValue` |
**Connectivity** | [CreateConnectionRequestAsSecretName](docs/v2/Connectivity/models/CreateConnectionRequestAsSecretName.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestAsSecretName` |
**Connectivity** | [CreateConnectionRequestBasicCredentials](docs/v2/Connectivity/models/CreateConnectionRequestBasicCredentials.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestBasicCredentials` |
**Connectivity** | [CreateConnectionRequestConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestDatabricksAuthenticationMode](docs/v2/Connectivity/models/CreateConnectionRequestDatabricksAuthenticationMode.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestDatabricksAuthenticationMode` |
**Connectivity** | [CreateConnectionRequestDatabricksConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestDatabricksConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestDatabricksConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestEncryptedProperty](docs/v2/Connectivity/models/CreateConnectionRequestEncryptedProperty.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestEncryptedProperty` |
**Connectivity** | [CreateConnectionRequestJdbcConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestJdbcConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestJdbcConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestOauthMachineToMachineAuth](docs/v2/Connectivity/models/CreateConnectionRequestOauthMachineToMachineAuth.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestOauthMachineToMachineAuth` |
**Connectivity** | [CreateConnectionRequestPersonalAccessToken](docs/v2/Connectivity/models/CreateConnectionRequestPersonalAccessToken.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestPersonalAccessToken` |
**Connectivity** | [CreateConnectionRequestRestConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestRestConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestRestConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestS3ConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestS3ConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestS3ConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestSnowflakeAuthenticationMode](docs/v2/Connectivity/models/CreateConnectionRequestSnowflakeAuthenticationMode.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestSnowflakeAuthenticationMode` |
**Connectivity** | [CreateConnectionRequestSnowflakeConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestSnowflakeConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestSnowflakeConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestSnowflakeExternalOauth](docs/v2/Connectivity/models/CreateConnectionRequestSnowflakeExternalOauth.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestSnowflakeExternalOauth` |
**Connectivity** | [CreateConnectionRequestSnowflakeKeyPairAuthentication](docs/v2/Connectivity/models/CreateConnectionRequestSnowflakeKeyPairAuthentication.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestSnowflakeKeyPairAuthentication` |
**Connectivity** | [CreateConnectionRequestWorkflowIdentityFederation](docs/v2/Connectivity/models/CreateConnectionRequestWorkflowIdentityFederation.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestWorkflowIdentityFederation` |
**Connectivity** | [CreateTableImportRequestDatabricksTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestDatabricksTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestDatabricksTableImportConfig` |
**Connectivity** | [CreateTableImportRequestJdbcTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestJdbcTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestJdbcTableImportConfig` |
**Connectivity** | [CreateTableImportRequestMicrosoftAccessTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestMicrosoftAccessTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestMicrosoftAccessTableImportConfig` |
**Connectivity** | [CreateTableImportRequestMicrosoftSqlServerTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestMicrosoftSqlServerTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestMicrosoftSqlServerTableImportConfig` |
**Connectivity** | [CreateTableImportRequestOracleTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestOracleTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestOracleTableImportConfig` |
**Connectivity** | [CreateTableImportRequestPostgreSqlTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestPostgreSqlTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestPostgreSqlTableImportConfig` |
**Connectivity** | [CreateTableImportRequestSnowflakeTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestSnowflakeTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestSnowflakeTableImportConfig` |
**Connectivity** | [CreateTableImportRequestTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestTableImportConfig` |
**Connectivity** | [DatabricksAuthenticationMode](docs/v2/Connectivity/models/DatabricksAuthenticationMode.md) | `from foundry_sdk.v2.connectivity.models import DatabricksAuthenticationMode` |
**Connectivity** | [DatabricksConnectionConfiguration](docs/v2/Connectivity/models/DatabricksConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import DatabricksConnectionConfiguration` |
**Connectivity** | [DatabricksTableImportConfig](docs/v2/Connectivity/models/DatabricksTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import DatabricksTableImportConfig` |
**Connectivity** | [DateColumnInitialIncrementalState](docs/v2/Connectivity/models/DateColumnInitialIncrementalState.md) | `from foundry_sdk.v2.connectivity.models import DateColumnInitialIncrementalState` |
**Connectivity** | [DecimalColumnInitialIncrementalState](docs/v2/Connectivity/models/DecimalColumnInitialIncrementalState.md) | `from foundry_sdk.v2.connectivity.models import DecimalColumnInitialIncrementalState` |
**Connectivity** | [Domain](docs/v2/Connectivity/models/Domain.md) | `from foundry_sdk.v2.connectivity.models import Domain` |
**Connectivity** | [EncryptedProperty](docs/v2/Connectivity/models/EncryptedProperty.md) | `from foundry_sdk.v2.connectivity.models import EncryptedProperty` |
**Connectivity** | [FileAnyPathMatchesFilter](docs/v2/Connectivity/models/FileAnyPathMatchesFilter.md) | `from foundry_sdk.v2.connectivity.models import FileAnyPathMatchesFilter` |
**Connectivity** | [FileAtLeastCountFilter](docs/v2/Connectivity/models/FileAtLeastCountFilter.md) | `from foundry_sdk.v2.connectivity.models import FileAtLeastCountFilter` |
**Connectivity** | [FileChangedSinceLastUploadFilter](docs/v2/Connectivity/models/FileChangedSinceLastUploadFilter.md) | `from foundry_sdk.v2.connectivity.models import FileChangedSinceLastUploadFilter` |
**Connectivity** | [FileImport](docs/v2/Connectivity/models/FileImport.md) | `from foundry_sdk.v2.connectivity.models import FileImport` |
**Connectivity** | [FileImportCustomFilter](docs/v2/Connectivity/models/FileImportCustomFilter.md) | `from foundry_sdk.v2.connectivity.models import FileImportCustomFilter` |
**Connectivity** | [FileImportDisplayName](docs/v2/Connectivity/models/FileImportDisplayName.md) | `from foundry_sdk.v2.connectivity.models import FileImportDisplayName` |
**Connectivity** | [FileImportFilter](docs/v2/Connectivity/models/FileImportFilter.md) | `from foundry_sdk.v2.connectivity.models import FileImportFilter` |
**Connectivity** | [FileImportMode](docs/v2/Connectivity/models/FileImportMode.md) | `from foundry_sdk.v2.connectivity.models import FileImportMode` |
**Connectivity** | [FileImportRid](docs/v2/Connectivity/models/FileImportRid.md) | `from foundry_sdk.v2.connectivity.models import FileImportRid` |
**Connectivity** | [FileLastModifiedAfterFilter](docs/v2/Connectivity/models/FileLastModifiedAfterFilter.md) | `from foundry_sdk.v2.connectivity.models import FileLastModifiedAfterFilter` |
**Connectivity** | [FilePathMatchesFilter](docs/v2/Connectivity/models/FilePathMatchesFilter.md) | `from foundry_sdk.v2.connectivity.models import FilePathMatchesFilter` |
**Connectivity** | [FilePathNotMatchesFilter](docs/v2/Connectivity/models/FilePathNotMatchesFilter.md) | `from foundry_sdk.v2.connectivity.models import FilePathNotMatchesFilter` |
**Connectivity** | [FileProperty](docs/v2/Connectivity/models/FileProperty.md) | `from foundry_sdk.v2.connectivity.models import FileProperty` |
**Connectivity** | [FilesCountLimitFilter](docs/v2/Connectivity/models/FilesCountLimitFilter.md) | `from foundry_sdk.v2.connectivity.models import FilesCountLimitFilter` |
**Connectivity** | [FileSizeFilter](docs/v2/Connectivity/models/FileSizeFilter.md) | `from foundry_sdk.v2.connectivity.models import FileSizeFilter` |
**Connectivity** | [HeaderApiKey](docs/v2/Connectivity/models/HeaderApiKey.md) | `from foundry_sdk.v2.connectivity.models import HeaderApiKey` |
**Connectivity** | [IntegerColumnInitialIncrementalState](docs/v2/Connectivity/models/IntegerColumnInitialIncrementalState.md) | `from foundry_sdk.v2.connectivity.models import IntegerColumnInitialIncrementalState` |
**Connectivity** | [JdbcConnectionConfiguration](docs/v2/Connectivity/models/JdbcConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import JdbcConnectionConfiguration` |
**Connectivity** | [JdbcProperties](docs/v2/Connectivity/models/JdbcProperties.md) | `from foundry_sdk.v2.connectivity.models import JdbcProperties` |
**Connectivity** | [JdbcTableImportConfig](docs/v2/Connectivity/models/JdbcTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import JdbcTableImportConfig` |
**Connectivity** | [ListFileImportsResponse](docs/v2/Connectivity/models/ListFileImportsResponse.md) | `from foundry_sdk.v2.connectivity.models import ListFileImportsResponse` |
**Connectivity** | [ListTableImportsResponse](docs/v2/Connectivity/models/ListTableImportsResponse.md) | `from foundry_sdk.v2.connectivity.models import ListTableImportsResponse` |
**Connectivity** | [LongColumnInitialIncrementalState](docs/v2/Connectivity/models/LongColumnInitialIncrementalState.md) | `from foundry_sdk.v2.connectivity.models import LongColumnInitialIncrementalState` |
**Connectivity** | [MicrosoftAccessTableImportConfig](docs/v2/Connectivity/models/MicrosoftAccessTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import MicrosoftAccessTableImportConfig` |
**Connectivity** | [MicrosoftSqlServerTableImportConfig](docs/v2/Connectivity/models/MicrosoftSqlServerTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import MicrosoftSqlServerTableImportConfig` |
**Connectivity** | [OauthMachineToMachineAuth](docs/v2/Connectivity/models/OauthMachineToMachineAuth.md) | `from foundry_sdk.v2.connectivity.models import OauthMachineToMachineAuth` |
**Connectivity** | [OracleTableImportConfig](docs/v2/Connectivity/models/OracleTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import OracleTableImportConfig` |
**Connectivity** | [PersonalAccessToken](docs/v2/Connectivity/models/PersonalAccessToken.md) | `from foundry_sdk.v2.connectivity.models import PersonalAccessToken` |
**Connectivity** | [PlaintextValue](docs/v2/Connectivity/models/PlaintextValue.md) | `from foundry_sdk.v2.connectivity.models import PlaintextValue` |
**Connectivity** | [PostgreSqlTableImportConfig](docs/v2/Connectivity/models/PostgreSqlTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import PostgreSqlTableImportConfig` |
**Connectivity** | [Protocol](docs/v2/Connectivity/models/Protocol.md) | `from foundry_sdk.v2.connectivity.models import Protocol` |
**Connectivity** | [QueryParameterApiKey](docs/v2/Connectivity/models/QueryParameterApiKey.md) | `from foundry_sdk.v2.connectivity.models import QueryParameterApiKey` |
**Connectivity** | [Region](docs/v2/Connectivity/models/Region.md) | `from foundry_sdk.v2.connectivity.models import Region` |
**Connectivity** | [ReplaceTableImportRequestDatabricksTableImportConfig](docs/v2/Connectivity/models/ReplaceTableImportRequestDatabricksTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import ReplaceTableImportRequestDatabricksTableImportConfig` |
**Connectivity** | [ReplaceTableImportRequestJdbcTableImportConfig](docs/v2/Connectivity/models/ReplaceTableImportRequestJdbcTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import ReplaceTableImportRequestJdbcTableImportConfig` |
**Connectivity** | [ReplaceTableImportRequestMicrosoftAccessTableImportConfig](docs/v2/Connectivity/models/ReplaceTableImportRequestMicrosoftAccessTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import ReplaceTableImportRequestMicrosoftAccessTableImportConfig` |
**Connectivity** | [ReplaceTableImportRequestMicrosoftSqlServerTableImportConfig](docs/v2/Connectivity/models/ReplaceTableImportRequestMicrosoftSqlServerTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import ReplaceTableImportRequestMicrosoftSqlServerTableImportConfig` |
**Connectivity** | [ReplaceTableImportRequestOracleTableImportConfig](docs/v2/Connectivity/models/ReplaceTableImportRequestOracleTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import ReplaceTableImportRequestOracleTableImportConfig` |
**Connectivity** | [ReplaceTableImportRequestPostgreSqlTableImportConfig](docs/v2/Connectivity/models/ReplaceTableImportRequestPostgreSqlTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import ReplaceTableImportRequestPostgreSqlTableImportConfig` |
**Connectivity** | [ReplaceTableImportRequestSnowflakeTableImportConfig](docs/v2/Connectivity/models/ReplaceTableImportRequestSnowflakeTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import ReplaceTableImportRequestSnowflakeTableImportConfig` |
**Connectivity** | [ReplaceTableImportRequestTableImportConfig](docs/v2/Connectivity/models/ReplaceTableImportRequestTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import ReplaceTableImportRequestTableImportConfig` |
**Connectivity** | [RestAuthenticationMode](docs/v2/Connectivity/models/RestAuthenticationMode.md) | `from foundry_sdk.v2.connectivity.models import RestAuthenticationMode` |
**Connectivity** | [RestConnectionAdditionalSecrets](docs/v2/Connectivity/models/RestConnectionAdditionalSecrets.md) | `from foundry_sdk.v2.connectivity.models import RestConnectionAdditionalSecrets` |
**Connectivity** | [RestConnectionConfiguration](docs/v2/Connectivity/models/RestConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import RestConnectionConfiguration` |
**Connectivity** | [RestConnectionOAuth2](docs/v2/Connectivity/models/RestConnectionOAuth2.md) | `from foundry_sdk.v2.connectivity.models import RestConnectionOAuth2` |
**Connectivity** | [RestRequestApiKeyLocation](docs/v2/Connectivity/models/RestRequestApiKeyLocation.md) | `from foundry_sdk.v2.connectivity.models import RestRequestApiKeyLocation` |
**Connectivity** | [S3AuthenticationMode](docs/v2/Connectivity/models/S3AuthenticationMode.md) | `from foundry_sdk.v2.connectivity.models import S3AuthenticationMode` |
**Connectivity** | [S3ConnectionConfiguration](docs/v2/Connectivity/models/S3ConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import S3ConnectionConfiguration` |
**Connectivity** | [S3KmsConfiguration](docs/v2/Connectivity/models/S3KmsConfiguration.md) | `from foundry_sdk.v2.connectivity.models import S3KmsConfiguration` |
**Connectivity** | [S3ProxyConfiguration](docs/v2/Connectivity/models/S3ProxyConfiguration.md) | `from foundry_sdk.v2.connectivity.models import S3ProxyConfiguration` |
**Connectivity** | [SecretName](docs/v2/Connectivity/models/SecretName.md) | `from foundry_sdk.v2.connectivity.models import SecretName` |
**Connectivity** | [SecretsNames](docs/v2/Connectivity/models/SecretsNames.md) | `from foundry_sdk.v2.connectivity.models import SecretsNames` |
**Connectivity** | [SecretsWithPlaintextValues](docs/v2/Connectivity/models/SecretsWithPlaintextValues.md) | `from foundry_sdk.v2.connectivity.models import SecretsWithPlaintextValues` |
**Connectivity** | [SnowflakeAuthenticationMode](docs/v2/Connectivity/models/SnowflakeAuthenticationMode.md) | `from foundry_sdk.v2.connectivity.models import SnowflakeAuthenticationMode` |
**Connectivity** | [SnowflakeConnectionConfiguration](docs/v2/Connectivity/models/SnowflakeConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import SnowflakeConnectionConfiguration` |
**Connectivity** | [SnowflakeExternalOauth](docs/v2/Connectivity/models/SnowflakeExternalOauth.md) | `from foundry_sdk.v2.connectivity.models import SnowflakeExternalOauth` |
**Connectivity** | [SnowflakeKeyPairAuthentication](docs/v2/Connectivity/models/SnowflakeKeyPairAuthentication.md) | `from foundry_sdk.v2.connectivity.models import SnowflakeKeyPairAuthentication` |
**Connectivity** | [SnowflakeTableImportConfig](docs/v2/Connectivity/models/SnowflakeTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import SnowflakeTableImportConfig` |
**Connectivity** | [StringColumnInitialIncrementalState](docs/v2/Connectivity/models/StringColumnInitialIncrementalState.md) | `from foundry_sdk.v2.connectivity.models import StringColumnInitialIncrementalState` |
**Connectivity** | [StsRoleConfiguration](docs/v2/Connectivity/models/StsRoleConfiguration.md) | `from foundry_sdk.v2.connectivity.models import StsRoleConfiguration` |
**Connectivity** | [TableImport](docs/v2/Connectivity/models/TableImport.md) | `from foundry_sdk.v2.connectivity.models import TableImport` |
**Connectivity** | [TableImportAllowSchemaChanges](docs/v2/Connectivity/models/TableImportAllowSchemaChanges.md) | `from foundry_sdk.v2.connectivity.models import TableImportAllowSchemaChanges` |
**Connectivity** | [TableImportConfig](docs/v2/Connectivity/models/TableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import TableImportConfig` |
**Connectivity** | [TableImportDisplayName](docs/v2/Connectivity/models/TableImportDisplayName.md) | `from foundry_sdk.v2.connectivity.models import TableImportDisplayName` |
**Connectivity** | [TableImportInitialIncrementalState](docs/v2/Connectivity/models/TableImportInitialIncrementalState.md) | `from foundry_sdk.v2.connectivity.models import TableImportInitialIncrementalState` |
**Connectivity** | [TableImportMode](docs/v2/Connectivity/models/TableImportMode.md) | `from foundry_sdk.v2.connectivity.models import TableImportMode` |
**Connectivity** | [TableImportQuery](docs/v2/Connectivity/models/TableImportQuery.md) | `from foundry_sdk.v2.connectivity.models import TableImportQuery` |
**Connectivity** | [TableImportRid](docs/v2/Connectivity/models/TableImportRid.md) | `from foundry_sdk.v2.connectivity.models import TableImportRid` |
**Connectivity** | [TimestampColumnInitialIncrementalState](docs/v2/Connectivity/models/TimestampColumnInitialIncrementalState.md) | `from foundry_sdk.v2.connectivity.models import TimestampColumnInitialIncrementalState` |
**Connectivity** | [UriScheme](docs/v2/Connectivity/models/UriScheme.md) | `from foundry_sdk.v2.connectivity.models import UriScheme` |
**Connectivity** | [WorkflowIdentityFederation](docs/v2/Connectivity/models/WorkflowIdentityFederation.md) | `from foundry_sdk.v2.connectivity.models import WorkflowIdentityFederation` |
**Core** | [AnyType](docs/v2/Core/models/AnyType.md) | `from foundry_sdk.v2.core.models import AnyType` |
**Core** | [ArrayFieldType](docs/v2/Core/models/ArrayFieldType.md) | `from foundry_sdk.v2.core.models import ArrayFieldType` |
**Core** | [AttachmentType](docs/v2/Core/models/AttachmentType.md) | `from foundry_sdk.v2.core.models import AttachmentType` |
**Core** | [BinaryType](docs/v2/Core/models/BinaryType.md) | `from foundry_sdk.v2.core.models import BinaryType` |
**Core** | [BooleanType](docs/v2/Core/models/BooleanType.md) | `from foundry_sdk.v2.core.models import BooleanType` |
**Core** | [BranchMetadata](docs/v2/Core/models/BranchMetadata.md) | `from foundry_sdk.v2.core.models import BranchMetadata` |
**Core** | [BuildRid](docs/v2/Core/models/BuildRid.md) | `from foundry_sdk.v2.core.models import BuildRid` |
**Core** | [ByteType](docs/v2/Core/models/ByteType.md) | `from foundry_sdk.v2.core.models import ByteType` |
**Core** | [ChangeDataCaptureConfiguration](docs/v2/Core/models/ChangeDataCaptureConfiguration.md) | `from foundry_sdk.v2.core.models import ChangeDataCaptureConfiguration` |
**Core** | [CipherTextType](docs/v2/Core/models/CipherTextType.md) | `from foundry_sdk.v2.core.models import CipherTextType` |
**Core** | [ComputeSeconds](docs/v2/Core/models/ComputeSeconds.md) | `from foundry_sdk.v2.core.models import ComputeSeconds` |
**Core** | [ContentLength](docs/v2/Core/models/ContentLength.md) | `from foundry_sdk.v2.core.models import ContentLength` |
**Core** | [ContentType](docs/v2/Core/models/ContentType.md) | `from foundry_sdk.v2.core.models import ContentType` |
**Core** | [CreatedBy](docs/v2/Core/models/CreatedBy.md) | `from foundry_sdk.v2.core.models import CreatedBy` |
**Core** | [CreatedTime](docs/v2/Core/models/CreatedTime.md) | `from foundry_sdk.v2.core.models import CreatedTime` |
**Core** | [CustomMetadata](docs/v2/Core/models/CustomMetadata.md) | `from foundry_sdk.v2.core.models import CustomMetadata` |
**Core** | [DatasetFieldSchema](docs/v2/Core/models/DatasetFieldSchema.md) | `from foundry_sdk.v2.core.models import DatasetFieldSchema` |
**Core** | [DatasetSchema](docs/v2/Core/models/DatasetSchema.md) | `from foundry_sdk.v2.core.models import DatasetSchema` |
**Core** | [DateType](docs/v2/Core/models/DateType.md) | `from foundry_sdk.v2.core.models import DateType` |
**Core** | [DecimalType](docs/v2/Core/models/DecimalType.md) | `from foundry_sdk.v2.core.models import DecimalType` |
**Core** | [DisplayName](docs/v2/Core/models/DisplayName.md) | `from foundry_sdk.v2.core.models import DisplayName` |
**Core** | [Distance](docs/v2/Core/models/Distance.md) | `from foundry_sdk.v2.core.models import Distance` |
**Core** | [DistanceUnit](docs/v2/Core/models/DistanceUnit.md) | `from foundry_sdk.v2.core.models import DistanceUnit` |
**Core** | [DoubleType](docs/v2/Core/models/DoubleType.md) | `from foundry_sdk.v2.core.models import DoubleType` |
**Core** | [Duration](docs/v2/Core/models/Duration.md) | `from foundry_sdk.v2.core.models import Duration` |
**Core** | [DurationSeconds](docs/v2/Core/models/DurationSeconds.md) | `from foundry_sdk.v2.core.models import DurationSeconds` |
**Core** | [EmbeddingModel](docs/v2/Core/models/EmbeddingModel.md) | `from foundry_sdk.v2.core.models import EmbeddingModel` |
**Core** | [EnrollmentRid](docs/v2/Core/models/EnrollmentRid.md) | `from foundry_sdk.v2.core.models import EnrollmentRid` |
**Core** | [Field](docs/v2/Core/models/Field.md) | `from foundry_sdk.v2.core.models import Field` |
**Core** | [FieldDataType](docs/v2/Core/models/FieldDataType.md) | `from foundry_sdk.v2.core.models import FieldDataType` |
**Core** | [FieldName](docs/v2/Core/models/FieldName.md) | `from foundry_sdk.v2.core.models import FieldName` |
**Core** | [FieldSchema](docs/v2/Core/models/FieldSchema.md) | `from foundry_sdk.v2.core.models import FieldSchema` |
**Core** | [Filename](docs/v2/Core/models/Filename.md) | `from foundry_sdk.v2.core.models import Filename` |
**Core** | [FilePath](docs/v2/Core/models/FilePath.md) | `from foundry_sdk.v2.core.models import FilePath` |
**Core** | [FilterBinaryType](docs/v2/Core/models/FilterBinaryType.md) | `from foundry_sdk.v2.core.models import FilterBinaryType` |
**Core** | [FilterBooleanType](docs/v2/Core/models/FilterBooleanType.md) | `from foundry_sdk.v2.core.models import FilterBooleanType` |
**Core** | [FilterDateTimeType](docs/v2/Core/models/FilterDateTimeType.md) | `from foundry_sdk.v2.core.models import FilterDateTimeType` |
**Core** | [FilterDateType](docs/v2/Core/models/FilterDateType.md) | `from foundry_sdk.v2.core.models import FilterDateType` |
**Core** | [FilterDoubleType](docs/v2/Core/models/FilterDoubleType.md) | `from foundry_sdk.v2.core.models import FilterDoubleType` |
**Core** | [FilterEnumType](docs/v2/Core/models/FilterEnumType.md) | `from foundry_sdk.v2.core.models import FilterEnumType` |
**Core** | [FilterFloatType](docs/v2/Core/models/FilterFloatType.md) | `from foundry_sdk.v2.core.models import FilterFloatType` |
**Core** | [FilterIntegerType](docs/v2/Core/models/FilterIntegerType.md) | `from foundry_sdk.v2.core.models import FilterIntegerType` |
**Core** | [FilterLongType](docs/v2/Core/models/FilterLongType.md) | `from foundry_sdk.v2.core.models import FilterLongType` |
**Core** | [FilterRidType](docs/v2/Core/models/FilterRidType.md) | `from foundry_sdk.v2.core.models import FilterRidType` |
**Core** | [FilterStringType](docs/v2/Core/models/FilterStringType.md) | `from foundry_sdk.v2.core.models import FilterStringType` |
**Core** | [FilterType](docs/v2/Core/models/FilterType.md) | `from foundry_sdk.v2.core.models import FilterType` |
**Core** | [FilterUuidType](docs/v2/Core/models/FilterUuidType.md) | `from foundry_sdk.v2.core.models import FilterUuidType` |
**Core** | [FloatType](docs/v2/Core/models/FloatType.md) | `from foundry_sdk.v2.core.models import FloatType` |
**Core** | [FolderRid](docs/v2/Core/models/FolderRid.md) | `from foundry_sdk.v2.core.models import FolderRid` |
**Core** | [FoundryBranch](docs/v2/Core/models/FoundryBranch.md) | `from foundry_sdk.v2.core.models import FoundryBranch` |
**Core** | [FoundryLiveDeployment](docs/v2/Core/models/FoundryLiveDeployment.md) | `from foundry_sdk.v2.core.models import FoundryLiveDeployment` |
**Core** | [FullRowChangeDataCaptureConfiguration](docs/v2/Core/models/FullRowChangeDataCaptureConfiguration.md) | `from foundry_sdk.v2.core.models import FullRowChangeDataCaptureConfiguration` |
**Core** | [GeohashType](docs/v2/Core/models/GeohashType.md) | `from foundry_sdk.v2.core.models import GeohashType` |
**Core** | [GeoPointType](docs/v2/Core/models/GeoPointType.md) | `from foundry_sdk.v2.core.models import GeoPointType` |
**Core** | [GeoShapeType](docs/v2/Core/models/GeoShapeType.md) | `from foundry_sdk.v2.core.models import GeoShapeType` |
**Core** | [GeotimeSeriesReferenceType](docs/v2/Core/models/GeotimeSeriesReferenceType.md) | `from foundry_sdk.v2.core.models import GeotimeSeriesReferenceType` |
**Core** | [GroupName](docs/v2/Core/models/GroupName.md) | `from foundry_sdk.v2.core.models import GroupName` |
**Core** | [GroupRid](docs/v2/Core/models/GroupRid.md) | `from foundry_sdk.v2.core.models import GroupRid` |
**Core** | [IncludeComputeUsage](docs/v2/Core/models/IncludeComputeUsage.md) | `from foundry_sdk.v2.core.models import IncludeComputeUsage` |
**Core** | [IntegerType](docs/v2/Core/models/IntegerType.md) | `from foundry_sdk.v2.core.models import IntegerType` |
**Core** | [JobRid](docs/v2/Core/models/JobRid.md) | `from foundry_sdk.v2.core.models import JobRid` |
**Core** | [LmsEmbeddingModel](docs/v2/Core/models/LmsEmbeddingModel.md) | `from foundry_sdk.v2.core.models import LmsEmbeddingModel` |
**Core** | [LmsEmbeddingModelValue](docs/v2/Core/models/LmsEmbeddingModelValue.md) | `from foundry_sdk.v2.core.models import LmsEmbeddingModelValue` |
**Core** | [LongType](docs/v2/Core/models/LongType.md) | `from foundry_sdk.v2.core.models import LongType` |
**Core** | [MapFieldType](docs/v2/Core/models/MapFieldType.md) | `from foundry_sdk.v2.core.models import MapFieldType` |
**Core** | [MarkingId](docs/v2/Core/models/MarkingId.md) | `from foundry_sdk.v2.core.models import MarkingId` |
**Core** | [MarkingType](docs/v2/Core/models/MarkingType.md) | `from foundry_sdk.v2.core.models import MarkingType` |
**Core** | [MediaItemPath](docs/v2/Core/models/MediaItemPath.md) | `from foundry_sdk.v2.core.models import MediaItemPath` |
**Core** | [MediaItemReadToken](docs/v2/Core/models/MediaItemReadToken.md) | `from foundry_sdk.v2.core.models import MediaItemReadToken` |
**Core** | [MediaItemRid](docs/v2/Core/models/MediaItemRid.md) | `from foundry_sdk.v2.core.models import MediaItemRid` |
**Core** | [MediaReference](docs/v2/Core/models/MediaReference.md) | `from foundry_sdk.v2.core.models import MediaReference` |
**Core** | [MediaReferenceType](docs/v2/Core/models/MediaReferenceType.md) | `from foundry_sdk.v2.core.models import MediaReferenceType` |
**Core** | [MediaSetRid](docs/v2/Core/models/MediaSetRid.md) | `from foundry_sdk.v2.core.models import MediaSetRid` |
**Core** | [MediaSetViewItem](docs/v2/Core/models/MediaSetViewItem.md) | `from foundry_sdk.v2.core.models import MediaSetViewItem` |
**Core** | [MediaSetViewItemWrapper](docs/v2/Core/models/MediaSetViewItemWrapper.md) | `from foundry_sdk.v2.core.models import MediaSetViewItemWrapper` |
**Core** | [MediaSetViewRid](docs/v2/Core/models/MediaSetViewRid.md) | `from foundry_sdk.v2.core.models import MediaSetViewRid` |
**Core** | [MediaType](docs/v2/Core/models/MediaType.md) | `from foundry_sdk.v2.core.models import MediaType` |
**Core** | [NullType](docs/v2/Core/models/NullType.md) | `from foundry_sdk.v2.core.models import NullType` |
**Core** | [Operation](docs/v2/Core/models/Operation.md) | `from foundry_sdk.v2.core.models import Operation` |
**Core** | [OperationScope](docs/v2/Core/models/OperationScope.md) | `from foundry_sdk.v2.core.models import OperationScope` |
**Core** | [OrderByDirection](docs/v2/Core/models/OrderByDirection.md) | `from foundry_sdk.v2.core.models import OrderByDirection` |
**Core** | [OrganizationRid](docs/v2/Core/models/OrganizationRid.md) | `from foundry_sdk.v2.core.models import OrganizationRid` |
**Core** | [PageSize](docs/v2/Core/models/PageSize.md) | `from foundry_sdk.v2.core.models import PageSize` |
**Core** | [PageToken](docs/v2/Core/models/PageToken.md) | `from foundry_sdk.v2.core.models import PageToken` |
**Core** | [PreviewMode](docs/v2/Core/models/PreviewMode.md) | `from foundry_sdk.v2.core.models import PreviewMode` |
**Core** | [PrincipalId](docs/v2/Core/models/PrincipalId.md) | `from foundry_sdk.v2.core.models import PrincipalId` |
**Core** | [PrincipalType](docs/v2/Core/models/PrincipalType.md) | `from foundry_sdk.v2.core.models import PrincipalType` |
**Core** | [Realm](docs/v2/Core/models/Realm.md) | `from foundry_sdk.v2.core.models import Realm` |
**Core** | [Reference](docs/v2/Core/models/Reference.md) | `from foundry_sdk.v2.core.models import Reference` |
**Core** | [ReleaseStatus](docs/v2/Core/models/ReleaseStatus.md) | `from foundry_sdk.v2.core.models import ReleaseStatus` |
**Core** | [Role](docs/v2/Core/models/Role.md) | `from foundry_sdk.v2.core.models import Role` |
**Core** | [RoleAssignmentUpdate](docs/v2/Core/models/RoleAssignmentUpdate.md) | `from foundry_sdk.v2.core.models import RoleAssignmentUpdate` |
**Core** | [RoleContext](docs/v2/Core/models/RoleContext.md) | `from foundry_sdk.v2.core.models import RoleContext` |
**Core** | [RoleId](docs/v2/Core/models/RoleId.md) | `from foundry_sdk.v2.core.models import RoleId` |
**Core** | [RoleSetId](docs/v2/Core/models/RoleSetId.md) | `from foundry_sdk.v2.core.models import RoleSetId` |
**Core** | [ScheduleRid](docs/v2/Core/models/ScheduleRid.md) | `from foundry_sdk.v2.core.models import ScheduleRid` |
**Core** | [ShortType](docs/v2/Core/models/ShortType.md) | `from foundry_sdk.v2.core.models import ShortType` |
**Core** | [SizeBytes](docs/v2/Core/models/SizeBytes.md) | `from foundry_sdk.v2.core.models import SizeBytes` |
**Core** | [StreamSchema](docs/v2/Core/models/StreamSchema.md) | `from foundry_sdk.v2.core.models import StreamSchema` |
**Core** | [StringType](docs/v2/Core/models/StringType.md) | `from foundry_sdk.v2.core.models import StringType` |
**Core** | [StructFieldName](docs/v2/Core/models/StructFieldName.md) | `from foundry_sdk.v2.core.models import StructFieldName` |
**Core** | [StructFieldType](docs/v2/Core/models/StructFieldType.md) | `from foundry_sdk.v2.core.models import StructFieldType` |
**Core** | [TimeSeriesItemType](docs/v2/Core/models/TimeSeriesItemType.md) | `from foundry_sdk.v2.core.models import TimeSeriesItemType` |
**Core** | [TimeseriesType](docs/v2/Core/models/TimeseriesType.md) | `from foundry_sdk.v2.core.models import TimeseriesType` |
**Core** | [TimestampType](docs/v2/Core/models/TimestampType.md) | `from foundry_sdk.v2.core.models import TimestampType` |
**Core** | [TimeUnit](docs/v2/Core/models/TimeUnit.md) | `from foundry_sdk.v2.core.models import TimeUnit` |
**Core** | [TotalCount](docs/v2/Core/models/TotalCount.md) | `from foundry_sdk.v2.core.models import TotalCount` |
**Core** | [TraceParent](docs/v2/Core/models/TraceParent.md) | `from foundry_sdk.v2.core.models import TraceParent` |
**Core** | [TraceState](docs/v2/Core/models/TraceState.md) | `from foundry_sdk.v2.core.models import TraceState` |
**Core** | [UnsupportedType](docs/v2/Core/models/UnsupportedType.md) | `from foundry_sdk.v2.core.models import UnsupportedType` |
**Core** | [UpdatedBy](docs/v2/Core/models/UpdatedBy.md) | `from foundry_sdk.v2.core.models import UpdatedBy` |
**Core** | [UpdatedTime](docs/v2/Core/models/UpdatedTime.md) | `from foundry_sdk.v2.core.models import UpdatedTime` |
**Core** | [UserId](docs/v2/Core/models/UserId.md) | `from foundry_sdk.v2.core.models import UserId` |
**Core** | [VectorSimilarityFunction](docs/v2/Core/models/VectorSimilarityFunction.md) | `from foundry_sdk.v2.core.models import VectorSimilarityFunction` |
**Core** | [VectorSimilarityFunctionValue](docs/v2/Core/models/VectorSimilarityFunctionValue.md) | `from foundry_sdk.v2.core.models import VectorSimilarityFunctionValue` |
**Core** | [VectorType](docs/v2/Core/models/VectorType.md) | `from foundry_sdk.v2.core.models import VectorType` |
**Core** | [VersionId](docs/v2/Core/models/VersionId.md) | `from foundry_sdk.v2.core.models import VersionId` |
**Core** | [ZoneId](docs/v2/Core/models/ZoneId.md) | `from foundry_sdk.v2.core.models import ZoneId` |
**Datasets** | [Branch](docs/v2/Datasets/models/Branch.md) | `from foundry_sdk.v2.datasets.models import Branch` |
**Datasets** | [BranchName](docs/v2/Datasets/models/BranchName.md) | `from foundry_sdk.v2.datasets.models import BranchName` |
**Datasets** | [DataframeReader](docs/v2/Datasets/models/DataframeReader.md) | `from foundry_sdk.v2.datasets.models import DataframeReader` |
**Datasets** | [Dataset](docs/v2/Datasets/models/Dataset.md) | `from foundry_sdk.v2.datasets.models import Dataset` |
**Datasets** | [DatasetName](docs/v2/Datasets/models/DatasetName.md) | `from foundry_sdk.v2.datasets.models import DatasetName` |
**Datasets** | [DatasetRid](docs/v2/Datasets/models/DatasetRid.md) | `from foundry_sdk.v2.datasets.models import DatasetRid` |
**Datasets** | [File](docs/v2/Datasets/models/File.md) | `from foundry_sdk.v2.datasets.models import File` |
**Datasets** | [FileUpdatedTime](docs/v2/Datasets/models/FileUpdatedTime.md) | `from foundry_sdk.v2.datasets.models import FileUpdatedTime` |
**Datasets** | [GetDatasetSchemaResponse](docs/v2/Datasets/models/GetDatasetSchemaResponse.md) | `from foundry_sdk.v2.datasets.models import GetDatasetSchemaResponse` |
**Datasets** | [ListBranchesResponse](docs/v2/Datasets/models/ListBranchesResponse.md) | `from foundry_sdk.v2.datasets.models import ListBranchesResponse` |
**Datasets** | [ListFilesResponse](docs/v2/Datasets/models/ListFilesResponse.md) | `from foundry_sdk.v2.datasets.models import ListFilesResponse` |
**Datasets** | [ListSchedulesResponse](docs/v2/Datasets/models/ListSchedulesResponse.md) | `from foundry_sdk.v2.datasets.models import ListSchedulesResponse` |
**Datasets** | [ListTransactionsOfDatasetResponse](docs/v2/Datasets/models/ListTransactionsOfDatasetResponse.md) | `from foundry_sdk.v2.datasets.models import ListTransactionsOfDatasetResponse` |
**Datasets** | [ListTransactionsResponse](docs/v2/Datasets/models/ListTransactionsResponse.md) | `from foundry_sdk.v2.datasets.models import ListTransactionsResponse` |
**Datasets** | [PrimaryKeyLatestWinsResolutionStrategy](docs/v2/Datasets/models/PrimaryKeyLatestWinsResolutionStrategy.md) | `from foundry_sdk.v2.datasets.models import PrimaryKeyLatestWinsResolutionStrategy` |
**Datasets** | [PrimaryKeyResolutionDuplicate](docs/v2/Datasets/models/PrimaryKeyResolutionDuplicate.md) | `from foundry_sdk.v2.datasets.models import PrimaryKeyResolutionDuplicate` |
**Datasets** | [PrimaryKeyResolutionStrategy](docs/v2/Datasets/models/PrimaryKeyResolutionStrategy.md) | `from foundry_sdk.v2.datasets.models import PrimaryKeyResolutionStrategy` |
**Datasets** | [PrimaryKeyResolutionUnique](docs/v2/Datasets/models/PrimaryKeyResolutionUnique.md) | `from foundry_sdk.v2.datasets.models import PrimaryKeyResolutionUnique` |
**Datasets** | [TableExportFormat](docs/v2/Datasets/models/TableExportFormat.md) | `from foundry_sdk.v2.datasets.models import TableExportFormat` |
**Datasets** | [Transaction](docs/v2/Datasets/models/Transaction.md) | `from foundry_sdk.v2.datasets.models import Transaction` |
**Datasets** | [TransactionCreatedTime](docs/v2/Datasets/models/TransactionCreatedTime.md) | `from foundry_sdk.v2.datasets.models import TransactionCreatedTime` |
**Datasets** | [TransactionRid](docs/v2/Datasets/models/TransactionRid.md) | `from foundry_sdk.v2.datasets.models import TransactionRid` |
**Datasets** | [TransactionStatus](docs/v2/Datasets/models/TransactionStatus.md) | `from foundry_sdk.v2.datasets.models import TransactionStatus` |
**Datasets** | [TransactionType](docs/v2/Datasets/models/TransactionType.md) | `from foundry_sdk.v2.datasets.models import TransactionType` |
**Datasets** | [View](docs/v2/Datasets/models/View.md) | `from foundry_sdk.v2.datasets.models import View` |
**Datasets** | [ViewBackingDataset](docs/v2/Datasets/models/ViewBackingDataset.md) | `from foundry_sdk.v2.datasets.models import ViewBackingDataset` |
**Datasets** | [ViewPrimaryKey](docs/v2/Datasets/models/ViewPrimaryKey.md) | `from foundry_sdk.v2.datasets.models import ViewPrimaryKey` |
**Datasets** | [ViewPrimaryKeyResolution](docs/v2/Datasets/models/ViewPrimaryKeyResolution.md) | `from foundry_sdk.v2.datasets.models import ViewPrimaryKeyResolution` |
**Filesystem** | [AccessRequirements](docs/v2/Filesystem/models/AccessRequirements.md) | `from foundry_sdk.v2.filesystem.models import AccessRequirements` |
**Filesystem** | [Everyone](docs/v2/Filesystem/models/Everyone.md) | `from foundry_sdk.v2.filesystem.models import Everyone` |
**Filesystem** | [FileSystemId](docs/v2/Filesystem/models/FileSystemId.md) | `from foundry_sdk.v2.filesystem.models import FileSystemId` |
**Filesystem** | [Folder](docs/v2/Filesystem/models/Folder.md) | `from foundry_sdk.v2.filesystem.models import Folder` |
**Filesystem** | [FolderRid](docs/v2/Filesystem/models/FolderRid.md) | `from foundry_sdk.v2.filesystem.models import FolderRid` |
**Filesystem** | [FolderType](docs/v2/Filesystem/models/FolderType.md) | `from foundry_sdk.v2.filesystem.models import FolderType` |
**Filesystem** | [IsDirectlyApplied](docs/v2/Filesystem/models/IsDirectlyApplied.md) | `from foundry_sdk.v2.filesystem.models import IsDirectlyApplied` |
**Filesystem** | [ListChildrenOfFolderResponse](docs/v2/Filesystem/models/ListChildrenOfFolderResponse.md) | `from foundry_sdk.v2.filesystem.models import ListChildrenOfFolderResponse` |
**Filesystem** | [ListMarkingsOfResourceResponse](docs/v2/Filesystem/models/ListMarkingsOfResourceResponse.md) | `from foundry_sdk.v2.filesystem.models import ListMarkingsOfResourceResponse` |
**Filesystem** | [ListOrganizationsOfProjectResponse](docs/v2/Filesystem/models/ListOrganizationsOfProjectResponse.md) | `from foundry_sdk.v2.filesystem.models import ListOrganizationsOfProjectResponse` |
**Filesystem** | [ListResourceRolesResponse](docs/v2/Filesystem/models/ListResourceRolesResponse.md) | `from foundry_sdk.v2.filesystem.models import ListResourceRolesResponse` |
**Filesystem** | [ListSpacesResponse](docs/v2/Filesystem/models/ListSpacesResponse.md) | `from foundry_sdk.v2.filesystem.models import ListSpacesResponse` |
**Filesystem** | [Marking](docs/v2/Filesystem/models/Marking.md) | `from foundry_sdk.v2.filesystem.models import Marking` |
**Filesystem** | [Organization](docs/v2/Filesystem/models/Organization.md) | `from foundry_sdk.v2.filesystem.models import Organization` |
**Filesystem** | [PrincipalWithId](docs/v2/Filesystem/models/PrincipalWithId.md) | `from foundry_sdk.v2.filesystem.models import PrincipalWithId` |
**Filesystem** | [Project](docs/v2/Filesystem/models/Project.md) | `from foundry_sdk.v2.filesystem.models import Project` |
**Filesystem** | [ProjectRid](docs/v2/Filesystem/models/ProjectRid.md) | `from foundry_sdk.v2.filesystem.models import ProjectRid` |
**Filesystem** | [ProjectTemplateRid](docs/v2/Filesystem/models/ProjectTemplateRid.md) | `from foundry_sdk.v2.filesystem.models import ProjectTemplateRid` |
**Filesystem** | [ProjectTemplateVariableId](docs/v2/Filesystem/models/ProjectTemplateVariableId.md) | `from foundry_sdk.v2.filesystem.models import ProjectTemplateVariableId` |
**Filesystem** | [ProjectTemplateVariableValue](docs/v2/Filesystem/models/ProjectTemplateVariableValue.md) | `from foundry_sdk.v2.filesystem.models import ProjectTemplateVariableValue` |
**Filesystem** | [Resource](docs/v2/Filesystem/models/Resource.md) | `from foundry_sdk.v2.filesystem.models import Resource` |
**Filesystem** | [ResourceDisplayName](docs/v2/Filesystem/models/ResourceDisplayName.md) | `from foundry_sdk.v2.filesystem.models import ResourceDisplayName` |
**Filesystem** | [ResourcePath](docs/v2/Filesystem/models/ResourcePath.md) | `from foundry_sdk.v2.filesystem.models import ResourcePath` |
**Filesystem** | [ResourceRid](docs/v2/Filesystem/models/ResourceRid.md) | `from foundry_sdk.v2.filesystem.models import ResourceRid` |
**Filesystem** | [ResourceRole](docs/v2/Filesystem/models/ResourceRole.md) | `from foundry_sdk.v2.filesystem.models import ResourceRole` |
**Filesystem** | [ResourceRolePrincipal](docs/v2/Filesystem/models/ResourceRolePrincipal.md) | `from foundry_sdk.v2.filesystem.models import ResourceRolePrincipal` |
**Filesystem** | [ResourceType](docs/v2/Filesystem/models/ResourceType.md) | `from foundry_sdk.v2.filesystem.models import ResourceType` |
**Filesystem** | [Space](docs/v2/Filesystem/models/Space.md) | `from foundry_sdk.v2.filesystem.models import Space` |
**Filesystem** | [SpaceRid](docs/v2/Filesystem/models/SpaceRid.md) | `from foundry_sdk.v2.filesystem.models import SpaceRid` |
**Filesystem** | [TrashStatus](docs/v2/Filesystem/models/TrashStatus.md) | `from foundry_sdk.v2.filesystem.models import TrashStatus` |
**Filesystem** | [UsageAccountRid](docs/v2/Filesystem/models/UsageAccountRid.md) | `from foundry_sdk.v2.filesystem.models import UsageAccountRid` |
**Functions** | [DataValue](docs/v2/Functions/models/DataValue.md) | `from foundry_sdk.v2.functions.models import DataValue` |
**Functions** | [ExecuteQueryResponse](docs/v2/Functions/models/ExecuteQueryResponse.md) | `from foundry_sdk.v2.functions.models import ExecuteQueryResponse` |
**Functions** | [FunctionRid](docs/v2/Functions/models/FunctionRid.md) | `from foundry_sdk.v2.functions.models import FunctionRid` |
**Functions** | [FunctionVersion](docs/v2/Functions/models/FunctionVersion.md) | `from foundry_sdk.v2.functions.models import FunctionVersion` |
**Functions** | [Parameter](docs/v2/Functions/models/Parameter.md) | `from foundry_sdk.v2.functions.models import Parameter` |
**Functions** | [ParameterId](docs/v2/Functions/models/ParameterId.md) | `from foundry_sdk.v2.functions.models import ParameterId` |
**Functions** | [Query](docs/v2/Functions/models/Query.md) | `from foundry_sdk.v2.functions.models import Query` |
**Functions** | [QueryAggregationKeyType](docs/v2/Functions/models/QueryAggregationKeyType.md) | `from foundry_sdk.v2.functions.models import QueryAggregationKeyType` |
**Functions** | [QueryAggregationRangeSubType](docs/v2/Functions/models/QueryAggregationRangeSubType.md) | `from foundry_sdk.v2.functions.models import QueryAggregationRangeSubType` |
**Functions** | [QueryAggregationRangeType](docs/v2/Functions/models/QueryAggregationRangeType.md) | `from foundry_sdk.v2.functions.models import QueryAggregationRangeType` |
**Functions** | [QueryAggregationValueType](docs/v2/Functions/models/QueryAggregationValueType.md) | `from foundry_sdk.v2.functions.models import QueryAggregationValueType` |
**Functions** | [QueryApiName](docs/v2/Functions/models/QueryApiName.md) | `from foundry_sdk.v2.functions.models import QueryApiName` |
**Functions** | [QueryArrayType](docs/v2/Functions/models/QueryArrayType.md) | `from foundry_sdk.v2.functions.models import QueryArrayType` |
**Functions** | [QueryDataType](docs/v2/Functions/models/QueryDataType.md) | `from foundry_sdk.v2.functions.models import QueryDataType` |
**Functions** | [QueryRuntimeErrorParameter](docs/v2/Functions/models/QueryRuntimeErrorParameter.md) | `from foundry_sdk.v2.functions.models import QueryRuntimeErrorParameter` |
**Functions** | [QuerySetType](docs/v2/Functions/models/QuerySetType.md) | `from foundry_sdk.v2.functions.models import QuerySetType` |
**Functions** | [QueryStructField](docs/v2/Functions/models/QueryStructField.md) | `from foundry_sdk.v2.functions.models import QueryStructField` |
**Functions** | [QueryStructType](docs/v2/Functions/models/QueryStructType.md) | `from foundry_sdk.v2.functions.models import QueryStructType` |
**Functions** | [QueryUnionType](docs/v2/Functions/models/QueryUnionType.md) | `from foundry_sdk.v2.functions.models import QueryUnionType` |
**Functions** | [StructFieldName](docs/v2/Functions/models/StructFieldName.md) | `from foundry_sdk.v2.functions.models import StructFieldName` |
**Functions** | [ThreeDimensionalAggregation](docs/v2/Functions/models/ThreeDimensionalAggregation.md) | `from foundry_sdk.v2.functions.models import ThreeDimensionalAggregation` |
**Functions** | [TwoDimensionalAggregation](docs/v2/Functions/models/TwoDimensionalAggregation.md) | `from foundry_sdk.v2.functions.models import TwoDimensionalAggregation` |
**Functions** | [ValueType](docs/v2/Functions/models/ValueType.md) | `from foundry_sdk.v2.functions.models import ValueType` |
**Functions** | [ValueTypeApiName](docs/v2/Functions/models/ValueTypeApiName.md) | `from foundry_sdk.v2.functions.models import ValueTypeApiName` |
**Functions** | [ValueTypeDataType](docs/v2/Functions/models/ValueTypeDataType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataType` |
**Functions** | [ValueTypeDataTypeArrayType](docs/v2/Functions/models/ValueTypeDataTypeArrayType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeArrayType` |
**Functions** | [ValueTypeDataTypeBinaryType](docs/v2/Functions/models/ValueTypeDataTypeBinaryType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeBinaryType` |
**Functions** | [ValueTypeDataTypeBooleanType](docs/v2/Functions/models/ValueTypeDataTypeBooleanType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeBooleanType` |
**Functions** | [ValueTypeDataTypeByteType](docs/v2/Functions/models/ValueTypeDataTypeByteType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeByteType` |
**Functions** | [ValueTypeDataTypeDateType](docs/v2/Functions/models/ValueTypeDataTypeDateType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeDateType` |
**Functions** | [ValueTypeDataTypeDecimalType](docs/v2/Functions/models/ValueTypeDataTypeDecimalType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeDecimalType` |
**Functions** | [ValueTypeDataTypeDoubleType](docs/v2/Functions/models/ValueTypeDataTypeDoubleType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeDoubleType` |
**Functions** | [ValueTypeDataTypeFloatType](docs/v2/Functions/models/ValueTypeDataTypeFloatType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeFloatType` |
**Functions** | [ValueTypeDataTypeIntegerType](docs/v2/Functions/models/ValueTypeDataTypeIntegerType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeIntegerType` |
**Functions** | [ValueTypeDataTypeLongType](docs/v2/Functions/models/ValueTypeDataTypeLongType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeLongType` |
**Functions** | [ValueTypeDataTypeMapType](docs/v2/Functions/models/ValueTypeDataTypeMapType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeMapType` |
**Functions** | [ValueTypeDataTypeOptionalType](docs/v2/Functions/models/ValueTypeDataTypeOptionalType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeOptionalType` |
**Functions** | [ValueTypeDataTypeShortType](docs/v2/Functions/models/ValueTypeDataTypeShortType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeShortType` |
**Functions** | [ValueTypeDataTypeStringType](docs/v2/Functions/models/ValueTypeDataTypeStringType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeStringType` |
**Functions** | [ValueTypeDataTypeStructElement](docs/v2/Functions/models/ValueTypeDataTypeStructElement.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeStructElement` |
**Functions** | [ValueTypeDataTypeStructFieldIdentifier](docs/v2/Functions/models/ValueTypeDataTypeStructFieldIdentifier.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeStructFieldIdentifier` |
**Functions** | [ValueTypeDataTypeStructType](docs/v2/Functions/models/ValueTypeDataTypeStructType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeStructType` |
**Functions** | [ValueTypeDataTypeTimestampType](docs/v2/Functions/models/ValueTypeDataTypeTimestampType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeTimestampType` |
**Functions** | [ValueTypeDataTypeUnionType](docs/v2/Functions/models/ValueTypeDataTypeUnionType.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeUnionType` |
**Functions** | [ValueTypeDataTypeValueTypeReference](docs/v2/Functions/models/ValueTypeDataTypeValueTypeReference.md) | `from foundry_sdk.v2.functions.models import ValueTypeDataTypeValueTypeReference` |
**Functions** | [ValueTypeDescription](docs/v2/Functions/models/ValueTypeDescription.md) | `from foundry_sdk.v2.functions.models import ValueTypeDescription` |
**Functions** | [ValueTypeReference](docs/v2/Functions/models/ValueTypeReference.md) | `from foundry_sdk.v2.functions.models import ValueTypeReference` |
**Functions** | [ValueTypeRid](docs/v2/Functions/models/ValueTypeRid.md) | `from foundry_sdk.v2.functions.models import ValueTypeRid` |
**Functions** | [ValueTypeVersion](docs/v2/Functions/models/ValueTypeVersion.md) | `from foundry_sdk.v2.functions.models import ValueTypeVersion` |
**Functions** | [ValueTypeVersionId](docs/v2/Functions/models/ValueTypeVersionId.md) | `from foundry_sdk.v2.functions.models import ValueTypeVersionId` |
**Functions** | [VersionId](docs/v2/Functions/models/VersionId.md) | `from foundry_sdk.v2.functions.models import VersionId` |
**Geo** | [BBox](docs/v2/Geo/models/BBox.md) | `from foundry_sdk.v2.geo.models import BBox` |
**Geo** | [Coordinate](docs/v2/Geo/models/Coordinate.md) | `from foundry_sdk.v2.geo.models import Coordinate` |
**Geo** | [Feature](docs/v2/Geo/models/Feature.md) | `from foundry_sdk.v2.geo.models import Feature` |
**Geo** | [FeatureCollection](docs/v2/Geo/models/FeatureCollection.md) | `from foundry_sdk.v2.geo.models import FeatureCollection` |
**Geo** | [FeatureCollectionTypes](docs/v2/Geo/models/FeatureCollectionTypes.md) | `from foundry_sdk.v2.geo.models import FeatureCollectionTypes` |
**Geo** | [FeaturePropertyKey](docs/v2/Geo/models/FeaturePropertyKey.md) | `from foundry_sdk.v2.geo.models import FeaturePropertyKey` |
**Geo** | [Geometry](docs/v2/Geo/models/Geometry.md) | `from foundry_sdk.v2.geo.models import Geometry` |
**Geo** | [GeometryCollection](docs/v2/Geo/models/GeometryCollection.md) | `from foundry_sdk.v2.geo.models import GeometryCollection` |
**Geo** | [GeoPoint](docs/v2/Geo/models/GeoPoint.md) | `from foundry_sdk.v2.geo.models import GeoPoint` |
**Geo** | [LinearRing](docs/v2/Geo/models/LinearRing.md) | `from foundry_sdk.v2.geo.models import LinearRing` |
**Geo** | [LineString](docs/v2/Geo/models/LineString.md) | `from foundry_sdk.v2.geo.models import LineString` |
**Geo** | [LineStringCoordinates](docs/v2/Geo/models/LineStringCoordinates.md) | `from foundry_sdk.v2.geo.models import LineStringCoordinates` |
**Geo** | [MultiLineString](docs/v2/Geo/models/MultiLineString.md) | `from foundry_sdk.v2.geo.models import MultiLineString` |
**Geo** | [MultiPoint](docs/v2/Geo/models/MultiPoint.md) | `from foundry_sdk.v2.geo.models import MultiPoint` |
**Geo** | [MultiPolygon](docs/v2/Geo/models/MultiPolygon.md) | `from foundry_sdk.v2.geo.models import MultiPolygon` |
**Geo** | [Polygon](docs/v2/Geo/models/Polygon.md) | `from foundry_sdk.v2.geo.models import Polygon` |
**Geo** | [Position](docs/v2/Geo/models/Position.md) | `from foundry_sdk.v2.geo.models import Position` |
**MediaSets** | [BranchName](docs/v2/MediaSets/models/BranchName.md) | `from foundry_sdk.v2.media_sets.models import BranchName` |
**MediaSets** | [BranchRid](docs/v2/MediaSets/models/BranchRid.md) | `from foundry_sdk.v2.media_sets.models import BranchRid` |
**MediaSets** | [GetMediaItemInfoResponse](docs/v2/MediaSets/models/GetMediaItemInfoResponse.md) | `from foundry_sdk.v2.media_sets.models import GetMediaItemInfoResponse` |
**MediaSets** | [GetMediaItemRidByPathResponse](docs/v2/MediaSets/models/GetMediaItemRidByPathResponse.md) | `from foundry_sdk.v2.media_sets.models import GetMediaItemRidByPathResponse` |
**MediaSets** | [LogicalTimestamp](docs/v2/MediaSets/models/LogicalTimestamp.md) | `from foundry_sdk.v2.media_sets.models import LogicalTimestamp` |
**MediaSets** | [MediaAttribution](docs/v2/MediaSets/models/MediaAttribution.md) | `from foundry_sdk.v2.media_sets.models import MediaAttribution` |
**MediaSets** | [PutMediaItemResponse](docs/v2/MediaSets/models/PutMediaItemResponse.md) | `from foundry_sdk.v2.media_sets.models import PutMediaItemResponse` |
**MediaSets** | [TransactionId](docs/v2/MediaSets/models/TransactionId.md) | `from foundry_sdk.v2.media_sets.models import TransactionId` |
**Ontologies** | [AbsoluteTimeRange](docs/v2/Ontologies/models/AbsoluteTimeRange.md) | `from foundry_sdk.v2.ontologies.models import AbsoluteTimeRange` |
**Ontologies** | [AbsoluteValuePropertyExpression](docs/v2/Ontologies/models/AbsoluteValuePropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import AbsoluteValuePropertyExpression` |
**Ontologies** | [ActionParameterArrayType](docs/v2/Ontologies/models/ActionParameterArrayType.md) | `from foundry_sdk.v2.ontologies.models import ActionParameterArrayType` |
**Ontologies** | [ActionParameterType](docs/v2/Ontologies/models/ActionParameterType.md) | `from foundry_sdk.v2.ontologies.models import ActionParameterType` |
**Ontologies** | [ActionParameterV2](docs/v2/Ontologies/models/ActionParameterV2.md) | `from foundry_sdk.v2.ontologies.models import ActionParameterV2` |
**Ontologies** | [ActionResults](docs/v2/Ontologies/models/ActionResults.md) | `from foundry_sdk.v2.ontologies.models import ActionResults` |
**Ontologies** | [ActionRid](docs/v2/Ontologies/models/ActionRid.md) | `from foundry_sdk.v2.ontologies.models import ActionRid` |
**Ontologies** | [ActionTypeApiName](docs/v2/Ontologies/models/ActionTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import ActionTypeApiName` |
**Ontologies** | [ActionTypeRid](docs/v2/Ontologies/models/ActionTypeRid.md) | `from foundry_sdk.v2.ontologies.models import ActionTypeRid` |
**Ontologies** | [ActionTypeV2](docs/v2/Ontologies/models/ActionTypeV2.md) | `from foundry_sdk.v2.ontologies.models import ActionTypeV2` |
**Ontologies** | [ActivePropertyTypeStatus](docs/v2/Ontologies/models/ActivePropertyTypeStatus.md) | `from foundry_sdk.v2.ontologies.models import ActivePropertyTypeStatus` |
**Ontologies** | [AddLink](docs/v2/Ontologies/models/AddLink.md) | `from foundry_sdk.v2.ontologies.models import AddLink` |
**Ontologies** | [AddLinkEdit](docs/v2/Ontologies/models/AddLinkEdit.md) | `from foundry_sdk.v2.ontologies.models import AddLinkEdit` |
**Ontologies** | [AddObject](docs/v2/Ontologies/models/AddObject.md) | `from foundry_sdk.v2.ontologies.models import AddObject` |
**Ontologies** | [AddObjectEdit](docs/v2/Ontologies/models/AddObjectEdit.md) | `from foundry_sdk.v2.ontologies.models import AddObjectEdit` |
**Ontologies** | [AddPropertyExpression](docs/v2/Ontologies/models/AddPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import AddPropertyExpression` |
**Ontologies** | [AggregateObjectsResponseItemV2](docs/v2/Ontologies/models/AggregateObjectsResponseItemV2.md) | `from foundry_sdk.v2.ontologies.models import AggregateObjectsResponseItemV2` |
**Ontologies** | [AggregateObjectsResponseV2](docs/v2/Ontologies/models/AggregateObjectsResponseV2.md) | `from foundry_sdk.v2.ontologies.models import AggregateObjectsResponseV2` |
**Ontologies** | [AggregateTimeSeries](docs/v2/Ontologies/models/AggregateTimeSeries.md) | `from foundry_sdk.v2.ontologies.models import AggregateTimeSeries` |
**Ontologies** | [AggregationAccuracy](docs/v2/Ontologies/models/AggregationAccuracy.md) | `from foundry_sdk.v2.ontologies.models import AggregationAccuracy` |
**Ontologies** | [AggregationAccuracyRequest](docs/v2/Ontologies/models/AggregationAccuracyRequest.md) | `from foundry_sdk.v2.ontologies.models import AggregationAccuracyRequest` |
**Ontologies** | [AggregationDurationGroupingV2](docs/v2/Ontologies/models/AggregationDurationGroupingV2.md) | `from foundry_sdk.v2.ontologies.models import AggregationDurationGroupingV2` |
**Ontologies** | [AggregationExactGroupingV2](docs/v2/Ontologies/models/AggregationExactGroupingV2.md) | `from foundry_sdk.v2.ontologies.models import AggregationExactGroupingV2` |
**Ontologies** | [AggregationFixedWidthGroupingV2](docs/v2/Ontologies/models/AggregationFixedWidthGroupingV2.md) | `from foundry_sdk.v2.ontologies.models import AggregationFixedWidthGroupingV2` |
**Ontologies** | [AggregationGroupByV2](docs/v2/Ontologies/models/AggregationGroupByV2.md) | `from foundry_sdk.v2.ontologies.models import AggregationGroupByV2` |
**Ontologies** | [AggregationGroupKeyV2](docs/v2/Ontologies/models/AggregationGroupKeyV2.md) | `from foundry_sdk.v2.ontologies.models import AggregationGroupKeyV2` |
**Ontologies** | [AggregationGroupValueV2](docs/v2/Ontologies/models/AggregationGroupValueV2.md) | `from foundry_sdk.v2.ontologies.models import AggregationGroupValueV2` |
**Ontologies** | [AggregationMetricName](docs/v2/Ontologies/models/AggregationMetricName.md) | `from foundry_sdk.v2.ontologies.models import AggregationMetricName` |
**Ontologies** | [AggregationMetricResultV2](docs/v2/Ontologies/models/AggregationMetricResultV2.md) | `from foundry_sdk.v2.ontologies.models import AggregationMetricResultV2` |
**Ontologies** | [AggregationRangesGroupingV2](docs/v2/Ontologies/models/AggregationRangesGroupingV2.md) | `from foundry_sdk.v2.ontologies.models import AggregationRangesGroupingV2` |
**Ontologies** | [AggregationRangeV2](docs/v2/Ontologies/models/AggregationRangeV2.md) | `from foundry_sdk.v2.ontologies.models import AggregationRangeV2` |
**Ontologies** | [AggregationV2](docs/v2/Ontologies/models/AggregationV2.md) | `from foundry_sdk.v2.ontologies.models import AggregationV2` |
**Ontologies** | [AndQueryV2](docs/v2/Ontologies/models/AndQueryV2.md) | `from foundry_sdk.v2.ontologies.models import AndQueryV2` |
**Ontologies** | [ApplyActionMode](docs/v2/Ontologies/models/ApplyActionMode.md) | `from foundry_sdk.v2.ontologies.models import ApplyActionMode` |
**Ontologies** | [ApplyActionRequestOptions](docs/v2/Ontologies/models/ApplyActionRequestOptions.md) | `from foundry_sdk.v2.ontologies.models import ApplyActionRequestOptions` |
**Ontologies** | [ApproximateDistinctAggregationV2](docs/v2/Ontologies/models/ApproximateDistinctAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import ApproximateDistinctAggregationV2` |
**Ontologies** | [ApproximatePercentileAggregationV2](docs/v2/Ontologies/models/ApproximatePercentileAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import ApproximatePercentileAggregationV2` |
**Ontologies** | [ArrayConstraint](docs/v2/Ontologies/models/ArrayConstraint.md) | `from foundry_sdk.v2.ontologies.models import ArrayConstraint` |
**Ontologies** | [ArrayEntryEvaluatedConstraint](docs/v2/Ontologies/models/ArrayEntryEvaluatedConstraint.md) | `from foundry_sdk.v2.ontologies.models import ArrayEntryEvaluatedConstraint` |
**Ontologies** | [ArrayEvaluatedConstraint](docs/v2/Ontologies/models/ArrayEvaluatedConstraint.md) | `from foundry_sdk.v2.ontologies.models import ArrayEvaluatedConstraint` |
**Ontologies** | [ArraySizeConstraint](docs/v2/Ontologies/models/ArraySizeConstraint.md) | `from foundry_sdk.v2.ontologies.models import ArraySizeConstraint` |
**Ontologies** | [ArtifactRepositoryRid](docs/v2/Ontologies/models/ArtifactRepositoryRid.md) | `from foundry_sdk.v2.ontologies.models import ArtifactRepositoryRid` |
**Ontologies** | [AttachmentMetadataResponse](docs/v2/Ontologies/models/AttachmentMetadataResponse.md) | `from foundry_sdk.v2.ontologies.models import AttachmentMetadataResponse` |
**Ontologies** | [AttachmentRid](docs/v2/Ontologies/models/AttachmentRid.md) | `from foundry_sdk.v2.ontologies.models import AttachmentRid` |
**Ontologies** | [AttachmentV2](docs/v2/Ontologies/models/AttachmentV2.md) | `from foundry_sdk.v2.ontologies.models import AttachmentV2` |
**Ontologies** | [AvgAggregationV2](docs/v2/Ontologies/models/AvgAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import AvgAggregationV2` |
**Ontologies** | [BatchActionObjectEdit](docs/v2/Ontologies/models/BatchActionObjectEdit.md) | `from foundry_sdk.v2.ontologies.models import BatchActionObjectEdit` |
**Ontologies** | [BatchActionObjectEdits](docs/v2/Ontologies/models/BatchActionObjectEdits.md) | `from foundry_sdk.v2.ontologies.models import BatchActionObjectEdits` |
**Ontologies** | [BatchActionResults](docs/v2/Ontologies/models/BatchActionResults.md) | `from foundry_sdk.v2.ontologies.models import BatchActionResults` |
**Ontologies** | [BatchApplyActionRequestItem](docs/v2/Ontologies/models/BatchApplyActionRequestItem.md) | `from foundry_sdk.v2.ontologies.models import BatchApplyActionRequestItem` |
**Ontologies** | [BatchApplyActionRequestOptions](docs/v2/Ontologies/models/BatchApplyActionRequestOptions.md) | `from foundry_sdk.v2.ontologies.models import BatchApplyActionRequestOptions` |
**Ontologies** | [BatchApplyActionResponseV2](docs/v2/Ontologies/models/BatchApplyActionResponseV2.md) | `from foundry_sdk.v2.ontologies.models import BatchApplyActionResponseV2` |
**Ontologies** | [BatchReturnEditsMode](docs/v2/Ontologies/models/BatchReturnEditsMode.md) | `from foundry_sdk.v2.ontologies.models import BatchReturnEditsMode` |
**Ontologies** | [BlueprintIcon](docs/v2/Ontologies/models/BlueprintIcon.md) | `from foundry_sdk.v2.ontologies.models import BlueprintIcon` |
**Ontologies** | [BoundingBoxValue](docs/v2/Ontologies/models/BoundingBoxValue.md) | `from foundry_sdk.v2.ontologies.models import BoundingBoxValue` |
**Ontologies** | [CenterPoint](docs/v2/Ontologies/models/CenterPoint.md) | `from foundry_sdk.v2.ontologies.models import CenterPoint` |
**Ontologies** | [CenterPointTypes](docs/v2/Ontologies/models/CenterPointTypes.md) | `from foundry_sdk.v2.ontologies.models import CenterPointTypes` |
**Ontologies** | [ContainsAllTermsInOrderPrefixLastTerm](docs/v2/Ontologies/models/ContainsAllTermsInOrderPrefixLastTerm.md) | `from foundry_sdk.v2.ontologies.models import ContainsAllTermsInOrderPrefixLastTerm` |
**Ontologies** | [ContainsAllTermsInOrderQuery](docs/v2/Ontologies/models/ContainsAllTermsInOrderQuery.md) | `from foundry_sdk.v2.ontologies.models import ContainsAllTermsInOrderQuery` |
**Ontologies** | [ContainsAllTermsQuery](docs/v2/Ontologies/models/ContainsAllTermsQuery.md) | `from foundry_sdk.v2.ontologies.models import ContainsAllTermsQuery` |
**Ontologies** | [ContainsAnyTermQuery](docs/v2/Ontologies/models/ContainsAnyTermQuery.md) | `from foundry_sdk.v2.ontologies.models import ContainsAnyTermQuery` |
**Ontologies** | [ContainsQueryV2](docs/v2/Ontologies/models/ContainsQueryV2.md) | `from foundry_sdk.v2.ontologies.models import ContainsQueryV2` |
**Ontologies** | [CountAggregationV2](docs/v2/Ontologies/models/CountAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import CountAggregationV2` |
**Ontologies** | [CountObjectsResponseV2](docs/v2/Ontologies/models/CountObjectsResponseV2.md) | `from foundry_sdk.v2.ontologies.models import CountObjectsResponseV2` |
**Ontologies** | [CreateInterfaceObjectRule](docs/v2/Ontologies/models/CreateInterfaceObjectRule.md) | `from foundry_sdk.v2.ontologies.models import CreateInterfaceObjectRule` |
**Ontologies** | [CreateLinkRule](docs/v2/Ontologies/models/CreateLinkRule.md) | `from foundry_sdk.v2.ontologies.models import CreateLinkRule` |
**Ontologies** | [CreateObjectRule](docs/v2/Ontologies/models/CreateObjectRule.md) | `from foundry_sdk.v2.ontologies.models import CreateObjectRule` |
**Ontologies** | [CreateTemporaryObjectSetResponseV2](docs/v2/Ontologies/models/CreateTemporaryObjectSetResponseV2.md) | `from foundry_sdk.v2.ontologies.models import CreateTemporaryObjectSetResponseV2` |
**Ontologies** | [DataValue](docs/v2/Ontologies/models/DataValue.md) | `from foundry_sdk.v2.ontologies.models import DataValue` |
**Ontologies** | [DecryptionResult](docs/v2/Ontologies/models/DecryptionResult.md) | `from foundry_sdk.v2.ontologies.models import DecryptionResult` |
**Ontologies** | [DeleteInterfaceObjectRule](docs/v2/Ontologies/models/DeleteInterfaceObjectRule.md) | `from foundry_sdk.v2.ontologies.models import DeleteInterfaceObjectRule` |
**Ontologies** | [DeleteLink](docs/v2/Ontologies/models/DeleteLink.md) | `from foundry_sdk.v2.ontologies.models import DeleteLink` |
**Ontologies** | [DeleteLinkEdit](docs/v2/Ontologies/models/DeleteLinkEdit.md) | `from foundry_sdk.v2.ontologies.models import DeleteLinkEdit` |
**Ontologies** | [DeleteLinkRule](docs/v2/Ontologies/models/DeleteLinkRule.md) | `from foundry_sdk.v2.ontologies.models import DeleteLinkRule` |
**Ontologies** | [DeleteObject](docs/v2/Ontologies/models/DeleteObject.md) | `from foundry_sdk.v2.ontologies.models import DeleteObject` |
**Ontologies** | [DeleteObjectEdit](docs/v2/Ontologies/models/DeleteObjectEdit.md) | `from foundry_sdk.v2.ontologies.models import DeleteObjectEdit` |
**Ontologies** | [DeleteObjectRule](docs/v2/Ontologies/models/DeleteObjectRule.md) | `from foundry_sdk.v2.ontologies.models import DeleteObjectRule` |
**Ontologies** | [DeprecatedPropertyTypeStatus](docs/v2/Ontologies/models/DeprecatedPropertyTypeStatus.md) | `from foundry_sdk.v2.ontologies.models import DeprecatedPropertyTypeStatus` |
**Ontologies** | [DerivedPropertyApiName](docs/v2/Ontologies/models/DerivedPropertyApiName.md) | `from foundry_sdk.v2.ontologies.models import DerivedPropertyApiName` |
**Ontologies** | [DerivedPropertyDefinition](docs/v2/Ontologies/models/DerivedPropertyDefinition.md) | `from foundry_sdk.v2.ontologies.models import DerivedPropertyDefinition` |
**Ontologies** | [DividePropertyExpression](docs/v2/Ontologies/models/DividePropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import DividePropertyExpression` |
**Ontologies** | [DoesNotIntersectBoundingBoxQuery](docs/v2/Ontologies/models/DoesNotIntersectBoundingBoxQuery.md) | `from foundry_sdk.v2.ontologies.models import DoesNotIntersectBoundingBoxQuery` |
**Ontologies** | [DoesNotIntersectPolygonQuery](docs/v2/Ontologies/models/DoesNotIntersectPolygonQuery.md) | `from foundry_sdk.v2.ontologies.models import DoesNotIntersectPolygonQuery` |
**Ontologies** | [DoubleVector](docs/v2/Ontologies/models/DoubleVector.md) | `from foundry_sdk.v2.ontologies.models import DoubleVector` |
**Ontologies** | [EntrySetType](docs/v2/Ontologies/models/EntrySetType.md) | `from foundry_sdk.v2.ontologies.models import EntrySetType` |
**Ontologies** | [EnumConstraint](docs/v2/Ontologies/models/EnumConstraint.md) | `from foundry_sdk.v2.ontologies.models import EnumConstraint` |
**Ontologies** | [EqualsQueryV2](docs/v2/Ontologies/models/EqualsQueryV2.md) | `from foundry_sdk.v2.ontologies.models import EqualsQueryV2` |
**Ontologies** | [ExactDistinctAggregationV2](docs/v2/Ontologies/models/ExactDistinctAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import ExactDistinctAggregationV2` |
**Ontologies** | [ExamplePropertyTypeStatus](docs/v2/Ontologies/models/ExamplePropertyTypeStatus.md) | `from foundry_sdk.v2.ontologies.models import ExamplePropertyTypeStatus` |
**Ontologies** | [ExecuteQueryResponse](docs/v2/Ontologies/models/ExecuteQueryResponse.md) | `from foundry_sdk.v2.ontologies.models import ExecuteQueryResponse` |
**Ontologies** | [ExperimentalPropertyTypeStatus](docs/v2/Ontologies/models/ExperimentalPropertyTypeStatus.md) | `from foundry_sdk.v2.ontologies.models import ExperimentalPropertyTypeStatus` |
**Ontologies** | [ExtractDatePart](docs/v2/Ontologies/models/ExtractDatePart.md) | `from foundry_sdk.v2.ontologies.models import ExtractDatePart` |
**Ontologies** | [ExtractPropertyExpression](docs/v2/Ontologies/models/ExtractPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import ExtractPropertyExpression` |
**Ontologies** | [FilterValue](docs/v2/Ontologies/models/FilterValue.md) | `from foundry_sdk.v2.ontologies.models import FilterValue` |
**Ontologies** | [FunctionRid](docs/v2/Ontologies/models/FunctionRid.md) | `from foundry_sdk.v2.ontologies.models import FunctionRid` |
**Ontologies** | [FunctionVersion](docs/v2/Ontologies/models/FunctionVersion.md) | `from foundry_sdk.v2.ontologies.models import FunctionVersion` |
**Ontologies** | [FuzzyV2](docs/v2/Ontologies/models/FuzzyV2.md) | `from foundry_sdk.v2.ontologies.models import FuzzyV2` |
**Ontologies** | [GetSelectedPropertyOperation](docs/v2/Ontologies/models/GetSelectedPropertyOperation.md) | `from foundry_sdk.v2.ontologies.models import GetSelectedPropertyOperation` |
**Ontologies** | [GreatestPropertyExpression](docs/v2/Ontologies/models/GreatestPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import GreatestPropertyExpression` |
**Ontologies** | [GroupMemberConstraint](docs/v2/Ontologies/models/GroupMemberConstraint.md) | `from foundry_sdk.v2.ontologies.models import GroupMemberConstraint` |
**Ontologies** | [GteQueryV2](docs/v2/Ontologies/models/GteQueryV2.md) | `from foundry_sdk.v2.ontologies.models import GteQueryV2` |
**Ontologies** | [GtQueryV2](docs/v2/Ontologies/models/GtQueryV2.md) | `from foundry_sdk.v2.ontologies.models import GtQueryV2` |
**Ontologies** | [Icon](docs/v2/Ontologies/models/Icon.md) | `from foundry_sdk.v2.ontologies.models import Icon` |
**Ontologies** | [InQuery](docs/v2/Ontologies/models/InQuery.md) | `from foundry_sdk.v2.ontologies.models import InQuery` |
**Ontologies** | [InterfaceLinkType](docs/v2/Ontologies/models/InterfaceLinkType.md) | `from foundry_sdk.v2.ontologies.models import InterfaceLinkType` |
**Ontologies** | [InterfaceLinkTypeApiName](docs/v2/Ontologies/models/InterfaceLinkTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import InterfaceLinkTypeApiName` |
**Ontologies** | [InterfaceLinkTypeCardinality](docs/v2/Ontologies/models/InterfaceLinkTypeCardinality.md) | `from foundry_sdk.v2.ontologies.models import InterfaceLinkTypeCardinality` |
**Ontologies** | [InterfaceLinkTypeLinkedEntityApiName](docs/v2/Ontologies/models/InterfaceLinkTypeLinkedEntityApiName.md) | `from foundry_sdk.v2.ontologies.models import InterfaceLinkTypeLinkedEntityApiName` |
**Ontologies** | [InterfaceLinkTypeRid](docs/v2/Ontologies/models/InterfaceLinkTypeRid.md) | `from foundry_sdk.v2.ontologies.models import InterfaceLinkTypeRid` |
**Ontologies** | [InterfaceSharedPropertyType](docs/v2/Ontologies/models/InterfaceSharedPropertyType.md) | `from foundry_sdk.v2.ontologies.models import InterfaceSharedPropertyType` |
**Ontologies** | [InterfaceToObjectTypeMapping](docs/v2/Ontologies/models/InterfaceToObjectTypeMapping.md) | `from foundry_sdk.v2.ontologies.models import InterfaceToObjectTypeMapping` |
**Ontologies** | [InterfaceToObjectTypeMappings](docs/v2/Ontologies/models/InterfaceToObjectTypeMappings.md) | `from foundry_sdk.v2.ontologies.models import InterfaceToObjectTypeMappings` |
**Ontologies** | [InterfaceType](docs/v2/Ontologies/models/InterfaceType.md) | `from foundry_sdk.v2.ontologies.models import InterfaceType` |
**Ontologies** | [InterfaceTypeApiName](docs/v2/Ontologies/models/InterfaceTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import InterfaceTypeApiName` |
**Ontologies** | [InterfaceTypeRid](docs/v2/Ontologies/models/InterfaceTypeRid.md) | `from foundry_sdk.v2.ontologies.models import InterfaceTypeRid` |
**Ontologies** | [IntersectsBoundingBoxQuery](docs/v2/Ontologies/models/IntersectsBoundingBoxQuery.md) | `from foundry_sdk.v2.ontologies.models import IntersectsBoundingBoxQuery` |
**Ontologies** | [IntersectsPolygonQuery](docs/v2/Ontologies/models/IntersectsPolygonQuery.md) | `from foundry_sdk.v2.ontologies.models import IntersectsPolygonQuery` |
**Ontologies** | [IsNullQueryV2](docs/v2/Ontologies/models/IsNullQueryV2.md) | `from foundry_sdk.v2.ontologies.models import IsNullQueryV2` |
**Ontologies** | [LeastPropertyExpression](docs/v2/Ontologies/models/LeastPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import LeastPropertyExpression` |
**Ontologies** | [LengthConstraint](docs/v2/Ontologies/models/LengthConstraint.md) | `from foundry_sdk.v2.ontologies.models import LengthConstraint` |
**Ontologies** | [LinkedInterfaceTypeApiName](docs/v2/Ontologies/models/LinkedInterfaceTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import LinkedInterfaceTypeApiName` |
**Ontologies** | [LinkedObjectTypeApiName](docs/v2/Ontologies/models/LinkedObjectTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import LinkedObjectTypeApiName` |
**Ontologies** | [LinkSideObject](docs/v2/Ontologies/models/LinkSideObject.md) | `from foundry_sdk.v2.ontologies.models import LinkSideObject` |
**Ontologies** | [LinkTypeApiName](docs/v2/Ontologies/models/LinkTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import LinkTypeApiName` |
**Ontologies** | [LinkTypeId](docs/v2/Ontologies/models/LinkTypeId.md) | `from foundry_sdk.v2.ontologies.models import LinkTypeId` |
**Ontologies** | [LinkTypeRid](docs/v2/Ontologies/models/LinkTypeRid.md) | `from foundry_sdk.v2.ontologies.models import LinkTypeRid` |
**Ontologies** | [LinkTypeSideCardinality](docs/v2/Ontologies/models/LinkTypeSideCardinality.md) | `from foundry_sdk.v2.ontologies.models import LinkTypeSideCardinality` |
**Ontologies** | [LinkTypeSideV2](docs/v2/Ontologies/models/LinkTypeSideV2.md) | `from foundry_sdk.v2.ontologies.models import LinkTypeSideV2` |
**Ontologies** | [ListActionTypesResponseV2](docs/v2/Ontologies/models/ListActionTypesResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListActionTypesResponseV2` |
**Ontologies** | [ListAttachmentsResponseV2](docs/v2/Ontologies/models/ListAttachmentsResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListAttachmentsResponseV2` |
**Ontologies** | [ListInterfaceTypesResponse](docs/v2/Ontologies/models/ListInterfaceTypesResponse.md) | `from foundry_sdk.v2.ontologies.models import ListInterfaceTypesResponse` |
**Ontologies** | [ListLinkedObjectsResponseV2](docs/v2/Ontologies/models/ListLinkedObjectsResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListLinkedObjectsResponseV2` |
**Ontologies** | [ListObjectsResponseV2](docs/v2/Ontologies/models/ListObjectsResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListObjectsResponseV2` |
**Ontologies** | [ListObjectTypesV2Response](docs/v2/Ontologies/models/ListObjectTypesV2Response.md) | `from foundry_sdk.v2.ontologies.models import ListObjectTypesV2Response` |
**Ontologies** | [ListOntologiesV2Response](docs/v2/Ontologies/models/ListOntologiesV2Response.md) | `from foundry_sdk.v2.ontologies.models import ListOntologiesV2Response` |
**Ontologies** | [ListOntologyValueTypesResponse](docs/v2/Ontologies/models/ListOntologyValueTypesResponse.md) | `from foundry_sdk.v2.ontologies.models import ListOntologyValueTypesResponse` |
**Ontologies** | [ListOutgoingInterfaceLinkTypesResponse](docs/v2/Ontologies/models/ListOutgoingInterfaceLinkTypesResponse.md) | `from foundry_sdk.v2.ontologies.models import ListOutgoingInterfaceLinkTypesResponse` |
**Ontologies** | [ListOutgoingLinkTypesResponseV2](docs/v2/Ontologies/models/ListOutgoingLinkTypesResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListOutgoingLinkTypesResponseV2` |
**Ontologies** | [ListQueryTypesResponseV2](docs/v2/Ontologies/models/ListQueryTypesResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListQueryTypesResponseV2` |
**Ontologies** | [LoadObjectSetResponseV2](docs/v2/Ontologies/models/LoadObjectSetResponseV2.md) | `from foundry_sdk.v2.ontologies.models import LoadObjectSetResponseV2` |
**Ontologies** | [LoadObjectSetV2MultipleObjectTypesResponse](docs/v2/Ontologies/models/LoadObjectSetV2MultipleObjectTypesResponse.md) | `from foundry_sdk.v2.ontologies.models import LoadObjectSetV2MultipleObjectTypesResponse` |
**Ontologies** | [LoadObjectSetV2ObjectsOrInterfacesResponse](docs/v2/Ontologies/models/LoadObjectSetV2ObjectsOrInterfacesResponse.md) | `from foundry_sdk.v2.ontologies.models import LoadObjectSetV2ObjectsOrInterfacesResponse` |
**Ontologies** | [LogicRule](docs/v2/Ontologies/models/LogicRule.md) | `from foundry_sdk.v2.ontologies.models import LogicRule` |
**Ontologies** | [LteQueryV2](docs/v2/Ontologies/models/LteQueryV2.md) | `from foundry_sdk.v2.ontologies.models import LteQueryV2` |
**Ontologies** | [LtQueryV2](docs/v2/Ontologies/models/LtQueryV2.md) | `from foundry_sdk.v2.ontologies.models import LtQueryV2` |
**Ontologies** | [MaxAggregationV2](docs/v2/Ontologies/models/MaxAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import MaxAggregationV2` |
**Ontologies** | [MediaMetadata](docs/v2/Ontologies/models/MediaMetadata.md) | `from foundry_sdk.v2.ontologies.models import MediaMetadata` |
**Ontologies** | [MethodObjectSet](docs/v2/Ontologies/models/MethodObjectSet.md) | `from foundry_sdk.v2.ontologies.models import MethodObjectSet` |
**Ontologies** | [MinAggregationV2](docs/v2/Ontologies/models/MinAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import MinAggregationV2` |
**Ontologies** | [ModifyInterfaceObjectRule](docs/v2/Ontologies/models/ModifyInterfaceObjectRule.md) | `from foundry_sdk.v2.ontologies.models import ModifyInterfaceObjectRule` |
**Ontologies** | [ModifyObject](docs/v2/Ontologies/models/ModifyObject.md) | `from foundry_sdk.v2.ontologies.models import ModifyObject` |
**Ontologies** | [ModifyObjectEdit](docs/v2/Ontologies/models/ModifyObjectEdit.md) | `from foundry_sdk.v2.ontologies.models import ModifyObjectEdit` |
**Ontologies** | [ModifyObjectRule](docs/v2/Ontologies/models/ModifyObjectRule.md) | `from foundry_sdk.v2.ontologies.models import ModifyObjectRule` |
**Ontologies** | [MultiplyPropertyExpression](docs/v2/Ontologies/models/MultiplyPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import MultiplyPropertyExpression` |
**Ontologies** | [NearestNeighborsQuery](docs/v2/Ontologies/models/NearestNeighborsQuery.md) | `from foundry_sdk.v2.ontologies.models import NearestNeighborsQuery` |
**Ontologies** | [NearestNeighborsQueryText](docs/v2/Ontologies/models/NearestNeighborsQueryText.md) | `from foundry_sdk.v2.ontologies.models import NearestNeighborsQueryText` |
**Ontologies** | [NegatePropertyExpression](docs/v2/Ontologies/models/NegatePropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import NegatePropertyExpression` |
**Ontologies** | [NestedQueryAggregation](docs/v2/Ontologies/models/NestedQueryAggregation.md) | `from foundry_sdk.v2.ontologies.models import NestedQueryAggregation` |
**Ontologies** | [NotQueryV2](docs/v2/Ontologies/models/NotQueryV2.md) | `from foundry_sdk.v2.ontologies.models import NotQueryV2` |
**Ontologies** | [ObjectEdit](docs/v2/Ontologies/models/ObjectEdit.md) | `from foundry_sdk.v2.ontologies.models import ObjectEdit` |
**Ontologies** | [ObjectEdits](docs/v2/Ontologies/models/ObjectEdits.md) | `from foundry_sdk.v2.ontologies.models import ObjectEdits` |
**Ontologies** | [ObjectPropertyType](docs/v2/Ontologies/models/ObjectPropertyType.md) | `from foundry_sdk.v2.ontologies.models import ObjectPropertyType` |
**Ontologies** | [ObjectPropertyValueConstraint](docs/v2/Ontologies/models/ObjectPropertyValueConstraint.md) | `from foundry_sdk.v2.ontologies.models import ObjectPropertyValueConstraint` |
**Ontologies** | [ObjectQueryResultConstraint](docs/v2/Ontologies/models/ObjectQueryResultConstraint.md) | `from foundry_sdk.v2.ontologies.models import ObjectQueryResultConstraint` |
**Ontologies** | [ObjectRid](docs/v2/Ontologies/models/ObjectRid.md) | `from foundry_sdk.v2.ontologies.models import ObjectRid` |
**Ontologies** | [ObjectSet](docs/v2/Ontologies/models/ObjectSet.md) | `from foundry_sdk.v2.ontologies.models import ObjectSet` |
**Ontologies** | [ObjectSetAsBaseObjectTypesType](docs/v2/Ontologies/models/ObjectSetAsBaseObjectTypesType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetAsBaseObjectTypesType` |
**Ontologies** | [ObjectSetAsTypeType](docs/v2/Ontologies/models/ObjectSetAsTypeType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetAsTypeType` |
**Ontologies** | [ObjectSetBaseType](docs/v2/Ontologies/models/ObjectSetBaseType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetBaseType` |
**Ontologies** | [ObjectSetFilterType](docs/v2/Ontologies/models/ObjectSetFilterType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetFilterType` |
**Ontologies** | [ObjectSetInterfaceBaseType](docs/v2/Ontologies/models/ObjectSetInterfaceBaseType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetInterfaceBaseType` |
**Ontologies** | [ObjectSetInterfaceLinkSearchAroundType](docs/v2/Ontologies/models/ObjectSetInterfaceLinkSearchAroundType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetInterfaceLinkSearchAroundType` |
**Ontologies** | [ObjectSetIntersectionType](docs/v2/Ontologies/models/ObjectSetIntersectionType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetIntersectionType` |
**Ontologies** | [ObjectSetMethodInputType](docs/v2/Ontologies/models/ObjectSetMethodInputType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetMethodInputType` |
**Ontologies** | [ObjectSetNearestNeighborsType](docs/v2/Ontologies/models/ObjectSetNearestNeighborsType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetNearestNeighborsType` |
**Ontologies** | [ObjectSetReferenceType](docs/v2/Ontologies/models/ObjectSetReferenceType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetReferenceType` |
**Ontologies** | [ObjectSetRid](docs/v2/Ontologies/models/ObjectSetRid.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetRid` |
**Ontologies** | [ObjectSetSearchAroundType](docs/v2/Ontologies/models/ObjectSetSearchAroundType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetSearchAroundType` |
**Ontologies** | [ObjectSetStaticType](docs/v2/Ontologies/models/ObjectSetStaticType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetStaticType` |
**Ontologies** | [ObjectSetSubtractType](docs/v2/Ontologies/models/ObjectSetSubtractType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetSubtractType` |
**Ontologies** | [ObjectSetUnionType](docs/v2/Ontologies/models/ObjectSetUnionType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetUnionType` |
**Ontologies** | [ObjectSetWithPropertiesType](docs/v2/Ontologies/models/ObjectSetWithPropertiesType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetWithPropertiesType` |
**Ontologies** | [ObjectTypeApiName](docs/v2/Ontologies/models/ObjectTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeApiName` |
**Ontologies** | [ObjectTypeEdits](docs/v2/Ontologies/models/ObjectTypeEdits.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeEdits` |
**Ontologies** | [ObjectTypeFullMetadata](docs/v2/Ontologies/models/ObjectTypeFullMetadata.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeFullMetadata` |
**Ontologies** | [ObjectTypeId](docs/v2/Ontologies/models/ObjectTypeId.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeId` |
**Ontologies** | [ObjectTypeInterfaceImplementation](docs/v2/Ontologies/models/ObjectTypeInterfaceImplementation.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeInterfaceImplementation` |
**Ontologies** | [ObjectTypeRid](docs/v2/Ontologies/models/ObjectTypeRid.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeRid` |
**Ontologies** | [ObjectTypeV2](docs/v2/Ontologies/models/ObjectTypeV2.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeV2` |
**Ontologies** | [ObjectTypeVisibility](docs/v2/Ontologies/models/ObjectTypeVisibility.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeVisibility` |
**Ontologies** | [OneOfConstraint](docs/v2/Ontologies/models/OneOfConstraint.md) | `from foundry_sdk.v2.ontologies.models import OneOfConstraint` |
**Ontologies** | [OntologyApiName](docs/v2/Ontologies/models/OntologyApiName.md) | `from foundry_sdk.v2.ontologies.models import OntologyApiName` |
**Ontologies** | [OntologyArrayType](docs/v2/Ontologies/models/OntologyArrayType.md) | `from foundry_sdk.v2.ontologies.models import OntologyArrayType` |
**Ontologies** | [OntologyDataType](docs/v2/Ontologies/models/OntologyDataType.md) | `from foundry_sdk.v2.ontologies.models import OntologyDataType` |
**Ontologies** | [OntologyFullMetadata](docs/v2/Ontologies/models/OntologyFullMetadata.md) | `from foundry_sdk.v2.ontologies.models import OntologyFullMetadata` |
**Ontologies** | [OntologyIdentifier](docs/v2/Ontologies/models/OntologyIdentifier.md) | `from foundry_sdk.v2.ontologies.models import OntologyIdentifier` |
**Ontologies** | [OntologyInterfaceObjectSetType](docs/v2/Ontologies/models/OntologyInterfaceObjectSetType.md) | `from foundry_sdk.v2.ontologies.models import OntologyInterfaceObjectSetType` |
**Ontologies** | [OntologyInterfaceObjectType](docs/v2/Ontologies/models/OntologyInterfaceObjectType.md) | `from foundry_sdk.v2.ontologies.models import OntologyInterfaceObjectType` |
**Ontologies** | [OntologyMapType](docs/v2/Ontologies/models/OntologyMapType.md) | `from foundry_sdk.v2.ontologies.models import OntologyMapType` |
**Ontologies** | [OntologyObjectArrayType](docs/v2/Ontologies/models/OntologyObjectArrayType.md) | `from foundry_sdk.v2.ontologies.models import OntologyObjectArrayType` |
**Ontologies** | [OntologyObjectSetType](docs/v2/Ontologies/models/OntologyObjectSetType.md) | `from foundry_sdk.v2.ontologies.models import OntologyObjectSetType` |
**Ontologies** | [OntologyObjectType](docs/v2/Ontologies/models/OntologyObjectType.md) | `from foundry_sdk.v2.ontologies.models import OntologyObjectType` |
**Ontologies** | [OntologyObjectTypeReferenceType](docs/v2/Ontologies/models/OntologyObjectTypeReferenceType.md) | `from foundry_sdk.v2.ontologies.models import OntologyObjectTypeReferenceType` |
**Ontologies** | [OntologyObjectV2](docs/v2/Ontologies/models/OntologyObjectV2.md) | `from foundry_sdk.v2.ontologies.models import OntologyObjectV2` |
**Ontologies** | [OntologyRid](docs/v2/Ontologies/models/OntologyRid.md) | `from foundry_sdk.v2.ontologies.models import OntologyRid` |
**Ontologies** | [OntologySetType](docs/v2/Ontologies/models/OntologySetType.md) | `from foundry_sdk.v2.ontologies.models import OntologySetType` |
**Ontologies** | [OntologyStructField](docs/v2/Ontologies/models/OntologyStructField.md) | `from foundry_sdk.v2.ontologies.models import OntologyStructField` |
**Ontologies** | [OntologyStructType](docs/v2/Ontologies/models/OntologyStructType.md) | `from foundry_sdk.v2.ontologies.models import OntologyStructType` |
**Ontologies** | [OntologyTransactionRid](docs/v2/Ontologies/models/OntologyTransactionRid.md) | `from foundry_sdk.v2.ontologies.models import OntologyTransactionRid` |
**Ontologies** | [OntologyV2](docs/v2/Ontologies/models/OntologyV2.md) | `from foundry_sdk.v2.ontologies.models import OntologyV2` |
**Ontologies** | [OntologyValueType](docs/v2/Ontologies/models/OntologyValueType.md) | `from foundry_sdk.v2.ontologies.models import OntologyValueType` |
**Ontologies** | [OrderBy](docs/v2/Ontologies/models/OrderBy.md) | `from foundry_sdk.v2.ontologies.models import OrderBy` |
**Ontologies** | [OrderByDirection](docs/v2/Ontologies/models/OrderByDirection.md) | `from foundry_sdk.v2.ontologies.models import OrderByDirection` |
**Ontologies** | [OrQueryV2](docs/v2/Ontologies/models/OrQueryV2.md) | `from foundry_sdk.v2.ontologies.models import OrQueryV2` |
**Ontologies** | [ParameterEvaluatedConstraint](docs/v2/Ontologies/models/ParameterEvaluatedConstraint.md) | `from foundry_sdk.v2.ontologies.models import ParameterEvaluatedConstraint` |
**Ontologies** | [ParameterEvaluationResult](docs/v2/Ontologies/models/ParameterEvaluationResult.md) | `from foundry_sdk.v2.ontologies.models import ParameterEvaluationResult` |
**Ontologies** | [ParameterId](docs/v2/Ontologies/models/ParameterId.md) | `from foundry_sdk.v2.ontologies.models import ParameterId` |
**Ontologies** | [ParameterOption](docs/v2/Ontologies/models/ParameterOption.md) | `from foundry_sdk.v2.ontologies.models import ParameterOption` |
**Ontologies** | [Plaintext](docs/v2/Ontologies/models/Plaintext.md) | `from foundry_sdk.v2.ontologies.models import Plaintext` |
**Ontologies** | [PolygonValue](docs/v2/Ontologies/models/PolygonValue.md) | `from foundry_sdk.v2.ontologies.models import PolygonValue` |
**Ontologies** | [PostTransactionEditsResponse](docs/v2/Ontologies/models/PostTransactionEditsResponse.md) | `from foundry_sdk.v2.ontologies.models import PostTransactionEditsResponse` |
**Ontologies** | [PreciseDuration](docs/v2/Ontologies/models/PreciseDuration.md) | `from foundry_sdk.v2.ontologies.models import PreciseDuration` |
**Ontologies** | [PreciseTimeUnit](docs/v2/Ontologies/models/PreciseTimeUnit.md) | `from foundry_sdk.v2.ontologies.models import PreciseTimeUnit` |
**Ontologies** | [PrimaryKeyValue](docs/v2/Ontologies/models/PrimaryKeyValue.md) | `from foundry_sdk.v2.ontologies.models import PrimaryKeyValue` |
**Ontologies** | [PropertyApiName](docs/v2/Ontologies/models/PropertyApiName.md) | `from foundry_sdk.v2.ontologies.models import PropertyApiName` |
**Ontologies** | [PropertyApiNameSelector](docs/v2/Ontologies/models/PropertyApiNameSelector.md) | `from foundry_sdk.v2.ontologies.models import PropertyApiNameSelector` |
**Ontologies** | [PropertyFilter](docs/v2/Ontologies/models/PropertyFilter.md) | `from foundry_sdk.v2.ontologies.models import PropertyFilter` |
**Ontologies** | [PropertyId](docs/v2/Ontologies/models/PropertyId.md) | `from foundry_sdk.v2.ontologies.models import PropertyId` |
**Ontologies** | [PropertyIdentifier](docs/v2/Ontologies/models/PropertyIdentifier.md) | `from foundry_sdk.v2.ontologies.models import PropertyIdentifier` |
**Ontologies** | [PropertyTypeRid](docs/v2/Ontologies/models/PropertyTypeRid.md) | `from foundry_sdk.v2.ontologies.models import PropertyTypeRid` |
**Ontologies** | [PropertyTypeStatus](docs/v2/Ontologies/models/PropertyTypeStatus.md) | `from foundry_sdk.v2.ontologies.models import PropertyTypeStatus` |
**Ontologies** | [PropertyTypeVisibility](docs/v2/Ontologies/models/PropertyTypeVisibility.md) | `from foundry_sdk.v2.ontologies.models import PropertyTypeVisibility` |
**Ontologies** | [PropertyV2](docs/v2/Ontologies/models/PropertyV2.md) | `from foundry_sdk.v2.ontologies.models import PropertyV2` |
**Ontologies** | [PropertyValue](docs/v2/Ontologies/models/PropertyValue.md) | `from foundry_sdk.v2.ontologies.models import PropertyValue` |
**Ontologies** | [PropertyValueEscapedString](docs/v2/Ontologies/models/PropertyValueEscapedString.md) | `from foundry_sdk.v2.ontologies.models import PropertyValueEscapedString` |
**Ontologies** | [QueryAggregation](docs/v2/Ontologies/models/QueryAggregation.md) | `from foundry_sdk.v2.ontologies.models import QueryAggregation` |
**Ontologies** | [QueryAggregationKeyType](docs/v2/Ontologies/models/QueryAggregationKeyType.md) | `from foundry_sdk.v2.ontologies.models import QueryAggregationKeyType` |
**Ontologies** | [QueryAggregationRangeSubType](docs/v2/Ontologies/models/QueryAggregationRangeSubType.md) | `from foundry_sdk.v2.ontologies.models import QueryAggregationRangeSubType` |
**Ontologies** | [QueryAggregationRangeType](docs/v2/Ontologies/models/QueryAggregationRangeType.md) | `from foundry_sdk.v2.ontologies.models import QueryAggregationRangeType` |
**Ontologies** | [QueryAggregationValueType](docs/v2/Ontologies/models/QueryAggregationValueType.md) | `from foundry_sdk.v2.ontologies.models import QueryAggregationValueType` |
**Ontologies** | [QueryApiName](docs/v2/Ontologies/models/QueryApiName.md) | `from foundry_sdk.v2.ontologies.models import QueryApiName` |
**Ontologies** | [QueryArrayType](docs/v2/Ontologies/models/QueryArrayType.md) | `from foundry_sdk.v2.ontologies.models import QueryArrayType` |
**Ontologies** | [QueryDataType](docs/v2/Ontologies/models/QueryDataType.md) | `from foundry_sdk.v2.ontologies.models import QueryDataType` |
**Ontologies** | [QueryParameterV2](docs/v2/Ontologies/models/QueryParameterV2.md) | `from foundry_sdk.v2.ontologies.models import QueryParameterV2` |
**Ontologies** | [QueryRuntimeErrorParameter](docs/v2/Ontologies/models/QueryRuntimeErrorParameter.md) | `from foundry_sdk.v2.ontologies.models import QueryRuntimeErrorParameter` |
**Ontologies** | [QuerySetType](docs/v2/Ontologies/models/QuerySetType.md) | `from foundry_sdk.v2.ontologies.models import QuerySetType` |
**Ontologies** | [QueryStructField](docs/v2/Ontologies/models/QueryStructField.md) | `from foundry_sdk.v2.ontologies.models import QueryStructField` |
**Ontologies** | [QueryStructType](docs/v2/Ontologies/models/QueryStructType.md) | `from foundry_sdk.v2.ontologies.models import QueryStructType` |
**Ontologies** | [QueryThreeDimensionalAggregation](docs/v2/Ontologies/models/QueryThreeDimensionalAggregation.md) | `from foundry_sdk.v2.ontologies.models import QueryThreeDimensionalAggregation` |
**Ontologies** | [QueryTwoDimensionalAggregation](docs/v2/Ontologies/models/QueryTwoDimensionalAggregation.md) | `from foundry_sdk.v2.ontologies.models import QueryTwoDimensionalAggregation` |
**Ontologies** | [QueryTypeV2](docs/v2/Ontologies/models/QueryTypeV2.md) | `from foundry_sdk.v2.ontologies.models import QueryTypeV2` |
**Ontologies** | [QueryUnionType](docs/v2/Ontologies/models/QueryUnionType.md) | `from foundry_sdk.v2.ontologies.models import QueryUnionType` |
**Ontologies** | [RangeConstraint](docs/v2/Ontologies/models/RangeConstraint.md) | `from foundry_sdk.v2.ontologies.models import RangeConstraint` |
**Ontologies** | [RangesConstraint](docs/v2/Ontologies/models/RangesConstraint.md) | `from foundry_sdk.v2.ontologies.models import RangesConstraint` |
**Ontologies** | [RegexConstraint](docs/v2/Ontologies/models/RegexConstraint.md) | `from foundry_sdk.v2.ontologies.models import RegexConstraint` |
**Ontologies** | [RelativeTime](docs/v2/Ontologies/models/RelativeTime.md) | `from foundry_sdk.v2.ontologies.models import RelativeTime` |
**Ontologies** | [RelativeTimeRange](docs/v2/Ontologies/models/RelativeTimeRange.md) | `from foundry_sdk.v2.ontologies.models import RelativeTimeRange` |
**Ontologies** | [RelativeTimeRelation](docs/v2/Ontologies/models/RelativeTimeRelation.md) | `from foundry_sdk.v2.ontologies.models import RelativeTimeRelation` |
**Ontologies** | [RelativeTimeSeriesTimeUnit](docs/v2/Ontologies/models/RelativeTimeSeriesTimeUnit.md) | `from foundry_sdk.v2.ontologies.models import RelativeTimeSeriesTimeUnit` |
**Ontologies** | [ReturnEditsMode](docs/v2/Ontologies/models/ReturnEditsMode.md) | `from foundry_sdk.v2.ontologies.models import ReturnEditsMode` |
**Ontologies** | [RidConstraint](docs/v2/Ontologies/models/RidConstraint.md) | `from foundry_sdk.v2.ontologies.models import RidConstraint` |
**Ontologies** | [RollingAggregateWindowPoints](docs/v2/Ontologies/models/RollingAggregateWindowPoints.md) | `from foundry_sdk.v2.ontologies.models import RollingAggregateWindowPoints` |
**Ontologies** | [SdkPackageName](docs/v2/Ontologies/models/SdkPackageName.md) | `from foundry_sdk.v2.ontologies.models import SdkPackageName` |
**Ontologies** | [SdkPackageRid](docs/v2/Ontologies/models/SdkPackageRid.md) | `from foundry_sdk.v2.ontologies.models import SdkPackageRid` |
**Ontologies** | [SdkVersion](docs/v2/Ontologies/models/SdkVersion.md) | `from foundry_sdk.v2.ontologies.models import SdkVersion` |
**Ontologies** | [SearchJsonQueryV2](docs/v2/Ontologies/models/SearchJsonQueryV2.md) | `from foundry_sdk.v2.ontologies.models import SearchJsonQueryV2` |
**Ontologies** | [SearchObjectsResponseV2](docs/v2/Ontologies/models/SearchObjectsResponseV2.md) | `from foundry_sdk.v2.ontologies.models import SearchObjectsResponseV2` |
**Ontologies** | [SearchOrderByType](docs/v2/Ontologies/models/SearchOrderByType.md) | `from foundry_sdk.v2.ontologies.models import SearchOrderByType` |
**Ontologies** | [SearchOrderByV2](docs/v2/Ontologies/models/SearchOrderByV2.md) | `from foundry_sdk.v2.ontologies.models import SearchOrderByV2` |
**Ontologies** | [SearchOrderingV2](docs/v2/Ontologies/models/SearchOrderingV2.md) | `from foundry_sdk.v2.ontologies.models import SearchOrderingV2` |
**Ontologies** | [SelectedPropertyApiName](docs/v2/Ontologies/models/SelectedPropertyApiName.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyApiName` |
**Ontologies** | [SelectedPropertyApproximateDistinctAggregation](docs/v2/Ontologies/models/SelectedPropertyApproximateDistinctAggregation.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyApproximateDistinctAggregation` |
**Ontologies** | [SelectedPropertyApproximatePercentileAggregation](docs/v2/Ontologies/models/SelectedPropertyApproximatePercentileAggregation.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyApproximatePercentileAggregation` |
**Ontologies** | [SelectedPropertyAvgAggregation](docs/v2/Ontologies/models/SelectedPropertyAvgAggregation.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyAvgAggregation` |
**Ontologies** | [SelectedPropertyCollectListAggregation](docs/v2/Ontologies/models/SelectedPropertyCollectListAggregation.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyCollectListAggregation` |
**Ontologies** | [SelectedPropertyCollectSetAggregation](docs/v2/Ontologies/models/SelectedPropertyCollectSetAggregation.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyCollectSetAggregation` |
**Ontologies** | [SelectedPropertyCountAggregation](docs/v2/Ontologies/models/SelectedPropertyCountAggregation.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyCountAggregation` |
**Ontologies** | [SelectedPropertyExactDistinctAggregation](docs/v2/Ontologies/models/SelectedPropertyExactDistinctAggregation.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyExactDistinctAggregation` |
**Ontologies** | [SelectedPropertyExpression](docs/v2/Ontologies/models/SelectedPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyExpression` |
**Ontologies** | [SelectedPropertyMaxAggregation](docs/v2/Ontologies/models/SelectedPropertyMaxAggregation.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyMaxAggregation` |
**Ontologies** | [SelectedPropertyMinAggregation](docs/v2/Ontologies/models/SelectedPropertyMinAggregation.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyMinAggregation` |
**Ontologies** | [SelectedPropertyOperation](docs/v2/Ontologies/models/SelectedPropertyOperation.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertyOperation` |
**Ontologies** | [SelectedPropertySumAggregation](docs/v2/Ontologies/models/SelectedPropertySumAggregation.md) | `from foundry_sdk.v2.ontologies.models import SelectedPropertySumAggregation` |
**Ontologies** | [SharedPropertyType](docs/v2/Ontologies/models/SharedPropertyType.md) | `from foundry_sdk.v2.ontologies.models import SharedPropertyType` |
**Ontologies** | [SharedPropertyTypeApiName](docs/v2/Ontologies/models/SharedPropertyTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import SharedPropertyTypeApiName` |
**Ontologies** | [SharedPropertyTypeRid](docs/v2/Ontologies/models/SharedPropertyTypeRid.md) | `from foundry_sdk.v2.ontologies.models import SharedPropertyTypeRid` |
**Ontologies** | [StartsWithQuery](docs/v2/Ontologies/models/StartsWithQuery.md) | `from foundry_sdk.v2.ontologies.models import StartsWithQuery` |
**Ontologies** | [StreamingOutputFormat](docs/v2/Ontologies/models/StreamingOutputFormat.md) | `from foundry_sdk.v2.ontologies.models import StreamingOutputFormat` |
**Ontologies** | [StringLengthConstraint](docs/v2/Ontologies/models/StringLengthConstraint.md) | `from foundry_sdk.v2.ontologies.models import StringLengthConstraint` |
**Ontologies** | [StringRegexMatchConstraint](docs/v2/Ontologies/models/StringRegexMatchConstraint.md) | `from foundry_sdk.v2.ontologies.models import StringRegexMatchConstraint` |
**Ontologies** | [StructConstraint](docs/v2/Ontologies/models/StructConstraint.md) | `from foundry_sdk.v2.ontologies.models import StructConstraint` |
**Ontologies** | [StructEvaluatedConstraint](docs/v2/Ontologies/models/StructEvaluatedConstraint.md) | `from foundry_sdk.v2.ontologies.models import StructEvaluatedConstraint` |
**Ontologies** | [StructFieldApiName](docs/v2/Ontologies/models/StructFieldApiName.md) | `from foundry_sdk.v2.ontologies.models import StructFieldApiName` |
**Ontologies** | [StructFieldEvaluatedConstraint](docs/v2/Ontologies/models/StructFieldEvaluatedConstraint.md) | `from foundry_sdk.v2.ontologies.models import StructFieldEvaluatedConstraint` |
**Ontologies** | [StructFieldEvaluationResult](docs/v2/Ontologies/models/StructFieldEvaluationResult.md) | `from foundry_sdk.v2.ontologies.models import StructFieldEvaluationResult` |
**Ontologies** | [StructFieldSelector](docs/v2/Ontologies/models/StructFieldSelector.md) | `from foundry_sdk.v2.ontologies.models import StructFieldSelector` |
**Ontologies** | [StructFieldType](docs/v2/Ontologies/models/StructFieldType.md) | `from foundry_sdk.v2.ontologies.models import StructFieldType` |
**Ontologies** | [StructFieldTypeRid](docs/v2/Ontologies/models/StructFieldTypeRid.md) | `from foundry_sdk.v2.ontologies.models import StructFieldTypeRid` |
**Ontologies** | [StructParameterFieldApiName](docs/v2/Ontologies/models/StructParameterFieldApiName.md) | `from foundry_sdk.v2.ontologies.models import StructParameterFieldApiName` |
**Ontologies** | [StructType](docs/v2/Ontologies/models/StructType.md) | `from foundry_sdk.v2.ontologies.models import StructType` |
**Ontologies** | [SubmissionCriteriaEvaluation](docs/v2/Ontologies/models/SubmissionCriteriaEvaluation.md) | `from foundry_sdk.v2.ontologies.models import SubmissionCriteriaEvaluation` |
**Ontologies** | [SubtractPropertyExpression](docs/v2/Ontologies/models/SubtractPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import SubtractPropertyExpression` |
**Ontologies** | [SumAggregationV2](docs/v2/Ontologies/models/SumAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import SumAggregationV2` |
**Ontologies** | [SyncApplyActionResponseV2](docs/v2/Ontologies/models/SyncApplyActionResponseV2.md) | `from foundry_sdk.v2.ontologies.models import SyncApplyActionResponseV2` |
**Ontologies** | [ThreeDimensionalAggregation](docs/v2/Ontologies/models/ThreeDimensionalAggregation.md) | `from foundry_sdk.v2.ontologies.models import ThreeDimensionalAggregation` |
**Ontologies** | [TimeRange](docs/v2/Ontologies/models/TimeRange.md) | `from foundry_sdk.v2.ontologies.models import TimeRange` |
**Ontologies** | [TimeSeriesAggregationMethod](docs/v2/Ontologies/models/TimeSeriesAggregationMethod.md) | `from foundry_sdk.v2.ontologies.models import TimeSeriesAggregationMethod` |
**Ontologies** | [TimeSeriesAggregationStrategy](docs/v2/Ontologies/models/TimeSeriesAggregationStrategy.md) | `from foundry_sdk.v2.ontologies.models import TimeSeriesAggregationStrategy` |
**Ontologies** | [TimeSeriesCumulativeAggregate](docs/v2/Ontologies/models/TimeSeriesCumulativeAggregate.md) | `from foundry_sdk.v2.ontologies.models import TimeSeriesCumulativeAggregate` |
**Ontologies** | [TimeseriesEntry](docs/v2/Ontologies/models/TimeseriesEntry.md) | `from foundry_sdk.v2.ontologies.models import TimeseriesEntry` |
**Ontologies** | [TimeSeriesPeriodicAggregate](docs/v2/Ontologies/models/TimeSeriesPeriodicAggregate.md) | `from foundry_sdk.v2.ontologies.models import TimeSeriesPeriodicAggregate` |
**Ontologies** | [TimeSeriesPoint](docs/v2/Ontologies/models/TimeSeriesPoint.md) | `from foundry_sdk.v2.ontologies.models import TimeSeriesPoint` |
**Ontologies** | [TimeSeriesRollingAggregate](docs/v2/Ontologies/models/TimeSeriesRollingAggregate.md) | `from foundry_sdk.v2.ontologies.models import TimeSeriesRollingAggregate` |
**Ontologies** | [TimeSeriesRollingAggregateWindow](docs/v2/Ontologies/models/TimeSeriesRollingAggregateWindow.md) | `from foundry_sdk.v2.ontologies.models import TimeSeriesRollingAggregateWindow` |
**Ontologies** | [TimeSeriesWindowType](docs/v2/Ontologies/models/TimeSeriesWindowType.md) | `from foundry_sdk.v2.ontologies.models import TimeSeriesWindowType` |
**Ontologies** | [TimeUnit](docs/v2/Ontologies/models/TimeUnit.md) | `from foundry_sdk.v2.ontologies.models import TimeUnit` |
**Ontologies** | [TransactionEdit](docs/v2/Ontologies/models/TransactionEdit.md) | `from foundry_sdk.v2.ontologies.models import TransactionEdit` |
**Ontologies** | [TwoDimensionalAggregation](docs/v2/Ontologies/models/TwoDimensionalAggregation.md) | `from foundry_sdk.v2.ontologies.models import TwoDimensionalAggregation` |
**Ontologies** | [UnevaluableConstraint](docs/v2/Ontologies/models/UnevaluableConstraint.md) | `from foundry_sdk.v2.ontologies.models import UnevaluableConstraint` |
**Ontologies** | [UuidConstraint](docs/v2/Ontologies/models/UuidConstraint.md) | `from foundry_sdk.v2.ontologies.models import UuidConstraint` |
**Ontologies** | [ValidateActionResponseV2](docs/v2/Ontologies/models/ValidateActionResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ValidateActionResponseV2` |
**Ontologies** | [ValidationResult](docs/v2/Ontologies/models/ValidationResult.md) | `from foundry_sdk.v2.ontologies.models import ValidationResult` |
**Ontologies** | [ValueType](docs/v2/Ontologies/models/ValueType.md) | `from foundry_sdk.v2.ontologies.models import ValueType` |
**Ontologies** | [ValueTypeApiName](docs/v2/Ontologies/models/ValueTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeApiName` |
**Ontologies** | [ValueTypeArrayType](docs/v2/Ontologies/models/ValueTypeArrayType.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeArrayType` |
**Ontologies** | [ValueTypeConstraint](docs/v2/Ontologies/models/ValueTypeConstraint.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeConstraint` |
**Ontologies** | [ValueTypeDecimalType](docs/v2/Ontologies/models/ValueTypeDecimalType.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeDecimalType` |
**Ontologies** | [ValueTypeFieldType](docs/v2/Ontologies/models/ValueTypeFieldType.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeFieldType` |
**Ontologies** | [ValueTypeMapType](docs/v2/Ontologies/models/ValueTypeMapType.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeMapType` |
**Ontologies** | [ValueTypeOptionalType](docs/v2/Ontologies/models/ValueTypeOptionalType.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeOptionalType` |
**Ontologies** | [ValueTypeReferenceType](docs/v2/Ontologies/models/ValueTypeReferenceType.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeReferenceType` |
**Ontologies** | [ValueTypeRid](docs/v2/Ontologies/models/ValueTypeRid.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeRid` |
**Ontologies** | [ValueTypeStatus](docs/v2/Ontologies/models/ValueTypeStatus.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeStatus` |
**Ontologies** | [ValueTypeStructField](docs/v2/Ontologies/models/ValueTypeStructField.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeStructField` |
**Ontologies** | [ValueTypeStructType](docs/v2/Ontologies/models/ValueTypeStructType.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeStructType` |
**Ontologies** | [ValueTypeUnionType](docs/v2/Ontologies/models/ValueTypeUnionType.md) | `from foundry_sdk.v2.ontologies.models import ValueTypeUnionType` |
**Ontologies** | [VersionedQueryTypeApiName](docs/v2/Ontologies/models/VersionedQueryTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import VersionedQueryTypeApiName` |
**Ontologies** | [WithinBoundingBoxPoint](docs/v2/Ontologies/models/WithinBoundingBoxPoint.md) | `from foundry_sdk.v2.ontologies.models import WithinBoundingBoxPoint` |
**Ontologies** | [WithinBoundingBoxQuery](docs/v2/Ontologies/models/WithinBoundingBoxQuery.md) | `from foundry_sdk.v2.ontologies.models import WithinBoundingBoxQuery` |
**Ontologies** | [WithinDistanceOfQuery](docs/v2/Ontologies/models/WithinDistanceOfQuery.md) | `from foundry_sdk.v2.ontologies.models import WithinDistanceOfQuery` |
**Ontologies** | [WithinPolygonQuery](docs/v2/Ontologies/models/WithinPolygonQuery.md) | `from foundry_sdk.v2.ontologies.models import WithinPolygonQuery` |
**Orchestration** | [AbortOnFailure](docs/v2/Orchestration/models/AbortOnFailure.md) | `from foundry_sdk.v2.orchestration.models import AbortOnFailure` |
**Orchestration** | [Action](docs/v2/Orchestration/models/Action.md) | `from foundry_sdk.v2.orchestration.models import Action` |
**Orchestration** | [AndTrigger](docs/v2/Orchestration/models/AndTrigger.md) | `from foundry_sdk.v2.orchestration.models import AndTrigger` |
**Orchestration** | [Build](docs/v2/Orchestration/models/Build.md) | `from foundry_sdk.v2.orchestration.models import Build` |
**Orchestration** | [BuildableRid](docs/v2/Orchestration/models/BuildableRid.md) | `from foundry_sdk.v2.orchestration.models import BuildableRid` |
**Orchestration** | [BuildStatus](docs/v2/Orchestration/models/BuildStatus.md) | `from foundry_sdk.v2.orchestration.models import BuildStatus` |
**Orchestration** | [BuildTarget](docs/v2/Orchestration/models/BuildTarget.md) | `from foundry_sdk.v2.orchestration.models import BuildTarget` |
**Orchestration** | [ConnectingTarget](docs/v2/Orchestration/models/ConnectingTarget.md) | `from foundry_sdk.v2.orchestration.models import ConnectingTarget` |
**Orchestration** | [CreateScheduleRequestAction](docs/v2/Orchestration/models/CreateScheduleRequestAction.md) | `from foundry_sdk.v2.orchestration.models import CreateScheduleRequestAction` |
**Orchestration** | [CreateScheduleRequestBuildTarget](docs/v2/Orchestration/models/CreateScheduleRequestBuildTarget.md) | `from foundry_sdk.v2.orchestration.models import CreateScheduleRequestBuildTarget` |
**Orchestration** | [CreateScheduleRequestConnectingTarget](docs/v2/Orchestration/models/CreateScheduleRequestConnectingTarget.md) | `from foundry_sdk.v2.orchestration.models import CreateScheduleRequestConnectingTarget` |
**Orchestration** | [CreateScheduleRequestManualTarget](docs/v2/Orchestration/models/CreateScheduleRequestManualTarget.md) | `from foundry_sdk.v2.orchestration.models import CreateScheduleRequestManualTarget` |
**Orchestration** | [CreateScheduleRequestProjectScope](docs/v2/Orchestration/models/CreateScheduleRequestProjectScope.md) | `from foundry_sdk.v2.orchestration.models import CreateScheduleRequestProjectScope` |
**Orchestration** | [CreateScheduleRequestScopeMode](docs/v2/Orchestration/models/CreateScheduleRequestScopeMode.md) | `from foundry_sdk.v2.orchestration.models import CreateScheduleRequestScopeMode` |
**Orchestration** | [CreateScheduleRequestUpstreamTarget](docs/v2/Orchestration/models/CreateScheduleRequestUpstreamTarget.md) | `from foundry_sdk.v2.orchestration.models import CreateScheduleRequestUpstreamTarget` |
**Orchestration** | [CreateScheduleRequestUserScope](docs/v2/Orchestration/models/CreateScheduleRequestUserScope.md) | `from foundry_sdk.v2.orchestration.models import CreateScheduleRequestUserScope` |
**Orchestration** | [CronExpression](docs/v2/Orchestration/models/CronExpression.md) | `from foundry_sdk.v2.orchestration.models import CronExpression` |
**Orchestration** | [DatasetJobOutput](docs/v2/Orchestration/models/DatasetJobOutput.md) | `from foundry_sdk.v2.orchestration.models import DatasetJobOutput` |
**Orchestration** | [DatasetUpdatedTrigger](docs/v2/Orchestration/models/DatasetUpdatedTrigger.md) | `from foundry_sdk.v2.orchestration.models import DatasetUpdatedTrigger` |
**Orchestration** | [FallbackBranches](docs/v2/Orchestration/models/FallbackBranches.md) | `from foundry_sdk.v2.orchestration.models import FallbackBranches` |
**Orchestration** | [ForceBuild](docs/v2/Orchestration/models/ForceBuild.md) | `from foundry_sdk.v2.orchestration.models import ForceBuild` |
**Orchestration** | [GetBuildsBatchRequestElement](docs/v2/Orchestration/models/GetBuildsBatchRequestElement.md) | `from foundry_sdk.v2.orchestration.models import GetBuildsBatchRequestElement` |
**Orchestration** | [GetBuildsBatchResponse](docs/v2/Orchestration/models/GetBuildsBatchResponse.md) | `from foundry_sdk.v2.orchestration.models import GetBuildsBatchResponse` |
**Orchestration** | [GetJobsBatchRequestElement](docs/v2/Orchestration/models/GetJobsBatchRequestElement.md) | `from foundry_sdk.v2.orchestration.models import GetJobsBatchRequestElement` |
**Orchestration** | [GetJobsBatchResponse](docs/v2/Orchestration/models/GetJobsBatchResponse.md) | `from foundry_sdk.v2.orchestration.models import GetJobsBatchResponse` |
**Orchestration** | [GetSchedulesBatchRequestElement](docs/v2/Orchestration/models/GetSchedulesBatchRequestElement.md) | `from foundry_sdk.v2.orchestration.models import GetSchedulesBatchRequestElement` |
**Orchestration** | [GetSchedulesBatchResponse](docs/v2/Orchestration/models/GetSchedulesBatchResponse.md) | `from foundry_sdk.v2.orchestration.models import GetSchedulesBatchResponse` |
**Orchestration** | [Job](docs/v2/Orchestration/models/Job.md) | `from foundry_sdk.v2.orchestration.models import Job` |
**Orchestration** | [JobOutput](docs/v2/Orchestration/models/JobOutput.md) | `from foundry_sdk.v2.orchestration.models import JobOutput` |
**Orchestration** | [JobStartedTime](docs/v2/Orchestration/models/JobStartedTime.md) | `from foundry_sdk.v2.orchestration.models import JobStartedTime` |
**Orchestration** | [JobStatus](docs/v2/Orchestration/models/JobStatus.md) | `from foundry_sdk.v2.orchestration.models import JobStatus` |
**Orchestration** | [JobSucceededTrigger](docs/v2/Orchestration/models/JobSucceededTrigger.md) | `from foundry_sdk.v2.orchestration.models import JobSucceededTrigger` |
**Orchestration** | [ListJobsOfBuildResponse](docs/v2/Orchestration/models/ListJobsOfBuildResponse.md) | `from foundry_sdk.v2.orchestration.models import ListJobsOfBuildResponse` |
**Orchestration** | [ListRunsOfScheduleResponse](docs/v2/Orchestration/models/ListRunsOfScheduleResponse.md) | `from foundry_sdk.v2.orchestration.models import ListRunsOfScheduleResponse` |
**Orchestration** | [ManualTarget](docs/v2/Orchestration/models/ManualTarget.md) | `from foundry_sdk.v2.orchestration.models import ManualTarget` |
**Orchestration** | [ManualTrigger](docs/v2/Orchestration/models/ManualTrigger.md) | `from foundry_sdk.v2.orchestration.models import ManualTrigger` |
**Orchestration** | [MediaSetUpdatedTrigger](docs/v2/Orchestration/models/MediaSetUpdatedTrigger.md) | `from foundry_sdk.v2.orchestration.models import MediaSetUpdatedTrigger` |
**Orchestration** | [NewLogicTrigger](docs/v2/Orchestration/models/NewLogicTrigger.md) | `from foundry_sdk.v2.orchestration.models import NewLogicTrigger` |
**Orchestration** | [NotificationsEnabled](docs/v2/Orchestration/models/NotificationsEnabled.md) | `from foundry_sdk.v2.orchestration.models import NotificationsEnabled` |
**Orchestration** | [OrTrigger](docs/v2/Orchestration/models/OrTrigger.md) | `from foundry_sdk.v2.orchestration.models import OrTrigger` |
**Orchestration** | [ProjectScope](docs/v2/Orchestration/models/ProjectScope.md) | `from foundry_sdk.v2.orchestration.models import ProjectScope` |
**Orchestration** | [ReplaceScheduleRequestAction](docs/v2/Orchestration/models/ReplaceScheduleRequestAction.md) | `from foundry_sdk.v2.orchestration.models import ReplaceScheduleRequestAction` |
**Orchestration** | [ReplaceScheduleRequestBuildTarget](docs/v2/Orchestration/models/ReplaceScheduleRequestBuildTarget.md) | `from foundry_sdk.v2.orchestration.models import ReplaceScheduleRequestBuildTarget` |
**Orchestration** | [ReplaceScheduleRequestConnectingTarget](docs/v2/Orchestration/models/ReplaceScheduleRequestConnectingTarget.md) | `from foundry_sdk.v2.orchestration.models import ReplaceScheduleRequestConnectingTarget` |
**Orchestration** | [ReplaceScheduleRequestManualTarget](docs/v2/Orchestration/models/ReplaceScheduleRequestManualTarget.md) | `from foundry_sdk.v2.orchestration.models import ReplaceScheduleRequestManualTarget` |
**Orchestration** | [ReplaceScheduleRequestProjectScope](docs/v2/Orchestration/models/ReplaceScheduleRequestProjectScope.md) | `from foundry_sdk.v2.orchestration.models import ReplaceScheduleRequestProjectScope` |
**Orchestration** | [ReplaceScheduleRequestScopeMode](docs/v2/Orchestration/models/ReplaceScheduleRequestScopeMode.md) | `from foundry_sdk.v2.orchestration.models import ReplaceScheduleRequestScopeMode` |
**Orchestration** | [ReplaceScheduleRequestUpstreamTarget](docs/v2/Orchestration/models/ReplaceScheduleRequestUpstreamTarget.md) | `from foundry_sdk.v2.orchestration.models import ReplaceScheduleRequestUpstreamTarget` |
**Orchestration** | [ReplaceScheduleRequestUserScope](docs/v2/Orchestration/models/ReplaceScheduleRequestUserScope.md) | `from foundry_sdk.v2.orchestration.models import ReplaceScheduleRequestUserScope` |
**Orchestration** | [RetryBackoffDuration](docs/v2/Orchestration/models/RetryBackoffDuration.md) | `from foundry_sdk.v2.orchestration.models import RetryBackoffDuration` |
**Orchestration** | [RetryCount](docs/v2/Orchestration/models/RetryCount.md) | `from foundry_sdk.v2.orchestration.models import RetryCount` |
**Orchestration** | [Schedule](docs/v2/Orchestration/models/Schedule.md) | `from foundry_sdk.v2.orchestration.models import Schedule` |
**Orchestration** | [SchedulePaused](docs/v2/Orchestration/models/SchedulePaused.md) | `from foundry_sdk.v2.orchestration.models import SchedulePaused` |
**Orchestration** | [ScheduleRun](docs/v2/Orchestration/models/ScheduleRun.md) | `from foundry_sdk.v2.orchestration.models import ScheduleRun` |
**Orchestration** | [ScheduleRunError](docs/v2/Orchestration/models/ScheduleRunError.md) | `from foundry_sdk.v2.orchestration.models import ScheduleRunError` |
**Orchestration** | [ScheduleRunErrorName](docs/v2/Orchestration/models/ScheduleRunErrorName.md) | `from foundry_sdk.v2.orchestration.models import ScheduleRunErrorName` |
**Orchestration** | [ScheduleRunIgnored](docs/v2/Orchestration/models/ScheduleRunIgnored.md) | `from foundry_sdk.v2.orchestration.models import ScheduleRunIgnored` |
**Orchestration** | [ScheduleRunResult](docs/v2/Orchestration/models/ScheduleRunResult.md) | `from foundry_sdk.v2.orchestration.models import ScheduleRunResult` |
**Orchestration** | [ScheduleRunRid](docs/v2/Orchestration/models/ScheduleRunRid.md) | `from foundry_sdk.v2.orchestration.models import ScheduleRunRid` |
**Orchestration** | [ScheduleRunSubmitted](docs/v2/Orchestration/models/ScheduleRunSubmitted.md) | `from foundry_sdk.v2.orchestration.models import ScheduleRunSubmitted` |
**Orchestration** | [ScheduleSucceededTrigger](docs/v2/Orchestration/models/ScheduleSucceededTrigger.md) | `from foundry_sdk.v2.orchestration.models import ScheduleSucceededTrigger` |
**Orchestration** | [ScheduleVersion](docs/v2/Orchestration/models/ScheduleVersion.md) | `from foundry_sdk.v2.orchestration.models import ScheduleVersion` |
**Orchestration** | [ScheduleVersionRid](docs/v2/Orchestration/models/ScheduleVersionRid.md) | `from foundry_sdk.v2.orchestration.models import ScheduleVersionRid` |
**Orchestration** | [ScopeMode](docs/v2/Orchestration/models/ScopeMode.md) | `from foundry_sdk.v2.orchestration.models import ScopeMode` |
**Orchestration** | [SearchBuildsAndFilter](docs/v2/Orchestration/models/SearchBuildsAndFilter.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsAndFilter` |
**Orchestration** | [SearchBuildsEqualsFilter](docs/v2/Orchestration/models/SearchBuildsEqualsFilter.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsEqualsFilter` |
**Orchestration** | [SearchBuildsEqualsFilterField](docs/v2/Orchestration/models/SearchBuildsEqualsFilterField.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsEqualsFilterField` |
**Orchestration** | [SearchBuildsFilter](docs/v2/Orchestration/models/SearchBuildsFilter.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsFilter` |
**Orchestration** | [SearchBuildsGteFilter](docs/v2/Orchestration/models/SearchBuildsGteFilter.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsGteFilter` |
**Orchestration** | [SearchBuildsGteFilterField](docs/v2/Orchestration/models/SearchBuildsGteFilterField.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsGteFilterField` |
**Orchestration** | [SearchBuildsLtFilter](docs/v2/Orchestration/models/SearchBuildsLtFilter.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsLtFilter` |
**Orchestration** | [SearchBuildsLtFilterField](docs/v2/Orchestration/models/SearchBuildsLtFilterField.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsLtFilterField` |
**Orchestration** | [SearchBuildsNotFilter](docs/v2/Orchestration/models/SearchBuildsNotFilter.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsNotFilter` |
**Orchestration** | [SearchBuildsOrderBy](docs/v2/Orchestration/models/SearchBuildsOrderBy.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsOrderBy` |
**Orchestration** | [SearchBuildsOrderByField](docs/v2/Orchestration/models/SearchBuildsOrderByField.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsOrderByField` |
**Orchestration** | [SearchBuildsOrderByItem](docs/v2/Orchestration/models/SearchBuildsOrderByItem.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsOrderByItem` |
**Orchestration** | [SearchBuildsOrFilter](docs/v2/Orchestration/models/SearchBuildsOrFilter.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsOrFilter` |
**Orchestration** | [SearchBuildsResponse](docs/v2/Orchestration/models/SearchBuildsResponse.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsResponse` |
**Orchestration** | [TimeTrigger](docs/v2/Orchestration/models/TimeTrigger.md) | `from foundry_sdk.v2.orchestration.models import TimeTrigger` |
**Orchestration** | [TransactionalMediaSetJobOutput](docs/v2/Orchestration/models/TransactionalMediaSetJobOutput.md) | `from foundry_sdk.v2.orchestration.models import TransactionalMediaSetJobOutput` |
**Orchestration** | [Trigger](docs/v2/Orchestration/models/Trigger.md) | `from foundry_sdk.v2.orchestration.models import Trigger` |
**Orchestration** | [UpstreamTarget](docs/v2/Orchestration/models/UpstreamTarget.md) | `from foundry_sdk.v2.orchestration.models import UpstreamTarget` |
**Orchestration** | [UserScope](docs/v2/Orchestration/models/UserScope.md) | `from foundry_sdk.v2.orchestration.models import UserScope` |
**SqlQueries** | [CanceledQueryStatus](docs/v2/SqlQueries/models/CanceledQueryStatus.md) | `from foundry_sdk.v2.sql_queries.models import CanceledQueryStatus` |
**SqlQueries** | [FailedQueryStatus](docs/v2/SqlQueries/models/FailedQueryStatus.md) | `from foundry_sdk.v2.sql_queries.models import FailedQueryStatus` |
**SqlQueries** | [QueryStatus](docs/v2/SqlQueries/models/QueryStatus.md) | `from foundry_sdk.v2.sql_queries.models import QueryStatus` |
**SqlQueries** | [RunningQueryStatus](docs/v2/SqlQueries/models/RunningQueryStatus.md) | `from foundry_sdk.v2.sql_queries.models import RunningQueryStatus` |
**SqlQueries** | [SqlQueryId](docs/v2/SqlQueries/models/SqlQueryId.md) | `from foundry_sdk.v2.sql_queries.models import SqlQueryId` |
**SqlQueries** | [SucceededQueryStatus](docs/v2/SqlQueries/models/SucceededQueryStatus.md) | `from foundry_sdk.v2.sql_queries.models import SucceededQueryStatus` |
**Streams** | [Compressed](docs/v2/Streams/models/Compressed.md) | `from foundry_sdk.v2.streams.models import Compressed` |
**Streams** | [CreateStreamRequestStreamSchema](docs/v2/Streams/models/CreateStreamRequestStreamSchema.md) | `from foundry_sdk.v2.streams.models import CreateStreamRequestStreamSchema` |
**Streams** | [Dataset](docs/v2/Streams/models/Dataset.md) | `from foundry_sdk.v2.streams.models import Dataset` |
**Streams** | [PartitionsCount](docs/v2/Streams/models/PartitionsCount.md) | `from foundry_sdk.v2.streams.models import PartitionsCount` |
**Streams** | [Record](docs/v2/Streams/models/Record.md) | `from foundry_sdk.v2.streams.models import Record` |
**Streams** | [Stream](docs/v2/Streams/models/Stream.md) | `from foundry_sdk.v2.streams.models import Stream` |
**Streams** | [StreamType](docs/v2/Streams/models/StreamType.md) | `from foundry_sdk.v2.streams.models import StreamType` |
**Streams** | [ViewRid](docs/v2/Streams/models/ViewRid.md) | `from foundry_sdk.v2.streams.models import ViewRid` |
**ThirdPartyApplications** | [ListVersionsResponse](docs/v2/ThirdPartyApplications/models/ListVersionsResponse.md) | `from foundry_sdk.v2.third_party_applications.models import ListVersionsResponse` |
**ThirdPartyApplications** | [Subdomain](docs/v2/ThirdPartyApplications/models/Subdomain.md) | `from foundry_sdk.v2.third_party_applications.models import Subdomain` |
**ThirdPartyApplications** | [ThirdPartyApplication](docs/v2/ThirdPartyApplications/models/ThirdPartyApplication.md) | `from foundry_sdk.v2.third_party_applications.models import ThirdPartyApplication` |
**ThirdPartyApplications** | [ThirdPartyApplicationRid](docs/v2/ThirdPartyApplications/models/ThirdPartyApplicationRid.md) | `from foundry_sdk.v2.third_party_applications.models import ThirdPartyApplicationRid` |
**ThirdPartyApplications** | [Version](docs/v2/ThirdPartyApplications/models/Version.md) | `from foundry_sdk.v2.third_party_applications.models import Version` |
**ThirdPartyApplications** | [VersionVersion](docs/v2/ThirdPartyApplications/models/VersionVersion.md) | `from foundry_sdk.v2.third_party_applications.models import VersionVersion` |
**ThirdPartyApplications** | [Website](docs/v2/ThirdPartyApplications/models/Website.md) | `from foundry_sdk.v2.third_party_applications.models import Website` |

<a id="models-v1-link"></a>
## Documentation for V1 models

Namespace | Name | Import |
--------- | ---- | ------ |
**Core** | [AnyType](docs/v1/Core/models/AnyType.md) | `from foundry_sdk.v1.core.models import AnyType` |
**Core** | [AttachmentType](docs/v1/Core/models/AttachmentType.md) | `from foundry_sdk.v1.core.models import AttachmentType` |
**Core** | [BinaryType](docs/v1/Core/models/BinaryType.md) | `from foundry_sdk.v1.core.models import BinaryType` |
**Core** | [BooleanType](docs/v1/Core/models/BooleanType.md) | `from foundry_sdk.v1.core.models import BooleanType` |
**Core** | [ByteType](docs/v1/Core/models/ByteType.md) | `from foundry_sdk.v1.core.models import ByteType` |
**Core** | [CipherTextType](docs/v1/Core/models/CipherTextType.md) | `from foundry_sdk.v1.core.models import CipherTextType` |
**Core** | [ContentLength](docs/v1/Core/models/ContentLength.md) | `from foundry_sdk.v1.core.models import ContentLength` |
**Core** | [ContentType](docs/v1/Core/models/ContentType.md) | `from foundry_sdk.v1.core.models import ContentType` |
**Core** | [DateType](docs/v1/Core/models/DateType.md) | `from foundry_sdk.v1.core.models import DateType` |
**Core** | [DecimalType](docs/v1/Core/models/DecimalType.md) | `from foundry_sdk.v1.core.models import DecimalType` |
**Core** | [DisplayName](docs/v1/Core/models/DisplayName.md) | `from foundry_sdk.v1.core.models import DisplayName` |
**Core** | [DistanceUnit](docs/v1/Core/models/DistanceUnit.md) | `from foundry_sdk.v1.core.models import DistanceUnit` |
**Core** | [DoubleType](docs/v1/Core/models/DoubleType.md) | `from foundry_sdk.v1.core.models import DoubleType` |
**Core** | [Filename](docs/v1/Core/models/Filename.md) | `from foundry_sdk.v1.core.models import Filename` |
**Core** | [FilePath](docs/v1/Core/models/FilePath.md) | `from foundry_sdk.v1.core.models import FilePath` |
**Core** | [FloatType](docs/v1/Core/models/FloatType.md) | `from foundry_sdk.v1.core.models import FloatType` |
**Core** | [FolderRid](docs/v1/Core/models/FolderRid.md) | `from foundry_sdk.v1.core.models import FolderRid` |
**Core** | [FoundryBranch](docs/v1/Core/models/FoundryBranch.md) | `from foundry_sdk.v1.core.models import FoundryBranch` |
**Core** | [IntegerType](docs/v1/Core/models/IntegerType.md) | `from foundry_sdk.v1.core.models import IntegerType` |
**Core** | [LongType](docs/v1/Core/models/LongType.md) | `from foundry_sdk.v1.core.models import LongType` |
**Core** | [MarkingType](docs/v1/Core/models/MarkingType.md) | `from foundry_sdk.v1.core.models import MarkingType` |
**Core** | [MediaType](docs/v1/Core/models/MediaType.md) | `from foundry_sdk.v1.core.models import MediaType` |
**Core** | [NullType](docs/v1/Core/models/NullType.md) | `from foundry_sdk.v1.core.models import NullType` |
**Core** | [OperationScope](docs/v1/Core/models/OperationScope.md) | `from foundry_sdk.v1.core.models import OperationScope` |
**Core** | [PageSize](docs/v1/Core/models/PageSize.md) | `from foundry_sdk.v1.core.models import PageSize` |
**Core** | [PageToken](docs/v1/Core/models/PageToken.md) | `from foundry_sdk.v1.core.models import PageToken` |
**Core** | [PreviewMode](docs/v1/Core/models/PreviewMode.md) | `from foundry_sdk.v1.core.models import PreviewMode` |
**Core** | [ReleaseStatus](docs/v1/Core/models/ReleaseStatus.md) | `from foundry_sdk.v1.core.models import ReleaseStatus` |
**Core** | [ShortType](docs/v1/Core/models/ShortType.md) | `from foundry_sdk.v1.core.models import ShortType` |
**Core** | [SizeBytes](docs/v1/Core/models/SizeBytes.md) | `from foundry_sdk.v1.core.models import SizeBytes` |
**Core** | [StringType](docs/v1/Core/models/StringType.md) | `from foundry_sdk.v1.core.models import StringType` |
**Core** | [StructFieldName](docs/v1/Core/models/StructFieldName.md) | `from foundry_sdk.v1.core.models import StructFieldName` |
**Core** | [TimestampType](docs/v1/Core/models/TimestampType.md) | `from foundry_sdk.v1.core.models import TimestampType` |
**Core** | [TotalCount](docs/v1/Core/models/TotalCount.md) | `from foundry_sdk.v1.core.models import TotalCount` |
**Core** | [TraceParent](docs/v1/Core/models/TraceParent.md) | `from foundry_sdk.v1.core.models import TraceParent` |
**Core** | [TraceState](docs/v1/Core/models/TraceState.md) | `from foundry_sdk.v1.core.models import TraceState` |
**Core** | [UnsupportedType](docs/v1/Core/models/UnsupportedType.md) | `from foundry_sdk.v1.core.models import UnsupportedType` |
**Datasets** | [Branch](docs/v1/Datasets/models/Branch.md) | `from foundry_sdk.v1.datasets.models import Branch` |
**Datasets** | [BranchId](docs/v1/Datasets/models/BranchId.md) | `from foundry_sdk.v1.datasets.models import BranchId` |
**Datasets** | [Dataset](docs/v1/Datasets/models/Dataset.md) | `from foundry_sdk.v1.datasets.models import Dataset` |
**Datasets** | [DatasetName](docs/v1/Datasets/models/DatasetName.md) | `from foundry_sdk.v1.datasets.models import DatasetName` |
**Datasets** | [DatasetRid](docs/v1/Datasets/models/DatasetRid.md) | `from foundry_sdk.v1.datasets.models import DatasetRid` |
**Datasets** | [File](docs/v1/Datasets/models/File.md) | `from foundry_sdk.v1.datasets.models import File` |
**Datasets** | [ListBranchesResponse](docs/v1/Datasets/models/ListBranchesResponse.md) | `from foundry_sdk.v1.datasets.models import ListBranchesResponse` |
**Datasets** | [ListFilesResponse](docs/v1/Datasets/models/ListFilesResponse.md) | `from foundry_sdk.v1.datasets.models import ListFilesResponse` |
**Datasets** | [TableExportFormat](docs/v1/Datasets/models/TableExportFormat.md) | `from foundry_sdk.v1.datasets.models import TableExportFormat` |
**Datasets** | [Transaction](docs/v1/Datasets/models/Transaction.md) | `from foundry_sdk.v1.datasets.models import Transaction` |
**Datasets** | [TransactionRid](docs/v1/Datasets/models/TransactionRid.md) | `from foundry_sdk.v1.datasets.models import TransactionRid` |
**Datasets** | [TransactionStatus](docs/v1/Datasets/models/TransactionStatus.md) | `from foundry_sdk.v1.datasets.models import TransactionStatus` |
**Datasets** | [TransactionType](docs/v1/Datasets/models/TransactionType.md) | `from foundry_sdk.v1.datasets.models import TransactionType` |
**Ontologies** | [ActionRid](docs/v1/Ontologies/models/ActionRid.md) | `from foundry_sdk.v1.ontologies.models import ActionRid` |
**Ontologies** | [ActionType](docs/v1/Ontologies/models/ActionType.md) | `from foundry_sdk.v1.ontologies.models import ActionType` |
**Ontologies** | [ActionTypeApiName](docs/v1/Ontologies/models/ActionTypeApiName.md) | `from foundry_sdk.v1.ontologies.models import ActionTypeApiName` |
**Ontologies** | [ActionTypeRid](docs/v1/Ontologies/models/ActionTypeRid.md) | `from foundry_sdk.v1.ontologies.models import ActionTypeRid` |
**Ontologies** | [AggregateObjectsResponse](docs/v1/Ontologies/models/AggregateObjectsResponse.md) | `from foundry_sdk.v1.ontologies.models import AggregateObjectsResponse` |
**Ontologies** | [AggregateObjectsResponseItem](docs/v1/Ontologies/models/AggregateObjectsResponseItem.md) | `from foundry_sdk.v1.ontologies.models import AggregateObjectsResponseItem` |
**Ontologies** | [Aggregation](docs/v1/Ontologies/models/Aggregation.md) | `from foundry_sdk.v1.ontologies.models import Aggregation` |
**Ontologies** | [AggregationDurationGrouping](docs/v1/Ontologies/models/AggregationDurationGrouping.md) | `from foundry_sdk.v1.ontologies.models import AggregationDurationGrouping` |
**Ontologies** | [AggregationExactGrouping](docs/v1/Ontologies/models/AggregationExactGrouping.md) | `from foundry_sdk.v1.ontologies.models import AggregationExactGrouping` |
**Ontologies** | [AggregationFixedWidthGrouping](docs/v1/Ontologies/models/AggregationFixedWidthGrouping.md) | `from foundry_sdk.v1.ontologies.models import AggregationFixedWidthGrouping` |
**Ontologies** | [AggregationGroupBy](docs/v1/Ontologies/models/AggregationGroupBy.md) | `from foundry_sdk.v1.ontologies.models import AggregationGroupBy` |
**Ontologies** | [AggregationGroupKey](docs/v1/Ontologies/models/AggregationGroupKey.md) | `from foundry_sdk.v1.ontologies.models import AggregationGroupKey` |
**Ontologies** | [AggregationGroupValue](docs/v1/Ontologies/models/AggregationGroupValue.md) | `from foundry_sdk.v1.ontologies.models import AggregationGroupValue` |
**Ontologies** | [AggregationMetricName](docs/v1/Ontologies/models/AggregationMetricName.md) | `from foundry_sdk.v1.ontologies.models import AggregationMetricName` |
**Ontologies** | [AggregationMetricResult](docs/v1/Ontologies/models/AggregationMetricResult.md) | `from foundry_sdk.v1.ontologies.models import AggregationMetricResult` |
**Ontologies** | [AggregationRange](docs/v1/Ontologies/models/AggregationRange.md) | `from foundry_sdk.v1.ontologies.models import AggregationRange` |
**Ontologies** | [AggregationRangesGrouping](docs/v1/Ontologies/models/AggregationRangesGrouping.md) | `from foundry_sdk.v1.ontologies.models import AggregationRangesGrouping` |
**Ontologies** | [AllTermsQuery](docs/v1/Ontologies/models/AllTermsQuery.md) | `from foundry_sdk.v1.ontologies.models import AllTermsQuery` |
**Ontologies** | [AndQuery](docs/v1/Ontologies/models/AndQuery.md) | `from foundry_sdk.v1.ontologies.models import AndQuery` |
**Ontologies** | [AnyTermQuery](docs/v1/Ontologies/models/AnyTermQuery.md) | `from foundry_sdk.v1.ontologies.models import AnyTermQuery` |
**Ontologies** | [ApplyActionMode](docs/v1/Ontologies/models/ApplyActionMode.md) | `from foundry_sdk.v1.ontologies.models import ApplyActionMode` |
**Ontologies** | [ApplyActionRequest](docs/v1/Ontologies/models/ApplyActionRequest.md) | `from foundry_sdk.v1.ontologies.models import ApplyActionRequest` |
**Ontologies** | [ApplyActionRequestOptions](docs/v1/Ontologies/models/ApplyActionRequestOptions.md) | `from foundry_sdk.v1.ontologies.models import ApplyActionRequestOptions` |
**Ontologies** | [ApplyActionResponse](docs/v1/Ontologies/models/ApplyActionResponse.md) | `from foundry_sdk.v1.ontologies.models import ApplyActionResponse` |
**Ontologies** | [ApproximateDistinctAggregation](docs/v1/Ontologies/models/ApproximateDistinctAggregation.md) | `from foundry_sdk.v1.ontologies.models import ApproximateDistinctAggregation` |
**Ontologies** | [ArrayEntryEvaluatedConstraint](docs/v1/Ontologies/models/ArrayEntryEvaluatedConstraint.md) | `from foundry_sdk.v1.ontologies.models import ArrayEntryEvaluatedConstraint` |
**Ontologies** | [ArrayEvaluatedConstraint](docs/v1/Ontologies/models/ArrayEvaluatedConstraint.md) | `from foundry_sdk.v1.ontologies.models import ArrayEvaluatedConstraint` |
**Ontologies** | [ArraySizeConstraint](docs/v1/Ontologies/models/ArraySizeConstraint.md) | `from foundry_sdk.v1.ontologies.models import ArraySizeConstraint` |
**Ontologies** | [ArtifactRepositoryRid](docs/v1/Ontologies/models/ArtifactRepositoryRid.md) | `from foundry_sdk.v1.ontologies.models import ArtifactRepositoryRid` |
**Ontologies** | [Attachment](docs/v1/Ontologies/models/Attachment.md) | `from foundry_sdk.v1.ontologies.models import Attachment` |
**Ontologies** | [AttachmentRid](docs/v1/Ontologies/models/AttachmentRid.md) | `from foundry_sdk.v1.ontologies.models import AttachmentRid` |
**Ontologies** | [AvgAggregation](docs/v1/Ontologies/models/AvgAggregation.md) | `from foundry_sdk.v1.ontologies.models import AvgAggregation` |
**Ontologies** | [BatchApplyActionResponse](docs/v1/Ontologies/models/BatchApplyActionResponse.md) | `from foundry_sdk.v1.ontologies.models import BatchApplyActionResponse` |
**Ontologies** | [ContainsQuery](docs/v1/Ontologies/models/ContainsQuery.md) | `from foundry_sdk.v1.ontologies.models import ContainsQuery` |
**Ontologies** | [CountAggregation](docs/v1/Ontologies/models/CountAggregation.md) | `from foundry_sdk.v1.ontologies.models import CountAggregation` |
**Ontologies** | [CreateInterfaceObjectRule](docs/v1/Ontologies/models/CreateInterfaceObjectRule.md) | `from foundry_sdk.v1.ontologies.models import CreateInterfaceObjectRule` |
**Ontologies** | [CreateLinkRule](docs/v1/Ontologies/models/CreateLinkRule.md) | `from foundry_sdk.v1.ontologies.models import CreateLinkRule` |
**Ontologies** | [CreateObjectRule](docs/v1/Ontologies/models/CreateObjectRule.md) | `from foundry_sdk.v1.ontologies.models import CreateObjectRule` |
**Ontologies** | [DataValue](docs/v1/Ontologies/models/DataValue.md) | `from foundry_sdk.v1.ontologies.models import DataValue` |
**Ontologies** | [DeleteInterfaceObjectRule](docs/v1/Ontologies/models/DeleteInterfaceObjectRule.md) | `from foundry_sdk.v1.ontologies.models import DeleteInterfaceObjectRule` |
**Ontologies** | [DeleteLinkRule](docs/v1/Ontologies/models/DeleteLinkRule.md) | `from foundry_sdk.v1.ontologies.models import DeleteLinkRule` |
**Ontologies** | [DeleteObjectRule](docs/v1/Ontologies/models/DeleteObjectRule.md) | `from foundry_sdk.v1.ontologies.models import DeleteObjectRule` |
**Ontologies** | [DerivedPropertyApiName](docs/v1/Ontologies/models/DerivedPropertyApiName.md) | `from foundry_sdk.v1.ontologies.models import DerivedPropertyApiName` |
**Ontologies** | [Duration](docs/v1/Ontologies/models/Duration.md) | `from foundry_sdk.v1.ontologies.models import Duration` |
**Ontologies** | [EntrySetType](docs/v1/Ontologies/models/EntrySetType.md) | `from foundry_sdk.v1.ontologies.models import EntrySetType` |
**Ontologies** | [EqualsQuery](docs/v1/Ontologies/models/EqualsQuery.md) | `from foundry_sdk.v1.ontologies.models import EqualsQuery` |
**Ontologies** | [ExecuteQueryResponse](docs/v1/Ontologies/models/ExecuteQueryResponse.md) | `from foundry_sdk.v1.ontologies.models import ExecuteQueryResponse` |
**Ontologies** | [FieldNameV1](docs/v1/Ontologies/models/FieldNameV1.md) | `from foundry_sdk.v1.ontologies.models import FieldNameV1` |
**Ontologies** | [FilterValue](docs/v1/Ontologies/models/FilterValue.md) | `from foundry_sdk.v1.ontologies.models import FilterValue` |
**Ontologies** | [FunctionRid](docs/v1/Ontologies/models/FunctionRid.md) | `from foundry_sdk.v1.ontologies.models import FunctionRid` |
**Ontologies** | [FunctionVersion](docs/v1/Ontologies/models/FunctionVersion.md) | `from foundry_sdk.v1.ontologies.models import FunctionVersion` |
**Ontologies** | [Fuzzy](docs/v1/Ontologies/models/Fuzzy.md) | `from foundry_sdk.v1.ontologies.models import Fuzzy` |
**Ontologies** | [GroupMemberConstraint](docs/v1/Ontologies/models/GroupMemberConstraint.md) | `from foundry_sdk.v1.ontologies.models import GroupMemberConstraint` |
**Ontologies** | [GteQuery](docs/v1/Ontologies/models/GteQuery.md) | `from foundry_sdk.v1.ontologies.models import GteQuery` |
**Ontologies** | [GtQuery](docs/v1/Ontologies/models/GtQuery.md) | `from foundry_sdk.v1.ontologies.models import GtQuery` |
**Ontologies** | [InterfaceLinkTypeApiName](docs/v1/Ontologies/models/InterfaceLinkTypeApiName.md) | `from foundry_sdk.v1.ontologies.models import InterfaceLinkTypeApiName` |
**Ontologies** | [InterfaceLinkTypeRid](docs/v1/Ontologies/models/InterfaceLinkTypeRid.md) | `from foundry_sdk.v1.ontologies.models import InterfaceLinkTypeRid` |
**Ontologies** | [InterfaceTypeApiName](docs/v1/Ontologies/models/InterfaceTypeApiName.md) | `from foundry_sdk.v1.ontologies.models import InterfaceTypeApiName` |
**Ontologies** | [InterfaceTypeRid](docs/v1/Ontologies/models/InterfaceTypeRid.md) | `from foundry_sdk.v1.ontologies.models import InterfaceTypeRid` |
**Ontologies** | [IsNullQuery](docs/v1/Ontologies/models/IsNullQuery.md) | `from foundry_sdk.v1.ontologies.models import IsNullQuery` |
**Ontologies** | [LinkTypeApiName](docs/v1/Ontologies/models/LinkTypeApiName.md) | `from foundry_sdk.v1.ontologies.models import LinkTypeApiName` |
**Ontologies** | [LinkTypeId](docs/v1/Ontologies/models/LinkTypeId.md) | `from foundry_sdk.v1.ontologies.models import LinkTypeId` |
**Ontologies** | [LinkTypeSide](docs/v1/Ontologies/models/LinkTypeSide.md) | `from foundry_sdk.v1.ontologies.models import LinkTypeSide` |
**Ontologies** | [LinkTypeSideCardinality](docs/v1/Ontologies/models/LinkTypeSideCardinality.md) | `from foundry_sdk.v1.ontologies.models import LinkTypeSideCardinality` |
**Ontologies** | [ListActionTypesResponse](docs/v1/Ontologies/models/ListActionTypesResponse.md) | `from foundry_sdk.v1.ontologies.models import ListActionTypesResponse` |
**Ontologies** | [ListLinkedObjectsResponse](docs/v1/Ontologies/models/ListLinkedObjectsResponse.md) | `from foundry_sdk.v1.ontologies.models import ListLinkedObjectsResponse` |
**Ontologies** | [ListObjectsResponse](docs/v1/Ontologies/models/ListObjectsResponse.md) | `from foundry_sdk.v1.ontologies.models import ListObjectsResponse` |
**Ontologies** | [ListObjectTypesResponse](docs/v1/Ontologies/models/ListObjectTypesResponse.md) | `from foundry_sdk.v1.ontologies.models import ListObjectTypesResponse` |
**Ontologies** | [ListOntologiesResponse](docs/v1/Ontologies/models/ListOntologiesResponse.md) | `from foundry_sdk.v1.ontologies.models import ListOntologiesResponse` |
**Ontologies** | [ListOutgoingLinkTypesResponse](docs/v1/Ontologies/models/ListOutgoingLinkTypesResponse.md) | `from foundry_sdk.v1.ontologies.models import ListOutgoingLinkTypesResponse` |
**Ontologies** | [ListQueryTypesResponse](docs/v1/Ontologies/models/ListQueryTypesResponse.md) | `from foundry_sdk.v1.ontologies.models import ListQueryTypesResponse` |
**Ontologies** | [LogicRule](docs/v1/Ontologies/models/LogicRule.md) | `from foundry_sdk.v1.ontologies.models import LogicRule` |
**Ontologies** | [LteQuery](docs/v1/Ontologies/models/LteQuery.md) | `from foundry_sdk.v1.ontologies.models import LteQuery` |
**Ontologies** | [LtQuery](docs/v1/Ontologies/models/LtQuery.md) | `from foundry_sdk.v1.ontologies.models import LtQuery` |
**Ontologies** | [MaxAggregation](docs/v1/Ontologies/models/MaxAggregation.md) | `from foundry_sdk.v1.ontologies.models import MaxAggregation` |
**Ontologies** | [MinAggregation](docs/v1/Ontologies/models/MinAggregation.md) | `from foundry_sdk.v1.ontologies.models import MinAggregation` |
**Ontologies** | [ModifyInterfaceObjectRule](docs/v1/Ontologies/models/ModifyInterfaceObjectRule.md) | `from foundry_sdk.v1.ontologies.models import ModifyInterfaceObjectRule` |
**Ontologies** | [ModifyObjectRule](docs/v1/Ontologies/models/ModifyObjectRule.md) | `from foundry_sdk.v1.ontologies.models import ModifyObjectRule` |
**Ontologies** | [NotQuery](docs/v1/Ontologies/models/NotQuery.md) | `from foundry_sdk.v1.ontologies.models import NotQuery` |
**Ontologies** | [ObjectPropertyValueConstraint](docs/v1/Ontologies/models/ObjectPropertyValueConstraint.md) | `from foundry_sdk.v1.ontologies.models import ObjectPropertyValueConstraint` |
**Ontologies** | [ObjectQueryResultConstraint](docs/v1/Ontologies/models/ObjectQueryResultConstraint.md) | `from foundry_sdk.v1.ontologies.models import ObjectQueryResultConstraint` |
**Ontologies** | [ObjectRid](docs/v1/Ontologies/models/ObjectRid.md) | `from foundry_sdk.v1.ontologies.models import ObjectRid` |
**Ontologies** | [ObjectSetRid](docs/v1/Ontologies/models/ObjectSetRid.md) | `from foundry_sdk.v1.ontologies.models import ObjectSetRid` |
**Ontologies** | [ObjectType](docs/v1/Ontologies/models/ObjectType.md) | `from foundry_sdk.v1.ontologies.models import ObjectType` |
**Ontologies** | [ObjectTypeApiName](docs/v1/Ontologies/models/ObjectTypeApiName.md) | `from foundry_sdk.v1.ontologies.models import ObjectTypeApiName` |
**Ontologies** | [ObjectTypeRid](docs/v1/Ontologies/models/ObjectTypeRid.md) | `from foundry_sdk.v1.ontologies.models import ObjectTypeRid` |
**Ontologies** | [ObjectTypeVisibility](docs/v1/Ontologies/models/ObjectTypeVisibility.md) | `from foundry_sdk.v1.ontologies.models import ObjectTypeVisibility` |
**Ontologies** | [OneOfConstraint](docs/v1/Ontologies/models/OneOfConstraint.md) | `from foundry_sdk.v1.ontologies.models import OneOfConstraint` |
**Ontologies** | [Ontology](docs/v1/Ontologies/models/Ontology.md) | `from foundry_sdk.v1.ontologies.models import Ontology` |
**Ontologies** | [OntologyApiName](docs/v1/Ontologies/models/OntologyApiName.md) | `from foundry_sdk.v1.ontologies.models import OntologyApiName` |
**Ontologies** | [OntologyArrayType](docs/v1/Ontologies/models/OntologyArrayType.md) | `from foundry_sdk.v1.ontologies.models import OntologyArrayType` |
**Ontologies** | [OntologyDataType](docs/v1/Ontologies/models/OntologyDataType.md) | `from foundry_sdk.v1.ontologies.models import OntologyDataType` |
**Ontologies** | [OntologyInterfaceObjectSetType](docs/v1/Ontologies/models/OntologyInterfaceObjectSetType.md) | `from foundry_sdk.v1.ontologies.models import OntologyInterfaceObjectSetType` |
**Ontologies** | [OntologyInterfaceObjectType](docs/v1/Ontologies/models/OntologyInterfaceObjectType.md) | `from foundry_sdk.v1.ontologies.models import OntologyInterfaceObjectType` |
**Ontologies** | [OntologyMapType](docs/v1/Ontologies/models/OntologyMapType.md) | `from foundry_sdk.v1.ontologies.models import OntologyMapType` |
**Ontologies** | [OntologyObject](docs/v1/Ontologies/models/OntologyObject.md) | `from foundry_sdk.v1.ontologies.models import OntologyObject` |
**Ontologies** | [OntologyObjectSetType](docs/v1/Ontologies/models/OntologyObjectSetType.md) | `from foundry_sdk.v1.ontologies.models import OntologyObjectSetType` |
**Ontologies** | [OntologyObjectType](docs/v1/Ontologies/models/OntologyObjectType.md) | `from foundry_sdk.v1.ontologies.models import OntologyObjectType` |
**Ontologies** | [OntologyRid](docs/v1/Ontologies/models/OntologyRid.md) | `from foundry_sdk.v1.ontologies.models import OntologyRid` |
**Ontologies** | [OntologySetType](docs/v1/Ontologies/models/OntologySetType.md) | `from foundry_sdk.v1.ontologies.models import OntologySetType` |
**Ontologies** | [OntologyStructField](docs/v1/Ontologies/models/OntologyStructField.md) | `from foundry_sdk.v1.ontologies.models import OntologyStructField` |
**Ontologies** | [OntologyStructType](docs/v1/Ontologies/models/OntologyStructType.md) | `from foundry_sdk.v1.ontologies.models import OntologyStructType` |
**Ontologies** | [OrderBy](docs/v1/Ontologies/models/OrderBy.md) | `from foundry_sdk.v1.ontologies.models import OrderBy` |
**Ontologies** | [OrQuery](docs/v1/Ontologies/models/OrQuery.md) | `from foundry_sdk.v1.ontologies.models import OrQuery` |
**Ontologies** | [Parameter](docs/v1/Ontologies/models/Parameter.md) | `from foundry_sdk.v1.ontologies.models import Parameter` |
**Ontologies** | [ParameterEvaluatedConstraint](docs/v1/Ontologies/models/ParameterEvaluatedConstraint.md) | `from foundry_sdk.v1.ontologies.models import ParameterEvaluatedConstraint` |
**Ontologies** | [ParameterEvaluationResult](docs/v1/Ontologies/models/ParameterEvaluationResult.md) | `from foundry_sdk.v1.ontologies.models import ParameterEvaluationResult` |
**Ontologies** | [ParameterId](docs/v1/Ontologies/models/ParameterId.md) | `from foundry_sdk.v1.ontologies.models import ParameterId` |
**Ontologies** | [ParameterOption](docs/v1/Ontologies/models/ParameterOption.md) | `from foundry_sdk.v1.ontologies.models import ParameterOption` |
**Ontologies** | [PhraseQuery](docs/v1/Ontologies/models/PhraseQuery.md) | `from foundry_sdk.v1.ontologies.models import PhraseQuery` |
**Ontologies** | [PrefixQuery](docs/v1/Ontologies/models/PrefixQuery.md) | `from foundry_sdk.v1.ontologies.models import PrefixQuery` |
**Ontologies** | [PrimaryKeyValue](docs/v1/Ontologies/models/PrimaryKeyValue.md) | `from foundry_sdk.v1.ontologies.models import PrimaryKeyValue` |
**Ontologies** | [Property](docs/v1/Ontologies/models/Property.md) | `from foundry_sdk.v1.ontologies.models import Property` |
**Ontologies** | [PropertyApiName](docs/v1/Ontologies/models/PropertyApiName.md) | `from foundry_sdk.v1.ontologies.models import PropertyApiName` |
**Ontologies** | [PropertyFilter](docs/v1/Ontologies/models/PropertyFilter.md) | `from foundry_sdk.v1.ontologies.models import PropertyFilter` |
**Ontologies** | [PropertyId](docs/v1/Ontologies/models/PropertyId.md) | `from foundry_sdk.v1.ontologies.models import PropertyId` |
**Ontologies** | [PropertyTypeRid](docs/v1/Ontologies/models/PropertyTypeRid.md) | `from foundry_sdk.v1.ontologies.models import PropertyTypeRid` |
**Ontologies** | [PropertyValue](docs/v1/Ontologies/models/PropertyValue.md) | `from foundry_sdk.v1.ontologies.models import PropertyValue` |
**Ontologies** | [PropertyValueEscapedString](docs/v1/Ontologies/models/PropertyValueEscapedString.md) | `from foundry_sdk.v1.ontologies.models import PropertyValueEscapedString` |
**Ontologies** | [QueryAggregationKeyType](docs/v1/Ontologies/models/QueryAggregationKeyType.md) | `from foundry_sdk.v1.ontologies.models import QueryAggregationKeyType` |
**Ontologies** | [QueryAggregationRangeSubType](docs/v1/Ontologies/models/QueryAggregationRangeSubType.md) | `from foundry_sdk.v1.ontologies.models import QueryAggregationRangeSubType` |
**Ontologies** | [QueryAggregationRangeType](docs/v1/Ontologies/models/QueryAggregationRangeType.md) | `from foundry_sdk.v1.ontologies.models import QueryAggregationRangeType` |
**Ontologies** | [QueryAggregationValueType](docs/v1/Ontologies/models/QueryAggregationValueType.md) | `from foundry_sdk.v1.ontologies.models import QueryAggregationValueType` |
**Ontologies** | [QueryApiName](docs/v1/Ontologies/models/QueryApiName.md) | `from foundry_sdk.v1.ontologies.models import QueryApiName` |
**Ontologies** | [QueryArrayType](docs/v1/Ontologies/models/QueryArrayType.md) | `from foundry_sdk.v1.ontologies.models import QueryArrayType` |
**Ontologies** | [QueryDataType](docs/v1/Ontologies/models/QueryDataType.md) | `from foundry_sdk.v1.ontologies.models import QueryDataType` |
**Ontologies** | [QueryRuntimeErrorParameter](docs/v1/Ontologies/models/QueryRuntimeErrorParameter.md) | `from foundry_sdk.v1.ontologies.models import QueryRuntimeErrorParameter` |
**Ontologies** | [QuerySetType](docs/v1/Ontologies/models/QuerySetType.md) | `from foundry_sdk.v1.ontologies.models import QuerySetType` |
**Ontologies** | [QueryStructField](docs/v1/Ontologies/models/QueryStructField.md) | `from foundry_sdk.v1.ontologies.models import QueryStructField` |
**Ontologies** | [QueryStructType](docs/v1/Ontologies/models/QueryStructType.md) | `from foundry_sdk.v1.ontologies.models import QueryStructType` |
**Ontologies** | [QueryType](docs/v1/Ontologies/models/QueryType.md) | `from foundry_sdk.v1.ontologies.models import QueryType` |
**Ontologies** | [QueryUnionType](docs/v1/Ontologies/models/QueryUnionType.md) | `from foundry_sdk.v1.ontologies.models import QueryUnionType` |
**Ontologies** | [RangeConstraint](docs/v1/Ontologies/models/RangeConstraint.md) | `from foundry_sdk.v1.ontologies.models import RangeConstraint` |
**Ontologies** | [ReturnEditsMode](docs/v1/Ontologies/models/ReturnEditsMode.md) | `from foundry_sdk.v1.ontologies.models import ReturnEditsMode` |
**Ontologies** | [SdkPackageName](docs/v1/Ontologies/models/SdkPackageName.md) | `from foundry_sdk.v1.ontologies.models import SdkPackageName` |
**Ontologies** | [SdkPackageRid](docs/v1/Ontologies/models/SdkPackageRid.md) | `from foundry_sdk.v1.ontologies.models import SdkPackageRid` |
**Ontologies** | [SdkVersion](docs/v1/Ontologies/models/SdkVersion.md) | `from foundry_sdk.v1.ontologies.models import SdkVersion` |
**Ontologies** | [SearchJsonQuery](docs/v1/Ontologies/models/SearchJsonQuery.md) | `from foundry_sdk.v1.ontologies.models import SearchJsonQuery` |
**Ontologies** | [SearchObjectsResponse](docs/v1/Ontologies/models/SearchObjectsResponse.md) | `from foundry_sdk.v1.ontologies.models import SearchObjectsResponse` |
**Ontologies** | [SearchOrderBy](docs/v1/Ontologies/models/SearchOrderBy.md) | `from foundry_sdk.v1.ontologies.models import SearchOrderBy` |
**Ontologies** | [SearchOrderByType](docs/v1/Ontologies/models/SearchOrderByType.md) | `from foundry_sdk.v1.ontologies.models import SearchOrderByType` |
**Ontologies** | [SearchOrdering](docs/v1/Ontologies/models/SearchOrdering.md) | `from foundry_sdk.v1.ontologies.models import SearchOrdering` |
**Ontologies** | [SelectedPropertyApiName](docs/v1/Ontologies/models/SelectedPropertyApiName.md) | `from foundry_sdk.v1.ontologies.models import SelectedPropertyApiName` |
**Ontologies** | [SharedPropertyTypeApiName](docs/v1/Ontologies/models/SharedPropertyTypeApiName.md) | `from foundry_sdk.v1.ontologies.models import SharedPropertyTypeApiName` |
**Ontologies** | [SharedPropertyTypeRid](docs/v1/Ontologies/models/SharedPropertyTypeRid.md) | `from foundry_sdk.v1.ontologies.models import SharedPropertyTypeRid` |
**Ontologies** | [StringLengthConstraint](docs/v1/Ontologies/models/StringLengthConstraint.md) | `from foundry_sdk.v1.ontologies.models import StringLengthConstraint` |
**Ontologies** | [StringRegexMatchConstraint](docs/v1/Ontologies/models/StringRegexMatchConstraint.md) | `from foundry_sdk.v1.ontologies.models import StringRegexMatchConstraint` |
**Ontologies** | [StructEvaluatedConstraint](docs/v1/Ontologies/models/StructEvaluatedConstraint.md) | `from foundry_sdk.v1.ontologies.models import StructEvaluatedConstraint` |
**Ontologies** | [StructFieldEvaluatedConstraint](docs/v1/Ontologies/models/StructFieldEvaluatedConstraint.md) | `from foundry_sdk.v1.ontologies.models import StructFieldEvaluatedConstraint` |
**Ontologies** | [StructFieldEvaluationResult](docs/v1/Ontologies/models/StructFieldEvaluationResult.md) | `from foundry_sdk.v1.ontologies.models import StructFieldEvaluationResult` |
**Ontologies** | [StructParameterFieldApiName](docs/v1/Ontologies/models/StructParameterFieldApiName.md) | `from foundry_sdk.v1.ontologies.models import StructParameterFieldApiName` |
**Ontologies** | [SubmissionCriteriaEvaluation](docs/v1/Ontologies/models/SubmissionCriteriaEvaluation.md) | `from foundry_sdk.v1.ontologies.models import SubmissionCriteriaEvaluation` |
**Ontologies** | [SumAggregation](docs/v1/Ontologies/models/SumAggregation.md) | `from foundry_sdk.v1.ontologies.models import SumAggregation` |
**Ontologies** | [ThreeDimensionalAggregation](docs/v1/Ontologies/models/ThreeDimensionalAggregation.md) | `from foundry_sdk.v1.ontologies.models import ThreeDimensionalAggregation` |
**Ontologies** | [TwoDimensionalAggregation](docs/v1/Ontologies/models/TwoDimensionalAggregation.md) | `from foundry_sdk.v1.ontologies.models import TwoDimensionalAggregation` |
**Ontologies** | [UnevaluableConstraint](docs/v1/Ontologies/models/UnevaluableConstraint.md) | `from foundry_sdk.v1.ontologies.models import UnevaluableConstraint` |
**Ontologies** | [ValidateActionResponse](docs/v1/Ontologies/models/ValidateActionResponse.md) | `from foundry_sdk.v1.ontologies.models import ValidateActionResponse` |
**Ontologies** | [ValidationResult](docs/v1/Ontologies/models/ValidationResult.md) | `from foundry_sdk.v1.ontologies.models import ValidationResult` |
**Ontologies** | [ValueType](docs/v1/Ontologies/models/ValueType.md) | `from foundry_sdk.v1.ontologies.models import ValueType` |
**Ontologies** | [ValueTypeApiName](docs/v1/Ontologies/models/ValueTypeApiName.md) | `from foundry_sdk.v1.ontologies.models import ValueTypeApiName` |
**Ontologies** | [ValueTypeRid](docs/v1/Ontologies/models/ValueTypeRid.md) | `from foundry_sdk.v1.ontologies.models import ValueTypeRid` |


<a id="all-errors"></a>
## Documentation for errors
<a id="errors-v2-link"></a>
## Documentation for V2 errors

Namespace | Name | Import |
--------- | ---- | ------ |
**Admin** | AddEnrollmentRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import AddEnrollmentRoleAssignmentsPermissionDenied` |
**Admin** | AddGroupMembersPermissionDenied | `from foundry_sdk.v2.admin.errors import AddGroupMembersPermissionDenied` |
**Admin** | AddMarkingMembersPermissionDenied | `from foundry_sdk.v2.admin.errors import AddMarkingMembersPermissionDenied` |
**Admin** | AddMarkingRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import AddMarkingRoleAssignmentsPermissionDenied` |
**Admin** | AddOrganizationRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import AddOrganizationRoleAssignmentsPermissionDenied` |
**Admin** | AuthenticationProviderNotFound | `from foundry_sdk.v2.admin.errors import AuthenticationProviderNotFound` |
**Admin** | CannotReplaceProviderInfoForPrincipalInProtectedRealm | `from foundry_sdk.v2.admin.errors import CannotReplaceProviderInfoForPrincipalInProtectedRealm` |
**Admin** | CreateGroupPermissionDenied | `from foundry_sdk.v2.admin.errors import CreateGroupPermissionDenied` |
**Admin** | CreateMarkingMissingInitialAdminRole | `from foundry_sdk.v2.admin.errors import CreateMarkingMissingInitialAdminRole` |
**Admin** | CreateMarkingPermissionDenied | `from foundry_sdk.v2.admin.errors import CreateMarkingPermissionDenied` |
**Admin** | CreateOrganizationMissingInitialAdminRole | `from foundry_sdk.v2.admin.errors import CreateOrganizationMissingInitialAdminRole` |
**Admin** | CreateOrganizationPermissionDenied | `from foundry_sdk.v2.admin.errors import CreateOrganizationPermissionDenied` |
**Admin** | DeleteGroupPermissionDenied | `from foundry_sdk.v2.admin.errors import DeleteGroupPermissionDenied` |
**Admin** | DeleteUserPermissionDenied | `from foundry_sdk.v2.admin.errors import DeleteUserPermissionDenied` |
**Admin** | EnrollmentNotFound | `from foundry_sdk.v2.admin.errors import EnrollmentNotFound` |
**Admin** | EnrollmentRoleNotFound | `from foundry_sdk.v2.admin.errors import EnrollmentRoleNotFound` |
**Admin** | GetCurrentEnrollmentPermissionDenied | `from foundry_sdk.v2.admin.errors import GetCurrentEnrollmentPermissionDenied` |
**Admin** | GetCurrentUserPermissionDenied | `from foundry_sdk.v2.admin.errors import GetCurrentUserPermissionDenied` |
**Admin** | GetGroupProviderInfoPermissionDenied | `from foundry_sdk.v2.admin.errors import GetGroupProviderInfoPermissionDenied` |
**Admin** | GetMarkingCategoryPermissionDenied | `from foundry_sdk.v2.admin.errors import GetMarkingCategoryPermissionDenied` |
**Admin** | GetMarkingPermissionDenied | `from foundry_sdk.v2.admin.errors import GetMarkingPermissionDenied` |
**Admin** | GetMarkingsUserPermissionDenied | `from foundry_sdk.v2.admin.errors import GetMarkingsUserPermissionDenied` |
**Admin** | GetProfilePictureOfUserPermissionDenied | `from foundry_sdk.v2.admin.errors import GetProfilePictureOfUserPermissionDenied` |
**Admin** | GetUserProviderInfoPermissionDenied | `from foundry_sdk.v2.admin.errors import GetUserProviderInfoPermissionDenied` |
**Admin** | GroupMembershipExpirationPolicyNotFound | `from foundry_sdk.v2.admin.errors import GroupMembershipExpirationPolicyNotFound` |
**Admin** | GroupNameAlreadyExists | `from foundry_sdk.v2.admin.errors import GroupNameAlreadyExists` |
**Admin** | GroupNotFound | `from foundry_sdk.v2.admin.errors import GroupNotFound` |
**Admin** | GroupProviderInfoNotFound | `from foundry_sdk.v2.admin.errors import GroupProviderInfoNotFound` |
**Admin** | InvalidGroupMembershipExpiration | `from foundry_sdk.v2.admin.errors import InvalidGroupMembershipExpiration` |
**Admin** | InvalidGroupOrganizations | `from foundry_sdk.v2.admin.errors import InvalidGroupOrganizations` |
**Admin** | InvalidHostName | `from foundry_sdk.v2.admin.errors import InvalidHostName` |
**Admin** | InvalidProfilePicture | `from foundry_sdk.v2.admin.errors import InvalidProfilePicture` |
**Admin** | ListAvailableRolesOrganizationPermissionDenied | `from foundry_sdk.v2.admin.errors import ListAvailableRolesOrganizationPermissionDenied` |
**Admin** | ListEnrollmentRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import ListEnrollmentRoleAssignmentsPermissionDenied` |
**Admin** | ListHostsPermissionDenied | `from foundry_sdk.v2.admin.errors import ListHostsPermissionDenied` |
**Admin** | ListMarkingMembersPermissionDenied | `from foundry_sdk.v2.admin.errors import ListMarkingMembersPermissionDenied` |
**Admin** | ListMarkingRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import ListMarkingRoleAssignmentsPermissionDenied` |
**Admin** | ListOrganizationRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import ListOrganizationRoleAssignmentsPermissionDenied` |
**Admin** | MarkingCategoryNotFound | `from foundry_sdk.v2.admin.errors import MarkingCategoryNotFound` |
**Admin** | MarkingNameInCategoryAlreadyExists | `from foundry_sdk.v2.admin.errors import MarkingNameInCategoryAlreadyExists` |
**Admin** | MarkingNameIsEmpty | `from foundry_sdk.v2.admin.errors import MarkingNameIsEmpty` |
**Admin** | MarkingNotFound | `from foundry_sdk.v2.admin.errors import MarkingNotFound` |
**Admin** | OrganizationNameAlreadyExists | `from foundry_sdk.v2.admin.errors import OrganizationNameAlreadyExists` |
**Admin** | OrganizationNotFound | `from foundry_sdk.v2.admin.errors import OrganizationNotFound` |
**Admin** | PreregisterGroupPermissionDenied | `from foundry_sdk.v2.admin.errors import PreregisterGroupPermissionDenied` |
**Admin** | PreregisterUserPermissionDenied | `from foundry_sdk.v2.admin.errors import PreregisterUserPermissionDenied` |
**Admin** | PrincipalNotFound | `from foundry_sdk.v2.admin.errors import PrincipalNotFound` |
**Admin** | ProfilePictureNotFound | `from foundry_sdk.v2.admin.errors import ProfilePictureNotFound` |
**Admin** | RemoveEnrollmentRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import RemoveEnrollmentRoleAssignmentsPermissionDenied` |
**Admin** | RemoveGroupMembersPermissionDenied | `from foundry_sdk.v2.admin.errors import RemoveGroupMembersPermissionDenied` |
**Admin** | RemoveMarkingMembersPermissionDenied | `from foundry_sdk.v2.admin.errors import RemoveMarkingMembersPermissionDenied` |
**Admin** | RemoveMarkingRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import RemoveMarkingRoleAssignmentsPermissionDenied` |
**Admin** | RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed | `from foundry_sdk.v2.admin.errors import RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed` |
**Admin** | RemoveOrganizationRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import RemoveOrganizationRoleAssignmentsPermissionDenied` |
**Admin** | ReplaceGroupMembershipExpirationPolicyPermissionDenied | `from foundry_sdk.v2.admin.errors import ReplaceGroupMembershipExpirationPolicyPermissionDenied` |
**Admin** | ReplaceGroupProviderInfoPermissionDenied | `from foundry_sdk.v2.admin.errors import ReplaceGroupProviderInfoPermissionDenied` |
**Admin** | ReplaceMarkingPermissionDenied | `from foundry_sdk.v2.admin.errors import ReplaceMarkingPermissionDenied` |
**Admin** | ReplaceOrganizationPermissionDenied | `from foundry_sdk.v2.admin.errors import ReplaceOrganizationPermissionDenied` |
**Admin** | ReplaceUserProviderInfoPermissionDenied | `from foundry_sdk.v2.admin.errors import ReplaceUserProviderInfoPermissionDenied` |
**Admin** | RevokeAllTokensUserPermissionDenied | `from foundry_sdk.v2.admin.errors import RevokeAllTokensUserPermissionDenied` |
**Admin** | RoleNotFound | `from foundry_sdk.v2.admin.errors import RoleNotFound` |
**Admin** | SearchGroupsPermissionDenied | `from foundry_sdk.v2.admin.errors import SearchGroupsPermissionDenied` |
**Admin** | SearchUsersPermissionDenied | `from foundry_sdk.v2.admin.errors import SearchUsersPermissionDenied` |
**Admin** | UserNotFound | `from foundry_sdk.v2.admin.errors import UserNotFound` |
**Admin** | UserProviderInfoNotFound | `from foundry_sdk.v2.admin.errors import UserProviderInfoNotFound` |
**AipAgents** | AgentIterationsExceededLimit | `from foundry_sdk.v2.aip_agents.errors import AgentIterationsExceededLimit` |
**AipAgents** | AgentNotFound | `from foundry_sdk.v2.aip_agents.errors import AgentNotFound` |
**AipAgents** | AgentVersionNotFound | `from foundry_sdk.v2.aip_agents.errors import AgentVersionNotFound` |
**AipAgents** | BlockingContinueSessionPermissionDenied | `from foundry_sdk.v2.aip_agents.errors import BlockingContinueSessionPermissionDenied` |
**AipAgents** | CancelSessionFailedMessageNotInProgress | `from foundry_sdk.v2.aip_agents.errors import CancelSessionFailedMessageNotInProgress` |
**AipAgents** | CancelSessionPermissionDenied | `from foundry_sdk.v2.aip_agents.errors import CancelSessionPermissionDenied` |
**AipAgents** | ContentNotFound | `from foundry_sdk.v2.aip_agents.errors import ContentNotFound` |
**AipAgents** | ContextSizeExceededLimit | `from foundry_sdk.v2.aip_agents.errors import ContextSizeExceededLimit` |
**AipAgents** | CreateSessionPermissionDenied | `from foundry_sdk.v2.aip_agents.errors import CreateSessionPermissionDenied` |
**AipAgents** | FunctionLocatorNotFound | `from foundry_sdk.v2.aip_agents.errors import FunctionLocatorNotFound` |
**AipAgents** | GetAllSessionsAgentsPermissionDenied | `from foundry_sdk.v2.aip_agents.errors import GetAllSessionsAgentsPermissionDenied` |
**AipAgents** | GetRagContextForSessionPermissionDenied | `from foundry_sdk.v2.aip_agents.errors import GetRagContextForSessionPermissionDenied` |
**AipAgents** | InvalidAgentVersion | `from foundry_sdk.v2.aip_agents.errors import InvalidAgentVersion` |
**AipAgents** | InvalidParameter | `from foundry_sdk.v2.aip_agents.errors import InvalidParameter` |
**AipAgents** | InvalidParameterType | `from foundry_sdk.v2.aip_agents.errors import InvalidParameterType` |
**AipAgents** | ListSessionsForAgentsPermissionDenied | `from foundry_sdk.v2.aip_agents.errors import ListSessionsForAgentsPermissionDenied` |
**AipAgents** | NoPublishedAgentVersion | `from foundry_sdk.v2.aip_agents.errors import NoPublishedAgentVersion` |
**AipAgents** | ObjectTypeIdsNotFound | `from foundry_sdk.v2.aip_agents.errors import ObjectTypeIdsNotFound` |
**AipAgents** | ObjectTypeRidsNotFound | `from foundry_sdk.v2.aip_agents.errors import ObjectTypeRidsNotFound` |
**AipAgents** | OntologyEntitiesNotFound | `from foundry_sdk.v2.aip_agents.errors import OntologyEntitiesNotFound` |
**AipAgents** | RateLimitExceeded | `from foundry_sdk.v2.aip_agents.errors import RateLimitExceeded` |
**AipAgents** | SessionExecutionFailed | `from foundry_sdk.v2.aip_agents.errors import SessionExecutionFailed` |
**AipAgents** | SessionNotFound | `from foundry_sdk.v2.aip_agents.errors import SessionNotFound` |
**AipAgents** | SessionTraceIdAlreadyExists | `from foundry_sdk.v2.aip_agents.errors import SessionTraceIdAlreadyExists` |
**AipAgents** | SessionTraceNotFound | `from foundry_sdk.v2.aip_agents.errors import SessionTraceNotFound` |
**AipAgents** | StreamingContinueSessionPermissionDenied | `from foundry_sdk.v2.aip_agents.errors import StreamingContinueSessionPermissionDenied` |
**AipAgents** | UpdateSessionTitlePermissionDenied | `from foundry_sdk.v2.aip_agents.errors import UpdateSessionTitlePermissionDenied` |
**Connectivity** | AdditionalSecretsMustBeSpecifiedAsPlaintextValueMap | `from foundry_sdk.v2.connectivity.errors import AdditionalSecretsMustBeSpecifiedAsPlaintextValueMap` |
**Connectivity** | ConnectionDetailsNotDetermined | `from foundry_sdk.v2.connectivity.errors import ConnectionDetailsNotDetermined` |
**Connectivity** | ConnectionNotFound | `from foundry_sdk.v2.connectivity.errors import ConnectionNotFound` |
**Connectivity** | ConnectionTypeNotSupported | `from foundry_sdk.v2.connectivity.errors import ConnectionTypeNotSupported` |
**Connectivity** | CreateConnectionPermissionDenied | `from foundry_sdk.v2.connectivity.errors import CreateConnectionPermissionDenied` |
**Connectivity** | CreateFileImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import CreateFileImportPermissionDenied` |
**Connectivity** | CreateTableImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import CreateTableImportPermissionDenied` |
**Connectivity** | DeleteFileImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import DeleteFileImportPermissionDenied` |
**Connectivity** | DeleteTableImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import DeleteTableImportPermissionDenied` |
**Connectivity** | DomainMustUseHttpsWithAuthentication | `from foundry_sdk.v2.connectivity.errors import DomainMustUseHttpsWithAuthentication` |
**Connectivity** | EncryptedPropertyMustBeSpecifiedAsPlaintextValue | `from foundry_sdk.v2.connectivity.errors import EncryptedPropertyMustBeSpecifiedAsPlaintextValue` |
**Connectivity** | ExecuteFileImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import ExecuteFileImportPermissionDenied` |
**Connectivity** | ExecuteTableImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import ExecuteTableImportPermissionDenied` |
**Connectivity** | FileAtLeastCountFilterInvalidMinCount | `from foundry_sdk.v2.connectivity.errors import FileAtLeastCountFilterInvalidMinCount` |
**Connectivity** | FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports | `from foundry_sdk.v2.connectivity.errors import FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports` |
**Connectivity** | FileImportNotFound | `from foundry_sdk.v2.connectivity.errors import FileImportNotFound` |
**Connectivity** | FileImportNotSupportedForConnection | `from foundry_sdk.v2.connectivity.errors import FileImportNotSupportedForConnection` |
**Connectivity** | FilesCountLimitFilterInvalidLimit | `from foundry_sdk.v2.connectivity.errors import FilesCountLimitFilterInvalidLimit` |
**Connectivity** | FileSizeFilterGreaterThanCannotBeNegative | `from foundry_sdk.v2.connectivity.errors import FileSizeFilterGreaterThanCannotBeNegative` |
**Connectivity** | FileSizeFilterInvalidGreaterThanAndLessThanRange | `from foundry_sdk.v2.connectivity.errors import FileSizeFilterInvalidGreaterThanAndLessThanRange` |
**Connectivity** | FileSizeFilterLessThanMustBeOneByteOrLarger | `from foundry_sdk.v2.connectivity.errors import FileSizeFilterLessThanMustBeOneByteOrLarger` |
**Connectivity** | FileSizeFilterMissingGreaterThanAndLessThan | `from foundry_sdk.v2.connectivity.errors import FileSizeFilterMissingGreaterThanAndLessThan` |
**Connectivity** | GetConfigurationPermissionDenied | `from foundry_sdk.v2.connectivity.errors import GetConfigurationPermissionDenied` |
**Connectivity** | HostNameCannotHaveProtocolOrPort | `from foundry_sdk.v2.connectivity.errors import HostNameCannotHaveProtocolOrPort` |
**Connectivity** | ParentFolderNotFoundForConnection | `from foundry_sdk.v2.connectivity.errors import ParentFolderNotFoundForConnection` |
**Connectivity** | PropertyCannotBeBlank | `from foundry_sdk.v2.connectivity.errors import PropertyCannotBeBlank` |
**Connectivity** | PropertyCannotBeEmpty | `from foundry_sdk.v2.connectivity.errors import PropertyCannotBeEmpty` |
**Connectivity** | ReplaceFileImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import ReplaceFileImportPermissionDenied` |
**Connectivity** | ReplaceTableImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import ReplaceTableImportPermissionDenied` |
**Connectivity** | SecretNamesDoNotExist | `from foundry_sdk.v2.connectivity.errors import SecretNamesDoNotExist` |
**Connectivity** | TableImportNotFound | `from foundry_sdk.v2.connectivity.errors import TableImportNotFound` |
**Connectivity** | TableImportNotSupportedForConnection | `from foundry_sdk.v2.connectivity.errors import TableImportNotSupportedForConnection` |
**Connectivity** | TableImportTypeNotSupported | `from foundry_sdk.v2.connectivity.errors import TableImportTypeNotSupported` |
**Connectivity** | UpdateExportSettingsForConnectionPermissionDenied | `from foundry_sdk.v2.connectivity.errors import UpdateExportSettingsForConnectionPermissionDenied` |
**Connectivity** | UpdateSecretsForConnectionPermissionDenied | `from foundry_sdk.v2.connectivity.errors import UpdateSecretsForConnectionPermissionDenied` |
**Core** | ApiFeaturePreviewUsageOnly | `from foundry_sdk.v2.core.errors import ApiFeaturePreviewUsageOnly` |
**Core** | ApiUsageDenied | `from foundry_sdk.v2.core.errors import ApiUsageDenied` |
**Core** | BatchRequestSizeExceededLimit | `from foundry_sdk.v2.core.errors import BatchRequestSizeExceededLimit` |
**Core** | FolderNotFound | `from foundry_sdk.v2.core.errors import FolderNotFound` |
**Core** | FoundryBranchNotFound | `from foundry_sdk.v2.core.errors import FoundryBranchNotFound` |
**Core** | InvalidAndFilter | `from foundry_sdk.v2.core.errors import InvalidAndFilter` |
**Core** | InvalidChangeDataCaptureConfiguration | `from foundry_sdk.v2.core.errors import InvalidChangeDataCaptureConfiguration` |
**Core** | InvalidFieldSchema | `from foundry_sdk.v2.core.errors import InvalidFieldSchema` |
**Core** | InvalidFilterValue | `from foundry_sdk.v2.core.errors import InvalidFilterValue` |
**Core** | InvalidOrFilter | `from foundry_sdk.v2.core.errors import InvalidOrFilter` |
**Core** | InvalidPageSize | `from foundry_sdk.v2.core.errors import InvalidPageSize` |
**Core** | InvalidPageToken | `from foundry_sdk.v2.core.errors import InvalidPageToken` |
**Core** | InvalidParameterCombination | `from foundry_sdk.v2.core.errors import InvalidParameterCombination` |
**Core** | InvalidSchema | `from foundry_sdk.v2.core.errors import InvalidSchema` |
**Core** | InvalidTimeZone | `from foundry_sdk.v2.core.errors import InvalidTimeZone` |
**Core** | MissingBatchRequest | `from foundry_sdk.v2.core.errors import MissingBatchRequest` |
**Core** | MissingPostBody | `from foundry_sdk.v2.core.errors import MissingPostBody` |
**Core** | ResourceNameAlreadyExists | `from foundry_sdk.v2.core.errors import ResourceNameAlreadyExists` |
**Core** | SchemaIsNotStreamSchema | `from foundry_sdk.v2.core.errors import SchemaIsNotStreamSchema` |
**Core** | UnknownDistanceUnit | `from foundry_sdk.v2.core.errors import UnknownDistanceUnit` |
**Datasets** | AbortTransactionPermissionDenied | `from foundry_sdk.v2.datasets.errors import AbortTransactionPermissionDenied` |
**Datasets** | AddBackingDatasetsPermissionDenied | `from foundry_sdk.v2.datasets.errors import AddBackingDatasetsPermissionDenied` |
**Datasets** | AddPrimaryKeyPermissionDenied | `from foundry_sdk.v2.datasets.errors import AddPrimaryKeyPermissionDenied` |
**Datasets** | BranchAlreadyExists | `from foundry_sdk.v2.datasets.errors import BranchAlreadyExists` |
**Datasets** | BranchNotFound | `from foundry_sdk.v2.datasets.errors import BranchNotFound` |
**Datasets** | BuildTransactionPermissionDenied | `from foundry_sdk.v2.datasets.errors import BuildTransactionPermissionDenied` |
**Datasets** | ColumnTypesNotSupported | `from foundry_sdk.v2.datasets.errors import ColumnTypesNotSupported` |
**Datasets** | CommitTransactionPermissionDenied | `from foundry_sdk.v2.datasets.errors import CommitTransactionPermissionDenied` |
**Datasets** | CreateBranchPermissionDenied | `from foundry_sdk.v2.datasets.errors import CreateBranchPermissionDenied` |
**Datasets** | CreateDatasetPermissionDenied | `from foundry_sdk.v2.datasets.errors import CreateDatasetPermissionDenied` |
**Datasets** | CreateTransactionPermissionDenied | `from foundry_sdk.v2.datasets.errors import CreateTransactionPermissionDenied` |
**Datasets** | CreateViewPermissionDenied | `from foundry_sdk.v2.datasets.errors import CreateViewPermissionDenied` |
**Datasets** | DatasetNotFound | `from foundry_sdk.v2.datasets.errors import DatasetNotFound` |
**Datasets** | DatasetReadNotSupported | `from foundry_sdk.v2.datasets.errors import DatasetReadNotSupported` |
**Datasets** | DatasetViewNotFound | `from foundry_sdk.v2.datasets.errors import DatasetViewNotFound` |
**Datasets** | DeleteBranchPermissionDenied | `from foundry_sdk.v2.datasets.errors import DeleteBranchPermissionDenied` |
**Datasets** | DeleteFilePermissionDenied | `from foundry_sdk.v2.datasets.errors import DeleteFilePermissionDenied` |
**Datasets** | DeleteSchemaPermissionDenied | `from foundry_sdk.v2.datasets.errors import DeleteSchemaPermissionDenied` |
**Datasets** | FileAlreadyExists | `from foundry_sdk.v2.datasets.errors import FileAlreadyExists` |
**Datasets** | FileNotFound | `from foundry_sdk.v2.datasets.errors import FileNotFound` |
**Datasets** | FileNotFoundOnBranch | `from foundry_sdk.v2.datasets.errors import FileNotFoundOnBranch` |
**Datasets** | FileNotFoundOnTransactionRange | `from foundry_sdk.v2.datasets.errors import FileNotFoundOnTransactionRange` |
**Datasets** | GetBranchTransactionHistoryPermissionDenied | `from foundry_sdk.v2.datasets.errors import GetBranchTransactionHistoryPermissionDenied` |
**Datasets** | GetDatasetSchedulesPermissionDenied | `from foundry_sdk.v2.datasets.errors import GetDatasetSchedulesPermissionDenied` |
**Datasets** | GetDatasetSchemaPermissionDenied | `from foundry_sdk.v2.datasets.errors import GetDatasetSchemaPermissionDenied` |
**Datasets** | GetFileContentPermissionDenied | `from foundry_sdk.v2.datasets.errors import GetFileContentPermissionDenied` |
**Datasets** | InputBackingDatasetNotInOutputViewProject | `from foundry_sdk.v2.datasets.errors import InputBackingDatasetNotInOutputViewProject` |
**Datasets** | InvalidBranchName | `from foundry_sdk.v2.datasets.errors import InvalidBranchName` |
**Datasets** | InvalidTransactionType | `from foundry_sdk.v2.datasets.errors import InvalidTransactionType` |
**Datasets** | InvalidViewBackingDataset | `from foundry_sdk.v2.datasets.errors import InvalidViewBackingDataset` |
**Datasets** | JobTransactionPermissionDenied | `from foundry_sdk.v2.datasets.errors import JobTransactionPermissionDenied` |
**Datasets** | OpenTransactionAlreadyExists | `from foundry_sdk.v2.datasets.errors import OpenTransactionAlreadyExists` |
**Datasets** | PutDatasetSchemaPermissionDenied | `from foundry_sdk.v2.datasets.errors import PutDatasetSchemaPermissionDenied` |
**Datasets** | PutSchemaPermissionDenied | `from foundry_sdk.v2.datasets.errors import PutSchemaPermissionDenied` |
**Datasets** | ReadTableDatasetPermissionDenied | `from foundry_sdk.v2.datasets.errors import ReadTableDatasetPermissionDenied` |
**Datasets** | ReadTableError | `from foundry_sdk.v2.datasets.errors import ReadTableError` |
**Datasets** | ReadTableRowLimitExceeded | `from foundry_sdk.v2.datasets.errors import ReadTableRowLimitExceeded` |
**Datasets** | ReadTableTimeout | `from foundry_sdk.v2.datasets.errors import ReadTableTimeout` |
**Datasets** | RemoveBackingDatasetsPermissionDenied | `from foundry_sdk.v2.datasets.errors import RemoveBackingDatasetsPermissionDenied` |
**Datasets** | ReplaceBackingDatasetsPermissionDenied | `from foundry_sdk.v2.datasets.errors import ReplaceBackingDatasetsPermissionDenied` |
**Datasets** | SchemaNotFound | `from foundry_sdk.v2.datasets.errors import SchemaNotFound` |
**Datasets** | TransactionNotCommitted | `from foundry_sdk.v2.datasets.errors import TransactionNotCommitted` |
**Datasets** | TransactionNotFound | `from foundry_sdk.v2.datasets.errors import TransactionNotFound` |
**Datasets** | TransactionNotOpen | `from foundry_sdk.v2.datasets.errors import TransactionNotOpen` |
**Datasets** | UploadFilePermissionDenied | `from foundry_sdk.v2.datasets.errors import UploadFilePermissionDenied` |
**Datasets** | ViewDatasetCleanupFailed | `from foundry_sdk.v2.datasets.errors import ViewDatasetCleanupFailed` |
**Datasets** | ViewNotFound | `from foundry_sdk.v2.datasets.errors import ViewNotFound` |
**Datasets** | ViewPrimaryKeyCannotBeModified | `from foundry_sdk.v2.datasets.errors import ViewPrimaryKeyCannotBeModified` |
**Datasets** | ViewPrimaryKeyMustContainAtLeastOneColumn | `from foundry_sdk.v2.datasets.errors import ViewPrimaryKeyMustContainAtLeastOneColumn` |
**Datasets** | ViewPrimaryKeyRequiresBackingDatasets | `from foundry_sdk.v2.datasets.errors import ViewPrimaryKeyRequiresBackingDatasets` |
**Filesystem** | AddGroupToParentGroupPermissionDenied | `from foundry_sdk.v2.filesystem.errors import AddGroupToParentGroupPermissionDenied` |
**Filesystem** | AddMarkingsPermissionDenied | `from foundry_sdk.v2.filesystem.errors import AddMarkingsPermissionDenied` |
**Filesystem** | AddOrganizationsPermissionDenied | `from foundry_sdk.v2.filesystem.errors import AddOrganizationsPermissionDenied` |
**Filesystem** | AddResourceRolesPermissionDenied | `from foundry_sdk.v2.filesystem.errors import AddResourceRolesPermissionDenied` |
**Filesystem** | CreateFolderOutsideProjectNotSupported | `from foundry_sdk.v2.filesystem.errors import CreateFolderOutsideProjectNotSupported` |
**Filesystem** | CreateFolderPermissionDenied | `from foundry_sdk.v2.filesystem.errors import CreateFolderPermissionDenied` |
**Filesystem** | CreateGroupPermissionDenied | `from foundry_sdk.v2.filesystem.errors import CreateGroupPermissionDenied` |
**Filesystem** | CreateProjectFromTemplatePermissionDenied | `from foundry_sdk.v2.filesystem.errors import CreateProjectFromTemplatePermissionDenied` |
**Filesystem** | CreateProjectNoOwnerLikeRoleGrant | `from foundry_sdk.v2.filesystem.errors import CreateProjectNoOwnerLikeRoleGrant` |
**Filesystem** | CreateProjectPermissionDenied | `from foundry_sdk.v2.filesystem.errors import CreateProjectPermissionDenied` |
**Filesystem** | CreateSpacePermissionDenied | `from foundry_sdk.v2.filesystem.errors import CreateSpacePermissionDenied` |
**Filesystem** | DefaultRolesNotInSpaceRoleSet | `from foundry_sdk.v2.filesystem.errors import DefaultRolesNotInSpaceRoleSet` |
**Filesystem** | DeleteResourcePermissionDenied | `from foundry_sdk.v2.filesystem.errors import DeleteResourcePermissionDenied` |
**Filesystem** | DeleteSpacePermissionDenied | `from foundry_sdk.v2.filesystem.errors import DeleteSpacePermissionDenied` |
**Filesystem** | EnrollmentNotFound | `from foundry_sdk.v2.filesystem.errors import EnrollmentNotFound` |
**Filesystem** | FolderNotFound | `from foundry_sdk.v2.filesystem.errors import FolderNotFound` |
**Filesystem** | ForbiddenOperationOnAutosavedResource | `from foundry_sdk.v2.filesystem.errors import ForbiddenOperationOnAutosavedResource` |
**Filesystem** | ForbiddenOperationOnHiddenResource | `from foundry_sdk.v2.filesystem.errors import ForbiddenOperationOnHiddenResource` |
**Filesystem** | GetAccessRequirementsPermissionDenied | `from foundry_sdk.v2.filesystem.errors import GetAccessRequirementsPermissionDenied` |
**Filesystem** | GetByPathPermissionDenied | `from foundry_sdk.v2.filesystem.errors import GetByPathPermissionDenied` |
**Filesystem** | GetRootFolderNotSupported | `from foundry_sdk.v2.filesystem.errors import GetRootFolderNotSupported` |
**Filesystem** | GetSpaceResourceNotSupported | `from foundry_sdk.v2.filesystem.errors import GetSpaceResourceNotSupported` |
**Filesystem** | InvalidDefaultRoles | `from foundry_sdk.v2.filesystem.errors import InvalidDefaultRoles` |
**Filesystem** | InvalidDescription | `from foundry_sdk.v2.filesystem.errors import InvalidDescription` |
**Filesystem** | InvalidDisplayName | `from foundry_sdk.v2.filesystem.errors import InvalidDisplayName` |
**Filesystem** | InvalidFolder | `from foundry_sdk.v2.filesystem.errors import InvalidFolder` |
**Filesystem** | InvalidOrganizationHierarchy | `from foundry_sdk.v2.filesystem.errors import InvalidOrganizationHierarchy` |
**Filesystem** | InvalidOrganizations | `from foundry_sdk.v2.filesystem.errors import InvalidOrganizations` |
**Filesystem** | InvalidPath | `from foundry_sdk.v2.filesystem.errors import InvalidPath` |
**Filesystem** | InvalidPrincipalIdsForGroupTemplate | `from foundry_sdk.v2.filesystem.errors import InvalidPrincipalIdsForGroupTemplate` |
**Filesystem** | InvalidRoleIds | `from foundry_sdk.v2.filesystem.errors import InvalidRoleIds` |
**Filesystem** | InvalidVariable | `from foundry_sdk.v2.filesystem.errors import InvalidVariable` |
**Filesystem** | InvalidVariableEnumOption | `from foundry_sdk.v2.filesystem.errors import InvalidVariableEnumOption` |
**Filesystem** | MarkingNotFound | `from foundry_sdk.v2.filesystem.errors import MarkingNotFound` |
**Filesystem** | MissingDisplayName | `from foundry_sdk.v2.filesystem.errors import MissingDisplayName` |
**Filesystem** | MissingVariableValue | `from foundry_sdk.v2.filesystem.errors import MissingVariableValue` |
**Filesystem** | NotAuthorizedToApplyOrganization | `from foundry_sdk.v2.filesystem.errors import NotAuthorizedToApplyOrganization` |
**Filesystem** | OrganizationCannotBeRemoved | `from foundry_sdk.v2.filesystem.errors import OrganizationCannotBeRemoved` |
**Filesystem** | OrganizationMarkingNotOnSpace | `from foundry_sdk.v2.filesystem.errors import OrganizationMarkingNotOnSpace` |
**Filesystem** | OrganizationMarkingNotSupported | `from foundry_sdk.v2.filesystem.errors import OrganizationMarkingNotSupported` |
**Filesystem** | OrganizationsNotFound | `from foundry_sdk.v2.filesystem.errors import OrganizationsNotFound` |
**Filesystem** | PathNotFound | `from foundry_sdk.v2.filesystem.errors import PathNotFound` |
**Filesystem** | PermanentlyDeleteResourcePermissionDenied | `from foundry_sdk.v2.filesystem.errors import PermanentlyDeleteResourcePermissionDenied` |
**Filesystem** | ProjectCreationNotSupported | `from foundry_sdk.v2.filesystem.errors import ProjectCreationNotSupported` |
**Filesystem** | ProjectNameAlreadyExists | `from foundry_sdk.v2.filesystem.errors import ProjectNameAlreadyExists` |
**Filesystem** | ProjectNotFound | `from foundry_sdk.v2.filesystem.errors import ProjectNotFound` |
**Filesystem** | ProjectTemplateNotFound | `from foundry_sdk.v2.filesystem.errors import ProjectTemplateNotFound` |
**Filesystem** | RemoveMarkingsPermissionDenied | `from foundry_sdk.v2.filesystem.errors import RemoveMarkingsPermissionDenied` |
**Filesystem** | RemoveOrganizationsPermissionDenied | `from foundry_sdk.v2.filesystem.errors import RemoveOrganizationsPermissionDenied` |
**Filesystem** | RemoveResourceRolesPermissionDenied | `from foundry_sdk.v2.filesystem.errors import RemoveResourceRolesPermissionDenied` |
**Filesystem** | ReplaceProjectPermissionDenied | `from foundry_sdk.v2.filesystem.errors import ReplaceProjectPermissionDenied` |
**Filesystem** | ReplaceSpacePermissionDenied | `from foundry_sdk.v2.filesystem.errors import ReplaceSpacePermissionDenied` |
**Filesystem** | ReservedSpaceCannotBeReplaced | `from foundry_sdk.v2.filesystem.errors import ReservedSpaceCannotBeReplaced` |
**Filesystem** | ResourceNameAlreadyExists | `from foundry_sdk.v2.filesystem.errors import ResourceNameAlreadyExists` |
**Filesystem** | ResourceNotDirectlyTrashed | `from foundry_sdk.v2.filesystem.errors import ResourceNotDirectlyTrashed` |
**Filesystem** | ResourceNotFound | `from foundry_sdk.v2.filesystem.errors import ResourceNotFound` |
**Filesystem** | ResourceNotTrashed | `from foundry_sdk.v2.filesystem.errors import ResourceNotTrashed` |
**Filesystem** | RestoreResourcePermissionDenied | `from foundry_sdk.v2.filesystem.errors import RestoreResourcePermissionDenied` |
**Filesystem** | RoleSetNotFound | `from foundry_sdk.v2.filesystem.errors import RoleSetNotFound` |
**Filesystem** | SpaceInternalError | `from foundry_sdk.v2.filesystem.errors import SpaceInternalError` |
**Filesystem** | SpaceInvalidArgument | `from foundry_sdk.v2.filesystem.errors import SpaceInvalidArgument` |
**Filesystem** | SpaceNameInvalid | `from foundry_sdk.v2.filesystem.errors import SpaceNameInvalid` |
**Filesystem** | SpaceNotEmpty | `from foundry_sdk.v2.filesystem.errors import SpaceNotEmpty` |
**Filesystem** | SpaceNotFound | `from foundry_sdk.v2.filesystem.errors import SpaceNotFound` |
**Filesystem** | TemplateGroupNameConflict | `from foundry_sdk.v2.filesystem.errors import TemplateGroupNameConflict` |
**Filesystem** | TemplateMarkingNameConflict | `from foundry_sdk.v2.filesystem.errors import TemplateMarkingNameConflict` |
**Filesystem** | TrashingAutosavedResourcesNotSupported | `from foundry_sdk.v2.filesystem.errors import TrashingAutosavedResourcesNotSupported` |
**Filesystem** | TrashingHiddenResourcesNotSupported | `from foundry_sdk.v2.filesystem.errors import TrashingHiddenResourcesNotSupported` |
**Filesystem** | TrashingSpaceNotSupported | `from foundry_sdk.v2.filesystem.errors import TrashingSpaceNotSupported` |
**Functions** | ExecuteQueryPermissionDenied | `from foundry_sdk.v2.functions.errors import ExecuteQueryPermissionDenied` |
**Functions** | GetByRidQueriesPermissionDenied | `from foundry_sdk.v2.functions.errors import GetByRidQueriesPermissionDenied` |
**Functions** | InvalidQueryOutputValue | `from foundry_sdk.v2.functions.errors import InvalidQueryOutputValue` |
**Functions** | InvalidQueryParameterValue | `from foundry_sdk.v2.functions.errors import InvalidQueryParameterValue` |
**Functions** | MissingParameter | `from foundry_sdk.v2.functions.errors import MissingParameter` |
**Functions** | QueryEncounteredUserFacingError | `from foundry_sdk.v2.functions.errors import QueryEncounteredUserFacingError` |
**Functions** | QueryMemoryExceededLimit | `from foundry_sdk.v2.functions.errors import QueryMemoryExceededLimit` |
**Functions** | QueryNotFound | `from foundry_sdk.v2.functions.errors import QueryNotFound` |
**Functions** | QueryRuntimeError | `from foundry_sdk.v2.functions.errors import QueryRuntimeError` |
**Functions** | QueryTimeExceededLimit | `from foundry_sdk.v2.functions.errors import QueryTimeExceededLimit` |
**Functions** | QueryVersionNotFound | `from foundry_sdk.v2.functions.errors import QueryVersionNotFound` |
**Functions** | UnknownParameter | `from foundry_sdk.v2.functions.errors import UnknownParameter` |
**Functions** | ValueTypeNotFound | `from foundry_sdk.v2.functions.errors import ValueTypeNotFound` |
**Functions** | VersionIdNotFound | `from foundry_sdk.v2.functions.errors import VersionIdNotFound` |
**MediaSets** | ConflictingMediaSetIdentifiers | `from foundry_sdk.v2.media_sets.errors import ConflictingMediaSetIdentifiers` |
**MediaSets** | GetMediaItemRidByPathPermissionDenied | `from foundry_sdk.v2.media_sets.errors import GetMediaItemRidByPathPermissionDenied` |
**MediaSets** | MediaItemNotFound | `from foundry_sdk.v2.media_sets.errors import MediaItemNotFound` |
**MediaSets** | MediaSetNotFound | `from foundry_sdk.v2.media_sets.errors import MediaSetNotFound` |
**MediaSets** | MissingMediaItemPath | `from foundry_sdk.v2.media_sets.errors import MissingMediaItemPath` |
**Ontologies** | ActionContainsDuplicateEdits | `from foundry_sdk.v2.ontologies.errors import ActionContainsDuplicateEdits` |
**Ontologies** | ActionEditedPropertiesNotFound | `from foundry_sdk.v2.ontologies.errors import ActionEditedPropertiesNotFound` |
**Ontologies** | ActionEditsReadOnlyEntity | `from foundry_sdk.v2.ontologies.errors import ActionEditsReadOnlyEntity` |
**Ontologies** | ActionNotFound | `from foundry_sdk.v2.ontologies.errors import ActionNotFound` |
**Ontologies** | ActionParameterInterfaceTypeNotFound | `from foundry_sdk.v2.ontologies.errors import ActionParameterInterfaceTypeNotFound` |
**Ontologies** | ActionParameterObjectNotFound | `from foundry_sdk.v2.ontologies.errors import ActionParameterObjectNotFound` |
**Ontologies** | ActionParameterObjectTypeNotFound | `from foundry_sdk.v2.ontologies.errors import ActionParameterObjectTypeNotFound` |
**Ontologies** | ActionTypeNotFound | `from foundry_sdk.v2.ontologies.errors import ActionTypeNotFound` |
**Ontologies** | ActionValidationFailed | `from foundry_sdk.v2.ontologies.errors import ActionValidationFailed` |
**Ontologies** | AggregationAccuracyNotSupported | `from foundry_sdk.v2.ontologies.errors import AggregationAccuracyNotSupported` |
**Ontologies** | AggregationGroupCountExceededLimit | `from foundry_sdk.v2.ontologies.errors import AggregationGroupCountExceededLimit` |
**Ontologies** | AggregationMemoryExceededLimit | `from foundry_sdk.v2.ontologies.errors import AggregationMemoryExceededLimit` |
**Ontologies** | AggregationNestedObjectSetSizeExceededLimit | `from foundry_sdk.v2.ontologies.errors import AggregationNestedObjectSetSizeExceededLimit` |
**Ontologies** | ApplyActionFailed | `from foundry_sdk.v2.ontologies.errors import ApplyActionFailed` |
**Ontologies** | AttachmentNotFound | `from foundry_sdk.v2.ontologies.errors import AttachmentNotFound` |
**Ontologies** | AttachmentSizeExceededLimit | `from foundry_sdk.v2.ontologies.errors import AttachmentSizeExceededLimit` |
**Ontologies** | CipherChannelNotFound | `from foundry_sdk.v2.ontologies.errors import CipherChannelNotFound` |
**Ontologies** | CompositePrimaryKeyNotSupported | `from foundry_sdk.v2.ontologies.errors import CompositePrimaryKeyNotSupported` |
**Ontologies** | DefaultAndNullGroupsNotSupported | `from foundry_sdk.v2.ontologies.errors import DefaultAndNullGroupsNotSupported` |
**Ontologies** | DerivedPropertyApiNamesNotUnique | `from foundry_sdk.v2.ontologies.errors import DerivedPropertyApiNamesNotUnique` |
**Ontologies** | DuplicateOrderBy | `from foundry_sdk.v2.ontologies.errors import DuplicateOrderBy` |
**Ontologies** | EditObjectPermissionDenied | `from foundry_sdk.v2.ontologies.errors import EditObjectPermissionDenied` |
**Ontologies** | FunctionEncounteredUserFacingError | `from foundry_sdk.v2.ontologies.errors import FunctionEncounteredUserFacingError` |
**Ontologies** | FunctionExecutionFailed | `from foundry_sdk.v2.ontologies.errors import FunctionExecutionFailed` |
**Ontologies** | FunctionExecutionTimedOut | `from foundry_sdk.v2.ontologies.errors import FunctionExecutionTimedOut` |
**Ontologies** | FunctionInvalidInput | `from foundry_sdk.v2.ontologies.errors import FunctionInvalidInput` |
**Ontologies** | HighScaleComputationNotEnabled | `from foundry_sdk.v2.ontologies.errors import HighScaleComputationNotEnabled` |
**Ontologies** | InterfaceLinkTypeNotFound | `from foundry_sdk.v2.ontologies.errors import InterfaceLinkTypeNotFound` |
**Ontologies** | InterfaceTypeNotFound | `from foundry_sdk.v2.ontologies.errors import InterfaceTypeNotFound` |
**Ontologies** | InterfaceTypesNotFound | `from foundry_sdk.v2.ontologies.errors import InterfaceTypesNotFound` |
**Ontologies** | InvalidAggregationOrdering | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationOrdering` |
**Ontologies** | InvalidAggregationOrderingWithNullValues | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationOrderingWithNullValues` |
**Ontologies** | InvalidAggregationRange | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationRange` |
**Ontologies** | InvalidAggregationRangePropertyType | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationRangePropertyType` |
**Ontologies** | InvalidAggregationRangeValue | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationRangeValue` |
**Ontologies** | InvalidApplyActionOptionCombination | `from foundry_sdk.v2.ontologies.errors import InvalidApplyActionOptionCombination` |
**Ontologies** | InvalidContentLength | `from foundry_sdk.v2.ontologies.errors import InvalidContentLength` |
**Ontologies** | InvalidContentType | `from foundry_sdk.v2.ontologies.errors import InvalidContentType` |
**Ontologies** | InvalidDerivedPropertyDefinition | `from foundry_sdk.v2.ontologies.errors import InvalidDerivedPropertyDefinition` |
**Ontologies** | InvalidDurationGroupByPropertyType | `from foundry_sdk.v2.ontologies.errors import InvalidDurationGroupByPropertyType` |
**Ontologies** | InvalidDurationGroupByValue | `from foundry_sdk.v2.ontologies.errors import InvalidDurationGroupByValue` |
**Ontologies** | InvalidFields | `from foundry_sdk.v2.ontologies.errors import InvalidFields` |
**Ontologies** | InvalidGroupId | `from foundry_sdk.v2.ontologies.errors import InvalidGroupId` |
**Ontologies** | InvalidOrderType | `from foundry_sdk.v2.ontologies.errors import InvalidOrderType` |
**Ontologies** | InvalidParameterValue | `from foundry_sdk.v2.ontologies.errors import InvalidParameterValue` |
**Ontologies** | InvalidPropertyFiltersCombination | `from foundry_sdk.v2.ontologies.errors import InvalidPropertyFiltersCombination` |
**Ontologies** | InvalidPropertyFilterValue | `from foundry_sdk.v2.ontologies.errors import InvalidPropertyFilterValue` |
**Ontologies** | InvalidPropertyType | `from foundry_sdk.v2.ontologies.errors import InvalidPropertyType` |
**Ontologies** | InvalidPropertyValue | `from foundry_sdk.v2.ontologies.errors import InvalidPropertyValue` |
**Ontologies** | InvalidQueryOutputValue | `from foundry_sdk.v2.ontologies.errors import InvalidQueryOutputValue` |
**Ontologies** | InvalidQueryParameterValue | `from foundry_sdk.v2.ontologies.errors import InvalidQueryParameterValue` |
**Ontologies** | InvalidRangeQuery | `from foundry_sdk.v2.ontologies.errors import InvalidRangeQuery` |
**Ontologies** | InvalidSortOrder | `from foundry_sdk.v2.ontologies.errors import InvalidSortOrder` |
**Ontologies** | InvalidSortType | `from foundry_sdk.v2.ontologies.errors import InvalidSortType` |
**Ontologies** | InvalidUserId | `from foundry_sdk.v2.ontologies.errors import InvalidUserId` |
**Ontologies** | InvalidVectorDimension | `from foundry_sdk.v2.ontologies.errors import InvalidVectorDimension` |
**Ontologies** | LinkAlreadyExists | `from foundry_sdk.v2.ontologies.errors import LinkAlreadyExists` |
**Ontologies** | LinkedObjectNotFound | `from foundry_sdk.v2.ontologies.errors import LinkedObjectNotFound` |
**Ontologies** | LinkTypeNotFound | `from foundry_sdk.v2.ontologies.errors import LinkTypeNotFound` |
**Ontologies** | MalformedPropertyFilters | `from foundry_sdk.v2.ontologies.errors import MalformedPropertyFilters` |
**Ontologies** | MarketplaceActionMappingNotFound | `from foundry_sdk.v2.ontologies.errors import MarketplaceActionMappingNotFound` |
**Ontologies** | MarketplaceInstallationNotFound | `from foundry_sdk.v2.ontologies.errors import MarketplaceInstallationNotFound` |
**Ontologies** | MarketplaceLinkMappingNotFound | `from foundry_sdk.v2.ontologies.errors import MarketplaceLinkMappingNotFound` |
**Ontologies** | MarketplaceObjectMappingNotFound | `from foundry_sdk.v2.ontologies.errors import MarketplaceObjectMappingNotFound` |
**Ontologies** | MarketplaceQueryMappingNotFound | `from foundry_sdk.v2.ontologies.errors import MarketplaceQueryMappingNotFound` |
**Ontologies** | MarketplaceSdkActionMappingNotFound | `from foundry_sdk.v2.ontologies.errors import MarketplaceSdkActionMappingNotFound` |
**Ontologies** | MarketplaceSdkInstallationNotFound | `from foundry_sdk.v2.ontologies.errors import MarketplaceSdkInstallationNotFound` |
**Ontologies** | MarketplaceSdkLinkMappingNotFound | `from foundry_sdk.v2.ontologies.errors import MarketplaceSdkLinkMappingNotFound` |
**Ontologies** | MarketplaceSdkObjectMappingNotFound | `from foundry_sdk.v2.ontologies.errors import MarketplaceSdkObjectMappingNotFound` |
**Ontologies** | MarketplaceSdkPropertyMappingNotFound | `from foundry_sdk.v2.ontologies.errors import MarketplaceSdkPropertyMappingNotFound` |
**Ontologies** | MarketplaceSdkQueryMappingNotFound | `from foundry_sdk.v2.ontologies.errors import MarketplaceSdkQueryMappingNotFound` |
**Ontologies** | MissingParameter | `from foundry_sdk.v2.ontologies.errors import MissingParameter` |
**Ontologies** | MultipleGroupByOnFieldNotSupported | `from foundry_sdk.v2.ontologies.errors import MultipleGroupByOnFieldNotSupported` |
**Ontologies** | MultiplePropertyValuesNotSupported | `from foundry_sdk.v2.ontologies.errors import MultiplePropertyValuesNotSupported` |
**Ontologies** | NotCipherFormatted | `from foundry_sdk.v2.ontologies.errors import NotCipherFormatted` |
**Ontologies** | ObjectAlreadyExists | `from foundry_sdk.v2.ontologies.errors import ObjectAlreadyExists` |
**Ontologies** | ObjectChanged | `from foundry_sdk.v2.ontologies.errors import ObjectChanged` |
**Ontologies** | ObjectNotFound | `from foundry_sdk.v2.ontologies.errors import ObjectNotFound` |
**Ontologies** | ObjectSetNotFound | `from foundry_sdk.v2.ontologies.errors import ObjectSetNotFound` |
**Ontologies** | ObjectsExceededLimit | `from foundry_sdk.v2.ontologies.errors import ObjectsExceededLimit` |
**Ontologies** | ObjectTypeNotFound | `from foundry_sdk.v2.ontologies.errors import ObjectTypeNotFound` |
**Ontologies** | ObjectTypeNotSynced | `from foundry_sdk.v2.ontologies.errors import ObjectTypeNotSynced` |
**Ontologies** | ObjectTypesNotSynced | `from foundry_sdk.v2.ontologies.errors import ObjectTypesNotSynced` |
**Ontologies** | OntologyApiNameNotUnique | `from foundry_sdk.v2.ontologies.errors import OntologyApiNameNotUnique` |
**Ontologies** | OntologyEditsExceededLimit | `from foundry_sdk.v2.ontologies.errors import OntologyEditsExceededLimit` |
**Ontologies** | OntologyNotFound | `from foundry_sdk.v2.ontologies.errors import OntologyNotFound` |
**Ontologies** | OntologySyncing | `from foundry_sdk.v2.ontologies.errors import OntologySyncing` |
**Ontologies** | OntologySyncingObjectTypes | `from foundry_sdk.v2.ontologies.errors import OntologySyncingObjectTypes` |
**Ontologies** | ParameterObjectNotFound | `from foundry_sdk.v2.ontologies.errors import ParameterObjectNotFound` |
**Ontologies** | ParameterObjectSetRidNotFound | `from foundry_sdk.v2.ontologies.errors import ParameterObjectSetRidNotFound` |
**Ontologies** | ParametersNotFound | `from foundry_sdk.v2.ontologies.errors import ParametersNotFound` |
**Ontologies** | ParameterTypeNotSupported | `from foundry_sdk.v2.ontologies.errors import ParameterTypeNotSupported` |
**Ontologies** | ParentAttachmentPermissionDenied | `from foundry_sdk.v2.ontologies.errors import ParentAttachmentPermissionDenied` |
**Ontologies** | PropertiesHaveDifferentIds | `from foundry_sdk.v2.ontologies.errors import PropertiesHaveDifferentIds` |
**Ontologies** | PropertiesNotFilterable | `from foundry_sdk.v2.ontologies.errors import PropertiesNotFilterable` |
**Ontologies** | PropertiesNotFound | `from foundry_sdk.v2.ontologies.errors import PropertiesNotFound` |
**Ontologies** | PropertiesNotSearchable | `from foundry_sdk.v2.ontologies.errors import PropertiesNotSearchable` |
**Ontologies** | PropertiesNotSortable | `from foundry_sdk.v2.ontologies.errors import PropertiesNotSortable` |
**Ontologies** | PropertyApiNameNotFound | `from foundry_sdk.v2.ontologies.errors import PropertyApiNameNotFound` |
**Ontologies** | PropertyBaseTypeNotSupported | `from foundry_sdk.v2.ontologies.errors import PropertyBaseTypeNotSupported` |
**Ontologies** | PropertyFiltersNotSupported | `from foundry_sdk.v2.ontologies.errors import PropertyFiltersNotSupported` |
**Ontologies** | PropertyNotFound | `from foundry_sdk.v2.ontologies.errors import PropertyNotFound` |
**Ontologies** | PropertyTypeDoesNotSupportNearestNeighbors | `from foundry_sdk.v2.ontologies.errors import PropertyTypeDoesNotSupportNearestNeighbors` |
**Ontologies** | PropertyTypeNotFound | `from foundry_sdk.v2.ontologies.errors import PropertyTypeNotFound` |
**Ontologies** | PropertyTypeRidNotFound | `from foundry_sdk.v2.ontologies.errors import PropertyTypeRidNotFound` |
**Ontologies** | PropertyTypesSearchNotSupported | `from foundry_sdk.v2.ontologies.errors import PropertyTypesSearchNotSupported` |
**Ontologies** | QueryEncounteredUserFacingError | `from foundry_sdk.v2.ontologies.errors import QueryEncounteredUserFacingError` |
**Ontologies** | QueryMemoryExceededLimit | `from foundry_sdk.v2.ontologies.errors import QueryMemoryExceededLimit` |
**Ontologies** | QueryNotFound | `from foundry_sdk.v2.ontologies.errors import QueryNotFound` |
**Ontologies** | QueryRuntimeError | `from foundry_sdk.v2.ontologies.errors import QueryRuntimeError` |
**Ontologies** | QueryTimeExceededLimit | `from foundry_sdk.v2.ontologies.errors import QueryTimeExceededLimit` |
**Ontologies** | QueryVersionNotFound | `from foundry_sdk.v2.ontologies.errors import QueryVersionNotFound` |
**Ontologies** | RateLimitReached | `from foundry_sdk.v2.ontologies.errors import RateLimitReached` |
**Ontologies** | SharedPropertiesNotFound | `from foundry_sdk.v2.ontologies.errors import SharedPropertiesNotFound` |
**Ontologies** | SharedPropertyTypeNotFound | `from foundry_sdk.v2.ontologies.errors import SharedPropertyTypeNotFound` |
**Ontologies** | TooManyNearestNeighborsRequested | `from foundry_sdk.v2.ontologies.errors import TooManyNearestNeighborsRequested` |
**Ontologies** | UnauthorizedCipherOperation | `from foundry_sdk.v2.ontologies.errors import UnauthorizedCipherOperation` |
**Ontologies** | UndecryptableValue | `from foundry_sdk.v2.ontologies.errors import UndecryptableValue` |
**Ontologies** | UnknownParameter | `from foundry_sdk.v2.ontologies.errors import UnknownParameter` |
**Ontologies** | UnsupportedObjectSet | `from foundry_sdk.v2.ontologies.errors import UnsupportedObjectSet` |
**Ontologies** | ValueTypeNotFound | `from foundry_sdk.v2.ontologies.errors import ValueTypeNotFound` |
**Ontologies** | ViewObjectPermissionDenied | `from foundry_sdk.v2.ontologies.errors import ViewObjectPermissionDenied` |
**Orchestration** | BuildInputsNotFound | `from foundry_sdk.v2.orchestration.errors import BuildInputsNotFound` |
**Orchestration** | BuildInputsPermissionDenied | `from foundry_sdk.v2.orchestration.errors import BuildInputsPermissionDenied` |
**Orchestration** | BuildNotFound | `from foundry_sdk.v2.orchestration.errors import BuildNotFound` |
**Orchestration** | BuildTargetsMissingJobSpecs | `from foundry_sdk.v2.orchestration.errors import BuildTargetsMissingJobSpecs` |
**Orchestration** | BuildTargetsNotFound | `from foundry_sdk.v2.orchestration.errors import BuildTargetsNotFound` |
**Orchestration** | BuildTargetsPermissionDenied | `from foundry_sdk.v2.orchestration.errors import BuildTargetsPermissionDenied` |
**Orchestration** | BuildTargetsResolutionError | `from foundry_sdk.v2.orchestration.errors import BuildTargetsResolutionError` |
**Orchestration** | BuildTargetsUpToDate | `from foundry_sdk.v2.orchestration.errors import BuildTargetsUpToDate` |
**Orchestration** | CancelBuildPermissionDenied | `from foundry_sdk.v2.orchestration.errors import CancelBuildPermissionDenied` |
**Orchestration** | CreateBuildPermissionDenied | `from foundry_sdk.v2.orchestration.errors import CreateBuildPermissionDenied` |
**Orchestration** | CreateSchedulePermissionDenied | `from foundry_sdk.v2.orchestration.errors import CreateSchedulePermissionDenied` |
**Orchestration** | DeleteSchedulePermissionDenied | `from foundry_sdk.v2.orchestration.errors import DeleteSchedulePermissionDenied` |
**Orchestration** | InvalidAndTrigger | `from foundry_sdk.v2.orchestration.errors import InvalidAndTrigger` |
**Orchestration** | InvalidMediaSetTrigger | `from foundry_sdk.v2.orchestration.errors import InvalidMediaSetTrigger` |
**Orchestration** | InvalidOrTrigger | `from foundry_sdk.v2.orchestration.errors import InvalidOrTrigger` |
**Orchestration** | InvalidScheduleDescription | `from foundry_sdk.v2.orchestration.errors import InvalidScheduleDescription` |
**Orchestration** | InvalidScheduleName | `from foundry_sdk.v2.orchestration.errors import InvalidScheduleName` |
**Orchestration** | InvalidTimeTrigger | `from foundry_sdk.v2.orchestration.errors import InvalidTimeTrigger` |
**Orchestration** | JobNotFound | `from foundry_sdk.v2.orchestration.errors import JobNotFound` |
**Orchestration** | MissingBuildTargets | `from foundry_sdk.v2.orchestration.errors import MissingBuildTargets` |
**Orchestration** | MissingConnectingBuildInputs | `from foundry_sdk.v2.orchestration.errors import MissingConnectingBuildInputs` |
**Orchestration** | MissingTrigger | `from foundry_sdk.v2.orchestration.errors import MissingTrigger` |
**Orchestration** | PauseSchedulePermissionDenied | `from foundry_sdk.v2.orchestration.errors import PauseSchedulePermissionDenied` |
**Orchestration** | ReplaceSchedulePermissionDenied | `from foundry_sdk.v2.orchestration.errors import ReplaceSchedulePermissionDenied` |
**Orchestration** | RunSchedulePermissionDenied | `from foundry_sdk.v2.orchestration.errors import RunSchedulePermissionDenied` |
**Orchestration** | ScheduleAlreadyRunning | `from foundry_sdk.v2.orchestration.errors import ScheduleAlreadyRunning` |
**Orchestration** | ScheduleNotFound | `from foundry_sdk.v2.orchestration.errors import ScheduleNotFound` |
**Orchestration** | ScheduleTriggerResourcesNotFound | `from foundry_sdk.v2.orchestration.errors import ScheduleTriggerResourcesNotFound` |
**Orchestration** | ScheduleTriggerResourcesPermissionDenied | `from foundry_sdk.v2.orchestration.errors import ScheduleTriggerResourcesPermissionDenied` |
**Orchestration** | ScheduleVersionNotFound | `from foundry_sdk.v2.orchestration.errors import ScheduleVersionNotFound` |
**Orchestration** | SearchBuildsPermissionDenied | `from foundry_sdk.v2.orchestration.errors import SearchBuildsPermissionDenied` |
**Orchestration** | TargetNotSupported | `from foundry_sdk.v2.orchestration.errors import TargetNotSupported` |
**Orchestration** | UnpauseSchedulePermissionDenied | `from foundry_sdk.v2.orchestration.errors import UnpauseSchedulePermissionDenied` |
**SqlQueries** | CancelSqlQueryPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import CancelSqlQueryPermissionDenied` |
**SqlQueries** | ExecuteSqlQueryPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import ExecuteSqlQueryPermissionDenied` |
**SqlQueries** | GetResultsSqlQueryPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import GetResultsSqlQueryPermissionDenied` |
**SqlQueries** | GetStatusSqlQueryPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import GetStatusSqlQueryPermissionDenied` |
**SqlQueries** | QueryCanceled | `from foundry_sdk.v2.sql_queries.errors import QueryCanceled` |
**SqlQueries** | QueryFailed | `from foundry_sdk.v2.sql_queries.errors import QueryFailed` |
**SqlQueries** | QueryParseError | `from foundry_sdk.v2.sql_queries.errors import QueryParseError` |
**SqlQueries** | QueryPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import QueryPermissionDenied` |
**SqlQueries** | QueryRunning | `from foundry_sdk.v2.sql_queries.errors import QueryRunning` |
**SqlQueries** | ReadQueryInputsPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import ReadQueryInputsPermissionDenied` |
**Streams** | CannotCreateStreamingDatasetInUserFolder | `from foundry_sdk.v2.streams.errors import CannotCreateStreamingDatasetInUserFolder` |
**Streams** | CannotWriteToTrashedStream | `from foundry_sdk.v2.streams.errors import CannotWriteToTrashedStream` |
**Streams** | CreateStreamingDatasetPermissionDenied | `from foundry_sdk.v2.streams.errors import CreateStreamingDatasetPermissionDenied` |
**Streams** | CreateStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import CreateStreamPermissionDenied` |
**Streams** | FailedToProcessBinaryRecord | `from foundry_sdk.v2.streams.errors import FailedToProcessBinaryRecord` |
**Streams** | InvalidStreamNoSchema | `from foundry_sdk.v2.streams.errors import InvalidStreamNoSchema` |
**Streams** | InvalidStreamType | `from foundry_sdk.v2.streams.errors import InvalidStreamType` |
**Streams** | PublishBinaryRecordToStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import PublishBinaryRecordToStreamPermissionDenied` |
**Streams** | PublishRecordsToStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import PublishRecordsToStreamPermissionDenied` |
**Streams** | PublishRecordToStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import PublishRecordToStreamPermissionDenied` |
**Streams** | RecordDoesNotMatchStreamSchema | `from foundry_sdk.v2.streams.errors import RecordDoesNotMatchStreamSchema` |
**Streams** | RecordTooLarge | `from foundry_sdk.v2.streams.errors import RecordTooLarge` |
**Streams** | ResetStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import ResetStreamPermissionDenied` |
**Streams** | StreamNotFound | `from foundry_sdk.v2.streams.errors import StreamNotFound` |
**Streams** | ViewNotFound | `from foundry_sdk.v2.streams.errors import ViewNotFound` |
**ThirdPartyApplications** | CannotDeleteDeployedVersion | `from foundry_sdk.v2.third_party_applications.errors import CannotDeleteDeployedVersion` |
**ThirdPartyApplications** | DeleteVersionPermissionDenied | `from foundry_sdk.v2.third_party_applications.errors import DeleteVersionPermissionDenied` |
**ThirdPartyApplications** | DeployWebsitePermissionDenied | `from foundry_sdk.v2.third_party_applications.errors import DeployWebsitePermissionDenied` |
**ThirdPartyApplications** | FileCountLimitExceeded | `from foundry_sdk.v2.third_party_applications.errors import FileCountLimitExceeded` |
**ThirdPartyApplications** | FileSizeLimitExceeded | `from foundry_sdk.v2.third_party_applications.errors import FileSizeLimitExceeded` |
**ThirdPartyApplications** | InvalidVersion | `from foundry_sdk.v2.third_party_applications.errors import InvalidVersion` |
**ThirdPartyApplications** | ThirdPartyApplicationNotFound | `from foundry_sdk.v2.third_party_applications.errors import ThirdPartyApplicationNotFound` |
**ThirdPartyApplications** | UndeployWebsitePermissionDenied | `from foundry_sdk.v2.third_party_applications.errors import UndeployWebsitePermissionDenied` |
**ThirdPartyApplications** | UploadSnapshotVersionPermissionDenied | `from foundry_sdk.v2.third_party_applications.errors import UploadSnapshotVersionPermissionDenied` |
**ThirdPartyApplications** | UploadVersionPermissionDenied | `from foundry_sdk.v2.third_party_applications.errors import UploadVersionPermissionDenied` |
**ThirdPartyApplications** | VersionAlreadyExists | `from foundry_sdk.v2.third_party_applications.errors import VersionAlreadyExists` |
**ThirdPartyApplications** | VersionLimitExceeded | `from foundry_sdk.v2.third_party_applications.errors import VersionLimitExceeded` |
**ThirdPartyApplications** | VersionNotFound | `from foundry_sdk.v2.third_party_applications.errors import VersionNotFound` |
**ThirdPartyApplications** | WebsiteNotFound | `from foundry_sdk.v2.third_party_applications.errors import WebsiteNotFound` |
<a id="errors-v1-link"></a>
## Documentation for V1 errors

Namespace | Name | Import |
--------- | ---- | ------ |
**Core** | ApiFeaturePreviewUsageOnly | `from foundry_sdk.v1.core.errors import ApiFeaturePreviewUsageOnly` |
**Core** | ApiUsageDenied | `from foundry_sdk.v1.core.errors import ApiUsageDenied` |
**Core** | FolderNotFound | `from foundry_sdk.v1.core.errors import FolderNotFound` |
**Core** | FoundryBranchNotFound | `from foundry_sdk.v1.core.errors import FoundryBranchNotFound` |
**Core** | InvalidPageSize | `from foundry_sdk.v1.core.errors import InvalidPageSize` |
**Core** | InvalidPageToken | `from foundry_sdk.v1.core.errors import InvalidPageToken` |
**Core** | InvalidParameterCombination | `from foundry_sdk.v1.core.errors import InvalidParameterCombination` |
**Core** | MissingPostBody | `from foundry_sdk.v1.core.errors import MissingPostBody` |
**Core** | ResourceNameAlreadyExists | `from foundry_sdk.v1.core.errors import ResourceNameAlreadyExists` |
**Core** | UnknownDistanceUnit | `from foundry_sdk.v1.core.errors import UnknownDistanceUnit` |
**Datasets** | AbortTransactionPermissionDenied | `from foundry_sdk.v1.datasets.errors import AbortTransactionPermissionDenied` |
**Datasets** | BranchAlreadyExists | `from foundry_sdk.v1.datasets.errors import BranchAlreadyExists` |
**Datasets** | BranchNotFound | `from foundry_sdk.v1.datasets.errors import BranchNotFound` |
**Datasets** | ColumnTypesNotSupported | `from foundry_sdk.v1.datasets.errors import ColumnTypesNotSupported` |
**Datasets** | CommitTransactionPermissionDenied | `from foundry_sdk.v1.datasets.errors import CommitTransactionPermissionDenied` |
**Datasets** | CreateBranchPermissionDenied | `from foundry_sdk.v1.datasets.errors import CreateBranchPermissionDenied` |
**Datasets** | CreateDatasetPermissionDenied | `from foundry_sdk.v1.datasets.errors import CreateDatasetPermissionDenied` |
**Datasets** | CreateTransactionPermissionDenied | `from foundry_sdk.v1.datasets.errors import CreateTransactionPermissionDenied` |
**Datasets** | DatasetNotFound | `from foundry_sdk.v1.datasets.errors import DatasetNotFound` |
**Datasets** | DatasetReadNotSupported | `from foundry_sdk.v1.datasets.errors import DatasetReadNotSupported` |
**Datasets** | DeleteBranchPermissionDenied | `from foundry_sdk.v1.datasets.errors import DeleteBranchPermissionDenied` |
**Datasets** | DeleteSchemaPermissionDenied | `from foundry_sdk.v1.datasets.errors import DeleteSchemaPermissionDenied` |
**Datasets** | FileAlreadyExists | `from foundry_sdk.v1.datasets.errors import FileAlreadyExists` |
**Datasets** | FileNotFoundOnBranch | `from foundry_sdk.v1.datasets.errors import FileNotFoundOnBranch` |
**Datasets** | FileNotFoundOnTransactionRange | `from foundry_sdk.v1.datasets.errors import FileNotFoundOnTransactionRange` |
**Datasets** | InvalidBranchId | `from foundry_sdk.v1.datasets.errors import InvalidBranchId` |
**Datasets** | InvalidTransactionType | `from foundry_sdk.v1.datasets.errors import InvalidTransactionType` |
**Datasets** | OpenTransactionAlreadyExists | `from foundry_sdk.v1.datasets.errors import OpenTransactionAlreadyExists` |
**Datasets** | PutSchemaPermissionDenied | `from foundry_sdk.v1.datasets.errors import PutSchemaPermissionDenied` |
**Datasets** | ReadTablePermissionDenied | `from foundry_sdk.v1.datasets.errors import ReadTablePermissionDenied` |
**Datasets** | SchemaNotFound | `from foundry_sdk.v1.datasets.errors import SchemaNotFound` |
**Datasets** | TransactionNotCommitted | `from foundry_sdk.v1.datasets.errors import TransactionNotCommitted` |
**Datasets** | TransactionNotFound | `from foundry_sdk.v1.datasets.errors import TransactionNotFound` |
**Datasets** | TransactionNotOpen | `from foundry_sdk.v1.datasets.errors import TransactionNotOpen` |
**Datasets** | UploadFilePermissionDenied | `from foundry_sdk.v1.datasets.errors import UploadFilePermissionDenied` |
**Ontologies** | ActionContainsDuplicateEdits | `from foundry_sdk.v1.ontologies.errors import ActionContainsDuplicateEdits` |
**Ontologies** | ActionEditedPropertiesNotFound | `from foundry_sdk.v1.ontologies.errors import ActionEditedPropertiesNotFound` |
**Ontologies** | ActionEditsReadOnlyEntity | `from foundry_sdk.v1.ontologies.errors import ActionEditsReadOnlyEntity` |
**Ontologies** | ActionNotFound | `from foundry_sdk.v1.ontologies.errors import ActionNotFound` |
**Ontologies** | ActionParameterInterfaceTypeNotFound | `from foundry_sdk.v1.ontologies.errors import ActionParameterInterfaceTypeNotFound` |
**Ontologies** | ActionParameterObjectNotFound | `from foundry_sdk.v1.ontologies.errors import ActionParameterObjectNotFound` |
**Ontologies** | ActionParameterObjectTypeNotFound | `from foundry_sdk.v1.ontologies.errors import ActionParameterObjectTypeNotFound` |
**Ontologies** | ActionTypeNotFound | `from foundry_sdk.v1.ontologies.errors import ActionTypeNotFound` |
**Ontologies** | ActionValidationFailed | `from foundry_sdk.v1.ontologies.errors import ActionValidationFailed` |
**Ontologies** | AggregationAccuracyNotSupported | `from foundry_sdk.v1.ontologies.errors import AggregationAccuracyNotSupported` |
**Ontologies** | AggregationGroupCountExceededLimit | `from foundry_sdk.v1.ontologies.errors import AggregationGroupCountExceededLimit` |
**Ontologies** | AggregationMemoryExceededLimit | `from foundry_sdk.v1.ontologies.errors import AggregationMemoryExceededLimit` |
**Ontologies** | AggregationNestedObjectSetSizeExceededLimit | `from foundry_sdk.v1.ontologies.errors import AggregationNestedObjectSetSizeExceededLimit` |
**Ontologies** | ApplyActionFailed | `from foundry_sdk.v1.ontologies.errors import ApplyActionFailed` |
**Ontologies** | AttachmentNotFound | `from foundry_sdk.v1.ontologies.errors import AttachmentNotFound` |
**Ontologies** | AttachmentSizeExceededLimit | `from foundry_sdk.v1.ontologies.errors import AttachmentSizeExceededLimit` |
**Ontologies** | CipherChannelNotFound | `from foundry_sdk.v1.ontologies.errors import CipherChannelNotFound` |
**Ontologies** | CompositePrimaryKeyNotSupported | `from foundry_sdk.v1.ontologies.errors import CompositePrimaryKeyNotSupported` |
**Ontologies** | DefaultAndNullGroupsNotSupported | `from foundry_sdk.v1.ontologies.errors import DefaultAndNullGroupsNotSupported` |
**Ontologies** | DerivedPropertyApiNamesNotUnique | `from foundry_sdk.v1.ontologies.errors import DerivedPropertyApiNamesNotUnique` |
**Ontologies** | DuplicateOrderBy | `from foundry_sdk.v1.ontologies.errors import DuplicateOrderBy` |
**Ontologies** | EditObjectPermissionDenied | `from foundry_sdk.v1.ontologies.errors import EditObjectPermissionDenied` |
**Ontologies** | FunctionEncounteredUserFacingError | `from foundry_sdk.v1.ontologies.errors import FunctionEncounteredUserFacingError` |
**Ontologies** | FunctionExecutionFailed | `from foundry_sdk.v1.ontologies.errors import FunctionExecutionFailed` |
**Ontologies** | FunctionExecutionTimedOut | `from foundry_sdk.v1.ontologies.errors import FunctionExecutionTimedOut` |
**Ontologies** | FunctionInvalidInput | `from foundry_sdk.v1.ontologies.errors import FunctionInvalidInput` |
**Ontologies** | HighScaleComputationNotEnabled | `from foundry_sdk.v1.ontologies.errors import HighScaleComputationNotEnabled` |
**Ontologies** | InterfaceLinkTypeNotFound | `from foundry_sdk.v1.ontologies.errors import InterfaceLinkTypeNotFound` |
**Ontologies** | InterfaceTypeNotFound | `from foundry_sdk.v1.ontologies.errors import InterfaceTypeNotFound` |
**Ontologies** | InterfaceTypesNotFound | `from foundry_sdk.v1.ontologies.errors import InterfaceTypesNotFound` |
**Ontologies** | InvalidAggregationOrdering | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationOrdering` |
**Ontologies** | InvalidAggregationOrderingWithNullValues | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationOrderingWithNullValues` |
**Ontologies** | InvalidAggregationRange | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationRange` |
**Ontologies** | InvalidAggregationRangePropertyType | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationRangePropertyType` |
**Ontologies** | InvalidAggregationRangeValue | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationRangeValue` |
**Ontologies** | InvalidApplyActionOptionCombination | `from foundry_sdk.v1.ontologies.errors import InvalidApplyActionOptionCombination` |
**Ontologies** | InvalidContentLength | `from foundry_sdk.v1.ontologies.errors import InvalidContentLength` |
**Ontologies** | InvalidContentType | `from foundry_sdk.v1.ontologies.errors import InvalidContentType` |
**Ontologies** | InvalidDerivedPropertyDefinition | `from foundry_sdk.v1.ontologies.errors import InvalidDerivedPropertyDefinition` |
**Ontologies** | InvalidDurationGroupByPropertyType | `from foundry_sdk.v1.ontologies.errors import InvalidDurationGroupByPropertyType` |
**Ontologies** | InvalidDurationGroupByValue | `from foundry_sdk.v1.ontologies.errors import InvalidDurationGroupByValue` |
**Ontologies** | InvalidFields | `from foundry_sdk.v1.ontologies.errors import InvalidFields` |
**Ontologies** | InvalidGroupId | `from foundry_sdk.v1.ontologies.errors import InvalidGroupId` |
**Ontologies** | InvalidOrderType | `from foundry_sdk.v1.ontologies.errors import InvalidOrderType` |
**Ontologies** | InvalidParameterValue | `from foundry_sdk.v1.ontologies.errors import InvalidParameterValue` |
**Ontologies** | InvalidPropertyFiltersCombination | `from foundry_sdk.v1.ontologies.errors import InvalidPropertyFiltersCombination` |
**Ontologies** | InvalidPropertyFilterValue | `from foundry_sdk.v1.ontologies.errors import InvalidPropertyFilterValue` |
**Ontologies** | InvalidPropertyType | `from foundry_sdk.v1.ontologies.errors import InvalidPropertyType` |
**Ontologies** | InvalidPropertyValue | `from foundry_sdk.v1.ontologies.errors import InvalidPropertyValue` |
**Ontologies** | InvalidQueryOutputValue | `from foundry_sdk.v1.ontologies.errors import InvalidQueryOutputValue` |
**Ontologies** | InvalidQueryParameterValue | `from foundry_sdk.v1.ontologies.errors import InvalidQueryParameterValue` |
**Ontologies** | InvalidRangeQuery | `from foundry_sdk.v1.ontologies.errors import InvalidRangeQuery` |
**Ontologies** | InvalidSortOrder | `from foundry_sdk.v1.ontologies.errors import InvalidSortOrder` |
**Ontologies** | InvalidSortType | `from foundry_sdk.v1.ontologies.errors import InvalidSortType` |
**Ontologies** | InvalidUserId | `from foundry_sdk.v1.ontologies.errors import InvalidUserId` |
**Ontologies** | InvalidVectorDimension | `from foundry_sdk.v1.ontologies.errors import InvalidVectorDimension` |
**Ontologies** | LinkAlreadyExists | `from foundry_sdk.v1.ontologies.errors import LinkAlreadyExists` |
**Ontologies** | LinkedObjectNotFound | `from foundry_sdk.v1.ontologies.errors import LinkedObjectNotFound` |
**Ontologies** | LinkTypeNotFound | `from foundry_sdk.v1.ontologies.errors import LinkTypeNotFound` |
**Ontologies** | MalformedPropertyFilters | `from foundry_sdk.v1.ontologies.errors import MalformedPropertyFilters` |
**Ontologies** | MarketplaceActionMappingNotFound | `from foundry_sdk.v1.ontologies.errors import MarketplaceActionMappingNotFound` |
**Ontologies** | MarketplaceInstallationNotFound | `from foundry_sdk.v1.ontologies.errors import MarketplaceInstallationNotFound` |
**Ontologies** | MarketplaceLinkMappingNotFound | `from foundry_sdk.v1.ontologies.errors import MarketplaceLinkMappingNotFound` |
**Ontologies** | MarketplaceObjectMappingNotFound | `from foundry_sdk.v1.ontologies.errors import MarketplaceObjectMappingNotFound` |
**Ontologies** | MarketplaceQueryMappingNotFound | `from foundry_sdk.v1.ontologies.errors import MarketplaceQueryMappingNotFound` |
**Ontologies** | MarketplaceSdkActionMappingNotFound | `from foundry_sdk.v1.ontologies.errors import MarketplaceSdkActionMappingNotFound` |
**Ontologies** | MarketplaceSdkInstallationNotFound | `from foundry_sdk.v1.ontologies.errors import MarketplaceSdkInstallationNotFound` |
**Ontologies** | MarketplaceSdkLinkMappingNotFound | `from foundry_sdk.v1.ontologies.errors import MarketplaceSdkLinkMappingNotFound` |
**Ontologies** | MarketplaceSdkObjectMappingNotFound | `from foundry_sdk.v1.ontologies.errors import MarketplaceSdkObjectMappingNotFound` |
**Ontologies** | MarketplaceSdkPropertyMappingNotFound | `from foundry_sdk.v1.ontologies.errors import MarketplaceSdkPropertyMappingNotFound` |
**Ontologies** | MarketplaceSdkQueryMappingNotFound | `from foundry_sdk.v1.ontologies.errors import MarketplaceSdkQueryMappingNotFound` |
**Ontologies** | MissingParameter | `from foundry_sdk.v1.ontologies.errors import MissingParameter` |
**Ontologies** | MultipleGroupByOnFieldNotSupported | `from foundry_sdk.v1.ontologies.errors import MultipleGroupByOnFieldNotSupported` |
**Ontologies** | MultiplePropertyValuesNotSupported | `from foundry_sdk.v1.ontologies.errors import MultiplePropertyValuesNotSupported` |
**Ontologies** | NotCipherFormatted | `from foundry_sdk.v1.ontologies.errors import NotCipherFormatted` |
**Ontologies** | ObjectAlreadyExists | `from foundry_sdk.v1.ontologies.errors import ObjectAlreadyExists` |
**Ontologies** | ObjectChanged | `from foundry_sdk.v1.ontologies.errors import ObjectChanged` |
**Ontologies** | ObjectNotFound | `from foundry_sdk.v1.ontologies.errors import ObjectNotFound` |
**Ontologies** | ObjectSetNotFound | `from foundry_sdk.v1.ontologies.errors import ObjectSetNotFound` |
**Ontologies** | ObjectsExceededLimit | `from foundry_sdk.v1.ontologies.errors import ObjectsExceededLimit` |
**Ontologies** | ObjectTypeNotFound | `from foundry_sdk.v1.ontologies.errors import ObjectTypeNotFound` |
**Ontologies** | ObjectTypeNotSynced | `from foundry_sdk.v1.ontologies.errors import ObjectTypeNotSynced` |
**Ontologies** | ObjectTypesNotSynced | `from foundry_sdk.v1.ontologies.errors import ObjectTypesNotSynced` |
**Ontologies** | OntologyApiNameNotUnique | `from foundry_sdk.v1.ontologies.errors import OntologyApiNameNotUnique` |
**Ontologies** | OntologyEditsExceededLimit | `from foundry_sdk.v1.ontologies.errors import OntologyEditsExceededLimit` |
**Ontologies** | OntologyNotFound | `from foundry_sdk.v1.ontologies.errors import OntologyNotFound` |
**Ontologies** | OntologySyncing | `from foundry_sdk.v1.ontologies.errors import OntologySyncing` |
**Ontologies** | OntologySyncingObjectTypes | `from foundry_sdk.v1.ontologies.errors import OntologySyncingObjectTypes` |
**Ontologies** | ParameterObjectNotFound | `from foundry_sdk.v1.ontologies.errors import ParameterObjectNotFound` |
**Ontologies** | ParameterObjectSetRidNotFound | `from foundry_sdk.v1.ontologies.errors import ParameterObjectSetRidNotFound` |
**Ontologies** | ParametersNotFound | `from foundry_sdk.v1.ontologies.errors import ParametersNotFound` |
**Ontologies** | ParameterTypeNotSupported | `from foundry_sdk.v1.ontologies.errors import ParameterTypeNotSupported` |
**Ontologies** | ParentAttachmentPermissionDenied | `from foundry_sdk.v1.ontologies.errors import ParentAttachmentPermissionDenied` |
**Ontologies** | PropertiesHaveDifferentIds | `from foundry_sdk.v1.ontologies.errors import PropertiesHaveDifferentIds` |
**Ontologies** | PropertiesNotFilterable | `from foundry_sdk.v1.ontologies.errors import PropertiesNotFilterable` |
**Ontologies** | PropertiesNotFound | `from foundry_sdk.v1.ontologies.errors import PropertiesNotFound` |
**Ontologies** | PropertiesNotSearchable | `from foundry_sdk.v1.ontologies.errors import PropertiesNotSearchable` |
**Ontologies** | PropertiesNotSortable | `from foundry_sdk.v1.ontologies.errors import PropertiesNotSortable` |
**Ontologies** | PropertyApiNameNotFound | `from foundry_sdk.v1.ontologies.errors import PropertyApiNameNotFound` |
**Ontologies** | PropertyBaseTypeNotSupported | `from foundry_sdk.v1.ontologies.errors import PropertyBaseTypeNotSupported` |
**Ontologies** | PropertyFiltersNotSupported | `from foundry_sdk.v1.ontologies.errors import PropertyFiltersNotSupported` |
**Ontologies** | PropertyNotFound | `from foundry_sdk.v1.ontologies.errors import PropertyNotFound` |
**Ontologies** | PropertyTypeDoesNotSupportNearestNeighbors | `from foundry_sdk.v1.ontologies.errors import PropertyTypeDoesNotSupportNearestNeighbors` |
**Ontologies** | PropertyTypeNotFound | `from foundry_sdk.v1.ontologies.errors import PropertyTypeNotFound` |
**Ontologies** | PropertyTypeRidNotFound | `from foundry_sdk.v1.ontologies.errors import PropertyTypeRidNotFound` |
**Ontologies** | PropertyTypesSearchNotSupported | `from foundry_sdk.v1.ontologies.errors import PropertyTypesSearchNotSupported` |
**Ontologies** | QueryEncounteredUserFacingError | `from foundry_sdk.v1.ontologies.errors import QueryEncounteredUserFacingError` |
**Ontologies** | QueryMemoryExceededLimit | `from foundry_sdk.v1.ontologies.errors import QueryMemoryExceededLimit` |
**Ontologies** | QueryNotFound | `from foundry_sdk.v1.ontologies.errors import QueryNotFound` |
**Ontologies** | QueryRuntimeError | `from foundry_sdk.v1.ontologies.errors import QueryRuntimeError` |
**Ontologies** | QueryTimeExceededLimit | `from foundry_sdk.v1.ontologies.errors import QueryTimeExceededLimit` |
**Ontologies** | QueryVersionNotFound | `from foundry_sdk.v1.ontologies.errors import QueryVersionNotFound` |
**Ontologies** | RateLimitReached | `from foundry_sdk.v1.ontologies.errors import RateLimitReached` |
**Ontologies** | SharedPropertiesNotFound | `from foundry_sdk.v1.ontologies.errors import SharedPropertiesNotFound` |
**Ontologies** | SharedPropertyTypeNotFound | `from foundry_sdk.v1.ontologies.errors import SharedPropertyTypeNotFound` |
**Ontologies** | TooManyNearestNeighborsRequested | `from foundry_sdk.v1.ontologies.errors import TooManyNearestNeighborsRequested` |
**Ontologies** | UnauthorizedCipherOperation | `from foundry_sdk.v1.ontologies.errors import UnauthorizedCipherOperation` |
**Ontologies** | UndecryptableValue | `from foundry_sdk.v1.ontologies.errors import UndecryptableValue` |
**Ontologies** | UnknownParameter | `from foundry_sdk.v1.ontologies.errors import UnknownParameter` |
**Ontologies** | UnsupportedObjectSet | `from foundry_sdk.v1.ontologies.errors import UnsupportedObjectSet` |
**Ontologies** | ValueTypeNotFound | `from foundry_sdk.v1.ontologies.errors import ValueTypeNotFound` |
**Ontologies** | ViewObjectPermissionDenied | `from foundry_sdk.v1.ontologies.errors import ViewObjectPermissionDenied` |


## Contributions

This repository does not accept code contributions.

If you have any questions, concerns, or ideas for improvements, create an
issue with Palantir Support.

## License
This project is made available under the [Apache 2.0 License](/LICENSE).
