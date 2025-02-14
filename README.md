# Foundry Platform SDK

![Supported Python Versions](https://img.shields.io/pypi/pyversions/foundry-platform-sdk)
[![PyPI Version](https://img.shields.io/pypi/v/foundry-platform-sdk)](https://pypi.org/project/foundry-platform-sdk/)
[![License](https://img.shields.io/badge/License-Apache%202.0-lightgrey.svg)](https://opensource.org/licenses/Apache-2.0)

> [!WARNING]
> This SDK is incubating and subject to change.

The Foundry Platform SDK is a Python SDK built on top of the Foundry API. Review [Foundry API documentation](https://www.palantir.com/docs/foundry/api/) for more details.

> [!NOTE]
> This Python package is automatically generated based on the Foundry API specification.


<a id="sdk-vs-sdk"></a>
## Foundry Platform SDK vs. Ontology SDK
Palantir provides two different Python Software Development Kits (SDKs) for interacting with Foundry. Make sure to choose the correct SDK for your use case. As a general rule of thumb, any applications which leverage the Ontology should use the Ontology SDK for a superior development experience.

> [!IMPORTANT]
> Make sure to understand the difference between the Foundry SDK and the Ontology SDK. Review this section before continuing with the installation of this library.

### Ontology SDK
The Ontology SDK allows you to access the full power of the Ontology directly from your development environment. You can generate the Ontology SDK using the Developer Console, a portal for creating and managing applications using Palantir APIs. Review the [Ontology SDK documentation](https://www.palantir.com/docs/foundry/ontology-sdk) for more information.

### Foundry Platform SDK
The Foundry Platform Software Development Kit (SDK) is generated from the Foundry API specification
file. The intention of this SDK is to encompass endpoints related to interacting
with the platform itself. Although there are Ontology services included by this SDK, this SDK surfaces endpoints
for interacting with Ontological resources such as object types, link types, and action types. In contrast, the OSDK allows you to interact with objects, links and Actions (for example, querying your objects, applying an action).

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

This SDK exposes several clients, one for each major version of the API. For example, the latest major version of the
SDK is **v2** and is exposed using the `FoundryClient` located in the
`foundry.v2` package. To use this SDK, you must choose the specific client (or clients)
you would like to use.

More information about how the API is versioned can be found [here](https://www.palantir.com/docs/foundry/api/general/overview/versioning/).

<a id="authorization"></a>
## Authorization and client initalization
There are two options for authorizing the SDK.

### User token
> [!WARNING]
> User tokens are associated with your personal Foundry user account and must not be used in
> production applications or committed to shared or public code repositories. We recommend
> you store test API tokens as environment variables during development. For authorizing
> production applications, you should register an OAuth2 application (see
> [OAuth2 Client](#oauth2-client) below for more details).

<!--
Configuration for hostname and an authentication token are provided by environment
variables (`PALANTIR_HOSTNAME`, `PALANTIR_TOKEN`)

* `PALANTIR_HOSTNAME` is the hostname of your instance (such as `example.palantirfoundry.com`)
* `PALANTIR_TOKEN` is a token acquired from the `Tokens` section of **Foundry Settings**


You can alternatively pass in the hostname and token as keyword arguments when
initializing the `UserTokenAuth`:
-->

You can pass in the hostname and token as keyword arguments when
initializing the `UserTokenAuth`:

```python
import foundry
import foundry.v2

foundry_client = foundry.v2.FoundryClient(
    auth=foundry.UserTokenAuth(token=os.environ["BEARER_TOKEN"]),
    hostname="example.palantirfoundry.com",
)
```

<a id="oauth2-client"></a>
### OAuth2 Client
OAuth2 clients are the recommended way to connect to Foundry in production applications. Currently, this SDK
natively supports the [client credentials grant flow](https://www.palantir.com/docs/foundry/platform-security-third-party/writing-oauth2-clients/#client-credentials-grant).
The token obtained by this grant can be used to access resources on behalf of the created service user. To use this
authentication method, you will first need to register a third-party application in Foundry by following [the guide on third-party application registration](https://www.palantir.com/docs/foundry/platform-security-third-party/register-3pa).

To use the confidential client functionality, you first need to contstruct a
`ConfidentialClientAuth` object. As these service user tokens have a short
lifespan (one hour), we automatically retry all operations one time if a `401`
(Unauthorized) error is thrown after refreshing the token.

```python
import foundry

auth = foundry.ConfidentialClientAuth(
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
import foundry.v2

foundry_client = foundry.v2.FoundryClient(auth=auth, hostname="example.palantirfoundry.com")
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
from foundry.v1 import FoundryClient
import foundry
from pprint import pprint

foundry_client = FoundryClient(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"
# BranchId |
branch_id = "my-branch"
# Optional[TransactionRid] |
transaction_rid = None


try:
    api_response = foundry_client.datasets.Dataset.Branch.create(
        dataset_rid,
        branch_id=branch_id,
        transaction_rid=transaction_rid,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry.PalantirRPCException as e:
    print("HTTP error when calling Branch.create: %s\n" % e)

```

Want to learn more about this Foundry SDK library? Review the following sections.

↳ [Error handling](#errors): Learn more about HTTP & data validation error handling  
↳ [Pagination](#pagination): Learn how to work with paginated endpoints in the SDK  
↳ [Streaming](#binary-streaming): Learn how to stream binary data from Foundry  
↳ [Static type analysis](#static-types): Learn about the static type analysis capabilities of this library  
↳ [HTTP Session Configuration](#session-config): Learn how to configure the HTTP session.  

## Error handling
### Data validation
The SDK employs [Pydantic](https://docs.pydantic.dev/latest/) for runtime validation
of arguments. In the example below, we are passing in a number to `transaction_rid`
which should actually be a string type:

```python
foundry_client.datasets.Dataset.Branch.create(
    "ri.foundry.main.dataset.abc",
    name="123",
    transaction_rid=123,
)
```

If you did this, you would receive an error that looks something like:

```
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
When an HTTP error status is returned, a `PalantirRPCException` is thrown. There are several
subclasses that be caught for more specific conditions, all of which inherit from
`PalantirRPCException`.


| Status Code | Error Class                |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `UnauthorizedError`        |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500,<600  | `InternalServerError`      |
| Other       | `PalantirRPCException`     |

```python
from foundry import PalantirRPCException
from foundry import NotFoundError
from foundry import RateLimitError


try:
    api_response = foundry_client.datasets.Transaction.abort(dataset_rid, transaction_rid)
    ...
except NotFoundError as e:
    print("Dataset or Transaction not found", e)
except RateLimitError as e:
    print("We are aborting too many Transactions", e)
except PalantirRPCException as e:
    print("Another HTTP exception occurred", e)
```

All HTTP exceptions will have the following properties. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors) for details about the Foundry error information.

| Property          | Type                   | Description                                                                                                                    |
| ----------------- | -----------------------| ------------------------------------------------------------------------------------------------------------------------------ |
| name              | str                    | The Palantir error name. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors).        |
| error_instance_id | str                    | The Palantir error instance ID. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors). |
| parameters        | Dict[str, Any]         | The Palantir error parameters. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors).  |

### Other exceptions
There are a handful of other exception classes that could be thrown when instantiating or using a client.

| ErrorClass               | Thrown Directly | Description                                                                                                                       |
| ------------------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------- |     
| NotAuthenticated         | Yes             | You used either `ConfidentialClientAuth` or `PublicClientAuth` to make an API call without going through the OAuth process first. |           
| ConnectionError          | Yes             | An issue occurred when connecting to the server. This also catches `ProxyError`.                                                  |
| ProxyError               | Yes             | An issue occurred when connecting to or authenticating with a proxy server.                                                       |
| TimeoutError             | No              | The request timed out. This catches both `ConnectTimeout`, `ReadTimeout` and `WriteTimeout`.                                                      |
| ConnectTimeout           | Yes             | The request timed out when attempting to connect to the server.                                                                   |
| ReadTimeout              | Yes             | The server did not send any data in the allotted amount of time.                                                                  |
| WriteTimeout             | Yes             | There was a timeout when writing data to the server.                                                                              |
| StreamConsumedError      | Yes             | The content of the given stream has already been consumed.                                                                        |
| SDKInternalError         | Yes             | An unexpected issue occurred and should be reported.                                                                              |

<a id="pagination"></a>
## Pagination
When calling any iterator endpoints, we return a `Pager` class designed to simplify the process of working
with paginated API endpoints. This class provides a convenient way to fetch, iterate over, and manage pages
of data, while handling the underlying pagination logic.

To iterate over all items, you can simply create a `Pager` instance and use it in a for loop, like this:

```python
for branch in foundry_client.datasets.Dataset.Branch.list(dataset_rid):
    print(branch)
```

This will automatically fetch and iterate through all the pages of data from the specified API endpoint. For more granular control, you can manually fetch each page using the `next_page_token`.

```python
page = foundry_client.datasets.Dataset.Branch.list(dataset_rid)
while page.next_page_token:
    for branch in page.data:
        print(branch)

    page = foundry_client.datasets.Dataset.Branch.list(dataset_rid, page_token=page.next_page_token)
```


<a id="binary-streaming"></a>
## Streaming
This SDK supports streaming binary data using a separate streaming client accessible under
`with_streaming_response` on each Resource. To ensure the stream is closed, you need to use a context
manager when making a request with this client.

```python
# Non-streaming response
with open("profile_picture.png", "wb") as f:
    f.write(foundry_client.admin.User.profile_picture(user_id))

# Streaming response
with open("profile_picture.png", "wb") as f:
    with foundry_client.admin.User.with_streaming_response.profile_picture(user_id) as response:
        for chunk in response.iter_bytes():
            f.write(chunk)
```

<a id="static-types"></a>
## Static type analysis
This library uses [Pydantic](https://docs.pydantic.dev) for creating and validating data models which you will see in the
method definitions (see [Documentation for Models](#models-link) below for a full list of models). All request parameters with nested
fields are typed as a `Union` between a Pydantic [BaseModel](https://docs.pydantic.dev/latest/api/base_model/) class and a [TypedDict](https://docs.python.org/3/library/typing.html#typing.TypedDict) whereas responses use `Pydantic`
class. For example, here is how `Group.search` method is defined in the `Admin` namespace:

```python
    @pydantic.validate_call
    @handle_unexpected
    def search(
        self,
        *,
        where: Union[GroupSearchFilter, GroupSearchFilterDict],
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[int, pydantic.Field(gt=0)]] = None,
    ) -> SearchGroupsResponse:
        ...
```

In this example, `GroupSearchFilter` is a `BaseModel` class and `GroupSearchFilterDict` is a `TypedDict` class. When calling this method,
you can choose whether to pass in a class instance or a dict.

```python
import foundry.v2
from foundry.v2.admin.models import GroupSearchFilter

client = foundry.v2.FoundryClient(...)

# Class instance
result = client.admin.Group.search(where=GroupSearchFilter(type="queryString", value="John Doe"))

# Dict
result = client.admin.Group.search(where={"type": "queryString", "value": "John Doe"})
```

> [!TIP]
> A `Pydantic` model can be converted into its `TypedDict` representation using the `to_dict` method. For example, if you handle
> a variable of type `Branch` and you called `to_dict()` on that variable you would receive a `BranchDict`
> variable.

If you are using a static type checker (for example, [mypy](https://mypy-lang.org), [pyright](https://github.com/microsoft/pyright)), you
get static type analysis for the arguments you provide to the function and with the response. For example, if you pass an `int`
to `name` but `name` expects a string or if you try to access `branchName` on the returned [`Branch`](docs/Branch.md) object (the
property is actually called `name`), you will get the following errors:


```python
branch = foundry_client.datasets.Dataset.Branch.create(
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
from foundry import Config
from foundry import UserTokenAuth
from foundry.v2 imoprt FoundryClient

client = FoundryClient(
    auth=UserTokenAuth(...),
    hostname="example.palantirfoundry.com",
    config=Config(
        # Set the default headers for every request
        default_headers={"Foo": "Bar"},
        # Default to a 60 second timeout
        timeout=60,
        # Create a proxy for the https protocol
        proxies={
            "https": "https://10.10.1.10:1080"
        },
    )
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

## Common errors
This section will document any user-related errors with information on how you may be able to resolve them.

### ApiFeaturePreviewUsageOnly
This error indicates you are trying to use an endpoint in public preview and have not set `preview=True` when
calling the endpoint. Before doing so, note that this endpoint is
in preview state and breaking changes may occur at any time.

During the first phase of an endpoint's lifecycle, it may be in `Public Preview`
state. This indicates that the endpoint is in development and is not intended for
production use. 

<a id="apis-link"></a>
<a id="apis-v2-link"></a>
## Documentation for V2 API endpoints

Namespace | Resource | Operation | HTTP request |
------------ | ------------- | ------------- | ------------- |
**Admin** | Group | [**create**](docs/v2/Admin/Group.md#create) | **POST** /v2/admin/groups |
**Admin** | Group | [**delete**](docs/v2/Admin/Group.md#delete) | **DELETE** /v2/admin/groups/{groupId} |
**Admin** | Group | [**get**](docs/v2/Admin/Group.md#get) | **GET** /v2/admin/groups/{groupId} |
**Admin** | Group | [**get_batch**](docs/v2/Admin/Group.md#get_batch) | **POST** /v2/admin/groups/getBatch |
**Admin** | Group | [**list**](docs/v2/Admin/Group.md#list) | **GET** /v2/admin/groups |
**Admin** | Group | [**page**](docs/v2/Admin/Group.md#page) | **GET** /v2/admin/groups |
**Admin** | Group | [**search**](docs/v2/Admin/Group.md#search) | **POST** /v2/admin/groups/search |
**Admin** | GroupMember | [**add**](docs/v2/Admin/GroupMember.md#add) | **POST** /v2/admin/groups/{groupId}/groupMembers/add |
**Admin** | GroupMember | [**list**](docs/v2/Admin/GroupMember.md#list) | **GET** /v2/admin/groups/{groupId}/groupMembers |
**Admin** | GroupMember | [**page**](docs/v2/Admin/GroupMember.md#page) | **GET** /v2/admin/groups/{groupId}/groupMembers |
**Admin** | GroupMember | [**remove**](docs/v2/Admin/GroupMember.md#remove) | **POST** /v2/admin/groups/{groupId}/groupMembers/remove |
**Admin** | GroupMembership | [**list**](docs/v2/Admin/GroupMembership.md#list) | **GET** /v2/admin/users/{userId}/groupMemberships |
**Admin** | GroupMembership | [**page**](docs/v2/Admin/GroupMembership.md#page) | **GET** /v2/admin/users/{userId}/groupMemberships |
**Admin** | GroupProviderInfo | [**get**](docs/v2/Admin/GroupProviderInfo.md#get) | **GET** /v2/admin/groups/{groupId}/providerInfo |
**Admin** | GroupProviderInfo | [**replace**](docs/v2/Admin/GroupProviderInfo.md#replace) | **PUT** /v2/admin/groups/{groupId}/providerInfo |
**Admin** | Marking | [**create**](docs/v2/Admin/Marking.md#create) | **POST** /v2/admin/markings |
**Admin** | Marking | [**get**](docs/v2/Admin/Marking.md#get) | **GET** /v2/admin/markings/{markingId} |
**Admin** | Marking | [**get_batch**](docs/v2/Admin/Marking.md#get_batch) | **POST** /v2/admin/markings/getBatch |
**Admin** | Marking | [**list**](docs/v2/Admin/Marking.md#list) | **GET** /v2/admin/markings |
**Admin** | Marking | [**page**](docs/v2/Admin/Marking.md#page) | **GET** /v2/admin/markings |
**Admin** | MarkingCategory | [**get**](docs/v2/Admin/MarkingCategory.md#get) | **GET** /v2/admin/markingCategories/{markingCategoryId} |
**Admin** | MarkingCategory | [**list**](docs/v2/Admin/MarkingCategory.md#list) | **GET** /v2/admin/markingCategories |
**Admin** | MarkingCategory | [**page**](docs/v2/Admin/MarkingCategory.md#page) | **GET** /v2/admin/markingCategories |
**Admin** | MarkingMember | [**add**](docs/v2/Admin/MarkingMember.md#add) | **POST** /v2/admin/markings/{markingId}/markingMembers/add |
**Admin** | MarkingMember | [**list**](docs/v2/Admin/MarkingMember.md#list) | **GET** /v2/admin/markings/{markingId}/markingMembers |
**Admin** | MarkingMember | [**page**](docs/v2/Admin/MarkingMember.md#page) | **GET** /v2/admin/markings/{markingId}/markingMembers |
**Admin** | MarkingMember | [**remove**](docs/v2/Admin/MarkingMember.md#remove) | **POST** /v2/admin/markings/{markingId}/markingMembers/remove |
**Admin** | MarkingRoleAssignment | [**add**](docs/v2/Admin/MarkingRoleAssignment.md#add) | **POST** /v2/admin/markings/{markingId}/roleAssignments/add |
**Admin** | MarkingRoleAssignment | [**list**](docs/v2/Admin/MarkingRoleAssignment.md#list) | **GET** /v2/admin/markings/{markingId}/roleAssignments |
**Admin** | MarkingRoleAssignment | [**page**](docs/v2/Admin/MarkingRoleAssignment.md#page) | **GET** /v2/admin/markings/{markingId}/roleAssignments |
**Admin** | MarkingRoleAssignment | [**remove**](docs/v2/Admin/MarkingRoleAssignment.md#remove) | **POST** /v2/admin/markings/{markingId}/roleAssignments/remove |
**Admin** | Organization | [**get**](docs/v2/Admin/Organization.md#get) | **GET** /v2/admin/organizations/{organizationRid} |
**Admin** | Organization | [**replace**](docs/v2/Admin/Organization.md#replace) | **PUT** /v2/admin/organizations/{organizationRid} |
**Admin** | User | [**delete**](docs/v2/Admin/User.md#delete) | **DELETE** /v2/admin/users/{userId} |
**Admin** | User | [**get**](docs/v2/Admin/User.md#get) | **GET** /v2/admin/users/{userId} |
**Admin** | User | [**get_batch**](docs/v2/Admin/User.md#get_batch) | **POST** /v2/admin/users/getBatch |
**Admin** | User | [**get_current**](docs/v2/Admin/User.md#get_current) | **GET** /v2/admin/users/getCurrent |
**Admin** | User | [**get_markings**](docs/v2/Admin/User.md#get_markings) | **GET** /v2/admin/users/{userId}/getMarkings |
**Admin** | User | [**list**](docs/v2/Admin/User.md#list) | **GET** /v2/admin/users |
**Admin** | User | [**page**](docs/v2/Admin/User.md#page) | **GET** /v2/admin/users |
**Admin** | User | [**profile_picture**](docs/v2/Admin/User.md#profile_picture) | **GET** /v2/admin/users/{userId}/profilePicture |
**Admin** | User | [**search**](docs/v2/Admin/User.md#search) | **POST** /v2/admin/users/search |
**Admin** | UserProviderInfo | [**get**](docs/v2/Admin/UserProviderInfo.md#get) | **GET** /v2/admin/users/{userId}/providerInfo |
**Admin** | UserProviderInfo | [**replace**](docs/v2/Admin/UserProviderInfo.md#replace) | **PUT** /v2/admin/users/{userId}/providerInfo |
**AipAgents** | Agent | [**all_sessions**](docs/v2/AipAgents/Agent.md#all_sessions) | **GET** /v2/aipAgents/agents/allSessions |
**AipAgents** | Agent | [**all_sessions_page**](docs/v2/AipAgents/Agent.md#all_sessions_page) | **GET** /v2/aipAgents/agents/allSessions |
**AipAgents** | Agent | [**get**](docs/v2/AipAgents/Agent.md#get) | **GET** /v2/aipAgents/agents/{agentRid} |
**AipAgents** | AgentVersion | [**get**](docs/v2/AipAgents/AgentVersion.md#get) | **GET** /v2/aipAgents/agents/{agentRid}/agentVersions/{agentVersionString} |
**AipAgents** | AgentVersion | [**list**](docs/v2/AipAgents/AgentVersion.md#list) | **GET** /v2/aipAgents/agents/{agentRid}/agentVersions |
**AipAgents** | AgentVersion | [**page**](docs/v2/AipAgents/AgentVersion.md#page) | **GET** /v2/aipAgents/agents/{agentRid}/agentVersions |
**AipAgents** | Content | [**get**](docs/v2/AipAgents/Content.md#get) | **GET** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/content |
**AipAgents** | Session | [**blocking_continue**](docs/v2/AipAgents/Session.md#blocking_continue) | **POST** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/blockingContinue |
**AipAgents** | Session | [**cancel**](docs/v2/AipAgents/Session.md#cancel) | **POST** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/cancel |
**AipAgents** | Session | [**create**](docs/v2/AipAgents/Session.md#create) | **POST** /v2/aipAgents/agents/{agentRid}/sessions |
**AipAgents** | Session | [**get**](docs/v2/AipAgents/Session.md#get) | **GET** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid} |
**AipAgents** | Session | [**list**](docs/v2/AipAgents/Session.md#list) | **GET** /v2/aipAgents/agents/{agentRid}/sessions |
**AipAgents** | Session | [**page**](docs/v2/AipAgents/Session.md#page) | **GET** /v2/aipAgents/agents/{agentRid}/sessions |
**AipAgents** | Session | [**rag_context**](docs/v2/AipAgents/Session.md#rag_context) | **PUT** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/ragContext |
**AipAgents** | Session | [**streaming_continue**](docs/v2/AipAgents/Session.md#streaming_continue) | **POST** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/streamingContinue |
**Connectivity** | Connection | [**update_secrets**](docs/v2/Connectivity/Connection.md#update_secrets) | **POST** /v2/connectivity/connections/{connectionRid}/updateSecrets |
**Connectivity** | FileImport | [**create**](docs/v2/Connectivity/FileImport.md#create) | **POST** /v2/connectivity/connections/{connectionRid}/fileImports |
**Connectivity** | FileImport | [**delete**](docs/v2/Connectivity/FileImport.md#delete) | **DELETE** /v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid} |
**Connectivity** | FileImport | [**execute**](docs/v2/Connectivity/FileImport.md#execute) | **POST** /v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}/execute |
**Connectivity** | FileImport | [**get**](docs/v2/Connectivity/FileImport.md#get) | **GET** /v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid} |
**Connectivity** | FileImport | [**list**](docs/v2/Connectivity/FileImport.md#list) | **GET** /v2/connectivity/connections/{connectionRid}/fileImports |
**Connectivity** | FileImport | [**page**](docs/v2/Connectivity/FileImport.md#page) | **GET** /v2/connectivity/connections/{connectionRid}/fileImports |
**Connectivity** | TableImport | [**create**](docs/v2/Connectivity/TableImport.md#create) | **POST** /v2/connectivity/connections/{connectionRid}/tableImports |
**Connectivity** | TableImport | [**delete**](docs/v2/Connectivity/TableImport.md#delete) | **DELETE** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid} |
**Connectivity** | TableImport | [**execute**](docs/v2/Connectivity/TableImport.md#execute) | **POST** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid}/execute |
**Connectivity** | TableImport | [**get**](docs/v2/Connectivity/TableImport.md#get) | **GET** /v2/connectivity/connections/{connectionRid}/tableImports/{tableImportRid} |
**Connectivity** | TableImport | [**list**](docs/v2/Connectivity/TableImport.md#list) | **GET** /v2/connectivity/connections/{connectionRid}/tableImports |
**Connectivity** | TableImport | [**page**](docs/v2/Connectivity/TableImport.md#page) | **GET** /v2/connectivity/connections/{connectionRid}/tableImports |
**Datasets** | Branch | [**create**](docs/v2/Datasets/Branch.md#create) | **POST** /v2/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**delete**](docs/v2/Datasets/Branch.md#delete) | **DELETE** /v2/datasets/{datasetRid}/branches/{branchName} |
**Datasets** | Branch | [**get**](docs/v2/Datasets/Branch.md#get) | **GET** /v2/datasets/{datasetRid}/branches/{branchName} |
**Datasets** | Branch | [**list**](docs/v2/Datasets/Branch.md#list) | **GET** /v2/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**page**](docs/v2/Datasets/Branch.md#page) | **GET** /v2/datasets/{datasetRid}/branches |
**Datasets** | Dataset | [**create**](docs/v2/Datasets/Dataset.md#create) | **POST** /v2/datasets |
**Datasets** | Dataset | [**get**](docs/v2/Datasets/Dataset.md#get) | **GET** /v2/datasets/{datasetRid} |
**Datasets** | Dataset | [**read_table**](docs/v2/Datasets/Dataset.md#read_table) | **GET** /v2/datasets/{datasetRid}/readTable |
**Datasets** | File | [**content**](docs/v2/Datasets/File.md#content) | **GET** /v2/datasets/{datasetRid}/files/{filePath}/content |
**Datasets** | File | [**delete**](docs/v2/Datasets/File.md#delete) | **DELETE** /v2/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**get**](docs/v2/Datasets/File.md#get) | **GET** /v2/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**list**](docs/v2/Datasets/File.md#list) | **GET** /v2/datasets/{datasetRid}/files |
**Datasets** | File | [**page**](docs/v2/Datasets/File.md#page) | **GET** /v2/datasets/{datasetRid}/files |
**Datasets** | File | [**upload**](docs/v2/Datasets/File.md#upload) | **POST** /v2/datasets/{datasetRid}/files/{filePath}/upload |
**Datasets** | Transaction | [**abort**](docs/v2/Datasets/Transaction.md#abort) | **POST** /v2/datasets/{datasetRid}/transactions/{transactionRid}/abort |
**Datasets** | Transaction | [**commit**](docs/v2/Datasets/Transaction.md#commit) | **POST** /v2/datasets/{datasetRid}/transactions/{transactionRid}/commit |
**Datasets** | Transaction | [**create**](docs/v2/Datasets/Transaction.md#create) | **POST** /v2/datasets/{datasetRid}/transactions |
**Datasets** | Transaction | [**get**](docs/v2/Datasets/Transaction.md#get) | **GET** /v2/datasets/{datasetRid}/transactions/{transactionRid} |
**Filesystem** | Folder | [**children**](docs/v2/Filesystem/Folder.md#children) | **GET** /v2/filesystem/folders/{folderRid}/children |
**Filesystem** | Folder | [**children_page**](docs/v2/Filesystem/Folder.md#children_page) | **GET** /v2/filesystem/folders/{folderRid}/children |
**Filesystem** | Folder | [**create**](docs/v2/Filesystem/Folder.md#create) | **POST** /v2/filesystem/folders |
**Filesystem** | Folder | [**get**](docs/v2/Filesystem/Folder.md#get) | **GET** /v2/filesystem/folders/{folderRid} |
**Filesystem** | Project | [**create**](docs/v2/Filesystem/Project.md#create) | **POST** /v2/filesystem/projects/create |
**MediaSets** | MediaSet | [**abort**](docs/v2/MediaSets/MediaSet.md#abort) | **POST** /v2/mediasets/{mediaSetRid}/transactions/{transactionId}/abort |
**MediaSets** | MediaSet | [**commit**](docs/v2/MediaSets/MediaSet.md#commit) | **POST** /v2/mediasets/{mediaSetRid}/transactions/{transactionId}/commit |
**MediaSets** | MediaSet | [**create**](docs/v2/MediaSets/MediaSet.md#create) | **POST** /v2/mediasets/{mediaSetRid}/transactions |
**MediaSets** | MediaSet | [**info**](docs/v2/MediaSets/MediaSet.md#info) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid} |
**MediaSets** | MediaSet | [**read**](docs/v2/MediaSets/MediaSet.md#read) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/content |
**MediaSets** | MediaSet | [**reference**](docs/v2/MediaSets/MediaSet.md#reference) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/reference |
**MediaSets** | MediaSet | [**upload**](docs/v2/MediaSets/MediaSet.md#upload) | **POST** /v2/mediasets/{mediaSetRid}/items |
**Ontologies** | Action | [**apply**](docs/v2/Ontologies/Action.md#apply) | **POST** /v2/ontologies/{ontology}/actions/{action}/apply |
**Ontologies** | Action | [**apply_batch**](docs/v2/Ontologies/Action.md#apply_batch) | **POST** /v2/ontologies/{ontology}/actions/{action}/applyBatch |
**Ontologies** | ActionType | [**get**](docs/v2/Ontologies/ActionType.md#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} |
**Ontologies** | ActionType | [**list**](docs/v2/Ontologies/ActionType.md#list) | **GET** /v2/ontologies/{ontology}/actionTypes |
**Ontologies** | ActionType | [**page**](docs/v2/Ontologies/ActionType.md#page) | **GET** /v2/ontologies/{ontology}/actionTypes |
**Ontologies** | Attachment | [**get**](docs/v2/Ontologies/Attachment.md#get) | **GET** /v2/ontologies/attachments/{attachmentRid} |
**Ontologies** | Attachment | [**read**](docs/v2/Ontologies/Attachment.md#read) | **GET** /v2/ontologies/attachments/{attachmentRid}/content |
**Ontologies** | Attachment | [**upload**](docs/v2/Ontologies/Attachment.md#upload) | **POST** /v2/ontologies/attachments/upload |
**Ontologies** | AttachmentProperty | [**get_attachment**](docs/v2/Ontologies/AttachmentProperty.md#get_attachment) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property} |
**Ontologies** | AttachmentProperty | [**get_attachment_by_rid**](docs/v2/Ontologies/AttachmentProperty.md#get_attachment_by_rid) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid} |
**Ontologies** | AttachmentProperty | [**read_attachment**](docs/v2/Ontologies/AttachmentProperty.md#read_attachment) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/content |
**Ontologies** | AttachmentProperty | [**read_attachment_by_rid**](docs/v2/Ontologies/AttachmentProperty.md#read_attachment_by_rid) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}/content |
**Ontologies** | LinkedObject | [**get_linked_object**](docs/v2/Ontologies/LinkedObject.md#get_linked_object) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey} |
**Ontologies** | LinkedObject | [**list_linked_objects**](docs/v2/Ontologies/LinkedObject.md#list_linked_objects) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType} |
**Ontologies** | LinkedObject | [**page_linked_objects**](docs/v2/Ontologies/LinkedObject.md#page_linked_objects) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType} |
**Ontologies** | ObjectType | [**get**](docs/v2/Ontologies/ObjectType.md#get) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType} |
**Ontologies** | ObjectType | [**get_outgoing_link_type**](docs/v2/Ontologies/ObjectType.md#get_outgoing_link_type) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
**Ontologies** | ObjectType | [**list**](docs/v2/Ontologies/ObjectType.md#list) | **GET** /v2/ontologies/{ontology}/objectTypes |
**Ontologies** | ObjectType | [**list_outgoing_link_types**](docs/v2/Ontologies/ObjectType.md#list_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | ObjectType | [**page**](docs/v2/Ontologies/ObjectType.md#page) | **GET** /v2/ontologies/{ontology}/objectTypes |
**Ontologies** | ObjectType | [**page_outgoing_link_types**](docs/v2/Ontologies/ObjectType.md#page_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | Ontology | [**get**](docs/v2/Ontologies/Ontology.md#get) | **GET** /v2/ontologies/{ontology} |
**Ontologies** | Ontology | [**get_full_metadata**](docs/v2/Ontologies/Ontology.md#get_full_metadata) | **GET** /v2/ontologies/{ontology}/fullMetadata |
**Ontologies** | OntologyInterface | [**get**](docs/v2/Ontologies/OntologyInterface.md#get) | **GET** /v2/ontologies/{ontology}/interfaceTypes/{interfaceType} |
**Ontologies** | OntologyInterface | [**list**](docs/v2/Ontologies/OntologyInterface.md#list) | **GET** /v2/ontologies/{ontology}/interfaceTypes |
**Ontologies** | OntologyInterface | [**page**](docs/v2/Ontologies/OntologyInterface.md#page) | **GET** /v2/ontologies/{ontology}/interfaceTypes |
**Ontologies** | OntologyObject | [**aggregate**](docs/v2/Ontologies/OntologyObject.md#aggregate) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/aggregate |
**Ontologies** | OntologyObject | [**get**](docs/v2/Ontologies/OntologyObject.md#get) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey} |
**Ontologies** | OntologyObject | [**list**](docs/v2/Ontologies/OntologyObject.md#list) | **GET** /v2/ontologies/{ontology}/objects/{objectType} |
**Ontologies** | OntologyObject | [**page**](docs/v2/Ontologies/OntologyObject.md#page) | **GET** /v2/ontologies/{ontology}/objects/{objectType} |
**Ontologies** | OntologyObject | [**search**](docs/v2/Ontologies/OntologyObject.md#search) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/search |
**Ontologies** | OntologyObjectSet | [**aggregate**](docs/v2/Ontologies/OntologyObjectSet.md#aggregate) | **POST** /v2/ontologies/{ontology}/objectSets/aggregate |
**Ontologies** | OntologyObjectSet | [**create_temporary**](docs/v2/Ontologies/OntologyObjectSet.md#create_temporary) | **POST** /v2/ontologies/{ontology}/objectSets/createTemporary |
**Ontologies** | OntologyObjectSet | [**load**](docs/v2/Ontologies/OntologyObjectSet.md#load) | **POST** /v2/ontologies/{ontology}/objectSets/loadObjects |
**Ontologies** | Query | [**execute**](docs/v2/Ontologies/Query.md#execute) | **POST** /v2/ontologies/{ontology}/queries/{queryApiName}/execute |
**Ontologies** | QueryType | [**get**](docs/v2/Ontologies/QueryType.md#get) | **GET** /v2/ontologies/{ontology}/queryTypes/{queryApiName} |
**Ontologies** | QueryType | [**list**](docs/v2/Ontologies/QueryType.md#list) | **GET** /v2/ontologies/{ontology}/queryTypes |
**Ontologies** | QueryType | [**page**](docs/v2/Ontologies/QueryType.md#page) | **GET** /v2/ontologies/{ontology}/queryTypes |
**Ontologies** | TimeSeriesPropertyV2 | [**get_first_point**](docs/v2/Ontologies/TimeSeriesPropertyV2.md#get_first_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/firstPoint |
**Ontologies** | TimeSeriesPropertyV2 | [**get_last_point**](docs/v2/Ontologies/TimeSeriesPropertyV2.md#get_last_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/lastPoint |
**Ontologies** | TimeSeriesPropertyV2 | [**stream_points**](docs/v2/Ontologies/TimeSeriesPropertyV2.md#stream_points) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamPoints |
**Orchestration** | Build | [**cancel**](docs/v2/Orchestration/Build.md#cancel) | **POST** /v2/orchestration/builds/{buildRid}/cancel |
**Orchestration** | Build | [**create**](docs/v2/Orchestration/Build.md#create) | **POST** /v2/orchestration/builds/create |
**Orchestration** | Build | [**get**](docs/v2/Orchestration/Build.md#get) | **GET** /v2/orchestration/builds/{buildRid} |
**Orchestration** | Build | [**get_batch**](docs/v2/Orchestration/Build.md#get_batch) | **POST** /v2/orchestration/builds/getBatch |
**Orchestration** | Schedule | [**create**](docs/v2/Orchestration/Schedule.md#create) | **POST** /v2/orchestration/schedules |
**Orchestration** | Schedule | [**delete**](docs/v2/Orchestration/Schedule.md#delete) | **DELETE** /v2/orchestration/schedules/{scheduleRid} |
**Orchestration** | Schedule | [**get**](docs/v2/Orchestration/Schedule.md#get) | **GET** /v2/orchestration/schedules/{scheduleRid} |
**Orchestration** | Schedule | [**pause**](docs/v2/Orchestration/Schedule.md#pause) | **POST** /v2/orchestration/schedules/{scheduleRid}/pause |
**Orchestration** | Schedule | [**replace**](docs/v2/Orchestration/Schedule.md#replace) | **PUT** /v2/orchestration/schedules/{scheduleRid} |
**Orchestration** | Schedule | [**run**](docs/v2/Orchestration/Schedule.md#run) | **POST** /v2/orchestration/schedules/{scheduleRid}/run |
**Orchestration** | Schedule | [**runs**](docs/v2/Orchestration/Schedule.md#runs) | **GET** /v2/orchestration/schedules/{scheduleRid}/runs |
**Orchestration** | Schedule | [**runs_page**](docs/v2/Orchestration/Schedule.md#runs_page) | **GET** /v2/orchestration/schedules/{scheduleRid}/runs |
**Orchestration** | Schedule | [**unpause**](docs/v2/Orchestration/Schedule.md#unpause) | **POST** /v2/orchestration/schedules/{scheduleRid}/unpause |
**Orchestration** | ScheduleVersion | [**get**](docs/v2/Orchestration/ScheduleVersion.md#get) | **GET** /v2/orchestration/scheduleVersions/{scheduleVersionRid} |
**Orchestration** | ScheduleVersion | [**schedule**](docs/v2/Orchestration/ScheduleVersion.md#schedule) | **GET** /v2/orchestration/scheduleVersions/{scheduleVersionRid}/schedule |
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
**ThirdPartyApplications** | Version | [**page**](docs/v2/ThirdPartyApplications/Version.md#page) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions |
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
**Datasets** | Branch | [**page**](docs/v1/Datasets/Branch.md#page) | **GET** /v1/datasets/{datasetRid}/branches |
**Datasets** | Dataset | [**create**](docs/v1/Datasets/Dataset.md#create) | **POST** /v1/datasets |
**Datasets** | Dataset | [**get**](docs/v1/Datasets/Dataset.md#get) | **GET** /v1/datasets/{datasetRid} |
**Datasets** | Dataset | [**read**](docs/v1/Datasets/Dataset.md#read) | **GET** /v1/datasets/{datasetRid}/readTable |
**Datasets** | File | [**delete**](docs/v1/Datasets/File.md#delete) | **DELETE** /v1/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**get**](docs/v1/Datasets/File.md#get) | **GET** /v1/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**list**](docs/v1/Datasets/File.md#list) | **GET** /v1/datasets/{datasetRid}/files |
**Datasets** | File | [**page**](docs/v1/Datasets/File.md#page) | **GET** /v1/datasets/{datasetRid}/files |
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
**Ontologies** | ActionType | [**page**](docs/v1/Ontologies/ActionType.md#page) | **GET** /v1/ontologies/{ontologyRid}/actionTypes |
**Ontologies** | ObjectType | [**get**](docs/v1/Ontologies/ObjectType.md#get) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType} |
**Ontologies** | ObjectType | [**get_outgoing_link_type**](docs/v1/Ontologies/ObjectType.md#get_outgoing_link_type) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
**Ontologies** | ObjectType | [**list**](docs/v1/Ontologies/ObjectType.md#list) | **GET** /v1/ontologies/{ontologyRid}/objectTypes |
**Ontologies** | ObjectType | [**list_outgoing_link_types**](docs/v1/Ontologies/ObjectType.md#list_outgoing_link_types) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | ObjectType | [**page**](docs/v1/Ontologies/ObjectType.md#page) | **GET** /v1/ontologies/{ontologyRid}/objectTypes |
**Ontologies** | ObjectType | [**page_outgoing_link_types**](docs/v1/Ontologies/ObjectType.md#page_outgoing_link_types) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | Ontology | [**get**](docs/v1/Ontologies/Ontology.md#get) | **GET** /v1/ontologies/{ontologyRid} |
**Ontologies** | Ontology | [**list**](docs/v1/Ontologies/Ontology.md#list) | **GET** /v1/ontologies |
**Ontologies** | OntologyObject | [**aggregate**](docs/v1/Ontologies/OntologyObject.md#aggregate) | **POST** /v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate |
**Ontologies** | OntologyObject | [**get**](docs/v1/Ontologies/OntologyObject.md#get) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey} |
**Ontologies** | OntologyObject | [**get_linked_object**](docs/v1/Ontologies/OntologyObject.md#get_linked_object) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey} |
**Ontologies** | OntologyObject | [**list**](docs/v1/Ontologies/OntologyObject.md#list) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType} |
**Ontologies** | OntologyObject | [**list_linked_objects**](docs/v1/Ontologies/OntologyObject.md#list_linked_objects) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType} |
**Ontologies** | OntologyObject | [**page**](docs/v1/Ontologies/OntologyObject.md#page) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType} |
**Ontologies** | OntologyObject | [**page_linked_objects**](docs/v1/Ontologies/OntologyObject.md#page_linked_objects) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType} |
**Ontologies** | OntologyObject | [**search**](docs/v1/Ontologies/OntologyObject.md#search) | **POST** /v1/ontologies/{ontologyRid}/objects/{objectType}/search |
**Ontologies** | Query | [**execute**](docs/v1/Ontologies/Query.md#execute) | **POST** /v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute |
**Ontologies** | QueryType | [**get**](docs/v1/Ontologies/QueryType.md#get) | **GET** /v1/ontologies/{ontologyRid}/queryTypes/{queryApiName} |
**Ontologies** | QueryType | [**list**](docs/v1/Ontologies/QueryType.md#list) | **GET** /v1/ontologies/{ontologyRid}/queryTypes |
**Ontologies** | QueryType | [**page**](docs/v1/Ontologies/QueryType.md#page) | **GET** /v1/ontologies/{ontologyRid}/queryTypes |


<a id="models-link"></a>
<a id="models-v2-link"></a>
## Documentation for V2 models

Namespace | Name | Import |
--------- | ---- | ------ |
**Admin** | [AttributeName](docs/v2/Admin/models/AttributeName.md) | `from foundry.v2.admin.models import AttributeName` |
**Admin** | [AttributeValue](docs/v2/Admin/models/AttributeValue.md) | `from foundry.v2.admin.models import AttributeValue` |
**Admin** | [AttributeValues](docs/v2/Admin/models/AttributeValues.md) | `from foundry.v2.admin.models import AttributeValues` |
**Admin** | [Enrollment](docs/v2/Admin/models/Enrollment.md) | `from foundry.v2.admin.models import Enrollment` |
**Admin** | [EnrollmentDict](docs/v2/Admin/models/EnrollmentDict.md) | `from foundry.v2.admin.models import EnrollmentDict` |
**Admin** | [EnrollmentName](docs/v2/Admin/models/EnrollmentName.md) | `from foundry.v2.admin.models import EnrollmentName` |
**Admin** | [GetGroupsBatchRequestElement](docs/v2/Admin/models/GetGroupsBatchRequestElement.md) | `from foundry.v2.admin.models import GetGroupsBatchRequestElement` |
**Admin** | [GetGroupsBatchRequestElementDict](docs/v2/Admin/models/GetGroupsBatchRequestElementDict.md) | `from foundry.v2.admin.models import GetGroupsBatchRequestElementDict` |
**Admin** | [GetGroupsBatchResponse](docs/v2/Admin/models/GetGroupsBatchResponse.md) | `from foundry.v2.admin.models import GetGroupsBatchResponse` |
**Admin** | [GetGroupsBatchResponseDict](docs/v2/Admin/models/GetGroupsBatchResponseDict.md) | `from foundry.v2.admin.models import GetGroupsBatchResponseDict` |
**Admin** | [GetMarkingsBatchRequestElement](docs/v2/Admin/models/GetMarkingsBatchRequestElement.md) | `from foundry.v2.admin.models import GetMarkingsBatchRequestElement` |
**Admin** | [GetMarkingsBatchRequestElementDict](docs/v2/Admin/models/GetMarkingsBatchRequestElementDict.md) | `from foundry.v2.admin.models import GetMarkingsBatchRequestElementDict` |
**Admin** | [GetMarkingsBatchResponse](docs/v2/Admin/models/GetMarkingsBatchResponse.md) | `from foundry.v2.admin.models import GetMarkingsBatchResponse` |
**Admin** | [GetMarkingsBatchResponseDict](docs/v2/Admin/models/GetMarkingsBatchResponseDict.md) | `from foundry.v2.admin.models import GetMarkingsBatchResponseDict` |
**Admin** | [GetUserMarkingsResponse](docs/v2/Admin/models/GetUserMarkingsResponse.md) | `from foundry.v2.admin.models import GetUserMarkingsResponse` |
**Admin** | [GetUserMarkingsResponseDict](docs/v2/Admin/models/GetUserMarkingsResponseDict.md) | `from foundry.v2.admin.models import GetUserMarkingsResponseDict` |
**Admin** | [GetUsersBatchRequestElement](docs/v2/Admin/models/GetUsersBatchRequestElement.md) | `from foundry.v2.admin.models import GetUsersBatchRequestElement` |
**Admin** | [GetUsersBatchRequestElementDict](docs/v2/Admin/models/GetUsersBatchRequestElementDict.md) | `from foundry.v2.admin.models import GetUsersBatchRequestElementDict` |
**Admin** | [GetUsersBatchResponse](docs/v2/Admin/models/GetUsersBatchResponse.md) | `from foundry.v2.admin.models import GetUsersBatchResponse` |
**Admin** | [GetUsersBatchResponseDict](docs/v2/Admin/models/GetUsersBatchResponseDict.md) | `from foundry.v2.admin.models import GetUsersBatchResponseDict` |
**Admin** | [Group](docs/v2/Admin/models/Group.md) | `from foundry.v2.admin.models import Group` |
**Admin** | [GroupDict](docs/v2/Admin/models/GroupDict.md) | `from foundry.v2.admin.models import GroupDict` |
**Admin** | [GroupMember](docs/v2/Admin/models/GroupMember.md) | `from foundry.v2.admin.models import GroupMember` |
**Admin** | [GroupMemberDict](docs/v2/Admin/models/GroupMemberDict.md) | `from foundry.v2.admin.models import GroupMemberDict` |
**Admin** | [GroupMembership](docs/v2/Admin/models/GroupMembership.md) | `from foundry.v2.admin.models import GroupMembership` |
**Admin** | [GroupMembershipDict](docs/v2/Admin/models/GroupMembershipDict.md) | `from foundry.v2.admin.models import GroupMembershipDict` |
**Admin** | [GroupMembershipExpiration](docs/v2/Admin/models/GroupMembershipExpiration.md) | `from foundry.v2.admin.models import GroupMembershipExpiration` |
**Admin** | [GroupName](docs/v2/Admin/models/GroupName.md) | `from foundry.v2.admin.models import GroupName` |
**Admin** | [GroupProviderInfo](docs/v2/Admin/models/GroupProviderInfo.md) | `from foundry.v2.admin.models import GroupProviderInfo` |
**Admin** | [GroupProviderInfoDict](docs/v2/Admin/models/GroupProviderInfoDict.md) | `from foundry.v2.admin.models import GroupProviderInfoDict` |
**Admin** | [GroupSearchFilter](docs/v2/Admin/models/GroupSearchFilter.md) | `from foundry.v2.admin.models import GroupSearchFilter` |
**Admin** | [GroupSearchFilterDict](docs/v2/Admin/models/GroupSearchFilterDict.md) | `from foundry.v2.admin.models import GroupSearchFilterDict` |
**Admin** | [Host](docs/v2/Admin/models/Host.md) | `from foundry.v2.admin.models import Host` |
**Admin** | [HostDict](docs/v2/Admin/models/HostDict.md) | `from foundry.v2.admin.models import HostDict` |
**Admin** | [HostName](docs/v2/Admin/models/HostName.md) | `from foundry.v2.admin.models import HostName` |
**Admin** | [ListGroupMembershipsResponse](docs/v2/Admin/models/ListGroupMembershipsResponse.md) | `from foundry.v2.admin.models import ListGroupMembershipsResponse` |
**Admin** | [ListGroupMembershipsResponseDict](docs/v2/Admin/models/ListGroupMembershipsResponseDict.md) | `from foundry.v2.admin.models import ListGroupMembershipsResponseDict` |
**Admin** | [ListGroupMembersResponse](docs/v2/Admin/models/ListGroupMembersResponse.md) | `from foundry.v2.admin.models import ListGroupMembersResponse` |
**Admin** | [ListGroupMembersResponseDict](docs/v2/Admin/models/ListGroupMembersResponseDict.md) | `from foundry.v2.admin.models import ListGroupMembersResponseDict` |
**Admin** | [ListGroupsResponse](docs/v2/Admin/models/ListGroupsResponse.md) | `from foundry.v2.admin.models import ListGroupsResponse` |
**Admin** | [ListGroupsResponseDict](docs/v2/Admin/models/ListGroupsResponseDict.md) | `from foundry.v2.admin.models import ListGroupsResponseDict` |
**Admin** | [ListHostsResponse](docs/v2/Admin/models/ListHostsResponse.md) | `from foundry.v2.admin.models import ListHostsResponse` |
**Admin** | [ListHostsResponseDict](docs/v2/Admin/models/ListHostsResponseDict.md) | `from foundry.v2.admin.models import ListHostsResponseDict` |
**Admin** | [ListMarkingCategoriesResponse](docs/v2/Admin/models/ListMarkingCategoriesResponse.md) | `from foundry.v2.admin.models import ListMarkingCategoriesResponse` |
**Admin** | [ListMarkingCategoriesResponseDict](docs/v2/Admin/models/ListMarkingCategoriesResponseDict.md) | `from foundry.v2.admin.models import ListMarkingCategoriesResponseDict` |
**Admin** | [ListMarkingMembersResponse](docs/v2/Admin/models/ListMarkingMembersResponse.md) | `from foundry.v2.admin.models import ListMarkingMembersResponse` |
**Admin** | [ListMarkingMembersResponseDict](docs/v2/Admin/models/ListMarkingMembersResponseDict.md) | `from foundry.v2.admin.models import ListMarkingMembersResponseDict` |
**Admin** | [ListMarkingRoleAssignmentsResponse](docs/v2/Admin/models/ListMarkingRoleAssignmentsResponse.md) | `from foundry.v2.admin.models import ListMarkingRoleAssignmentsResponse` |
**Admin** | [ListMarkingRoleAssignmentsResponseDict](docs/v2/Admin/models/ListMarkingRoleAssignmentsResponseDict.md) | `from foundry.v2.admin.models import ListMarkingRoleAssignmentsResponseDict` |
**Admin** | [ListMarkingsResponse](docs/v2/Admin/models/ListMarkingsResponse.md) | `from foundry.v2.admin.models import ListMarkingsResponse` |
**Admin** | [ListMarkingsResponseDict](docs/v2/Admin/models/ListMarkingsResponseDict.md) | `from foundry.v2.admin.models import ListMarkingsResponseDict` |
**Admin** | [ListUsersResponse](docs/v2/Admin/models/ListUsersResponse.md) | `from foundry.v2.admin.models import ListUsersResponse` |
**Admin** | [ListUsersResponseDict](docs/v2/Admin/models/ListUsersResponseDict.md) | `from foundry.v2.admin.models import ListUsersResponseDict` |
**Admin** | [Marking](docs/v2/Admin/models/Marking.md) | `from foundry.v2.admin.models import Marking` |
**Admin** | [MarkingCategory](docs/v2/Admin/models/MarkingCategory.md) | `from foundry.v2.admin.models import MarkingCategory` |
**Admin** | [MarkingCategoryDict](docs/v2/Admin/models/MarkingCategoryDict.md) | `from foundry.v2.admin.models import MarkingCategoryDict` |
**Admin** | [MarkingCategoryId](docs/v2/Admin/models/MarkingCategoryId.md) | `from foundry.v2.admin.models import MarkingCategoryId` |
**Admin** | [MarkingCategoryName](docs/v2/Admin/models/MarkingCategoryName.md) | `from foundry.v2.admin.models import MarkingCategoryName` |
**Admin** | [MarkingCategoryType](docs/v2/Admin/models/MarkingCategoryType.md) | `from foundry.v2.admin.models import MarkingCategoryType` |
**Admin** | [MarkingDict](docs/v2/Admin/models/MarkingDict.md) | `from foundry.v2.admin.models import MarkingDict` |
**Admin** | [MarkingMember](docs/v2/Admin/models/MarkingMember.md) | `from foundry.v2.admin.models import MarkingMember` |
**Admin** | [MarkingMemberDict](docs/v2/Admin/models/MarkingMemberDict.md) | `from foundry.v2.admin.models import MarkingMemberDict` |
**Admin** | [MarkingName](docs/v2/Admin/models/MarkingName.md) | `from foundry.v2.admin.models import MarkingName` |
**Admin** | [MarkingRole](docs/v2/Admin/models/MarkingRole.md) | `from foundry.v2.admin.models import MarkingRole` |
**Admin** | [MarkingRoleAssignment](docs/v2/Admin/models/MarkingRoleAssignment.md) | `from foundry.v2.admin.models import MarkingRoleAssignment` |
**Admin** | [MarkingRoleAssignmentDict](docs/v2/Admin/models/MarkingRoleAssignmentDict.md) | `from foundry.v2.admin.models import MarkingRoleAssignmentDict` |
**Admin** | [MarkingRoleUpdate](docs/v2/Admin/models/MarkingRoleUpdate.md) | `from foundry.v2.admin.models import MarkingRoleUpdate` |
**Admin** | [MarkingRoleUpdateDict](docs/v2/Admin/models/MarkingRoleUpdateDict.md) | `from foundry.v2.admin.models import MarkingRoleUpdateDict` |
**Admin** | [MarkingType](docs/v2/Admin/models/MarkingType.md) | `from foundry.v2.admin.models import MarkingType` |
**Admin** | [Organization](docs/v2/Admin/models/Organization.md) | `from foundry.v2.admin.models import Organization` |
**Admin** | [OrganizationDict](docs/v2/Admin/models/OrganizationDict.md) | `from foundry.v2.admin.models import OrganizationDict` |
**Admin** | [OrganizationName](docs/v2/Admin/models/OrganizationName.md) | `from foundry.v2.admin.models import OrganizationName` |
**Admin** | [PrincipalFilterType](docs/v2/Admin/models/PrincipalFilterType.md) | `from foundry.v2.admin.models import PrincipalFilterType` |
**Admin** | [ProviderId](docs/v2/Admin/models/ProviderId.md) | `from foundry.v2.admin.models import ProviderId` |
**Admin** | [SearchGroupsResponse](docs/v2/Admin/models/SearchGroupsResponse.md) | `from foundry.v2.admin.models import SearchGroupsResponse` |
**Admin** | [SearchGroupsResponseDict](docs/v2/Admin/models/SearchGroupsResponseDict.md) | `from foundry.v2.admin.models import SearchGroupsResponseDict` |
**Admin** | [SearchUsersResponse](docs/v2/Admin/models/SearchUsersResponse.md) | `from foundry.v2.admin.models import SearchUsersResponse` |
**Admin** | [SearchUsersResponseDict](docs/v2/Admin/models/SearchUsersResponseDict.md) | `from foundry.v2.admin.models import SearchUsersResponseDict` |
**Admin** | [User](docs/v2/Admin/models/User.md) | `from foundry.v2.admin.models import User` |
**Admin** | [UserDict](docs/v2/Admin/models/UserDict.md) | `from foundry.v2.admin.models import UserDict` |
**Admin** | [UserProviderInfo](docs/v2/Admin/models/UserProviderInfo.md) | `from foundry.v2.admin.models import UserProviderInfo` |
**Admin** | [UserProviderInfoDict](docs/v2/Admin/models/UserProviderInfoDict.md) | `from foundry.v2.admin.models import UserProviderInfoDict` |
**Admin** | [UserSearchFilter](docs/v2/Admin/models/UserSearchFilter.md) | `from foundry.v2.admin.models import UserSearchFilter` |
**Admin** | [UserSearchFilterDict](docs/v2/Admin/models/UserSearchFilterDict.md) | `from foundry.v2.admin.models import UserSearchFilterDict` |
**Admin** | [UserUsername](docs/v2/Admin/models/UserUsername.md) | `from foundry.v2.admin.models import UserUsername` |
**AipAgents** | [Agent](docs/v2/AipAgents/models/Agent.md) | `from foundry.v2.aip_agents.models import Agent` |
**AipAgents** | [AgentDict](docs/v2/AipAgents/models/AgentDict.md) | `from foundry.v2.aip_agents.models import AgentDict` |
**AipAgents** | [AgentMarkdownResponse](docs/v2/AipAgents/models/AgentMarkdownResponse.md) | `from foundry.v2.aip_agents.models import AgentMarkdownResponse` |
**AipAgents** | [AgentMetadata](docs/v2/AipAgents/models/AgentMetadata.md) | `from foundry.v2.aip_agents.models import AgentMetadata` |
**AipAgents** | [AgentMetadataDict](docs/v2/AipAgents/models/AgentMetadataDict.md) | `from foundry.v2.aip_agents.models import AgentMetadataDict` |
**AipAgents** | [AgentRid](docs/v2/AipAgents/models/AgentRid.md) | `from foundry.v2.aip_agents.models import AgentRid` |
**AipAgents** | [AgentSessionRagContextResponse](docs/v2/AipAgents/models/AgentSessionRagContextResponse.md) | `from foundry.v2.aip_agents.models import AgentSessionRagContextResponse` |
**AipAgents** | [AgentSessionRagContextResponseDict](docs/v2/AipAgents/models/AgentSessionRagContextResponseDict.md) | `from foundry.v2.aip_agents.models import AgentSessionRagContextResponseDict` |
**AipAgents** | [AgentsSessionsPage](docs/v2/AipAgents/models/AgentsSessionsPage.md) | `from foundry.v2.aip_agents.models import AgentsSessionsPage` |
**AipAgents** | [AgentsSessionsPageDict](docs/v2/AipAgents/models/AgentsSessionsPageDict.md) | `from foundry.v2.aip_agents.models import AgentsSessionsPageDict` |
**AipAgents** | [AgentVersion](docs/v2/AipAgents/models/AgentVersion.md) | `from foundry.v2.aip_agents.models import AgentVersion` |
**AipAgents** | [AgentVersionDetails](docs/v2/AipAgents/models/AgentVersionDetails.md) | `from foundry.v2.aip_agents.models import AgentVersionDetails` |
**AipAgents** | [AgentVersionDetailsDict](docs/v2/AipAgents/models/AgentVersionDetailsDict.md) | `from foundry.v2.aip_agents.models import AgentVersionDetailsDict` |
**AipAgents** | [AgentVersionDict](docs/v2/AipAgents/models/AgentVersionDict.md) | `from foundry.v2.aip_agents.models import AgentVersionDict` |
**AipAgents** | [AgentVersionString](docs/v2/AipAgents/models/AgentVersionString.md) | `from foundry.v2.aip_agents.models import AgentVersionString` |
**AipAgents** | [CancelSessionResponse](docs/v2/AipAgents/models/CancelSessionResponse.md) | `from foundry.v2.aip_agents.models import CancelSessionResponse` |
**AipAgents** | [CancelSessionResponseDict](docs/v2/AipAgents/models/CancelSessionResponseDict.md) | `from foundry.v2.aip_agents.models import CancelSessionResponseDict` |
**AipAgents** | [Content](docs/v2/AipAgents/models/Content.md) | `from foundry.v2.aip_agents.models import Content` |
**AipAgents** | [ContentDict](docs/v2/AipAgents/models/ContentDict.md) | `from foundry.v2.aip_agents.models import ContentDict` |
**AipAgents** | [FunctionRetrievedContext](docs/v2/AipAgents/models/FunctionRetrievedContext.md) | `from foundry.v2.aip_agents.models import FunctionRetrievedContext` |
**AipAgents** | [FunctionRetrievedContextDict](docs/v2/AipAgents/models/FunctionRetrievedContextDict.md) | `from foundry.v2.aip_agents.models import FunctionRetrievedContextDict` |
**AipAgents** | [InputContext](docs/v2/AipAgents/models/InputContext.md) | `from foundry.v2.aip_agents.models import InputContext` |
**AipAgents** | [InputContextDict](docs/v2/AipAgents/models/InputContextDict.md) | `from foundry.v2.aip_agents.models import InputContextDict` |
**AipAgents** | [ListAgentVersionsResponse](docs/v2/AipAgents/models/ListAgentVersionsResponse.md) | `from foundry.v2.aip_agents.models import ListAgentVersionsResponse` |
**AipAgents** | [ListAgentVersionsResponseDict](docs/v2/AipAgents/models/ListAgentVersionsResponseDict.md) | `from foundry.v2.aip_agents.models import ListAgentVersionsResponseDict` |
**AipAgents** | [ListSessionsResponse](docs/v2/AipAgents/models/ListSessionsResponse.md) | `from foundry.v2.aip_agents.models import ListSessionsResponse` |
**AipAgents** | [ListSessionsResponseDict](docs/v2/AipAgents/models/ListSessionsResponseDict.md) | `from foundry.v2.aip_agents.models import ListSessionsResponseDict` |
**AipAgents** | [MessageId](docs/v2/AipAgents/models/MessageId.md) | `from foundry.v2.aip_agents.models import MessageId` |
**AipAgents** | [ObjectContext](docs/v2/AipAgents/models/ObjectContext.md) | `from foundry.v2.aip_agents.models import ObjectContext` |
**AipAgents** | [ObjectContextDict](docs/v2/AipAgents/models/ObjectContextDict.md) | `from foundry.v2.aip_agents.models import ObjectContextDict` |
**AipAgents** | [ObjectSetParameter](docs/v2/AipAgents/models/ObjectSetParameter.md) | `from foundry.v2.aip_agents.models import ObjectSetParameter` |
**AipAgents** | [ObjectSetParameterDict](docs/v2/AipAgents/models/ObjectSetParameterDict.md) | `from foundry.v2.aip_agents.models import ObjectSetParameterDict` |
**AipAgents** | [ObjectSetParameterValue](docs/v2/AipAgents/models/ObjectSetParameterValue.md) | `from foundry.v2.aip_agents.models import ObjectSetParameterValue` |
**AipAgents** | [ObjectSetParameterValueDict](docs/v2/AipAgents/models/ObjectSetParameterValueDict.md) | `from foundry.v2.aip_agents.models import ObjectSetParameterValueDict` |
**AipAgents** | [ObjectSetParameterValueUpdate](docs/v2/AipAgents/models/ObjectSetParameterValueUpdate.md) | `from foundry.v2.aip_agents.models import ObjectSetParameterValueUpdate` |
**AipAgents** | [ObjectSetParameterValueUpdateDict](docs/v2/AipAgents/models/ObjectSetParameterValueUpdateDict.md) | `from foundry.v2.aip_agents.models import ObjectSetParameterValueUpdateDict` |
**AipAgents** | [Parameter](docs/v2/AipAgents/models/Parameter.md) | `from foundry.v2.aip_agents.models import Parameter` |
**AipAgents** | [ParameterAccessMode](docs/v2/AipAgents/models/ParameterAccessMode.md) | `from foundry.v2.aip_agents.models import ParameterAccessMode` |
**AipAgents** | [ParameterDict](docs/v2/AipAgents/models/ParameterDict.md) | `from foundry.v2.aip_agents.models import ParameterDict` |
**AipAgents** | [ParameterId](docs/v2/AipAgents/models/ParameterId.md) | `from foundry.v2.aip_agents.models import ParameterId` |
**AipAgents** | [ParameterType](docs/v2/AipAgents/models/ParameterType.md) | `from foundry.v2.aip_agents.models import ParameterType` |
**AipAgents** | [ParameterTypeDict](docs/v2/AipAgents/models/ParameterTypeDict.md) | `from foundry.v2.aip_agents.models import ParameterTypeDict` |
**AipAgents** | [ParameterValue](docs/v2/AipAgents/models/ParameterValue.md) | `from foundry.v2.aip_agents.models import ParameterValue` |
**AipAgents** | [ParameterValueDict](docs/v2/AipAgents/models/ParameterValueDict.md) | `from foundry.v2.aip_agents.models import ParameterValueDict` |
**AipAgents** | [ParameterValueUpdate](docs/v2/AipAgents/models/ParameterValueUpdate.md) | `from foundry.v2.aip_agents.models import ParameterValueUpdate` |
**AipAgents** | [ParameterValueUpdateDict](docs/v2/AipAgents/models/ParameterValueUpdateDict.md) | `from foundry.v2.aip_agents.models import ParameterValueUpdateDict` |
**AipAgents** | [Session](docs/v2/AipAgents/models/Session.md) | `from foundry.v2.aip_agents.models import Session` |
**AipAgents** | [SessionDict](docs/v2/AipAgents/models/SessionDict.md) | `from foundry.v2.aip_agents.models import SessionDict` |
**AipAgents** | [SessionExchange](docs/v2/AipAgents/models/SessionExchange.md) | `from foundry.v2.aip_agents.models import SessionExchange` |
**AipAgents** | [SessionExchangeContexts](docs/v2/AipAgents/models/SessionExchangeContexts.md) | `from foundry.v2.aip_agents.models import SessionExchangeContexts` |
**AipAgents** | [SessionExchangeContextsDict](docs/v2/AipAgents/models/SessionExchangeContextsDict.md) | `from foundry.v2.aip_agents.models import SessionExchangeContextsDict` |
**AipAgents** | [SessionExchangeDict](docs/v2/AipAgents/models/SessionExchangeDict.md) | `from foundry.v2.aip_agents.models import SessionExchangeDict` |
**AipAgents** | [SessionExchangeResult](docs/v2/AipAgents/models/SessionExchangeResult.md) | `from foundry.v2.aip_agents.models import SessionExchangeResult` |
**AipAgents** | [SessionExchangeResultDict](docs/v2/AipAgents/models/SessionExchangeResultDict.md) | `from foundry.v2.aip_agents.models import SessionExchangeResultDict` |
**AipAgents** | [SessionMetadata](docs/v2/AipAgents/models/SessionMetadata.md) | `from foundry.v2.aip_agents.models import SessionMetadata` |
**AipAgents** | [SessionMetadataDict](docs/v2/AipAgents/models/SessionMetadataDict.md) | `from foundry.v2.aip_agents.models import SessionMetadataDict` |
**AipAgents** | [SessionRid](docs/v2/AipAgents/models/SessionRid.md) | `from foundry.v2.aip_agents.models import SessionRid` |
**AipAgents** | [StringParameter](docs/v2/AipAgents/models/StringParameter.md) | `from foundry.v2.aip_agents.models import StringParameter` |
**AipAgents** | [StringParameterDict](docs/v2/AipAgents/models/StringParameterDict.md) | `from foundry.v2.aip_agents.models import StringParameterDict` |
**AipAgents** | [StringParameterValue](docs/v2/AipAgents/models/StringParameterValue.md) | `from foundry.v2.aip_agents.models import StringParameterValue` |
**AipAgents** | [StringParameterValueDict](docs/v2/AipAgents/models/StringParameterValueDict.md) | `from foundry.v2.aip_agents.models import StringParameterValueDict` |
**AipAgents** | [UserTextInput](docs/v2/AipAgents/models/UserTextInput.md) | `from foundry.v2.aip_agents.models import UserTextInput` |
**AipAgents** | [UserTextInputDict](docs/v2/AipAgents/models/UserTextInputDict.md) | `from foundry.v2.aip_agents.models import UserTextInputDict` |
**Connectivity** | [AgentProxyRuntime](docs/v2/Connectivity/models/AgentProxyRuntime.md) | `from foundry.v2.connectivity.models import AgentProxyRuntime` |
**Connectivity** | [AgentProxyRuntimeDict](docs/v2/Connectivity/models/AgentProxyRuntimeDict.md) | `from foundry.v2.connectivity.models import AgentProxyRuntimeDict` |
**Connectivity** | [AgentRid](docs/v2/Connectivity/models/AgentRid.md) | `from foundry.v2.connectivity.models import AgentRid` |
**Connectivity** | [AgentWorkerRuntime](docs/v2/Connectivity/models/AgentWorkerRuntime.md) | `from foundry.v2.connectivity.models import AgentWorkerRuntime` |
**Connectivity** | [AgentWorkerRuntimeDict](docs/v2/Connectivity/models/AgentWorkerRuntimeDict.md) | `from foundry.v2.connectivity.models import AgentWorkerRuntimeDict` |
**Connectivity** | [AsPlaintextValue](docs/v2/Connectivity/models/AsPlaintextValue.md) | `from foundry.v2.connectivity.models import AsPlaintextValue` |
**Connectivity** | [AsPlaintextValueDict](docs/v2/Connectivity/models/AsPlaintextValueDict.md) | `from foundry.v2.connectivity.models import AsPlaintextValueDict` |
**Connectivity** | [AsSecretName](docs/v2/Connectivity/models/AsSecretName.md) | `from foundry.v2.connectivity.models import AsSecretName` |
**Connectivity** | [AsSecretNameDict](docs/v2/Connectivity/models/AsSecretNameDict.md) | `from foundry.v2.connectivity.models import AsSecretNameDict` |
**Connectivity** | [AwsAccessKey](docs/v2/Connectivity/models/AwsAccessKey.md) | `from foundry.v2.connectivity.models import AwsAccessKey` |
**Connectivity** | [AwsAccessKeyDict](docs/v2/Connectivity/models/AwsAccessKeyDict.md) | `from foundry.v2.connectivity.models import AwsAccessKeyDict` |
**Connectivity** | [BasicCredentials](docs/v2/Connectivity/models/BasicCredentials.md) | `from foundry.v2.connectivity.models import BasicCredentials` |
**Connectivity** | [BasicCredentialsDict](docs/v2/Connectivity/models/BasicCredentialsDict.md) | `from foundry.v2.connectivity.models import BasicCredentialsDict` |
**Connectivity** | [CloudIdentity](docs/v2/Connectivity/models/CloudIdentity.md) | `from foundry.v2.connectivity.models import CloudIdentity` |
**Connectivity** | [CloudIdentityDict](docs/v2/Connectivity/models/CloudIdentityDict.md) | `from foundry.v2.connectivity.models import CloudIdentityDict` |
**Connectivity** | [CloudIdentityRid](docs/v2/Connectivity/models/CloudIdentityRid.md) | `from foundry.v2.connectivity.models import CloudIdentityRid` |
**Connectivity** | [Connection](docs/v2/Connectivity/models/Connection.md) | `from foundry.v2.connectivity.models import Connection` |
**Connectivity** | [ConnectionConfiguration](docs/v2/Connectivity/models/ConnectionConfiguration.md) | `from foundry.v2.connectivity.models import ConnectionConfiguration` |
**Connectivity** | [ConnectionConfigurationDict](docs/v2/Connectivity/models/ConnectionConfigurationDict.md) | `from foundry.v2.connectivity.models import ConnectionConfigurationDict` |
**Connectivity** | [ConnectionDict](docs/v2/Connectivity/models/ConnectionDict.md) | `from foundry.v2.connectivity.models import ConnectionDict` |
**Connectivity** | [ConnectionDisplayName](docs/v2/Connectivity/models/ConnectionDisplayName.md) | `from foundry.v2.connectivity.models import ConnectionDisplayName` |
**Connectivity** | [ConnectionRid](docs/v2/Connectivity/models/ConnectionRid.md) | `from foundry.v2.connectivity.models import ConnectionRid` |
**Connectivity** | [CreateConnectionRequestAgentProxyRuntime](docs/v2/Connectivity/models/CreateConnectionRequestAgentProxyRuntime.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestAgentProxyRuntime` |
**Connectivity** | [CreateConnectionRequestAgentProxyRuntimeDict](docs/v2/Connectivity/models/CreateConnectionRequestAgentProxyRuntimeDict.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestAgentProxyRuntimeDict` |
**Connectivity** | [CreateConnectionRequestAgentWorkerRuntime](docs/v2/Connectivity/models/CreateConnectionRequestAgentWorkerRuntime.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestAgentWorkerRuntime` |
**Connectivity** | [CreateConnectionRequestAgentWorkerRuntimeDict](docs/v2/Connectivity/models/CreateConnectionRequestAgentWorkerRuntimeDict.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestAgentWorkerRuntimeDict` |
**Connectivity** | [CreateConnectionRequestConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestConnectionConfiguration.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestConnectionConfigurationDict](docs/v2/Connectivity/models/CreateConnectionRequestConnectionConfigurationDict.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestConnectionConfigurationDict` |
**Connectivity** | [CreateConnectionRequestDirectConnectionRuntime](docs/v2/Connectivity/models/CreateConnectionRequestDirectConnectionRuntime.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestDirectConnectionRuntime` |
**Connectivity** | [CreateConnectionRequestDirectConnectionRuntimeDict](docs/v2/Connectivity/models/CreateConnectionRequestDirectConnectionRuntimeDict.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestDirectConnectionRuntimeDict` |
**Connectivity** | [CreateConnectionRequestRuntimePlatform](docs/v2/Connectivity/models/CreateConnectionRequestRuntimePlatform.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestRuntimePlatform` |
**Connectivity** | [CreateConnectionRequestRuntimePlatformDict](docs/v2/Connectivity/models/CreateConnectionRequestRuntimePlatformDict.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestRuntimePlatformDict` |
**Connectivity** | [CreateConnectionRequestS3ConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestS3ConnectionConfiguration.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestS3ConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestS3ConnectionConfigurationDict](docs/v2/Connectivity/models/CreateConnectionRequestS3ConnectionConfigurationDict.md) | `from foundry.v2.connectivity.models import CreateConnectionRequestS3ConnectionConfigurationDict` |
**Connectivity** | [CreateTableImportRequestJdbcImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestJdbcImportConfig.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestJdbcImportConfig` |
**Connectivity** | [CreateTableImportRequestJdbcImportConfigDict](docs/v2/Connectivity/models/CreateTableImportRequestJdbcImportConfigDict.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestJdbcImportConfigDict` |
**Connectivity** | [CreateTableImportRequestMicrosoftAccessImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestMicrosoftAccessImportConfig.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestMicrosoftAccessImportConfig` |
**Connectivity** | [CreateTableImportRequestMicrosoftAccessImportConfigDict](docs/v2/Connectivity/models/CreateTableImportRequestMicrosoftAccessImportConfigDict.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestMicrosoftAccessImportConfigDict` |
**Connectivity** | [CreateTableImportRequestMicrosoftSqlServerImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestMicrosoftSqlServerImportConfig.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestMicrosoftSqlServerImportConfig` |
**Connectivity** | [CreateTableImportRequestMicrosoftSqlServerImportConfigDict](docs/v2/Connectivity/models/CreateTableImportRequestMicrosoftSqlServerImportConfigDict.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestMicrosoftSqlServerImportConfigDict` |
**Connectivity** | [CreateTableImportRequestOracleImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestOracleImportConfig.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestOracleImportConfig` |
**Connectivity** | [CreateTableImportRequestOracleImportConfigDict](docs/v2/Connectivity/models/CreateTableImportRequestOracleImportConfigDict.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestOracleImportConfigDict` |
**Connectivity** | [CreateTableImportRequestPostgreSqlImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestPostgreSqlImportConfig.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestPostgreSqlImportConfig` |
**Connectivity** | [CreateTableImportRequestPostgreSqlImportConfigDict](docs/v2/Connectivity/models/CreateTableImportRequestPostgreSqlImportConfigDict.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestPostgreSqlImportConfigDict` |
**Connectivity** | [CreateTableImportRequestTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestTableImportConfig.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestTableImportConfig` |
**Connectivity** | [CreateTableImportRequestTableImportConfigDict](docs/v2/Connectivity/models/CreateTableImportRequestTableImportConfigDict.md) | `from foundry.v2.connectivity.models import CreateTableImportRequestTableImportConfigDict` |
**Connectivity** | [DirectConnectionRuntime](docs/v2/Connectivity/models/DirectConnectionRuntime.md) | `from foundry.v2.connectivity.models import DirectConnectionRuntime` |
**Connectivity** | [DirectConnectionRuntimeDict](docs/v2/Connectivity/models/DirectConnectionRuntimeDict.md) | `from foundry.v2.connectivity.models import DirectConnectionRuntimeDict` |
**Connectivity** | [EncryptedProperty](docs/v2/Connectivity/models/EncryptedProperty.md) | `from foundry.v2.connectivity.models import EncryptedProperty` |
**Connectivity** | [EncryptedPropertyDict](docs/v2/Connectivity/models/EncryptedPropertyDict.md) | `from foundry.v2.connectivity.models import EncryptedPropertyDict` |
**Connectivity** | [FileAnyPathMatchesFilter](docs/v2/Connectivity/models/FileAnyPathMatchesFilter.md) | `from foundry.v2.connectivity.models import FileAnyPathMatchesFilter` |
**Connectivity** | [FileAnyPathMatchesFilterDict](docs/v2/Connectivity/models/FileAnyPathMatchesFilterDict.md) | `from foundry.v2.connectivity.models import FileAnyPathMatchesFilterDict` |
**Connectivity** | [FileAtLeastCountFilter](docs/v2/Connectivity/models/FileAtLeastCountFilter.md) | `from foundry.v2.connectivity.models import FileAtLeastCountFilter` |
**Connectivity** | [FileAtLeastCountFilterDict](docs/v2/Connectivity/models/FileAtLeastCountFilterDict.md) | `from foundry.v2.connectivity.models import FileAtLeastCountFilterDict` |
**Connectivity** | [FileChangedSinceLastUploadFilter](docs/v2/Connectivity/models/FileChangedSinceLastUploadFilter.md) | `from foundry.v2.connectivity.models import FileChangedSinceLastUploadFilter` |
**Connectivity** | [FileChangedSinceLastUploadFilterDict](docs/v2/Connectivity/models/FileChangedSinceLastUploadFilterDict.md) | `from foundry.v2.connectivity.models import FileChangedSinceLastUploadFilterDict` |
**Connectivity** | [FileImport](docs/v2/Connectivity/models/FileImport.md) | `from foundry.v2.connectivity.models import FileImport` |
**Connectivity** | [FileImportCustomFilter](docs/v2/Connectivity/models/FileImportCustomFilter.md) | `from foundry.v2.connectivity.models import FileImportCustomFilter` |
**Connectivity** | [FileImportCustomFilterDict](docs/v2/Connectivity/models/FileImportCustomFilterDict.md) | `from foundry.v2.connectivity.models import FileImportCustomFilterDict` |
**Connectivity** | [FileImportDict](docs/v2/Connectivity/models/FileImportDict.md) | `from foundry.v2.connectivity.models import FileImportDict` |
**Connectivity** | [FileImportDisplayName](docs/v2/Connectivity/models/FileImportDisplayName.md) | `from foundry.v2.connectivity.models import FileImportDisplayName` |
**Connectivity** | [FileImportFilter](docs/v2/Connectivity/models/FileImportFilter.md) | `from foundry.v2.connectivity.models import FileImportFilter` |
**Connectivity** | [FileImportFilterDict](docs/v2/Connectivity/models/FileImportFilterDict.md) | `from foundry.v2.connectivity.models import FileImportFilterDict` |
**Connectivity** | [FileImportMode](docs/v2/Connectivity/models/FileImportMode.md) | `from foundry.v2.connectivity.models import FileImportMode` |
**Connectivity** | [FileImportRid](docs/v2/Connectivity/models/FileImportRid.md) | `from foundry.v2.connectivity.models import FileImportRid` |
**Connectivity** | [FileLastModifiedAfterFilter](docs/v2/Connectivity/models/FileLastModifiedAfterFilter.md) | `from foundry.v2.connectivity.models import FileLastModifiedAfterFilter` |
**Connectivity** | [FileLastModifiedAfterFilterDict](docs/v2/Connectivity/models/FileLastModifiedAfterFilterDict.md) | `from foundry.v2.connectivity.models import FileLastModifiedAfterFilterDict` |
**Connectivity** | [FilePathMatchesFilter](docs/v2/Connectivity/models/FilePathMatchesFilter.md) | `from foundry.v2.connectivity.models import FilePathMatchesFilter` |
**Connectivity** | [FilePathMatchesFilterDict](docs/v2/Connectivity/models/FilePathMatchesFilterDict.md) | `from foundry.v2.connectivity.models import FilePathMatchesFilterDict` |
**Connectivity** | [FilePathNotMatchesFilter](docs/v2/Connectivity/models/FilePathNotMatchesFilter.md) | `from foundry.v2.connectivity.models import FilePathNotMatchesFilter` |
**Connectivity** | [FilePathNotMatchesFilterDict](docs/v2/Connectivity/models/FilePathNotMatchesFilterDict.md) | `from foundry.v2.connectivity.models import FilePathNotMatchesFilterDict` |
**Connectivity** | [FileProperty](docs/v2/Connectivity/models/FileProperty.md) | `from foundry.v2.connectivity.models import FileProperty` |
**Connectivity** | [FilesCountLimitFilter](docs/v2/Connectivity/models/FilesCountLimitFilter.md) | `from foundry.v2.connectivity.models import FilesCountLimitFilter` |
**Connectivity** | [FilesCountLimitFilterDict](docs/v2/Connectivity/models/FilesCountLimitFilterDict.md) | `from foundry.v2.connectivity.models import FilesCountLimitFilterDict` |
**Connectivity** | [FileSizeFilter](docs/v2/Connectivity/models/FileSizeFilter.md) | `from foundry.v2.connectivity.models import FileSizeFilter` |
**Connectivity** | [FileSizeFilterDict](docs/v2/Connectivity/models/FileSizeFilterDict.md) | `from foundry.v2.connectivity.models import FileSizeFilterDict` |
**Connectivity** | [JdbcImportConfig](docs/v2/Connectivity/models/JdbcImportConfig.md) | `from foundry.v2.connectivity.models import JdbcImportConfig` |
**Connectivity** | [JdbcImportConfigDict](docs/v2/Connectivity/models/JdbcImportConfigDict.md) | `from foundry.v2.connectivity.models import JdbcImportConfigDict` |
**Connectivity** | [ListFileImportsResponse](docs/v2/Connectivity/models/ListFileImportsResponse.md) | `from foundry.v2.connectivity.models import ListFileImportsResponse` |
**Connectivity** | [ListFileImportsResponseDict](docs/v2/Connectivity/models/ListFileImportsResponseDict.md) | `from foundry.v2.connectivity.models import ListFileImportsResponseDict` |
**Connectivity** | [ListTableImportsResponse](docs/v2/Connectivity/models/ListTableImportsResponse.md) | `from foundry.v2.connectivity.models import ListTableImportsResponse` |
**Connectivity** | [ListTableImportsResponseDict](docs/v2/Connectivity/models/ListTableImportsResponseDict.md) | `from foundry.v2.connectivity.models import ListTableImportsResponseDict` |
**Connectivity** | [MicrosoftAccessImportConfig](docs/v2/Connectivity/models/MicrosoftAccessImportConfig.md) | `from foundry.v2.connectivity.models import MicrosoftAccessImportConfig` |
**Connectivity** | [MicrosoftAccessImportConfigDict](docs/v2/Connectivity/models/MicrosoftAccessImportConfigDict.md) | `from foundry.v2.connectivity.models import MicrosoftAccessImportConfigDict` |
**Connectivity** | [MicrosoftSqlServerImportConfig](docs/v2/Connectivity/models/MicrosoftSqlServerImportConfig.md) | `from foundry.v2.connectivity.models import MicrosoftSqlServerImportConfig` |
**Connectivity** | [MicrosoftSqlServerImportConfigDict](docs/v2/Connectivity/models/MicrosoftSqlServerImportConfigDict.md) | `from foundry.v2.connectivity.models import MicrosoftSqlServerImportConfigDict` |
**Connectivity** | [NetworkEgressPolicyRid](docs/v2/Connectivity/models/NetworkEgressPolicyRid.md) | `from foundry.v2.connectivity.models import NetworkEgressPolicyRid` |
**Connectivity** | [Oidc](docs/v2/Connectivity/models/Oidc.md) | `from foundry.v2.connectivity.models import Oidc` |
**Connectivity** | [OidcDict](docs/v2/Connectivity/models/OidcDict.md) | `from foundry.v2.connectivity.models import OidcDict` |
**Connectivity** | [OracleImportConfig](docs/v2/Connectivity/models/OracleImportConfig.md) | `from foundry.v2.connectivity.models import OracleImportConfig` |
**Connectivity** | [OracleImportConfigDict](docs/v2/Connectivity/models/OracleImportConfigDict.md) | `from foundry.v2.connectivity.models import OracleImportConfigDict` |
**Connectivity** | [PlaintextValue](docs/v2/Connectivity/models/PlaintextValue.md) | `from foundry.v2.connectivity.models import PlaintextValue` |
**Connectivity** | [PostgreSqlImportConfig](docs/v2/Connectivity/models/PostgreSqlImportConfig.md) | `from foundry.v2.connectivity.models import PostgreSqlImportConfig` |
**Connectivity** | [PostgreSqlImportConfigDict](docs/v2/Connectivity/models/PostgreSqlImportConfigDict.md) | `from foundry.v2.connectivity.models import PostgreSqlImportConfigDict` |
**Connectivity** | [Protocol](docs/v2/Connectivity/models/Protocol.md) | `from foundry.v2.connectivity.models import Protocol` |
**Connectivity** | [Region](docs/v2/Connectivity/models/Region.md) | `from foundry.v2.connectivity.models import Region` |
**Connectivity** | [RuntimePlatform](docs/v2/Connectivity/models/RuntimePlatform.md) | `from foundry.v2.connectivity.models import RuntimePlatform` |
**Connectivity** | [RuntimePlatformDict](docs/v2/Connectivity/models/RuntimePlatformDict.md) | `from foundry.v2.connectivity.models import RuntimePlatformDict` |
**Connectivity** | [S3AuthenticationMode](docs/v2/Connectivity/models/S3AuthenticationMode.md) | `from foundry.v2.connectivity.models import S3AuthenticationMode` |
**Connectivity** | [S3AuthenticationModeDict](docs/v2/Connectivity/models/S3AuthenticationModeDict.md) | `from foundry.v2.connectivity.models import S3AuthenticationModeDict` |
**Connectivity** | [S3ConnectionConfiguration](docs/v2/Connectivity/models/S3ConnectionConfiguration.md) | `from foundry.v2.connectivity.models import S3ConnectionConfiguration` |
**Connectivity** | [S3ConnectionConfigurationDict](docs/v2/Connectivity/models/S3ConnectionConfigurationDict.md) | `from foundry.v2.connectivity.models import S3ConnectionConfigurationDict` |
**Connectivity** | [S3KmsConfiguration](docs/v2/Connectivity/models/S3KmsConfiguration.md) | `from foundry.v2.connectivity.models import S3KmsConfiguration` |
**Connectivity** | [S3KmsConfigurationDict](docs/v2/Connectivity/models/S3KmsConfigurationDict.md) | `from foundry.v2.connectivity.models import S3KmsConfigurationDict` |
**Connectivity** | [S3ProxyConfiguration](docs/v2/Connectivity/models/S3ProxyConfiguration.md) | `from foundry.v2.connectivity.models import S3ProxyConfiguration` |
**Connectivity** | [S3ProxyConfigurationDict](docs/v2/Connectivity/models/S3ProxyConfigurationDict.md) | `from foundry.v2.connectivity.models import S3ProxyConfigurationDict` |
**Connectivity** | [SecretName](docs/v2/Connectivity/models/SecretName.md) | `from foundry.v2.connectivity.models import SecretName` |
**Connectivity** | [StsRoleConfiguration](docs/v2/Connectivity/models/StsRoleConfiguration.md) | `from foundry.v2.connectivity.models import StsRoleConfiguration` |
**Connectivity** | [StsRoleConfigurationDict](docs/v2/Connectivity/models/StsRoleConfigurationDict.md) | `from foundry.v2.connectivity.models import StsRoleConfigurationDict` |
**Connectivity** | [TableImport](docs/v2/Connectivity/models/TableImport.md) | `from foundry.v2.connectivity.models import TableImport` |
**Connectivity** | [TableImportAllowSchemaChanges](docs/v2/Connectivity/models/TableImportAllowSchemaChanges.md) | `from foundry.v2.connectivity.models import TableImportAllowSchemaChanges` |
**Connectivity** | [TableImportConfig](docs/v2/Connectivity/models/TableImportConfig.md) | `from foundry.v2.connectivity.models import TableImportConfig` |
**Connectivity** | [TableImportConfigDict](docs/v2/Connectivity/models/TableImportConfigDict.md) | `from foundry.v2.connectivity.models import TableImportConfigDict` |
**Connectivity** | [TableImportDict](docs/v2/Connectivity/models/TableImportDict.md) | `from foundry.v2.connectivity.models import TableImportDict` |
**Connectivity** | [TableImportDisplayName](docs/v2/Connectivity/models/TableImportDisplayName.md) | `from foundry.v2.connectivity.models import TableImportDisplayName` |
**Connectivity** | [TableImportMode](docs/v2/Connectivity/models/TableImportMode.md) | `from foundry.v2.connectivity.models import TableImportMode` |
**Connectivity** | [TableImportRid](docs/v2/Connectivity/models/TableImportRid.md) | `from foundry.v2.connectivity.models import TableImportRid` |
**Core** | [AnyType](docs/v2/Core/models/AnyType.md) | `from foundry.v2.core.models import AnyType` |
**Core** | [AnyTypeDict](docs/v2/Core/models/AnyTypeDict.md) | `from foundry.v2.core.models import AnyTypeDict` |
**Core** | [ArrayFieldType](docs/v2/Core/models/ArrayFieldType.md) | `from foundry.v2.core.models import ArrayFieldType` |
**Core** | [ArrayFieldTypeDict](docs/v2/Core/models/ArrayFieldTypeDict.md) | `from foundry.v2.core.models import ArrayFieldTypeDict` |
**Core** | [AttachmentType](docs/v2/Core/models/AttachmentType.md) | `from foundry.v2.core.models import AttachmentType` |
**Core** | [AttachmentTypeDict](docs/v2/Core/models/AttachmentTypeDict.md) | `from foundry.v2.core.models import AttachmentTypeDict` |
**Core** | [BinaryType](docs/v2/Core/models/BinaryType.md) | `from foundry.v2.core.models import BinaryType` |
**Core** | [BinaryTypeDict](docs/v2/Core/models/BinaryTypeDict.md) | `from foundry.v2.core.models import BinaryTypeDict` |
**Core** | [BooleanType](docs/v2/Core/models/BooleanType.md) | `from foundry.v2.core.models import BooleanType` |
**Core** | [BooleanTypeDict](docs/v2/Core/models/BooleanTypeDict.md) | `from foundry.v2.core.models import BooleanTypeDict` |
**Core** | [ByteType](docs/v2/Core/models/ByteType.md) | `from foundry.v2.core.models import ByteType` |
**Core** | [ByteTypeDict](docs/v2/Core/models/ByteTypeDict.md) | `from foundry.v2.core.models import ByteTypeDict` |
**Core** | [ChangeDataCaptureConfiguration](docs/v2/Core/models/ChangeDataCaptureConfiguration.md) | `from foundry.v2.core.models import ChangeDataCaptureConfiguration` |
**Core** | [ChangeDataCaptureConfigurationDict](docs/v2/Core/models/ChangeDataCaptureConfigurationDict.md) | `from foundry.v2.core.models import ChangeDataCaptureConfigurationDict` |
**Core** | [CipherTextType](docs/v2/Core/models/CipherTextType.md) | `from foundry.v2.core.models import CipherTextType` |
**Core** | [CipherTextTypeDict](docs/v2/Core/models/CipherTextTypeDict.md) | `from foundry.v2.core.models import CipherTextTypeDict` |
**Core** | [ContentLength](docs/v2/Core/models/ContentLength.md) | `from foundry.v2.core.models import ContentLength` |
**Core** | [ContentType](docs/v2/Core/models/ContentType.md) | `from foundry.v2.core.models import ContentType` |
**Core** | [CreatedBy](docs/v2/Core/models/CreatedBy.md) | `from foundry.v2.core.models import CreatedBy` |
**Core** | [CreatedTime](docs/v2/Core/models/CreatedTime.md) | `from foundry.v2.core.models import CreatedTime` |
**Core** | [CustomMetadata](docs/v2/Core/models/CustomMetadata.md) | `from foundry.v2.core.models import CustomMetadata` |
**Core** | [DateType](docs/v2/Core/models/DateType.md) | `from foundry.v2.core.models import DateType` |
**Core** | [DateTypeDict](docs/v2/Core/models/DateTypeDict.md) | `from foundry.v2.core.models import DateTypeDict` |
**Core** | [DecimalType](docs/v2/Core/models/DecimalType.md) | `from foundry.v2.core.models import DecimalType` |
**Core** | [DecimalTypeDict](docs/v2/Core/models/DecimalTypeDict.md) | `from foundry.v2.core.models import DecimalTypeDict` |
**Core** | [DisplayName](docs/v2/Core/models/DisplayName.md) | `from foundry.v2.core.models import DisplayName` |
**Core** | [Distance](docs/v2/Core/models/Distance.md) | `from foundry.v2.core.models import Distance` |
**Core** | [DistanceDict](docs/v2/Core/models/DistanceDict.md) | `from foundry.v2.core.models import DistanceDict` |
**Core** | [DistanceUnit](docs/v2/Core/models/DistanceUnit.md) | `from foundry.v2.core.models import DistanceUnit` |
**Core** | [DoubleType](docs/v2/Core/models/DoubleType.md) | `from foundry.v2.core.models import DoubleType` |
**Core** | [DoubleTypeDict](docs/v2/Core/models/DoubleTypeDict.md) | `from foundry.v2.core.models import DoubleTypeDict` |
**Core** | [Duration](docs/v2/Core/models/Duration.md) | `from foundry.v2.core.models import Duration` |
**Core** | [DurationDict](docs/v2/Core/models/DurationDict.md) | `from foundry.v2.core.models import DurationDict` |
**Core** | [EmbeddingModel](docs/v2/Core/models/EmbeddingModel.md) | `from foundry.v2.core.models import EmbeddingModel` |
**Core** | [EmbeddingModelDict](docs/v2/Core/models/EmbeddingModelDict.md) | `from foundry.v2.core.models import EmbeddingModelDict` |
**Core** | [EnrollmentRid](docs/v2/Core/models/EnrollmentRid.md) | `from foundry.v2.core.models import EnrollmentRid` |
**Core** | [Field](docs/v2/Core/models/Field.md) | `from foundry.v2.core.models import Field` |
**Core** | [FieldDataType](docs/v2/Core/models/FieldDataType.md) | `from foundry.v2.core.models import FieldDataType` |
**Core** | [FieldDataTypeDict](docs/v2/Core/models/FieldDataTypeDict.md) | `from foundry.v2.core.models import FieldDataTypeDict` |
**Core** | [FieldDict](docs/v2/Core/models/FieldDict.md) | `from foundry.v2.core.models import FieldDict` |
**Core** | [FieldName](docs/v2/Core/models/FieldName.md) | `from foundry.v2.core.models import FieldName` |
**Core** | [FieldSchema](docs/v2/Core/models/FieldSchema.md) | `from foundry.v2.core.models import FieldSchema` |
**Core** | [FieldSchemaDict](docs/v2/Core/models/FieldSchemaDict.md) | `from foundry.v2.core.models import FieldSchemaDict` |
**Core** | [Filename](docs/v2/Core/models/Filename.md) | `from foundry.v2.core.models import Filename` |
**Core** | [FilePath](docs/v2/Core/models/FilePath.md) | `from foundry.v2.core.models import FilePath` |
**Core** | [FilterBinaryTypeDict](docs/v2/Core/models/FilterBinaryTypeDict.md) | `from foundry.v2.core.models import FilterBinaryTypeDict` |
**Core** | [FilterBooleanTypeDict](docs/v2/Core/models/FilterBooleanTypeDict.md) | `from foundry.v2.core.models import FilterBooleanTypeDict` |
**Core** | [FilterDateTimeTypeDict](docs/v2/Core/models/FilterDateTimeTypeDict.md) | `from foundry.v2.core.models import FilterDateTimeTypeDict` |
**Core** | [FilterDateTypeDict](docs/v2/Core/models/FilterDateTypeDict.md) | `from foundry.v2.core.models import FilterDateTypeDict` |
**Core** | [FilterDoubleTypeDict](docs/v2/Core/models/FilterDoubleTypeDict.md) | `from foundry.v2.core.models import FilterDoubleTypeDict` |
**Core** | [FilterEnumTypeDict](docs/v2/Core/models/FilterEnumTypeDict.md) | `from foundry.v2.core.models import FilterEnumTypeDict` |
**Core** | [FilterFloatTypeDict](docs/v2/Core/models/FilterFloatTypeDict.md) | `from foundry.v2.core.models import FilterFloatTypeDict` |
**Core** | [FilterIntegerTypeDict](docs/v2/Core/models/FilterIntegerTypeDict.md) | `from foundry.v2.core.models import FilterIntegerTypeDict` |
**Core** | [FilterLongTypeDict](docs/v2/Core/models/FilterLongTypeDict.md) | `from foundry.v2.core.models import FilterLongTypeDict` |
**Core** | [FilterRidTypeDict](docs/v2/Core/models/FilterRidTypeDict.md) | `from foundry.v2.core.models import FilterRidTypeDict` |
**Core** | [FilterStringTypeDict](docs/v2/Core/models/FilterStringTypeDict.md) | `from foundry.v2.core.models import FilterStringTypeDict` |
**Core** | [FilterTypeDict](docs/v2/Core/models/FilterTypeDict.md) | `from foundry.v2.core.models import FilterTypeDict` |
**Core** | [FilterUuidTypeDict](docs/v2/Core/models/FilterUuidTypeDict.md) | `from foundry.v2.core.models import FilterUuidTypeDict` |
**Core** | [FloatType](docs/v2/Core/models/FloatType.md) | `from foundry.v2.core.models import FloatType` |
**Core** | [FloatTypeDict](docs/v2/Core/models/FloatTypeDict.md) | `from foundry.v2.core.models import FloatTypeDict` |
**Core** | [FolderRid](docs/v2/Core/models/FolderRid.md) | `from foundry.v2.core.models import FolderRid` |
**Core** | [FoundryLiveDeployment](docs/v2/Core/models/FoundryLiveDeployment.md) | `from foundry.v2.core.models import FoundryLiveDeployment` |
**Core** | [FoundryLiveDeploymentDict](docs/v2/Core/models/FoundryLiveDeploymentDict.md) | `from foundry.v2.core.models import FoundryLiveDeploymentDict` |
**Core** | [FullRowChangeDataCaptureConfiguration](docs/v2/Core/models/FullRowChangeDataCaptureConfiguration.md) | `from foundry.v2.core.models import FullRowChangeDataCaptureConfiguration` |
**Core** | [FullRowChangeDataCaptureConfigurationDict](docs/v2/Core/models/FullRowChangeDataCaptureConfigurationDict.md) | `from foundry.v2.core.models import FullRowChangeDataCaptureConfigurationDict` |
**Core** | [GeoPointType](docs/v2/Core/models/GeoPointType.md) | `from foundry.v2.core.models import GeoPointType` |
**Core** | [GeoPointTypeDict](docs/v2/Core/models/GeoPointTypeDict.md) | `from foundry.v2.core.models import GeoPointTypeDict` |
**Core** | [GeoShapeType](docs/v2/Core/models/GeoShapeType.md) | `from foundry.v2.core.models import GeoShapeType` |
**Core** | [GeoShapeTypeDict](docs/v2/Core/models/GeoShapeTypeDict.md) | `from foundry.v2.core.models import GeoShapeTypeDict` |
**Core** | [GeotimeSeriesReferenceType](docs/v2/Core/models/GeotimeSeriesReferenceType.md) | `from foundry.v2.core.models import GeotimeSeriesReferenceType` |
**Core** | [GeotimeSeriesReferenceTypeDict](docs/v2/Core/models/GeotimeSeriesReferenceTypeDict.md) | `from foundry.v2.core.models import GeotimeSeriesReferenceTypeDict` |
**Core** | [GroupName](docs/v2/Core/models/GroupName.md) | `from foundry.v2.core.models import GroupName` |
**Core** | [GroupRid](docs/v2/Core/models/GroupRid.md) | `from foundry.v2.core.models import GroupRid` |
**Core** | [IntegerType](docs/v2/Core/models/IntegerType.md) | `from foundry.v2.core.models import IntegerType` |
**Core** | [IntegerTypeDict](docs/v2/Core/models/IntegerTypeDict.md) | `from foundry.v2.core.models import IntegerTypeDict` |
**Core** | [LmsEmbeddingModel](docs/v2/Core/models/LmsEmbeddingModel.md) | `from foundry.v2.core.models import LmsEmbeddingModel` |
**Core** | [LmsEmbeddingModelDict](docs/v2/Core/models/LmsEmbeddingModelDict.md) | `from foundry.v2.core.models import LmsEmbeddingModelDict` |
**Core** | [LmsEmbeddingModelValue](docs/v2/Core/models/LmsEmbeddingModelValue.md) | `from foundry.v2.core.models import LmsEmbeddingModelValue` |
**Core** | [LongType](docs/v2/Core/models/LongType.md) | `from foundry.v2.core.models import LongType` |
**Core** | [LongTypeDict](docs/v2/Core/models/LongTypeDict.md) | `from foundry.v2.core.models import LongTypeDict` |
**Core** | [MapFieldType](docs/v2/Core/models/MapFieldType.md) | `from foundry.v2.core.models import MapFieldType` |
**Core** | [MapFieldTypeDict](docs/v2/Core/models/MapFieldTypeDict.md) | `from foundry.v2.core.models import MapFieldTypeDict` |
**Core** | [MarkingId](docs/v2/Core/models/MarkingId.md) | `from foundry.v2.core.models import MarkingId` |
**Core** | [MarkingType](docs/v2/Core/models/MarkingType.md) | `from foundry.v2.core.models import MarkingType` |
**Core** | [MarkingTypeDict](docs/v2/Core/models/MarkingTypeDict.md) | `from foundry.v2.core.models import MarkingTypeDict` |
**Core** | [MediaItemPath](docs/v2/Core/models/MediaItemPath.md) | `from foundry.v2.core.models import MediaItemPath` |
**Core** | [MediaItemReadToken](docs/v2/Core/models/MediaItemReadToken.md) | `from foundry.v2.core.models import MediaItemReadToken` |
**Core** | [MediaItemRid](docs/v2/Core/models/MediaItemRid.md) | `from foundry.v2.core.models import MediaItemRid` |
**Core** | [MediaReference](docs/v2/Core/models/MediaReference.md) | `from foundry.v2.core.models import MediaReference` |
**Core** | [MediaReferenceDict](docs/v2/Core/models/MediaReferenceDict.md) | `from foundry.v2.core.models import MediaReferenceDict` |
**Core** | [MediaReferenceType](docs/v2/Core/models/MediaReferenceType.md) | `from foundry.v2.core.models import MediaReferenceType` |
**Core** | [MediaReferenceTypeDict](docs/v2/Core/models/MediaReferenceTypeDict.md) | `from foundry.v2.core.models import MediaReferenceTypeDict` |
**Core** | [MediaSetRid](docs/v2/Core/models/MediaSetRid.md) | `from foundry.v2.core.models import MediaSetRid` |
**Core** | [MediaSetViewItem](docs/v2/Core/models/MediaSetViewItem.md) | `from foundry.v2.core.models import MediaSetViewItem` |
**Core** | [MediaSetViewItemDict](docs/v2/Core/models/MediaSetViewItemDict.md) | `from foundry.v2.core.models import MediaSetViewItemDict` |
**Core** | [MediaSetViewItemWrapper](docs/v2/Core/models/MediaSetViewItemWrapper.md) | `from foundry.v2.core.models import MediaSetViewItemWrapper` |
**Core** | [MediaSetViewItemWrapperDict](docs/v2/Core/models/MediaSetViewItemWrapperDict.md) | `from foundry.v2.core.models import MediaSetViewItemWrapperDict` |
**Core** | [MediaSetViewRid](docs/v2/Core/models/MediaSetViewRid.md) | `from foundry.v2.core.models import MediaSetViewRid` |
**Core** | [MediaType](docs/v2/Core/models/MediaType.md) | `from foundry.v2.core.models import MediaType` |
**Core** | [NullType](docs/v2/Core/models/NullType.md) | `from foundry.v2.core.models import NullType` |
**Core** | [NullTypeDict](docs/v2/Core/models/NullTypeDict.md) | `from foundry.v2.core.models import NullTypeDict` |
**Core** | [OrderByDirection](docs/v2/Core/models/OrderByDirection.md) | `from foundry.v2.core.models import OrderByDirection` |
**Core** | [OrganizationRid](docs/v2/Core/models/OrganizationRid.md) | `from foundry.v2.core.models import OrganizationRid` |
**Core** | [PageSize](docs/v2/Core/models/PageSize.md) | `from foundry.v2.core.models import PageSize` |
**Core** | [PageToken](docs/v2/Core/models/PageToken.md) | `from foundry.v2.core.models import PageToken` |
**Core** | [PreviewMode](docs/v2/Core/models/PreviewMode.md) | `from foundry.v2.core.models import PreviewMode` |
**Core** | [PrincipalId](docs/v2/Core/models/PrincipalId.md) | `from foundry.v2.core.models import PrincipalId` |
**Core** | [PrincipalType](docs/v2/Core/models/PrincipalType.md) | `from foundry.v2.core.models import PrincipalType` |
**Core** | [Realm](docs/v2/Core/models/Realm.md) | `from foundry.v2.core.models import Realm` |
**Core** | [Reference](docs/v2/Core/models/Reference.md) | `from foundry.v2.core.models import Reference` |
**Core** | [ReferenceDict](docs/v2/Core/models/ReferenceDict.md) | `from foundry.v2.core.models import ReferenceDict` |
**Core** | [ReleaseStatus](docs/v2/Core/models/ReleaseStatus.md) | `from foundry.v2.core.models import ReleaseStatus` |
**Core** | [RoleId](docs/v2/Core/models/RoleId.md) | `from foundry.v2.core.models import RoleId` |
**Core** | [ShortType](docs/v2/Core/models/ShortType.md) | `from foundry.v2.core.models import ShortType` |
**Core** | [ShortTypeDict](docs/v2/Core/models/ShortTypeDict.md) | `from foundry.v2.core.models import ShortTypeDict` |
**Core** | [SizeBytes](docs/v2/Core/models/SizeBytes.md) | `from foundry.v2.core.models import SizeBytes` |
**Core** | [StreamSchema](docs/v2/Core/models/StreamSchema.md) | `from foundry.v2.core.models import StreamSchema` |
**Core** | [StreamSchemaDict](docs/v2/Core/models/StreamSchemaDict.md) | `from foundry.v2.core.models import StreamSchemaDict` |
**Core** | [StringType](docs/v2/Core/models/StringType.md) | `from foundry.v2.core.models import StringType` |
**Core** | [StringTypeDict](docs/v2/Core/models/StringTypeDict.md) | `from foundry.v2.core.models import StringTypeDict` |
**Core** | [StructFieldName](docs/v2/Core/models/StructFieldName.md) | `from foundry.v2.core.models import StructFieldName` |
**Core** | [StructFieldType](docs/v2/Core/models/StructFieldType.md) | `from foundry.v2.core.models import StructFieldType` |
**Core** | [StructFieldTypeDict](docs/v2/Core/models/StructFieldTypeDict.md) | `from foundry.v2.core.models import StructFieldTypeDict` |
**Core** | [TimeSeriesItemType](docs/v2/Core/models/TimeSeriesItemType.md) | `from foundry.v2.core.models import TimeSeriesItemType` |
**Core** | [TimeSeriesItemTypeDict](docs/v2/Core/models/TimeSeriesItemTypeDict.md) | `from foundry.v2.core.models import TimeSeriesItemTypeDict` |
**Core** | [TimeseriesType](docs/v2/Core/models/TimeseriesType.md) | `from foundry.v2.core.models import TimeseriesType` |
**Core** | [TimeseriesTypeDict](docs/v2/Core/models/TimeseriesTypeDict.md) | `from foundry.v2.core.models import TimeseriesTypeDict` |
**Core** | [TimestampType](docs/v2/Core/models/TimestampType.md) | `from foundry.v2.core.models import TimestampType` |
**Core** | [TimestampTypeDict](docs/v2/Core/models/TimestampTypeDict.md) | `from foundry.v2.core.models import TimestampTypeDict` |
**Core** | [TimeUnit](docs/v2/Core/models/TimeUnit.md) | `from foundry.v2.core.models import TimeUnit` |
**Core** | [TotalCount](docs/v2/Core/models/TotalCount.md) | `from foundry.v2.core.models import TotalCount` |
**Core** | [UnsupportedType](docs/v2/Core/models/UnsupportedType.md) | `from foundry.v2.core.models import UnsupportedType` |
**Core** | [UnsupportedTypeDict](docs/v2/Core/models/UnsupportedTypeDict.md) | `from foundry.v2.core.models import UnsupportedTypeDict` |
**Core** | [UpdatedBy](docs/v2/Core/models/UpdatedBy.md) | `from foundry.v2.core.models import UpdatedBy` |
**Core** | [UpdatedTime](docs/v2/Core/models/UpdatedTime.md) | `from foundry.v2.core.models import UpdatedTime` |
**Core** | [UserId](docs/v2/Core/models/UserId.md) | `from foundry.v2.core.models import UserId` |
**Core** | [VectorSimilarityFunction](docs/v2/Core/models/VectorSimilarityFunction.md) | `from foundry.v2.core.models import VectorSimilarityFunction` |
**Core** | [VectorSimilarityFunctionDict](docs/v2/Core/models/VectorSimilarityFunctionDict.md) | `from foundry.v2.core.models import VectorSimilarityFunctionDict` |
**Core** | [VectorSimilarityFunctionValue](docs/v2/Core/models/VectorSimilarityFunctionValue.md) | `from foundry.v2.core.models import VectorSimilarityFunctionValue` |
**Core** | [VectorType](docs/v2/Core/models/VectorType.md) | `from foundry.v2.core.models import VectorType` |
**Core** | [VectorTypeDict](docs/v2/Core/models/VectorTypeDict.md) | `from foundry.v2.core.models import VectorTypeDict` |
**Core** | [ZoneId](docs/v2/Core/models/ZoneId.md) | `from foundry.v2.core.models import ZoneId` |
**Datasets** | [Branch](docs/v2/Datasets/models/Branch.md) | `from foundry.v2.datasets.models import Branch` |
**Datasets** | [BranchDict](docs/v2/Datasets/models/BranchDict.md) | `from foundry.v2.datasets.models import BranchDict` |
**Datasets** | [BranchName](docs/v2/Datasets/models/BranchName.md) | `from foundry.v2.datasets.models import BranchName` |
**Datasets** | [Dataset](docs/v2/Datasets/models/Dataset.md) | `from foundry.v2.datasets.models import Dataset` |
**Datasets** | [DatasetDict](docs/v2/Datasets/models/DatasetDict.md) | `from foundry.v2.datasets.models import DatasetDict` |
**Datasets** | [DatasetName](docs/v2/Datasets/models/DatasetName.md) | `from foundry.v2.datasets.models import DatasetName` |
**Datasets** | [DatasetRid](docs/v2/Datasets/models/DatasetRid.md) | `from foundry.v2.datasets.models import DatasetRid` |
**Datasets** | [File](docs/v2/Datasets/models/File.md) | `from foundry.v2.datasets.models import File` |
**Datasets** | [FileDict](docs/v2/Datasets/models/FileDict.md) | `from foundry.v2.datasets.models import FileDict` |
**Datasets** | [FileUpdatedTime](docs/v2/Datasets/models/FileUpdatedTime.md) | `from foundry.v2.datasets.models import FileUpdatedTime` |
**Datasets** | [ListBranchesResponse](docs/v2/Datasets/models/ListBranchesResponse.md) | `from foundry.v2.datasets.models import ListBranchesResponse` |
**Datasets** | [ListBranchesResponseDict](docs/v2/Datasets/models/ListBranchesResponseDict.md) | `from foundry.v2.datasets.models import ListBranchesResponseDict` |
**Datasets** | [ListFilesResponse](docs/v2/Datasets/models/ListFilesResponse.md) | `from foundry.v2.datasets.models import ListFilesResponse` |
**Datasets** | [ListFilesResponseDict](docs/v2/Datasets/models/ListFilesResponseDict.md) | `from foundry.v2.datasets.models import ListFilesResponseDict` |
**Datasets** | [TableExportFormat](docs/v2/Datasets/models/TableExportFormat.md) | `from foundry.v2.datasets.models import TableExportFormat` |
**Datasets** | [Transaction](docs/v2/Datasets/models/Transaction.md) | `from foundry.v2.datasets.models import Transaction` |
**Datasets** | [TransactionCreatedTime](docs/v2/Datasets/models/TransactionCreatedTime.md) | `from foundry.v2.datasets.models import TransactionCreatedTime` |
**Datasets** | [TransactionDict](docs/v2/Datasets/models/TransactionDict.md) | `from foundry.v2.datasets.models import TransactionDict` |
**Datasets** | [TransactionRid](docs/v2/Datasets/models/TransactionRid.md) | `from foundry.v2.datasets.models import TransactionRid` |
**Datasets** | [TransactionStatus](docs/v2/Datasets/models/TransactionStatus.md) | `from foundry.v2.datasets.models import TransactionStatus` |
**Datasets** | [TransactionType](docs/v2/Datasets/models/TransactionType.md) | `from foundry.v2.datasets.models import TransactionType` |
**Filesystem** | [AccessRequirements](docs/v2/Filesystem/models/AccessRequirements.md) | `from foundry.v2.filesystem.models import AccessRequirements` |
**Filesystem** | [AccessRequirementsDict](docs/v2/Filesystem/models/AccessRequirementsDict.md) | `from foundry.v2.filesystem.models import AccessRequirementsDict` |
**Filesystem** | [Everyone](docs/v2/Filesystem/models/Everyone.md) | `from foundry.v2.filesystem.models import Everyone` |
**Filesystem** | [EveryoneDict](docs/v2/Filesystem/models/EveryoneDict.md) | `from foundry.v2.filesystem.models import EveryoneDict` |
**Filesystem** | [FileSystemId](docs/v2/Filesystem/models/FileSystemId.md) | `from foundry.v2.filesystem.models import FileSystemId` |
**Filesystem** | [Folder](docs/v2/Filesystem/models/Folder.md) | `from foundry.v2.filesystem.models import Folder` |
**Filesystem** | [FolderDict](docs/v2/Filesystem/models/FolderDict.md) | `from foundry.v2.filesystem.models import FolderDict` |
**Filesystem** | [FolderRid](docs/v2/Filesystem/models/FolderRid.md) | `from foundry.v2.filesystem.models import FolderRid` |
**Filesystem** | [FolderType](docs/v2/Filesystem/models/FolderType.md) | `from foundry.v2.filesystem.models import FolderType` |
**Filesystem** | [IsDirectlyApplied](docs/v2/Filesystem/models/IsDirectlyApplied.md) | `from foundry.v2.filesystem.models import IsDirectlyApplied` |
**Filesystem** | [ListChildrenOfFolderResponse](docs/v2/Filesystem/models/ListChildrenOfFolderResponse.md) | `from foundry.v2.filesystem.models import ListChildrenOfFolderResponse` |
**Filesystem** | [ListChildrenOfFolderResponseDict](docs/v2/Filesystem/models/ListChildrenOfFolderResponseDict.md) | `from foundry.v2.filesystem.models import ListChildrenOfFolderResponseDict` |
**Filesystem** | [ListMarkingsOfResourceResponse](docs/v2/Filesystem/models/ListMarkingsOfResourceResponse.md) | `from foundry.v2.filesystem.models import ListMarkingsOfResourceResponse` |
**Filesystem** | [ListMarkingsOfResourceResponseDict](docs/v2/Filesystem/models/ListMarkingsOfResourceResponseDict.md) | `from foundry.v2.filesystem.models import ListMarkingsOfResourceResponseDict` |
**Filesystem** | [ListOrganizationsOfProjectResponse](docs/v2/Filesystem/models/ListOrganizationsOfProjectResponse.md) | `from foundry.v2.filesystem.models import ListOrganizationsOfProjectResponse` |
**Filesystem** | [ListOrganizationsOfProjectResponseDict](docs/v2/Filesystem/models/ListOrganizationsOfProjectResponseDict.md) | `from foundry.v2.filesystem.models import ListOrganizationsOfProjectResponseDict` |
**Filesystem** | [ListResourceRolesResponse](docs/v2/Filesystem/models/ListResourceRolesResponse.md) | `from foundry.v2.filesystem.models import ListResourceRolesResponse` |
**Filesystem** | [ListResourceRolesResponseDict](docs/v2/Filesystem/models/ListResourceRolesResponseDict.md) | `from foundry.v2.filesystem.models import ListResourceRolesResponseDict` |
**Filesystem** | [ListSpacesResponse](docs/v2/Filesystem/models/ListSpacesResponse.md) | `from foundry.v2.filesystem.models import ListSpacesResponse` |
**Filesystem** | [ListSpacesResponseDict](docs/v2/Filesystem/models/ListSpacesResponseDict.md) | `from foundry.v2.filesystem.models import ListSpacesResponseDict` |
**Filesystem** | [Marking](docs/v2/Filesystem/models/Marking.md) | `from foundry.v2.filesystem.models import Marking` |
**Filesystem** | [MarkingDict](docs/v2/Filesystem/models/MarkingDict.md) | `from foundry.v2.filesystem.models import MarkingDict` |
**Filesystem** | [Organization](docs/v2/Filesystem/models/Organization.md) | `from foundry.v2.filesystem.models import Organization` |
**Filesystem** | [OrganizationDict](docs/v2/Filesystem/models/OrganizationDict.md) | `from foundry.v2.filesystem.models import OrganizationDict` |
**Filesystem** | [PrincipalWithId](docs/v2/Filesystem/models/PrincipalWithId.md) | `from foundry.v2.filesystem.models import PrincipalWithId` |
**Filesystem** | [PrincipalWithIdDict](docs/v2/Filesystem/models/PrincipalWithIdDict.md) | `from foundry.v2.filesystem.models import PrincipalWithIdDict` |
**Filesystem** | [Project](docs/v2/Filesystem/models/Project.md) | `from foundry.v2.filesystem.models import Project` |
**Filesystem** | [ProjectDict](docs/v2/Filesystem/models/ProjectDict.md) | `from foundry.v2.filesystem.models import ProjectDict` |
**Filesystem** | [ProjectRid](docs/v2/Filesystem/models/ProjectRid.md) | `from foundry.v2.filesystem.models import ProjectRid` |
**Filesystem** | [ProjectTemplateRid](docs/v2/Filesystem/models/ProjectTemplateRid.md) | `from foundry.v2.filesystem.models import ProjectTemplateRid` |
**Filesystem** | [ProjectTemplateVariableId](docs/v2/Filesystem/models/ProjectTemplateVariableId.md) | `from foundry.v2.filesystem.models import ProjectTemplateVariableId` |
**Filesystem** | [ProjectTemplateVariableValue](docs/v2/Filesystem/models/ProjectTemplateVariableValue.md) | `from foundry.v2.filesystem.models import ProjectTemplateVariableValue` |
**Filesystem** | [Resource](docs/v2/Filesystem/models/Resource.md) | `from foundry.v2.filesystem.models import Resource` |
**Filesystem** | [ResourceDict](docs/v2/Filesystem/models/ResourceDict.md) | `from foundry.v2.filesystem.models import ResourceDict` |
**Filesystem** | [ResourceDisplayName](docs/v2/Filesystem/models/ResourceDisplayName.md) | `from foundry.v2.filesystem.models import ResourceDisplayName` |
**Filesystem** | [ResourcePath](docs/v2/Filesystem/models/ResourcePath.md) | `from foundry.v2.filesystem.models import ResourcePath` |
**Filesystem** | [ResourceRid](docs/v2/Filesystem/models/ResourceRid.md) | `from foundry.v2.filesystem.models import ResourceRid` |
**Filesystem** | [ResourceRole](docs/v2/Filesystem/models/ResourceRole.md) | `from foundry.v2.filesystem.models import ResourceRole` |
**Filesystem** | [ResourceRoleDict](docs/v2/Filesystem/models/ResourceRoleDict.md) | `from foundry.v2.filesystem.models import ResourceRoleDict` |
**Filesystem** | [ResourceRolePrincipal](docs/v2/Filesystem/models/ResourceRolePrincipal.md) | `from foundry.v2.filesystem.models import ResourceRolePrincipal` |
**Filesystem** | [ResourceRolePrincipalDict](docs/v2/Filesystem/models/ResourceRolePrincipalDict.md) | `from foundry.v2.filesystem.models import ResourceRolePrincipalDict` |
**Filesystem** | [ResourceType](docs/v2/Filesystem/models/ResourceType.md) | `from foundry.v2.filesystem.models import ResourceType` |
**Filesystem** | [Space](docs/v2/Filesystem/models/Space.md) | `from foundry.v2.filesystem.models import Space` |
**Filesystem** | [SpaceDict](docs/v2/Filesystem/models/SpaceDict.md) | `from foundry.v2.filesystem.models import SpaceDict` |
**Filesystem** | [SpaceRid](docs/v2/Filesystem/models/SpaceRid.md) | `from foundry.v2.filesystem.models import SpaceRid` |
**Filesystem** | [TrashStatus](docs/v2/Filesystem/models/TrashStatus.md) | `from foundry.v2.filesystem.models import TrashStatus` |
**Filesystem** | [UsageAccountRid](docs/v2/Filesystem/models/UsageAccountRid.md) | `from foundry.v2.filesystem.models import UsageAccountRid` |
**Functions** | [DataValue](docs/v2/Functions/models/DataValue.md) | `from foundry.v2.functions.models import DataValue` |
**Functions** | [ExecuteQueryResponse](docs/v2/Functions/models/ExecuteQueryResponse.md) | `from foundry.v2.functions.models import ExecuteQueryResponse` |
**Functions** | [ExecuteQueryResponseDict](docs/v2/Functions/models/ExecuteQueryResponseDict.md) | `from foundry.v2.functions.models import ExecuteQueryResponseDict` |
**Functions** | [FunctionRid](docs/v2/Functions/models/FunctionRid.md) | `from foundry.v2.functions.models import FunctionRid` |
**Functions** | [FunctionVersion](docs/v2/Functions/models/FunctionVersion.md) | `from foundry.v2.functions.models import FunctionVersion` |
**Functions** | [Parameter](docs/v2/Functions/models/Parameter.md) | `from foundry.v2.functions.models import Parameter` |
**Functions** | [ParameterDict](docs/v2/Functions/models/ParameterDict.md) | `from foundry.v2.functions.models import ParameterDict` |
**Functions** | [ParameterId](docs/v2/Functions/models/ParameterId.md) | `from foundry.v2.functions.models import ParameterId` |
**Functions** | [Query](docs/v2/Functions/models/Query.md) | `from foundry.v2.functions.models import Query` |
**Functions** | [QueryAggregationKeyType](docs/v2/Functions/models/QueryAggregationKeyType.md) | `from foundry.v2.functions.models import QueryAggregationKeyType` |
**Functions** | [QueryAggregationKeyTypeDict](docs/v2/Functions/models/QueryAggregationKeyTypeDict.md) | `from foundry.v2.functions.models import QueryAggregationKeyTypeDict` |
**Functions** | [QueryAggregationRangeSubType](docs/v2/Functions/models/QueryAggregationRangeSubType.md) | `from foundry.v2.functions.models import QueryAggregationRangeSubType` |
**Functions** | [QueryAggregationRangeSubTypeDict](docs/v2/Functions/models/QueryAggregationRangeSubTypeDict.md) | `from foundry.v2.functions.models import QueryAggregationRangeSubTypeDict` |
**Functions** | [QueryAggregationRangeType](docs/v2/Functions/models/QueryAggregationRangeType.md) | `from foundry.v2.functions.models import QueryAggregationRangeType` |
**Functions** | [QueryAggregationRangeTypeDict](docs/v2/Functions/models/QueryAggregationRangeTypeDict.md) | `from foundry.v2.functions.models import QueryAggregationRangeTypeDict` |
**Functions** | [QueryAggregationValueType](docs/v2/Functions/models/QueryAggregationValueType.md) | `from foundry.v2.functions.models import QueryAggregationValueType` |
**Functions** | [QueryAggregationValueTypeDict](docs/v2/Functions/models/QueryAggregationValueTypeDict.md) | `from foundry.v2.functions.models import QueryAggregationValueTypeDict` |
**Functions** | [QueryApiName](docs/v2/Functions/models/QueryApiName.md) | `from foundry.v2.functions.models import QueryApiName` |
**Functions** | [QueryArrayType](docs/v2/Functions/models/QueryArrayType.md) | `from foundry.v2.functions.models import QueryArrayType` |
**Functions** | [QueryArrayTypeDict](docs/v2/Functions/models/QueryArrayTypeDict.md) | `from foundry.v2.functions.models import QueryArrayTypeDict` |
**Functions** | [QueryDataType](docs/v2/Functions/models/QueryDataType.md) | `from foundry.v2.functions.models import QueryDataType` |
**Functions** | [QueryDataTypeDict](docs/v2/Functions/models/QueryDataTypeDict.md) | `from foundry.v2.functions.models import QueryDataTypeDict` |
**Functions** | [QueryDict](docs/v2/Functions/models/QueryDict.md) | `from foundry.v2.functions.models import QueryDict` |
**Functions** | [QueryRuntimeErrorParameter](docs/v2/Functions/models/QueryRuntimeErrorParameter.md) | `from foundry.v2.functions.models import QueryRuntimeErrorParameter` |
**Functions** | [QuerySetType](docs/v2/Functions/models/QuerySetType.md) | `from foundry.v2.functions.models import QuerySetType` |
**Functions** | [QuerySetTypeDict](docs/v2/Functions/models/QuerySetTypeDict.md) | `from foundry.v2.functions.models import QuerySetTypeDict` |
**Functions** | [QueryStructField](docs/v2/Functions/models/QueryStructField.md) | `from foundry.v2.functions.models import QueryStructField` |
**Functions** | [QueryStructFieldDict](docs/v2/Functions/models/QueryStructFieldDict.md) | `from foundry.v2.functions.models import QueryStructFieldDict` |
**Functions** | [QueryStructType](docs/v2/Functions/models/QueryStructType.md) | `from foundry.v2.functions.models import QueryStructType` |
**Functions** | [QueryStructTypeDict](docs/v2/Functions/models/QueryStructTypeDict.md) | `from foundry.v2.functions.models import QueryStructTypeDict` |
**Functions** | [QueryUnionType](docs/v2/Functions/models/QueryUnionType.md) | `from foundry.v2.functions.models import QueryUnionType` |
**Functions** | [QueryUnionTypeDict](docs/v2/Functions/models/QueryUnionTypeDict.md) | `from foundry.v2.functions.models import QueryUnionTypeDict` |
**Functions** | [StructFieldName](docs/v2/Functions/models/StructFieldName.md) | `from foundry.v2.functions.models import StructFieldName` |
**Functions** | [ThreeDimensionalAggregation](docs/v2/Functions/models/ThreeDimensionalAggregation.md) | `from foundry.v2.functions.models import ThreeDimensionalAggregation` |
**Functions** | [ThreeDimensionalAggregationDict](docs/v2/Functions/models/ThreeDimensionalAggregationDict.md) | `from foundry.v2.functions.models import ThreeDimensionalAggregationDict` |
**Functions** | [TwoDimensionalAggregation](docs/v2/Functions/models/TwoDimensionalAggregation.md) | `from foundry.v2.functions.models import TwoDimensionalAggregation` |
**Functions** | [TwoDimensionalAggregationDict](docs/v2/Functions/models/TwoDimensionalAggregationDict.md) | `from foundry.v2.functions.models import TwoDimensionalAggregationDict` |
**Functions** | [ValueType](docs/v2/Functions/models/ValueType.md) | `from foundry.v2.functions.models import ValueType` |
**Functions** | [ValueTypeApiName](docs/v2/Functions/models/ValueTypeApiName.md) | `from foundry.v2.functions.models import ValueTypeApiName` |
**Functions** | [ValueTypeDataType](docs/v2/Functions/models/ValueTypeDataType.md) | `from foundry.v2.functions.models import ValueTypeDataType` |
**Functions** | [ValueTypeDataTypeArrayType](docs/v2/Functions/models/ValueTypeDataTypeArrayType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeArrayType` |
**Functions** | [ValueTypeDataTypeArrayTypeDict](docs/v2/Functions/models/ValueTypeDataTypeArrayTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeArrayTypeDict` |
**Functions** | [ValueTypeDataTypeBinaryType](docs/v2/Functions/models/ValueTypeDataTypeBinaryType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeBinaryType` |
**Functions** | [ValueTypeDataTypeBinaryTypeDict](docs/v2/Functions/models/ValueTypeDataTypeBinaryTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeBinaryTypeDict` |
**Functions** | [ValueTypeDataTypeBooleanType](docs/v2/Functions/models/ValueTypeDataTypeBooleanType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeBooleanType` |
**Functions** | [ValueTypeDataTypeBooleanTypeDict](docs/v2/Functions/models/ValueTypeDataTypeBooleanTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeBooleanTypeDict` |
**Functions** | [ValueTypeDataTypeByteType](docs/v2/Functions/models/ValueTypeDataTypeByteType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeByteType` |
**Functions** | [ValueTypeDataTypeByteTypeDict](docs/v2/Functions/models/ValueTypeDataTypeByteTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeByteTypeDict` |
**Functions** | [ValueTypeDataTypeDateType](docs/v2/Functions/models/ValueTypeDataTypeDateType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeDateType` |
**Functions** | [ValueTypeDataTypeDateTypeDict](docs/v2/Functions/models/ValueTypeDataTypeDateTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeDateTypeDict` |
**Functions** | [ValueTypeDataTypeDecimalType](docs/v2/Functions/models/ValueTypeDataTypeDecimalType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeDecimalType` |
**Functions** | [ValueTypeDataTypeDecimalTypeDict](docs/v2/Functions/models/ValueTypeDataTypeDecimalTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeDecimalTypeDict` |
**Functions** | [ValueTypeDataTypeDict](docs/v2/Functions/models/ValueTypeDataTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeDict` |
**Functions** | [ValueTypeDataTypeDoubleType](docs/v2/Functions/models/ValueTypeDataTypeDoubleType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeDoubleType` |
**Functions** | [ValueTypeDataTypeDoubleTypeDict](docs/v2/Functions/models/ValueTypeDataTypeDoubleTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeDoubleTypeDict` |
**Functions** | [ValueTypeDataTypeFloatType](docs/v2/Functions/models/ValueTypeDataTypeFloatType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeFloatType` |
**Functions** | [ValueTypeDataTypeFloatTypeDict](docs/v2/Functions/models/ValueTypeDataTypeFloatTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeFloatTypeDict` |
**Functions** | [ValueTypeDataTypeIntegerType](docs/v2/Functions/models/ValueTypeDataTypeIntegerType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeIntegerType` |
**Functions** | [ValueTypeDataTypeIntegerTypeDict](docs/v2/Functions/models/ValueTypeDataTypeIntegerTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeIntegerTypeDict` |
**Functions** | [ValueTypeDataTypeLongType](docs/v2/Functions/models/ValueTypeDataTypeLongType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeLongType` |
**Functions** | [ValueTypeDataTypeLongTypeDict](docs/v2/Functions/models/ValueTypeDataTypeLongTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeLongTypeDict` |
**Functions** | [ValueTypeDataTypeMapType](docs/v2/Functions/models/ValueTypeDataTypeMapType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeMapType` |
**Functions** | [ValueTypeDataTypeMapTypeDict](docs/v2/Functions/models/ValueTypeDataTypeMapTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeMapTypeDict` |
**Functions** | [ValueTypeDataTypeOptionalType](docs/v2/Functions/models/ValueTypeDataTypeOptionalType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeOptionalType` |
**Functions** | [ValueTypeDataTypeOptionalTypeDict](docs/v2/Functions/models/ValueTypeDataTypeOptionalTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeOptionalTypeDict` |
**Functions** | [ValueTypeDataTypeShortType](docs/v2/Functions/models/ValueTypeDataTypeShortType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeShortType` |
**Functions** | [ValueTypeDataTypeShortTypeDict](docs/v2/Functions/models/ValueTypeDataTypeShortTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeShortTypeDict` |
**Functions** | [ValueTypeDataTypeStringType](docs/v2/Functions/models/ValueTypeDataTypeStringType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeStringType` |
**Functions** | [ValueTypeDataTypeStringTypeDict](docs/v2/Functions/models/ValueTypeDataTypeStringTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeStringTypeDict` |
**Functions** | [ValueTypeDataTypeStructElement](docs/v2/Functions/models/ValueTypeDataTypeStructElement.md) | `from foundry.v2.functions.models import ValueTypeDataTypeStructElement` |
**Functions** | [ValueTypeDataTypeStructElementDict](docs/v2/Functions/models/ValueTypeDataTypeStructElementDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeStructElementDict` |
**Functions** | [ValueTypeDataTypeStructFieldIdentifier](docs/v2/Functions/models/ValueTypeDataTypeStructFieldIdentifier.md) | `from foundry.v2.functions.models import ValueTypeDataTypeStructFieldIdentifier` |
**Functions** | [ValueTypeDataTypeStructType](docs/v2/Functions/models/ValueTypeDataTypeStructType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeStructType` |
**Functions** | [ValueTypeDataTypeStructTypeDict](docs/v2/Functions/models/ValueTypeDataTypeStructTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeStructTypeDict` |
**Functions** | [ValueTypeDataTypeTimestampType](docs/v2/Functions/models/ValueTypeDataTypeTimestampType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeTimestampType` |
**Functions** | [ValueTypeDataTypeTimestampTypeDict](docs/v2/Functions/models/ValueTypeDataTypeTimestampTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeTimestampTypeDict` |
**Functions** | [ValueTypeDataTypeUnionType](docs/v2/Functions/models/ValueTypeDataTypeUnionType.md) | `from foundry.v2.functions.models import ValueTypeDataTypeUnionType` |
**Functions** | [ValueTypeDataTypeUnionTypeDict](docs/v2/Functions/models/ValueTypeDataTypeUnionTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeUnionTypeDict` |
**Functions** | [ValueTypeDataTypeValueTypeReference](docs/v2/Functions/models/ValueTypeDataTypeValueTypeReference.md) | `from foundry.v2.functions.models import ValueTypeDataTypeValueTypeReference` |
**Functions** | [ValueTypeDataTypeValueTypeReferenceDict](docs/v2/Functions/models/ValueTypeDataTypeValueTypeReferenceDict.md) | `from foundry.v2.functions.models import ValueTypeDataTypeValueTypeReferenceDict` |
**Functions** | [ValueTypeDescription](docs/v2/Functions/models/ValueTypeDescription.md) | `from foundry.v2.functions.models import ValueTypeDescription` |
**Functions** | [ValueTypeDict](docs/v2/Functions/models/ValueTypeDict.md) | `from foundry.v2.functions.models import ValueTypeDict` |
**Functions** | [ValueTypeReference](docs/v2/Functions/models/ValueTypeReference.md) | `from foundry.v2.functions.models import ValueTypeReference` |
**Functions** | [ValueTypeReferenceDict](docs/v2/Functions/models/ValueTypeReferenceDict.md) | `from foundry.v2.functions.models import ValueTypeReferenceDict` |
**Functions** | [ValueTypeRid](docs/v2/Functions/models/ValueTypeRid.md) | `from foundry.v2.functions.models import ValueTypeRid` |
**Functions** | [ValueTypeVersion](docs/v2/Functions/models/ValueTypeVersion.md) | `from foundry.v2.functions.models import ValueTypeVersion` |
**Functions** | [ValueTypeVersionId](docs/v2/Functions/models/ValueTypeVersionId.md) | `from foundry.v2.functions.models import ValueTypeVersionId` |
**Functions** | [VersionId](docs/v2/Functions/models/VersionId.md) | `from foundry.v2.functions.models import VersionId` |
**Functions** | [VersionIdDict](docs/v2/Functions/models/VersionIdDict.md) | `from foundry.v2.functions.models import VersionIdDict` |
**Geo** | [BBox](docs/v2/Geo/models/BBox.md) | `from foundry.v2.geo.models import BBox` |
**Geo** | [Coordinate](docs/v2/Geo/models/Coordinate.md) | `from foundry.v2.geo.models import Coordinate` |
**Geo** | [Feature](docs/v2/Geo/models/Feature.md) | `from foundry.v2.geo.models import Feature` |
**Geo** | [FeatureCollection](docs/v2/Geo/models/FeatureCollection.md) | `from foundry.v2.geo.models import FeatureCollection` |
**Geo** | [FeatureCollectionDict](docs/v2/Geo/models/FeatureCollectionDict.md) | `from foundry.v2.geo.models import FeatureCollectionDict` |
**Geo** | [FeatureCollectionTypes](docs/v2/Geo/models/FeatureCollectionTypes.md) | `from foundry.v2.geo.models import FeatureCollectionTypes` |
**Geo** | [FeatureCollectionTypesDict](docs/v2/Geo/models/FeatureCollectionTypesDict.md) | `from foundry.v2.geo.models import FeatureCollectionTypesDict` |
**Geo** | [FeatureDict](docs/v2/Geo/models/FeatureDict.md) | `from foundry.v2.geo.models import FeatureDict` |
**Geo** | [FeaturePropertyKey](docs/v2/Geo/models/FeaturePropertyKey.md) | `from foundry.v2.geo.models import FeaturePropertyKey` |
**Geo** | [Geometry](docs/v2/Geo/models/Geometry.md) | `from foundry.v2.geo.models import Geometry` |
**Geo** | [GeometryCollection](docs/v2/Geo/models/GeometryCollection.md) | `from foundry.v2.geo.models import GeometryCollection` |
**Geo** | [GeometryCollectionDict](docs/v2/Geo/models/GeometryCollectionDict.md) | `from foundry.v2.geo.models import GeometryCollectionDict` |
**Geo** | [GeometryDict](docs/v2/Geo/models/GeometryDict.md) | `from foundry.v2.geo.models import GeometryDict` |
**Geo** | [GeoPoint](docs/v2/Geo/models/GeoPoint.md) | `from foundry.v2.geo.models import GeoPoint` |
**Geo** | [GeoPointDict](docs/v2/Geo/models/GeoPointDict.md) | `from foundry.v2.geo.models import GeoPointDict` |
**Geo** | [LinearRing](docs/v2/Geo/models/LinearRing.md) | `from foundry.v2.geo.models import LinearRing` |
**Geo** | [LineString](docs/v2/Geo/models/LineString.md) | `from foundry.v2.geo.models import LineString` |
**Geo** | [LineStringCoordinates](docs/v2/Geo/models/LineStringCoordinates.md) | `from foundry.v2.geo.models import LineStringCoordinates` |
**Geo** | [LineStringDict](docs/v2/Geo/models/LineStringDict.md) | `from foundry.v2.geo.models import LineStringDict` |
**Geo** | [MultiLineString](docs/v2/Geo/models/MultiLineString.md) | `from foundry.v2.geo.models import MultiLineString` |
**Geo** | [MultiLineStringDict](docs/v2/Geo/models/MultiLineStringDict.md) | `from foundry.v2.geo.models import MultiLineStringDict` |
**Geo** | [MultiPoint](docs/v2/Geo/models/MultiPoint.md) | `from foundry.v2.geo.models import MultiPoint` |
**Geo** | [MultiPointDict](docs/v2/Geo/models/MultiPointDict.md) | `from foundry.v2.geo.models import MultiPointDict` |
**Geo** | [MultiPolygon](docs/v2/Geo/models/MultiPolygon.md) | `from foundry.v2.geo.models import MultiPolygon` |
**Geo** | [MultiPolygonDict](docs/v2/Geo/models/MultiPolygonDict.md) | `from foundry.v2.geo.models import MultiPolygonDict` |
**Geo** | [Polygon](docs/v2/Geo/models/Polygon.md) | `from foundry.v2.geo.models import Polygon` |
**Geo** | [PolygonDict](docs/v2/Geo/models/PolygonDict.md) | `from foundry.v2.geo.models import PolygonDict` |
**Geo** | [Position](docs/v2/Geo/models/Position.md) | `from foundry.v2.geo.models import Position` |
**MediaSets** | [BranchName](docs/v2/MediaSets/models/BranchName.md) | `from foundry.v2.media_sets.models import BranchName` |
**MediaSets** | [BranchRid](docs/v2/MediaSets/models/BranchRid.md) | `from foundry.v2.media_sets.models import BranchRid` |
**MediaSets** | [GetMediaItemInfoResponse](docs/v2/MediaSets/models/GetMediaItemInfoResponse.md) | `from foundry.v2.media_sets.models import GetMediaItemInfoResponse` |
**MediaSets** | [GetMediaItemInfoResponseDict](docs/v2/MediaSets/models/GetMediaItemInfoResponseDict.md) | `from foundry.v2.media_sets.models import GetMediaItemInfoResponseDict` |
**MediaSets** | [LogicalTimestamp](docs/v2/MediaSets/models/LogicalTimestamp.md) | `from foundry.v2.media_sets.models import LogicalTimestamp` |
**MediaSets** | [MediaAttribution](docs/v2/MediaSets/models/MediaAttribution.md) | `from foundry.v2.media_sets.models import MediaAttribution` |
**MediaSets** | [MediaAttributionDict](docs/v2/MediaSets/models/MediaAttributionDict.md) | `from foundry.v2.media_sets.models import MediaAttributionDict` |
**MediaSets** | [PutMediaItemResponse](docs/v2/MediaSets/models/PutMediaItemResponse.md) | `from foundry.v2.media_sets.models import PutMediaItemResponse` |
**MediaSets** | [PutMediaItemResponseDict](docs/v2/MediaSets/models/PutMediaItemResponseDict.md) | `from foundry.v2.media_sets.models import PutMediaItemResponseDict` |
**MediaSets** | [TransactionId](docs/v2/MediaSets/models/TransactionId.md) | `from foundry.v2.media_sets.models import TransactionId` |
**Ontologies** | [AbsoluteTimeRange](docs/v2/Ontologies/models/AbsoluteTimeRange.md) | `from foundry.v2.ontologies.models import AbsoluteTimeRange` |
**Ontologies** | [AbsoluteTimeRangeDict](docs/v2/Ontologies/models/AbsoluteTimeRangeDict.md) | `from foundry.v2.ontologies.models import AbsoluteTimeRangeDict` |
**Ontologies** | [ActionParameterArrayType](docs/v2/Ontologies/models/ActionParameterArrayType.md) | `from foundry.v2.ontologies.models import ActionParameterArrayType` |
**Ontologies** | [ActionParameterArrayTypeDict](docs/v2/Ontologies/models/ActionParameterArrayTypeDict.md) | `from foundry.v2.ontologies.models import ActionParameterArrayTypeDict` |
**Ontologies** | [ActionParameterType](docs/v2/Ontologies/models/ActionParameterType.md) | `from foundry.v2.ontologies.models import ActionParameterType` |
**Ontologies** | [ActionParameterTypeDict](docs/v2/Ontologies/models/ActionParameterTypeDict.md) | `from foundry.v2.ontologies.models import ActionParameterTypeDict` |
**Ontologies** | [ActionParameterV2](docs/v2/Ontologies/models/ActionParameterV2.md) | `from foundry.v2.ontologies.models import ActionParameterV2` |
**Ontologies** | [ActionParameterV2Dict](docs/v2/Ontologies/models/ActionParameterV2Dict.md) | `from foundry.v2.ontologies.models import ActionParameterV2Dict` |
**Ontologies** | [ActionResults](docs/v2/Ontologies/models/ActionResults.md) | `from foundry.v2.ontologies.models import ActionResults` |
**Ontologies** | [ActionResultsDict](docs/v2/Ontologies/models/ActionResultsDict.md) | `from foundry.v2.ontologies.models import ActionResultsDict` |
**Ontologies** | [ActionTypeApiName](docs/v2/Ontologies/models/ActionTypeApiName.md) | `from foundry.v2.ontologies.models import ActionTypeApiName` |
**Ontologies** | [ActionTypeRid](docs/v2/Ontologies/models/ActionTypeRid.md) | `from foundry.v2.ontologies.models import ActionTypeRid` |
**Ontologies** | [ActionTypeV2](docs/v2/Ontologies/models/ActionTypeV2.md) | `from foundry.v2.ontologies.models import ActionTypeV2` |
**Ontologies** | [ActionTypeV2Dict](docs/v2/Ontologies/models/ActionTypeV2Dict.md) | `from foundry.v2.ontologies.models import ActionTypeV2Dict` |
**Ontologies** | [ActivePropertyTypeStatus](docs/v2/Ontologies/models/ActivePropertyTypeStatus.md) | `from foundry.v2.ontologies.models import ActivePropertyTypeStatus` |
**Ontologies** | [ActivePropertyTypeStatusDict](docs/v2/Ontologies/models/ActivePropertyTypeStatusDict.md) | `from foundry.v2.ontologies.models import ActivePropertyTypeStatusDict` |
**Ontologies** | [AddLink](docs/v2/Ontologies/models/AddLink.md) | `from foundry.v2.ontologies.models import AddLink` |
**Ontologies** | [AddLinkDict](docs/v2/Ontologies/models/AddLinkDict.md) | `from foundry.v2.ontologies.models import AddLinkDict` |
**Ontologies** | [AddObject](docs/v2/Ontologies/models/AddObject.md) | `from foundry.v2.ontologies.models import AddObject` |
**Ontologies** | [AddObjectDict](docs/v2/Ontologies/models/AddObjectDict.md) | `from foundry.v2.ontologies.models import AddObjectDict` |
**Ontologies** | [AggregateObjectsResponseItemV2](docs/v2/Ontologies/models/AggregateObjectsResponseItemV2.md) | `from foundry.v2.ontologies.models import AggregateObjectsResponseItemV2` |
**Ontologies** | [AggregateObjectsResponseItemV2Dict](docs/v2/Ontologies/models/AggregateObjectsResponseItemV2Dict.md) | `from foundry.v2.ontologies.models import AggregateObjectsResponseItemV2Dict` |
**Ontologies** | [AggregateObjectsResponseV2](docs/v2/Ontologies/models/AggregateObjectsResponseV2.md) | `from foundry.v2.ontologies.models import AggregateObjectsResponseV2` |
**Ontologies** | [AggregateObjectsResponseV2Dict](docs/v2/Ontologies/models/AggregateObjectsResponseV2Dict.md) | `from foundry.v2.ontologies.models import AggregateObjectsResponseV2Dict` |
**Ontologies** | [AggregationAccuracy](docs/v2/Ontologies/models/AggregationAccuracy.md) | `from foundry.v2.ontologies.models import AggregationAccuracy` |
**Ontologies** | [AggregationAccuracyRequest](docs/v2/Ontologies/models/AggregationAccuracyRequest.md) | `from foundry.v2.ontologies.models import AggregationAccuracyRequest` |
**Ontologies** | [AggregationDurationGroupingV2](docs/v2/Ontologies/models/AggregationDurationGroupingV2.md) | `from foundry.v2.ontologies.models import AggregationDurationGroupingV2` |
**Ontologies** | [AggregationDurationGroupingV2Dict](docs/v2/Ontologies/models/AggregationDurationGroupingV2Dict.md) | `from foundry.v2.ontologies.models import AggregationDurationGroupingV2Dict` |
**Ontologies** | [AggregationExactGroupingV2](docs/v2/Ontologies/models/AggregationExactGroupingV2.md) | `from foundry.v2.ontologies.models import AggregationExactGroupingV2` |
**Ontologies** | [AggregationExactGroupingV2Dict](docs/v2/Ontologies/models/AggregationExactGroupingV2Dict.md) | `from foundry.v2.ontologies.models import AggregationExactGroupingV2Dict` |
**Ontologies** | [AggregationFixedWidthGroupingV2](docs/v2/Ontologies/models/AggregationFixedWidthGroupingV2.md) | `from foundry.v2.ontologies.models import AggregationFixedWidthGroupingV2` |
**Ontologies** | [AggregationFixedWidthGroupingV2Dict](docs/v2/Ontologies/models/AggregationFixedWidthGroupingV2Dict.md) | `from foundry.v2.ontologies.models import AggregationFixedWidthGroupingV2Dict` |
**Ontologies** | [AggregationGroupByV2](docs/v2/Ontologies/models/AggregationGroupByV2.md) | `from foundry.v2.ontologies.models import AggregationGroupByV2` |
**Ontologies** | [AggregationGroupByV2Dict](docs/v2/Ontologies/models/AggregationGroupByV2Dict.md) | `from foundry.v2.ontologies.models import AggregationGroupByV2Dict` |
**Ontologies** | [AggregationGroupKeyV2](docs/v2/Ontologies/models/AggregationGroupKeyV2.md) | `from foundry.v2.ontologies.models import AggregationGroupKeyV2` |
**Ontologies** | [AggregationGroupValueV2](docs/v2/Ontologies/models/AggregationGroupValueV2.md) | `from foundry.v2.ontologies.models import AggregationGroupValueV2` |
**Ontologies** | [AggregationMetricName](docs/v2/Ontologies/models/AggregationMetricName.md) | `from foundry.v2.ontologies.models import AggregationMetricName` |
**Ontologies** | [AggregationMetricResultV2](docs/v2/Ontologies/models/AggregationMetricResultV2.md) | `from foundry.v2.ontologies.models import AggregationMetricResultV2` |
**Ontologies** | [AggregationMetricResultV2Dict](docs/v2/Ontologies/models/AggregationMetricResultV2Dict.md) | `from foundry.v2.ontologies.models import AggregationMetricResultV2Dict` |
**Ontologies** | [AggregationRangesGroupingV2](docs/v2/Ontologies/models/AggregationRangesGroupingV2.md) | `from foundry.v2.ontologies.models import AggregationRangesGroupingV2` |
**Ontologies** | [AggregationRangesGroupingV2Dict](docs/v2/Ontologies/models/AggregationRangesGroupingV2Dict.md) | `from foundry.v2.ontologies.models import AggregationRangesGroupingV2Dict` |
**Ontologies** | [AggregationRangeV2](docs/v2/Ontologies/models/AggregationRangeV2.md) | `from foundry.v2.ontologies.models import AggregationRangeV2` |
**Ontologies** | [AggregationRangeV2Dict](docs/v2/Ontologies/models/AggregationRangeV2Dict.md) | `from foundry.v2.ontologies.models import AggregationRangeV2Dict` |
**Ontologies** | [AggregationV2](docs/v2/Ontologies/models/AggregationV2.md) | `from foundry.v2.ontologies.models import AggregationV2` |
**Ontologies** | [AggregationV2Dict](docs/v2/Ontologies/models/AggregationV2Dict.md) | `from foundry.v2.ontologies.models import AggregationV2Dict` |
**Ontologies** | [AndQueryV2](docs/v2/Ontologies/models/AndQueryV2.md) | `from foundry.v2.ontologies.models import AndQueryV2` |
**Ontologies** | [AndQueryV2Dict](docs/v2/Ontologies/models/AndQueryV2Dict.md) | `from foundry.v2.ontologies.models import AndQueryV2Dict` |
**Ontologies** | [ApplyActionMode](docs/v2/Ontologies/models/ApplyActionMode.md) | `from foundry.v2.ontologies.models import ApplyActionMode` |
**Ontologies** | [ApplyActionRequestOptions](docs/v2/Ontologies/models/ApplyActionRequestOptions.md) | `from foundry.v2.ontologies.models import ApplyActionRequestOptions` |
**Ontologies** | [ApplyActionRequestOptionsDict](docs/v2/Ontologies/models/ApplyActionRequestOptionsDict.md) | `from foundry.v2.ontologies.models import ApplyActionRequestOptionsDict` |
**Ontologies** | [ApproximateDistinctAggregationV2](docs/v2/Ontologies/models/ApproximateDistinctAggregationV2.md) | `from foundry.v2.ontologies.models import ApproximateDistinctAggregationV2` |
**Ontologies** | [ApproximateDistinctAggregationV2Dict](docs/v2/Ontologies/models/ApproximateDistinctAggregationV2Dict.md) | `from foundry.v2.ontologies.models import ApproximateDistinctAggregationV2Dict` |
**Ontologies** | [ApproximatePercentileAggregationV2](docs/v2/Ontologies/models/ApproximatePercentileAggregationV2.md) | `from foundry.v2.ontologies.models import ApproximatePercentileAggregationV2` |
**Ontologies** | [ApproximatePercentileAggregationV2Dict](docs/v2/Ontologies/models/ApproximatePercentileAggregationV2Dict.md) | `from foundry.v2.ontologies.models import ApproximatePercentileAggregationV2Dict` |
**Ontologies** | [ArraySizeConstraint](docs/v2/Ontologies/models/ArraySizeConstraint.md) | `from foundry.v2.ontologies.models import ArraySizeConstraint` |
**Ontologies** | [ArraySizeConstraintDict](docs/v2/Ontologies/models/ArraySizeConstraintDict.md) | `from foundry.v2.ontologies.models import ArraySizeConstraintDict` |
**Ontologies** | [ArtifactRepositoryRid](docs/v2/Ontologies/models/ArtifactRepositoryRid.md) | `from foundry.v2.ontologies.models import ArtifactRepositoryRid` |
**Ontologies** | [AttachmentMetadataResponse](docs/v2/Ontologies/models/AttachmentMetadataResponse.md) | `from foundry.v2.ontologies.models import AttachmentMetadataResponse` |
**Ontologies** | [AttachmentMetadataResponseDict](docs/v2/Ontologies/models/AttachmentMetadataResponseDict.md) | `from foundry.v2.ontologies.models import AttachmentMetadataResponseDict` |
**Ontologies** | [AttachmentRid](docs/v2/Ontologies/models/AttachmentRid.md) | `from foundry.v2.ontologies.models import AttachmentRid` |
**Ontologies** | [AttachmentV2](docs/v2/Ontologies/models/AttachmentV2.md) | `from foundry.v2.ontologies.models import AttachmentV2` |
**Ontologies** | [AttachmentV2Dict](docs/v2/Ontologies/models/AttachmentV2Dict.md) | `from foundry.v2.ontologies.models import AttachmentV2Dict` |
**Ontologies** | [AvgAggregationV2](docs/v2/Ontologies/models/AvgAggregationV2.md) | `from foundry.v2.ontologies.models import AvgAggregationV2` |
**Ontologies** | [AvgAggregationV2Dict](docs/v2/Ontologies/models/AvgAggregationV2Dict.md) | `from foundry.v2.ontologies.models import AvgAggregationV2Dict` |
**Ontologies** | [BatchApplyActionRequestItem](docs/v2/Ontologies/models/BatchApplyActionRequestItem.md) | `from foundry.v2.ontologies.models import BatchApplyActionRequestItem` |
**Ontologies** | [BatchApplyActionRequestItemDict](docs/v2/Ontologies/models/BatchApplyActionRequestItemDict.md) | `from foundry.v2.ontologies.models import BatchApplyActionRequestItemDict` |
**Ontologies** | [BatchApplyActionRequestOptions](docs/v2/Ontologies/models/BatchApplyActionRequestOptions.md) | `from foundry.v2.ontologies.models import BatchApplyActionRequestOptions` |
**Ontologies** | [BatchApplyActionRequestOptionsDict](docs/v2/Ontologies/models/BatchApplyActionRequestOptionsDict.md) | `from foundry.v2.ontologies.models import BatchApplyActionRequestOptionsDict` |
**Ontologies** | [BatchApplyActionResponseV2](docs/v2/Ontologies/models/BatchApplyActionResponseV2.md) | `from foundry.v2.ontologies.models import BatchApplyActionResponseV2` |
**Ontologies** | [BatchApplyActionResponseV2Dict](docs/v2/Ontologies/models/BatchApplyActionResponseV2Dict.md) | `from foundry.v2.ontologies.models import BatchApplyActionResponseV2Dict` |
**Ontologies** | [BlueprintIcon](docs/v2/Ontologies/models/BlueprintIcon.md) | `from foundry.v2.ontologies.models import BlueprintIcon` |
**Ontologies** | [BlueprintIconDict](docs/v2/Ontologies/models/BlueprintIconDict.md) | `from foundry.v2.ontologies.models import BlueprintIconDict` |
**Ontologies** | [BoundingBoxValue](docs/v2/Ontologies/models/BoundingBoxValue.md) | `from foundry.v2.ontologies.models import BoundingBoxValue` |
**Ontologies** | [BoundingBoxValueDict](docs/v2/Ontologies/models/BoundingBoxValueDict.md) | `from foundry.v2.ontologies.models import BoundingBoxValueDict` |
**Ontologies** | [CenterPoint](docs/v2/Ontologies/models/CenterPoint.md) | `from foundry.v2.ontologies.models import CenterPoint` |
**Ontologies** | [CenterPointDict](docs/v2/Ontologies/models/CenterPointDict.md) | `from foundry.v2.ontologies.models import CenterPointDict` |
**Ontologies** | [CenterPointTypes](docs/v2/Ontologies/models/CenterPointTypes.md) | `from foundry.v2.ontologies.models import CenterPointTypes` |
**Ontologies** | [CenterPointTypesDict](docs/v2/Ontologies/models/CenterPointTypesDict.md) | `from foundry.v2.ontologies.models import CenterPointTypesDict` |
**Ontologies** | [ContainsAllTermsInOrderPrefixLastTerm](docs/v2/Ontologies/models/ContainsAllTermsInOrderPrefixLastTerm.md) | `from foundry.v2.ontologies.models import ContainsAllTermsInOrderPrefixLastTerm` |
**Ontologies** | [ContainsAllTermsInOrderPrefixLastTermDict](docs/v2/Ontologies/models/ContainsAllTermsInOrderPrefixLastTermDict.md) | `from foundry.v2.ontologies.models import ContainsAllTermsInOrderPrefixLastTermDict` |
**Ontologies** | [ContainsAllTermsInOrderQuery](docs/v2/Ontologies/models/ContainsAllTermsInOrderQuery.md) | `from foundry.v2.ontologies.models import ContainsAllTermsInOrderQuery` |
**Ontologies** | [ContainsAllTermsInOrderQueryDict](docs/v2/Ontologies/models/ContainsAllTermsInOrderQueryDict.md) | `from foundry.v2.ontologies.models import ContainsAllTermsInOrderQueryDict` |
**Ontologies** | [ContainsAllTermsQuery](docs/v2/Ontologies/models/ContainsAllTermsQuery.md) | `from foundry.v2.ontologies.models import ContainsAllTermsQuery` |
**Ontologies** | [ContainsAllTermsQueryDict](docs/v2/Ontologies/models/ContainsAllTermsQueryDict.md) | `from foundry.v2.ontologies.models import ContainsAllTermsQueryDict` |
**Ontologies** | [ContainsAnyTermQuery](docs/v2/Ontologies/models/ContainsAnyTermQuery.md) | `from foundry.v2.ontologies.models import ContainsAnyTermQuery` |
**Ontologies** | [ContainsAnyTermQueryDict](docs/v2/Ontologies/models/ContainsAnyTermQueryDict.md) | `from foundry.v2.ontologies.models import ContainsAnyTermQueryDict` |
**Ontologies** | [ContainsQueryV2](docs/v2/Ontologies/models/ContainsQueryV2.md) | `from foundry.v2.ontologies.models import ContainsQueryV2` |
**Ontologies** | [ContainsQueryV2Dict](docs/v2/Ontologies/models/ContainsQueryV2Dict.md) | `from foundry.v2.ontologies.models import ContainsQueryV2Dict` |
**Ontologies** | [CountAggregationV2](docs/v2/Ontologies/models/CountAggregationV2.md) | `from foundry.v2.ontologies.models import CountAggregationV2` |
**Ontologies** | [CountAggregationV2Dict](docs/v2/Ontologies/models/CountAggregationV2Dict.md) | `from foundry.v2.ontologies.models import CountAggregationV2Dict` |
**Ontologies** | [CountObjectsResponseV2](docs/v2/Ontologies/models/CountObjectsResponseV2.md) | `from foundry.v2.ontologies.models import CountObjectsResponseV2` |
**Ontologies** | [CountObjectsResponseV2Dict](docs/v2/Ontologies/models/CountObjectsResponseV2Dict.md) | `from foundry.v2.ontologies.models import CountObjectsResponseV2Dict` |
**Ontologies** | [CreateInterfaceObjectRule](docs/v2/Ontologies/models/CreateInterfaceObjectRule.md) | `from foundry.v2.ontologies.models import CreateInterfaceObjectRule` |
**Ontologies** | [CreateInterfaceObjectRuleDict](docs/v2/Ontologies/models/CreateInterfaceObjectRuleDict.md) | `from foundry.v2.ontologies.models import CreateInterfaceObjectRuleDict` |
**Ontologies** | [CreateLinkRule](docs/v2/Ontologies/models/CreateLinkRule.md) | `from foundry.v2.ontologies.models import CreateLinkRule` |
**Ontologies** | [CreateLinkRuleDict](docs/v2/Ontologies/models/CreateLinkRuleDict.md) | `from foundry.v2.ontologies.models import CreateLinkRuleDict` |
**Ontologies** | [CreateObjectRule](docs/v2/Ontologies/models/CreateObjectRule.md) | `from foundry.v2.ontologies.models import CreateObjectRule` |
**Ontologies** | [CreateObjectRuleDict](docs/v2/Ontologies/models/CreateObjectRuleDict.md) | `from foundry.v2.ontologies.models import CreateObjectRuleDict` |
**Ontologies** | [CreateTemporaryObjectSetResponseV2](docs/v2/Ontologies/models/CreateTemporaryObjectSetResponseV2.md) | `from foundry.v2.ontologies.models import CreateTemporaryObjectSetResponseV2` |
**Ontologies** | [CreateTemporaryObjectSetResponseV2Dict](docs/v2/Ontologies/models/CreateTemporaryObjectSetResponseV2Dict.md) | `from foundry.v2.ontologies.models import CreateTemporaryObjectSetResponseV2Dict` |
**Ontologies** | [DataValue](docs/v2/Ontologies/models/DataValue.md) | `from foundry.v2.ontologies.models import DataValue` |
**Ontologies** | [DeleteInterfaceObjectRule](docs/v2/Ontologies/models/DeleteInterfaceObjectRule.md) | `from foundry.v2.ontologies.models import DeleteInterfaceObjectRule` |
**Ontologies** | [DeleteInterfaceObjectRuleDict](docs/v2/Ontologies/models/DeleteInterfaceObjectRuleDict.md) | `from foundry.v2.ontologies.models import DeleteInterfaceObjectRuleDict` |
**Ontologies** | [DeleteLinkRule](docs/v2/Ontologies/models/DeleteLinkRule.md) | `from foundry.v2.ontologies.models import DeleteLinkRule` |
**Ontologies** | [DeleteLinkRuleDict](docs/v2/Ontologies/models/DeleteLinkRuleDict.md) | `from foundry.v2.ontologies.models import DeleteLinkRuleDict` |
**Ontologies** | [DeleteObjectRule](docs/v2/Ontologies/models/DeleteObjectRule.md) | `from foundry.v2.ontologies.models import DeleteObjectRule` |
**Ontologies** | [DeleteObjectRuleDict](docs/v2/Ontologies/models/DeleteObjectRuleDict.md) | `from foundry.v2.ontologies.models import DeleteObjectRuleDict` |
**Ontologies** | [DeprecatedPropertyTypeStatus](docs/v2/Ontologies/models/DeprecatedPropertyTypeStatus.md) | `from foundry.v2.ontologies.models import DeprecatedPropertyTypeStatus` |
**Ontologies** | [DeprecatedPropertyTypeStatusDict](docs/v2/Ontologies/models/DeprecatedPropertyTypeStatusDict.md) | `from foundry.v2.ontologies.models import DeprecatedPropertyTypeStatusDict` |
**Ontologies** | [DerivedPropertyApiName](docs/v2/Ontologies/models/DerivedPropertyApiName.md) | `from foundry.v2.ontologies.models import DerivedPropertyApiName` |
**Ontologies** | [DerivedPropertyDefinition](docs/v2/Ontologies/models/DerivedPropertyDefinition.md) | `from foundry.v2.ontologies.models import DerivedPropertyDefinition` |
**Ontologies** | [DerivedPropertyDefinitionDict](docs/v2/Ontologies/models/DerivedPropertyDefinitionDict.md) | `from foundry.v2.ontologies.models import DerivedPropertyDefinitionDict` |
**Ontologies** | [DoesNotIntersectBoundingBoxQuery](docs/v2/Ontologies/models/DoesNotIntersectBoundingBoxQuery.md) | `from foundry.v2.ontologies.models import DoesNotIntersectBoundingBoxQuery` |
**Ontologies** | [DoesNotIntersectBoundingBoxQueryDict](docs/v2/Ontologies/models/DoesNotIntersectBoundingBoxQueryDict.md) | `from foundry.v2.ontologies.models import DoesNotIntersectBoundingBoxQueryDict` |
**Ontologies** | [DoesNotIntersectPolygonQuery](docs/v2/Ontologies/models/DoesNotIntersectPolygonQuery.md) | `from foundry.v2.ontologies.models import DoesNotIntersectPolygonQuery` |
**Ontologies** | [DoesNotIntersectPolygonQueryDict](docs/v2/Ontologies/models/DoesNotIntersectPolygonQueryDict.md) | `from foundry.v2.ontologies.models import DoesNotIntersectPolygonQueryDict` |
**Ontologies** | [DoubleVector](docs/v2/Ontologies/models/DoubleVector.md) | `from foundry.v2.ontologies.models import DoubleVector` |
**Ontologies** | [DoubleVectorDict](docs/v2/Ontologies/models/DoubleVectorDict.md) | `from foundry.v2.ontologies.models import DoubleVectorDict` |
**Ontologies** | [EqualsQueryV2](docs/v2/Ontologies/models/EqualsQueryV2.md) | `from foundry.v2.ontologies.models import EqualsQueryV2` |
**Ontologies** | [EqualsQueryV2Dict](docs/v2/Ontologies/models/EqualsQueryV2Dict.md) | `from foundry.v2.ontologies.models import EqualsQueryV2Dict` |
**Ontologies** | [ExactDistinctAggregationV2](docs/v2/Ontologies/models/ExactDistinctAggregationV2.md) | `from foundry.v2.ontologies.models import ExactDistinctAggregationV2` |
**Ontologies** | [ExactDistinctAggregationV2Dict](docs/v2/Ontologies/models/ExactDistinctAggregationV2Dict.md) | `from foundry.v2.ontologies.models import ExactDistinctAggregationV2Dict` |
**Ontologies** | [ExamplePropertyTypeStatus](docs/v2/Ontologies/models/ExamplePropertyTypeStatus.md) | `from foundry.v2.ontologies.models import ExamplePropertyTypeStatus` |
**Ontologies** | [ExamplePropertyTypeStatusDict](docs/v2/Ontologies/models/ExamplePropertyTypeStatusDict.md) | `from foundry.v2.ontologies.models import ExamplePropertyTypeStatusDict` |
**Ontologies** | [ExecuteQueryResponse](docs/v2/Ontologies/models/ExecuteQueryResponse.md) | `from foundry.v2.ontologies.models import ExecuteQueryResponse` |
**Ontologies** | [ExecuteQueryResponseDict](docs/v2/Ontologies/models/ExecuteQueryResponseDict.md) | `from foundry.v2.ontologies.models import ExecuteQueryResponseDict` |
**Ontologies** | [ExperimentalPropertyTypeStatus](docs/v2/Ontologies/models/ExperimentalPropertyTypeStatus.md) | `from foundry.v2.ontologies.models import ExperimentalPropertyTypeStatus` |
**Ontologies** | [ExperimentalPropertyTypeStatusDict](docs/v2/Ontologies/models/ExperimentalPropertyTypeStatusDict.md) | `from foundry.v2.ontologies.models import ExperimentalPropertyTypeStatusDict` |
**Ontologies** | [FunctionRid](docs/v2/Ontologies/models/FunctionRid.md) | `from foundry.v2.ontologies.models import FunctionRid` |
**Ontologies** | [FunctionVersion](docs/v2/Ontologies/models/FunctionVersion.md) | `from foundry.v2.ontologies.models import FunctionVersion` |
**Ontologies** | [FuzzyV2](docs/v2/Ontologies/models/FuzzyV2.md) | `from foundry.v2.ontologies.models import FuzzyV2` |
**Ontologies** | [GetSelectedPropertyOperation](docs/v2/Ontologies/models/GetSelectedPropertyOperation.md) | `from foundry.v2.ontologies.models import GetSelectedPropertyOperation` |
**Ontologies** | [GetSelectedPropertyOperationDict](docs/v2/Ontologies/models/GetSelectedPropertyOperationDict.md) | `from foundry.v2.ontologies.models import GetSelectedPropertyOperationDict` |
**Ontologies** | [GroupMemberConstraint](docs/v2/Ontologies/models/GroupMemberConstraint.md) | `from foundry.v2.ontologies.models import GroupMemberConstraint` |
**Ontologies** | [GroupMemberConstraintDict](docs/v2/Ontologies/models/GroupMemberConstraintDict.md) | `from foundry.v2.ontologies.models import GroupMemberConstraintDict` |
**Ontologies** | [GteQueryV2](docs/v2/Ontologies/models/GteQueryV2.md) | `from foundry.v2.ontologies.models import GteQueryV2` |
**Ontologies** | [GteQueryV2Dict](docs/v2/Ontologies/models/GteQueryV2Dict.md) | `from foundry.v2.ontologies.models import GteQueryV2Dict` |
**Ontologies** | [GtQueryV2](docs/v2/Ontologies/models/GtQueryV2.md) | `from foundry.v2.ontologies.models import GtQueryV2` |
**Ontologies** | [GtQueryV2Dict](docs/v2/Ontologies/models/GtQueryV2Dict.md) | `from foundry.v2.ontologies.models import GtQueryV2Dict` |
**Ontologies** | [Icon](docs/v2/Ontologies/models/Icon.md) | `from foundry.v2.ontologies.models import Icon` |
**Ontologies** | [IconDict](docs/v2/Ontologies/models/IconDict.md) | `from foundry.v2.ontologies.models import IconDict` |
**Ontologies** | [InQuery](docs/v2/Ontologies/models/InQuery.md) | `from foundry.v2.ontologies.models import InQuery` |
**Ontologies** | [InQueryDict](docs/v2/Ontologies/models/InQueryDict.md) | `from foundry.v2.ontologies.models import InQueryDict` |
**Ontologies** | [InterfaceLinkType](docs/v2/Ontologies/models/InterfaceLinkType.md) | `from foundry.v2.ontologies.models import InterfaceLinkType` |
**Ontologies** | [InterfaceLinkTypeApiName](docs/v2/Ontologies/models/InterfaceLinkTypeApiName.md) | `from foundry.v2.ontologies.models import InterfaceLinkTypeApiName` |
**Ontologies** | [InterfaceLinkTypeCardinality](docs/v2/Ontologies/models/InterfaceLinkTypeCardinality.md) | `from foundry.v2.ontologies.models import InterfaceLinkTypeCardinality` |
**Ontologies** | [InterfaceLinkTypeDict](docs/v2/Ontologies/models/InterfaceLinkTypeDict.md) | `from foundry.v2.ontologies.models import InterfaceLinkTypeDict` |
**Ontologies** | [InterfaceLinkTypeLinkedEntityApiName](docs/v2/Ontologies/models/InterfaceLinkTypeLinkedEntityApiName.md) | `from foundry.v2.ontologies.models import InterfaceLinkTypeLinkedEntityApiName` |
**Ontologies** | [InterfaceLinkTypeLinkedEntityApiNameDict](docs/v2/Ontologies/models/InterfaceLinkTypeLinkedEntityApiNameDict.md) | `from foundry.v2.ontologies.models import InterfaceLinkTypeLinkedEntityApiNameDict` |
**Ontologies** | [InterfaceLinkTypeRid](docs/v2/Ontologies/models/InterfaceLinkTypeRid.md) | `from foundry.v2.ontologies.models import InterfaceLinkTypeRid` |
**Ontologies** | [InterfaceType](docs/v2/Ontologies/models/InterfaceType.md) | `from foundry.v2.ontologies.models import InterfaceType` |
**Ontologies** | [InterfaceTypeApiName](docs/v2/Ontologies/models/InterfaceTypeApiName.md) | `from foundry.v2.ontologies.models import InterfaceTypeApiName` |
**Ontologies** | [InterfaceTypeDict](docs/v2/Ontologies/models/InterfaceTypeDict.md) | `from foundry.v2.ontologies.models import InterfaceTypeDict` |
**Ontologies** | [InterfaceTypeRid](docs/v2/Ontologies/models/InterfaceTypeRid.md) | `from foundry.v2.ontologies.models import InterfaceTypeRid` |
**Ontologies** | [IntersectsBoundingBoxQuery](docs/v2/Ontologies/models/IntersectsBoundingBoxQuery.md) | `from foundry.v2.ontologies.models import IntersectsBoundingBoxQuery` |
**Ontologies** | [IntersectsBoundingBoxQueryDict](docs/v2/Ontologies/models/IntersectsBoundingBoxQueryDict.md) | `from foundry.v2.ontologies.models import IntersectsBoundingBoxQueryDict` |
**Ontologies** | [IntersectsPolygonQuery](docs/v2/Ontologies/models/IntersectsPolygonQuery.md) | `from foundry.v2.ontologies.models import IntersectsPolygonQuery` |
**Ontologies** | [IntersectsPolygonQueryDict](docs/v2/Ontologies/models/IntersectsPolygonQueryDict.md) | `from foundry.v2.ontologies.models import IntersectsPolygonQueryDict` |
**Ontologies** | [IsNullQueryV2](docs/v2/Ontologies/models/IsNullQueryV2.md) | `from foundry.v2.ontologies.models import IsNullQueryV2` |
**Ontologies** | [IsNullQueryV2Dict](docs/v2/Ontologies/models/IsNullQueryV2Dict.md) | `from foundry.v2.ontologies.models import IsNullQueryV2Dict` |
**Ontologies** | [LinkedInterfaceTypeApiName](docs/v2/Ontologies/models/LinkedInterfaceTypeApiName.md) | `from foundry.v2.ontologies.models import LinkedInterfaceTypeApiName` |
**Ontologies** | [LinkedInterfaceTypeApiNameDict](docs/v2/Ontologies/models/LinkedInterfaceTypeApiNameDict.md) | `from foundry.v2.ontologies.models import LinkedInterfaceTypeApiNameDict` |
**Ontologies** | [LinkedObjectTypeApiName](docs/v2/Ontologies/models/LinkedObjectTypeApiName.md) | `from foundry.v2.ontologies.models import LinkedObjectTypeApiName` |
**Ontologies** | [LinkedObjectTypeApiNameDict](docs/v2/Ontologies/models/LinkedObjectTypeApiNameDict.md) | `from foundry.v2.ontologies.models import LinkedObjectTypeApiNameDict` |
**Ontologies** | [LinkSideObject](docs/v2/Ontologies/models/LinkSideObject.md) | `from foundry.v2.ontologies.models import LinkSideObject` |
**Ontologies** | [LinkSideObjectDict](docs/v2/Ontologies/models/LinkSideObjectDict.md) | `from foundry.v2.ontologies.models import LinkSideObjectDict` |
**Ontologies** | [LinkTypeApiName](docs/v2/Ontologies/models/LinkTypeApiName.md) | `from foundry.v2.ontologies.models import LinkTypeApiName` |
**Ontologies** | [LinkTypeRid](docs/v2/Ontologies/models/LinkTypeRid.md) | `from foundry.v2.ontologies.models import LinkTypeRid` |
**Ontologies** | [LinkTypeSideCardinality](docs/v2/Ontologies/models/LinkTypeSideCardinality.md) | `from foundry.v2.ontologies.models import LinkTypeSideCardinality` |
**Ontologies** | [LinkTypeSideV2](docs/v2/Ontologies/models/LinkTypeSideV2.md) | `from foundry.v2.ontologies.models import LinkTypeSideV2` |
**Ontologies** | [LinkTypeSideV2Dict](docs/v2/Ontologies/models/LinkTypeSideV2Dict.md) | `from foundry.v2.ontologies.models import LinkTypeSideV2Dict` |
**Ontologies** | [ListActionTypesResponseV2](docs/v2/Ontologies/models/ListActionTypesResponseV2.md) | `from foundry.v2.ontologies.models import ListActionTypesResponseV2` |
**Ontologies** | [ListActionTypesResponseV2Dict](docs/v2/Ontologies/models/ListActionTypesResponseV2Dict.md) | `from foundry.v2.ontologies.models import ListActionTypesResponseV2Dict` |
**Ontologies** | [ListAttachmentsResponseV2](docs/v2/Ontologies/models/ListAttachmentsResponseV2.md) | `from foundry.v2.ontologies.models import ListAttachmentsResponseV2` |
**Ontologies** | [ListAttachmentsResponseV2Dict](docs/v2/Ontologies/models/ListAttachmentsResponseV2Dict.md) | `from foundry.v2.ontologies.models import ListAttachmentsResponseV2Dict` |
**Ontologies** | [ListInterfaceTypesResponse](docs/v2/Ontologies/models/ListInterfaceTypesResponse.md) | `from foundry.v2.ontologies.models import ListInterfaceTypesResponse` |
**Ontologies** | [ListInterfaceTypesResponseDict](docs/v2/Ontologies/models/ListInterfaceTypesResponseDict.md) | `from foundry.v2.ontologies.models import ListInterfaceTypesResponseDict` |
**Ontologies** | [ListLinkedObjectsResponseV2](docs/v2/Ontologies/models/ListLinkedObjectsResponseV2.md) | `from foundry.v2.ontologies.models import ListLinkedObjectsResponseV2` |
**Ontologies** | [ListLinkedObjectsResponseV2Dict](docs/v2/Ontologies/models/ListLinkedObjectsResponseV2Dict.md) | `from foundry.v2.ontologies.models import ListLinkedObjectsResponseV2Dict` |
**Ontologies** | [ListObjectsResponseV2](docs/v2/Ontologies/models/ListObjectsResponseV2.md) | `from foundry.v2.ontologies.models import ListObjectsResponseV2` |
**Ontologies** | [ListObjectsResponseV2Dict](docs/v2/Ontologies/models/ListObjectsResponseV2Dict.md) | `from foundry.v2.ontologies.models import ListObjectsResponseV2Dict` |
**Ontologies** | [ListObjectTypesV2Response](docs/v2/Ontologies/models/ListObjectTypesV2Response.md) | `from foundry.v2.ontologies.models import ListObjectTypesV2Response` |
**Ontologies** | [ListObjectTypesV2ResponseDict](docs/v2/Ontologies/models/ListObjectTypesV2ResponseDict.md) | `from foundry.v2.ontologies.models import ListObjectTypesV2ResponseDict` |
**Ontologies** | [ListOutgoingLinkTypesResponseV2](docs/v2/Ontologies/models/ListOutgoingLinkTypesResponseV2.md) | `from foundry.v2.ontologies.models import ListOutgoingLinkTypesResponseV2` |
**Ontologies** | [ListOutgoingLinkTypesResponseV2Dict](docs/v2/Ontologies/models/ListOutgoingLinkTypesResponseV2Dict.md) | `from foundry.v2.ontologies.models import ListOutgoingLinkTypesResponseV2Dict` |
**Ontologies** | [ListQueryTypesResponseV2](docs/v2/Ontologies/models/ListQueryTypesResponseV2.md) | `from foundry.v2.ontologies.models import ListQueryTypesResponseV2` |
**Ontologies** | [ListQueryTypesResponseV2Dict](docs/v2/Ontologies/models/ListQueryTypesResponseV2Dict.md) | `from foundry.v2.ontologies.models import ListQueryTypesResponseV2Dict` |
**Ontologies** | [LoadObjectSetResponseV2](docs/v2/Ontologies/models/LoadObjectSetResponseV2.md) | `from foundry.v2.ontologies.models import LoadObjectSetResponseV2` |
**Ontologies** | [LoadObjectSetResponseV2Dict](docs/v2/Ontologies/models/LoadObjectSetResponseV2Dict.md) | `from foundry.v2.ontologies.models import LoadObjectSetResponseV2Dict` |
**Ontologies** | [LogicRule](docs/v2/Ontologies/models/LogicRule.md) | `from foundry.v2.ontologies.models import LogicRule` |
**Ontologies** | [LogicRuleDict](docs/v2/Ontologies/models/LogicRuleDict.md) | `from foundry.v2.ontologies.models import LogicRuleDict` |
**Ontologies** | [LteQueryV2](docs/v2/Ontologies/models/LteQueryV2.md) | `from foundry.v2.ontologies.models import LteQueryV2` |
**Ontologies** | [LteQueryV2Dict](docs/v2/Ontologies/models/LteQueryV2Dict.md) | `from foundry.v2.ontologies.models import LteQueryV2Dict` |
**Ontologies** | [LtQueryV2](docs/v2/Ontologies/models/LtQueryV2.md) | `from foundry.v2.ontologies.models import LtQueryV2` |
**Ontologies** | [LtQueryV2Dict](docs/v2/Ontologies/models/LtQueryV2Dict.md) | `from foundry.v2.ontologies.models import LtQueryV2Dict` |
**Ontologies** | [MaxAggregationV2](docs/v2/Ontologies/models/MaxAggregationV2.md) | `from foundry.v2.ontologies.models import MaxAggregationV2` |
**Ontologies** | [MaxAggregationV2Dict](docs/v2/Ontologies/models/MaxAggregationV2Dict.md) | `from foundry.v2.ontologies.models import MaxAggregationV2Dict` |
**Ontologies** | [MethodObjectSet](docs/v2/Ontologies/models/MethodObjectSet.md) | `from foundry.v2.ontologies.models import MethodObjectSet` |
**Ontologies** | [MethodObjectSetDict](docs/v2/Ontologies/models/MethodObjectSetDict.md) | `from foundry.v2.ontologies.models import MethodObjectSetDict` |
**Ontologies** | [MinAggregationV2](docs/v2/Ontologies/models/MinAggregationV2.md) | `from foundry.v2.ontologies.models import MinAggregationV2` |
**Ontologies** | [MinAggregationV2Dict](docs/v2/Ontologies/models/MinAggregationV2Dict.md) | `from foundry.v2.ontologies.models import MinAggregationV2Dict` |
**Ontologies** | [ModifyInterfaceObjectRule](docs/v2/Ontologies/models/ModifyInterfaceObjectRule.md) | `from foundry.v2.ontologies.models import ModifyInterfaceObjectRule` |
**Ontologies** | [ModifyInterfaceObjectRuleDict](docs/v2/Ontologies/models/ModifyInterfaceObjectRuleDict.md) | `from foundry.v2.ontologies.models import ModifyInterfaceObjectRuleDict` |
**Ontologies** | [ModifyObject](docs/v2/Ontologies/models/ModifyObject.md) | `from foundry.v2.ontologies.models import ModifyObject` |
**Ontologies** | [ModifyObjectDict](docs/v2/Ontologies/models/ModifyObjectDict.md) | `from foundry.v2.ontologies.models import ModifyObjectDict` |
**Ontologies** | [ModifyObjectRule](docs/v2/Ontologies/models/ModifyObjectRule.md) | `from foundry.v2.ontologies.models import ModifyObjectRule` |
**Ontologies** | [ModifyObjectRuleDict](docs/v2/Ontologies/models/ModifyObjectRuleDict.md) | `from foundry.v2.ontologies.models import ModifyObjectRuleDict` |
**Ontologies** | [NearestNeighborsQuery](docs/v2/Ontologies/models/NearestNeighborsQuery.md) | `from foundry.v2.ontologies.models import NearestNeighborsQuery` |
**Ontologies** | [NearestNeighborsQueryDict](docs/v2/Ontologies/models/NearestNeighborsQueryDict.md) | `from foundry.v2.ontologies.models import NearestNeighborsQueryDict` |
**Ontologies** | [NearestNeighborsQueryText](docs/v2/Ontologies/models/NearestNeighborsQueryText.md) | `from foundry.v2.ontologies.models import NearestNeighborsQueryText` |
**Ontologies** | [NearestNeighborsQueryTextDict](docs/v2/Ontologies/models/NearestNeighborsQueryTextDict.md) | `from foundry.v2.ontologies.models import NearestNeighborsQueryTextDict` |
**Ontologies** | [NotQueryV2](docs/v2/Ontologies/models/NotQueryV2.md) | `from foundry.v2.ontologies.models import NotQueryV2` |
**Ontologies** | [NotQueryV2Dict](docs/v2/Ontologies/models/NotQueryV2Dict.md) | `from foundry.v2.ontologies.models import NotQueryV2Dict` |
**Ontologies** | [ObjectEdit](docs/v2/Ontologies/models/ObjectEdit.md) | `from foundry.v2.ontologies.models import ObjectEdit` |
**Ontologies** | [ObjectEditDict](docs/v2/Ontologies/models/ObjectEditDict.md) | `from foundry.v2.ontologies.models import ObjectEditDict` |
**Ontologies** | [ObjectEdits](docs/v2/Ontologies/models/ObjectEdits.md) | `from foundry.v2.ontologies.models import ObjectEdits` |
**Ontologies** | [ObjectEditsDict](docs/v2/Ontologies/models/ObjectEditsDict.md) | `from foundry.v2.ontologies.models import ObjectEditsDict` |
**Ontologies** | [ObjectPropertyType](docs/v2/Ontologies/models/ObjectPropertyType.md) | `from foundry.v2.ontologies.models import ObjectPropertyType` |
**Ontologies** | [ObjectPropertyTypeDict](docs/v2/Ontologies/models/ObjectPropertyTypeDict.md) | `from foundry.v2.ontologies.models import ObjectPropertyTypeDict` |
**Ontologies** | [ObjectPropertyValueConstraint](docs/v2/Ontologies/models/ObjectPropertyValueConstraint.md) | `from foundry.v2.ontologies.models import ObjectPropertyValueConstraint` |
**Ontologies** | [ObjectPropertyValueConstraintDict](docs/v2/Ontologies/models/ObjectPropertyValueConstraintDict.md) | `from foundry.v2.ontologies.models import ObjectPropertyValueConstraintDict` |
**Ontologies** | [ObjectQueryResultConstraint](docs/v2/Ontologies/models/ObjectQueryResultConstraint.md) | `from foundry.v2.ontologies.models import ObjectQueryResultConstraint` |
**Ontologies** | [ObjectQueryResultConstraintDict](docs/v2/Ontologies/models/ObjectQueryResultConstraintDict.md) | `from foundry.v2.ontologies.models import ObjectQueryResultConstraintDict` |
**Ontologies** | [ObjectRid](docs/v2/Ontologies/models/ObjectRid.md) | `from foundry.v2.ontologies.models import ObjectRid` |
**Ontologies** | [ObjectSet](docs/v2/Ontologies/models/ObjectSet.md) | `from foundry.v2.ontologies.models import ObjectSet` |
**Ontologies** | [ObjectSetAsBaseObjectTypesType](docs/v2/Ontologies/models/ObjectSetAsBaseObjectTypesType.md) | `from foundry.v2.ontologies.models import ObjectSetAsBaseObjectTypesType` |
**Ontologies** | [ObjectSetAsBaseObjectTypesTypeDict](docs/v2/Ontologies/models/ObjectSetAsBaseObjectTypesTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetAsBaseObjectTypesTypeDict` |
**Ontologies** | [ObjectSetAsTypeType](docs/v2/Ontologies/models/ObjectSetAsTypeType.md) | `from foundry.v2.ontologies.models import ObjectSetAsTypeType` |
**Ontologies** | [ObjectSetAsTypeTypeDict](docs/v2/Ontologies/models/ObjectSetAsTypeTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetAsTypeTypeDict` |
**Ontologies** | [ObjectSetBaseType](docs/v2/Ontologies/models/ObjectSetBaseType.md) | `from foundry.v2.ontologies.models import ObjectSetBaseType` |
**Ontologies** | [ObjectSetBaseTypeDict](docs/v2/Ontologies/models/ObjectSetBaseTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetBaseTypeDict` |
**Ontologies** | [ObjectSetDict](docs/v2/Ontologies/models/ObjectSetDict.md) | `from foundry.v2.ontologies.models import ObjectSetDict` |
**Ontologies** | [ObjectSetFilterType](docs/v2/Ontologies/models/ObjectSetFilterType.md) | `from foundry.v2.ontologies.models import ObjectSetFilterType` |
**Ontologies** | [ObjectSetFilterTypeDict](docs/v2/Ontologies/models/ObjectSetFilterTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetFilterTypeDict` |
**Ontologies** | [ObjectSetInterfaceBaseType](docs/v2/Ontologies/models/ObjectSetInterfaceBaseType.md) | `from foundry.v2.ontologies.models import ObjectSetInterfaceBaseType` |
**Ontologies** | [ObjectSetInterfaceBaseTypeDict](docs/v2/Ontologies/models/ObjectSetInterfaceBaseTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetInterfaceBaseTypeDict` |
**Ontologies** | [ObjectSetIntersectionType](docs/v2/Ontologies/models/ObjectSetIntersectionType.md) | `from foundry.v2.ontologies.models import ObjectSetIntersectionType` |
**Ontologies** | [ObjectSetIntersectionTypeDict](docs/v2/Ontologies/models/ObjectSetIntersectionTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetIntersectionTypeDict` |
**Ontologies** | [ObjectSetMethodInputType](docs/v2/Ontologies/models/ObjectSetMethodInputType.md) | `from foundry.v2.ontologies.models import ObjectSetMethodInputType` |
**Ontologies** | [ObjectSetMethodInputTypeDict](docs/v2/Ontologies/models/ObjectSetMethodInputTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetMethodInputTypeDict` |
**Ontologies** | [ObjectSetNearestNeighborsType](docs/v2/Ontologies/models/ObjectSetNearestNeighborsType.md) | `from foundry.v2.ontologies.models import ObjectSetNearestNeighborsType` |
**Ontologies** | [ObjectSetNearestNeighborsTypeDict](docs/v2/Ontologies/models/ObjectSetNearestNeighborsTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetNearestNeighborsTypeDict` |
**Ontologies** | [ObjectSetReferenceType](docs/v2/Ontologies/models/ObjectSetReferenceType.md) | `from foundry.v2.ontologies.models import ObjectSetReferenceType` |
**Ontologies** | [ObjectSetReferenceTypeDict](docs/v2/Ontologies/models/ObjectSetReferenceTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetReferenceTypeDict` |
**Ontologies** | [ObjectSetRid](docs/v2/Ontologies/models/ObjectSetRid.md) | `from foundry.v2.ontologies.models import ObjectSetRid` |
**Ontologies** | [ObjectSetSearchAroundType](docs/v2/Ontologies/models/ObjectSetSearchAroundType.md) | `from foundry.v2.ontologies.models import ObjectSetSearchAroundType` |
**Ontologies** | [ObjectSetSearchAroundTypeDict](docs/v2/Ontologies/models/ObjectSetSearchAroundTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetSearchAroundTypeDict` |
**Ontologies** | [ObjectSetStaticType](docs/v2/Ontologies/models/ObjectSetStaticType.md) | `from foundry.v2.ontologies.models import ObjectSetStaticType` |
**Ontologies** | [ObjectSetStaticTypeDict](docs/v2/Ontologies/models/ObjectSetStaticTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetStaticTypeDict` |
**Ontologies** | [ObjectSetSubtractType](docs/v2/Ontologies/models/ObjectSetSubtractType.md) | `from foundry.v2.ontologies.models import ObjectSetSubtractType` |
**Ontologies** | [ObjectSetSubtractTypeDict](docs/v2/Ontologies/models/ObjectSetSubtractTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetSubtractTypeDict` |
**Ontologies** | [ObjectSetUnionType](docs/v2/Ontologies/models/ObjectSetUnionType.md) | `from foundry.v2.ontologies.models import ObjectSetUnionType` |
**Ontologies** | [ObjectSetUnionTypeDict](docs/v2/Ontologies/models/ObjectSetUnionTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetUnionTypeDict` |
**Ontologies** | [ObjectSetWithPropertiesType](docs/v2/Ontologies/models/ObjectSetWithPropertiesType.md) | `from foundry.v2.ontologies.models import ObjectSetWithPropertiesType` |
**Ontologies** | [ObjectSetWithPropertiesTypeDict](docs/v2/Ontologies/models/ObjectSetWithPropertiesTypeDict.md) | `from foundry.v2.ontologies.models import ObjectSetWithPropertiesTypeDict` |
**Ontologies** | [ObjectTypeApiName](docs/v2/Ontologies/models/ObjectTypeApiName.md) | `from foundry.v2.ontologies.models import ObjectTypeApiName` |
**Ontologies** | [ObjectTypeEdits](docs/v2/Ontologies/models/ObjectTypeEdits.md) | `from foundry.v2.ontologies.models import ObjectTypeEdits` |
**Ontologies** | [ObjectTypeEditsDict](docs/v2/Ontologies/models/ObjectTypeEditsDict.md) | `from foundry.v2.ontologies.models import ObjectTypeEditsDict` |
**Ontologies** | [ObjectTypeFullMetadata](docs/v2/Ontologies/models/ObjectTypeFullMetadata.md) | `from foundry.v2.ontologies.models import ObjectTypeFullMetadata` |
**Ontologies** | [ObjectTypeFullMetadataDict](docs/v2/Ontologies/models/ObjectTypeFullMetadataDict.md) | `from foundry.v2.ontologies.models import ObjectTypeFullMetadataDict` |
**Ontologies** | [ObjectTypeId](docs/v2/Ontologies/models/ObjectTypeId.md) | `from foundry.v2.ontologies.models import ObjectTypeId` |
**Ontologies** | [ObjectTypeInterfaceImplementation](docs/v2/Ontologies/models/ObjectTypeInterfaceImplementation.md) | `from foundry.v2.ontologies.models import ObjectTypeInterfaceImplementation` |
**Ontologies** | [ObjectTypeInterfaceImplementationDict](docs/v2/Ontologies/models/ObjectTypeInterfaceImplementationDict.md) | `from foundry.v2.ontologies.models import ObjectTypeInterfaceImplementationDict` |
**Ontologies** | [ObjectTypeRid](docs/v2/Ontologies/models/ObjectTypeRid.md) | `from foundry.v2.ontologies.models import ObjectTypeRid` |
**Ontologies** | [ObjectTypeV2](docs/v2/Ontologies/models/ObjectTypeV2.md) | `from foundry.v2.ontologies.models import ObjectTypeV2` |
**Ontologies** | [ObjectTypeV2Dict](docs/v2/Ontologies/models/ObjectTypeV2Dict.md) | `from foundry.v2.ontologies.models import ObjectTypeV2Dict` |
**Ontologies** | [ObjectTypeVisibility](docs/v2/Ontologies/models/ObjectTypeVisibility.md) | `from foundry.v2.ontologies.models import ObjectTypeVisibility` |
**Ontologies** | [OneOfConstraint](docs/v2/Ontologies/models/OneOfConstraint.md) | `from foundry.v2.ontologies.models import OneOfConstraint` |
**Ontologies** | [OneOfConstraintDict](docs/v2/Ontologies/models/OneOfConstraintDict.md) | `from foundry.v2.ontologies.models import OneOfConstraintDict` |
**Ontologies** | [OntologyApiName](docs/v2/Ontologies/models/OntologyApiName.md) | `from foundry.v2.ontologies.models import OntologyApiName` |
**Ontologies** | [OntologyArrayType](docs/v2/Ontologies/models/OntologyArrayType.md) | `from foundry.v2.ontologies.models import OntologyArrayType` |
**Ontologies** | [OntologyArrayTypeDict](docs/v2/Ontologies/models/OntologyArrayTypeDict.md) | `from foundry.v2.ontologies.models import OntologyArrayTypeDict` |
**Ontologies** | [OntologyDataType](docs/v2/Ontologies/models/OntologyDataType.md) | `from foundry.v2.ontologies.models import OntologyDataType` |
**Ontologies** | [OntologyDataTypeDict](docs/v2/Ontologies/models/OntologyDataTypeDict.md) | `from foundry.v2.ontologies.models import OntologyDataTypeDict` |
**Ontologies** | [OntologyFullMetadata](docs/v2/Ontologies/models/OntologyFullMetadata.md) | `from foundry.v2.ontologies.models import OntologyFullMetadata` |
**Ontologies** | [OntologyFullMetadataDict](docs/v2/Ontologies/models/OntologyFullMetadataDict.md) | `from foundry.v2.ontologies.models import OntologyFullMetadataDict` |
**Ontologies** | [OntologyIdentifier](docs/v2/Ontologies/models/OntologyIdentifier.md) | `from foundry.v2.ontologies.models import OntologyIdentifier` |
**Ontologies** | [OntologyInterfaceObjectType](docs/v2/Ontologies/models/OntologyInterfaceObjectType.md) | `from foundry.v2.ontologies.models import OntologyInterfaceObjectType` |
**Ontologies** | [OntologyInterfaceObjectTypeDict](docs/v2/Ontologies/models/OntologyInterfaceObjectTypeDict.md) | `from foundry.v2.ontologies.models import OntologyInterfaceObjectTypeDict` |
**Ontologies** | [OntologyMapType](docs/v2/Ontologies/models/OntologyMapType.md) | `from foundry.v2.ontologies.models import OntologyMapType` |
**Ontologies** | [OntologyMapTypeDict](docs/v2/Ontologies/models/OntologyMapTypeDict.md) | `from foundry.v2.ontologies.models import OntologyMapTypeDict` |
**Ontologies** | [OntologyObjectArrayType](docs/v2/Ontologies/models/OntologyObjectArrayType.md) | `from foundry.v2.ontologies.models import OntologyObjectArrayType` |
**Ontologies** | [OntologyObjectArrayTypeDict](docs/v2/Ontologies/models/OntologyObjectArrayTypeDict.md) | `from foundry.v2.ontologies.models import OntologyObjectArrayTypeDict` |
**Ontologies** | [OntologyObjectSetType](docs/v2/Ontologies/models/OntologyObjectSetType.md) | `from foundry.v2.ontologies.models import OntologyObjectSetType` |
**Ontologies** | [OntologyObjectSetTypeDict](docs/v2/Ontologies/models/OntologyObjectSetTypeDict.md) | `from foundry.v2.ontologies.models import OntologyObjectSetTypeDict` |
**Ontologies** | [OntologyObjectType](docs/v2/Ontologies/models/OntologyObjectType.md) | `from foundry.v2.ontologies.models import OntologyObjectType` |
**Ontologies** | [OntologyObjectTypeDict](docs/v2/Ontologies/models/OntologyObjectTypeDict.md) | `from foundry.v2.ontologies.models import OntologyObjectTypeDict` |
**Ontologies** | [OntologyObjectTypeReferenceType](docs/v2/Ontologies/models/OntologyObjectTypeReferenceType.md) | `from foundry.v2.ontologies.models import OntologyObjectTypeReferenceType` |
**Ontologies** | [OntologyObjectTypeReferenceTypeDict](docs/v2/Ontologies/models/OntologyObjectTypeReferenceTypeDict.md) | `from foundry.v2.ontologies.models import OntologyObjectTypeReferenceTypeDict` |
**Ontologies** | [OntologyObjectV2](docs/v2/Ontologies/models/OntologyObjectV2.md) | `from foundry.v2.ontologies.models import OntologyObjectV2` |
**Ontologies** | [OntologyRid](docs/v2/Ontologies/models/OntologyRid.md) | `from foundry.v2.ontologies.models import OntologyRid` |
**Ontologies** | [OntologySetType](docs/v2/Ontologies/models/OntologySetType.md) | `from foundry.v2.ontologies.models import OntologySetType` |
**Ontologies** | [OntologySetTypeDict](docs/v2/Ontologies/models/OntologySetTypeDict.md) | `from foundry.v2.ontologies.models import OntologySetTypeDict` |
**Ontologies** | [OntologyStructField](docs/v2/Ontologies/models/OntologyStructField.md) | `from foundry.v2.ontologies.models import OntologyStructField` |
**Ontologies** | [OntologyStructFieldDict](docs/v2/Ontologies/models/OntologyStructFieldDict.md) | `from foundry.v2.ontologies.models import OntologyStructFieldDict` |
**Ontologies** | [OntologyStructType](docs/v2/Ontologies/models/OntologyStructType.md) | `from foundry.v2.ontologies.models import OntologyStructType` |
**Ontologies** | [OntologyStructTypeDict](docs/v2/Ontologies/models/OntologyStructTypeDict.md) | `from foundry.v2.ontologies.models import OntologyStructTypeDict` |
**Ontologies** | [OntologyV2](docs/v2/Ontologies/models/OntologyV2.md) | `from foundry.v2.ontologies.models import OntologyV2` |
**Ontologies** | [OntologyV2Dict](docs/v2/Ontologies/models/OntologyV2Dict.md) | `from foundry.v2.ontologies.models import OntologyV2Dict` |
**Ontologies** | [OrderBy](docs/v2/Ontologies/models/OrderBy.md) | `from foundry.v2.ontologies.models import OrderBy` |
**Ontologies** | [OrderByDirection](docs/v2/Ontologies/models/OrderByDirection.md) | `from foundry.v2.ontologies.models import OrderByDirection` |
**Ontologies** | [OrQueryV2](docs/v2/Ontologies/models/OrQueryV2.md) | `from foundry.v2.ontologies.models import OrQueryV2` |
**Ontologies** | [OrQueryV2Dict](docs/v2/Ontologies/models/OrQueryV2Dict.md) | `from foundry.v2.ontologies.models import OrQueryV2Dict` |
**Ontologies** | [ParameterEvaluatedConstraint](docs/v2/Ontologies/models/ParameterEvaluatedConstraint.md) | `from foundry.v2.ontologies.models import ParameterEvaluatedConstraint` |
**Ontologies** | [ParameterEvaluatedConstraintDict](docs/v2/Ontologies/models/ParameterEvaluatedConstraintDict.md) | `from foundry.v2.ontologies.models import ParameterEvaluatedConstraintDict` |
**Ontologies** | [ParameterEvaluationResult](docs/v2/Ontologies/models/ParameterEvaluationResult.md) | `from foundry.v2.ontologies.models import ParameterEvaluationResult` |
**Ontologies** | [ParameterEvaluationResultDict](docs/v2/Ontologies/models/ParameterEvaluationResultDict.md) | `from foundry.v2.ontologies.models import ParameterEvaluationResultDict` |
**Ontologies** | [ParameterId](docs/v2/Ontologies/models/ParameterId.md) | `from foundry.v2.ontologies.models import ParameterId` |
**Ontologies** | [ParameterOption](docs/v2/Ontologies/models/ParameterOption.md) | `from foundry.v2.ontologies.models import ParameterOption` |
**Ontologies** | [ParameterOptionDict](docs/v2/Ontologies/models/ParameterOptionDict.md) | `from foundry.v2.ontologies.models import ParameterOptionDict` |
**Ontologies** | [PolygonValue](docs/v2/Ontologies/models/PolygonValue.md) | `from foundry.v2.ontologies.models import PolygonValue` |
**Ontologies** | [PolygonValueDict](docs/v2/Ontologies/models/PolygonValueDict.md) | `from foundry.v2.ontologies.models import PolygonValueDict` |
**Ontologies** | [PropertyApiName](docs/v2/Ontologies/models/PropertyApiName.md) | `from foundry.v2.ontologies.models import PropertyApiName` |
**Ontologies** | [PropertyApiNameSelector](docs/v2/Ontologies/models/PropertyApiNameSelector.md) | `from foundry.v2.ontologies.models import PropertyApiNameSelector` |
**Ontologies** | [PropertyApiNameSelectorDict](docs/v2/Ontologies/models/PropertyApiNameSelectorDict.md) | `from foundry.v2.ontologies.models import PropertyApiNameSelectorDict` |
**Ontologies** | [PropertyIdentifier](docs/v2/Ontologies/models/PropertyIdentifier.md) | `from foundry.v2.ontologies.models import PropertyIdentifier` |
**Ontologies** | [PropertyIdentifierDict](docs/v2/Ontologies/models/PropertyIdentifierDict.md) | `from foundry.v2.ontologies.models import PropertyIdentifierDict` |
**Ontologies** | [PropertyTypeRid](docs/v2/Ontologies/models/PropertyTypeRid.md) | `from foundry.v2.ontologies.models import PropertyTypeRid` |
**Ontologies** | [PropertyTypeStatus](docs/v2/Ontologies/models/PropertyTypeStatus.md) | `from foundry.v2.ontologies.models import PropertyTypeStatus` |
**Ontologies** | [PropertyTypeStatusDict](docs/v2/Ontologies/models/PropertyTypeStatusDict.md) | `from foundry.v2.ontologies.models import PropertyTypeStatusDict` |
**Ontologies** | [PropertyTypeVisibility](docs/v2/Ontologies/models/PropertyTypeVisibility.md) | `from foundry.v2.ontologies.models import PropertyTypeVisibility` |
**Ontologies** | [PropertyV2](docs/v2/Ontologies/models/PropertyV2.md) | `from foundry.v2.ontologies.models import PropertyV2` |
**Ontologies** | [PropertyV2Dict](docs/v2/Ontologies/models/PropertyV2Dict.md) | `from foundry.v2.ontologies.models import PropertyV2Dict` |
**Ontologies** | [PropertyValue](docs/v2/Ontologies/models/PropertyValue.md) | `from foundry.v2.ontologies.models import PropertyValue` |
**Ontologies** | [PropertyValueEscapedString](docs/v2/Ontologies/models/PropertyValueEscapedString.md) | `from foundry.v2.ontologies.models import PropertyValueEscapedString` |
**Ontologies** | [QueryAggregationKeyType](docs/v2/Ontologies/models/QueryAggregationKeyType.md) | `from foundry.v2.ontologies.models import QueryAggregationKeyType` |
**Ontologies** | [QueryAggregationKeyTypeDict](docs/v2/Ontologies/models/QueryAggregationKeyTypeDict.md) | `from foundry.v2.ontologies.models import QueryAggregationKeyTypeDict` |
**Ontologies** | [QueryAggregationRangeSubType](docs/v2/Ontologies/models/QueryAggregationRangeSubType.md) | `from foundry.v2.ontologies.models import QueryAggregationRangeSubType` |
**Ontologies** | [QueryAggregationRangeSubTypeDict](docs/v2/Ontologies/models/QueryAggregationRangeSubTypeDict.md) | `from foundry.v2.ontologies.models import QueryAggregationRangeSubTypeDict` |
**Ontologies** | [QueryAggregationRangeType](docs/v2/Ontologies/models/QueryAggregationRangeType.md) | `from foundry.v2.ontologies.models import QueryAggregationRangeType` |
**Ontologies** | [QueryAggregationRangeTypeDict](docs/v2/Ontologies/models/QueryAggregationRangeTypeDict.md) | `from foundry.v2.ontologies.models import QueryAggregationRangeTypeDict` |
**Ontologies** | [QueryAggregationValueType](docs/v2/Ontologies/models/QueryAggregationValueType.md) | `from foundry.v2.ontologies.models import QueryAggregationValueType` |
**Ontologies** | [QueryAggregationValueTypeDict](docs/v2/Ontologies/models/QueryAggregationValueTypeDict.md) | `from foundry.v2.ontologies.models import QueryAggregationValueTypeDict` |
**Ontologies** | [QueryApiName](docs/v2/Ontologies/models/QueryApiName.md) | `from foundry.v2.ontologies.models import QueryApiName` |
**Ontologies** | [QueryArrayType](docs/v2/Ontologies/models/QueryArrayType.md) | `from foundry.v2.ontologies.models import QueryArrayType` |
**Ontologies** | [QueryArrayTypeDict](docs/v2/Ontologies/models/QueryArrayTypeDict.md) | `from foundry.v2.ontologies.models import QueryArrayTypeDict` |
**Ontologies** | [QueryDataType](docs/v2/Ontologies/models/QueryDataType.md) | `from foundry.v2.ontologies.models import QueryDataType` |
**Ontologies** | [QueryDataTypeDict](docs/v2/Ontologies/models/QueryDataTypeDict.md) | `from foundry.v2.ontologies.models import QueryDataTypeDict` |
**Ontologies** | [QueryParameterV2](docs/v2/Ontologies/models/QueryParameterV2.md) | `from foundry.v2.ontologies.models import QueryParameterV2` |
**Ontologies** | [QueryParameterV2Dict](docs/v2/Ontologies/models/QueryParameterV2Dict.md) | `from foundry.v2.ontologies.models import QueryParameterV2Dict` |
**Ontologies** | [QuerySetType](docs/v2/Ontologies/models/QuerySetType.md) | `from foundry.v2.ontologies.models import QuerySetType` |
**Ontologies** | [QuerySetTypeDict](docs/v2/Ontologies/models/QuerySetTypeDict.md) | `from foundry.v2.ontologies.models import QuerySetTypeDict` |
**Ontologies** | [QueryStructField](docs/v2/Ontologies/models/QueryStructField.md) | `from foundry.v2.ontologies.models import QueryStructField` |
**Ontologies** | [QueryStructFieldDict](docs/v2/Ontologies/models/QueryStructFieldDict.md) | `from foundry.v2.ontologies.models import QueryStructFieldDict` |
**Ontologies** | [QueryStructType](docs/v2/Ontologies/models/QueryStructType.md) | `from foundry.v2.ontologies.models import QueryStructType` |
**Ontologies** | [QueryStructTypeDict](docs/v2/Ontologies/models/QueryStructTypeDict.md) | `from foundry.v2.ontologies.models import QueryStructTypeDict` |
**Ontologies** | [QueryTypeV2](docs/v2/Ontologies/models/QueryTypeV2.md) | `from foundry.v2.ontologies.models import QueryTypeV2` |
**Ontologies** | [QueryTypeV2Dict](docs/v2/Ontologies/models/QueryTypeV2Dict.md) | `from foundry.v2.ontologies.models import QueryTypeV2Dict` |
**Ontologies** | [QueryUnionType](docs/v2/Ontologies/models/QueryUnionType.md) | `from foundry.v2.ontologies.models import QueryUnionType` |
**Ontologies** | [QueryUnionTypeDict](docs/v2/Ontologies/models/QueryUnionTypeDict.md) | `from foundry.v2.ontologies.models import QueryUnionTypeDict` |
**Ontologies** | [RangeConstraint](docs/v2/Ontologies/models/RangeConstraint.md) | `from foundry.v2.ontologies.models import RangeConstraint` |
**Ontologies** | [RangeConstraintDict](docs/v2/Ontologies/models/RangeConstraintDict.md) | `from foundry.v2.ontologies.models import RangeConstraintDict` |
**Ontologies** | [RelativeTime](docs/v2/Ontologies/models/RelativeTime.md) | `from foundry.v2.ontologies.models import RelativeTime` |
**Ontologies** | [RelativeTimeDict](docs/v2/Ontologies/models/RelativeTimeDict.md) | `from foundry.v2.ontologies.models import RelativeTimeDict` |
**Ontologies** | [RelativeTimeRange](docs/v2/Ontologies/models/RelativeTimeRange.md) | `from foundry.v2.ontologies.models import RelativeTimeRange` |
**Ontologies** | [RelativeTimeRangeDict](docs/v2/Ontologies/models/RelativeTimeRangeDict.md) | `from foundry.v2.ontologies.models import RelativeTimeRangeDict` |
**Ontologies** | [RelativeTimeRelation](docs/v2/Ontologies/models/RelativeTimeRelation.md) | `from foundry.v2.ontologies.models import RelativeTimeRelation` |
**Ontologies** | [RelativeTimeSeriesTimeUnit](docs/v2/Ontologies/models/RelativeTimeSeriesTimeUnit.md) | `from foundry.v2.ontologies.models import RelativeTimeSeriesTimeUnit` |
**Ontologies** | [ReturnEditsMode](docs/v2/Ontologies/models/ReturnEditsMode.md) | `from foundry.v2.ontologies.models import ReturnEditsMode` |
**Ontologies** | [SdkPackageName](docs/v2/Ontologies/models/SdkPackageName.md) | `from foundry.v2.ontologies.models import SdkPackageName` |
**Ontologies** | [SearchJsonQueryV2](docs/v2/Ontologies/models/SearchJsonQueryV2.md) | `from foundry.v2.ontologies.models import SearchJsonQueryV2` |
**Ontologies** | [SearchJsonQueryV2Dict](docs/v2/Ontologies/models/SearchJsonQueryV2Dict.md) | `from foundry.v2.ontologies.models import SearchJsonQueryV2Dict` |
**Ontologies** | [SearchObjectsResponseV2](docs/v2/Ontologies/models/SearchObjectsResponseV2.md) | `from foundry.v2.ontologies.models import SearchObjectsResponseV2` |
**Ontologies** | [SearchObjectsResponseV2Dict](docs/v2/Ontologies/models/SearchObjectsResponseV2Dict.md) | `from foundry.v2.ontologies.models import SearchObjectsResponseV2Dict` |
**Ontologies** | [SearchOrderByType](docs/v2/Ontologies/models/SearchOrderByType.md) | `from foundry.v2.ontologies.models import SearchOrderByType` |
**Ontologies** | [SearchOrderByV2](docs/v2/Ontologies/models/SearchOrderByV2.md) | `from foundry.v2.ontologies.models import SearchOrderByV2` |
**Ontologies** | [SearchOrderByV2Dict](docs/v2/Ontologies/models/SearchOrderByV2Dict.md) | `from foundry.v2.ontologies.models import SearchOrderByV2Dict` |
**Ontologies** | [SearchOrderingV2](docs/v2/Ontologies/models/SearchOrderingV2.md) | `from foundry.v2.ontologies.models import SearchOrderingV2` |
**Ontologies** | [SearchOrderingV2Dict](docs/v2/Ontologies/models/SearchOrderingV2Dict.md) | `from foundry.v2.ontologies.models import SearchOrderingV2Dict` |
**Ontologies** | [SelectedPropertyApiName](docs/v2/Ontologies/models/SelectedPropertyApiName.md) | `from foundry.v2.ontologies.models import SelectedPropertyApiName` |
**Ontologies** | [SelectedPropertyApproximateDistinctAggregation](docs/v2/Ontologies/models/SelectedPropertyApproximateDistinctAggregation.md) | `from foundry.v2.ontologies.models import SelectedPropertyApproximateDistinctAggregation` |
**Ontologies** | [SelectedPropertyApproximateDistinctAggregationDict](docs/v2/Ontologies/models/SelectedPropertyApproximateDistinctAggregationDict.md) | `from foundry.v2.ontologies.models import SelectedPropertyApproximateDistinctAggregationDict` |
**Ontologies** | [SelectedPropertyApproximatePercentileAggregation](docs/v2/Ontologies/models/SelectedPropertyApproximatePercentileAggregation.md) | `from foundry.v2.ontologies.models import SelectedPropertyApproximatePercentileAggregation` |
**Ontologies** | [SelectedPropertyApproximatePercentileAggregationDict](docs/v2/Ontologies/models/SelectedPropertyApproximatePercentileAggregationDict.md) | `from foundry.v2.ontologies.models import SelectedPropertyApproximatePercentileAggregationDict` |
**Ontologies** | [SelectedPropertyAvgAggregation](docs/v2/Ontologies/models/SelectedPropertyAvgAggregation.md) | `from foundry.v2.ontologies.models import SelectedPropertyAvgAggregation` |
**Ontologies** | [SelectedPropertyAvgAggregationDict](docs/v2/Ontologies/models/SelectedPropertyAvgAggregationDict.md) | `from foundry.v2.ontologies.models import SelectedPropertyAvgAggregationDict` |
**Ontologies** | [SelectedPropertyCollectListAggregation](docs/v2/Ontologies/models/SelectedPropertyCollectListAggregation.md) | `from foundry.v2.ontologies.models import SelectedPropertyCollectListAggregation` |
**Ontologies** | [SelectedPropertyCollectListAggregationDict](docs/v2/Ontologies/models/SelectedPropertyCollectListAggregationDict.md) | `from foundry.v2.ontologies.models import SelectedPropertyCollectListAggregationDict` |
**Ontologies** | [SelectedPropertyCollectSetAggregation](docs/v2/Ontologies/models/SelectedPropertyCollectSetAggregation.md) | `from foundry.v2.ontologies.models import SelectedPropertyCollectSetAggregation` |
**Ontologies** | [SelectedPropertyCollectSetAggregationDict](docs/v2/Ontologies/models/SelectedPropertyCollectSetAggregationDict.md) | `from foundry.v2.ontologies.models import SelectedPropertyCollectSetAggregationDict` |
**Ontologies** | [SelectedPropertyCountAggregation](docs/v2/Ontologies/models/SelectedPropertyCountAggregation.md) | `from foundry.v2.ontologies.models import SelectedPropertyCountAggregation` |
**Ontologies** | [SelectedPropertyCountAggregationDict](docs/v2/Ontologies/models/SelectedPropertyCountAggregationDict.md) | `from foundry.v2.ontologies.models import SelectedPropertyCountAggregationDict` |
**Ontologies** | [SelectedPropertyDefinition](docs/v2/Ontologies/models/SelectedPropertyDefinition.md) | `from foundry.v2.ontologies.models import SelectedPropertyDefinition` |
**Ontologies** | [SelectedPropertyDefinitionDict](docs/v2/Ontologies/models/SelectedPropertyDefinitionDict.md) | `from foundry.v2.ontologies.models import SelectedPropertyDefinitionDict` |
**Ontologies** | [SelectedPropertyExactDistinctAggregation](docs/v2/Ontologies/models/SelectedPropertyExactDistinctAggregation.md) | `from foundry.v2.ontologies.models import SelectedPropertyExactDistinctAggregation` |
**Ontologies** | [SelectedPropertyExactDistinctAggregationDict](docs/v2/Ontologies/models/SelectedPropertyExactDistinctAggregationDict.md) | `from foundry.v2.ontologies.models import SelectedPropertyExactDistinctAggregationDict` |
**Ontologies** | [SelectedPropertyMaxAggregation](docs/v2/Ontologies/models/SelectedPropertyMaxAggregation.md) | `from foundry.v2.ontologies.models import SelectedPropertyMaxAggregation` |
**Ontologies** | [SelectedPropertyMaxAggregationDict](docs/v2/Ontologies/models/SelectedPropertyMaxAggregationDict.md) | `from foundry.v2.ontologies.models import SelectedPropertyMaxAggregationDict` |
**Ontologies** | [SelectedPropertyMinAggregation](docs/v2/Ontologies/models/SelectedPropertyMinAggregation.md) | `from foundry.v2.ontologies.models import SelectedPropertyMinAggregation` |
**Ontologies** | [SelectedPropertyMinAggregationDict](docs/v2/Ontologies/models/SelectedPropertyMinAggregationDict.md) | `from foundry.v2.ontologies.models import SelectedPropertyMinAggregationDict` |
**Ontologies** | [SelectedPropertyOperation](docs/v2/Ontologies/models/SelectedPropertyOperation.md) | `from foundry.v2.ontologies.models import SelectedPropertyOperation` |
**Ontologies** | [SelectedPropertyOperationDict](docs/v2/Ontologies/models/SelectedPropertyOperationDict.md) | `from foundry.v2.ontologies.models import SelectedPropertyOperationDict` |
**Ontologies** | [SelectedPropertySumAggregation](docs/v2/Ontologies/models/SelectedPropertySumAggregation.md) | `from foundry.v2.ontologies.models import SelectedPropertySumAggregation` |
**Ontologies** | [SelectedPropertySumAggregationDict](docs/v2/Ontologies/models/SelectedPropertySumAggregationDict.md) | `from foundry.v2.ontologies.models import SelectedPropertySumAggregationDict` |
**Ontologies** | [SharedPropertyType](docs/v2/Ontologies/models/SharedPropertyType.md) | `from foundry.v2.ontologies.models import SharedPropertyType` |
**Ontologies** | [SharedPropertyTypeApiName](docs/v2/Ontologies/models/SharedPropertyTypeApiName.md) | `from foundry.v2.ontologies.models import SharedPropertyTypeApiName` |
**Ontologies** | [SharedPropertyTypeDict](docs/v2/Ontologies/models/SharedPropertyTypeDict.md) | `from foundry.v2.ontologies.models import SharedPropertyTypeDict` |
**Ontologies** | [SharedPropertyTypeRid](docs/v2/Ontologies/models/SharedPropertyTypeRid.md) | `from foundry.v2.ontologies.models import SharedPropertyTypeRid` |
**Ontologies** | [StartsWithQuery](docs/v2/Ontologies/models/StartsWithQuery.md) | `from foundry.v2.ontologies.models import StartsWithQuery` |
**Ontologies** | [StartsWithQueryDict](docs/v2/Ontologies/models/StartsWithQueryDict.md) | `from foundry.v2.ontologies.models import StartsWithQueryDict` |
**Ontologies** | [StreamingOutputFormat](docs/v2/Ontologies/models/StreamingOutputFormat.md) | `from foundry.v2.ontologies.models import StreamingOutputFormat` |
**Ontologies** | [StringLengthConstraint](docs/v2/Ontologies/models/StringLengthConstraint.md) | `from foundry.v2.ontologies.models import StringLengthConstraint` |
**Ontologies** | [StringLengthConstraintDict](docs/v2/Ontologies/models/StringLengthConstraintDict.md) | `from foundry.v2.ontologies.models import StringLengthConstraintDict` |
**Ontologies** | [StringRegexMatchConstraint](docs/v2/Ontologies/models/StringRegexMatchConstraint.md) | `from foundry.v2.ontologies.models import StringRegexMatchConstraint` |
**Ontologies** | [StringRegexMatchConstraintDict](docs/v2/Ontologies/models/StringRegexMatchConstraintDict.md) | `from foundry.v2.ontologies.models import StringRegexMatchConstraintDict` |
**Ontologies** | [StructFieldApiName](docs/v2/Ontologies/models/StructFieldApiName.md) | `from foundry.v2.ontologies.models import StructFieldApiName` |
**Ontologies** | [StructFieldSelector](docs/v2/Ontologies/models/StructFieldSelector.md) | `from foundry.v2.ontologies.models import StructFieldSelector` |
**Ontologies** | [StructFieldSelectorDict](docs/v2/Ontologies/models/StructFieldSelectorDict.md) | `from foundry.v2.ontologies.models import StructFieldSelectorDict` |
**Ontologies** | [StructFieldType](docs/v2/Ontologies/models/StructFieldType.md) | `from foundry.v2.ontologies.models import StructFieldType` |
**Ontologies** | [StructFieldTypeDict](docs/v2/Ontologies/models/StructFieldTypeDict.md) | `from foundry.v2.ontologies.models import StructFieldTypeDict` |
**Ontologies** | [StructType](docs/v2/Ontologies/models/StructType.md) | `from foundry.v2.ontologies.models import StructType` |
**Ontologies** | [StructTypeDict](docs/v2/Ontologies/models/StructTypeDict.md) | `from foundry.v2.ontologies.models import StructTypeDict` |
**Ontologies** | [SubmissionCriteriaEvaluation](docs/v2/Ontologies/models/SubmissionCriteriaEvaluation.md) | `from foundry.v2.ontologies.models import SubmissionCriteriaEvaluation` |
**Ontologies** | [SubmissionCriteriaEvaluationDict](docs/v2/Ontologies/models/SubmissionCriteriaEvaluationDict.md) | `from foundry.v2.ontologies.models import SubmissionCriteriaEvaluationDict` |
**Ontologies** | [SumAggregationV2](docs/v2/Ontologies/models/SumAggregationV2.md) | `from foundry.v2.ontologies.models import SumAggregationV2` |
**Ontologies** | [SumAggregationV2Dict](docs/v2/Ontologies/models/SumAggregationV2Dict.md) | `from foundry.v2.ontologies.models import SumAggregationV2Dict` |
**Ontologies** | [SyncApplyActionResponseV2](docs/v2/Ontologies/models/SyncApplyActionResponseV2.md) | `from foundry.v2.ontologies.models import SyncApplyActionResponseV2` |
**Ontologies** | [SyncApplyActionResponseV2Dict](docs/v2/Ontologies/models/SyncApplyActionResponseV2Dict.md) | `from foundry.v2.ontologies.models import SyncApplyActionResponseV2Dict` |
**Ontologies** | [ThreeDimensionalAggregation](docs/v2/Ontologies/models/ThreeDimensionalAggregation.md) | `from foundry.v2.ontologies.models import ThreeDimensionalAggregation` |
**Ontologies** | [ThreeDimensionalAggregationDict](docs/v2/Ontologies/models/ThreeDimensionalAggregationDict.md) | `from foundry.v2.ontologies.models import ThreeDimensionalAggregationDict` |
**Ontologies** | [TimeRange](docs/v2/Ontologies/models/TimeRange.md) | `from foundry.v2.ontologies.models import TimeRange` |
**Ontologies** | [TimeRangeDict](docs/v2/Ontologies/models/TimeRangeDict.md) | `from foundry.v2.ontologies.models import TimeRangeDict` |
**Ontologies** | [TimeSeriesPoint](docs/v2/Ontologies/models/TimeSeriesPoint.md) | `from foundry.v2.ontologies.models import TimeSeriesPoint` |
**Ontologies** | [TimeSeriesPointDict](docs/v2/Ontologies/models/TimeSeriesPointDict.md) | `from foundry.v2.ontologies.models import TimeSeriesPointDict` |
**Ontologies** | [TimeUnit](docs/v2/Ontologies/models/TimeUnit.md) | `from foundry.v2.ontologies.models import TimeUnit` |
**Ontologies** | [TwoDimensionalAggregation](docs/v2/Ontologies/models/TwoDimensionalAggregation.md) | `from foundry.v2.ontologies.models import TwoDimensionalAggregation` |
**Ontologies** | [TwoDimensionalAggregationDict](docs/v2/Ontologies/models/TwoDimensionalAggregationDict.md) | `from foundry.v2.ontologies.models import TwoDimensionalAggregationDict` |
**Ontologies** | [UnevaluableConstraint](docs/v2/Ontologies/models/UnevaluableConstraint.md) | `from foundry.v2.ontologies.models import UnevaluableConstraint` |
**Ontologies** | [UnevaluableConstraintDict](docs/v2/Ontologies/models/UnevaluableConstraintDict.md) | `from foundry.v2.ontologies.models import UnevaluableConstraintDict` |
**Ontologies** | [ValidateActionResponseV2](docs/v2/Ontologies/models/ValidateActionResponseV2.md) | `from foundry.v2.ontologies.models import ValidateActionResponseV2` |
**Ontologies** | [ValidateActionResponseV2Dict](docs/v2/Ontologies/models/ValidateActionResponseV2Dict.md) | `from foundry.v2.ontologies.models import ValidateActionResponseV2Dict` |
**Ontologies** | [ValidationResult](docs/v2/Ontologies/models/ValidationResult.md) | `from foundry.v2.ontologies.models import ValidationResult` |
**Ontologies** | [WithinBoundingBoxPoint](docs/v2/Ontologies/models/WithinBoundingBoxPoint.md) | `from foundry.v2.ontologies.models import WithinBoundingBoxPoint` |
**Ontologies** | [WithinBoundingBoxPointDict](docs/v2/Ontologies/models/WithinBoundingBoxPointDict.md) | `from foundry.v2.ontologies.models import WithinBoundingBoxPointDict` |
**Ontologies** | [WithinBoundingBoxQuery](docs/v2/Ontologies/models/WithinBoundingBoxQuery.md) | `from foundry.v2.ontologies.models import WithinBoundingBoxQuery` |
**Ontologies** | [WithinBoundingBoxQueryDict](docs/v2/Ontologies/models/WithinBoundingBoxQueryDict.md) | `from foundry.v2.ontologies.models import WithinBoundingBoxQueryDict` |
**Ontologies** | [WithinDistanceOfQuery](docs/v2/Ontologies/models/WithinDistanceOfQuery.md) | `from foundry.v2.ontologies.models import WithinDistanceOfQuery` |
**Ontologies** | [WithinDistanceOfQueryDict](docs/v2/Ontologies/models/WithinDistanceOfQueryDict.md) | `from foundry.v2.ontologies.models import WithinDistanceOfQueryDict` |
**Ontologies** | [WithinPolygonQuery](docs/v2/Ontologies/models/WithinPolygonQuery.md) | `from foundry.v2.ontologies.models import WithinPolygonQuery` |
**Ontologies** | [WithinPolygonQueryDict](docs/v2/Ontologies/models/WithinPolygonQueryDict.md) | `from foundry.v2.ontologies.models import WithinPolygonQueryDict` |
**Orchestration** | [AbortOnFailure](docs/v2/Orchestration/models/AbortOnFailure.md) | `from foundry.v2.orchestration.models import AbortOnFailure` |
**Orchestration** | [Action](docs/v2/Orchestration/models/Action.md) | `from foundry.v2.orchestration.models import Action` |
**Orchestration** | [ActionDict](docs/v2/Orchestration/models/ActionDict.md) | `from foundry.v2.orchestration.models import ActionDict` |
**Orchestration** | [AndTrigger](docs/v2/Orchestration/models/AndTrigger.md) | `from foundry.v2.orchestration.models import AndTrigger` |
**Orchestration** | [AndTriggerDict](docs/v2/Orchestration/models/AndTriggerDict.md) | `from foundry.v2.orchestration.models import AndTriggerDict` |
**Orchestration** | [Build](docs/v2/Orchestration/models/Build.md) | `from foundry.v2.orchestration.models import Build` |
**Orchestration** | [BuildableRid](docs/v2/Orchestration/models/BuildableRid.md) | `from foundry.v2.orchestration.models import BuildableRid` |
**Orchestration** | [BuildDict](docs/v2/Orchestration/models/BuildDict.md) | `from foundry.v2.orchestration.models import BuildDict` |
**Orchestration** | [BuildRid](docs/v2/Orchestration/models/BuildRid.md) | `from foundry.v2.orchestration.models import BuildRid` |
**Orchestration** | [BuildStatus](docs/v2/Orchestration/models/BuildStatus.md) | `from foundry.v2.orchestration.models import BuildStatus` |
**Orchestration** | [BuildTarget](docs/v2/Orchestration/models/BuildTarget.md) | `from foundry.v2.orchestration.models import BuildTarget` |
**Orchestration** | [BuildTargetDict](docs/v2/Orchestration/models/BuildTargetDict.md) | `from foundry.v2.orchestration.models import BuildTargetDict` |
**Orchestration** | [ConnectingTarget](docs/v2/Orchestration/models/ConnectingTarget.md) | `from foundry.v2.orchestration.models import ConnectingTarget` |
**Orchestration** | [ConnectingTargetDict](docs/v2/Orchestration/models/ConnectingTargetDict.md) | `from foundry.v2.orchestration.models import ConnectingTargetDict` |
**Orchestration** | [CreateScheduleRequestAction](docs/v2/Orchestration/models/CreateScheduleRequestAction.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestAction` |
**Orchestration** | [CreateScheduleRequestActionDict](docs/v2/Orchestration/models/CreateScheduleRequestActionDict.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestActionDict` |
**Orchestration** | [CreateScheduleRequestBuildTarget](docs/v2/Orchestration/models/CreateScheduleRequestBuildTarget.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestBuildTarget` |
**Orchestration** | [CreateScheduleRequestBuildTargetDict](docs/v2/Orchestration/models/CreateScheduleRequestBuildTargetDict.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestBuildTargetDict` |
**Orchestration** | [CreateScheduleRequestConnectingTarget](docs/v2/Orchestration/models/CreateScheduleRequestConnectingTarget.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestConnectingTarget` |
**Orchestration** | [CreateScheduleRequestConnectingTargetDict](docs/v2/Orchestration/models/CreateScheduleRequestConnectingTargetDict.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestConnectingTargetDict` |
**Orchestration** | [CreateScheduleRequestManualTarget](docs/v2/Orchestration/models/CreateScheduleRequestManualTarget.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestManualTarget` |
**Orchestration** | [CreateScheduleRequestManualTargetDict](docs/v2/Orchestration/models/CreateScheduleRequestManualTargetDict.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestManualTargetDict` |
**Orchestration** | [CreateScheduleRequestProjectScope](docs/v2/Orchestration/models/CreateScheduleRequestProjectScope.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestProjectScope` |
**Orchestration** | [CreateScheduleRequestProjectScopeDict](docs/v2/Orchestration/models/CreateScheduleRequestProjectScopeDict.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestProjectScopeDict` |
**Orchestration** | [CreateScheduleRequestScopeMode](docs/v2/Orchestration/models/CreateScheduleRequestScopeMode.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestScopeMode` |
**Orchestration** | [CreateScheduleRequestScopeModeDict](docs/v2/Orchestration/models/CreateScheduleRequestScopeModeDict.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestScopeModeDict` |
**Orchestration** | [CreateScheduleRequestUpstreamTarget](docs/v2/Orchestration/models/CreateScheduleRequestUpstreamTarget.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestUpstreamTarget` |
**Orchestration** | [CreateScheduleRequestUpstreamTargetDict](docs/v2/Orchestration/models/CreateScheduleRequestUpstreamTargetDict.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestUpstreamTargetDict` |
**Orchestration** | [CreateScheduleRequestUserScope](docs/v2/Orchestration/models/CreateScheduleRequestUserScope.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestUserScope` |
**Orchestration** | [CreateScheduleRequestUserScopeDict](docs/v2/Orchestration/models/CreateScheduleRequestUserScopeDict.md) | `from foundry.v2.orchestration.models import CreateScheduleRequestUserScopeDict` |
**Orchestration** | [CronExpression](docs/v2/Orchestration/models/CronExpression.md) | `from foundry.v2.orchestration.models import CronExpression` |
**Orchestration** | [DatasetUpdatedTrigger](docs/v2/Orchestration/models/DatasetUpdatedTrigger.md) | `from foundry.v2.orchestration.models import DatasetUpdatedTrigger` |
**Orchestration** | [DatasetUpdatedTriggerDict](docs/v2/Orchestration/models/DatasetUpdatedTriggerDict.md) | `from foundry.v2.orchestration.models import DatasetUpdatedTriggerDict` |
**Orchestration** | [FallbackBranches](docs/v2/Orchestration/models/FallbackBranches.md) | `from foundry.v2.orchestration.models import FallbackBranches` |
**Orchestration** | [ForceBuild](docs/v2/Orchestration/models/ForceBuild.md) | `from foundry.v2.orchestration.models import ForceBuild` |
**Orchestration** | [GetBuildsBatchRequestElement](docs/v2/Orchestration/models/GetBuildsBatchRequestElement.md) | `from foundry.v2.orchestration.models import GetBuildsBatchRequestElement` |
**Orchestration** | [GetBuildsBatchRequestElementDict](docs/v2/Orchestration/models/GetBuildsBatchRequestElementDict.md) | `from foundry.v2.orchestration.models import GetBuildsBatchRequestElementDict` |
**Orchestration** | [GetBuildsBatchResponse](docs/v2/Orchestration/models/GetBuildsBatchResponse.md) | `from foundry.v2.orchestration.models import GetBuildsBatchResponse` |
**Orchestration** | [GetBuildsBatchResponseDict](docs/v2/Orchestration/models/GetBuildsBatchResponseDict.md) | `from foundry.v2.orchestration.models import GetBuildsBatchResponseDict` |
**Orchestration** | [Job](docs/v2/Orchestration/models/Job.md) | `from foundry.v2.orchestration.models import Job` |
**Orchestration** | [JobDict](docs/v2/Orchestration/models/JobDict.md) | `from foundry.v2.orchestration.models import JobDict` |
**Orchestration** | [JobRid](docs/v2/Orchestration/models/JobRid.md) | `from foundry.v2.orchestration.models import JobRid` |
**Orchestration** | [JobSucceededTrigger](docs/v2/Orchestration/models/JobSucceededTrigger.md) | `from foundry.v2.orchestration.models import JobSucceededTrigger` |
**Orchestration** | [JobSucceededTriggerDict](docs/v2/Orchestration/models/JobSucceededTriggerDict.md) | `from foundry.v2.orchestration.models import JobSucceededTriggerDict` |
**Orchestration** | [ListRunsOfScheduleResponse](docs/v2/Orchestration/models/ListRunsOfScheduleResponse.md) | `from foundry.v2.orchestration.models import ListRunsOfScheduleResponse` |
**Orchestration** | [ListRunsOfScheduleResponseDict](docs/v2/Orchestration/models/ListRunsOfScheduleResponseDict.md) | `from foundry.v2.orchestration.models import ListRunsOfScheduleResponseDict` |
**Orchestration** | [ManualTarget](docs/v2/Orchestration/models/ManualTarget.md) | `from foundry.v2.orchestration.models import ManualTarget` |
**Orchestration** | [ManualTargetDict](docs/v2/Orchestration/models/ManualTargetDict.md) | `from foundry.v2.orchestration.models import ManualTargetDict` |
**Orchestration** | [MediaSetUpdatedTrigger](docs/v2/Orchestration/models/MediaSetUpdatedTrigger.md) | `from foundry.v2.orchestration.models import MediaSetUpdatedTrigger` |
**Orchestration** | [MediaSetUpdatedTriggerDict](docs/v2/Orchestration/models/MediaSetUpdatedTriggerDict.md) | `from foundry.v2.orchestration.models import MediaSetUpdatedTriggerDict` |
**Orchestration** | [NewLogicTrigger](docs/v2/Orchestration/models/NewLogicTrigger.md) | `from foundry.v2.orchestration.models import NewLogicTrigger` |
**Orchestration** | [NewLogicTriggerDict](docs/v2/Orchestration/models/NewLogicTriggerDict.md) | `from foundry.v2.orchestration.models import NewLogicTriggerDict` |
**Orchestration** | [NotificationsEnabled](docs/v2/Orchestration/models/NotificationsEnabled.md) | `from foundry.v2.orchestration.models import NotificationsEnabled` |
**Orchestration** | [OrTrigger](docs/v2/Orchestration/models/OrTrigger.md) | `from foundry.v2.orchestration.models import OrTrigger` |
**Orchestration** | [OrTriggerDict](docs/v2/Orchestration/models/OrTriggerDict.md) | `from foundry.v2.orchestration.models import OrTriggerDict` |
**Orchestration** | [ProjectScope](docs/v2/Orchestration/models/ProjectScope.md) | `from foundry.v2.orchestration.models import ProjectScope` |
**Orchestration** | [ProjectScopeDict](docs/v2/Orchestration/models/ProjectScopeDict.md) | `from foundry.v2.orchestration.models import ProjectScopeDict` |
**Orchestration** | [ReplaceScheduleRequestAction](docs/v2/Orchestration/models/ReplaceScheduleRequestAction.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestAction` |
**Orchestration** | [ReplaceScheduleRequestActionDict](docs/v2/Orchestration/models/ReplaceScheduleRequestActionDict.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestActionDict` |
**Orchestration** | [ReplaceScheduleRequestBuildTarget](docs/v2/Orchestration/models/ReplaceScheduleRequestBuildTarget.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestBuildTarget` |
**Orchestration** | [ReplaceScheduleRequestBuildTargetDict](docs/v2/Orchestration/models/ReplaceScheduleRequestBuildTargetDict.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestBuildTargetDict` |
**Orchestration** | [ReplaceScheduleRequestConnectingTarget](docs/v2/Orchestration/models/ReplaceScheduleRequestConnectingTarget.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestConnectingTarget` |
**Orchestration** | [ReplaceScheduleRequestConnectingTargetDict](docs/v2/Orchestration/models/ReplaceScheduleRequestConnectingTargetDict.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestConnectingTargetDict` |
**Orchestration** | [ReplaceScheduleRequestManualTarget](docs/v2/Orchestration/models/ReplaceScheduleRequestManualTarget.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestManualTarget` |
**Orchestration** | [ReplaceScheduleRequestManualTargetDict](docs/v2/Orchestration/models/ReplaceScheduleRequestManualTargetDict.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestManualTargetDict` |
**Orchestration** | [ReplaceScheduleRequestProjectScope](docs/v2/Orchestration/models/ReplaceScheduleRequestProjectScope.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestProjectScope` |
**Orchestration** | [ReplaceScheduleRequestProjectScopeDict](docs/v2/Orchestration/models/ReplaceScheduleRequestProjectScopeDict.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestProjectScopeDict` |
**Orchestration** | [ReplaceScheduleRequestScopeMode](docs/v2/Orchestration/models/ReplaceScheduleRequestScopeMode.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestScopeMode` |
**Orchestration** | [ReplaceScheduleRequestScopeModeDict](docs/v2/Orchestration/models/ReplaceScheduleRequestScopeModeDict.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestScopeModeDict` |
**Orchestration** | [ReplaceScheduleRequestUpstreamTarget](docs/v2/Orchestration/models/ReplaceScheduleRequestUpstreamTarget.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestUpstreamTarget` |
**Orchestration** | [ReplaceScheduleRequestUpstreamTargetDict](docs/v2/Orchestration/models/ReplaceScheduleRequestUpstreamTargetDict.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestUpstreamTargetDict` |
**Orchestration** | [ReplaceScheduleRequestUserScope](docs/v2/Orchestration/models/ReplaceScheduleRequestUserScope.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestUserScope` |
**Orchestration** | [ReplaceScheduleRequestUserScopeDict](docs/v2/Orchestration/models/ReplaceScheduleRequestUserScopeDict.md) | `from foundry.v2.orchestration.models import ReplaceScheduleRequestUserScopeDict` |
**Orchestration** | [RetryBackoffDuration](docs/v2/Orchestration/models/RetryBackoffDuration.md) | `from foundry.v2.orchestration.models import RetryBackoffDuration` |
**Orchestration** | [RetryBackoffDurationDict](docs/v2/Orchestration/models/RetryBackoffDurationDict.md) | `from foundry.v2.orchestration.models import RetryBackoffDurationDict` |
**Orchestration** | [RetryCount](docs/v2/Orchestration/models/RetryCount.md) | `from foundry.v2.orchestration.models import RetryCount` |
**Orchestration** | [Schedule](docs/v2/Orchestration/models/Schedule.md) | `from foundry.v2.orchestration.models import Schedule` |
**Orchestration** | [ScheduleDict](docs/v2/Orchestration/models/ScheduleDict.md) | `from foundry.v2.orchestration.models import ScheduleDict` |
**Orchestration** | [SchedulePaused](docs/v2/Orchestration/models/SchedulePaused.md) | `from foundry.v2.orchestration.models import SchedulePaused` |
**Orchestration** | [ScheduleRid](docs/v2/Orchestration/models/ScheduleRid.md) | `from foundry.v2.orchestration.models import ScheduleRid` |
**Orchestration** | [ScheduleRun](docs/v2/Orchestration/models/ScheduleRun.md) | `from foundry.v2.orchestration.models import ScheduleRun` |
**Orchestration** | [ScheduleRunDict](docs/v2/Orchestration/models/ScheduleRunDict.md) | `from foundry.v2.orchestration.models import ScheduleRunDict` |
**Orchestration** | [ScheduleRunError](docs/v2/Orchestration/models/ScheduleRunError.md) | `from foundry.v2.orchestration.models import ScheduleRunError` |
**Orchestration** | [ScheduleRunErrorDict](docs/v2/Orchestration/models/ScheduleRunErrorDict.md) | `from foundry.v2.orchestration.models import ScheduleRunErrorDict` |
**Orchestration** | [ScheduleRunErrorName](docs/v2/Orchestration/models/ScheduleRunErrorName.md) | `from foundry.v2.orchestration.models import ScheduleRunErrorName` |
**Orchestration** | [ScheduleRunIgnored](docs/v2/Orchestration/models/ScheduleRunIgnored.md) | `from foundry.v2.orchestration.models import ScheduleRunIgnored` |
**Orchestration** | [ScheduleRunIgnoredDict](docs/v2/Orchestration/models/ScheduleRunIgnoredDict.md) | `from foundry.v2.orchestration.models import ScheduleRunIgnoredDict` |
**Orchestration** | [ScheduleRunResult](docs/v2/Orchestration/models/ScheduleRunResult.md) | `from foundry.v2.orchestration.models import ScheduleRunResult` |
**Orchestration** | [ScheduleRunResultDict](docs/v2/Orchestration/models/ScheduleRunResultDict.md) | `from foundry.v2.orchestration.models import ScheduleRunResultDict` |
**Orchestration** | [ScheduleRunRid](docs/v2/Orchestration/models/ScheduleRunRid.md) | `from foundry.v2.orchestration.models import ScheduleRunRid` |
**Orchestration** | [ScheduleRunSubmitted](docs/v2/Orchestration/models/ScheduleRunSubmitted.md) | `from foundry.v2.orchestration.models import ScheduleRunSubmitted` |
**Orchestration** | [ScheduleRunSubmittedDict](docs/v2/Orchestration/models/ScheduleRunSubmittedDict.md) | `from foundry.v2.orchestration.models import ScheduleRunSubmittedDict` |
**Orchestration** | [ScheduleSucceededTrigger](docs/v2/Orchestration/models/ScheduleSucceededTrigger.md) | `from foundry.v2.orchestration.models import ScheduleSucceededTrigger` |
**Orchestration** | [ScheduleSucceededTriggerDict](docs/v2/Orchestration/models/ScheduleSucceededTriggerDict.md) | `from foundry.v2.orchestration.models import ScheduleSucceededTriggerDict` |
**Orchestration** | [ScheduleVersion](docs/v2/Orchestration/models/ScheduleVersion.md) | `from foundry.v2.orchestration.models import ScheduleVersion` |
**Orchestration** | [ScheduleVersionDict](docs/v2/Orchestration/models/ScheduleVersionDict.md) | `from foundry.v2.orchestration.models import ScheduleVersionDict` |
**Orchestration** | [ScheduleVersionRid](docs/v2/Orchestration/models/ScheduleVersionRid.md) | `from foundry.v2.orchestration.models import ScheduleVersionRid` |
**Orchestration** | [ScopeMode](docs/v2/Orchestration/models/ScopeMode.md) | `from foundry.v2.orchestration.models import ScopeMode` |
**Orchestration** | [ScopeModeDict](docs/v2/Orchestration/models/ScopeModeDict.md) | `from foundry.v2.orchestration.models import ScopeModeDict` |
**Orchestration** | [SearchBuildsAndFilter](docs/v2/Orchestration/models/SearchBuildsAndFilter.md) | `from foundry.v2.orchestration.models import SearchBuildsAndFilter` |
**Orchestration** | [SearchBuildsAndFilterDict](docs/v2/Orchestration/models/SearchBuildsAndFilterDict.md) | `from foundry.v2.orchestration.models import SearchBuildsAndFilterDict` |
**Orchestration** | [SearchBuildsEqualsFilter](docs/v2/Orchestration/models/SearchBuildsEqualsFilter.md) | `from foundry.v2.orchestration.models import SearchBuildsEqualsFilter` |
**Orchestration** | [SearchBuildsEqualsFilterDict](docs/v2/Orchestration/models/SearchBuildsEqualsFilterDict.md) | `from foundry.v2.orchestration.models import SearchBuildsEqualsFilterDict` |
**Orchestration** | [SearchBuildsEqualsFilterField](docs/v2/Orchestration/models/SearchBuildsEqualsFilterField.md) | `from foundry.v2.orchestration.models import SearchBuildsEqualsFilterField` |
**Orchestration** | [SearchBuildsFilter](docs/v2/Orchestration/models/SearchBuildsFilter.md) | `from foundry.v2.orchestration.models import SearchBuildsFilter` |
**Orchestration** | [SearchBuildsFilterDict](docs/v2/Orchestration/models/SearchBuildsFilterDict.md) | `from foundry.v2.orchestration.models import SearchBuildsFilterDict` |
**Orchestration** | [SearchBuildsGteFilter](docs/v2/Orchestration/models/SearchBuildsGteFilter.md) | `from foundry.v2.orchestration.models import SearchBuildsGteFilter` |
**Orchestration** | [SearchBuildsGteFilterDict](docs/v2/Orchestration/models/SearchBuildsGteFilterDict.md) | `from foundry.v2.orchestration.models import SearchBuildsGteFilterDict` |
**Orchestration** | [SearchBuildsGteFilterField](docs/v2/Orchestration/models/SearchBuildsGteFilterField.md) | `from foundry.v2.orchestration.models import SearchBuildsGteFilterField` |
**Orchestration** | [SearchBuildsLtFilter](docs/v2/Orchestration/models/SearchBuildsLtFilter.md) | `from foundry.v2.orchestration.models import SearchBuildsLtFilter` |
**Orchestration** | [SearchBuildsLtFilterDict](docs/v2/Orchestration/models/SearchBuildsLtFilterDict.md) | `from foundry.v2.orchestration.models import SearchBuildsLtFilterDict` |
**Orchestration** | [SearchBuildsLtFilterField](docs/v2/Orchestration/models/SearchBuildsLtFilterField.md) | `from foundry.v2.orchestration.models import SearchBuildsLtFilterField` |
**Orchestration** | [SearchBuildsNotFilter](docs/v2/Orchestration/models/SearchBuildsNotFilter.md) | `from foundry.v2.orchestration.models import SearchBuildsNotFilter` |
**Orchestration** | [SearchBuildsNotFilterDict](docs/v2/Orchestration/models/SearchBuildsNotFilterDict.md) | `from foundry.v2.orchestration.models import SearchBuildsNotFilterDict` |
**Orchestration** | [SearchBuildsOrderBy](docs/v2/Orchestration/models/SearchBuildsOrderBy.md) | `from foundry.v2.orchestration.models import SearchBuildsOrderBy` |
**Orchestration** | [SearchBuildsOrderByDict](docs/v2/Orchestration/models/SearchBuildsOrderByDict.md) | `from foundry.v2.orchestration.models import SearchBuildsOrderByDict` |
**Orchestration** | [SearchBuildsOrderByField](docs/v2/Orchestration/models/SearchBuildsOrderByField.md) | `from foundry.v2.orchestration.models import SearchBuildsOrderByField` |
**Orchestration** | [SearchBuildsOrderByItem](docs/v2/Orchestration/models/SearchBuildsOrderByItem.md) | `from foundry.v2.orchestration.models import SearchBuildsOrderByItem` |
**Orchestration** | [SearchBuildsOrderByItemDict](docs/v2/Orchestration/models/SearchBuildsOrderByItemDict.md) | `from foundry.v2.orchestration.models import SearchBuildsOrderByItemDict` |
**Orchestration** | [SearchBuildsOrFilter](docs/v2/Orchestration/models/SearchBuildsOrFilter.md) | `from foundry.v2.orchestration.models import SearchBuildsOrFilter` |
**Orchestration** | [SearchBuildsOrFilterDict](docs/v2/Orchestration/models/SearchBuildsOrFilterDict.md) | `from foundry.v2.orchestration.models import SearchBuildsOrFilterDict` |
**Orchestration** | [SearchBuildsResponse](docs/v2/Orchestration/models/SearchBuildsResponse.md) | `from foundry.v2.orchestration.models import SearchBuildsResponse` |
**Orchestration** | [SearchBuildsResponseDict](docs/v2/Orchestration/models/SearchBuildsResponseDict.md) | `from foundry.v2.orchestration.models import SearchBuildsResponseDict` |
**Orchestration** | [TimeTrigger](docs/v2/Orchestration/models/TimeTrigger.md) | `from foundry.v2.orchestration.models import TimeTrigger` |
**Orchestration** | [TimeTriggerDict](docs/v2/Orchestration/models/TimeTriggerDict.md) | `from foundry.v2.orchestration.models import TimeTriggerDict` |
**Orchestration** | [Trigger](docs/v2/Orchestration/models/Trigger.md) | `from foundry.v2.orchestration.models import Trigger` |
**Orchestration** | [TriggerDict](docs/v2/Orchestration/models/TriggerDict.md) | `from foundry.v2.orchestration.models import TriggerDict` |
**Orchestration** | [UpstreamTarget](docs/v2/Orchestration/models/UpstreamTarget.md) | `from foundry.v2.orchestration.models import UpstreamTarget` |
**Orchestration** | [UpstreamTargetDict](docs/v2/Orchestration/models/UpstreamTargetDict.md) | `from foundry.v2.orchestration.models import UpstreamTargetDict` |
**Orchestration** | [UserScope](docs/v2/Orchestration/models/UserScope.md) | `from foundry.v2.orchestration.models import UserScope` |
**Orchestration** | [UserScopeDict](docs/v2/Orchestration/models/UserScopeDict.md) | `from foundry.v2.orchestration.models import UserScopeDict` |
**Streams** | [Compressed](docs/v2/Streams/models/Compressed.md) | `from foundry.v2.streams.models import Compressed` |
**Streams** | [CreateStreamRequestStreamSchema](docs/v2/Streams/models/CreateStreamRequestStreamSchema.md) | `from foundry.v2.streams.models import CreateStreamRequestStreamSchema` |
**Streams** | [CreateStreamRequestStreamSchemaDict](docs/v2/Streams/models/CreateStreamRequestStreamSchemaDict.md) | `from foundry.v2.streams.models import CreateStreamRequestStreamSchemaDict` |
**Streams** | [Dataset](docs/v2/Streams/models/Dataset.md) | `from foundry.v2.streams.models import Dataset` |
**Streams** | [DatasetDict](docs/v2/Streams/models/DatasetDict.md) | `from foundry.v2.streams.models import DatasetDict` |
**Streams** | [PartitionsCount](docs/v2/Streams/models/PartitionsCount.md) | `from foundry.v2.streams.models import PartitionsCount` |
**Streams** | [Record](docs/v2/Streams/models/Record.md) | `from foundry.v2.streams.models import Record` |
**Streams** | [Stream](docs/v2/Streams/models/Stream.md) | `from foundry.v2.streams.models import Stream` |
**Streams** | [StreamDict](docs/v2/Streams/models/StreamDict.md) | `from foundry.v2.streams.models import StreamDict` |
**Streams** | [StreamType](docs/v2/Streams/models/StreamType.md) | `from foundry.v2.streams.models import StreamType` |
**Streams** | [ViewRid](docs/v2/Streams/models/ViewRid.md) | `from foundry.v2.streams.models import ViewRid` |
**ThirdPartyApplications** | [ListVersionsResponse](docs/v2/ThirdPartyApplications/models/ListVersionsResponse.md) | `from foundry.v2.third_party_applications.models import ListVersionsResponse` |
**ThirdPartyApplications** | [ListVersionsResponseDict](docs/v2/ThirdPartyApplications/models/ListVersionsResponseDict.md) | `from foundry.v2.third_party_applications.models import ListVersionsResponseDict` |
**ThirdPartyApplications** | [Subdomain](docs/v2/ThirdPartyApplications/models/Subdomain.md) | `from foundry.v2.third_party_applications.models import Subdomain` |
**ThirdPartyApplications** | [ThirdPartyApplication](docs/v2/ThirdPartyApplications/models/ThirdPartyApplication.md) | `from foundry.v2.third_party_applications.models import ThirdPartyApplication` |
**ThirdPartyApplications** | [ThirdPartyApplicationDict](docs/v2/ThirdPartyApplications/models/ThirdPartyApplicationDict.md) | `from foundry.v2.third_party_applications.models import ThirdPartyApplicationDict` |
**ThirdPartyApplications** | [ThirdPartyApplicationRid](docs/v2/ThirdPartyApplications/models/ThirdPartyApplicationRid.md) | `from foundry.v2.third_party_applications.models import ThirdPartyApplicationRid` |
**ThirdPartyApplications** | [Version](docs/v2/ThirdPartyApplications/models/Version.md) | `from foundry.v2.third_party_applications.models import Version` |
**ThirdPartyApplications** | [VersionDict](docs/v2/ThirdPartyApplications/models/VersionDict.md) | `from foundry.v2.third_party_applications.models import VersionDict` |
**ThirdPartyApplications** | [VersionVersion](docs/v2/ThirdPartyApplications/models/VersionVersion.md) | `from foundry.v2.third_party_applications.models import VersionVersion` |
**ThirdPartyApplications** | [Website](docs/v2/ThirdPartyApplications/models/Website.md) | `from foundry.v2.third_party_applications.models import Website` |
**ThirdPartyApplications** | [WebsiteDict](docs/v2/ThirdPartyApplications/models/WebsiteDict.md) | `from foundry.v2.third_party_applications.models import WebsiteDict` |

<a id="models-v1-link"></a>
## Documentation for V1 models

Namespace | Name | Import |
--------- | ---- | ------ |
**Core** | [AnyType](docs/v1/Core/models/AnyType.md) | `from foundry.v1.core.models import AnyType` |
**Core** | [AnyTypeDict](docs/v1/Core/models/AnyTypeDict.md) | `from foundry.v1.core.models import AnyTypeDict` |
**Core** | [AttachmentTypeDict](docs/v1/Core/models/AttachmentTypeDict.md) | `from foundry.v1.core.models import AttachmentTypeDict` |
**Core** | [BinaryType](docs/v1/Core/models/BinaryType.md) | `from foundry.v1.core.models import BinaryType` |
**Core** | [BinaryTypeDict](docs/v1/Core/models/BinaryTypeDict.md) | `from foundry.v1.core.models import BinaryTypeDict` |
**Core** | [BooleanType](docs/v1/Core/models/BooleanType.md) | `from foundry.v1.core.models import BooleanType` |
**Core** | [BooleanTypeDict](docs/v1/Core/models/BooleanTypeDict.md) | `from foundry.v1.core.models import BooleanTypeDict` |
**Core** | [ByteType](docs/v1/Core/models/ByteType.md) | `from foundry.v1.core.models import ByteType` |
**Core** | [ByteTypeDict](docs/v1/Core/models/ByteTypeDict.md) | `from foundry.v1.core.models import ByteTypeDict` |
**Core** | [CipherTextType](docs/v1/Core/models/CipherTextType.md) | `from foundry.v1.core.models import CipherTextType` |
**Core** | [CipherTextTypeDict](docs/v1/Core/models/CipherTextTypeDict.md) | `from foundry.v1.core.models import CipherTextTypeDict` |
**Core** | [DateType](docs/v1/Core/models/DateType.md) | `from foundry.v1.core.models import DateType` |
**Core** | [DateTypeDict](docs/v1/Core/models/DateTypeDict.md) | `from foundry.v1.core.models import DateTypeDict` |
**Core** | [DecimalType](docs/v1/Core/models/DecimalType.md) | `from foundry.v1.core.models import DecimalType` |
**Core** | [DecimalTypeDict](docs/v1/Core/models/DecimalTypeDict.md) | `from foundry.v1.core.models import DecimalTypeDict` |
**Core** | [DisplayName](docs/v1/Core/models/DisplayName.md) | `from foundry.v1.core.models import DisplayName` |
**Core** | [DistanceUnit](docs/v1/Core/models/DistanceUnit.md) | `from foundry.v1.core.models import DistanceUnit` |
**Core** | [DoubleType](docs/v1/Core/models/DoubleType.md) | `from foundry.v1.core.models import DoubleType` |
**Core** | [DoubleTypeDict](docs/v1/Core/models/DoubleTypeDict.md) | `from foundry.v1.core.models import DoubleTypeDict` |
**Core** | [FilePath](docs/v1/Core/models/FilePath.md) | `from foundry.v1.core.models import FilePath` |
**Core** | [FloatType](docs/v1/Core/models/FloatType.md) | `from foundry.v1.core.models import FloatType` |
**Core** | [FloatTypeDict](docs/v1/Core/models/FloatTypeDict.md) | `from foundry.v1.core.models import FloatTypeDict` |
**Core** | [FolderRid](docs/v1/Core/models/FolderRid.md) | `from foundry.v1.core.models import FolderRid` |
**Core** | [IntegerType](docs/v1/Core/models/IntegerType.md) | `from foundry.v1.core.models import IntegerType` |
**Core** | [IntegerTypeDict](docs/v1/Core/models/IntegerTypeDict.md) | `from foundry.v1.core.models import IntegerTypeDict` |
**Core** | [LongType](docs/v1/Core/models/LongType.md) | `from foundry.v1.core.models import LongType` |
**Core** | [LongTypeDict](docs/v1/Core/models/LongTypeDict.md) | `from foundry.v1.core.models import LongTypeDict` |
**Core** | [MarkingType](docs/v1/Core/models/MarkingType.md) | `from foundry.v1.core.models import MarkingType` |
**Core** | [MarkingTypeDict](docs/v1/Core/models/MarkingTypeDict.md) | `from foundry.v1.core.models import MarkingTypeDict` |
**Core** | [NullTypeDict](docs/v1/Core/models/NullTypeDict.md) | `from foundry.v1.core.models import NullTypeDict` |
**Core** | [PageSize](docs/v1/Core/models/PageSize.md) | `from foundry.v1.core.models import PageSize` |
**Core** | [PageToken](docs/v1/Core/models/PageToken.md) | `from foundry.v1.core.models import PageToken` |
**Core** | [PreviewMode](docs/v1/Core/models/PreviewMode.md) | `from foundry.v1.core.models import PreviewMode` |
**Core** | [ReleaseStatus](docs/v1/Core/models/ReleaseStatus.md) | `from foundry.v1.core.models import ReleaseStatus` |
**Core** | [ShortType](docs/v1/Core/models/ShortType.md) | `from foundry.v1.core.models import ShortType` |
**Core** | [ShortTypeDict](docs/v1/Core/models/ShortTypeDict.md) | `from foundry.v1.core.models import ShortTypeDict` |
**Core** | [StringType](docs/v1/Core/models/StringType.md) | `from foundry.v1.core.models import StringType` |
**Core** | [StringTypeDict](docs/v1/Core/models/StringTypeDict.md) | `from foundry.v1.core.models import StringTypeDict` |
**Core** | [StructFieldName](docs/v1/Core/models/StructFieldName.md) | `from foundry.v1.core.models import StructFieldName` |
**Core** | [TimestampType](docs/v1/Core/models/TimestampType.md) | `from foundry.v1.core.models import TimestampType` |
**Core** | [TimestampTypeDict](docs/v1/Core/models/TimestampTypeDict.md) | `from foundry.v1.core.models import TimestampTypeDict` |
**Core** | [TotalCount](docs/v1/Core/models/TotalCount.md) | `from foundry.v1.core.models import TotalCount` |
**Core** | [UnsupportedType](docs/v1/Core/models/UnsupportedType.md) | `from foundry.v1.core.models import UnsupportedType` |
**Core** | [UnsupportedTypeDict](docs/v1/Core/models/UnsupportedTypeDict.md) | `from foundry.v1.core.models import UnsupportedTypeDict` |
**Datasets** | [Branch](docs/v1/Datasets/models/Branch.md) | `from foundry.v1.datasets.models import Branch` |
**Datasets** | [BranchDict](docs/v1/Datasets/models/BranchDict.md) | `from foundry.v1.datasets.models import BranchDict` |
**Datasets** | [BranchId](docs/v1/Datasets/models/BranchId.md) | `from foundry.v1.datasets.models import BranchId` |
**Datasets** | [Dataset](docs/v1/Datasets/models/Dataset.md) | `from foundry.v1.datasets.models import Dataset` |
**Datasets** | [DatasetDict](docs/v1/Datasets/models/DatasetDict.md) | `from foundry.v1.datasets.models import DatasetDict` |
**Datasets** | [DatasetName](docs/v1/Datasets/models/DatasetName.md) | `from foundry.v1.datasets.models import DatasetName` |
**Datasets** | [DatasetRid](docs/v1/Datasets/models/DatasetRid.md) | `from foundry.v1.datasets.models import DatasetRid` |
**Datasets** | [File](docs/v1/Datasets/models/File.md) | `from foundry.v1.datasets.models import File` |
**Datasets** | [FileDict](docs/v1/Datasets/models/FileDict.md) | `from foundry.v1.datasets.models import FileDict` |
**Datasets** | [ListBranchesResponse](docs/v1/Datasets/models/ListBranchesResponse.md) | `from foundry.v1.datasets.models import ListBranchesResponse` |
**Datasets** | [ListBranchesResponseDict](docs/v1/Datasets/models/ListBranchesResponseDict.md) | `from foundry.v1.datasets.models import ListBranchesResponseDict` |
**Datasets** | [ListFilesResponse](docs/v1/Datasets/models/ListFilesResponse.md) | `from foundry.v1.datasets.models import ListFilesResponse` |
**Datasets** | [ListFilesResponseDict](docs/v1/Datasets/models/ListFilesResponseDict.md) | `from foundry.v1.datasets.models import ListFilesResponseDict` |
**Datasets** | [TableExportFormat](docs/v1/Datasets/models/TableExportFormat.md) | `from foundry.v1.datasets.models import TableExportFormat` |
**Datasets** | [Transaction](docs/v1/Datasets/models/Transaction.md) | `from foundry.v1.datasets.models import Transaction` |
**Datasets** | [TransactionDict](docs/v1/Datasets/models/TransactionDict.md) | `from foundry.v1.datasets.models import TransactionDict` |
**Datasets** | [TransactionRid](docs/v1/Datasets/models/TransactionRid.md) | `from foundry.v1.datasets.models import TransactionRid` |
**Datasets** | [TransactionStatus](docs/v1/Datasets/models/TransactionStatus.md) | `from foundry.v1.datasets.models import TransactionStatus` |
**Datasets** | [TransactionType](docs/v1/Datasets/models/TransactionType.md) | `from foundry.v1.datasets.models import TransactionType` |
**Ontologies** | [ActionRid](docs/v1/Ontologies/models/ActionRid.md) | `from foundry.v1.ontologies.models import ActionRid` |
**Ontologies** | [ActionType](docs/v1/Ontologies/models/ActionType.md) | `from foundry.v1.ontologies.models import ActionType` |
**Ontologies** | [ActionTypeApiName](docs/v1/Ontologies/models/ActionTypeApiName.md) | `from foundry.v1.ontologies.models import ActionTypeApiName` |
**Ontologies** | [ActionTypeDict](docs/v1/Ontologies/models/ActionTypeDict.md) | `from foundry.v1.ontologies.models import ActionTypeDict` |
**Ontologies** | [ActionTypeRid](docs/v1/Ontologies/models/ActionTypeRid.md) | `from foundry.v1.ontologies.models import ActionTypeRid` |
**Ontologies** | [AggregateObjectsResponse](docs/v1/Ontologies/models/AggregateObjectsResponse.md) | `from foundry.v1.ontologies.models import AggregateObjectsResponse` |
**Ontologies** | [AggregateObjectsResponseDict](docs/v1/Ontologies/models/AggregateObjectsResponseDict.md) | `from foundry.v1.ontologies.models import AggregateObjectsResponseDict` |
**Ontologies** | [AggregateObjectsResponseItem](docs/v1/Ontologies/models/AggregateObjectsResponseItem.md) | `from foundry.v1.ontologies.models import AggregateObjectsResponseItem` |
**Ontologies** | [AggregateObjectsResponseItemDict](docs/v1/Ontologies/models/AggregateObjectsResponseItemDict.md) | `from foundry.v1.ontologies.models import AggregateObjectsResponseItemDict` |
**Ontologies** | [Aggregation](docs/v1/Ontologies/models/Aggregation.md) | `from foundry.v1.ontologies.models import Aggregation` |
**Ontologies** | [AggregationDict](docs/v1/Ontologies/models/AggregationDict.md) | `from foundry.v1.ontologies.models import AggregationDict` |
**Ontologies** | [AggregationDurationGrouping](docs/v1/Ontologies/models/AggregationDurationGrouping.md) | `from foundry.v1.ontologies.models import AggregationDurationGrouping` |
**Ontologies** | [AggregationDurationGroupingDict](docs/v1/Ontologies/models/AggregationDurationGroupingDict.md) | `from foundry.v1.ontologies.models import AggregationDurationGroupingDict` |
**Ontologies** | [AggregationExactGrouping](docs/v1/Ontologies/models/AggregationExactGrouping.md) | `from foundry.v1.ontologies.models import AggregationExactGrouping` |
**Ontologies** | [AggregationExactGroupingDict](docs/v1/Ontologies/models/AggregationExactGroupingDict.md) | `from foundry.v1.ontologies.models import AggregationExactGroupingDict` |
**Ontologies** | [AggregationFixedWidthGrouping](docs/v1/Ontologies/models/AggregationFixedWidthGrouping.md) | `from foundry.v1.ontologies.models import AggregationFixedWidthGrouping` |
**Ontologies** | [AggregationFixedWidthGroupingDict](docs/v1/Ontologies/models/AggregationFixedWidthGroupingDict.md) | `from foundry.v1.ontologies.models import AggregationFixedWidthGroupingDict` |
**Ontologies** | [AggregationGroupBy](docs/v1/Ontologies/models/AggregationGroupBy.md) | `from foundry.v1.ontologies.models import AggregationGroupBy` |
**Ontologies** | [AggregationGroupByDict](docs/v1/Ontologies/models/AggregationGroupByDict.md) | `from foundry.v1.ontologies.models import AggregationGroupByDict` |
**Ontologies** | [AggregationGroupKey](docs/v1/Ontologies/models/AggregationGroupKey.md) | `from foundry.v1.ontologies.models import AggregationGroupKey` |
**Ontologies** | [AggregationGroupValue](docs/v1/Ontologies/models/AggregationGroupValue.md) | `from foundry.v1.ontologies.models import AggregationGroupValue` |
**Ontologies** | [AggregationMetricName](docs/v1/Ontologies/models/AggregationMetricName.md) | `from foundry.v1.ontologies.models import AggregationMetricName` |
**Ontologies** | [AggregationMetricResult](docs/v1/Ontologies/models/AggregationMetricResult.md) | `from foundry.v1.ontologies.models import AggregationMetricResult` |
**Ontologies** | [AggregationMetricResultDict](docs/v1/Ontologies/models/AggregationMetricResultDict.md) | `from foundry.v1.ontologies.models import AggregationMetricResultDict` |
**Ontologies** | [AggregationRange](docs/v1/Ontologies/models/AggregationRange.md) | `from foundry.v1.ontologies.models import AggregationRange` |
**Ontologies** | [AggregationRangeDict](docs/v1/Ontologies/models/AggregationRangeDict.md) | `from foundry.v1.ontologies.models import AggregationRangeDict` |
**Ontologies** | [AggregationRangesGrouping](docs/v1/Ontologies/models/AggregationRangesGrouping.md) | `from foundry.v1.ontologies.models import AggregationRangesGrouping` |
**Ontologies** | [AggregationRangesGroupingDict](docs/v1/Ontologies/models/AggregationRangesGroupingDict.md) | `from foundry.v1.ontologies.models import AggregationRangesGroupingDict` |
**Ontologies** | [AllTermsQuery](docs/v1/Ontologies/models/AllTermsQuery.md) | `from foundry.v1.ontologies.models import AllTermsQuery` |
**Ontologies** | [AllTermsQueryDict](docs/v1/Ontologies/models/AllTermsQueryDict.md) | `from foundry.v1.ontologies.models import AllTermsQueryDict` |
**Ontologies** | [AndQuery](docs/v1/Ontologies/models/AndQuery.md) | `from foundry.v1.ontologies.models import AndQuery` |
**Ontologies** | [AndQueryDict](docs/v1/Ontologies/models/AndQueryDict.md) | `from foundry.v1.ontologies.models import AndQueryDict` |
**Ontologies** | [AnyTermQuery](docs/v1/Ontologies/models/AnyTermQuery.md) | `from foundry.v1.ontologies.models import AnyTermQuery` |
**Ontologies** | [AnyTermQueryDict](docs/v1/Ontologies/models/AnyTermQueryDict.md) | `from foundry.v1.ontologies.models import AnyTermQueryDict` |
**Ontologies** | [ApplyActionMode](docs/v1/Ontologies/models/ApplyActionMode.md) | `from foundry.v1.ontologies.models import ApplyActionMode` |
**Ontologies** | [ApplyActionRequest](docs/v1/Ontologies/models/ApplyActionRequest.md) | `from foundry.v1.ontologies.models import ApplyActionRequest` |
**Ontologies** | [ApplyActionRequestDict](docs/v1/Ontologies/models/ApplyActionRequestDict.md) | `from foundry.v1.ontologies.models import ApplyActionRequestDict` |
**Ontologies** | [ApplyActionRequestOptions](docs/v1/Ontologies/models/ApplyActionRequestOptions.md) | `from foundry.v1.ontologies.models import ApplyActionRequestOptions` |
**Ontologies** | [ApplyActionRequestOptionsDict](docs/v1/Ontologies/models/ApplyActionRequestOptionsDict.md) | `from foundry.v1.ontologies.models import ApplyActionRequestOptionsDict` |
**Ontologies** | [ApplyActionResponse](docs/v1/Ontologies/models/ApplyActionResponse.md) | `from foundry.v1.ontologies.models import ApplyActionResponse` |
**Ontologies** | [ApplyActionResponseDict](docs/v1/Ontologies/models/ApplyActionResponseDict.md) | `from foundry.v1.ontologies.models import ApplyActionResponseDict` |
**Ontologies** | [ApproximateDistinctAggregation](docs/v1/Ontologies/models/ApproximateDistinctAggregation.md) | `from foundry.v1.ontologies.models import ApproximateDistinctAggregation` |
**Ontologies** | [ApproximateDistinctAggregationDict](docs/v1/Ontologies/models/ApproximateDistinctAggregationDict.md) | `from foundry.v1.ontologies.models import ApproximateDistinctAggregationDict` |
**Ontologies** | [ArraySizeConstraint](docs/v1/Ontologies/models/ArraySizeConstraint.md) | `from foundry.v1.ontologies.models import ArraySizeConstraint` |
**Ontologies** | [ArraySizeConstraintDict](docs/v1/Ontologies/models/ArraySizeConstraintDict.md) | `from foundry.v1.ontologies.models import ArraySizeConstraintDict` |
**Ontologies** | [ArtifactRepositoryRid](docs/v1/Ontologies/models/ArtifactRepositoryRid.md) | `from foundry.v1.ontologies.models import ArtifactRepositoryRid` |
**Ontologies** | [AttachmentRid](docs/v1/Ontologies/models/AttachmentRid.md) | `from foundry.v1.ontologies.models import AttachmentRid` |
**Ontologies** | [AvgAggregation](docs/v1/Ontologies/models/AvgAggregation.md) | `from foundry.v1.ontologies.models import AvgAggregation` |
**Ontologies** | [AvgAggregationDict](docs/v1/Ontologies/models/AvgAggregationDict.md) | `from foundry.v1.ontologies.models import AvgAggregationDict` |
**Ontologies** | [BatchApplyActionResponse](docs/v1/Ontologies/models/BatchApplyActionResponse.md) | `from foundry.v1.ontologies.models import BatchApplyActionResponse` |
**Ontologies** | [BatchApplyActionResponseDict](docs/v1/Ontologies/models/BatchApplyActionResponseDict.md) | `from foundry.v1.ontologies.models import BatchApplyActionResponseDict` |
**Ontologies** | [ContainsQuery](docs/v1/Ontologies/models/ContainsQuery.md) | `from foundry.v1.ontologies.models import ContainsQuery` |
**Ontologies** | [ContainsQueryDict](docs/v1/Ontologies/models/ContainsQueryDict.md) | `from foundry.v1.ontologies.models import ContainsQueryDict` |
**Ontologies** | [CountAggregation](docs/v1/Ontologies/models/CountAggregation.md) | `from foundry.v1.ontologies.models import CountAggregation` |
**Ontologies** | [CountAggregationDict](docs/v1/Ontologies/models/CountAggregationDict.md) | `from foundry.v1.ontologies.models import CountAggregationDict` |
**Ontologies** | [CreateInterfaceObjectRule](docs/v1/Ontologies/models/CreateInterfaceObjectRule.md) | `from foundry.v1.ontologies.models import CreateInterfaceObjectRule` |
**Ontologies** | [CreateInterfaceObjectRuleDict](docs/v1/Ontologies/models/CreateInterfaceObjectRuleDict.md) | `from foundry.v1.ontologies.models import CreateInterfaceObjectRuleDict` |
**Ontologies** | [CreateLinkRule](docs/v1/Ontologies/models/CreateLinkRule.md) | `from foundry.v1.ontologies.models import CreateLinkRule` |
**Ontologies** | [CreateLinkRuleDict](docs/v1/Ontologies/models/CreateLinkRuleDict.md) | `from foundry.v1.ontologies.models import CreateLinkRuleDict` |
**Ontologies** | [CreateObjectRule](docs/v1/Ontologies/models/CreateObjectRule.md) | `from foundry.v1.ontologies.models import CreateObjectRule` |
**Ontologies** | [CreateObjectRuleDict](docs/v1/Ontologies/models/CreateObjectRuleDict.md) | `from foundry.v1.ontologies.models import CreateObjectRuleDict` |
**Ontologies** | [DataValue](docs/v1/Ontologies/models/DataValue.md) | `from foundry.v1.ontologies.models import DataValue` |
**Ontologies** | [DeleteInterfaceObjectRule](docs/v1/Ontologies/models/DeleteInterfaceObjectRule.md) | `from foundry.v1.ontologies.models import DeleteInterfaceObjectRule` |
**Ontologies** | [DeleteInterfaceObjectRuleDict](docs/v1/Ontologies/models/DeleteInterfaceObjectRuleDict.md) | `from foundry.v1.ontologies.models import DeleteInterfaceObjectRuleDict` |
**Ontologies** | [DeleteLinkRule](docs/v1/Ontologies/models/DeleteLinkRule.md) | `from foundry.v1.ontologies.models import DeleteLinkRule` |
**Ontologies** | [DeleteLinkRuleDict](docs/v1/Ontologies/models/DeleteLinkRuleDict.md) | `from foundry.v1.ontologies.models import DeleteLinkRuleDict` |
**Ontologies** | [DeleteObjectRule](docs/v1/Ontologies/models/DeleteObjectRule.md) | `from foundry.v1.ontologies.models import DeleteObjectRule` |
**Ontologies** | [DeleteObjectRuleDict](docs/v1/Ontologies/models/DeleteObjectRuleDict.md) | `from foundry.v1.ontologies.models import DeleteObjectRuleDict` |
**Ontologies** | [DerivedPropertyApiName](docs/v1/Ontologies/models/DerivedPropertyApiName.md) | `from foundry.v1.ontologies.models import DerivedPropertyApiName` |
**Ontologies** | [Duration](docs/v1/Ontologies/models/Duration.md) | `from foundry.v1.ontologies.models import Duration` |
**Ontologies** | [EqualsQuery](docs/v1/Ontologies/models/EqualsQuery.md) | `from foundry.v1.ontologies.models import EqualsQuery` |
**Ontologies** | [EqualsQueryDict](docs/v1/Ontologies/models/EqualsQueryDict.md) | `from foundry.v1.ontologies.models import EqualsQueryDict` |
**Ontologies** | [ExecuteQueryResponse](docs/v1/Ontologies/models/ExecuteQueryResponse.md) | `from foundry.v1.ontologies.models import ExecuteQueryResponse` |
**Ontologies** | [ExecuteQueryResponseDict](docs/v1/Ontologies/models/ExecuteQueryResponseDict.md) | `from foundry.v1.ontologies.models import ExecuteQueryResponseDict` |
**Ontologies** | [FieldNameV1](docs/v1/Ontologies/models/FieldNameV1.md) | `from foundry.v1.ontologies.models import FieldNameV1` |
**Ontologies** | [FilterValue](docs/v1/Ontologies/models/FilterValue.md) | `from foundry.v1.ontologies.models import FilterValue` |
**Ontologies** | [FunctionRid](docs/v1/Ontologies/models/FunctionRid.md) | `from foundry.v1.ontologies.models import FunctionRid` |
**Ontologies** | [FunctionVersion](docs/v1/Ontologies/models/FunctionVersion.md) | `from foundry.v1.ontologies.models import FunctionVersion` |
**Ontologies** | [Fuzzy](docs/v1/Ontologies/models/Fuzzy.md) | `from foundry.v1.ontologies.models import Fuzzy` |
**Ontologies** | [GroupMemberConstraint](docs/v1/Ontologies/models/GroupMemberConstraint.md) | `from foundry.v1.ontologies.models import GroupMemberConstraint` |
**Ontologies** | [GroupMemberConstraintDict](docs/v1/Ontologies/models/GroupMemberConstraintDict.md) | `from foundry.v1.ontologies.models import GroupMemberConstraintDict` |
**Ontologies** | [GteQuery](docs/v1/Ontologies/models/GteQuery.md) | `from foundry.v1.ontologies.models import GteQuery` |
**Ontologies** | [GteQueryDict](docs/v1/Ontologies/models/GteQueryDict.md) | `from foundry.v1.ontologies.models import GteQueryDict` |
**Ontologies** | [GtQuery](docs/v1/Ontologies/models/GtQuery.md) | `from foundry.v1.ontologies.models import GtQuery` |
**Ontologies** | [GtQueryDict](docs/v1/Ontologies/models/GtQueryDict.md) | `from foundry.v1.ontologies.models import GtQueryDict` |
**Ontologies** | [InterfaceTypeApiName](docs/v1/Ontologies/models/InterfaceTypeApiName.md) | `from foundry.v1.ontologies.models import InterfaceTypeApiName` |
**Ontologies** | [InterfaceTypeRid](docs/v1/Ontologies/models/InterfaceTypeRid.md) | `from foundry.v1.ontologies.models import InterfaceTypeRid` |
**Ontologies** | [IsNullQuery](docs/v1/Ontologies/models/IsNullQuery.md) | `from foundry.v1.ontologies.models import IsNullQuery` |
**Ontologies** | [IsNullQueryDict](docs/v1/Ontologies/models/IsNullQueryDict.md) | `from foundry.v1.ontologies.models import IsNullQueryDict` |
**Ontologies** | [LinkTypeApiName](docs/v1/Ontologies/models/LinkTypeApiName.md) | `from foundry.v1.ontologies.models import LinkTypeApiName` |
**Ontologies** | [LinkTypeSide](docs/v1/Ontologies/models/LinkTypeSide.md) | `from foundry.v1.ontologies.models import LinkTypeSide` |
**Ontologies** | [LinkTypeSideCardinality](docs/v1/Ontologies/models/LinkTypeSideCardinality.md) | `from foundry.v1.ontologies.models import LinkTypeSideCardinality` |
**Ontologies** | [LinkTypeSideDict](docs/v1/Ontologies/models/LinkTypeSideDict.md) | `from foundry.v1.ontologies.models import LinkTypeSideDict` |
**Ontologies** | [ListActionTypesResponse](docs/v1/Ontologies/models/ListActionTypesResponse.md) | `from foundry.v1.ontologies.models import ListActionTypesResponse` |
**Ontologies** | [ListActionTypesResponseDict](docs/v1/Ontologies/models/ListActionTypesResponseDict.md) | `from foundry.v1.ontologies.models import ListActionTypesResponseDict` |
**Ontologies** | [ListLinkedObjectsResponse](docs/v1/Ontologies/models/ListLinkedObjectsResponse.md) | `from foundry.v1.ontologies.models import ListLinkedObjectsResponse` |
**Ontologies** | [ListLinkedObjectsResponseDict](docs/v1/Ontologies/models/ListLinkedObjectsResponseDict.md) | `from foundry.v1.ontologies.models import ListLinkedObjectsResponseDict` |
**Ontologies** | [ListObjectsResponse](docs/v1/Ontologies/models/ListObjectsResponse.md) | `from foundry.v1.ontologies.models import ListObjectsResponse` |
**Ontologies** | [ListObjectsResponseDict](docs/v1/Ontologies/models/ListObjectsResponseDict.md) | `from foundry.v1.ontologies.models import ListObjectsResponseDict` |
**Ontologies** | [ListObjectTypesResponse](docs/v1/Ontologies/models/ListObjectTypesResponse.md) | `from foundry.v1.ontologies.models import ListObjectTypesResponse` |
**Ontologies** | [ListObjectTypesResponseDict](docs/v1/Ontologies/models/ListObjectTypesResponseDict.md) | `from foundry.v1.ontologies.models import ListObjectTypesResponseDict` |
**Ontologies** | [ListOntologiesResponse](docs/v1/Ontologies/models/ListOntologiesResponse.md) | `from foundry.v1.ontologies.models import ListOntologiesResponse` |
**Ontologies** | [ListOntologiesResponseDict](docs/v1/Ontologies/models/ListOntologiesResponseDict.md) | `from foundry.v1.ontologies.models import ListOntologiesResponseDict` |
**Ontologies** | [ListOutgoingLinkTypesResponse](docs/v1/Ontologies/models/ListOutgoingLinkTypesResponse.md) | `from foundry.v1.ontologies.models import ListOutgoingLinkTypesResponse` |
**Ontologies** | [ListOutgoingLinkTypesResponseDict](docs/v1/Ontologies/models/ListOutgoingLinkTypesResponseDict.md) | `from foundry.v1.ontologies.models import ListOutgoingLinkTypesResponseDict` |
**Ontologies** | [ListQueryTypesResponse](docs/v1/Ontologies/models/ListQueryTypesResponse.md) | `from foundry.v1.ontologies.models import ListQueryTypesResponse` |
**Ontologies** | [ListQueryTypesResponseDict](docs/v1/Ontologies/models/ListQueryTypesResponseDict.md) | `from foundry.v1.ontologies.models import ListQueryTypesResponseDict` |
**Ontologies** | [LogicRule](docs/v1/Ontologies/models/LogicRule.md) | `from foundry.v1.ontologies.models import LogicRule` |
**Ontologies** | [LogicRuleDict](docs/v1/Ontologies/models/LogicRuleDict.md) | `from foundry.v1.ontologies.models import LogicRuleDict` |
**Ontologies** | [LteQuery](docs/v1/Ontologies/models/LteQuery.md) | `from foundry.v1.ontologies.models import LteQuery` |
**Ontologies** | [LteQueryDict](docs/v1/Ontologies/models/LteQueryDict.md) | `from foundry.v1.ontologies.models import LteQueryDict` |
**Ontologies** | [LtQuery](docs/v1/Ontologies/models/LtQuery.md) | `from foundry.v1.ontologies.models import LtQuery` |
**Ontologies** | [LtQueryDict](docs/v1/Ontologies/models/LtQueryDict.md) | `from foundry.v1.ontologies.models import LtQueryDict` |
**Ontologies** | [MaxAggregation](docs/v1/Ontologies/models/MaxAggregation.md) | `from foundry.v1.ontologies.models import MaxAggregation` |
**Ontologies** | [MaxAggregationDict](docs/v1/Ontologies/models/MaxAggregationDict.md) | `from foundry.v1.ontologies.models import MaxAggregationDict` |
**Ontologies** | [MinAggregation](docs/v1/Ontologies/models/MinAggregation.md) | `from foundry.v1.ontologies.models import MinAggregation` |
**Ontologies** | [MinAggregationDict](docs/v1/Ontologies/models/MinAggregationDict.md) | `from foundry.v1.ontologies.models import MinAggregationDict` |
**Ontologies** | [ModifyInterfaceObjectRule](docs/v1/Ontologies/models/ModifyInterfaceObjectRule.md) | `from foundry.v1.ontologies.models import ModifyInterfaceObjectRule` |
**Ontologies** | [ModifyInterfaceObjectRuleDict](docs/v1/Ontologies/models/ModifyInterfaceObjectRuleDict.md) | `from foundry.v1.ontologies.models import ModifyInterfaceObjectRuleDict` |
**Ontologies** | [ModifyObjectRule](docs/v1/Ontologies/models/ModifyObjectRule.md) | `from foundry.v1.ontologies.models import ModifyObjectRule` |
**Ontologies** | [ModifyObjectRuleDict](docs/v1/Ontologies/models/ModifyObjectRuleDict.md) | `from foundry.v1.ontologies.models import ModifyObjectRuleDict` |
**Ontologies** | [NotQuery](docs/v1/Ontologies/models/NotQuery.md) | `from foundry.v1.ontologies.models import NotQuery` |
**Ontologies** | [NotQueryDict](docs/v1/Ontologies/models/NotQueryDict.md) | `from foundry.v1.ontologies.models import NotQueryDict` |
**Ontologies** | [ObjectPropertyValueConstraint](docs/v1/Ontologies/models/ObjectPropertyValueConstraint.md) | `from foundry.v1.ontologies.models import ObjectPropertyValueConstraint` |
**Ontologies** | [ObjectPropertyValueConstraintDict](docs/v1/Ontologies/models/ObjectPropertyValueConstraintDict.md) | `from foundry.v1.ontologies.models import ObjectPropertyValueConstraintDict` |
**Ontologies** | [ObjectQueryResultConstraint](docs/v1/Ontologies/models/ObjectQueryResultConstraint.md) | `from foundry.v1.ontologies.models import ObjectQueryResultConstraint` |
**Ontologies** | [ObjectQueryResultConstraintDict](docs/v1/Ontologies/models/ObjectQueryResultConstraintDict.md) | `from foundry.v1.ontologies.models import ObjectQueryResultConstraintDict` |
**Ontologies** | [ObjectRid](docs/v1/Ontologies/models/ObjectRid.md) | `from foundry.v1.ontologies.models import ObjectRid` |
**Ontologies** | [ObjectSetRid](docs/v1/Ontologies/models/ObjectSetRid.md) | `from foundry.v1.ontologies.models import ObjectSetRid` |
**Ontologies** | [ObjectType](docs/v1/Ontologies/models/ObjectType.md) | `from foundry.v1.ontologies.models import ObjectType` |
**Ontologies** | [ObjectTypeApiName](docs/v1/Ontologies/models/ObjectTypeApiName.md) | `from foundry.v1.ontologies.models import ObjectTypeApiName` |
**Ontologies** | [ObjectTypeDict](docs/v1/Ontologies/models/ObjectTypeDict.md) | `from foundry.v1.ontologies.models import ObjectTypeDict` |
**Ontologies** | [ObjectTypeRid](docs/v1/Ontologies/models/ObjectTypeRid.md) | `from foundry.v1.ontologies.models import ObjectTypeRid` |
**Ontologies** | [ObjectTypeVisibility](docs/v1/Ontologies/models/ObjectTypeVisibility.md) | `from foundry.v1.ontologies.models import ObjectTypeVisibility` |
**Ontologies** | [OneOfConstraint](docs/v1/Ontologies/models/OneOfConstraint.md) | `from foundry.v1.ontologies.models import OneOfConstraint` |
**Ontologies** | [OneOfConstraintDict](docs/v1/Ontologies/models/OneOfConstraintDict.md) | `from foundry.v1.ontologies.models import OneOfConstraintDict` |
**Ontologies** | [Ontology](docs/v1/Ontologies/models/Ontology.md) | `from foundry.v1.ontologies.models import Ontology` |
**Ontologies** | [OntologyApiName](docs/v1/Ontologies/models/OntologyApiName.md) | `from foundry.v1.ontologies.models import OntologyApiName` |
**Ontologies** | [OntologyArrayType](docs/v1/Ontologies/models/OntologyArrayType.md) | `from foundry.v1.ontologies.models import OntologyArrayType` |
**Ontologies** | [OntologyArrayTypeDict](docs/v1/Ontologies/models/OntologyArrayTypeDict.md) | `from foundry.v1.ontologies.models import OntologyArrayTypeDict` |
**Ontologies** | [OntologyDataType](docs/v1/Ontologies/models/OntologyDataType.md) | `from foundry.v1.ontologies.models import OntologyDataType` |
**Ontologies** | [OntologyDataTypeDict](docs/v1/Ontologies/models/OntologyDataTypeDict.md) | `from foundry.v1.ontologies.models import OntologyDataTypeDict` |
**Ontologies** | [OntologyDict](docs/v1/Ontologies/models/OntologyDict.md) | `from foundry.v1.ontologies.models import OntologyDict` |
**Ontologies** | [OntologyMapType](docs/v1/Ontologies/models/OntologyMapType.md) | `from foundry.v1.ontologies.models import OntologyMapType` |
**Ontologies** | [OntologyMapTypeDict](docs/v1/Ontologies/models/OntologyMapTypeDict.md) | `from foundry.v1.ontologies.models import OntologyMapTypeDict` |
**Ontologies** | [OntologyObject](docs/v1/Ontologies/models/OntologyObject.md) | `from foundry.v1.ontologies.models import OntologyObject` |
**Ontologies** | [OntologyObjectDict](docs/v1/Ontologies/models/OntologyObjectDict.md) | `from foundry.v1.ontologies.models import OntologyObjectDict` |
**Ontologies** | [OntologyObjectSetType](docs/v1/Ontologies/models/OntologyObjectSetType.md) | `from foundry.v1.ontologies.models import OntologyObjectSetType` |
**Ontologies** | [OntologyObjectSetTypeDict](docs/v1/Ontologies/models/OntologyObjectSetTypeDict.md) | `from foundry.v1.ontologies.models import OntologyObjectSetTypeDict` |
**Ontologies** | [OntologyObjectType](docs/v1/Ontologies/models/OntologyObjectType.md) | `from foundry.v1.ontologies.models import OntologyObjectType` |
**Ontologies** | [OntologyObjectTypeDict](docs/v1/Ontologies/models/OntologyObjectTypeDict.md) | `from foundry.v1.ontologies.models import OntologyObjectTypeDict` |
**Ontologies** | [OntologyRid](docs/v1/Ontologies/models/OntologyRid.md) | `from foundry.v1.ontologies.models import OntologyRid` |
**Ontologies** | [OntologySetType](docs/v1/Ontologies/models/OntologySetType.md) | `from foundry.v1.ontologies.models import OntologySetType` |
**Ontologies** | [OntologySetTypeDict](docs/v1/Ontologies/models/OntologySetTypeDict.md) | `from foundry.v1.ontologies.models import OntologySetTypeDict` |
**Ontologies** | [OntologyStructField](docs/v1/Ontologies/models/OntologyStructField.md) | `from foundry.v1.ontologies.models import OntologyStructField` |
**Ontologies** | [OntologyStructFieldDict](docs/v1/Ontologies/models/OntologyStructFieldDict.md) | `from foundry.v1.ontologies.models import OntologyStructFieldDict` |
**Ontologies** | [OntologyStructType](docs/v1/Ontologies/models/OntologyStructType.md) | `from foundry.v1.ontologies.models import OntologyStructType` |
**Ontologies** | [OntologyStructTypeDict](docs/v1/Ontologies/models/OntologyStructTypeDict.md) | `from foundry.v1.ontologies.models import OntologyStructTypeDict` |
**Ontologies** | [OrderBy](docs/v1/Ontologies/models/OrderBy.md) | `from foundry.v1.ontologies.models import OrderBy` |
**Ontologies** | [OrQuery](docs/v1/Ontologies/models/OrQuery.md) | `from foundry.v1.ontologies.models import OrQuery` |
**Ontologies** | [OrQueryDict](docs/v1/Ontologies/models/OrQueryDict.md) | `from foundry.v1.ontologies.models import OrQueryDict` |
**Ontologies** | [Parameter](docs/v1/Ontologies/models/Parameter.md) | `from foundry.v1.ontologies.models import Parameter` |
**Ontologies** | [ParameterDict](docs/v1/Ontologies/models/ParameterDict.md) | `from foundry.v1.ontologies.models import ParameterDict` |
**Ontologies** | [ParameterEvaluatedConstraint](docs/v1/Ontologies/models/ParameterEvaluatedConstraint.md) | `from foundry.v1.ontologies.models import ParameterEvaluatedConstraint` |
**Ontologies** | [ParameterEvaluatedConstraintDict](docs/v1/Ontologies/models/ParameterEvaluatedConstraintDict.md) | `from foundry.v1.ontologies.models import ParameterEvaluatedConstraintDict` |
**Ontologies** | [ParameterEvaluationResult](docs/v1/Ontologies/models/ParameterEvaluationResult.md) | `from foundry.v1.ontologies.models import ParameterEvaluationResult` |
**Ontologies** | [ParameterEvaluationResultDict](docs/v1/Ontologies/models/ParameterEvaluationResultDict.md) | `from foundry.v1.ontologies.models import ParameterEvaluationResultDict` |
**Ontologies** | [ParameterId](docs/v1/Ontologies/models/ParameterId.md) | `from foundry.v1.ontologies.models import ParameterId` |
**Ontologies** | [ParameterOption](docs/v1/Ontologies/models/ParameterOption.md) | `from foundry.v1.ontologies.models import ParameterOption` |
**Ontologies** | [ParameterOptionDict](docs/v1/Ontologies/models/ParameterOptionDict.md) | `from foundry.v1.ontologies.models import ParameterOptionDict` |
**Ontologies** | [PhraseQuery](docs/v1/Ontologies/models/PhraseQuery.md) | `from foundry.v1.ontologies.models import PhraseQuery` |
**Ontologies** | [PhraseQueryDict](docs/v1/Ontologies/models/PhraseQueryDict.md) | `from foundry.v1.ontologies.models import PhraseQueryDict` |
**Ontologies** | [PrefixQuery](docs/v1/Ontologies/models/PrefixQuery.md) | `from foundry.v1.ontologies.models import PrefixQuery` |
**Ontologies** | [PrefixQueryDict](docs/v1/Ontologies/models/PrefixQueryDict.md) | `from foundry.v1.ontologies.models import PrefixQueryDict` |
**Ontologies** | [PrimaryKeyValue](docs/v1/Ontologies/models/PrimaryKeyValue.md) | `from foundry.v1.ontologies.models import PrimaryKeyValue` |
**Ontologies** | [Property](docs/v1/Ontologies/models/Property.md) | `from foundry.v1.ontologies.models import Property` |
**Ontologies** | [PropertyApiName](docs/v1/Ontologies/models/PropertyApiName.md) | `from foundry.v1.ontologies.models import PropertyApiName` |
**Ontologies** | [PropertyDict](docs/v1/Ontologies/models/PropertyDict.md) | `from foundry.v1.ontologies.models import PropertyDict` |
**Ontologies** | [PropertyFilter](docs/v1/Ontologies/models/PropertyFilter.md) | `from foundry.v1.ontologies.models import PropertyFilter` |
**Ontologies** | [PropertyId](docs/v1/Ontologies/models/PropertyId.md) | `from foundry.v1.ontologies.models import PropertyId` |
**Ontologies** | [PropertyValue](docs/v1/Ontologies/models/PropertyValue.md) | `from foundry.v1.ontologies.models import PropertyValue` |
**Ontologies** | [PropertyValueEscapedString](docs/v1/Ontologies/models/PropertyValueEscapedString.md) | `from foundry.v1.ontologies.models import PropertyValueEscapedString` |
**Ontologies** | [QueryAggregationKeyTypeDict](docs/v1/Ontologies/models/QueryAggregationKeyTypeDict.md) | `from foundry.v1.ontologies.models import QueryAggregationKeyTypeDict` |
**Ontologies** | [QueryAggregationRangeSubTypeDict](docs/v1/Ontologies/models/QueryAggregationRangeSubTypeDict.md) | `from foundry.v1.ontologies.models import QueryAggregationRangeSubTypeDict` |
**Ontologies** | [QueryAggregationRangeTypeDict](docs/v1/Ontologies/models/QueryAggregationRangeTypeDict.md) | `from foundry.v1.ontologies.models import QueryAggregationRangeTypeDict` |
**Ontologies** | [QueryAggregationValueTypeDict](docs/v1/Ontologies/models/QueryAggregationValueTypeDict.md) | `from foundry.v1.ontologies.models import QueryAggregationValueTypeDict` |
**Ontologies** | [QueryApiName](docs/v1/Ontologies/models/QueryApiName.md) | `from foundry.v1.ontologies.models import QueryApiName` |
**Ontologies** | [QueryArrayTypeDict](docs/v1/Ontologies/models/QueryArrayTypeDict.md) | `from foundry.v1.ontologies.models import QueryArrayTypeDict` |
**Ontologies** | [QueryDataTypeDict](docs/v1/Ontologies/models/QueryDataTypeDict.md) | `from foundry.v1.ontologies.models import QueryDataTypeDict` |
**Ontologies** | [QueryRuntimeErrorParameter](docs/v1/Ontologies/models/QueryRuntimeErrorParameter.md) | `from foundry.v1.ontologies.models import QueryRuntimeErrorParameter` |
**Ontologies** | [QuerySetTypeDict](docs/v1/Ontologies/models/QuerySetTypeDict.md) | `from foundry.v1.ontologies.models import QuerySetTypeDict` |
**Ontologies** | [QueryStructFieldDict](docs/v1/Ontologies/models/QueryStructFieldDict.md) | `from foundry.v1.ontologies.models import QueryStructFieldDict` |
**Ontologies** | [QueryStructTypeDict](docs/v1/Ontologies/models/QueryStructTypeDict.md) | `from foundry.v1.ontologies.models import QueryStructTypeDict` |
**Ontologies** | [QueryType](docs/v1/Ontologies/models/QueryType.md) | `from foundry.v1.ontologies.models import QueryType` |
**Ontologies** | [QueryTypeDict](docs/v1/Ontologies/models/QueryTypeDict.md) | `from foundry.v1.ontologies.models import QueryTypeDict` |
**Ontologies** | [QueryUnionTypeDict](docs/v1/Ontologies/models/QueryUnionTypeDict.md) | `from foundry.v1.ontologies.models import QueryUnionTypeDict` |
**Ontologies** | [RangeConstraint](docs/v1/Ontologies/models/RangeConstraint.md) | `from foundry.v1.ontologies.models import RangeConstraint` |
**Ontologies** | [RangeConstraintDict](docs/v1/Ontologies/models/RangeConstraintDict.md) | `from foundry.v1.ontologies.models import RangeConstraintDict` |
**Ontologies** | [ReturnEditsMode](docs/v1/Ontologies/models/ReturnEditsMode.md) | `from foundry.v1.ontologies.models import ReturnEditsMode` |
**Ontologies** | [SdkPackageName](docs/v1/Ontologies/models/SdkPackageName.md) | `from foundry.v1.ontologies.models import SdkPackageName` |
**Ontologies** | [SearchJsonQuery](docs/v1/Ontologies/models/SearchJsonQuery.md) | `from foundry.v1.ontologies.models import SearchJsonQuery` |
**Ontologies** | [SearchJsonQueryDict](docs/v1/Ontologies/models/SearchJsonQueryDict.md) | `from foundry.v1.ontologies.models import SearchJsonQueryDict` |
**Ontologies** | [SearchObjectsResponse](docs/v1/Ontologies/models/SearchObjectsResponse.md) | `from foundry.v1.ontologies.models import SearchObjectsResponse` |
**Ontologies** | [SearchObjectsResponseDict](docs/v1/Ontologies/models/SearchObjectsResponseDict.md) | `from foundry.v1.ontologies.models import SearchObjectsResponseDict` |
**Ontologies** | [SearchOrderBy](docs/v1/Ontologies/models/SearchOrderBy.md) | `from foundry.v1.ontologies.models import SearchOrderBy` |
**Ontologies** | [SearchOrderByDict](docs/v1/Ontologies/models/SearchOrderByDict.md) | `from foundry.v1.ontologies.models import SearchOrderByDict` |
**Ontologies** | [SearchOrderByType](docs/v1/Ontologies/models/SearchOrderByType.md) | `from foundry.v1.ontologies.models import SearchOrderByType` |
**Ontologies** | [SearchOrdering](docs/v1/Ontologies/models/SearchOrdering.md) | `from foundry.v1.ontologies.models import SearchOrdering` |
**Ontologies** | [SearchOrderingDict](docs/v1/Ontologies/models/SearchOrderingDict.md) | `from foundry.v1.ontologies.models import SearchOrderingDict` |
**Ontologies** | [SelectedPropertyApiName](docs/v1/Ontologies/models/SelectedPropertyApiName.md) | `from foundry.v1.ontologies.models import SelectedPropertyApiName` |
**Ontologies** | [SharedPropertyTypeApiName](docs/v1/Ontologies/models/SharedPropertyTypeApiName.md) | `from foundry.v1.ontologies.models import SharedPropertyTypeApiName` |
**Ontologies** | [SharedPropertyTypeRid](docs/v1/Ontologies/models/SharedPropertyTypeRid.md) | `from foundry.v1.ontologies.models import SharedPropertyTypeRid` |
**Ontologies** | [StringLengthConstraint](docs/v1/Ontologies/models/StringLengthConstraint.md) | `from foundry.v1.ontologies.models import StringLengthConstraint` |
**Ontologies** | [StringLengthConstraintDict](docs/v1/Ontologies/models/StringLengthConstraintDict.md) | `from foundry.v1.ontologies.models import StringLengthConstraintDict` |
**Ontologies** | [StringRegexMatchConstraint](docs/v1/Ontologies/models/StringRegexMatchConstraint.md) | `from foundry.v1.ontologies.models import StringRegexMatchConstraint` |
**Ontologies** | [StringRegexMatchConstraintDict](docs/v1/Ontologies/models/StringRegexMatchConstraintDict.md) | `from foundry.v1.ontologies.models import StringRegexMatchConstraintDict` |
**Ontologies** | [SubmissionCriteriaEvaluation](docs/v1/Ontologies/models/SubmissionCriteriaEvaluation.md) | `from foundry.v1.ontologies.models import SubmissionCriteriaEvaluation` |
**Ontologies** | [SubmissionCriteriaEvaluationDict](docs/v1/Ontologies/models/SubmissionCriteriaEvaluationDict.md) | `from foundry.v1.ontologies.models import SubmissionCriteriaEvaluationDict` |
**Ontologies** | [SumAggregation](docs/v1/Ontologies/models/SumAggregation.md) | `from foundry.v1.ontologies.models import SumAggregation` |
**Ontologies** | [SumAggregationDict](docs/v1/Ontologies/models/SumAggregationDict.md) | `from foundry.v1.ontologies.models import SumAggregationDict` |
**Ontologies** | [ThreeDimensionalAggregationDict](docs/v1/Ontologies/models/ThreeDimensionalAggregationDict.md) | `from foundry.v1.ontologies.models import ThreeDimensionalAggregationDict` |
**Ontologies** | [TwoDimensionalAggregationDict](docs/v1/Ontologies/models/TwoDimensionalAggregationDict.md) | `from foundry.v1.ontologies.models import TwoDimensionalAggregationDict` |
**Ontologies** | [UnevaluableConstraint](docs/v1/Ontologies/models/UnevaluableConstraint.md) | `from foundry.v1.ontologies.models import UnevaluableConstraint` |
**Ontologies** | [UnevaluableConstraintDict](docs/v1/Ontologies/models/UnevaluableConstraintDict.md) | `from foundry.v1.ontologies.models import UnevaluableConstraintDict` |
**Ontologies** | [ValidateActionResponse](docs/v1/Ontologies/models/ValidateActionResponse.md) | `from foundry.v1.ontologies.models import ValidateActionResponse` |
**Ontologies** | [ValidateActionResponseDict](docs/v1/Ontologies/models/ValidateActionResponseDict.md) | `from foundry.v1.ontologies.models import ValidateActionResponseDict` |
**Ontologies** | [ValidationResult](docs/v1/Ontologies/models/ValidationResult.md) | `from foundry.v1.ontologies.models import ValidationResult` |
**Ontologies** | [ValueType](docs/v1/Ontologies/models/ValueType.md) | `from foundry.v1.ontologies.models import ValueType` |


## Contributions

This repository does not accept code contributions.

If you have any questions, concerns, or ideas for improvements, create an
issue with Palantir Support.

## License
This project is made available under the [Apache 2.0 License](/LICENSE).
