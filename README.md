<p align="right">
<a href="https://autorelease.general.dmz.palantir.tech/palantir/foundry-platform-python"><img src="https://img.shields.io/badge/Perform%20an-Autorelease-success.svg" alt="Autorelease"></a>
</p>

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
↳ [Data Frames](#data-frames): Learn how to work with tabular data using data frame libraries  
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

All RPC exceptions will have the following properties. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors) for details about the Foundry error information.

| Property          | Type                   | Description                                                                                                                                                       |
| ----------------- | -----------------------| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name              | str                    | The Palantir error name. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors).        |
| error_instance_id | str                    | The Palantir error instance ID. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors). |
| parameters        | Dict[str, Any]         | The Palantir error parameters. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors).  |
| error_code        | str                    | The Palantir error code. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors).        |
| error_description | str                    | The Palantir error description. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors). |

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
| RateLimitError             | Yes             | The request was rate limited. Reduce your request rate and retry your request shortly.                                            |
| ServiceUnavailable         | Yes             | The service is temporarily unavailable. Retry your request shortly.                                                               |
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

<a id="data-frames"></a>
## Data Frames

This SDK supports working with tabular data using popular Python data frame libraries. When an API endpoint returns data in Arrow IPC or Parquet format, the response is wrapped in a `TableResponse` class that provides methods to convert to various data frame formats:

- `to_pyarrow()`: Converts to a PyArrow Table
- `to_pandas()`: Converts to a Pandas DataFrame
- `to_polars()`: Converts to a Polars DataFrame
- `to_duckdb()`: Converts to a DuckDB relation

This allows you to seamlessly work with Foundry tabular data using your preferred data analysis library.

### Example: Working with Data Frames

```python
# Read tabular data in Arrow format
table_data = client.datasets.Dataset.read_table(dataset_rid, format=format, branch_name=branch_name, columns=columns, end_transaction_rid=end_transaction_rid, row_limit=row_limit, start_transaction_rid=start_transaction_rid)

# Convert to pandas DataFrame for data analysis
pandas_df = table_data.to_pandas()

# Perform data analysis operations
summary = pandas_df.describe()
filtered_data = pandas_df[pandas_df["value"] > 100]

# Or use Polars for high-performance data operations
import polars as pl
polars_df = table_data.to_polars()
result = polars_df.filter(pl.col("value") > 100).group_by("category").agg(pl.sum("amount"))

# Or use DuckDB for SQL-based analysis
import duckdb
duckdb_relation = table_data.to_duckdb()
result = duckdb_relation.query("SELECT category, SUM(amount) FROM duckdb_relation WHERE value > 100 GROUP BY category")
```

You can inclue the extra dependencies using:

```bash
# For pyarrow support
pip install foundry-platform-sdk[pyarrow]

# For pandas support
pip install foundry-platform-sdk[pandas]

# For polars support
pip install foundry-platform-sdk[polars]

# For duckdb support
pip install foundry-platform-sdk[duckdb]
```

If you attempt to use a conversion method without the required dependency installed, the SDK will provide a helpful error message with installation instructions.

<a id="static-types"></a>
## Static type analysis

### Hashable Models

All model objects in the SDK can be used as dictionary keys or set members. This provides several benefits:

```python
# Example: Using models as dictionary keys
from foundry_sdk import FoundryClient

client = FoundryClient(...)
file1 = client.datasets.Dataset.File.get(dataset_rid="ri.foundry.main.dataset.123", file_path="/data.csv")
file2 = client.datasets.Dataset.File.get(dataset_rid="ri.foundry.main.dataset.123", file_path="/data.csv")

# Models with the same content are equal and have the same hash
assert file1 == file2
assert hash(file1) == hash(file2)

# Use models as dictionary keys
file_metadata = {}
file_metadata[file1] = {"last_modified": "2024-08-09"}

# Can look up using any equivalent object
assert file_metadata[file2] == {"last_modified": "2024-08-09"}
```

**Note:** Models remain mutable for backward compatibility. If you modify a model after using it as a dictionary key,
the system will issue a warning and the model's hash value will be reset. Although allowed, mutating models and using
their hash values is not recommended as it can lead to unexpected behavior when using them in dictionaries or sets.

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
**AipAgents** | Session | [**delete**](docs/v2/AipAgents/Session.md#delete) | **DELETE** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid} |
**AipAgents** | Session | [**get**](docs/v2/AipAgents/Session.md#get) | **GET** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid} |
**AipAgents** | Session | [**list**](docs/v2/AipAgents/Session.md#list) | **GET** /v2/aipAgents/agents/{agentRid}/sessions |
**AipAgents** | Session | [**rag_context**](docs/v2/AipAgents/Session.md#rag_context) | **PUT** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/ragContext |
**AipAgents** | Session | [**streaming_continue**](docs/v2/AipAgents/Session.md#streaming_continue) | **POST** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/streamingContinue |
**AipAgents** | Session | [**update_title**](docs/v2/AipAgents/Session.md#update_title) | **PUT** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/updateTitle |
**AipAgents** | SessionTrace | [**get**](docs/v2/AipAgents/SessionTrace.md#get) | **GET** /v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/sessionTraces/{sessionTraceId} |
**Audit** | LogFile | [**content**](docs/v2/Audit/LogFile.md#content) | **GET** /v2/audit/organizations/{organizationRid}/logFiles/{logFileId}/content |
**Audit** | LogFile | [**list**](docs/v2/Audit/LogFile.md#list) | **GET** /v2/audit/organizations/{organizationRid}/logFiles |
**Checkpoints** | Record | [**get**](docs/v2/Checkpoints/Record.md#get) | **GET** /v2/checkpoints/records/{recordRid} |
**Checkpoints** | Record | [**get_batch**](docs/v2/Checkpoints/Record.md#get_batch) | **POST** /v2/checkpoints/records/getBatch |
**Checkpoints** | Record | [**search**](docs/v2/Checkpoints/Record.md#search) | **POST** /v2/checkpoints/records/search |
**Connectivity** | Connection | [**create**](docs/v2/Connectivity/Connection.md#create) | **POST** /v2/connectivity/connections |
**Connectivity** | Connection | [**get**](docs/v2/Connectivity/Connection.md#get) | **GET** /v2/connectivity/connections/{connectionRid} |
**Connectivity** | Connection | [**get_configuration**](docs/v2/Connectivity/Connection.md#get_configuration) | **GET** /v2/connectivity/connections/{connectionRid}/getConfiguration |
**Connectivity** | Connection | [**get_configuration_batch**](docs/v2/Connectivity/Connection.md#get_configuration_batch) | **POST** /v2/connectivity/connections/getConfigurationBatch |
**Connectivity** | Connection | [**update_export_settings**](docs/v2/Connectivity/Connection.md#update_export_settings) | **POST** /v2/connectivity/connections/{connectionRid}/updateExportSettings |
**Connectivity** | Connection | [**update_secrets**](docs/v2/Connectivity/Connection.md#update_secrets) | **POST** /v2/connectivity/connections/{connectionRid}/updateSecrets |
**Connectivity** | Connection | [**upload_custom_jdbc_drivers**](docs/v2/Connectivity/Connection.md#upload_custom_jdbc_drivers) | **POST** /v2/connectivity/connections/{connectionRid}/uploadCustomJdbcDrivers |
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
**Connectivity** | VirtualTable | [**create**](docs/v2/Connectivity/VirtualTable.md#create) | **POST** /v2/connectivity/connections/{connectionRid}/virtualTables |
**DataHealth** | Check | [**create**](docs/v2/DataHealth/Check.md#create) | **POST** /v2/dataHealth/checks |
**DataHealth** | Check | [**delete**](docs/v2/DataHealth/Check.md#delete) | **DELETE** /v2/dataHealth/checks/{checkRid} |
**DataHealth** | Check | [**get**](docs/v2/DataHealth/Check.md#get) | **GET** /v2/dataHealth/checks/{checkRid} |
**DataHealth** | Check | [**replace**](docs/v2/DataHealth/Check.md#replace) | **PUT** /v2/dataHealth/checks/{checkRid} |
**DataHealth** | CheckReport | [**get**](docs/v2/DataHealth/CheckReport.md#get) | **GET** /v2/dataHealth/checks/{checkRid}/checkReports/{checkReportRid} |
**DataHealth** | CheckReport | [**get_latest**](docs/v2/DataHealth/CheckReport.md#get_latest) | **GET** /v2/dataHealth/checks/{checkRid}/checkReports/getLatest |
**Datasets** | Branch | [**create**](docs/v2/Datasets/Branch.md#create) | **POST** /v2/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**delete**](docs/v2/Datasets/Branch.md#delete) | **DELETE** /v2/datasets/{datasetRid}/branches/{branchName} |
**Datasets** | Branch | [**get**](docs/v2/Datasets/Branch.md#get) | **GET** /v2/datasets/{datasetRid}/branches/{branchName} |
**Datasets** | Branch | [**list**](docs/v2/Datasets/Branch.md#list) | **GET** /v2/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**transactions**](docs/v2/Datasets/Branch.md#transactions) | **GET** /v2/datasets/{datasetRid}/branches/{branchName}/transactions |
**Datasets** | Dataset | [**create**](docs/v2/Datasets/Dataset.md#create) | **POST** /v2/datasets |
**Datasets** | Dataset | [**get**](docs/v2/Datasets/Dataset.md#get) | **GET** /v2/datasets/{datasetRid} |
**Datasets** | Dataset | [**get_health_check_reports**](docs/v2/Datasets/Dataset.md#get_health_check_reports) | **GET** /v2/datasets/{datasetRid}/getHealthCheckReports |
**Datasets** | Dataset | [**get_health_checks**](docs/v2/Datasets/Dataset.md#get_health_checks) | **GET** /v2/datasets/{datasetRid}/getHealthChecks |
**Datasets** | Dataset | [**get_schedules**](docs/v2/Datasets/Dataset.md#get_schedules) | **GET** /v2/datasets/{datasetRid}/getSchedules |
**Datasets** | Dataset | [**get_schema**](docs/v2/Datasets/Dataset.md#get_schema) | **GET** /v2/datasets/{datasetRid}/getSchema |
**Datasets** | Dataset | [**get_schema_batch**](docs/v2/Datasets/Dataset.md#get_schema_batch) | **POST** /v2/datasets/getSchemaBatch |
**Datasets** | Dataset | [**jobs**](docs/v2/Datasets/Dataset.md#jobs) | **POST** /v2/datasets/{datasetRid}/jobs |
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
**Filesystem** | Folder | [**get_batch**](docs/v2/Filesystem/Folder.md#get_batch) | **POST** /v2/filesystem/folders/getBatch |
**Filesystem** | Project | [**add_organizations**](docs/v2/Filesystem/Project.md#add_organizations) | **POST** /v2/filesystem/projects/{projectRid}/addOrganizations |
**Filesystem** | Project | [**create**](docs/v2/Filesystem/Project.md#create) | **POST** /v2/filesystem/projects/create |
**Filesystem** | Project | [**create_from_template**](docs/v2/Filesystem/Project.md#create_from_template) | **POST** /v2/filesystem/projects/createFromTemplate |
**Filesystem** | Project | [**get**](docs/v2/Filesystem/Project.md#get) | **GET** /v2/filesystem/projects/{projectRid} |
**Filesystem** | Project | [**organizations**](docs/v2/Filesystem/Project.md#organizations) | **GET** /v2/filesystem/projects/{projectRid}/organizations |
**Filesystem** | Project | [**remove_organizations**](docs/v2/Filesystem/Project.md#remove_organizations) | **POST** /v2/filesystem/projects/{projectRid}/removeOrganizations |
**Filesystem** | Resource | [**add_markings**](docs/v2/Filesystem/Resource.md#add_markings) | **POST** /v2/filesystem/resources/{resourceRid}/addMarkings |
**Filesystem** | Resource | [**delete**](docs/v2/Filesystem/Resource.md#delete) | **DELETE** /v2/filesystem/resources/{resourceRid} |
**Filesystem** | Resource | [**get**](docs/v2/Filesystem/Resource.md#get) | **GET** /v2/filesystem/resources/{resourceRid} |
**Filesystem** | Resource | [**get_access_requirements**](docs/v2/Filesystem/Resource.md#get_access_requirements) | **GET** /v2/filesystem/resources/{resourceRid}/getAccessRequirements |
**Filesystem** | Resource | [**get_batch**](docs/v2/Filesystem/Resource.md#get_batch) | **POST** /v2/filesystem/resources/getBatch |
**Filesystem** | Resource | [**get_by_path**](docs/v2/Filesystem/Resource.md#get_by_path) | **GET** /v2/filesystem/resources/getByPath |
**Filesystem** | Resource | [**get_by_path_batch**](docs/v2/Filesystem/Resource.md#get_by_path_batch) | **POST** /v2/filesystem/resources/getByPathBatch |
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
**MediaSets** | MediaSet | [**get**](docs/v2/MediaSets/MediaSet.md#get) | **GET** /v2/mediasets/{mediaSetRid} |
**MediaSets** | MediaSet | [**get_result**](docs/v2/MediaSets/MediaSet.md#get_result) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transformationJobs/{transformationJobId}/result |
**MediaSets** | MediaSet | [**get_rid_by_path**](docs/v2/MediaSets/MediaSet.md#get_rid_by_path) | **GET** /v2/mediasets/{mediaSetRid}/items/getRidByPath |
**MediaSets** | MediaSet | [**get_status**](docs/v2/MediaSets/MediaSet.md#get_status) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transformationJobs/{transformationJobId} |
**MediaSets** | MediaSet | [**info**](docs/v2/MediaSets/MediaSet.md#info) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid} |
**MediaSets** | MediaSet | [**metadata**](docs/v2/MediaSets/MediaSet.md#metadata) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/metadata |
**MediaSets** | MediaSet | [**read**](docs/v2/MediaSets/MediaSet.md#read) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/content |
**MediaSets** | MediaSet | [**read_original**](docs/v2/MediaSets/MediaSet.md#read_original) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/original |
**MediaSets** | MediaSet | [**reference**](docs/v2/MediaSets/MediaSet.md#reference) | **GET** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/reference |
**MediaSets** | MediaSet | [**register**](docs/v2/MediaSets/MediaSet.md#register) | **POST** /v2/mediasets/{mediaSetRid}/items/register |
**MediaSets** | MediaSet | [**transform**](docs/v2/MediaSets/MediaSet.md#transform) | **POST** /v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform |
**MediaSets** | MediaSet | [**upload**](docs/v2/MediaSets/MediaSet.md#upload) | **POST** /v2/mediasets/{mediaSetRid}/items |
**MediaSets** | MediaSet | [**upload_media**](docs/v2/MediaSets/MediaSet.md#upload_media) | **PUT** /v2/mediasets/media/upload |
**Models** | LiveDeployment | [**transform_json**](docs/v2/Models/LiveDeployment.md#transform_json) | **POST** /v2/models/liveDeployments/{liveDeploymentRid}/transformJson |
**Models** | Model | [**create**](docs/v2/Models/Model.md#create) | **POST** /v2/models |
**Models** | Model | [**get**](docs/v2/Models/Model.md#get) | **GET** /v2/models/{modelRid} |
**Models** | ModelVersion | [**get**](docs/v2/Models/ModelVersion.md#get) | **GET** /v2/models/{modelRid}/versions/{modelVersionRid} |
**Models** | ModelVersion | [**list**](docs/v2/Models/ModelVersion.md#list) | **GET** /v2/models/{modelRid}/versions |
**Ontologies** | Action | [**apply**](docs/v2/Ontologies/Action.md#apply) | **POST** /v2/ontologies/{ontology}/actions/{action}/apply |
**Ontologies** | Action | [**apply_batch**](docs/v2/Ontologies/Action.md#apply_batch) | **POST** /v2/ontologies/{ontology}/actions/{action}/applyBatch |
**Ontologies** | ActionType | [**get**](docs/v2/Ontologies/ActionType.md#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} |
**Ontologies** | ActionType | [**get_by_rid**](docs/v2/Ontologies/ActionType.md#get_by_rid) | **GET** /v2/ontologies/{ontology}/actionTypes/byRid/{actionTypeRid} |
**Ontologies** | ActionType | [**get_by_rid_batch**](docs/v2/Ontologies/ActionType.md#get_by_rid_batch) | **POST** /v2/ontologies/{ontology}/actionTypes/getByRidBatch |
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
**Ontologies** | ObjectType | [**get_edits_history**](docs/v2/Ontologies/ObjectType.md#get_edits_history) | **POST** /v2/ontologies/{ontology}/objectTypes/{objectType}/editsHistory |
**Ontologies** | ObjectType | [**get_full_metadata**](docs/v2/Ontologies/ObjectType.md#get_full_metadata) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/fullMetadata |
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
**Ontologies** | OntologyValueType | [**get**](docs/v2/Ontologies/OntologyValueType.md#get) | **GET** /v2/ontologies/{ontology}/valueTypes/{valueType} |
**Ontologies** | OntologyValueType | [**list**](docs/v2/Ontologies/OntologyValueType.md#list) | **GET** /v2/ontologies/{ontology}/valueTypes |
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
**Orchestration** | Schedule | [**get_affected_resources**](docs/v2/Orchestration/Schedule.md#get_affected_resources) | **POST** /v2/orchestration/schedules/{scheduleRid}/getAffectedResources |
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
**Streams** | Stream | [**get_end_offsets**](docs/v2/Streams/Stream.md#get_end_offsets) | **GET** /v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/getEndOffsets |
**Streams** | Stream | [**get_records**](docs/v2/Streams/Stream.md#get_records) | **GET** /v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/getRecords |
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
**Admin** | [AddEnrollmentRoleAssignmentsRequest](docs/v2/Admin/models/AddEnrollmentRoleAssignmentsRequest.md) | `from foundry_sdk.v2.admin.models import AddEnrollmentRoleAssignmentsRequest` |
**Admin** | [AddGroupMembersRequest](docs/v2/Admin/models/AddGroupMembersRequest.md) | `from foundry_sdk.v2.admin.models import AddGroupMembersRequest` |
**Admin** | [AddMarkingMembersRequest](docs/v2/Admin/models/AddMarkingMembersRequest.md) | `from foundry_sdk.v2.admin.models import AddMarkingMembersRequest` |
**Admin** | [AddMarkingRoleAssignmentsRequest](docs/v2/Admin/models/AddMarkingRoleAssignmentsRequest.md) | `from foundry_sdk.v2.admin.models import AddMarkingRoleAssignmentsRequest` |
**Admin** | [AddOrganizationRoleAssignmentsRequest](docs/v2/Admin/models/AddOrganizationRoleAssignmentsRequest.md) | `from foundry_sdk.v2.admin.models import AddOrganizationRoleAssignmentsRequest` |
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
**Admin** | [CreateGroupRequest](docs/v2/Admin/models/CreateGroupRequest.md) | `from foundry_sdk.v2.admin.models import CreateGroupRequest` |
**Admin** | [CreateMarkingCategoryRequest](docs/v2/Admin/models/CreateMarkingCategoryRequest.md) | `from foundry_sdk.v2.admin.models import CreateMarkingCategoryRequest` |
**Admin** | [CreateMarkingRequest](docs/v2/Admin/models/CreateMarkingRequest.md) | `from foundry_sdk.v2.admin.models import CreateMarkingRequest` |
**Admin** | [CreateOrganizationRequest](docs/v2/Admin/models/CreateOrganizationRequest.md) | `from foundry_sdk.v2.admin.models import CreateOrganizationRequest` |
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
**Admin** | [MarkingCategoryDescription](docs/v2/Admin/models/MarkingCategoryDescription.md) | `from foundry_sdk.v2.admin.models import MarkingCategoryDescription` |
**Admin** | [MarkingCategoryId](docs/v2/Admin/models/MarkingCategoryId.md) | `from foundry_sdk.v2.admin.models import MarkingCategoryId` |
**Admin** | [MarkingCategoryName](docs/v2/Admin/models/MarkingCategoryName.md) | `from foundry_sdk.v2.admin.models import MarkingCategoryName` |
**Admin** | [MarkingCategoryPermissions](docs/v2/Admin/models/MarkingCategoryPermissions.md) | `from foundry_sdk.v2.admin.models import MarkingCategoryPermissions` |
**Admin** | [MarkingCategoryPermissionsIsPublic](docs/v2/Admin/models/MarkingCategoryPermissionsIsPublic.md) | `from foundry_sdk.v2.admin.models import MarkingCategoryPermissionsIsPublic` |
**Admin** | [MarkingCategoryRole](docs/v2/Admin/models/MarkingCategoryRole.md) | `from foundry_sdk.v2.admin.models import MarkingCategoryRole` |
**Admin** | [MarkingCategoryRoleAssignment](docs/v2/Admin/models/MarkingCategoryRoleAssignment.md) | `from foundry_sdk.v2.admin.models import MarkingCategoryRoleAssignment` |
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
**Admin** | [PreregisterGroupRequest](docs/v2/Admin/models/PreregisterGroupRequest.md) | `from foundry_sdk.v2.admin.models import PreregisterGroupRequest` |
**Admin** | [PreregisterUserRequest](docs/v2/Admin/models/PreregisterUserRequest.md) | `from foundry_sdk.v2.admin.models import PreregisterUserRequest` |
**Admin** | [PrincipalFilterType](docs/v2/Admin/models/PrincipalFilterType.md) | `from foundry_sdk.v2.admin.models import PrincipalFilterType` |
**Admin** | [ProviderId](docs/v2/Admin/models/ProviderId.md) | `from foundry_sdk.v2.admin.models import ProviderId` |
**Admin** | [RemoveEnrollmentRoleAssignmentsRequest](docs/v2/Admin/models/RemoveEnrollmentRoleAssignmentsRequest.md) | `from foundry_sdk.v2.admin.models import RemoveEnrollmentRoleAssignmentsRequest` |
**Admin** | [RemoveGroupMembersRequest](docs/v2/Admin/models/RemoveGroupMembersRequest.md) | `from foundry_sdk.v2.admin.models import RemoveGroupMembersRequest` |
**Admin** | [RemoveMarkingMembersRequest](docs/v2/Admin/models/RemoveMarkingMembersRequest.md) | `from foundry_sdk.v2.admin.models import RemoveMarkingMembersRequest` |
**Admin** | [RemoveMarkingRoleAssignmentsRequest](docs/v2/Admin/models/RemoveMarkingRoleAssignmentsRequest.md) | `from foundry_sdk.v2.admin.models import RemoveMarkingRoleAssignmentsRequest` |
**Admin** | [RemoveOrganizationRoleAssignmentsRequest](docs/v2/Admin/models/RemoveOrganizationRoleAssignmentsRequest.md) | `from foundry_sdk.v2.admin.models import RemoveOrganizationRoleAssignmentsRequest` |
**Admin** | [ReplaceGroupMembershipExpirationPolicyRequest](docs/v2/Admin/models/ReplaceGroupMembershipExpirationPolicyRequest.md) | `from foundry_sdk.v2.admin.models import ReplaceGroupMembershipExpirationPolicyRequest` |
**Admin** | [ReplaceGroupProviderInfoRequest](docs/v2/Admin/models/ReplaceGroupProviderInfoRequest.md) | `from foundry_sdk.v2.admin.models import ReplaceGroupProviderInfoRequest` |
**Admin** | [ReplaceMarkingCategoryRequest](docs/v2/Admin/models/ReplaceMarkingCategoryRequest.md) | `from foundry_sdk.v2.admin.models import ReplaceMarkingCategoryRequest` |
**Admin** | [ReplaceMarkingRequest](docs/v2/Admin/models/ReplaceMarkingRequest.md) | `from foundry_sdk.v2.admin.models import ReplaceMarkingRequest` |
**Admin** | [ReplaceOrganizationRequest](docs/v2/Admin/models/ReplaceOrganizationRequest.md) | `from foundry_sdk.v2.admin.models import ReplaceOrganizationRequest` |
**Admin** | [ReplaceUserProviderInfoRequest](docs/v2/Admin/models/ReplaceUserProviderInfoRequest.md) | `from foundry_sdk.v2.admin.models import ReplaceUserProviderInfoRequest` |
**Admin** | [Role](docs/v2/Admin/models/Role.md) | `from foundry_sdk.v2.admin.models import Role` |
**Admin** | [RoleDescription](docs/v2/Admin/models/RoleDescription.md) | `from foundry_sdk.v2.admin.models import RoleDescription` |
**Admin** | [RoleDisplayName](docs/v2/Admin/models/RoleDisplayName.md) | `from foundry_sdk.v2.admin.models import RoleDisplayName` |
**Admin** | [SamlAuthenticationProtocol](docs/v2/Admin/models/SamlAuthenticationProtocol.md) | `from foundry_sdk.v2.admin.models import SamlAuthenticationProtocol` |
**Admin** | [SamlServiceProviderMetadata](docs/v2/Admin/models/SamlServiceProviderMetadata.md) | `from foundry_sdk.v2.admin.models import SamlServiceProviderMetadata` |
**Admin** | [SearchGroupsRequest](docs/v2/Admin/models/SearchGroupsRequest.md) | `from foundry_sdk.v2.admin.models import SearchGroupsRequest` |
**Admin** | [SearchGroupsResponse](docs/v2/Admin/models/SearchGroupsResponse.md) | `from foundry_sdk.v2.admin.models import SearchGroupsResponse` |
**Admin** | [SearchUsersRequest](docs/v2/Admin/models/SearchUsersRequest.md) | `from foundry_sdk.v2.admin.models import SearchUsersRequest` |
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
**AipAgents** | [BlockingContinueSessionRequest](docs/v2/AipAgents/models/BlockingContinueSessionRequest.md) | `from foundry_sdk.v2.aip_agents.models import BlockingContinueSessionRequest` |
**AipAgents** | [CancelSessionRequest](docs/v2/AipAgents/models/CancelSessionRequest.md) | `from foundry_sdk.v2.aip_agents.models import CancelSessionRequest` |
**AipAgents** | [CancelSessionResponse](docs/v2/AipAgents/models/CancelSessionResponse.md) | `from foundry_sdk.v2.aip_agents.models import CancelSessionResponse` |
**AipAgents** | [Content](docs/v2/AipAgents/models/Content.md) | `from foundry_sdk.v2.aip_agents.models import Content` |
**AipAgents** | [CreateSessionRequest](docs/v2/AipAgents/models/CreateSessionRequest.md) | `from foundry_sdk.v2.aip_agents.models import CreateSessionRequest` |
**AipAgents** | [FailureToolCallOutput](docs/v2/AipAgents/models/FailureToolCallOutput.md) | `from foundry_sdk.v2.aip_agents.models import FailureToolCallOutput` |
**AipAgents** | [FunctionRetrievedContext](docs/v2/AipAgents/models/FunctionRetrievedContext.md) | `from foundry_sdk.v2.aip_agents.models import FunctionRetrievedContext` |
**AipAgents** | [GetRagContextForSessionRequest](docs/v2/AipAgents/models/GetRagContextForSessionRequest.md) | `from foundry_sdk.v2.aip_agents.models import GetRagContextForSessionRequest` |
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
**AipAgents** | [StreamingContinueSessionRequest](docs/v2/AipAgents/models/StreamingContinueSessionRequest.md) | `from foundry_sdk.v2.aip_agents.models import StreamingContinueSessionRequest` |
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
**AipAgents** | [UpdateSessionTitleRequest](docs/v2/AipAgents/models/UpdateSessionTitleRequest.md) | `from foundry_sdk.v2.aip_agents.models import UpdateSessionTitleRequest` |
**AipAgents** | [UserTextInput](docs/v2/AipAgents/models/UserTextInput.md) | `from foundry_sdk.v2.aip_agents.models import UserTextInput` |
**Audit** | [FileId](docs/v2/Audit/models/FileId.md) | `from foundry_sdk.v2.audit.models import FileId` |
**Audit** | [ListLogFilesResponse](docs/v2/Audit/models/ListLogFilesResponse.md) | `from foundry_sdk.v2.audit.models import ListLogFilesResponse` |
**Audit** | [LogFile](docs/v2/Audit/models/LogFile.md) | `from foundry_sdk.v2.audit.models import LogFile` |
**Checkpoints** | [AcknowledgementJustification](docs/v2/Checkpoints/models/AcknowledgementJustification.md) | `from foundry_sdk.v2.checkpoints.models import AcknowledgementJustification` |
**Checkpoints** | [ActingUser](docs/v2/Checkpoints/models/ActingUser.md) | `from foundry_sdk.v2.checkpoints.models import ActingUser` |
**Checkpoints** | [ApprovalsMetadata](docs/v2/Checkpoints/models/ApprovalsMetadata.md) | `from foundry_sdk.v2.checkpoints.models import ApprovalsMetadata` |
**Checkpoints** | [ApprovalsSubtaskId](docs/v2/Checkpoints/models/ApprovalsSubtaskId.md) | `from foundry_sdk.v2.checkpoints.models import ApprovalsSubtaskId` |
**Checkpoints** | [ApprovalsTaskId](docs/v2/Checkpoints/models/ApprovalsTaskId.md) | `from foundry_sdk.v2.checkpoints.models import ApprovalsTaskId` |
**Checkpoints** | [CheckpointedActionType](docs/v2/Checkpoints/models/CheckpointedActionType.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedActionType` |
**Checkpoints** | [CheckpointedActionTypeRid](docs/v2/Checkpoints/models/CheckpointedActionTypeRid.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedActionTypeRid` |
**Checkpoints** | [CheckpointedGroup](docs/v2/Checkpoints/models/CheckpointedGroup.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedGroup` |
**Checkpoints** | [CheckpointedGroupId](docs/v2/Checkpoints/models/CheckpointedGroupId.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedGroupId` |
**Checkpoints** | [CheckpointedIntervention](docs/v2/Checkpoints/models/CheckpointedIntervention.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedIntervention` |
**Checkpoints** | [CheckpointedInterventionRid](docs/v2/Checkpoints/models/CheckpointedInterventionRid.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedInterventionRid` |
**Checkpoints** | [CheckpointedIssue](docs/v2/Checkpoints/models/CheckpointedIssue.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedIssue` |
**Checkpoints** | [CheckpointedIssueRid](docs/v2/Checkpoints/models/CheckpointedIssueRid.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedIssueRid` |
**Checkpoints** | [CheckpointedItem](docs/v2/Checkpoints/models/CheckpointedItem.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedItem` |
**Checkpoints** | [CheckpointedItemId](docs/v2/Checkpoints/models/CheckpointedItemId.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedItemId` |
**Checkpoints** | [CheckpointedJob](docs/v2/Checkpoints/models/CheckpointedJob.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedJob` |
**Checkpoints** | [CheckpointedJobRid](docs/v2/Checkpoints/models/CheckpointedJobRid.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedJobRid` |
**Checkpoints** | [CheckpointedJobSpecification](docs/v2/Checkpoints/models/CheckpointedJobSpecification.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedJobSpecification` |
**Checkpoints** | [CheckpointedJobSpecRid](docs/v2/Checkpoints/models/CheckpointedJobSpecRid.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedJobSpecRid` |
**Checkpoints** | [CheckpointedLanguageModel](docs/v2/Checkpoints/models/CheckpointedLanguageModel.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedLanguageModel` |
**Checkpoints** | [CheckpointedLanguageModelRid](docs/v2/Checkpoints/models/CheckpointedLanguageModelRid.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedLanguageModelRid` |
**Checkpoints** | [CheckpointedLanguageModelSession](docs/v2/Checkpoints/models/CheckpointedLanguageModelSession.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedLanguageModelSession` |
**Checkpoints** | [CheckpointedLanguageModelSessionRid](docs/v2/Checkpoints/models/CheckpointedLanguageModelSessionRid.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedLanguageModelSessionRid` |
**Checkpoints** | [CheckpointedMarketplaceProduct](docs/v2/Checkpoints/models/CheckpointedMarketplaceProduct.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedMarketplaceProduct` |
**Checkpoints** | [CheckpointedMarketplaceProductId](docs/v2/Checkpoints/models/CheckpointedMarketplaceProductId.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedMarketplaceProductId` |
**Checkpoints** | [CheckpointedMarking](docs/v2/Checkpoints/models/CheckpointedMarking.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedMarking` |
**Checkpoints** | [CheckpointedMarkingId](docs/v2/Checkpoints/models/CheckpointedMarkingId.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedMarkingId` |
**Checkpoints** | [CheckpointedObjectSet](docs/v2/Checkpoints/models/CheckpointedObjectSet.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedObjectSet` |
**Checkpoints** | [CheckpointedObjectSetTypesProxy](docs/v2/Checkpoints/models/CheckpointedObjectSetTypesProxy.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedObjectSetTypesProxy` |
**Checkpoints** | [CheckpointedObjectSetTypesProxyRids](docs/v2/Checkpoints/models/CheckpointedObjectSetTypesProxyRids.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedObjectSetTypesProxyRids` |
**Checkpoints** | [CheckpointedObjectSetVersionedRid](docs/v2/Checkpoints/models/CheckpointedObjectSetVersionedRid.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedObjectSetVersionedRid` |
**Checkpoints** | [CheckpointedOntology](docs/v2/Checkpoints/models/CheckpointedOntology.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedOntology` |
**Checkpoints** | [CheckpointedOntologyWithObjectTypes](docs/v2/Checkpoints/models/CheckpointedOntologyWithObjectTypes.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedOntologyWithObjectTypes` |
**Checkpoints** | [CheckpointedPrincipal](docs/v2/Checkpoints/models/CheckpointedPrincipal.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedPrincipal` |
**Checkpoints** | [CheckpointedPrincipalId](docs/v2/Checkpoints/models/CheckpointedPrincipalId.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedPrincipalId` |
**Checkpoints** | [CheckpointedPrincipalRole](docs/v2/Checkpoints/models/CheckpointedPrincipalRole.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedPrincipalRole` |
**Checkpoints** | [CheckpointedResource](docs/v2/Checkpoints/models/CheckpointedResource.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedResource` |
**Checkpoints** | [CheckpointedResourceRid](docs/v2/Checkpoints/models/CheckpointedResourceRid.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedResourceRid` |
**Checkpoints** | [CheckpointedResourceType](docs/v2/Checkpoints/models/CheckpointedResourceType.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedResourceType` |
**Checkpoints** | [CheckpointedRole](docs/v2/Checkpoints/models/CheckpointedRole.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedRole` |
**Checkpoints** | [CheckpointedRoleId](docs/v2/Checkpoints/models/CheckpointedRoleId.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedRoleId` |
**Checkpoints** | [CheckpointedSchedule](docs/v2/Checkpoints/models/CheckpointedSchedule.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedSchedule` |
**Checkpoints** | [CheckpointedScheduleRid](docs/v2/Checkpoints/models/CheckpointedScheduleRid.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedScheduleRid` |
**Checkpoints** | [CheckpointedToken](docs/v2/Checkpoints/models/CheckpointedToken.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedToken` |
**Checkpoints** | [CheckpointedTokenId](docs/v2/Checkpoints/models/CheckpointedTokenId.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedTokenId` |
**Checkpoints** | [CheckpointedTokenType](docs/v2/Checkpoints/models/CheckpointedTokenType.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedTokenType` |
**Checkpoints** | [CheckpointedUserIntakeFormInput](docs/v2/Checkpoints/models/CheckpointedUserIntakeFormInput.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedUserIntakeFormInput` |
**Checkpoints** | [CheckpointedUserIntakeFormInputId](docs/v2/Checkpoints/models/CheckpointedUserIntakeFormInputId.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedUserIntakeFormInputId` |
**Checkpoints** | [CheckpointedUserIntakeSubmission](docs/v2/Checkpoints/models/CheckpointedUserIntakeSubmission.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedUserIntakeSubmission` |
**Checkpoints** | [CheckpointedUserIntakeSubmissionRid](docs/v2/Checkpoints/models/CheckpointedUserIntakeSubmissionRid.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedUserIntakeSubmissionRid` |
**Checkpoints** | [CheckpointedVersionedObjectSet](docs/v2/Checkpoints/models/CheckpointedVersionedObjectSet.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointedVersionedObjectSet` |
**Checkpoints** | [CheckpointType](docs/v2/Checkpoints/models/CheckpointType.md) | `from foundry_sdk.v2.checkpoints.models import CheckpointType` |
**Checkpoints** | [ConfigRid](docs/v2/Checkpoints/models/ConfigRid.md) | `from foundry_sdk.v2.checkpoints.models import ConfigRid` |
**Checkpoints** | [DropdownJustification](docs/v2/Checkpoints/models/DropdownJustification.md) | `from foundry_sdk.v2.checkpoints.models import DropdownJustification` |
**Checkpoints** | [DropdownSelection](docs/v2/Checkpoints/models/DropdownSelection.md) | `from foundry_sdk.v2.checkpoints.models import DropdownSelection` |
**Checkpoints** | [GetRecordsBatchRequestElement](docs/v2/Checkpoints/models/GetRecordsBatchRequestElement.md) | `from foundry_sdk.v2.checkpoints.models import GetRecordsBatchRequestElement` |
**Checkpoints** | [GetRecordsBatchResponse](docs/v2/Checkpoints/models/GetRecordsBatchResponse.md) | `from foundry_sdk.v2.checkpoints.models import GetRecordsBatchResponse` |
**Checkpoints** | [InteractionRid](docs/v2/Checkpoints/models/InteractionRid.md) | `from foundry_sdk.v2.checkpoints.models import InteractionRid` |
**Checkpoints** | [Justification](docs/v2/Checkpoints/models/Justification.md) | `from foundry_sdk.v2.checkpoints.models import Justification` |
**Checkpoints** | [JustificationMatchType](docs/v2/Checkpoints/models/JustificationMatchType.md) | `from foundry_sdk.v2.checkpoints.models import JustificationMatchType` |
**Checkpoints** | [NamespaceRid](docs/v2/Checkpoints/models/NamespaceRid.md) | `from foundry_sdk.v2.checkpoints.models import NamespaceRid` |
**Checkpoints** | [OrganizationRid](docs/v2/Checkpoints/models/OrganizationRid.md) | `from foundry_sdk.v2.checkpoints.models import OrganizationRid` |
**Checkpoints** | [ProjectRid](docs/v2/Checkpoints/models/ProjectRid.md) | `from foundry_sdk.v2.checkpoints.models import ProjectRid` |
**Checkpoints** | [ReauthenticationJustification](docs/v2/Checkpoints/models/ReauthenticationJustification.md) | `from foundry_sdk.v2.checkpoints.models import ReauthenticationJustification` |
**Checkpoints** | [Record](docs/v2/Checkpoints/models/Record.md) | `from foundry_sdk.v2.checkpoints.models import Record` |
**Checkpoints** | [RecordCreatedAt](docs/v2/Checkpoints/models/RecordCreatedAt.md) | `from foundry_sdk.v2.checkpoints.models import RecordCreatedAt` |
**Checkpoints** | [RecordRid](docs/v2/Checkpoints/models/RecordRid.md) | `from foundry_sdk.v2.checkpoints.models import RecordRid` |
**Checkpoints** | [RedactableString](docs/v2/Checkpoints/models/RedactableString.md) | `from foundry_sdk.v2.checkpoints.models import RedactableString` |
**Checkpoints** | [RedactionType](docs/v2/Checkpoints/models/RedactionType.md) | `from foundry_sdk.v2.checkpoints.models import RedactionType` |
**Checkpoints** | [ResponseJustification](docs/v2/Checkpoints/models/ResponseJustification.md) | `from foundry_sdk.v2.checkpoints.models import ResponseJustification` |
**Checkpoints** | [Scope](docs/v2/Checkpoints/models/Scope.md) | `from foundry_sdk.v2.checkpoints.models import Scope` |
**Checkpoints** | [SearchCheckpointRecordsAndFilter](docs/v2/Checkpoints/models/SearchCheckpointRecordsAndFilter.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsAndFilter` |
**Checkpoints** | [SearchCheckpointRecordsCheckpointedItemIdFilter](docs/v2/Checkpoints/models/SearchCheckpointRecordsCheckpointedItemIdFilter.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsCheckpointedItemIdFilter` |
**Checkpoints** | [SearchCheckpointRecordsEqualsFilter](docs/v2/Checkpoints/models/SearchCheckpointRecordsEqualsFilter.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsEqualsFilter` |
**Checkpoints** | [SearchCheckpointRecordsEqualsFilterField](docs/v2/Checkpoints/models/SearchCheckpointRecordsEqualsFilterField.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsEqualsFilterField` |
**Checkpoints** | [SearchCheckpointRecordsFilter](docs/v2/Checkpoints/models/SearchCheckpointRecordsFilter.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsFilter` |
**Checkpoints** | [SearchCheckpointRecordsGteFilter](docs/v2/Checkpoints/models/SearchCheckpointRecordsGteFilter.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsGteFilter` |
**Checkpoints** | [SearchCheckpointRecordsGteFilterField](docs/v2/Checkpoints/models/SearchCheckpointRecordsGteFilterField.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsGteFilterField` |
**Checkpoints** | [SearchCheckpointRecordsLtFilter](docs/v2/Checkpoints/models/SearchCheckpointRecordsLtFilter.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsLtFilter` |
**Checkpoints** | [SearchCheckpointRecordsLtFilterField](docs/v2/Checkpoints/models/SearchCheckpointRecordsLtFilterField.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsLtFilterField` |
**Checkpoints** | [SearchCheckpointRecordsNotFilter](docs/v2/Checkpoints/models/SearchCheckpointRecordsNotFilter.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsNotFilter` |
**Checkpoints** | [SearchCheckpointRecordsOrFilter](docs/v2/Checkpoints/models/SearchCheckpointRecordsOrFilter.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsOrFilter` |
**Checkpoints** | [SearchCheckpointRecordsRequest](docs/v2/Checkpoints/models/SearchCheckpointRecordsRequest.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsRequest` |
**Checkpoints** | [SearchCheckpointRecordsResponse](docs/v2/Checkpoints/models/SearchCheckpointRecordsResponse.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsResponse` |
**Checkpoints** | [SearchCheckpointRecordsTextSearchFilter](docs/v2/Checkpoints/models/SearchCheckpointRecordsTextSearchFilter.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsTextSearchFilter` |
**Checkpoints** | [SearchCheckpointRecordsTextSearchFilterField](docs/v2/Checkpoints/models/SearchCheckpointRecordsTextSearchFilterField.md) | `from foundry_sdk.v2.checkpoints.models import SearchCheckpointRecordsTextSearchFilterField` |
**Checkpoints** | [SearchRecordsRequest](docs/v2/Checkpoints/models/SearchRecordsRequest.md) | `from foundry_sdk.v2.checkpoints.models import SearchRecordsRequest` |
**Checkpoints** | [SortDirection](docs/v2/Checkpoints/models/SortDirection.md) | `from foundry_sdk.v2.checkpoints.models import SortDirection` |
**Connectivity** | [ApiKeyAuthentication](docs/v2/Connectivity/models/ApiKeyAuthentication.md) | `from foundry_sdk.v2.connectivity.models import ApiKeyAuthentication` |
**Connectivity** | [AsPlaintextValue](docs/v2/Connectivity/models/AsPlaintextValue.md) | `from foundry_sdk.v2.connectivity.models import AsPlaintextValue` |
**Connectivity** | [AsSecretName](docs/v2/Connectivity/models/AsSecretName.md) | `from foundry_sdk.v2.connectivity.models import AsSecretName` |
**Connectivity** | [AwsAccessKey](docs/v2/Connectivity/models/AwsAccessKey.md) | `from foundry_sdk.v2.connectivity.models import AwsAccessKey` |
**Connectivity** | [AwsOidcAuthentication](docs/v2/Connectivity/models/AwsOidcAuthentication.md) | `from foundry_sdk.v2.connectivity.models import AwsOidcAuthentication` |
**Connectivity** | [BasicCredentials](docs/v2/Connectivity/models/BasicCredentials.md) | `from foundry_sdk.v2.connectivity.models import BasicCredentials` |
**Connectivity** | [BearerToken](docs/v2/Connectivity/models/BearerToken.md) | `from foundry_sdk.v2.connectivity.models import BearerToken` |
**Connectivity** | [BigQueryVirtualTableConfig](docs/v2/Connectivity/models/BigQueryVirtualTableConfig.md) | `from foundry_sdk.v2.connectivity.models import BigQueryVirtualTableConfig` |
**Connectivity** | [CloudIdentity](docs/v2/Connectivity/models/CloudIdentity.md) | `from foundry_sdk.v2.connectivity.models import CloudIdentity` |
**Connectivity** | [CloudIdentityRid](docs/v2/Connectivity/models/CloudIdentityRid.md) | `from foundry_sdk.v2.connectivity.models import CloudIdentityRid` |
**Connectivity** | [Connection](docs/v2/Connectivity/models/Connection.md) | `from foundry_sdk.v2.connectivity.models import Connection` |
**Connectivity** | [ConnectionConfiguration](docs/v2/Connectivity/models/ConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import ConnectionConfiguration` |
**Connectivity** | [ConnectionDisplayName](docs/v2/Connectivity/models/ConnectionDisplayName.md) | `from foundry_sdk.v2.connectivity.models import ConnectionDisplayName` |
**Connectivity** | [ConnectionExportSettings](docs/v2/Connectivity/models/ConnectionExportSettings.md) | `from foundry_sdk.v2.connectivity.models import ConnectionExportSettings` |
**Connectivity** | [ConnectionRid](docs/v2/Connectivity/models/ConnectionRid.md) | `from foundry_sdk.v2.connectivity.models import ConnectionRid` |
**Connectivity** | [ConnectionWorker](docs/v2/Connectivity/models/ConnectionWorker.md) | `from foundry_sdk.v2.connectivity.models import ConnectionWorker` |
**Connectivity** | [CreateConnectionRequest](docs/v2/Connectivity/models/CreateConnectionRequest.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequest` |
**Connectivity** | [CreateConnectionRequestAsPlaintextValue](docs/v2/Connectivity/models/CreateConnectionRequestAsPlaintextValue.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestAsPlaintextValue` |
**Connectivity** | [CreateConnectionRequestAsSecretName](docs/v2/Connectivity/models/CreateConnectionRequestAsSecretName.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestAsSecretName` |
**Connectivity** | [CreateConnectionRequestBasicCredentials](docs/v2/Connectivity/models/CreateConnectionRequestBasicCredentials.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestBasicCredentials` |
**Connectivity** | [CreateConnectionRequestConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestConnectionWorker](docs/v2/Connectivity/models/CreateConnectionRequestConnectionWorker.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestConnectionWorker` |
**Connectivity** | [CreateConnectionRequestDatabricksAuthenticationMode](docs/v2/Connectivity/models/CreateConnectionRequestDatabricksAuthenticationMode.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestDatabricksAuthenticationMode` |
**Connectivity** | [CreateConnectionRequestDatabricksConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestDatabricksConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestDatabricksConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestEncryptedProperty](docs/v2/Connectivity/models/CreateConnectionRequestEncryptedProperty.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestEncryptedProperty` |
**Connectivity** | [CreateConnectionRequestFoundryWorker](docs/v2/Connectivity/models/CreateConnectionRequestFoundryWorker.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestFoundryWorker` |
**Connectivity** | [CreateConnectionRequestJdbcConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestJdbcConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestJdbcConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestOauthMachineToMachineAuth](docs/v2/Connectivity/models/CreateConnectionRequestOauthMachineToMachineAuth.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestOauthMachineToMachineAuth` |
**Connectivity** | [CreateConnectionRequestPersonalAccessToken](docs/v2/Connectivity/models/CreateConnectionRequestPersonalAccessToken.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestPersonalAccessToken` |
**Connectivity** | [CreateConnectionRequestRestConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestRestConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestRestConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestS3ConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestS3ConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestS3ConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestSmbAuth](docs/v2/Connectivity/models/CreateConnectionRequestSmbAuth.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestSmbAuth` |
**Connectivity** | [CreateConnectionRequestSmbConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestSmbConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestSmbConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestSmbUsernamePasswordAuth](docs/v2/Connectivity/models/CreateConnectionRequestSmbUsernamePasswordAuth.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestSmbUsernamePasswordAuth` |
**Connectivity** | [CreateConnectionRequestSnowflakeAuthenticationMode](docs/v2/Connectivity/models/CreateConnectionRequestSnowflakeAuthenticationMode.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestSnowflakeAuthenticationMode` |
**Connectivity** | [CreateConnectionRequestSnowflakeConnectionConfiguration](docs/v2/Connectivity/models/CreateConnectionRequestSnowflakeConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestSnowflakeConnectionConfiguration` |
**Connectivity** | [CreateConnectionRequestSnowflakeExternalOauth](docs/v2/Connectivity/models/CreateConnectionRequestSnowflakeExternalOauth.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestSnowflakeExternalOauth` |
**Connectivity** | [CreateConnectionRequestSnowflakeKeyPairAuthentication](docs/v2/Connectivity/models/CreateConnectionRequestSnowflakeKeyPairAuthentication.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestSnowflakeKeyPairAuthentication` |
**Connectivity** | [CreateConnectionRequestUnknownWorker](docs/v2/Connectivity/models/CreateConnectionRequestUnknownWorker.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestUnknownWorker` |
**Connectivity** | [CreateConnectionRequestWorkflowIdentityFederation](docs/v2/Connectivity/models/CreateConnectionRequestWorkflowIdentityFederation.md) | `from foundry_sdk.v2.connectivity.models import CreateConnectionRequestWorkflowIdentityFederation` |
**Connectivity** | [CreateFileImportRequest](docs/v2/Connectivity/models/CreateFileImportRequest.md) | `from foundry_sdk.v2.connectivity.models import CreateFileImportRequest` |
**Connectivity** | [CreateTableImportRequest](docs/v2/Connectivity/models/CreateTableImportRequest.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequest` |
**Connectivity** | [CreateTableImportRequestDatabricksTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestDatabricksTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestDatabricksTableImportConfig` |
**Connectivity** | [CreateTableImportRequestJdbcTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestJdbcTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestJdbcTableImportConfig` |
**Connectivity** | [CreateTableImportRequestMicrosoftAccessTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestMicrosoftAccessTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestMicrosoftAccessTableImportConfig` |
**Connectivity** | [CreateTableImportRequestMicrosoftSqlServerTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestMicrosoftSqlServerTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestMicrosoftSqlServerTableImportConfig` |
**Connectivity** | [CreateTableImportRequestOracleTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestOracleTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestOracleTableImportConfig` |
**Connectivity** | [CreateTableImportRequestPostgreSqlTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestPostgreSqlTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestPostgreSqlTableImportConfig` |
**Connectivity** | [CreateTableImportRequestSnowflakeTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestSnowflakeTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestSnowflakeTableImportConfig` |
**Connectivity** | [CreateTableImportRequestTableImportConfig](docs/v2/Connectivity/models/CreateTableImportRequestTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import CreateTableImportRequestTableImportConfig` |
**Connectivity** | [CreateVirtualTableRequest](docs/v2/Connectivity/models/CreateVirtualTableRequest.md) | `from foundry_sdk.v2.connectivity.models import CreateVirtualTableRequest` |
**Connectivity** | [DatabricksAuthenticationMode](docs/v2/Connectivity/models/DatabricksAuthenticationMode.md) | `from foundry_sdk.v2.connectivity.models import DatabricksAuthenticationMode` |
**Connectivity** | [DatabricksConnectionConfiguration](docs/v2/Connectivity/models/DatabricksConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import DatabricksConnectionConfiguration` |
**Connectivity** | [DatabricksTableImportConfig](docs/v2/Connectivity/models/DatabricksTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import DatabricksTableImportConfig` |
**Connectivity** | [DateColumnInitialIncrementalState](docs/v2/Connectivity/models/DateColumnInitialIncrementalState.md) | `from foundry_sdk.v2.connectivity.models import DateColumnInitialIncrementalState` |
**Connectivity** | [DecimalColumnInitialIncrementalState](docs/v2/Connectivity/models/DecimalColumnInitialIncrementalState.md) | `from foundry_sdk.v2.connectivity.models import DecimalColumnInitialIncrementalState` |
**Connectivity** | [DeltaVirtualTableConfig](docs/v2/Connectivity/models/DeltaVirtualTableConfig.md) | `from foundry_sdk.v2.connectivity.models import DeltaVirtualTableConfig` |
**Connectivity** | [Domain](docs/v2/Connectivity/models/Domain.md) | `from foundry_sdk.v2.connectivity.models import Domain` |
**Connectivity** | [EncryptedProperty](docs/v2/Connectivity/models/EncryptedProperty.md) | `from foundry_sdk.v2.connectivity.models import EncryptedProperty` |
**Connectivity** | [FileAnyPathMatchesFilter](docs/v2/Connectivity/models/FileAnyPathMatchesFilter.md) | `from foundry_sdk.v2.connectivity.models import FileAnyPathMatchesFilter` |
**Connectivity** | [FileAtLeastCountFilter](docs/v2/Connectivity/models/FileAtLeastCountFilter.md) | `from foundry_sdk.v2.connectivity.models import FileAtLeastCountFilter` |
**Connectivity** | [FileChangedSinceLastUploadFilter](docs/v2/Connectivity/models/FileChangedSinceLastUploadFilter.md) | `from foundry_sdk.v2.connectivity.models import FileChangedSinceLastUploadFilter` |
**Connectivity** | [FileFormat](docs/v2/Connectivity/models/FileFormat.md) | `from foundry_sdk.v2.connectivity.models import FileFormat` |
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
**Connectivity** | [FilesVirtualTableConfig](docs/v2/Connectivity/models/FilesVirtualTableConfig.md) | `from foundry_sdk.v2.connectivity.models import FilesVirtualTableConfig` |
**Connectivity** | [FoundryWorker](docs/v2/Connectivity/models/FoundryWorker.md) | `from foundry_sdk.v2.connectivity.models import FoundryWorker` |
**Connectivity** | [GetConfigurationConnectionsBatchRequestElement](docs/v2/Connectivity/models/GetConfigurationConnectionsBatchRequestElement.md) | `from foundry_sdk.v2.connectivity.models import GetConfigurationConnectionsBatchRequestElement` |
**Connectivity** | [GetConfigurationConnectionsBatchResponse](docs/v2/Connectivity/models/GetConfigurationConnectionsBatchResponse.md) | `from foundry_sdk.v2.connectivity.models import GetConfigurationConnectionsBatchResponse` |
**Connectivity** | [GlueVirtualTableConfig](docs/v2/Connectivity/models/GlueVirtualTableConfig.md) | `from foundry_sdk.v2.connectivity.models import GlueVirtualTableConfig` |
**Connectivity** | [HeaderApiKey](docs/v2/Connectivity/models/HeaderApiKey.md) | `from foundry_sdk.v2.connectivity.models import HeaderApiKey` |
**Connectivity** | [IcebergVirtualTableConfig](docs/v2/Connectivity/models/IcebergVirtualTableConfig.md) | `from foundry_sdk.v2.connectivity.models import IcebergVirtualTableConfig` |
**Connectivity** | [IntegerColumnInitialIncrementalState](docs/v2/Connectivity/models/IntegerColumnInitialIncrementalState.md) | `from foundry_sdk.v2.connectivity.models import IntegerColumnInitialIncrementalState` |
**Connectivity** | [InvalidConnectionReason](docs/v2/Connectivity/models/InvalidConnectionReason.md) | `from foundry_sdk.v2.connectivity.models import InvalidConnectionReason` |
**Connectivity** | [JdbcConnectionConfiguration](docs/v2/Connectivity/models/JdbcConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import JdbcConnectionConfiguration` |
**Connectivity** | [JdbcDriverArtifactName](docs/v2/Connectivity/models/JdbcDriverArtifactName.md) | `from foundry_sdk.v2.connectivity.models import JdbcDriverArtifactName` |
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
**Connectivity** | [ReplaceFileImportRequest](docs/v2/Connectivity/models/ReplaceFileImportRequest.md) | `from foundry_sdk.v2.connectivity.models import ReplaceFileImportRequest` |
**Connectivity** | [ReplaceTableImportRequest](docs/v2/Connectivity/models/ReplaceTableImportRequest.md) | `from foundry_sdk.v2.connectivity.models import ReplaceTableImportRequest` |
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
**Connectivity** | [SmbAuth](docs/v2/Connectivity/models/SmbAuth.md) | `from foundry_sdk.v2.connectivity.models import SmbAuth` |
**Connectivity** | [SmbConnectionConfiguration](docs/v2/Connectivity/models/SmbConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import SmbConnectionConfiguration` |
**Connectivity** | [SmbProxyConfiguration](docs/v2/Connectivity/models/SmbProxyConfiguration.md) | `from foundry_sdk.v2.connectivity.models import SmbProxyConfiguration` |
**Connectivity** | [SmbProxyType](docs/v2/Connectivity/models/SmbProxyType.md) | `from foundry_sdk.v2.connectivity.models import SmbProxyType` |
**Connectivity** | [SmbUsernamePasswordAuth](docs/v2/Connectivity/models/SmbUsernamePasswordAuth.md) | `from foundry_sdk.v2.connectivity.models import SmbUsernamePasswordAuth` |
**Connectivity** | [SnowflakeAuthenticationMode](docs/v2/Connectivity/models/SnowflakeAuthenticationMode.md) | `from foundry_sdk.v2.connectivity.models import SnowflakeAuthenticationMode` |
**Connectivity** | [SnowflakeConnectionConfiguration](docs/v2/Connectivity/models/SnowflakeConnectionConfiguration.md) | `from foundry_sdk.v2.connectivity.models import SnowflakeConnectionConfiguration` |
**Connectivity** | [SnowflakeExternalOauth](docs/v2/Connectivity/models/SnowflakeExternalOauth.md) | `from foundry_sdk.v2.connectivity.models import SnowflakeExternalOauth` |
**Connectivity** | [SnowflakeKeyPairAuthentication](docs/v2/Connectivity/models/SnowflakeKeyPairAuthentication.md) | `from foundry_sdk.v2.connectivity.models import SnowflakeKeyPairAuthentication` |
**Connectivity** | [SnowflakeTableImportConfig](docs/v2/Connectivity/models/SnowflakeTableImportConfig.md) | `from foundry_sdk.v2.connectivity.models import SnowflakeTableImportConfig` |
**Connectivity** | [SnowflakeVirtualTableConfig](docs/v2/Connectivity/models/SnowflakeVirtualTableConfig.md) | `from foundry_sdk.v2.connectivity.models import SnowflakeVirtualTableConfig` |
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
**Connectivity** | [TableName](docs/v2/Connectivity/models/TableName.md) | `from foundry_sdk.v2.connectivity.models import TableName` |
**Connectivity** | [TableRid](docs/v2/Connectivity/models/TableRid.md) | `from foundry_sdk.v2.connectivity.models import TableRid` |
**Connectivity** | [TimestampColumnInitialIncrementalState](docs/v2/Connectivity/models/TimestampColumnInitialIncrementalState.md) | `from foundry_sdk.v2.connectivity.models import TimestampColumnInitialIncrementalState` |
**Connectivity** | [UnityVirtualTableConfig](docs/v2/Connectivity/models/UnityVirtualTableConfig.md) | `from foundry_sdk.v2.connectivity.models import UnityVirtualTableConfig` |
**Connectivity** | [UnknownWorker](docs/v2/Connectivity/models/UnknownWorker.md) | `from foundry_sdk.v2.connectivity.models import UnknownWorker` |
**Connectivity** | [UpdateExportSettingsForConnectionRequest](docs/v2/Connectivity/models/UpdateExportSettingsForConnectionRequest.md) | `from foundry_sdk.v2.connectivity.models import UpdateExportSettingsForConnectionRequest` |
**Connectivity** | [UpdateSecretsForConnectionRequest](docs/v2/Connectivity/models/UpdateSecretsForConnectionRequest.md) | `from foundry_sdk.v2.connectivity.models import UpdateSecretsForConnectionRequest` |
**Connectivity** | [UriScheme](docs/v2/Connectivity/models/UriScheme.md) | `from foundry_sdk.v2.connectivity.models import UriScheme` |
**Connectivity** | [VirtualTable](docs/v2/Connectivity/models/VirtualTable.md) | `from foundry_sdk.v2.connectivity.models import VirtualTable` |
**Connectivity** | [VirtualTableConfig](docs/v2/Connectivity/models/VirtualTableConfig.md) | `from foundry_sdk.v2.connectivity.models import VirtualTableConfig` |
**Connectivity** | [WorkflowIdentityFederation](docs/v2/Connectivity/models/WorkflowIdentityFederation.md) | `from foundry_sdk.v2.connectivity.models import WorkflowIdentityFederation` |
**Core** | [AnyType](docs/v2/Core/models/AnyType.md) | `from foundry_sdk.v2.core.models import AnyType` |
**Core** | [ArrayFieldType](docs/v2/Core/models/ArrayFieldType.md) | `from foundry_sdk.v2.core.models import ArrayFieldType` |
**Core** | [AttachmentType](docs/v2/Core/models/AttachmentType.md) | `from foundry_sdk.v2.core.models import AttachmentType` |
**Core** | [Attribution](docs/v2/Core/models/Attribution.md) | `from foundry_sdk.v2.core.models import Attribution` |
**Core** | [BinaryType](docs/v2/Core/models/BinaryType.md) | `from foundry_sdk.v2.core.models import BinaryType` |
**Core** | [BooleanType](docs/v2/Core/models/BooleanType.md) | `from foundry_sdk.v2.core.models import BooleanType` |
**Core** | [BranchMetadata](docs/v2/Core/models/BranchMetadata.md) | `from foundry_sdk.v2.core.models import BranchMetadata` |
**Core** | [BranchName](docs/v2/Core/models/BranchName.md) | `from foundry_sdk.v2.core.models import BranchName` |
**Core** | [BuildRid](docs/v2/Core/models/BuildRid.md) | `from foundry_sdk.v2.core.models import BuildRid` |
**Core** | [ByteType](docs/v2/Core/models/ByteType.md) | `from foundry_sdk.v2.core.models import ByteType` |
**Core** | [ChangeDataCaptureConfiguration](docs/v2/Core/models/ChangeDataCaptureConfiguration.md) | `from foundry_sdk.v2.core.models import ChangeDataCaptureConfiguration` |
**Core** | [CheckReportRid](docs/v2/Core/models/CheckReportRid.md) | `from foundry_sdk.v2.core.models import CheckReportRid` |
**Core** | [CheckRid](docs/v2/Core/models/CheckRid.md) | `from foundry_sdk.v2.core.models import CheckRid` |
**Core** | [CipherTextType](docs/v2/Core/models/CipherTextType.md) | `from foundry_sdk.v2.core.models import CipherTextType` |
**Core** | [ColumnName](docs/v2/Core/models/ColumnName.md) | `from foundry_sdk.v2.core.models import ColumnName` |
**Core** | [ComputeSeconds](docs/v2/Core/models/ComputeSeconds.md) | `from foundry_sdk.v2.core.models import ComputeSeconds` |
**Core** | [ContentLength](docs/v2/Core/models/ContentLength.md) | `from foundry_sdk.v2.core.models import ContentLength` |
**Core** | [ContentType](docs/v2/Core/models/ContentType.md) | `from foundry_sdk.v2.core.models import ContentType` |
**Core** | [CreatedBy](docs/v2/Core/models/CreatedBy.md) | `from foundry_sdk.v2.core.models import CreatedBy` |
**Core** | [CreatedTime](docs/v2/Core/models/CreatedTime.md) | `from foundry_sdk.v2.core.models import CreatedTime` |
**Core** | [CustomMetadata](docs/v2/Core/models/CustomMetadata.md) | `from foundry_sdk.v2.core.models import CustomMetadata` |
**Core** | [DatasetFieldSchema](docs/v2/Core/models/DatasetFieldSchema.md) | `from foundry_sdk.v2.core.models import DatasetFieldSchema` |
**Core** | [DatasetRid](docs/v2/Core/models/DatasetRid.md) | `from foundry_sdk.v2.core.models import DatasetRid` |
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
**Core** | [GroupId](docs/v2/Core/models/GroupId.md) | `from foundry_sdk.v2.core.models import GroupId` |
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
**Core** | [NetworkEgressPolicyRid](docs/v2/Core/models/NetworkEgressPolicyRid.md) | `from foundry_sdk.v2.core.models import NetworkEgressPolicyRid` |
**Core** | [NullType](docs/v2/Core/models/NullType.md) | `from foundry_sdk.v2.core.models import NullType` |
**Core** | [NumericOrNonNumericType](docs/v2/Core/models/NumericOrNonNumericType.md) | `from foundry_sdk.v2.core.models import NumericOrNonNumericType` |
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
**Core** | [SchemaFieldType](docs/v2/Core/models/SchemaFieldType.md) | `from foundry_sdk.v2.core.models import SchemaFieldType` |
**Core** | [ShortType](docs/v2/Core/models/ShortType.md) | `from foundry_sdk.v2.core.models import ShortType` |
**Core** | [SizeBytes](docs/v2/Core/models/SizeBytes.md) | `from foundry_sdk.v2.core.models import SizeBytes` |
**Core** | [StreamSchema](docs/v2/Core/models/StreamSchema.md) | `from foundry_sdk.v2.core.models import StreamSchema` |
**Core** | [StringType](docs/v2/Core/models/StringType.md) | `from foundry_sdk.v2.core.models import StringType` |
**Core** | [StructFieldName](docs/v2/Core/models/StructFieldName.md) | `from foundry_sdk.v2.core.models import StructFieldName` |
**Core** | [StructFieldType](docs/v2/Core/models/StructFieldType.md) | `from foundry_sdk.v2.core.models import StructFieldType` |
**Core** | [TableRid](docs/v2/Core/models/TableRid.md) | `from foundry_sdk.v2.core.models import TableRid` |
**Core** | [TimeSeriesItemType](docs/v2/Core/models/TimeSeriesItemType.md) | `from foundry_sdk.v2.core.models import TimeSeriesItemType` |
**Core** | [TimeseriesType](docs/v2/Core/models/TimeseriesType.md) | `from foundry_sdk.v2.core.models import TimeseriesType` |
**Core** | [TimestampType](docs/v2/Core/models/TimestampType.md) | `from foundry_sdk.v2.core.models import TimestampType` |
**Core** | [TimeUnit](docs/v2/Core/models/TimeUnit.md) | `from foundry_sdk.v2.core.models import TimeUnit` |
**Core** | [TotalCount](docs/v2/Core/models/TotalCount.md) | `from foundry_sdk.v2.core.models import TotalCount` |
**Core** | [TraceParent](docs/v2/Core/models/TraceParent.md) | `from foundry_sdk.v2.core.models import TraceParent` |
**Core** | [TraceState](docs/v2/Core/models/TraceState.md) | `from foundry_sdk.v2.core.models import TraceState` |
**Core** | [UnsupportedType](docs/v2/Core/models/UnsupportedType.md) | `from foundry_sdk.v2.core.models import UnsupportedType` |
**Core** | [UnsupportedTypeParamKey](docs/v2/Core/models/UnsupportedTypeParamKey.md) | `from foundry_sdk.v2.core.models import UnsupportedTypeParamKey` |
**Core** | [UnsupportedTypeParamValue](docs/v2/Core/models/UnsupportedTypeParamValue.md) | `from foundry_sdk.v2.core.models import UnsupportedTypeParamValue` |
**Core** | [UpdatedBy](docs/v2/Core/models/UpdatedBy.md) | `from foundry_sdk.v2.core.models import UpdatedBy` |
**Core** | [UpdatedTime](docs/v2/Core/models/UpdatedTime.md) | `from foundry_sdk.v2.core.models import UpdatedTime` |
**Core** | [UserId](docs/v2/Core/models/UserId.md) | `from foundry_sdk.v2.core.models import UserId` |
**Core** | [UserStatus](docs/v2/Core/models/UserStatus.md) | `from foundry_sdk.v2.core.models import UserStatus` |
**Core** | [VectorSimilarityFunction](docs/v2/Core/models/VectorSimilarityFunction.md) | `from foundry_sdk.v2.core.models import VectorSimilarityFunction` |
**Core** | [VectorSimilarityFunctionValue](docs/v2/Core/models/VectorSimilarityFunctionValue.md) | `from foundry_sdk.v2.core.models import VectorSimilarityFunctionValue` |
**Core** | [VectorType](docs/v2/Core/models/VectorType.md) | `from foundry_sdk.v2.core.models import VectorType` |
**Core** | [VersionId](docs/v2/Core/models/VersionId.md) | `from foundry_sdk.v2.core.models import VersionId` |
**Core** | [VoidType](docs/v2/Core/models/VoidType.md) | `from foundry_sdk.v2.core.models import VoidType` |
**Core** | [ZoneId](docs/v2/Core/models/ZoneId.md) | `from foundry_sdk.v2.core.models import ZoneId` |
**DataHealth** | [AllowedColumnValuesCheckConfig](docs/v2/DataHealth/models/AllowedColumnValuesCheckConfig.md) | `from foundry_sdk.v2.data_health.models import AllowedColumnValuesCheckConfig` |
**DataHealth** | [ApproximateUniquePercentageCheckConfig](docs/v2/DataHealth/models/ApproximateUniquePercentageCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ApproximateUniquePercentageCheckConfig` |
**DataHealth** | [BooleanColumnValue](docs/v2/DataHealth/models/BooleanColumnValue.md) | `from foundry_sdk.v2.data_health.models import BooleanColumnValue` |
**DataHealth** | [BuildDurationCheckConfig](docs/v2/DataHealth/models/BuildDurationCheckConfig.md) | `from foundry_sdk.v2.data_health.models import BuildDurationCheckConfig` |
**DataHealth** | [BuildStatusCheckConfig](docs/v2/DataHealth/models/BuildStatusCheckConfig.md) | `from foundry_sdk.v2.data_health.models import BuildStatusCheckConfig` |
**DataHealth** | [Check](docs/v2/DataHealth/models/Check.md) | `from foundry_sdk.v2.data_health.models import Check` |
**DataHealth** | [CheckConfig](docs/v2/DataHealth/models/CheckConfig.md) | `from foundry_sdk.v2.data_health.models import CheckConfig` |
**DataHealth** | [CheckGroupRid](docs/v2/DataHealth/models/CheckGroupRid.md) | `from foundry_sdk.v2.data_health.models import CheckGroupRid` |
**DataHealth** | [CheckIntent](docs/v2/DataHealth/models/CheckIntent.md) | `from foundry_sdk.v2.data_health.models import CheckIntent` |
**DataHealth** | [CheckReport](docs/v2/DataHealth/models/CheckReport.md) | `from foundry_sdk.v2.data_health.models import CheckReport` |
**DataHealth** | [CheckReportLimit](docs/v2/DataHealth/models/CheckReportLimit.md) | `from foundry_sdk.v2.data_health.models import CheckReportLimit` |
**DataHealth** | [CheckResult](docs/v2/DataHealth/models/CheckResult.md) | `from foundry_sdk.v2.data_health.models import CheckResult` |
**DataHealth** | [CheckResultStatus](docs/v2/DataHealth/models/CheckResultStatus.md) | `from foundry_sdk.v2.data_health.models import CheckResultStatus` |
**DataHealth** | [ColumnCountConfig](docs/v2/DataHealth/models/ColumnCountConfig.md) | `from foundry_sdk.v2.data_health.models import ColumnCountConfig` |
**DataHealth** | [ColumnInfo](docs/v2/DataHealth/models/ColumnInfo.md) | `from foundry_sdk.v2.data_health.models import ColumnInfo` |
**DataHealth** | [ColumnName](docs/v2/DataHealth/models/ColumnName.md) | `from foundry_sdk.v2.data_health.models import ColumnName` |
**DataHealth** | [ColumnTypeCheckConfig](docs/v2/DataHealth/models/ColumnTypeCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ColumnTypeCheckConfig` |
**DataHealth** | [ColumnTypeConfig](docs/v2/DataHealth/models/ColumnTypeConfig.md) | `from foundry_sdk.v2.data_health.models import ColumnTypeConfig` |
**DataHealth** | [ColumnValue](docs/v2/DataHealth/models/ColumnValue.md) | `from foundry_sdk.v2.data_health.models import ColumnValue` |
**DataHealth** | [CreateCheckRequest](docs/v2/DataHealth/models/CreateCheckRequest.md) | `from foundry_sdk.v2.data_health.models import CreateCheckRequest` |
**DataHealth** | [DatasetSubject](docs/v2/DataHealth/models/DatasetSubject.md) | `from foundry_sdk.v2.data_health.models import DatasetSubject` |
**DataHealth** | [DateBounds](docs/v2/DataHealth/models/DateBounds.md) | `from foundry_sdk.v2.data_health.models import DateBounds` |
**DataHealth** | [DateBoundsConfig](docs/v2/DataHealth/models/DateBoundsConfig.md) | `from foundry_sdk.v2.data_health.models import DateBoundsConfig` |
**DataHealth** | [DateColumnRangeCheckConfig](docs/v2/DataHealth/models/DateColumnRangeCheckConfig.md) | `from foundry_sdk.v2.data_health.models import DateColumnRangeCheckConfig` |
**DataHealth** | [DateColumnValue](docs/v2/DataHealth/models/DateColumnValue.md) | `from foundry_sdk.v2.data_health.models import DateColumnValue` |
**DataHealth** | [EscalationConfig](docs/v2/DataHealth/models/EscalationConfig.md) | `from foundry_sdk.v2.data_health.models import EscalationConfig` |
**DataHealth** | [GetLatestCheckReportsResponse](docs/v2/DataHealth/models/GetLatestCheckReportsResponse.md) | `from foundry_sdk.v2.data_health.models import GetLatestCheckReportsResponse` |
**DataHealth** | [IgnoreEmptyTransactions](docs/v2/DataHealth/models/IgnoreEmptyTransactions.md) | `from foundry_sdk.v2.data_health.models import IgnoreEmptyTransactions` |
**DataHealth** | [JobDurationCheckConfig](docs/v2/DataHealth/models/JobDurationCheckConfig.md) | `from foundry_sdk.v2.data_health.models import JobDurationCheckConfig` |
**DataHealth** | [JobStatusCheckConfig](docs/v2/DataHealth/models/JobStatusCheckConfig.md) | `from foundry_sdk.v2.data_health.models import JobStatusCheckConfig` |
**DataHealth** | [MedianDeviation](docs/v2/DataHealth/models/MedianDeviation.md) | `from foundry_sdk.v2.data_health.models import MedianDeviation` |
**DataHealth** | [MedianDeviationBoundsType](docs/v2/DataHealth/models/MedianDeviationBoundsType.md) | `from foundry_sdk.v2.data_health.models import MedianDeviationBoundsType` |
**DataHealth** | [MedianDeviationConfig](docs/v2/DataHealth/models/MedianDeviationConfig.md) | `from foundry_sdk.v2.data_health.models import MedianDeviationConfig` |
**DataHealth** | [NullPercentageCheckConfig](docs/v2/DataHealth/models/NullPercentageCheckConfig.md) | `from foundry_sdk.v2.data_health.models import NullPercentageCheckConfig` |
**DataHealth** | [NumericBounds](docs/v2/DataHealth/models/NumericBounds.md) | `from foundry_sdk.v2.data_health.models import NumericBounds` |
**DataHealth** | [NumericBoundsConfig](docs/v2/DataHealth/models/NumericBoundsConfig.md) | `from foundry_sdk.v2.data_health.models import NumericBoundsConfig` |
**DataHealth** | [NumericColumnCheckConfig](docs/v2/DataHealth/models/NumericColumnCheckConfig.md) | `from foundry_sdk.v2.data_health.models import NumericColumnCheckConfig` |
**DataHealth** | [NumericColumnMeanCheckConfig](docs/v2/DataHealth/models/NumericColumnMeanCheckConfig.md) | `from foundry_sdk.v2.data_health.models import NumericColumnMeanCheckConfig` |
**DataHealth** | [NumericColumnMedianCheckConfig](docs/v2/DataHealth/models/NumericColumnMedianCheckConfig.md) | `from foundry_sdk.v2.data_health.models import NumericColumnMedianCheckConfig` |
**DataHealth** | [NumericColumnRangeCheckConfig](docs/v2/DataHealth/models/NumericColumnRangeCheckConfig.md) | `from foundry_sdk.v2.data_health.models import NumericColumnRangeCheckConfig` |
**DataHealth** | [NumericColumnValue](docs/v2/DataHealth/models/NumericColumnValue.md) | `from foundry_sdk.v2.data_health.models import NumericColumnValue` |
**DataHealth** | [PercentageBounds](docs/v2/DataHealth/models/PercentageBounds.md) | `from foundry_sdk.v2.data_health.models import PercentageBounds` |
**DataHealth** | [PercentageBoundsConfig](docs/v2/DataHealth/models/PercentageBoundsConfig.md) | `from foundry_sdk.v2.data_health.models import PercentageBoundsConfig` |
**DataHealth** | [PercentageCheckConfig](docs/v2/DataHealth/models/PercentageCheckConfig.md) | `from foundry_sdk.v2.data_health.models import PercentageCheckConfig` |
**DataHealth** | [PercentageValue](docs/v2/DataHealth/models/PercentageValue.md) | `from foundry_sdk.v2.data_health.models import PercentageValue` |
**DataHealth** | [PrimaryKeyCheckConfig](docs/v2/DataHealth/models/PrimaryKeyCheckConfig.md) | `from foundry_sdk.v2.data_health.models import PrimaryKeyCheckConfig` |
**DataHealth** | [PrimaryKeyConfig](docs/v2/DataHealth/models/PrimaryKeyConfig.md) | `from foundry_sdk.v2.data_health.models import PrimaryKeyConfig` |
**DataHealth** | [ReplaceAllowedColumnValuesCheckConfig](docs/v2/DataHealth/models/ReplaceAllowedColumnValuesCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceAllowedColumnValuesCheckConfig` |
**DataHealth** | [ReplaceApproximateUniquePercentageCheckConfig](docs/v2/DataHealth/models/ReplaceApproximateUniquePercentageCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceApproximateUniquePercentageCheckConfig` |
**DataHealth** | [ReplaceBuildDurationCheckConfig](docs/v2/DataHealth/models/ReplaceBuildDurationCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceBuildDurationCheckConfig` |
**DataHealth** | [ReplaceBuildStatusCheckConfig](docs/v2/DataHealth/models/ReplaceBuildStatusCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceBuildStatusCheckConfig` |
**DataHealth** | [ReplaceCheckConfig](docs/v2/DataHealth/models/ReplaceCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceCheckConfig` |
**DataHealth** | [ReplaceCheckRequest](docs/v2/DataHealth/models/ReplaceCheckRequest.md) | `from foundry_sdk.v2.data_health.models import ReplaceCheckRequest` |
**DataHealth** | [ReplaceColumnTypeCheckConfig](docs/v2/DataHealth/models/ReplaceColumnTypeCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceColumnTypeCheckConfig` |
**DataHealth** | [ReplaceColumnTypeConfig](docs/v2/DataHealth/models/ReplaceColumnTypeConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceColumnTypeConfig` |
**DataHealth** | [ReplaceDateColumnRangeCheckConfig](docs/v2/DataHealth/models/ReplaceDateColumnRangeCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceDateColumnRangeCheckConfig` |
**DataHealth** | [ReplaceJobDurationCheckConfig](docs/v2/DataHealth/models/ReplaceJobDurationCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceJobDurationCheckConfig` |
**DataHealth** | [ReplaceJobStatusCheckConfig](docs/v2/DataHealth/models/ReplaceJobStatusCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceJobStatusCheckConfig` |
**DataHealth** | [ReplaceNullPercentageCheckConfig](docs/v2/DataHealth/models/ReplaceNullPercentageCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceNullPercentageCheckConfig` |
**DataHealth** | [ReplaceNumericColumnCheckConfig](docs/v2/DataHealth/models/ReplaceNumericColumnCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceNumericColumnCheckConfig` |
**DataHealth** | [ReplaceNumericColumnMeanCheckConfig](docs/v2/DataHealth/models/ReplaceNumericColumnMeanCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceNumericColumnMeanCheckConfig` |
**DataHealth** | [ReplaceNumericColumnMedianCheckConfig](docs/v2/DataHealth/models/ReplaceNumericColumnMedianCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceNumericColumnMedianCheckConfig` |
**DataHealth** | [ReplaceNumericColumnRangeCheckConfig](docs/v2/DataHealth/models/ReplaceNumericColumnRangeCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceNumericColumnRangeCheckConfig` |
**DataHealth** | [ReplacePercentageCheckConfig](docs/v2/DataHealth/models/ReplacePercentageCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplacePercentageCheckConfig` |
**DataHealth** | [ReplacePrimaryKeyCheckConfig](docs/v2/DataHealth/models/ReplacePrimaryKeyCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplacePrimaryKeyCheckConfig` |
**DataHealth** | [ReplacePrimaryKeyConfig](docs/v2/DataHealth/models/ReplacePrimaryKeyConfig.md) | `from foundry_sdk.v2.data_health.models import ReplacePrimaryKeyConfig` |
**DataHealth** | [ReplaceSchemaComparisonCheckConfig](docs/v2/DataHealth/models/ReplaceSchemaComparisonCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceSchemaComparisonCheckConfig` |
**DataHealth** | [ReplaceTimeSinceLastUpdatedCheckConfig](docs/v2/DataHealth/models/ReplaceTimeSinceLastUpdatedCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceTimeSinceLastUpdatedCheckConfig` |
**DataHealth** | [ReplaceTotalColumnCountCheckConfig](docs/v2/DataHealth/models/ReplaceTotalColumnCountCheckConfig.md) | `from foundry_sdk.v2.data_health.models import ReplaceTotalColumnCountCheckConfig` |
**DataHealth** | [SchemaComparisonCheckConfig](docs/v2/DataHealth/models/SchemaComparisonCheckConfig.md) | `from foundry_sdk.v2.data_health.models import SchemaComparisonCheckConfig` |
**DataHealth** | [SchemaComparisonConfig](docs/v2/DataHealth/models/SchemaComparisonConfig.md) | `from foundry_sdk.v2.data_health.models import SchemaComparisonConfig` |
**DataHealth** | [SchemaComparisonType](docs/v2/DataHealth/models/SchemaComparisonType.md) | `from foundry_sdk.v2.data_health.models import SchemaComparisonType` |
**DataHealth** | [SchemaInfo](docs/v2/DataHealth/models/SchemaInfo.md) | `from foundry_sdk.v2.data_health.models import SchemaInfo` |
**DataHealth** | [SeverityLevel](docs/v2/DataHealth/models/SeverityLevel.md) | `from foundry_sdk.v2.data_health.models import SeverityLevel` |
**DataHealth** | [StatusCheckConfig](docs/v2/DataHealth/models/StatusCheckConfig.md) | `from foundry_sdk.v2.data_health.models import StatusCheckConfig` |
**DataHealth** | [StringColumnValue](docs/v2/DataHealth/models/StringColumnValue.md) | `from foundry_sdk.v2.data_health.models import StringColumnValue` |
**DataHealth** | [TimeBounds](docs/v2/DataHealth/models/TimeBounds.md) | `from foundry_sdk.v2.data_health.models import TimeBounds` |
**DataHealth** | [TimeBoundsConfig](docs/v2/DataHealth/models/TimeBoundsConfig.md) | `from foundry_sdk.v2.data_health.models import TimeBoundsConfig` |
**DataHealth** | [TimeCheckConfig](docs/v2/DataHealth/models/TimeCheckConfig.md) | `from foundry_sdk.v2.data_health.models import TimeCheckConfig` |
**DataHealth** | [TimeSinceLastUpdatedCheckConfig](docs/v2/DataHealth/models/TimeSinceLastUpdatedCheckConfig.md) | `from foundry_sdk.v2.data_health.models import TimeSinceLastUpdatedCheckConfig` |
**DataHealth** | [TotalColumnCountCheckConfig](docs/v2/DataHealth/models/TotalColumnCountCheckConfig.md) | `from foundry_sdk.v2.data_health.models import TotalColumnCountCheckConfig` |
**DataHealth** | [TransactionTimeCheckConfig](docs/v2/DataHealth/models/TransactionTimeCheckConfig.md) | `from foundry_sdk.v2.data_health.models import TransactionTimeCheckConfig` |
**DataHealth** | [TrendConfig](docs/v2/DataHealth/models/TrendConfig.md) | `from foundry_sdk.v2.data_health.models import TrendConfig` |
**DataHealth** | [TrendType](docs/v2/DataHealth/models/TrendType.md) | `from foundry_sdk.v2.data_health.models import TrendType` |
**Datasets** | [AddBackingDatasetsRequest](docs/v2/Datasets/models/AddBackingDatasetsRequest.md) | `from foundry_sdk.v2.datasets.models import AddBackingDatasetsRequest` |
**Datasets** | [AddPrimaryKeyRequest](docs/v2/Datasets/models/AddPrimaryKeyRequest.md) | `from foundry_sdk.v2.datasets.models import AddPrimaryKeyRequest` |
**Datasets** | [Branch](docs/v2/Datasets/models/Branch.md) | `from foundry_sdk.v2.datasets.models import Branch` |
**Datasets** | [CreateBranchRequest](docs/v2/Datasets/models/CreateBranchRequest.md) | `from foundry_sdk.v2.datasets.models import CreateBranchRequest` |
**Datasets** | [CreateDatasetRequest](docs/v2/Datasets/models/CreateDatasetRequest.md) | `from foundry_sdk.v2.datasets.models import CreateDatasetRequest` |
**Datasets** | [CreateTransactionRequest](docs/v2/Datasets/models/CreateTransactionRequest.md) | `from foundry_sdk.v2.datasets.models import CreateTransactionRequest` |
**Datasets** | [CreateViewRequest](docs/v2/Datasets/models/CreateViewRequest.md) | `from foundry_sdk.v2.datasets.models import CreateViewRequest` |
**Datasets** | [DataframeReader](docs/v2/Datasets/models/DataframeReader.md) | `from foundry_sdk.v2.datasets.models import DataframeReader` |
**Datasets** | [Dataset](docs/v2/Datasets/models/Dataset.md) | `from foundry_sdk.v2.datasets.models import Dataset` |
**Datasets** | [DatasetName](docs/v2/Datasets/models/DatasetName.md) | `from foundry_sdk.v2.datasets.models import DatasetName` |
**Datasets** | [File](docs/v2/Datasets/models/File.md) | `from foundry_sdk.v2.datasets.models import File` |
**Datasets** | [FileUpdatedTime](docs/v2/Datasets/models/FileUpdatedTime.md) | `from foundry_sdk.v2.datasets.models import FileUpdatedTime` |
**Datasets** | [GetDatasetJobsAndFilter](docs/v2/Datasets/models/GetDatasetJobsAndFilter.md) | `from foundry_sdk.v2.datasets.models import GetDatasetJobsAndFilter` |
**Datasets** | [GetDatasetJobsComparisonType](docs/v2/Datasets/models/GetDatasetJobsComparisonType.md) | `from foundry_sdk.v2.datasets.models import GetDatasetJobsComparisonType` |
**Datasets** | [GetDatasetJobsOrFilter](docs/v2/Datasets/models/GetDatasetJobsOrFilter.md) | `from foundry_sdk.v2.datasets.models import GetDatasetJobsOrFilter` |
**Datasets** | [GetDatasetJobsQuery](docs/v2/Datasets/models/GetDatasetJobsQuery.md) | `from foundry_sdk.v2.datasets.models import GetDatasetJobsQuery` |
**Datasets** | [GetDatasetJobsRequest](docs/v2/Datasets/models/GetDatasetJobsRequest.md) | `from foundry_sdk.v2.datasets.models import GetDatasetJobsRequest` |
**Datasets** | [GetDatasetJobsSort](docs/v2/Datasets/models/GetDatasetJobsSort.md) | `from foundry_sdk.v2.datasets.models import GetDatasetJobsSort` |
**Datasets** | [GetDatasetJobsSortDirection](docs/v2/Datasets/models/GetDatasetJobsSortDirection.md) | `from foundry_sdk.v2.datasets.models import GetDatasetJobsSortDirection` |
**Datasets** | [GetDatasetJobsSortType](docs/v2/Datasets/models/GetDatasetJobsSortType.md) | `from foundry_sdk.v2.datasets.models import GetDatasetJobsSortType` |
**Datasets** | [GetDatasetJobsTimeFilter](docs/v2/Datasets/models/GetDatasetJobsTimeFilter.md) | `from foundry_sdk.v2.datasets.models import GetDatasetJobsTimeFilter` |
**Datasets** | [GetDatasetJobsTimeFilterField](docs/v2/Datasets/models/GetDatasetJobsTimeFilterField.md) | `from foundry_sdk.v2.datasets.models import GetDatasetJobsTimeFilterField` |
**Datasets** | [GetDatasetSchemaResponse](docs/v2/Datasets/models/GetDatasetSchemaResponse.md) | `from foundry_sdk.v2.datasets.models import GetDatasetSchemaResponse` |
**Datasets** | [GetHealthCheckReportsResponse](docs/v2/Datasets/models/GetHealthCheckReportsResponse.md) | `from foundry_sdk.v2.datasets.models import GetHealthCheckReportsResponse` |
**Datasets** | [GetJobResponse](docs/v2/Datasets/models/GetJobResponse.md) | `from foundry_sdk.v2.datasets.models import GetJobResponse` |
**Datasets** | [GetSchemaDatasetsBatchRequestElement](docs/v2/Datasets/models/GetSchemaDatasetsBatchRequestElement.md) | `from foundry_sdk.v2.datasets.models import GetSchemaDatasetsBatchRequestElement` |
**Datasets** | [GetSchemaDatasetsBatchResponse](docs/v2/Datasets/models/GetSchemaDatasetsBatchResponse.md) | `from foundry_sdk.v2.datasets.models import GetSchemaDatasetsBatchResponse` |
**Datasets** | [JobDetails](docs/v2/Datasets/models/JobDetails.md) | `from foundry_sdk.v2.datasets.models import JobDetails` |
**Datasets** | [ListBranchesResponse](docs/v2/Datasets/models/ListBranchesResponse.md) | `from foundry_sdk.v2.datasets.models import ListBranchesResponse` |
**Datasets** | [ListFilesResponse](docs/v2/Datasets/models/ListFilesResponse.md) | `from foundry_sdk.v2.datasets.models import ListFilesResponse` |
**Datasets** | [ListHealthChecksResponse](docs/v2/Datasets/models/ListHealthChecksResponse.md) | `from foundry_sdk.v2.datasets.models import ListHealthChecksResponse` |
**Datasets** | [ListSchedulesResponse](docs/v2/Datasets/models/ListSchedulesResponse.md) | `from foundry_sdk.v2.datasets.models import ListSchedulesResponse` |
**Datasets** | [ListTransactionsOfDatasetResponse](docs/v2/Datasets/models/ListTransactionsOfDatasetResponse.md) | `from foundry_sdk.v2.datasets.models import ListTransactionsOfDatasetResponse` |
**Datasets** | [ListTransactionsResponse](docs/v2/Datasets/models/ListTransactionsResponse.md) | `from foundry_sdk.v2.datasets.models import ListTransactionsResponse` |
**Datasets** | [PrimaryKeyLatestWinsResolutionStrategy](docs/v2/Datasets/models/PrimaryKeyLatestWinsResolutionStrategy.md) | `from foundry_sdk.v2.datasets.models import PrimaryKeyLatestWinsResolutionStrategy` |
**Datasets** | [PrimaryKeyResolutionDuplicate](docs/v2/Datasets/models/PrimaryKeyResolutionDuplicate.md) | `from foundry_sdk.v2.datasets.models import PrimaryKeyResolutionDuplicate` |
**Datasets** | [PrimaryKeyResolutionStrategy](docs/v2/Datasets/models/PrimaryKeyResolutionStrategy.md) | `from foundry_sdk.v2.datasets.models import PrimaryKeyResolutionStrategy` |
**Datasets** | [PrimaryKeyResolutionUnique](docs/v2/Datasets/models/PrimaryKeyResolutionUnique.md) | `from foundry_sdk.v2.datasets.models import PrimaryKeyResolutionUnique` |
**Datasets** | [PutDatasetSchemaRequest](docs/v2/Datasets/models/PutDatasetSchemaRequest.md) | `from foundry_sdk.v2.datasets.models import PutDatasetSchemaRequest` |
**Datasets** | [RemoveBackingDatasetsRequest](docs/v2/Datasets/models/RemoveBackingDatasetsRequest.md) | `from foundry_sdk.v2.datasets.models import RemoveBackingDatasetsRequest` |
**Datasets** | [ReplaceBackingDatasetsRequest](docs/v2/Datasets/models/ReplaceBackingDatasetsRequest.md) | `from foundry_sdk.v2.datasets.models import ReplaceBackingDatasetsRequest` |
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
**Filesystem** | [AddMarkingsRequest](docs/v2/Filesystem/models/AddMarkingsRequest.md) | `from foundry_sdk.v2.filesystem.models import AddMarkingsRequest` |
**Filesystem** | [AddOrganizationsRequest](docs/v2/Filesystem/models/AddOrganizationsRequest.md) | `from foundry_sdk.v2.filesystem.models import AddOrganizationsRequest` |
**Filesystem** | [AddResourceRolesRequest](docs/v2/Filesystem/models/AddResourceRolesRequest.md) | `from foundry_sdk.v2.filesystem.models import AddResourceRolesRequest` |
**Filesystem** | [CreateFolderRequest](docs/v2/Filesystem/models/CreateFolderRequest.md) | `from foundry_sdk.v2.filesystem.models import CreateFolderRequest` |
**Filesystem** | [CreateProjectFromTemplateRequest](docs/v2/Filesystem/models/CreateProjectFromTemplateRequest.md) | `from foundry_sdk.v2.filesystem.models import CreateProjectFromTemplateRequest` |
**Filesystem** | [CreateProjectRequest](docs/v2/Filesystem/models/CreateProjectRequest.md) | `from foundry_sdk.v2.filesystem.models import CreateProjectRequest` |
**Filesystem** | [CreateSpaceRequest](docs/v2/Filesystem/models/CreateSpaceRequest.md) | `from foundry_sdk.v2.filesystem.models import CreateSpaceRequest` |
**Filesystem** | [Everyone](docs/v2/Filesystem/models/Everyone.md) | `from foundry_sdk.v2.filesystem.models import Everyone` |
**Filesystem** | [FileSystemId](docs/v2/Filesystem/models/FileSystemId.md) | `from foundry_sdk.v2.filesystem.models import FileSystemId` |
**Filesystem** | [Folder](docs/v2/Filesystem/models/Folder.md) | `from foundry_sdk.v2.filesystem.models import Folder` |
**Filesystem** | [FolderRid](docs/v2/Filesystem/models/FolderRid.md) | `from foundry_sdk.v2.filesystem.models import FolderRid` |
**Filesystem** | [FolderType](docs/v2/Filesystem/models/FolderType.md) | `from foundry_sdk.v2.filesystem.models import FolderType` |
**Filesystem** | [GetByPathResourcesBatchRequestElement](docs/v2/Filesystem/models/GetByPathResourcesBatchRequestElement.md) | `from foundry_sdk.v2.filesystem.models import GetByPathResourcesBatchRequestElement` |
**Filesystem** | [GetByPathResourcesBatchResponse](docs/v2/Filesystem/models/GetByPathResourcesBatchResponse.md) | `from foundry_sdk.v2.filesystem.models import GetByPathResourcesBatchResponse` |
**Filesystem** | [GetFoldersBatchRequestElement](docs/v2/Filesystem/models/GetFoldersBatchRequestElement.md) | `from foundry_sdk.v2.filesystem.models import GetFoldersBatchRequestElement` |
**Filesystem** | [GetFoldersBatchResponse](docs/v2/Filesystem/models/GetFoldersBatchResponse.md) | `from foundry_sdk.v2.filesystem.models import GetFoldersBatchResponse` |
**Filesystem** | [GetResourcesBatchRequestElement](docs/v2/Filesystem/models/GetResourcesBatchRequestElement.md) | `from foundry_sdk.v2.filesystem.models import GetResourcesBatchRequestElement` |
**Filesystem** | [GetResourcesBatchResponse](docs/v2/Filesystem/models/GetResourcesBatchResponse.md) | `from foundry_sdk.v2.filesystem.models import GetResourcesBatchResponse` |
**Filesystem** | [IsDirectlyApplied](docs/v2/Filesystem/models/IsDirectlyApplied.md) | `from foundry_sdk.v2.filesystem.models import IsDirectlyApplied` |
**Filesystem** | [ListChildrenOfFolderResponse](docs/v2/Filesystem/models/ListChildrenOfFolderResponse.md) | `from foundry_sdk.v2.filesystem.models import ListChildrenOfFolderResponse` |
**Filesystem** | [ListMarkingsOfResourceResponse](docs/v2/Filesystem/models/ListMarkingsOfResourceResponse.md) | `from foundry_sdk.v2.filesystem.models import ListMarkingsOfResourceResponse` |
**Filesystem** | [ListOrganizationsOfProjectResponse](docs/v2/Filesystem/models/ListOrganizationsOfProjectResponse.md) | `from foundry_sdk.v2.filesystem.models import ListOrganizationsOfProjectResponse` |
**Filesystem** | [ListResourceRolesResponse](docs/v2/Filesystem/models/ListResourceRolesResponse.md) | `from foundry_sdk.v2.filesystem.models import ListResourceRolesResponse` |
**Filesystem** | [ListSpacesResponse](docs/v2/Filesystem/models/ListSpacesResponse.md) | `from foundry_sdk.v2.filesystem.models import ListSpacesResponse` |
**Filesystem** | [Marking](docs/v2/Filesystem/models/Marking.md) | `from foundry_sdk.v2.filesystem.models import Marking` |
**Filesystem** | [Organization](docs/v2/Filesystem/models/Organization.md) | `from foundry_sdk.v2.filesystem.models import Organization` |
**Filesystem** | [PrincipalIdOnly](docs/v2/Filesystem/models/PrincipalIdOnly.md) | `from foundry_sdk.v2.filesystem.models import PrincipalIdOnly` |
**Filesystem** | [PrincipalWithId](docs/v2/Filesystem/models/PrincipalWithId.md) | `from foundry_sdk.v2.filesystem.models import PrincipalWithId` |
**Filesystem** | [Project](docs/v2/Filesystem/models/Project.md) | `from foundry_sdk.v2.filesystem.models import Project` |
**Filesystem** | [ProjectRid](docs/v2/Filesystem/models/ProjectRid.md) | `from foundry_sdk.v2.filesystem.models import ProjectRid` |
**Filesystem** | [ProjectTemplateRid](docs/v2/Filesystem/models/ProjectTemplateRid.md) | `from foundry_sdk.v2.filesystem.models import ProjectTemplateRid` |
**Filesystem** | [ProjectTemplateVariableId](docs/v2/Filesystem/models/ProjectTemplateVariableId.md) | `from foundry_sdk.v2.filesystem.models import ProjectTemplateVariableId` |
**Filesystem** | [ProjectTemplateVariableValue](docs/v2/Filesystem/models/ProjectTemplateVariableValue.md) | `from foundry_sdk.v2.filesystem.models import ProjectTemplateVariableValue` |
**Filesystem** | [RemoveMarkingsRequest](docs/v2/Filesystem/models/RemoveMarkingsRequest.md) | `from foundry_sdk.v2.filesystem.models import RemoveMarkingsRequest` |
**Filesystem** | [RemoveOrganizationsRequest](docs/v2/Filesystem/models/RemoveOrganizationsRequest.md) | `from foundry_sdk.v2.filesystem.models import RemoveOrganizationsRequest` |
**Filesystem** | [RemoveResourceRolesRequest](docs/v2/Filesystem/models/RemoveResourceRolesRequest.md) | `from foundry_sdk.v2.filesystem.models import RemoveResourceRolesRequest` |
**Filesystem** | [ReplaceProjectRequest](docs/v2/Filesystem/models/ReplaceProjectRequest.md) | `from foundry_sdk.v2.filesystem.models import ReplaceProjectRequest` |
**Filesystem** | [ReplaceSpaceRequest](docs/v2/Filesystem/models/ReplaceSpaceRequest.md) | `from foundry_sdk.v2.filesystem.models import ReplaceSpaceRequest` |
**Filesystem** | [Resource](docs/v2/Filesystem/models/Resource.md) | `from foundry_sdk.v2.filesystem.models import Resource` |
**Filesystem** | [ResourceDisplayName](docs/v2/Filesystem/models/ResourceDisplayName.md) | `from foundry_sdk.v2.filesystem.models import ResourceDisplayName` |
**Filesystem** | [ResourcePath](docs/v2/Filesystem/models/ResourcePath.md) | `from foundry_sdk.v2.filesystem.models import ResourcePath` |
**Filesystem** | [ResourceRid](docs/v2/Filesystem/models/ResourceRid.md) | `from foundry_sdk.v2.filesystem.models import ResourceRid` |
**Filesystem** | [ResourceRole](docs/v2/Filesystem/models/ResourceRole.md) | `from foundry_sdk.v2.filesystem.models import ResourceRole` |
**Filesystem** | [ResourceRoleIdentifier](docs/v2/Filesystem/models/ResourceRoleIdentifier.md) | `from foundry_sdk.v2.filesystem.models import ResourceRoleIdentifier` |
**Filesystem** | [ResourceRolePrincipal](docs/v2/Filesystem/models/ResourceRolePrincipal.md) | `from foundry_sdk.v2.filesystem.models import ResourceRolePrincipal` |
**Filesystem** | [ResourceRolePrincipalIdentifier](docs/v2/Filesystem/models/ResourceRolePrincipalIdentifier.md) | `from foundry_sdk.v2.filesystem.models import ResourceRolePrincipalIdentifier` |
**Filesystem** | [ResourceType](docs/v2/Filesystem/models/ResourceType.md) | `from foundry_sdk.v2.filesystem.models import ResourceType` |
**Filesystem** | [Space](docs/v2/Filesystem/models/Space.md) | `from foundry_sdk.v2.filesystem.models import Space` |
**Filesystem** | [SpaceMavenIdentifier](docs/v2/Filesystem/models/SpaceMavenIdentifier.md) | `from foundry_sdk.v2.filesystem.models import SpaceMavenIdentifier` |
**Filesystem** | [SpaceRid](docs/v2/Filesystem/models/SpaceRid.md) | `from foundry_sdk.v2.filesystem.models import SpaceRid` |
**Filesystem** | [TrashStatus](docs/v2/Filesystem/models/TrashStatus.md) | `from foundry_sdk.v2.filesystem.models import TrashStatus` |
**Filesystem** | [UsageAccountRid](docs/v2/Filesystem/models/UsageAccountRid.md) | `from foundry_sdk.v2.filesystem.models import UsageAccountRid` |
**Functions** | [ArrayConstraint](docs/v2/Functions/models/ArrayConstraint.md) | `from foundry_sdk.v2.functions.models import ArrayConstraint` |
**Functions** | [DataValue](docs/v2/Functions/models/DataValue.md) | `from foundry_sdk.v2.functions.models import DataValue` |
**Functions** | [EnumConstraint](docs/v2/Functions/models/EnumConstraint.md) | `from foundry_sdk.v2.functions.models import EnumConstraint` |
**Functions** | [ExecuteQueryRequest](docs/v2/Functions/models/ExecuteQueryRequest.md) | `from foundry_sdk.v2.functions.models import ExecuteQueryRequest` |
**Functions** | [ExecuteQueryResponse](docs/v2/Functions/models/ExecuteQueryResponse.md) | `from foundry_sdk.v2.functions.models import ExecuteQueryResponse` |
**Functions** | [FunctionRid](docs/v2/Functions/models/FunctionRid.md) | `from foundry_sdk.v2.functions.models import FunctionRid` |
**Functions** | [FunctionVersion](docs/v2/Functions/models/FunctionVersion.md) | `from foundry_sdk.v2.functions.models import FunctionVersion` |
**Functions** | [GetByRidQueriesBatchRequestElement](docs/v2/Functions/models/GetByRidQueriesBatchRequestElement.md) | `from foundry_sdk.v2.functions.models import GetByRidQueriesBatchRequestElement` |
**Functions** | [GetByRidQueriesBatchResponse](docs/v2/Functions/models/GetByRidQueriesBatchResponse.md) | `from foundry_sdk.v2.functions.models import GetByRidQueriesBatchResponse` |
**Functions** | [LengthConstraint](docs/v2/Functions/models/LengthConstraint.md) | `from foundry_sdk.v2.functions.models import LengthConstraint` |
**Functions** | [MapConstraint](docs/v2/Functions/models/MapConstraint.md) | `from foundry_sdk.v2.functions.models import MapConstraint` |
**Functions** | [NullableConstraint](docs/v2/Functions/models/NullableConstraint.md) | `from foundry_sdk.v2.functions.models import NullableConstraint` |
**Functions** | [NullableConstraintValue](docs/v2/Functions/models/NullableConstraintValue.md) | `from foundry_sdk.v2.functions.models import NullableConstraintValue` |
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
**Functions** | [RangesConstraint](docs/v2/Functions/models/RangesConstraint.md) | `from foundry_sdk.v2.functions.models import RangesConstraint` |
**Functions** | [RegexConstraint](docs/v2/Functions/models/RegexConstraint.md) | `from foundry_sdk.v2.functions.models import RegexConstraint` |
**Functions** | [RidConstraint](docs/v2/Functions/models/RidConstraint.md) | `from foundry_sdk.v2.functions.models import RidConstraint` |
**Functions** | [StreamingExecuteQueryRequest](docs/v2/Functions/models/StreamingExecuteQueryRequest.md) | `from foundry_sdk.v2.functions.models import StreamingExecuteQueryRequest` |
**Functions** | [StructConstraint](docs/v2/Functions/models/StructConstraint.md) | `from foundry_sdk.v2.functions.models import StructConstraint` |
**Functions** | [StructFieldApiName](docs/v2/Functions/models/StructFieldApiName.md) | `from foundry_sdk.v2.functions.models import StructFieldApiName` |
**Functions** | [StructFieldName](docs/v2/Functions/models/StructFieldName.md) | `from foundry_sdk.v2.functions.models import StructFieldName` |
**Functions** | [StructV1Constraint](docs/v2/Functions/models/StructV1Constraint.md) | `from foundry_sdk.v2.functions.models import StructV1Constraint` |
**Functions** | [ThreeDimensionalAggregation](docs/v2/Functions/models/ThreeDimensionalAggregation.md) | `from foundry_sdk.v2.functions.models import ThreeDimensionalAggregation` |
**Functions** | [TransactionId](docs/v2/Functions/models/TransactionId.md) | `from foundry_sdk.v2.functions.models import TransactionId` |
**Functions** | [TwoDimensionalAggregation](docs/v2/Functions/models/TwoDimensionalAggregation.md) | `from foundry_sdk.v2.functions.models import TwoDimensionalAggregation` |
**Functions** | [UuidConstraint](docs/v2/Functions/models/UuidConstraint.md) | `from foundry_sdk.v2.functions.models import UuidConstraint` |
**Functions** | [ValueType](docs/v2/Functions/models/ValueType.md) | `from foundry_sdk.v2.functions.models import ValueType` |
**Functions** | [ValueTypeApiName](docs/v2/Functions/models/ValueTypeApiName.md) | `from foundry_sdk.v2.functions.models import ValueTypeApiName` |
**Functions** | [ValueTypeConstraint](docs/v2/Functions/models/ValueTypeConstraint.md) | `from foundry_sdk.v2.functions.models import ValueTypeConstraint` |
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
**LanguageModels** | [AnthropicAnyToolChoice](docs/v2/LanguageModels/models/AnthropicAnyToolChoice.md) | `from foundry_sdk.v2.language_models.models import AnthropicAnyToolChoice` |
**LanguageModels** | [AnthropicAutoToolChoice](docs/v2/LanguageModels/models/AnthropicAutoToolChoice.md) | `from foundry_sdk.v2.language_models.models import AnthropicAutoToolChoice` |
**LanguageModels** | [AnthropicBase64PdfDocumentSource](docs/v2/LanguageModels/models/AnthropicBase64PdfDocumentSource.md) | `from foundry_sdk.v2.language_models.models import AnthropicBase64PdfDocumentSource` |
**LanguageModels** | [AnthropicCacheControl](docs/v2/LanguageModels/models/AnthropicCacheControl.md) | `from foundry_sdk.v2.language_models.models import AnthropicCacheControl` |
**LanguageModels** | [AnthropicCharacterLocationCitation](docs/v2/LanguageModels/models/AnthropicCharacterLocationCitation.md) | `from foundry_sdk.v2.language_models.models import AnthropicCharacterLocationCitation` |
**LanguageModels** | [AnthropicCompletionCitation](docs/v2/LanguageModels/models/AnthropicCompletionCitation.md) | `from foundry_sdk.v2.language_models.models import AnthropicCompletionCitation` |
**LanguageModels** | [AnthropicCompletionContent](docs/v2/LanguageModels/models/AnthropicCompletionContent.md) | `from foundry_sdk.v2.language_models.models import AnthropicCompletionContent` |
**LanguageModels** | [AnthropicCompletionRedactedThinking](docs/v2/LanguageModels/models/AnthropicCompletionRedactedThinking.md) | `from foundry_sdk.v2.language_models.models import AnthropicCompletionRedactedThinking` |
**LanguageModels** | [AnthropicCompletionText](docs/v2/LanguageModels/models/AnthropicCompletionText.md) | `from foundry_sdk.v2.language_models.models import AnthropicCompletionText` |
**LanguageModels** | [AnthropicCompletionThinking](docs/v2/LanguageModels/models/AnthropicCompletionThinking.md) | `from foundry_sdk.v2.language_models.models import AnthropicCompletionThinking` |
**LanguageModels** | [AnthropicCompletionToolUse](docs/v2/LanguageModels/models/AnthropicCompletionToolUse.md) | `from foundry_sdk.v2.language_models.models import AnthropicCompletionToolUse` |
**LanguageModels** | [AnthropicCustomTool](docs/v2/LanguageModels/models/AnthropicCustomTool.md) | `from foundry_sdk.v2.language_models.models import AnthropicCustomTool` |
**LanguageModels** | [AnthropicDisabledThinking](docs/v2/LanguageModels/models/AnthropicDisabledThinking.md) | `from foundry_sdk.v2.language_models.models import AnthropicDisabledThinking` |
**LanguageModels** | [AnthropicDisableParallelToolUse](docs/v2/LanguageModels/models/AnthropicDisableParallelToolUse.md) | `from foundry_sdk.v2.language_models.models import AnthropicDisableParallelToolUse` |
**LanguageModels** | [AnthropicDocument](docs/v2/LanguageModels/models/AnthropicDocument.md) | `from foundry_sdk.v2.language_models.models import AnthropicDocument` |
**LanguageModels** | [AnthropicDocumentCitations](docs/v2/LanguageModels/models/AnthropicDocumentCitations.md) | `from foundry_sdk.v2.language_models.models import AnthropicDocumentCitations` |
**LanguageModels** | [AnthropicDocumentSource](docs/v2/LanguageModels/models/AnthropicDocumentSource.md) | `from foundry_sdk.v2.language_models.models import AnthropicDocumentSource` |
**LanguageModels** | [AnthropicEffort](docs/v2/LanguageModels/models/AnthropicEffort.md) | `from foundry_sdk.v2.language_models.models import AnthropicEffort` |
**LanguageModels** | [AnthropicEnabledThinking](docs/v2/LanguageModels/models/AnthropicEnabledThinking.md) | `from foundry_sdk.v2.language_models.models import AnthropicEnabledThinking` |
**LanguageModels** | [AnthropicEphemeralCacheControl](docs/v2/LanguageModels/models/AnthropicEphemeralCacheControl.md) | `from foundry_sdk.v2.language_models.models import AnthropicEphemeralCacheControl` |
**LanguageModels** | [AnthropicImage](docs/v2/LanguageModels/models/AnthropicImage.md) | `from foundry_sdk.v2.language_models.models import AnthropicImage` |
**LanguageModels** | [AnthropicImageBase64Source](docs/v2/LanguageModels/models/AnthropicImageBase64Source.md) | `from foundry_sdk.v2.language_models.models import AnthropicImageBase64Source` |
**LanguageModels** | [AnthropicImageSource](docs/v2/LanguageModels/models/AnthropicImageSource.md) | `from foundry_sdk.v2.language_models.models import AnthropicImageSource` |
**LanguageModels** | [AnthropicJsonSchemaOutputFormat](docs/v2/LanguageModels/models/AnthropicJsonSchemaOutputFormat.md) | `from foundry_sdk.v2.language_models.models import AnthropicJsonSchemaOutputFormat` |
**LanguageModels** | [AnthropicMediaType](docs/v2/LanguageModels/models/AnthropicMediaType.md) | `from foundry_sdk.v2.language_models.models import AnthropicMediaType` |
**LanguageModels** | [AnthropicMessage](docs/v2/LanguageModels/models/AnthropicMessage.md) | `from foundry_sdk.v2.language_models.models import AnthropicMessage` |
**LanguageModels** | [AnthropicMessageContent](docs/v2/LanguageModels/models/AnthropicMessageContent.md) | `from foundry_sdk.v2.language_models.models import AnthropicMessageContent` |
**LanguageModels** | [AnthropicMessageRole](docs/v2/LanguageModels/models/AnthropicMessageRole.md) | `from foundry_sdk.v2.language_models.models import AnthropicMessageRole` |
**LanguageModels** | [AnthropicMessagesRequest](docs/v2/LanguageModels/models/AnthropicMessagesRequest.md) | `from foundry_sdk.v2.language_models.models import AnthropicMessagesRequest` |
**LanguageModels** | [AnthropicMessagesResponse](docs/v2/LanguageModels/models/AnthropicMessagesResponse.md) | `from foundry_sdk.v2.language_models.models import AnthropicMessagesResponse` |
**LanguageModels** | [AnthropicNoneToolChoice](docs/v2/LanguageModels/models/AnthropicNoneToolChoice.md) | `from foundry_sdk.v2.language_models.models import AnthropicNoneToolChoice` |
**LanguageModels** | [AnthropicOutputConfig](docs/v2/LanguageModels/models/AnthropicOutputConfig.md) | `from foundry_sdk.v2.language_models.models import AnthropicOutputConfig` |
**LanguageModels** | [AnthropicOutputFormat](docs/v2/LanguageModels/models/AnthropicOutputFormat.md) | `from foundry_sdk.v2.language_models.models import AnthropicOutputFormat` |
**LanguageModels** | [AnthropicRedactedThinking](docs/v2/LanguageModels/models/AnthropicRedactedThinking.md) | `from foundry_sdk.v2.language_models.models import AnthropicRedactedThinking` |
**LanguageModels** | [AnthropicSystemMessage](docs/v2/LanguageModels/models/AnthropicSystemMessage.md) | `from foundry_sdk.v2.language_models.models import AnthropicSystemMessage` |
**LanguageModels** | [AnthropicText](docs/v2/LanguageModels/models/AnthropicText.md) | `from foundry_sdk.v2.language_models.models import AnthropicText` |
**LanguageModels** | [AnthropicTextDocumentSource](docs/v2/LanguageModels/models/AnthropicTextDocumentSource.md) | `from foundry_sdk.v2.language_models.models import AnthropicTextDocumentSource` |
**LanguageModels** | [AnthropicThinking](docs/v2/LanguageModels/models/AnthropicThinking.md) | `from foundry_sdk.v2.language_models.models import AnthropicThinking` |
**LanguageModels** | [AnthropicThinkingConfig](docs/v2/LanguageModels/models/AnthropicThinkingConfig.md) | `from foundry_sdk.v2.language_models.models import AnthropicThinkingConfig` |
**LanguageModels** | [AnthropicTokenUsage](docs/v2/LanguageModels/models/AnthropicTokenUsage.md) | `from foundry_sdk.v2.language_models.models import AnthropicTokenUsage` |
**LanguageModels** | [AnthropicTool](docs/v2/LanguageModels/models/AnthropicTool.md) | `from foundry_sdk.v2.language_models.models import AnthropicTool` |
**LanguageModels** | [AnthropicToolChoice](docs/v2/LanguageModels/models/AnthropicToolChoice.md) | `from foundry_sdk.v2.language_models.models import AnthropicToolChoice` |
**LanguageModels** | [AnthropicToolResult](docs/v2/LanguageModels/models/AnthropicToolResult.md) | `from foundry_sdk.v2.language_models.models import AnthropicToolResult` |
**LanguageModels** | [AnthropicToolResultContent](docs/v2/LanguageModels/models/AnthropicToolResultContent.md) | `from foundry_sdk.v2.language_models.models import AnthropicToolResultContent` |
**LanguageModels** | [AnthropicToolToolChoice](docs/v2/LanguageModels/models/AnthropicToolToolChoice.md) | `from foundry_sdk.v2.language_models.models import AnthropicToolToolChoice` |
**LanguageModels** | [AnthropicToolUse](docs/v2/LanguageModels/models/AnthropicToolUse.md) | `from foundry_sdk.v2.language_models.models import AnthropicToolUse` |
**LanguageModels** | [JsonSchema](docs/v2/LanguageModels/models/JsonSchema.md) | `from foundry_sdk.v2.language_models.models import JsonSchema` |
**LanguageModels** | [LanguageModelApiName](docs/v2/LanguageModels/models/LanguageModelApiName.md) | `from foundry_sdk.v2.language_models.models import LanguageModelApiName` |
**LanguageModels** | [OpenAiEmbeddingInput](docs/v2/LanguageModels/models/OpenAiEmbeddingInput.md) | `from foundry_sdk.v2.language_models.models import OpenAiEmbeddingInput` |
**LanguageModels** | [OpenAiEmbeddingsRequest](docs/v2/LanguageModels/models/OpenAiEmbeddingsRequest.md) | `from foundry_sdk.v2.language_models.models import OpenAiEmbeddingsRequest` |
**LanguageModels** | [OpenAiEmbeddingsResponse](docs/v2/LanguageModels/models/OpenAiEmbeddingsResponse.md) | `from foundry_sdk.v2.language_models.models import OpenAiEmbeddingsResponse` |
**LanguageModels** | [OpenAiEmbeddingTokenUsage](docs/v2/LanguageModels/models/OpenAiEmbeddingTokenUsage.md) | `from foundry_sdk.v2.language_models.models import OpenAiEmbeddingTokenUsage` |
**LanguageModels** | [OpenAiEncodingFormat](docs/v2/LanguageModels/models/OpenAiEncodingFormat.md) | `from foundry_sdk.v2.language_models.models import OpenAiEncodingFormat` |
**MediaSets** | [AffineTransform](docs/v2/MediaSets/models/AffineTransform.md) | `from foundry_sdk.v2.media_sets.models import AffineTransform` |
**MediaSets** | [AnnotateGeometry](docs/v2/MediaSets/models/AnnotateGeometry.md) | `from foundry_sdk.v2.media_sets.models import AnnotateGeometry` |
**MediaSets** | [AnnotateImageOperation](docs/v2/MediaSets/models/AnnotateImageOperation.md) | `from foundry_sdk.v2.media_sets.models import AnnotateImageOperation` |
**MediaSets** | [Annotation](docs/v2/MediaSets/models/Annotation.md) | `from foundry_sdk.v2.media_sets.models import Annotation` |
**MediaSets** | [ApiNameLocatorWrapper](docs/v2/MediaSets/models/ApiNameLocatorWrapper.md) | `from foundry_sdk.v2.media_sets.models import ApiNameLocatorWrapper` |
**MediaSets** | [ArchiveEncodeFormat](docs/v2/MediaSets/models/ArchiveEncodeFormat.md) | `from foundry_sdk.v2.media_sets.models import ArchiveEncodeFormat` |
**MediaSets** | [AudioChannelLayout](docs/v2/MediaSets/models/AudioChannelLayout.md) | `from foundry_sdk.v2.media_sets.models import AudioChannelLayout` |
**MediaSets** | [AudioChannelOperation](docs/v2/MediaSets/models/AudioChannelOperation.md) | `from foundry_sdk.v2.media_sets.models import AudioChannelOperation` |
**MediaSets** | [AudioChunkOperation](docs/v2/MediaSets/models/AudioChunkOperation.md) | `from foundry_sdk.v2.media_sets.models import AudioChunkOperation` |
**MediaSets** | [AudioDecodeFormat](docs/v2/MediaSets/models/AudioDecodeFormat.md) | `from foundry_sdk.v2.media_sets.models import AudioDecodeFormat` |
**MediaSets** | [AudioEncodeFormat](docs/v2/MediaSets/models/AudioEncodeFormat.md) | `from foundry_sdk.v2.media_sets.models import AudioEncodeFormat` |
**MediaSets** | [AudioMediaItemMetadata](docs/v2/MediaSets/models/AudioMediaItemMetadata.md) | `from foundry_sdk.v2.media_sets.models import AudioMediaItemMetadata` |
**MediaSets** | [AudioOperation](docs/v2/MediaSets/models/AudioOperation.md) | `from foundry_sdk.v2.media_sets.models import AudioOperation` |
**MediaSets** | [AudioSpecification](docs/v2/MediaSets/models/AudioSpecification.md) | `from foundry_sdk.v2.media_sets.models import AudioSpecification` |
**MediaSets** | [AudioToTextOperation](docs/v2/MediaSets/models/AudioToTextOperation.md) | `from foundry_sdk.v2.media_sets.models import AudioToTextOperation` |
**MediaSets** | [AudioToTextTransformation](docs/v2/MediaSets/models/AudioToTextTransformation.md) | `from foundry_sdk.v2.media_sets.models import AudioToTextTransformation` |
**MediaSets** | [AudioTransformation](docs/v2/MediaSets/models/AudioTransformation.md) | `from foundry_sdk.v2.media_sets.models import AudioTransformation` |
**MediaSets** | [AvailableEmbeddingModelIds](docs/v2/MediaSets/models/AvailableEmbeddingModelIds.md) | `from foundry_sdk.v2.media_sets.models import AvailableEmbeddingModelIds` |
**MediaSets** | [BandInfo](docs/v2/MediaSets/models/BandInfo.md) | `from foundry_sdk.v2.media_sets.models import BandInfo` |
**MediaSets** | [BatchTransactionsTransactionPolicy](docs/v2/MediaSets/models/BatchTransactionsTransactionPolicy.md) | `from foundry_sdk.v2.media_sets.models import BatchTransactionsTransactionPolicy` |
**MediaSets** | [BoundingBox](docs/v2/MediaSets/models/BoundingBox.md) | `from foundry_sdk.v2.media_sets.models import BoundingBox` |
**MediaSets** | [BoundingBoxGeometry](docs/v2/MediaSets/models/BoundingBoxGeometry.md) | `from foundry_sdk.v2.media_sets.models import BoundingBoxGeometry` |
**MediaSets** | [BranchName](docs/v2/MediaSets/models/BranchName.md) | `from foundry_sdk.v2.media_sets.models import BranchName` |
**MediaSets** | [BranchRid](docs/v2/MediaSets/models/BranchRid.md) | `from foundry_sdk.v2.media_sets.models import BranchRid` |
**MediaSets** | [ChatLlmSpec](docs/v2/MediaSets/models/ChatLlmSpec.md) | `from foundry_sdk.v2.media_sets.models import ChatLlmSpec` |
**MediaSets** | [ChatLlmSpecWrapper](docs/v2/MediaSets/models/ChatLlmSpecWrapper.md) | `from foundry_sdk.v2.media_sets.models import ChatLlmSpecWrapper` |
**MediaSets** | [Color](docs/v2/MediaSets/models/Color.md) | `from foundry_sdk.v2.media_sets.models import Color` |
**MediaSets** | [ColorInterpretation](docs/v2/MediaSets/models/ColorInterpretation.md) | `from foundry_sdk.v2.media_sets.models import ColorInterpretation` |
**MediaSets** | [CommonDicomDataElements](docs/v2/MediaSets/models/CommonDicomDataElements.md) | `from foundry_sdk.v2.media_sets.models import CommonDicomDataElements` |
**MediaSets** | [ContrastBinarize](docs/v2/MediaSets/models/ContrastBinarize.md) | `from foundry_sdk.v2.media_sets.models import ContrastBinarize` |
**MediaSets** | [ContrastEqualize](docs/v2/MediaSets/models/ContrastEqualize.md) | `from foundry_sdk.v2.media_sets.models import ContrastEqualize` |
**MediaSets** | [ContrastImageOperation](docs/v2/MediaSets/models/ContrastImageOperation.md) | `from foundry_sdk.v2.media_sets.models import ContrastImageOperation` |
**MediaSets** | [ContrastRayleigh](docs/v2/MediaSets/models/ContrastRayleigh.md) | `from foundry_sdk.v2.media_sets.models import ContrastRayleigh` |
**MediaSets** | [ContrastType](docs/v2/MediaSets/models/ContrastType.md) | `from foundry_sdk.v2.media_sets.models import ContrastType` |
**MediaSets** | [ConvertAudioOperation](docs/v2/MediaSets/models/ConvertAudioOperation.md) | `from foundry_sdk.v2.media_sets.models import ConvertAudioOperation` |
**MediaSets** | [ConvertDocumentOperation](docs/v2/MediaSets/models/ConvertDocumentOperation.md) | `from foundry_sdk.v2.media_sets.models import ConvertDocumentOperation` |
**MediaSets** | [ConvertSheetToJsonOperation](docs/v2/MediaSets/models/ConvertSheetToJsonOperation.md) | `from foundry_sdk.v2.media_sets.models import ConvertSheetToJsonOperation` |
**MediaSets** | [CoordinateReferenceSystem](docs/v2/MediaSets/models/CoordinateReferenceSystem.md) | `from foundry_sdk.v2.media_sets.models import CoordinateReferenceSystem` |
**MediaSets** | [CreatePdfOperation](docs/v2/MediaSets/models/CreatePdfOperation.md) | `from foundry_sdk.v2.media_sets.models import CreatePdfOperation` |
**MediaSets** | [CropConfig](docs/v2/MediaSets/models/CropConfig.md) | `from foundry_sdk.v2.media_sets.models import CropConfig` |
**MediaSets** | [CropImageOperation](docs/v2/MediaSets/models/CropImageOperation.md) | `from foundry_sdk.v2.media_sets.models import CropImageOperation` |
**MediaSets** | [DataType](docs/v2/MediaSets/models/DataType.md) | `from foundry_sdk.v2.media_sets.models import DataType` |
**MediaSets** | [DecryptImageOperation](docs/v2/MediaSets/models/DecryptImageOperation.md) | `from foundry_sdk.v2.media_sets.models import DecryptImageOperation` |
**MediaSets** | [DicomDataElementKey](docs/v2/MediaSets/models/DicomDataElementKey.md) | `from foundry_sdk.v2.media_sets.models import DicomDataElementKey` |
**MediaSets** | [DicomMediaItemMetadata](docs/v2/MediaSets/models/DicomMediaItemMetadata.md) | `from foundry_sdk.v2.media_sets.models import DicomMediaItemMetadata` |
**MediaSets** | [DicomMediaType](docs/v2/MediaSets/models/DicomMediaType.md) | `from foundry_sdk.v2.media_sets.models import DicomMediaType` |
**MediaSets** | [DicomMetaInformation](docs/v2/MediaSets/models/DicomMetaInformation.md) | `from foundry_sdk.v2.media_sets.models import DicomMetaInformation` |
**MediaSets** | [DicomMetaInformationV1](docs/v2/MediaSets/models/DicomMetaInformationV1.md) | `from foundry_sdk.v2.media_sets.models import DicomMetaInformationV1` |
**MediaSets** | [DicomToImageOperation](docs/v2/MediaSets/models/DicomToImageOperation.md) | `from foundry_sdk.v2.media_sets.models import DicomToImageOperation` |
**MediaSets** | [DicomToImageTransformation](docs/v2/MediaSets/models/DicomToImageTransformation.md) | `from foundry_sdk.v2.media_sets.models import DicomToImageTransformation` |
**MediaSets** | [Dimensions](docs/v2/MediaSets/models/Dimensions.md) | `from foundry_sdk.v2.media_sets.models import Dimensions` |
**MediaSets** | [DocumentDecodeFormat](docs/v2/MediaSets/models/DocumentDecodeFormat.md) | `from foundry_sdk.v2.media_sets.models import DocumentDecodeFormat` |
**MediaSets** | [DocumentEncodeFormat](docs/v2/MediaSets/models/DocumentEncodeFormat.md) | `from foundry_sdk.v2.media_sets.models import DocumentEncodeFormat` |
**MediaSets** | [DocumentExtractLayoutAwareContentOperation](docs/v2/MediaSets/models/DocumentExtractLayoutAwareContentOperation.md) | `from foundry_sdk.v2.media_sets.models import DocumentExtractLayoutAwareContentOperation` |
**MediaSets** | [DocumentMediaItemMetadata](docs/v2/MediaSets/models/DocumentMediaItemMetadata.md) | `from foundry_sdk.v2.media_sets.models import DocumentMediaItemMetadata` |
**MediaSets** | [DocumentToDocumentOperation](docs/v2/MediaSets/models/DocumentToDocumentOperation.md) | `from foundry_sdk.v2.media_sets.models import DocumentToDocumentOperation` |
**MediaSets** | [DocumentToDocumentTransformation](docs/v2/MediaSets/models/DocumentToDocumentTransformation.md) | `from foundry_sdk.v2.media_sets.models import DocumentToDocumentTransformation` |
**MediaSets** | [DocumentToImageOperation](docs/v2/MediaSets/models/DocumentToImageOperation.md) | `from foundry_sdk.v2.media_sets.models import DocumentToImageOperation` |
**MediaSets** | [DocumentToImageTransformation](docs/v2/MediaSets/models/DocumentToImageTransformation.md) | `from foundry_sdk.v2.media_sets.models import DocumentToImageTransformation` |
**MediaSets** | [DocumentToTextOperation](docs/v2/MediaSets/models/DocumentToTextOperation.md) | `from foundry_sdk.v2.media_sets.models import DocumentToTextOperation` |
**MediaSets** | [DocumentToTextTransformation](docs/v2/MediaSets/models/DocumentToTextTransformation.md) | `from foundry_sdk.v2.media_sets.models import DocumentToTextTransformation` |
**MediaSets** | [EmailAttachment](docs/v2/MediaSets/models/EmailAttachment.md) | `from foundry_sdk.v2.media_sets.models import EmailAttachment` |
**MediaSets** | [EmailDecodeFormat](docs/v2/MediaSets/models/EmailDecodeFormat.md) | `from foundry_sdk.v2.media_sets.models import EmailDecodeFormat` |
**MediaSets** | [EmailMediaItemMetadata](docs/v2/MediaSets/models/EmailMediaItemMetadata.md) | `from foundry_sdk.v2.media_sets.models import EmailMediaItemMetadata` |
**MediaSets** | [EmailToAttachmentOperation](docs/v2/MediaSets/models/EmailToAttachmentOperation.md) | `from foundry_sdk.v2.media_sets.models import EmailToAttachmentOperation` |
**MediaSets** | [EmailToAttachmentTransformation](docs/v2/MediaSets/models/EmailToAttachmentTransformation.md) | `from foundry_sdk.v2.media_sets.models import EmailToAttachmentTransformation` |
**MediaSets** | [EmailToTextEncodeFormat](docs/v2/MediaSets/models/EmailToTextEncodeFormat.md) | `from foundry_sdk.v2.media_sets.models import EmailToTextEncodeFormat` |
**MediaSets** | [EmailToTextOperation](docs/v2/MediaSets/models/EmailToTextOperation.md) | `from foundry_sdk.v2.media_sets.models import EmailToTextOperation` |
**MediaSets** | [EmailToTextTransformation](docs/v2/MediaSets/models/EmailToTextTransformation.md) | `from foundry_sdk.v2.media_sets.models import EmailToTextTransformation` |
**MediaSets** | [EncryptImageOperation](docs/v2/MediaSets/models/EncryptImageOperation.md) | `from foundry_sdk.v2.media_sets.models import EncryptImageOperation` |
**MediaSets** | [ExtractAllTextOperation](docs/v2/MediaSets/models/ExtractAllTextOperation.md) | `from foundry_sdk.v2.media_sets.models import ExtractAllTextOperation` |
**MediaSets** | [ExtractAudioOperation](docs/v2/MediaSets/models/ExtractAudioOperation.md) | `from foundry_sdk.v2.media_sets.models import ExtractAudioOperation` |
**MediaSets** | [ExtractDocumentLayoutAwareTextV2Config](docs/v2/MediaSets/models/ExtractDocumentLayoutAwareTextV2Config.md) | `from foundry_sdk.v2.media_sets.models import ExtractDocumentLayoutAwareTextV2Config` |
**MediaSets** | [ExtractDocumentLayoutAwareTextV2Operation](docs/v2/MediaSets/models/ExtractDocumentLayoutAwareTextV2Operation.md) | `from foundry_sdk.v2.media_sets.models import ExtractDocumentLayoutAwareTextV2Operation` |
**MediaSets** | [ExtractDocumentTextV2Config](docs/v2/MediaSets/models/ExtractDocumentTextV2Config.md) | `from foundry_sdk.v2.media_sets.models import ExtractDocumentTextV2Config` |
**MediaSets** | [ExtractDocumentTextV2Operation](docs/v2/MediaSets/models/ExtractDocumentTextV2Operation.md) | `from foundry_sdk.v2.media_sets.models import ExtractDocumentTextV2Operation` |
**MediaSets** | [ExtractFirstFrameOperation](docs/v2/MediaSets/models/ExtractFirstFrameOperation.md) | `from foundry_sdk.v2.media_sets.models import ExtractFirstFrameOperation` |
**MediaSets** | [ExtractFormFieldsOperation](docs/v2/MediaSets/models/ExtractFormFieldsOperation.md) | `from foundry_sdk.v2.media_sets.models import ExtractFormFieldsOperation` |
**MediaSets** | [ExtractFramesAtTimestampsOperation](docs/v2/MediaSets/models/ExtractFramesAtTimestampsOperation.md) | `from foundry_sdk.v2.media_sets.models import ExtractFramesAtTimestampsOperation` |
**MediaSets** | [ExtractSceneFramesOperation](docs/v2/MediaSets/models/ExtractSceneFramesOperation.md) | `from foundry_sdk.v2.media_sets.models import ExtractSceneFramesOperation` |
**MediaSets** | [ExtractTableOfContentsOperation](docs/v2/MediaSets/models/ExtractTableOfContentsOperation.md) | `from foundry_sdk.v2.media_sets.models import ExtractTableOfContentsOperation` |
**MediaSets** | [ExtractTextFromPagesToArrayOperation](docs/v2/MediaSets/models/ExtractTextFromPagesToArrayOperation.md) | `from foundry_sdk.v2.media_sets.models import ExtractTextFromPagesToArrayOperation` |
**MediaSets** | [ExtractTextPreprocessingWrapper](docs/v2/MediaSets/models/ExtractTextPreprocessingWrapper.md) | `from foundry_sdk.v2.media_sets.models import ExtractTextPreprocessingWrapper` |
**MediaSets** | [ExtractUnstructuredTextFromPageOperation](docs/v2/MediaSets/models/ExtractUnstructuredTextFromPageOperation.md) | `from foundry_sdk.v2.media_sets.models import ExtractUnstructuredTextFromPageOperation` |
**MediaSets** | [ExtractVlmTextOperation](docs/v2/MediaSets/models/ExtractVlmTextOperation.md) | `from foundry_sdk.v2.media_sets.models import ExtractVlmTextOperation` |
**MediaSets** | [FlipAxis](docs/v2/MediaSets/models/FlipAxis.md) | `from foundry_sdk.v2.media_sets.models import FlipAxis` |
**MediaSets** | [GcpList](docs/v2/MediaSets/models/GcpList.md) | `from foundry_sdk.v2.media_sets.models import GcpList` |
**MediaSets** | [GenerateEmbeddingOperation](docs/v2/MediaSets/models/GenerateEmbeddingOperation.md) | `from foundry_sdk.v2.media_sets.models import GenerateEmbeddingOperation` |
**MediaSets** | [GeoMetadata](docs/v2/MediaSets/models/GeoMetadata.md) | `from foundry_sdk.v2.media_sets.models import GeoMetadata` |
**MediaSets** | [GetEmailAttachmentOperation](docs/v2/MediaSets/models/GetEmailAttachmentOperation.md) | `from foundry_sdk.v2.media_sets.models import GetEmailAttachmentOperation` |
**MediaSets** | [GetEmailBodyOperation](docs/v2/MediaSets/models/GetEmailBodyOperation.md) | `from foundry_sdk.v2.media_sets.models import GetEmailBodyOperation` |
**MediaSets** | [GetMediaItemInfoResponse](docs/v2/MediaSets/models/GetMediaItemInfoResponse.md) | `from foundry_sdk.v2.media_sets.models import GetMediaItemInfoResponse` |
**MediaSets** | [GetMediaItemRidByPathResponse](docs/v2/MediaSets/models/GetMediaItemRidByPathResponse.md) | `from foundry_sdk.v2.media_sets.models import GetMediaItemRidByPathResponse` |
**MediaSets** | [GetMediaSetResponse](docs/v2/MediaSets/models/GetMediaSetResponse.md) | `from foundry_sdk.v2.media_sets.models import GetMediaSetResponse` |
**MediaSets** | [GetPdfPageDimensionsOperation](docs/v2/MediaSets/models/GetPdfPageDimensionsOperation.md) | `from foundry_sdk.v2.media_sets.models import GetPdfPageDimensionsOperation` |
**MediaSets** | [GetTimestampsForSceneFramesOperation](docs/v2/MediaSets/models/GetTimestampsForSceneFramesOperation.md) | `from foundry_sdk.v2.media_sets.models import GetTimestampsForSceneFramesOperation` |
**MediaSets** | [GetTransformationJobStatusResponse](docs/v2/MediaSets/models/GetTransformationJobStatusResponse.md) | `from foundry_sdk.v2.media_sets.models import GetTransformationJobStatusResponse` |
**MediaSets** | [GpsMetadata](docs/v2/MediaSets/models/GpsMetadata.md) | `from foundry_sdk.v2.media_sets.models import GpsMetadata` |
**MediaSets** | [GrayscaleImageOperation](docs/v2/MediaSets/models/GrayscaleImageOperation.md) | `from foundry_sdk.v2.media_sets.models import GrayscaleImageOperation` |
**MediaSets** | [GroundControlPoint](docs/v2/MediaSets/models/GroundControlPoint.md) | `from foundry_sdk.v2.media_sets.models import GroundControlPoint` |
**MediaSets** | [Group](docs/v2/MediaSets/models/Group.md) | `from foundry_sdk.v2.media_sets.models import Group` |
**MediaSets** | [GroupWrapper](docs/v2/MediaSets/models/GroupWrapper.md) | `from foundry_sdk.v2.media_sets.models import GroupWrapper` |
**MediaSets** | [ImageAttributeDomain](docs/v2/MediaSets/models/ImageAttributeDomain.md) | `from foundry_sdk.v2.media_sets.models import ImageAttributeDomain` |
**MediaSets** | [ImageAttributeKey](docs/v2/MediaSets/models/ImageAttributeKey.md) | `from foundry_sdk.v2.media_sets.models import ImageAttributeKey` |
**MediaSets** | [ImageExtractLayoutAwareContentOperation](docs/v2/MediaSets/models/ImageExtractLayoutAwareContentOperation.md) | `from foundry_sdk.v2.media_sets.models import ImageExtractLayoutAwareContentOperation` |
**MediaSets** | [ImageOcrOperation](docs/v2/MediaSets/models/ImageOcrOperation.md) | `from foundry_sdk.v2.media_sets.models import ImageOcrOperation` |
**MediaSets** | [ImageOperation](docs/v2/MediaSets/models/ImageOperation.md) | `from foundry_sdk.v2.media_sets.models import ImageOperation` |
**MediaSets** | [ImagePixelCoordinate](docs/v2/MediaSets/models/ImagePixelCoordinate.md) | `from foundry_sdk.v2.media_sets.models import ImagePixelCoordinate` |
**MediaSets** | [ImageRegionPolygon](docs/v2/MediaSets/models/ImageRegionPolygon.md) | `from foundry_sdk.v2.media_sets.models import ImageRegionPolygon` |
**MediaSets** | [ImageryDecodeFormat](docs/v2/MediaSets/models/ImageryDecodeFormat.md) | `from foundry_sdk.v2.media_sets.models import ImageryDecodeFormat` |
**MediaSets** | [ImageryEncodeFormat](docs/v2/MediaSets/models/ImageryEncodeFormat.md) | `from foundry_sdk.v2.media_sets.models import ImageryEncodeFormat` |
**MediaSets** | [ImageryMediaItemMetadata](docs/v2/MediaSets/models/ImageryMediaItemMetadata.md) | `from foundry_sdk.v2.media_sets.models import ImageryMediaItemMetadata` |
**MediaSets** | [ImageSpec](docs/v2/MediaSets/models/ImageSpec.md) | `from foundry_sdk.v2.media_sets.models import ImageSpec` |
**MediaSets** | [ImageToDocumentOperation](docs/v2/MediaSets/models/ImageToDocumentOperation.md) | `from foundry_sdk.v2.media_sets.models import ImageToDocumentOperation` |
**MediaSets** | [ImageToDocumentTransformation](docs/v2/MediaSets/models/ImageToDocumentTransformation.md) | `from foundry_sdk.v2.media_sets.models import ImageToDocumentTransformation` |
**MediaSets** | [ImageToEmbeddingOperation](docs/v2/MediaSets/models/ImageToEmbeddingOperation.md) | `from foundry_sdk.v2.media_sets.models import ImageToEmbeddingOperation` |
**MediaSets** | [ImageToEmbeddingTransformation](docs/v2/MediaSets/models/ImageToEmbeddingTransformation.md) | `from foundry_sdk.v2.media_sets.models import ImageToEmbeddingTransformation` |
**MediaSets** | [ImageToTextOperation](docs/v2/MediaSets/models/ImageToTextOperation.md) | `from foundry_sdk.v2.media_sets.models import ImageToTextOperation` |
**MediaSets** | [ImageToTextTransformation](docs/v2/MediaSets/models/ImageToTextTransformation.md) | `from foundry_sdk.v2.media_sets.models import ImageToTextTransformation` |
**MediaSets** | [ImageTransformation](docs/v2/MediaSets/models/ImageTransformation.md) | `from foundry_sdk.v2.media_sets.models import ImageTransformation` |
**MediaSets** | [JpgFormat](docs/v2/MediaSets/models/JpgFormat.md) | `from foundry_sdk.v2.media_sets.models import JpgFormat` |
**MediaSets** | [LanguageModelLocator](docs/v2/MediaSets/models/LanguageModelLocator.md) | `from foundry_sdk.v2.media_sets.models import LanguageModelLocator` |
**MediaSets** | [LayoutAwareExtractionParameters](docs/v2/MediaSets/models/LayoutAwareExtractionParameters.md) | `from foundry_sdk.v2.media_sets.models import LayoutAwareExtractionParameters` |
**MediaSets** | [LayoutAwareExtractionPreprocessingConfig](docs/v2/MediaSets/models/LayoutAwareExtractionPreprocessingConfig.md) | `from foundry_sdk.v2.media_sets.models import LayoutAwareExtractionPreprocessingConfig` |
**MediaSets** | [LayoutAwarePreprocessingWrapper](docs/v2/MediaSets/models/LayoutAwarePreprocessingWrapper.md) | `from foundry_sdk.v2.media_sets.models import LayoutAwarePreprocessingWrapper` |
**MediaSets** | [LlmSpec](docs/v2/MediaSets/models/LlmSpec.md) | `from foundry_sdk.v2.media_sets.models import LlmSpec` |
**MediaSets** | [LogicalTimestamp](docs/v2/MediaSets/models/LogicalTimestamp.md) | `from foundry_sdk.v2.media_sets.models import LogicalTimestamp` |
**MediaSets** | [Mailbox](docs/v2/MediaSets/models/Mailbox.md) | `from foundry_sdk.v2.media_sets.models import Mailbox` |
**MediaSets** | [MailboxOrGroup](docs/v2/MediaSets/models/MailboxOrGroup.md) | `from foundry_sdk.v2.media_sets.models import MailboxOrGroup` |
**MediaSets** | [MailboxWrapper](docs/v2/MediaSets/models/MailboxWrapper.md) | `from foundry_sdk.v2.media_sets.models import MailboxWrapper` |
**MediaSets** | [MediaAttribution](docs/v2/MediaSets/models/MediaAttribution.md) | `from foundry_sdk.v2.media_sets.models import MediaAttribution` |
**MediaSets** | [MediaItemMetadata](docs/v2/MediaSets/models/MediaItemMetadata.md) | `from foundry_sdk.v2.media_sets.models import MediaItemMetadata` |
**MediaSets** | [MediaItemXmlFormat](docs/v2/MediaSets/models/MediaItemXmlFormat.md) | `from foundry_sdk.v2.media_sets.models import MediaItemXmlFormat` |
**MediaSets** | [MediaSchema](docs/v2/MediaSets/models/MediaSchema.md) | `from foundry_sdk.v2.media_sets.models import MediaSchema` |
**MediaSets** | [MkvVideoContainerFormat](docs/v2/MediaSets/models/MkvVideoContainerFormat.md) | `from foundry_sdk.v2.media_sets.models import MkvVideoContainerFormat` |
**MediaSets** | [Modality](docs/v2/MediaSets/models/Modality.md) | `from foundry_sdk.v2.media_sets.models import Modality` |
**MediaSets** | [Model3dDecodeFormat](docs/v2/MediaSets/models/Model3dDecodeFormat.md) | `from foundry_sdk.v2.media_sets.models import Model3dDecodeFormat` |
**MediaSets** | [Model3dMediaItemMetadata](docs/v2/MediaSets/models/Model3dMediaItemMetadata.md) | `from foundry_sdk.v2.media_sets.models import Model3dMediaItemMetadata` |
**MediaSets** | [Model3dType](docs/v2/MediaSets/models/Model3dType.md) | `from foundry_sdk.v2.media_sets.models import Model3dType` |
**MediaSets** | [MovVideoContainerFormat](docs/v2/MediaSets/models/MovVideoContainerFormat.md) | `from foundry_sdk.v2.media_sets.models import MovVideoContainerFormat` |
**MediaSets** | [Mp3Format](docs/v2/MediaSets/models/Mp3Format.md) | `from foundry_sdk.v2.media_sets.models import Mp3Format` |
**MediaSets** | [Mp4VideoContainerFormat](docs/v2/MediaSets/models/Mp4VideoContainerFormat.md) | `from foundry_sdk.v2.media_sets.models import Mp4VideoContainerFormat` |
**MediaSets** | [NoTransactionsTransactionPolicy](docs/v2/MediaSets/models/NoTransactionsTransactionPolicy.md) | `from foundry_sdk.v2.media_sets.models import NoTransactionsTransactionPolicy` |
**MediaSets** | [NumberOfChannels](docs/v2/MediaSets/models/NumberOfChannels.md) | `from foundry_sdk.v2.media_sets.models import NumberOfChannels` |
**MediaSets** | [OcrHocrOutputFormat](docs/v2/MediaSets/models/OcrHocrOutputFormat.md) | `from foundry_sdk.v2.media_sets.models import OcrHocrOutputFormat` |
**MediaSets** | [OcrLanguage](docs/v2/MediaSets/models/OcrLanguage.md) | `from foundry_sdk.v2.media_sets.models import OcrLanguage` |
**MediaSets** | [OcrLanguageOrScript](docs/v2/MediaSets/models/OcrLanguageOrScript.md) | `from foundry_sdk.v2.media_sets.models import OcrLanguageOrScript` |
**MediaSets** | [OcrLanguageWrapper](docs/v2/MediaSets/models/OcrLanguageWrapper.md) | `from foundry_sdk.v2.media_sets.models import OcrLanguageWrapper` |
**MediaSets** | [OcrMode](docs/v2/MediaSets/models/OcrMode.md) | `from foundry_sdk.v2.media_sets.models import OcrMode` |
**MediaSets** | [OcrOnPageOperation](docs/v2/MediaSets/models/OcrOnPageOperation.md) | `from foundry_sdk.v2.media_sets.models import OcrOnPageOperation` |
**MediaSets** | [OcrOnPagesOperation](docs/v2/MediaSets/models/OcrOnPagesOperation.md) | `from foundry_sdk.v2.media_sets.models import OcrOnPagesOperation` |
**MediaSets** | [OcrOutputFormat](docs/v2/MediaSets/models/OcrOutputFormat.md) | `from foundry_sdk.v2.media_sets.models import OcrOutputFormat` |
**MediaSets** | [OcrParameters](docs/v2/MediaSets/models/OcrParameters.md) | `from foundry_sdk.v2.media_sets.models import OcrParameters` |
**MediaSets** | [OcrScript](docs/v2/MediaSets/models/OcrScript.md) | `from foundry_sdk.v2.media_sets.models import OcrScript` |
**MediaSets** | [OcrScriptWrapper](docs/v2/MediaSets/models/OcrScriptWrapper.md) | `from foundry_sdk.v2.media_sets.models import OcrScriptWrapper` |
**MediaSets** | [OcrTextOutputFormat](docs/v2/MediaSets/models/OcrTextOutputFormat.md) | `from foundry_sdk.v2.media_sets.models import OcrTextOutputFormat` |
**MediaSets** | [Orientation](docs/v2/MediaSets/models/Orientation.md) | `from foundry_sdk.v2.media_sets.models import Orientation` |
**MediaSets** | [PageRange](docs/v2/MediaSets/models/PageRange.md) | `from foundry_sdk.v2.media_sets.models import PageRange` |
**MediaSets** | [PaletteInterpretation](docs/v2/MediaSets/models/PaletteInterpretation.md) | `from foundry_sdk.v2.media_sets.models import PaletteInterpretation` |
**MediaSets** | [PdfFormat](docs/v2/MediaSets/models/PdfFormat.md) | `from foundry_sdk.v2.media_sets.models import PdfFormat` |
**MediaSets** | [PerformanceMode](docs/v2/MediaSets/models/PerformanceMode.md) | `from foundry_sdk.v2.media_sets.models import PerformanceMode` |
**MediaSets** | [PlainTextNoSegmentData](docs/v2/MediaSets/models/PlainTextNoSegmentData.md) | `from foundry_sdk.v2.media_sets.models import PlainTextNoSegmentData` |
**MediaSets** | [PngFormat](docs/v2/MediaSets/models/PngFormat.md) | `from foundry_sdk.v2.media_sets.models import PngFormat` |
**MediaSets** | [Pttml](docs/v2/MediaSets/models/Pttml.md) | `from foundry_sdk.v2.media_sets.models import Pttml` |
**MediaSets** | [PutMediaItemResponse](docs/v2/MediaSets/models/PutMediaItemResponse.md) | `from foundry_sdk.v2.media_sets.models import PutMediaItemResponse` |
**MediaSets** | [RegisterMediaItemRequest](docs/v2/MediaSets/models/RegisterMediaItemRequest.md) | `from foundry_sdk.v2.media_sets.models import RegisterMediaItemRequest` |
**MediaSets** | [RegisterMediaItemResponse](docs/v2/MediaSets/models/RegisterMediaItemResponse.md) | `from foundry_sdk.v2.media_sets.models import RegisterMediaItemResponse` |
**MediaSets** | [RenderImageLayerOperation](docs/v2/MediaSets/models/RenderImageLayerOperation.md) | `from foundry_sdk.v2.media_sets.models import RenderImageLayerOperation` |
**MediaSets** | [RenderPageOperation](docs/v2/MediaSets/models/RenderPageOperation.md) | `from foundry_sdk.v2.media_sets.models import RenderPageOperation` |
**MediaSets** | [RenderPageToFitBoundingBoxOperation](docs/v2/MediaSets/models/RenderPageToFitBoundingBoxOperation.md) | `from foundry_sdk.v2.media_sets.models import RenderPageToFitBoundingBoxOperation` |
**MediaSets** | [ResizeImageOperation](docs/v2/MediaSets/models/ResizeImageOperation.md) | `from foundry_sdk.v2.media_sets.models import ResizeImageOperation` |
**MediaSets** | [ResizeToFitBoundingBoxOperation](docs/v2/MediaSets/models/ResizeToFitBoundingBoxOperation.md) | `from foundry_sdk.v2.media_sets.models import ResizeToFitBoundingBoxOperation` |
**MediaSets** | [ResizingMode](docs/v2/MediaSets/models/ResizingMode.md) | `from foundry_sdk.v2.media_sets.models import ResizingMode` |
**MediaSets** | [RotateImageOperation](docs/v2/MediaSets/models/RotateImageOperation.md) | `from foundry_sdk.v2.media_sets.models import RotateImageOperation` |
**MediaSets** | [RotationAngle](docs/v2/MediaSets/models/RotationAngle.md) | `from foundry_sdk.v2.media_sets.models import RotationAngle` |
**MediaSets** | [SceneScore](docs/v2/MediaSets/models/SceneScore.md) | `from foundry_sdk.v2.media_sets.models import SceneScore` |
**MediaSets** | [SlicePdfRangeOperation](docs/v2/MediaSets/models/SlicePdfRangeOperation.md) | `from foundry_sdk.v2.media_sets.models import SlicePdfRangeOperation` |
**MediaSets** | [SpreadsheetDecodeFormat](docs/v2/MediaSets/models/SpreadsheetDecodeFormat.md) | `from foundry_sdk.v2.media_sets.models import SpreadsheetDecodeFormat` |
**MediaSets** | [SpreadsheetMediaItemMetadata](docs/v2/MediaSets/models/SpreadsheetMediaItemMetadata.md) | `from foundry_sdk.v2.media_sets.models import SpreadsheetMediaItemMetadata` |
**MediaSets** | [SpreadsheetToTextOperation](docs/v2/MediaSets/models/SpreadsheetToTextOperation.md) | `from foundry_sdk.v2.media_sets.models import SpreadsheetToTextOperation` |
**MediaSets** | [SpreadsheetToTextTransformation](docs/v2/MediaSets/models/SpreadsheetToTextTransformation.md) | `from foundry_sdk.v2.media_sets.models import SpreadsheetToTextTransformation` |
**MediaSets** | [TarFormat](docs/v2/MediaSets/models/TarFormat.md) | `from foundry_sdk.v2.media_sets.models import TarFormat` |
**MediaSets** | [TextOutputFormat](docs/v2/MediaSets/models/TextOutputFormat.md) | `from foundry_sdk.v2.media_sets.models import TextOutputFormat` |
**MediaSets** | [TiffFormat](docs/v2/MediaSets/models/TiffFormat.md) | `from foundry_sdk.v2.media_sets.models import TiffFormat` |
**MediaSets** | [TileImageOperation](docs/v2/MediaSets/models/TileImageOperation.md) | `from foundry_sdk.v2.media_sets.models import TileImageOperation` |
**MediaSets** | [TrackedTransformationFailedResponse](docs/v2/MediaSets/models/TrackedTransformationFailedResponse.md) | `from foundry_sdk.v2.media_sets.models import TrackedTransformationFailedResponse` |
**MediaSets** | [TrackedTransformationPendingResponse](docs/v2/MediaSets/models/TrackedTransformationPendingResponse.md) | `from foundry_sdk.v2.media_sets.models import TrackedTransformationPendingResponse` |
**MediaSets** | [TrackedTransformationResponse](docs/v2/MediaSets/models/TrackedTransformationResponse.md) | `from foundry_sdk.v2.media_sets.models import TrackedTransformationResponse` |
**MediaSets** | [TrackedTransformationSuccessfulResponse](docs/v2/MediaSets/models/TrackedTransformationSuccessfulResponse.md) | `from foundry_sdk.v2.media_sets.models import TrackedTransformationSuccessfulResponse` |
**MediaSets** | [TransactionId](docs/v2/MediaSets/models/TransactionId.md) | `from foundry_sdk.v2.media_sets.models import TransactionId` |
**MediaSets** | [TransactionPolicy](docs/v2/MediaSets/models/TransactionPolicy.md) | `from foundry_sdk.v2.media_sets.models import TransactionPolicy` |
**MediaSets** | [TranscodeOperation](docs/v2/MediaSets/models/TranscodeOperation.md) | `from foundry_sdk.v2.media_sets.models import TranscodeOperation` |
**MediaSets** | [TranscribeJson](docs/v2/MediaSets/models/TranscribeJson.md) | `from foundry_sdk.v2.media_sets.models import TranscribeJson` |
**MediaSets** | [TranscribeOperation](docs/v2/MediaSets/models/TranscribeOperation.md) | `from foundry_sdk.v2.media_sets.models import TranscribeOperation` |
**MediaSets** | [TranscribeTextEncodeFormat](docs/v2/MediaSets/models/TranscribeTextEncodeFormat.md) | `from foundry_sdk.v2.media_sets.models import TranscribeTextEncodeFormat` |
**MediaSets** | [TranscriptionLanguage](docs/v2/MediaSets/models/TranscriptionLanguage.md) | `from foundry_sdk.v2.media_sets.models import TranscriptionLanguage` |
**MediaSets** | [Transformation](docs/v2/MediaSets/models/Transformation.md) | `from foundry_sdk.v2.media_sets.models import Transformation` |
**MediaSets** | [TransformationJobId](docs/v2/MediaSets/models/TransformationJobId.md) | `from foundry_sdk.v2.media_sets.models import TransformationJobId` |
**MediaSets** | [TransformationJobStatus](docs/v2/MediaSets/models/TransformationJobStatus.md) | `from foundry_sdk.v2.media_sets.models import TransformationJobStatus` |
**MediaSets** | [TransformMediaItemRequest](docs/v2/MediaSets/models/TransformMediaItemRequest.md) | `from foundry_sdk.v2.media_sets.models import TransformMediaItemRequest` |
**MediaSets** | [TransformMediaItemResponse](docs/v2/MediaSets/models/TransformMediaItemResponse.md) | `from foundry_sdk.v2.media_sets.models import TransformMediaItemResponse` |
**MediaSets** | [TsAudioContainerFormat](docs/v2/MediaSets/models/TsAudioContainerFormat.md) | `from foundry_sdk.v2.media_sets.models import TsAudioContainerFormat` |
**MediaSets** | [TsVideoContainerFormat](docs/v2/MediaSets/models/TsVideoContainerFormat.md) | `from foundry_sdk.v2.media_sets.models import TsVideoContainerFormat` |
**MediaSets** | [UnitInterpretation](docs/v2/MediaSets/models/UnitInterpretation.md) | `from foundry_sdk.v2.media_sets.models import UnitInterpretation` |
**MediaSets** | [UntypedMediaItemMetadata](docs/v2/MediaSets/models/UntypedMediaItemMetadata.md) | `from foundry_sdk.v2.media_sets.models import UntypedMediaItemMetadata` |
**MediaSets** | [VideoChunkOperation](docs/v2/MediaSets/models/VideoChunkOperation.md) | `from foundry_sdk.v2.media_sets.models import VideoChunkOperation` |
**MediaSets** | [VideoDecodeFormat](docs/v2/MediaSets/models/VideoDecodeFormat.md) | `from foundry_sdk.v2.media_sets.models import VideoDecodeFormat` |
**MediaSets** | [VideoEncodeFormat](docs/v2/MediaSets/models/VideoEncodeFormat.md) | `from foundry_sdk.v2.media_sets.models import VideoEncodeFormat` |
**MediaSets** | [VideoMediaItemMetadata](docs/v2/MediaSets/models/VideoMediaItemMetadata.md) | `from foundry_sdk.v2.media_sets.models import VideoMediaItemMetadata` |
**MediaSets** | [VideoOperation](docs/v2/MediaSets/models/VideoOperation.md) | `from foundry_sdk.v2.media_sets.models import VideoOperation` |
**MediaSets** | [VideoSpecification](docs/v2/MediaSets/models/VideoSpecification.md) | `from foundry_sdk.v2.media_sets.models import VideoSpecification` |
**MediaSets** | [VideoToArchiveOperation](docs/v2/MediaSets/models/VideoToArchiveOperation.md) | `from foundry_sdk.v2.media_sets.models import VideoToArchiveOperation` |
**MediaSets** | [VideoToArchiveTransformation](docs/v2/MediaSets/models/VideoToArchiveTransformation.md) | `from foundry_sdk.v2.media_sets.models import VideoToArchiveTransformation` |
**MediaSets** | [VideoToAudioOperation](docs/v2/MediaSets/models/VideoToAudioOperation.md) | `from foundry_sdk.v2.media_sets.models import VideoToAudioOperation` |
**MediaSets** | [VideoToAudioTransformation](docs/v2/MediaSets/models/VideoToAudioTransformation.md) | `from foundry_sdk.v2.media_sets.models import VideoToAudioTransformation` |
**MediaSets** | [VideoToImageOperation](docs/v2/MediaSets/models/VideoToImageOperation.md) | `from foundry_sdk.v2.media_sets.models import VideoToImageOperation` |
**MediaSets** | [VideoToImageTransformation](docs/v2/MediaSets/models/VideoToImageTransformation.md) | `from foundry_sdk.v2.media_sets.models import VideoToImageTransformation` |
**MediaSets** | [VideoToTextOperation](docs/v2/MediaSets/models/VideoToTextOperation.md) | `from foundry_sdk.v2.media_sets.models import VideoToTextOperation` |
**MediaSets** | [VideoToTextTransformation](docs/v2/MediaSets/models/VideoToTextTransformation.md) | `from foundry_sdk.v2.media_sets.models import VideoToTextTransformation` |
**MediaSets** | [VideoTransformation](docs/v2/MediaSets/models/VideoTransformation.md) | `from foundry_sdk.v2.media_sets.models import VideoTransformation` |
**MediaSets** | [VlmPreprocessingConfig](docs/v2/MediaSets/models/VlmPreprocessingConfig.md) | `from foundry_sdk.v2.media_sets.models import VlmPreprocessingConfig` |
**MediaSets** | [WaveformOperation](docs/v2/MediaSets/models/WaveformOperation.md) | `from foundry_sdk.v2.media_sets.models import WaveformOperation` |
**MediaSets** | [WavEncodeFormat](docs/v2/MediaSets/models/WavEncodeFormat.md) | `from foundry_sdk.v2.media_sets.models import WavEncodeFormat` |
**MediaSets** | [WebpFormat](docs/v2/MediaSets/models/WebpFormat.md) | `from foundry_sdk.v2.media_sets.models import WebpFormat` |
**Models** | [BooleanParameter](docs/v2/Models/models/BooleanParameter.md) | `from foundry_sdk.v2.models.models import BooleanParameter` |
**Models** | [ColumnTypeSpecId](docs/v2/Models/models/ColumnTypeSpecId.md) | `from foundry_sdk.v2.models.models import ColumnTypeSpecId` |
**Models** | [CreateModelRequest](docs/v2/Models/models/CreateModelRequest.md) | `from foundry_sdk.v2.models.models import CreateModelRequest` |
**Models** | [CreateModelStudioConfigVersionRequest](docs/v2/Models/models/CreateModelStudioConfigVersionRequest.md) | `from foundry_sdk.v2.models.models import CreateModelStudioConfigVersionRequest` |
**Models** | [CreateModelStudioRequest](docs/v2/Models/models/CreateModelStudioRequest.md) | `from foundry_sdk.v2.models.models import CreateModelStudioRequest` |
**Models** | [CreateModelVersionRequest](docs/v2/Models/models/CreateModelVersionRequest.md) | `from foundry_sdk.v2.models.models import CreateModelVersionRequest` |
**Models** | [DatasetInput](docs/v2/Models/models/DatasetInput.md) | `from foundry_sdk.v2.models.models import DatasetInput` |
**Models** | [DatetimeParameter](docs/v2/Models/models/DatetimeParameter.md) | `from foundry_sdk.v2.models.models import DatetimeParameter` |
**Models** | [DillModelFiles](docs/v2/Models/models/DillModelFiles.md) | `from foundry_sdk.v2.models.models import DillModelFiles` |
**Models** | [DoubleParameter](docs/v2/Models/models/DoubleParameter.md) | `from foundry_sdk.v2.models.models import DoubleParameter` |
**Models** | [DoubleSeriesAggregations](docs/v2/Models/models/DoubleSeriesAggregations.md) | `from foundry_sdk.v2.models.models import DoubleSeriesAggregations` |
**Models** | [DoubleSeriesV1](docs/v2/Models/models/DoubleSeriesV1.md) | `from foundry_sdk.v2.models.models import DoubleSeriesV1` |
**Models** | [DoubleSeriesValueV1](docs/v2/Models/models/DoubleSeriesValueV1.md) | `from foundry_sdk.v2.models.models import DoubleSeriesValueV1` |
**Models** | [EpochMillis](docs/v2/Models/models/EpochMillis.md) | `from foundry_sdk.v2.models.models import EpochMillis` |
**Models** | [Experiment](docs/v2/Models/models/Experiment.md) | `from foundry_sdk.v2.models.models import Experiment` |
**Models** | [ExperimentArtifactDetails](docs/v2/Models/models/ExperimentArtifactDetails.md) | `from foundry_sdk.v2.models.models import ExperimentArtifactDetails` |
**Models** | [ExperimentArtifactMetadata](docs/v2/Models/models/ExperimentArtifactMetadata.md) | `from foundry_sdk.v2.models.models import ExperimentArtifactMetadata` |
**Models** | [ExperimentArtifactName](docs/v2/Models/models/ExperimentArtifactName.md) | `from foundry_sdk.v2.models.models import ExperimentArtifactName` |
**Models** | [ExperimentAuthoringSource](docs/v2/Models/models/ExperimentAuthoringSource.md) | `from foundry_sdk.v2.models.models import ExperimentAuthoringSource` |
**Models** | [ExperimentBranch](docs/v2/Models/models/ExperimentBranch.md) | `from foundry_sdk.v2.models.models import ExperimentBranch` |
**Models** | [ExperimentCodeWorkspaceSource](docs/v2/Models/models/ExperimentCodeWorkspaceSource.md) | `from foundry_sdk.v2.models.models import ExperimentCodeWorkspaceSource` |
**Models** | [ExperimentRid](docs/v2/Models/models/ExperimentRid.md) | `from foundry_sdk.v2.models.models import ExperimentRid` |
**Models** | [ExperimentSdkSource](docs/v2/Models/models/ExperimentSdkSource.md) | `from foundry_sdk.v2.models.models import ExperimentSdkSource` |
**Models** | [ExperimentSource](docs/v2/Models/models/ExperimentSource.md) | `from foundry_sdk.v2.models.models import ExperimentSource` |
**Models** | [ExperimentStatus](docs/v2/Models/models/ExperimentStatus.md) | `from foundry_sdk.v2.models.models import ExperimentStatus` |
**Models** | [ExperimentTagText](docs/v2/Models/models/ExperimentTagText.md) | `from foundry_sdk.v2.models.models import ExperimentTagText` |
**Models** | [InconsistentArrayDimensionsError](docs/v2/Models/models/InconsistentArrayDimensionsError.md) | `from foundry_sdk.v2.models.models import InconsistentArrayDimensionsError` |
**Models** | [InferenceInputErrorType](docs/v2/Models/models/InferenceInputErrorType.md) | `from foundry_sdk.v2.models.models import InferenceInputErrorType` |
**Models** | [InputAlias](docs/v2/Models/models/InputAlias.md) | `from foundry_sdk.v2.models.models import InputAlias` |
**Models** | [IntegerParameter](docs/v2/Models/models/IntegerParameter.md) | `from foundry_sdk.v2.models.models import IntegerParameter` |
**Models** | [InvalidArrayShapeError](docs/v2/Models/models/InvalidArrayShapeError.md) | `from foundry_sdk.v2.models.models import InvalidArrayShapeError` |
**Models** | [InvalidMapFormatError](docs/v2/Models/models/InvalidMapFormatError.md) | `from foundry_sdk.v2.models.models import InvalidMapFormatError` |
**Models** | [InvalidTabularFormatError](docs/v2/Models/models/InvalidTabularFormatError.md) | `from foundry_sdk.v2.models.models import InvalidTabularFormatError` |
**Models** | [ListModelStudioConfigVersionsResponse](docs/v2/Models/models/ListModelStudioConfigVersionsResponse.md) | `from foundry_sdk.v2.models.models import ListModelStudioConfigVersionsResponse` |
**Models** | [ListModelStudioRunsResponse](docs/v2/Models/models/ListModelStudioRunsResponse.md) | `from foundry_sdk.v2.models.models import ListModelStudioRunsResponse` |
**Models** | [ListModelStudioTrainersResponse](docs/v2/Models/models/ListModelStudioTrainersResponse.md) | `from foundry_sdk.v2.models.models import ListModelStudioTrainersResponse` |
**Models** | [ListModelVersionsResponse](docs/v2/Models/models/ListModelVersionsResponse.md) | `from foundry_sdk.v2.models.models import ListModelVersionsResponse` |
**Models** | [LiveDeploymentRid](docs/v2/Models/models/LiveDeploymentRid.md) | `from foundry_sdk.v2.models.models import LiveDeploymentRid` |
**Models** | [Model](docs/v2/Models/models/Model.md) | `from foundry_sdk.v2.models.models import Model` |
**Models** | [ModelApi](docs/v2/Models/models/ModelApi.md) | `from foundry_sdk.v2.models.models import ModelApi` |
**Models** | [ModelApiAnyType](docs/v2/Models/models/ModelApiAnyType.md) | `from foundry_sdk.v2.models.models import ModelApiAnyType` |
**Models** | [ModelApiArrayType](docs/v2/Models/models/ModelApiArrayType.md) | `from foundry_sdk.v2.models.models import ModelApiArrayType` |
**Models** | [ModelApiColumn](docs/v2/Models/models/ModelApiColumn.md) | `from foundry_sdk.v2.models.models import ModelApiColumn` |
**Models** | [ModelApiDataType](docs/v2/Models/models/ModelApiDataType.md) | `from foundry_sdk.v2.models.models import ModelApiDataType` |
**Models** | [ModelApiInput](docs/v2/Models/models/ModelApiInput.md) | `from foundry_sdk.v2.models.models import ModelApiInput` |
**Models** | [ModelApiMapType](docs/v2/Models/models/ModelApiMapType.md) | `from foundry_sdk.v2.models.models import ModelApiMapType` |
**Models** | [ModelApiOutput](docs/v2/Models/models/ModelApiOutput.md) | `from foundry_sdk.v2.models.models import ModelApiOutput` |
**Models** | [ModelApiParameterType](docs/v2/Models/models/ModelApiParameterType.md) | `from foundry_sdk.v2.models.models import ModelApiParameterType` |
**Models** | [ModelApiTabularFormat](docs/v2/Models/models/ModelApiTabularFormat.md) | `from foundry_sdk.v2.models.models import ModelApiTabularFormat` |
**Models** | [ModelApiTabularType](docs/v2/Models/models/ModelApiTabularType.md) | `from foundry_sdk.v2.models.models import ModelApiTabularType` |
**Models** | [ModelFiles](docs/v2/Models/models/ModelFiles.md) | `from foundry_sdk.v2.models.models import ModelFiles` |
**Models** | [ModelName](docs/v2/Models/models/ModelName.md) | `from foundry_sdk.v2.models.models import ModelName` |
**Models** | [ModelOutput](docs/v2/Models/models/ModelOutput.md) | `from foundry_sdk.v2.models.models import ModelOutput` |
**Models** | [ModelRid](docs/v2/Models/models/ModelRid.md) | `from foundry_sdk.v2.models.models import ModelRid` |
**Models** | [ModelStudio](docs/v2/Models/models/ModelStudio.md) | `from foundry_sdk.v2.models.models import ModelStudio` |
**Models** | [ModelStudioConfigVersion](docs/v2/Models/models/ModelStudioConfigVersion.md) | `from foundry_sdk.v2.models.models import ModelStudioConfigVersion` |
**Models** | [ModelStudioConfigVersionName](docs/v2/Models/models/ModelStudioConfigVersionName.md) | `from foundry_sdk.v2.models.models import ModelStudioConfigVersionName` |
**Models** | [ModelStudioConfigVersionNumber](docs/v2/Models/models/ModelStudioConfigVersionNumber.md) | `from foundry_sdk.v2.models.models import ModelStudioConfigVersionNumber` |
**Models** | [ModelStudioInput](docs/v2/Models/models/ModelStudioInput.md) | `from foundry_sdk.v2.models.models import ModelStudioInput` |
**Models** | [ModelStudioOutput](docs/v2/Models/models/ModelStudioOutput.md) | `from foundry_sdk.v2.models.models import ModelStudioOutput` |
**Models** | [ModelStudioRid](docs/v2/Models/models/ModelStudioRid.md) | `from foundry_sdk.v2.models.models import ModelStudioRid` |
**Models** | [ModelStudioRun](docs/v2/Models/models/ModelStudioRun.md) | `from foundry_sdk.v2.models.models import ModelStudioRun` |
**Models** | [ModelStudioRunBuildRid](docs/v2/Models/models/ModelStudioRunBuildRid.md) | `from foundry_sdk.v2.models.models import ModelStudioRunBuildRid` |
**Models** | [ModelStudioRunJobRid](docs/v2/Models/models/ModelStudioRunJobRid.md) | `from foundry_sdk.v2.models.models import ModelStudioRunJobRid` |
**Models** | [ModelStudioRunModelOutput](docs/v2/Models/models/ModelStudioRunModelOutput.md) | `from foundry_sdk.v2.models.models import ModelStudioRunModelOutput` |
**Models** | [ModelStudioRunOutput](docs/v2/Models/models/ModelStudioRunOutput.md) | `from foundry_sdk.v2.models.models import ModelStudioRunOutput` |
**Models** | [ModelStudioTrainer](docs/v2/Models/models/ModelStudioTrainer.md) | `from foundry_sdk.v2.models.models import ModelStudioTrainer` |
**Models** | [ModelStudioTrainerExperimental](docs/v2/Models/models/ModelStudioTrainerExperimental.md) | `from foundry_sdk.v2.models.models import ModelStudioTrainerExperimental` |
**Models** | [ModelStudioWorkerConfig](docs/v2/Models/models/ModelStudioWorkerConfig.md) | `from foundry_sdk.v2.models.models import ModelStudioWorkerConfig` |
**Models** | [ModelVersion](docs/v2/Models/models/ModelVersion.md) | `from foundry_sdk.v2.models.models import ModelVersion` |
**Models** | [ModelVersionRid](docs/v2/Models/models/ModelVersionRid.md) | `from foundry_sdk.v2.models.models import ModelVersionRid` |
**Models** | [OutputAlias](docs/v2/Models/models/OutputAlias.md) | `from foundry_sdk.v2.models.models import OutputAlias` |
**Models** | [Parameter](docs/v2/Models/models/Parameter.md) | `from foundry_sdk.v2.models.models import Parameter` |
**Models** | [ParameterName](docs/v2/Models/models/ParameterName.md) | `from foundry_sdk.v2.models.models import ParameterName` |
**Models** | [ParameterValue](docs/v2/Models/models/ParameterValue.md) | `from foundry_sdk.v2.models.models import ParameterValue` |
**Models** | [RequiredValueMissingError](docs/v2/Models/models/RequiredValueMissingError.md) | `from foundry_sdk.v2.models.models import RequiredValueMissingError` |
**Models** | [ResourceConfiguration](docs/v2/Models/models/ResourceConfiguration.md) | `from foundry_sdk.v2.models.models import ResourceConfiguration` |
**Models** | [RunId](docs/v2/Models/models/RunId.md) | `from foundry_sdk.v2.models.models import RunId` |
**Models** | [SearchExperimentsAndFilter](docs/v2/Models/models/SearchExperimentsAndFilter.md) | `from foundry_sdk.v2.models.models import SearchExperimentsAndFilter` |
**Models** | [SearchExperimentsContainsFilter](docs/v2/Models/models/SearchExperimentsContainsFilter.md) | `from foundry_sdk.v2.models.models import SearchExperimentsContainsFilter` |
**Models** | [SearchExperimentsContainsFilterField](docs/v2/Models/models/SearchExperimentsContainsFilterField.md) | `from foundry_sdk.v2.models.models import SearchExperimentsContainsFilterField` |
**Models** | [SearchExperimentsEqualsFilter](docs/v2/Models/models/SearchExperimentsEqualsFilter.md) | `from foundry_sdk.v2.models.models import SearchExperimentsEqualsFilter` |
**Models** | [SearchExperimentsEqualsFilterField](docs/v2/Models/models/SearchExperimentsEqualsFilterField.md) | `from foundry_sdk.v2.models.models import SearchExperimentsEqualsFilterField` |
**Models** | [SearchExperimentsFilter](docs/v2/Models/models/SearchExperimentsFilter.md) | `from foundry_sdk.v2.models.models import SearchExperimentsFilter` |
**Models** | [SearchExperimentsNotFilter](docs/v2/Models/models/SearchExperimentsNotFilter.md) | `from foundry_sdk.v2.models.models import SearchExperimentsNotFilter` |
**Models** | [SearchExperimentsNumericFilterOperator](docs/v2/Models/models/SearchExperimentsNumericFilterOperator.md) | `from foundry_sdk.v2.models.models import SearchExperimentsNumericFilterOperator` |
**Models** | [SearchExperimentsOrderBy](docs/v2/Models/models/SearchExperimentsOrderBy.md) | `from foundry_sdk.v2.models.models import SearchExperimentsOrderBy` |
**Models** | [SearchExperimentsOrderByField](docs/v2/Models/models/SearchExperimentsOrderByField.md) | `from foundry_sdk.v2.models.models import SearchExperimentsOrderByField` |
**Models** | [SearchExperimentsOrFilter](docs/v2/Models/models/SearchExperimentsOrFilter.md) | `from foundry_sdk.v2.models.models import SearchExperimentsOrFilter` |
**Models** | [SearchExperimentsParameterFilter](docs/v2/Models/models/SearchExperimentsParameterFilter.md) | `from foundry_sdk.v2.models.models import SearchExperimentsParameterFilter` |
**Models** | [SearchExperimentsParameterFilterOperator](docs/v2/Models/models/SearchExperimentsParameterFilterOperator.md) | `from foundry_sdk.v2.models.models import SearchExperimentsParameterFilterOperator` |
**Models** | [SearchExperimentsRequest](docs/v2/Models/models/SearchExperimentsRequest.md) | `from foundry_sdk.v2.models.models import SearchExperimentsRequest` |
**Models** | [SearchExperimentsResponse](docs/v2/Models/models/SearchExperimentsResponse.md) | `from foundry_sdk.v2.models.models import SearchExperimentsResponse` |
**Models** | [SearchExperimentsSeriesFilter](docs/v2/Models/models/SearchExperimentsSeriesFilter.md) | `from foundry_sdk.v2.models.models import SearchExperimentsSeriesFilter` |
**Models** | [SearchExperimentsSeriesFilterField](docs/v2/Models/models/SearchExperimentsSeriesFilterField.md) | `from foundry_sdk.v2.models.models import SearchExperimentsSeriesFilterField` |
**Models** | [SearchExperimentsStartsWithFilter](docs/v2/Models/models/SearchExperimentsStartsWithFilter.md) | `from foundry_sdk.v2.models.models import SearchExperimentsStartsWithFilter` |
**Models** | [SearchExperimentsStartsWithFilterField](docs/v2/Models/models/SearchExperimentsStartsWithFilterField.md) | `from foundry_sdk.v2.models.models import SearchExperimentsStartsWithFilterField` |
**Models** | [SearchExperimentsSummaryMetricFilter](docs/v2/Models/models/SearchExperimentsSummaryMetricFilter.md) | `from foundry_sdk.v2.models.models import SearchExperimentsSummaryMetricFilter` |
**Models** | [Series](docs/v2/Models/models/Series.md) | `from foundry_sdk.v2.models.models import Series` |
**Models** | [SeriesAggregations](docs/v2/Models/models/SeriesAggregations.md) | `from foundry_sdk.v2.models.models import SeriesAggregations` |
**Models** | [SeriesAggregationsValue](docs/v2/Models/models/SeriesAggregationsValue.md) | `from foundry_sdk.v2.models.models import SeriesAggregationsValue` |
**Models** | [SeriesName](docs/v2/Models/models/SeriesName.md) | `from foundry_sdk.v2.models.models import SeriesName` |
**Models** | [StringParameter](docs/v2/Models/models/StringParameter.md) | `from foundry_sdk.v2.models.models import StringParameter` |
**Models** | [SummaryMetric](docs/v2/Models/models/SummaryMetric.md) | `from foundry_sdk.v2.models.models import SummaryMetric` |
**Models** | [SummaryMetricAggregation](docs/v2/Models/models/SummaryMetricAggregation.md) | `from foundry_sdk.v2.models.models import SummaryMetricAggregation` |
**Models** | [TableArtifactDetails](docs/v2/Models/models/TableArtifactDetails.md) | `from foundry_sdk.v2.models.models import TableArtifactDetails` |
**Models** | [TrainerDescription](docs/v2/Models/models/TrainerDescription.md) | `from foundry_sdk.v2.models.models import TrainerDescription` |
**Models** | [TrainerId](docs/v2/Models/models/TrainerId.md) | `from foundry_sdk.v2.models.models import TrainerId` |
**Models** | [TrainerInputsSpecification](docs/v2/Models/models/TrainerInputsSpecification.md) | `from foundry_sdk.v2.models.models import TrainerInputsSpecification` |
**Models** | [TrainerName](docs/v2/Models/models/TrainerName.md) | `from foundry_sdk.v2.models.models import TrainerName` |
**Models** | [TrainerOutputsSpecification](docs/v2/Models/models/TrainerOutputsSpecification.md) | `from foundry_sdk.v2.models.models import TrainerOutputsSpecification` |
**Models** | [TrainerSchemaDefinition](docs/v2/Models/models/TrainerSchemaDefinition.md) | `from foundry_sdk.v2.models.models import TrainerSchemaDefinition` |
**Models** | [TrainerType](docs/v2/Models/models/TrainerType.md) | `from foundry_sdk.v2.models.models import TrainerType` |
**Models** | [TrainerVersion](docs/v2/Models/models/TrainerVersion.md) | `from foundry_sdk.v2.models.models import TrainerVersion` |
**Models** | [TrainerVersionLocator](docs/v2/Models/models/TrainerVersionLocator.md) | `from foundry_sdk.v2.models.models import TrainerVersionLocator` |
**Models** | [TransformJsonLiveDeploymentRequest](docs/v2/Models/models/TransformJsonLiveDeploymentRequest.md) | `from foundry_sdk.v2.models.models import TransformJsonLiveDeploymentRequest` |
**Models** | [TransformLiveDeploymentResponse](docs/v2/Models/models/TransformLiveDeploymentResponse.md) | `from foundry_sdk.v2.models.models import TransformLiveDeploymentResponse` |
**Models** | [TypeMismatchError](docs/v2/Models/models/TypeMismatchError.md) | `from foundry_sdk.v2.models.models import TypeMismatchError` |
**Models** | [UnknownInputNameError](docs/v2/Models/models/UnknownInputNameError.md) | `from foundry_sdk.v2.models.models import UnknownInputNameError` |
**Models** | [UnsupportedTypeError](docs/v2/Models/models/UnsupportedTypeError.md) | `from foundry_sdk.v2.models.models import UnsupportedTypeError` |
**Ontologies** | [AbsoluteTimeRange](docs/v2/Ontologies/models/AbsoluteTimeRange.md) | `from foundry_sdk.v2.ontologies.models import AbsoluteTimeRange` |
**Ontologies** | [AbsoluteValuePropertyExpression](docs/v2/Ontologies/models/AbsoluteValuePropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import AbsoluteValuePropertyExpression` |
**Ontologies** | [ActionExecutionTime](docs/v2/Ontologies/models/ActionExecutionTime.md) | `from foundry_sdk.v2.ontologies.models import ActionExecutionTime` |
**Ontologies** | [ActionLogicRule](docs/v2/Ontologies/models/ActionLogicRule.md) | `from foundry_sdk.v2.ontologies.models import ActionLogicRule` |
**Ontologies** | [ActionParameterArrayType](docs/v2/Ontologies/models/ActionParameterArrayType.md) | `from foundry_sdk.v2.ontologies.models import ActionParameterArrayType` |
**Ontologies** | [ActionParameterType](docs/v2/Ontologies/models/ActionParameterType.md) | `from foundry_sdk.v2.ontologies.models import ActionParameterType` |
**Ontologies** | [ActionParameterV2](docs/v2/Ontologies/models/ActionParameterV2.md) | `from foundry_sdk.v2.ontologies.models import ActionParameterV2` |
**Ontologies** | [ActionResults](docs/v2/Ontologies/models/ActionResults.md) | `from foundry_sdk.v2.ontologies.models import ActionResults` |
**Ontologies** | [ActionRid](docs/v2/Ontologies/models/ActionRid.md) | `from foundry_sdk.v2.ontologies.models import ActionRid` |
**Ontologies** | [ActionTypeApiName](docs/v2/Ontologies/models/ActionTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import ActionTypeApiName` |
**Ontologies** | [ActionTypeFullMetadata](docs/v2/Ontologies/models/ActionTypeFullMetadata.md) | `from foundry_sdk.v2.ontologies.models import ActionTypeFullMetadata` |
**Ontologies** | [ActionTypeRid](docs/v2/Ontologies/models/ActionTypeRid.md) | `from foundry_sdk.v2.ontologies.models import ActionTypeRid` |
**Ontologies** | [ActionTypeV2](docs/v2/Ontologies/models/ActionTypeV2.md) | `from foundry_sdk.v2.ontologies.models import ActionTypeV2` |
**Ontologies** | [ActivePropertyTypeStatus](docs/v2/Ontologies/models/ActivePropertyTypeStatus.md) | `from foundry_sdk.v2.ontologies.models import ActivePropertyTypeStatus` |
**Ontologies** | [AddLink](docs/v2/Ontologies/models/AddLink.md) | `from foundry_sdk.v2.ontologies.models import AddLink` |
**Ontologies** | [AddLinkEdit](docs/v2/Ontologies/models/AddLinkEdit.md) | `from foundry_sdk.v2.ontologies.models import AddLinkEdit` |
**Ontologies** | [AddObject](docs/v2/Ontologies/models/AddObject.md) | `from foundry_sdk.v2.ontologies.models import AddObject` |
**Ontologies** | [AddObjectEdit](docs/v2/Ontologies/models/AddObjectEdit.md) | `from foundry_sdk.v2.ontologies.models import AddObjectEdit` |
**Ontologies** | [AddPropertyExpression](docs/v2/Ontologies/models/AddPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import AddPropertyExpression` |
**Ontologies** | [Affix](docs/v2/Ontologies/models/Affix.md) | `from foundry_sdk.v2.ontologies.models import Affix` |
**Ontologies** | [AggregateObjectSetRequestV2](docs/v2/Ontologies/models/AggregateObjectSetRequestV2.md) | `from foundry_sdk.v2.ontologies.models import AggregateObjectSetRequestV2` |
**Ontologies** | [AggregateObjectsRequestV2](docs/v2/Ontologies/models/AggregateObjectsRequestV2.md) | `from foundry_sdk.v2.ontologies.models import AggregateObjectsRequestV2` |
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
**Ontologies** | [AllOfRule](docs/v2/Ontologies/models/AllOfRule.md) | `from foundry_sdk.v2.ontologies.models import AllOfRule` |
**Ontologies** | [AndQueryV2](docs/v2/Ontologies/models/AndQueryV2.md) | `from foundry_sdk.v2.ontologies.models import AndQueryV2` |
**Ontologies** | [AnyOfRule](docs/v2/Ontologies/models/AnyOfRule.md) | `from foundry_sdk.v2.ontologies.models import AnyOfRule` |
**Ontologies** | [ApplyActionMode](docs/v2/Ontologies/models/ApplyActionMode.md) | `from foundry_sdk.v2.ontologies.models import ApplyActionMode` |
**Ontologies** | [ApplyActionOverrides](docs/v2/Ontologies/models/ApplyActionOverrides.md) | `from foundry_sdk.v2.ontologies.models import ApplyActionOverrides` |
**Ontologies** | [ApplyActionRequestOptions](docs/v2/Ontologies/models/ApplyActionRequestOptions.md) | `from foundry_sdk.v2.ontologies.models import ApplyActionRequestOptions` |
**Ontologies** | [ApplyActionRequestV2](docs/v2/Ontologies/models/ApplyActionRequestV2.md) | `from foundry_sdk.v2.ontologies.models import ApplyActionRequestV2` |
**Ontologies** | [ApplyActionWithOverridesRequest](docs/v2/Ontologies/models/ApplyActionWithOverridesRequest.md) | `from foundry_sdk.v2.ontologies.models import ApplyActionWithOverridesRequest` |
**Ontologies** | [ApplyReducersAndExtractMainValueLoadLevel](docs/v2/Ontologies/models/ApplyReducersAndExtractMainValueLoadLevel.md) | `from foundry_sdk.v2.ontologies.models import ApplyReducersAndExtractMainValueLoadLevel` |
**Ontologies** | [ApplyReducersLoadLevel](docs/v2/Ontologies/models/ApplyReducersLoadLevel.md) | `from foundry_sdk.v2.ontologies.models import ApplyReducersLoadLevel` |
**Ontologies** | [ApproximateDistinctAggregationV2](docs/v2/Ontologies/models/ApproximateDistinctAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import ApproximateDistinctAggregationV2` |
**Ontologies** | [ApproximatePercentileAggregationV2](docs/v2/Ontologies/models/ApproximatePercentileAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import ApproximatePercentileAggregationV2` |
**Ontologies** | [Arg](docs/v2/Ontologies/models/Arg.md) | `from foundry_sdk.v2.ontologies.models import Arg` |
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
**Ontologies** | [BatchApplyActionRequestV2](docs/v2/Ontologies/models/BatchApplyActionRequestV2.md) | `from foundry_sdk.v2.ontologies.models import BatchApplyActionRequestV2` |
**Ontologies** | [BatchApplyActionResponseV2](docs/v2/Ontologies/models/BatchApplyActionResponseV2.md) | `from foundry_sdk.v2.ontologies.models import BatchApplyActionResponseV2` |
**Ontologies** | [BatchedFunctionLogicRule](docs/v2/Ontologies/models/BatchedFunctionLogicRule.md) | `from foundry_sdk.v2.ontologies.models import BatchedFunctionLogicRule` |
**Ontologies** | [BatchReturnEditsMode](docs/v2/Ontologies/models/BatchReturnEditsMode.md) | `from foundry_sdk.v2.ontologies.models import BatchReturnEditsMode` |
**Ontologies** | [BlueprintIcon](docs/v2/Ontologies/models/BlueprintIcon.md) | `from foundry_sdk.v2.ontologies.models import BlueprintIcon` |
**Ontologies** | [BooleanValue](docs/v2/Ontologies/models/BooleanValue.md) | `from foundry_sdk.v2.ontologies.models import BooleanValue` |
**Ontologies** | [BoundingBoxValue](docs/v2/Ontologies/models/BoundingBoxValue.md) | `from foundry_sdk.v2.ontologies.models import BoundingBoxValue` |
**Ontologies** | [CenterPoint](docs/v2/Ontologies/models/CenterPoint.md) | `from foundry_sdk.v2.ontologies.models import CenterPoint` |
**Ontologies** | [CenterPointTypes](docs/v2/Ontologies/models/CenterPointTypes.md) | `from foundry_sdk.v2.ontologies.models import CenterPointTypes` |
**Ontologies** | [ConjunctiveMarkingSummary](docs/v2/Ontologies/models/ConjunctiveMarkingSummary.md) | `from foundry_sdk.v2.ontologies.models import ConjunctiveMarkingSummary` |
**Ontologies** | [ContainerConjunctiveMarkingSummary](docs/v2/Ontologies/models/ContainerConjunctiveMarkingSummary.md) | `from foundry_sdk.v2.ontologies.models import ContainerConjunctiveMarkingSummary` |
**Ontologies** | [ContainerDisjunctiveMarkingSummary](docs/v2/Ontologies/models/ContainerDisjunctiveMarkingSummary.md) | `from foundry_sdk.v2.ontologies.models import ContainerDisjunctiveMarkingSummary` |
**Ontologies** | [ContainsAllTermsInOrderPrefixLastTerm](docs/v2/Ontologies/models/ContainsAllTermsInOrderPrefixLastTerm.md) | `from foundry_sdk.v2.ontologies.models import ContainsAllTermsInOrderPrefixLastTerm` |
**Ontologies** | [ContainsAllTermsInOrderQuery](docs/v2/Ontologies/models/ContainsAllTermsInOrderQuery.md) | `from foundry_sdk.v2.ontologies.models import ContainsAllTermsInOrderQuery` |
**Ontologies** | [ContainsAllTermsQuery](docs/v2/Ontologies/models/ContainsAllTermsQuery.md) | `from foundry_sdk.v2.ontologies.models import ContainsAllTermsQuery` |
**Ontologies** | [ContainsAnyTermQuery](docs/v2/Ontologies/models/ContainsAnyTermQuery.md) | `from foundry_sdk.v2.ontologies.models import ContainsAnyTermQuery` |
**Ontologies** | [ContainsQueryV2](docs/v2/Ontologies/models/ContainsQueryV2.md) | `from foundry_sdk.v2.ontologies.models import ContainsQueryV2` |
**Ontologies** | [CountAggregationV2](docs/v2/Ontologies/models/CountAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import CountAggregationV2` |
**Ontologies** | [CountObjectsResponseV2](docs/v2/Ontologies/models/CountObjectsResponseV2.md) | `from foundry_sdk.v2.ontologies.models import CountObjectsResponseV2` |
**Ontologies** | [CreateEdit](docs/v2/Ontologies/models/CreateEdit.md) | `from foundry_sdk.v2.ontologies.models import CreateEdit` |
**Ontologies** | [CreateInterfaceLinkLogicRule](docs/v2/Ontologies/models/CreateInterfaceLinkLogicRule.md) | `from foundry_sdk.v2.ontologies.models import CreateInterfaceLinkLogicRule` |
**Ontologies** | [CreateInterfaceLogicRule](docs/v2/Ontologies/models/CreateInterfaceLogicRule.md) | `from foundry_sdk.v2.ontologies.models import CreateInterfaceLogicRule` |
**Ontologies** | [CreateInterfaceObjectRule](docs/v2/Ontologies/models/CreateInterfaceObjectRule.md) | `from foundry_sdk.v2.ontologies.models import CreateInterfaceObjectRule` |
**Ontologies** | [CreateLinkLogicRule](docs/v2/Ontologies/models/CreateLinkLogicRule.md) | `from foundry_sdk.v2.ontologies.models import CreateLinkLogicRule` |
**Ontologies** | [CreateLinkRule](docs/v2/Ontologies/models/CreateLinkRule.md) | `from foundry_sdk.v2.ontologies.models import CreateLinkRule` |
**Ontologies** | [CreateObjectLogicRule](docs/v2/Ontologies/models/CreateObjectLogicRule.md) | `from foundry_sdk.v2.ontologies.models import CreateObjectLogicRule` |
**Ontologies** | [CreateObjectRule](docs/v2/Ontologies/models/CreateObjectRule.md) | `from foundry_sdk.v2.ontologies.models import CreateObjectRule` |
**Ontologies** | [CreateOrModifyObjectLogicRule](docs/v2/Ontologies/models/CreateOrModifyObjectLogicRule.md) | `from foundry_sdk.v2.ontologies.models import CreateOrModifyObjectLogicRule` |
**Ontologies** | [CreateOrModifyObjectLogicRuleV2](docs/v2/Ontologies/models/CreateOrModifyObjectLogicRuleV2.md) | `from foundry_sdk.v2.ontologies.models import CreateOrModifyObjectLogicRuleV2` |
**Ontologies** | [CreateTemporaryObjectSetRequestV2](docs/v2/Ontologies/models/CreateTemporaryObjectSetRequestV2.md) | `from foundry_sdk.v2.ontologies.models import CreateTemporaryObjectSetRequestV2` |
**Ontologies** | [CreateTemporaryObjectSetResponseV2](docs/v2/Ontologies/models/CreateTemporaryObjectSetResponseV2.md) | `from foundry_sdk.v2.ontologies.models import CreateTemporaryObjectSetResponseV2` |
**Ontologies** | [CurrentTimeArgument](docs/v2/Ontologies/models/CurrentTimeArgument.md) | `from foundry_sdk.v2.ontologies.models import CurrentTimeArgument` |
**Ontologies** | [CurrentUserArgument](docs/v2/Ontologies/models/CurrentUserArgument.md) | `from foundry_sdk.v2.ontologies.models import CurrentUserArgument` |
**Ontologies** | [DataValue](docs/v2/Ontologies/models/DataValue.md) | `from foundry_sdk.v2.ontologies.models import DataValue` |
**Ontologies** | [DatetimeFormat](docs/v2/Ontologies/models/DatetimeFormat.md) | `from foundry_sdk.v2.ontologies.models import DatetimeFormat` |
**Ontologies** | [DatetimeLocalizedFormat](docs/v2/Ontologies/models/DatetimeLocalizedFormat.md) | `from foundry_sdk.v2.ontologies.models import DatetimeLocalizedFormat` |
**Ontologies** | [DatetimeLocalizedFormatType](docs/v2/Ontologies/models/DatetimeLocalizedFormatType.md) | `from foundry_sdk.v2.ontologies.models import DatetimeLocalizedFormatType` |
**Ontologies** | [DatetimeStringFormat](docs/v2/Ontologies/models/DatetimeStringFormat.md) | `from foundry_sdk.v2.ontologies.models import DatetimeStringFormat` |
**Ontologies** | [DatetimeTimezone](docs/v2/Ontologies/models/DatetimeTimezone.md) | `from foundry_sdk.v2.ontologies.models import DatetimeTimezone` |
**Ontologies** | [DatetimeTimezoneStatic](docs/v2/Ontologies/models/DatetimeTimezoneStatic.md) | `from foundry_sdk.v2.ontologies.models import DatetimeTimezoneStatic` |
**Ontologies** | [DatetimeTimezoneUser](docs/v2/Ontologies/models/DatetimeTimezoneUser.md) | `from foundry_sdk.v2.ontologies.models import DatetimeTimezoneUser` |
**Ontologies** | [DateValue](docs/v2/Ontologies/models/DateValue.md) | `from foundry_sdk.v2.ontologies.models import DateValue` |
**Ontologies** | [DecryptionResult](docs/v2/Ontologies/models/DecryptionResult.md) | `from foundry_sdk.v2.ontologies.models import DecryptionResult` |
**Ontologies** | [DeleteEdit](docs/v2/Ontologies/models/DeleteEdit.md) | `from foundry_sdk.v2.ontologies.models import DeleteEdit` |
**Ontologies** | [DeleteInterfaceLinkLogicRule](docs/v2/Ontologies/models/DeleteInterfaceLinkLogicRule.md) | `from foundry_sdk.v2.ontologies.models import DeleteInterfaceLinkLogicRule` |
**Ontologies** | [DeleteInterfaceObjectRule](docs/v2/Ontologies/models/DeleteInterfaceObjectRule.md) | `from foundry_sdk.v2.ontologies.models import DeleteInterfaceObjectRule` |
**Ontologies** | [DeleteLink](docs/v2/Ontologies/models/DeleteLink.md) | `from foundry_sdk.v2.ontologies.models import DeleteLink` |
**Ontologies** | [DeleteLinkEdit](docs/v2/Ontologies/models/DeleteLinkEdit.md) | `from foundry_sdk.v2.ontologies.models import DeleteLinkEdit` |
**Ontologies** | [DeleteLinkLogicRule](docs/v2/Ontologies/models/DeleteLinkLogicRule.md) | `from foundry_sdk.v2.ontologies.models import DeleteLinkLogicRule` |
**Ontologies** | [DeleteLinkRule](docs/v2/Ontologies/models/DeleteLinkRule.md) | `from foundry_sdk.v2.ontologies.models import DeleteLinkRule` |
**Ontologies** | [DeleteObject](docs/v2/Ontologies/models/DeleteObject.md) | `from foundry_sdk.v2.ontologies.models import DeleteObject` |
**Ontologies** | [DeleteObjectEdit](docs/v2/Ontologies/models/DeleteObjectEdit.md) | `from foundry_sdk.v2.ontologies.models import DeleteObjectEdit` |
**Ontologies** | [DeleteObjectLogicRule](docs/v2/Ontologies/models/DeleteObjectLogicRule.md) | `from foundry_sdk.v2.ontologies.models import DeleteObjectLogicRule` |
**Ontologies** | [DeleteObjectRule](docs/v2/Ontologies/models/DeleteObjectRule.md) | `from foundry_sdk.v2.ontologies.models import DeleteObjectRule` |
**Ontologies** | [DeprecatedPropertyTypeStatus](docs/v2/Ontologies/models/DeprecatedPropertyTypeStatus.md) | `from foundry_sdk.v2.ontologies.models import DeprecatedPropertyTypeStatus` |
**Ontologies** | [DerivedPropertyApiName](docs/v2/Ontologies/models/DerivedPropertyApiName.md) | `from foundry_sdk.v2.ontologies.models import DerivedPropertyApiName` |
**Ontologies** | [DerivedPropertyDefinition](docs/v2/Ontologies/models/DerivedPropertyDefinition.md) | `from foundry_sdk.v2.ontologies.models import DerivedPropertyDefinition` |
**Ontologies** | [DisjunctiveMarkingSummary](docs/v2/Ontologies/models/DisjunctiveMarkingSummary.md) | `from foundry_sdk.v2.ontologies.models import DisjunctiveMarkingSummary` |
**Ontologies** | [DividePropertyExpression](docs/v2/Ontologies/models/DividePropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import DividePropertyExpression` |
**Ontologies** | [DoesNotIntersectBoundingBoxQuery](docs/v2/Ontologies/models/DoesNotIntersectBoundingBoxQuery.md) | `from foundry_sdk.v2.ontologies.models import DoesNotIntersectBoundingBoxQuery` |
**Ontologies** | [DoesNotIntersectPolygonQuery](docs/v2/Ontologies/models/DoesNotIntersectPolygonQuery.md) | `from foundry_sdk.v2.ontologies.models import DoesNotIntersectPolygonQuery` |
**Ontologies** | [DoubleValue](docs/v2/Ontologies/models/DoubleValue.md) | `from foundry_sdk.v2.ontologies.models import DoubleValue` |
**Ontologies** | [DoubleVector](docs/v2/Ontologies/models/DoubleVector.md) | `from foundry_sdk.v2.ontologies.models import DoubleVector` |
**Ontologies** | [DurationBaseValue](docs/v2/Ontologies/models/DurationBaseValue.md) | `from foundry_sdk.v2.ontologies.models import DurationBaseValue` |
**Ontologies** | [DurationFormatStyle](docs/v2/Ontologies/models/DurationFormatStyle.md) | `from foundry_sdk.v2.ontologies.models import DurationFormatStyle` |
**Ontologies** | [DurationPrecision](docs/v2/Ontologies/models/DurationPrecision.md) | `from foundry_sdk.v2.ontologies.models import DurationPrecision` |
**Ontologies** | [EditHistoryEdit](docs/v2/Ontologies/models/EditHistoryEdit.md) | `from foundry_sdk.v2.ontologies.models import EditHistoryEdit` |
**Ontologies** | [EditsHistoryFilter](docs/v2/Ontologies/models/EditsHistoryFilter.md) | `from foundry_sdk.v2.ontologies.models import EditsHistoryFilter` |
**Ontologies** | [EditsHistoryOperationIdsFilter](docs/v2/Ontologies/models/EditsHistoryOperationIdsFilter.md) | `from foundry_sdk.v2.ontologies.models import EditsHistoryOperationIdsFilter` |
**Ontologies** | [EditsHistorySortOrder](docs/v2/Ontologies/models/EditsHistorySortOrder.md) | `from foundry_sdk.v2.ontologies.models import EditsHistorySortOrder` |
**Ontologies** | [EditsHistoryTimestampFilter](docs/v2/Ontologies/models/EditsHistoryTimestampFilter.md) | `from foundry_sdk.v2.ontologies.models import EditsHistoryTimestampFilter` |
**Ontologies** | [EntrySetType](docs/v2/Ontologies/models/EntrySetType.md) | `from foundry_sdk.v2.ontologies.models import EntrySetType` |
**Ontologies** | [EnumConstraint](docs/v2/Ontologies/models/EnumConstraint.md) | `from foundry_sdk.v2.ontologies.models import EnumConstraint` |
**Ontologies** | [EqualsQueryV2](docs/v2/Ontologies/models/EqualsQueryV2.md) | `from foundry_sdk.v2.ontologies.models import EqualsQueryV2` |
**Ontologies** | [Error](docs/v2/Ontologies/models/Error.md) | `from foundry_sdk.v2.ontologies.models import Error` |
**Ontologies** | [ErrorComputingSecurity](docs/v2/Ontologies/models/ErrorComputingSecurity.md) | `from foundry_sdk.v2.ontologies.models import ErrorComputingSecurity` |
**Ontologies** | [ErrorName](docs/v2/Ontologies/models/ErrorName.md) | `from foundry_sdk.v2.ontologies.models import ErrorName` |
**Ontologies** | [ExactDistinctAggregationV2](docs/v2/Ontologies/models/ExactDistinctAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import ExactDistinctAggregationV2` |
**Ontologies** | [ExamplePropertyTypeStatus](docs/v2/Ontologies/models/ExamplePropertyTypeStatus.md) | `from foundry_sdk.v2.ontologies.models import ExamplePropertyTypeStatus` |
**Ontologies** | [ExecuteQueryRequest](docs/v2/Ontologies/models/ExecuteQueryRequest.md) | `from foundry_sdk.v2.ontologies.models import ExecuteQueryRequest` |
**Ontologies** | [ExecuteQueryResponse](docs/v2/Ontologies/models/ExecuteQueryResponse.md) | `from foundry_sdk.v2.ontologies.models import ExecuteQueryResponse` |
**Ontologies** | [ExperimentalPropertyTypeStatus](docs/v2/Ontologies/models/ExperimentalPropertyTypeStatus.md) | `from foundry_sdk.v2.ontologies.models import ExperimentalPropertyTypeStatus` |
**Ontologies** | [ExtractDatePart](docs/v2/Ontologies/models/ExtractDatePart.md) | `from foundry_sdk.v2.ontologies.models import ExtractDatePart` |
**Ontologies** | [ExtractMainValueLoadLevel](docs/v2/Ontologies/models/ExtractMainValueLoadLevel.md) | `from foundry_sdk.v2.ontologies.models import ExtractMainValueLoadLevel` |
**Ontologies** | [ExtractPropertyExpression](docs/v2/Ontologies/models/ExtractPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import ExtractPropertyExpression` |
**Ontologies** | [FilterValue](docs/v2/Ontologies/models/FilterValue.md) | `from foundry_sdk.v2.ontologies.models import FilterValue` |
**Ontologies** | [FixedValuesMapKey](docs/v2/Ontologies/models/FixedValuesMapKey.md) | `from foundry_sdk.v2.ontologies.models import FixedValuesMapKey` |
**Ontologies** | [FunctionLogicRule](docs/v2/Ontologies/models/FunctionLogicRule.md) | `from foundry_sdk.v2.ontologies.models import FunctionLogicRule` |
**Ontologies** | [FunctionParameterName](docs/v2/Ontologies/models/FunctionParameterName.md) | `from foundry_sdk.v2.ontologies.models import FunctionParameterName` |
**Ontologies** | [FunctionRid](docs/v2/Ontologies/models/FunctionRid.md) | `from foundry_sdk.v2.ontologies.models import FunctionRid` |
**Ontologies** | [FunctionVersion](docs/v2/Ontologies/models/FunctionVersion.md) | `from foundry_sdk.v2.ontologies.models import FunctionVersion` |
**Ontologies** | [FuzzyRule](docs/v2/Ontologies/models/FuzzyRule.md) | `from foundry_sdk.v2.ontologies.models import FuzzyRule` |
**Ontologies** | [FuzzyV2](docs/v2/Ontologies/models/FuzzyV2.md) | `from foundry_sdk.v2.ontologies.models import FuzzyV2` |
**Ontologies** | [GeoJsonString](docs/v2/Ontologies/models/GeoJsonString.md) | `from foundry_sdk.v2.ontologies.models import GeoJsonString` |
**Ontologies** | [GeoShapeV2Geometry](docs/v2/Ontologies/models/GeoShapeV2Geometry.md) | `from foundry_sdk.v2.ontologies.models import GeoShapeV2Geometry` |
**Ontologies** | [GeoShapeV2Query](docs/v2/Ontologies/models/GeoShapeV2Query.md) | `from foundry_sdk.v2.ontologies.models import GeoShapeV2Query` |
**Ontologies** | [GeotemporalSeriesEntry](docs/v2/Ontologies/models/GeotemporalSeriesEntry.md) | `from foundry_sdk.v2.ontologies.models import GeotemporalSeriesEntry` |
**Ontologies** | [GeotimeSeriesValue](docs/v2/Ontologies/models/GeotimeSeriesValue.md) | `from foundry_sdk.v2.ontologies.models import GeotimeSeriesValue` |
**Ontologies** | [GetActionTypeByRidBatchRequest](docs/v2/Ontologies/models/GetActionTypeByRidBatchRequest.md) | `from foundry_sdk.v2.ontologies.models import GetActionTypeByRidBatchRequest` |
**Ontologies** | [GetActionTypeByRidBatchRequestElement](docs/v2/Ontologies/models/GetActionTypeByRidBatchRequestElement.md) | `from foundry_sdk.v2.ontologies.models import GetActionTypeByRidBatchRequestElement` |
**Ontologies** | [GetActionTypeByRidBatchResponse](docs/v2/Ontologies/models/GetActionTypeByRidBatchResponse.md) | `from foundry_sdk.v2.ontologies.models import GetActionTypeByRidBatchResponse` |
**Ontologies** | [GetSelectedPropertyOperation](docs/v2/Ontologies/models/GetSelectedPropertyOperation.md) | `from foundry_sdk.v2.ontologies.models import GetSelectedPropertyOperation` |
**Ontologies** | [GreatestPropertyExpression](docs/v2/Ontologies/models/GreatestPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import GreatestPropertyExpression` |
**Ontologies** | [GroupMemberConstraint](docs/v2/Ontologies/models/GroupMemberConstraint.md) | `from foundry_sdk.v2.ontologies.models import GroupMemberConstraint` |
**Ontologies** | [GteQueryV2](docs/v2/Ontologies/models/GteQueryV2.md) | `from foundry_sdk.v2.ontologies.models import GteQueryV2` |
**Ontologies** | [GtQueryV2](docs/v2/Ontologies/models/GtQueryV2.md) | `from foundry_sdk.v2.ontologies.models import GtQueryV2` |
**Ontologies** | [HumanReadableFormat](docs/v2/Ontologies/models/HumanReadableFormat.md) | `from foundry_sdk.v2.ontologies.models import HumanReadableFormat` |
**Ontologies** | [Icon](docs/v2/Ontologies/models/Icon.md) | `from foundry_sdk.v2.ontologies.models import Icon` |
**Ontologies** | [InQuery](docs/v2/Ontologies/models/InQuery.md) | `from foundry_sdk.v2.ontologies.models import InQuery` |
**Ontologies** | [IntegerValue](docs/v2/Ontologies/models/IntegerValue.md) | `from foundry_sdk.v2.ontologies.models import IntegerValue` |
**Ontologies** | [InterfaceDefinedPropertyType](docs/v2/Ontologies/models/InterfaceDefinedPropertyType.md) | `from foundry_sdk.v2.ontologies.models import InterfaceDefinedPropertyType` |
**Ontologies** | [InterfaceLinkType](docs/v2/Ontologies/models/InterfaceLinkType.md) | `from foundry_sdk.v2.ontologies.models import InterfaceLinkType` |
**Ontologies** | [InterfaceLinkTypeApiName](docs/v2/Ontologies/models/InterfaceLinkTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import InterfaceLinkTypeApiName` |
**Ontologies** | [InterfaceLinkTypeCardinality](docs/v2/Ontologies/models/InterfaceLinkTypeCardinality.md) | `from foundry_sdk.v2.ontologies.models import InterfaceLinkTypeCardinality` |
**Ontologies** | [InterfaceLinkTypeLinkedEntityApiName](docs/v2/Ontologies/models/InterfaceLinkTypeLinkedEntityApiName.md) | `from foundry_sdk.v2.ontologies.models import InterfaceLinkTypeLinkedEntityApiName` |
**Ontologies** | [InterfaceLinkTypeRid](docs/v2/Ontologies/models/InterfaceLinkTypeRid.md) | `from foundry_sdk.v2.ontologies.models import InterfaceLinkTypeRid` |
**Ontologies** | [InterfaceParameterPropertyArgument](docs/v2/Ontologies/models/InterfaceParameterPropertyArgument.md) | `from foundry_sdk.v2.ontologies.models import InterfaceParameterPropertyArgument` |
**Ontologies** | [InterfacePropertyApiName](docs/v2/Ontologies/models/InterfacePropertyApiName.md) | `from foundry_sdk.v2.ontologies.models import InterfacePropertyApiName` |
**Ontologies** | [InterfacePropertyLocalPropertyImplementation](docs/v2/Ontologies/models/InterfacePropertyLocalPropertyImplementation.md) | `from foundry_sdk.v2.ontologies.models import InterfacePropertyLocalPropertyImplementation` |
**Ontologies** | [InterfacePropertyReducedPropertyImplementation](docs/v2/Ontologies/models/InterfacePropertyReducedPropertyImplementation.md) | `from foundry_sdk.v2.ontologies.models import InterfacePropertyReducedPropertyImplementation` |
**Ontologies** | [InterfacePropertyStructFieldImplementation](docs/v2/Ontologies/models/InterfacePropertyStructFieldImplementation.md) | `from foundry_sdk.v2.ontologies.models import InterfacePropertyStructFieldImplementation` |
**Ontologies** | [InterfacePropertyStructImplementation](docs/v2/Ontologies/models/InterfacePropertyStructImplementation.md) | `from foundry_sdk.v2.ontologies.models import InterfacePropertyStructImplementation` |
**Ontologies** | [InterfacePropertyStructImplementationMapping](docs/v2/Ontologies/models/InterfacePropertyStructImplementationMapping.md) | `from foundry_sdk.v2.ontologies.models import InterfacePropertyStructImplementationMapping` |
**Ontologies** | [InterfacePropertyType](docs/v2/Ontologies/models/InterfacePropertyType.md) | `from foundry_sdk.v2.ontologies.models import InterfacePropertyType` |
**Ontologies** | [InterfacePropertyTypeImplementation](docs/v2/Ontologies/models/InterfacePropertyTypeImplementation.md) | `from foundry_sdk.v2.ontologies.models import InterfacePropertyTypeImplementation` |
**Ontologies** | [InterfacePropertyTypeRid](docs/v2/Ontologies/models/InterfacePropertyTypeRid.md) | `from foundry_sdk.v2.ontologies.models import InterfacePropertyTypeRid` |
**Ontologies** | [InterfaceSharedPropertyType](docs/v2/Ontologies/models/InterfaceSharedPropertyType.md) | `from foundry_sdk.v2.ontologies.models import InterfaceSharedPropertyType` |
**Ontologies** | [InterfaceToObjectTypeMapping](docs/v2/Ontologies/models/InterfaceToObjectTypeMapping.md) | `from foundry_sdk.v2.ontologies.models import InterfaceToObjectTypeMapping` |
**Ontologies** | [InterfaceToObjectTypeMappings](docs/v2/Ontologies/models/InterfaceToObjectTypeMappings.md) | `from foundry_sdk.v2.ontologies.models import InterfaceToObjectTypeMappings` |
**Ontologies** | [InterfaceToObjectTypeMappingsV2](docs/v2/Ontologies/models/InterfaceToObjectTypeMappingsV2.md) | `from foundry_sdk.v2.ontologies.models import InterfaceToObjectTypeMappingsV2` |
**Ontologies** | [InterfaceToObjectTypeMappingV2](docs/v2/Ontologies/models/InterfaceToObjectTypeMappingV2.md) | `from foundry_sdk.v2.ontologies.models import InterfaceToObjectTypeMappingV2` |
**Ontologies** | [InterfaceType](docs/v2/Ontologies/models/InterfaceType.md) | `from foundry_sdk.v2.ontologies.models import InterfaceType` |
**Ontologies** | [InterfaceTypeApiName](docs/v2/Ontologies/models/InterfaceTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import InterfaceTypeApiName` |
**Ontologies** | [InterfaceTypeRid](docs/v2/Ontologies/models/InterfaceTypeRid.md) | `from foundry_sdk.v2.ontologies.models import InterfaceTypeRid` |
**Ontologies** | [IntersectsBoundingBoxQuery](docs/v2/Ontologies/models/IntersectsBoundingBoxQuery.md) | `from foundry_sdk.v2.ontologies.models import IntersectsBoundingBoxQuery` |
**Ontologies** | [IntersectsPolygonQuery](docs/v2/Ontologies/models/IntersectsPolygonQuery.md) | `from foundry_sdk.v2.ontologies.models import IntersectsPolygonQuery` |
**Ontologies** | [IntervalQuery](docs/v2/Ontologies/models/IntervalQuery.md) | `from foundry_sdk.v2.ontologies.models import IntervalQuery` |
**Ontologies** | [IntervalQueryRule](docs/v2/Ontologies/models/IntervalQueryRule.md) | `from foundry_sdk.v2.ontologies.models import IntervalQueryRule` |
**Ontologies** | [IsNullQueryV2](docs/v2/Ontologies/models/IsNullQueryV2.md) | `from foundry_sdk.v2.ontologies.models import IsNullQueryV2` |
**Ontologies** | [KnownType](docs/v2/Ontologies/models/KnownType.md) | `from foundry_sdk.v2.ontologies.models import KnownType` |
**Ontologies** | [LeastPropertyExpression](docs/v2/Ontologies/models/LeastPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import LeastPropertyExpression` |
**Ontologies** | [LengthConstraint](docs/v2/Ontologies/models/LengthConstraint.md) | `from foundry_sdk.v2.ontologies.models import LengthConstraint` |
**Ontologies** | [LinkedInterfaceTypeApiName](docs/v2/Ontologies/models/LinkedInterfaceTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import LinkedInterfaceTypeApiName` |
**Ontologies** | [LinkedObjectLocator](docs/v2/Ontologies/models/LinkedObjectLocator.md) | `from foundry_sdk.v2.ontologies.models import LinkedObjectLocator` |
**Ontologies** | [LinkedObjectTypeApiName](docs/v2/Ontologies/models/LinkedObjectTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import LinkedObjectTypeApiName` |
**Ontologies** | [LinksFromObject](docs/v2/Ontologies/models/LinksFromObject.md) | `from foundry_sdk.v2.ontologies.models import LinksFromObject` |
**Ontologies** | [LinkSideObject](docs/v2/Ontologies/models/LinkSideObject.md) | `from foundry_sdk.v2.ontologies.models import LinkSideObject` |
**Ontologies** | [LinkTypeApiName](docs/v2/Ontologies/models/LinkTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import LinkTypeApiName` |
**Ontologies** | [LinkTypeId](docs/v2/Ontologies/models/LinkTypeId.md) | `from foundry_sdk.v2.ontologies.models import LinkTypeId` |
**Ontologies** | [LinkTypeRid](docs/v2/Ontologies/models/LinkTypeRid.md) | `from foundry_sdk.v2.ontologies.models import LinkTypeRid` |
**Ontologies** | [LinkTypeSideCardinality](docs/v2/Ontologies/models/LinkTypeSideCardinality.md) | `from foundry_sdk.v2.ontologies.models import LinkTypeSideCardinality` |
**Ontologies** | [LinkTypeSideV2](docs/v2/Ontologies/models/LinkTypeSideV2.md) | `from foundry_sdk.v2.ontologies.models import LinkTypeSideV2` |
**Ontologies** | [ListActionTypesFullMetadataResponse](docs/v2/Ontologies/models/ListActionTypesFullMetadataResponse.md) | `from foundry_sdk.v2.ontologies.models import ListActionTypesFullMetadataResponse` |
**Ontologies** | [ListActionTypesResponseV2](docs/v2/Ontologies/models/ListActionTypesResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListActionTypesResponseV2` |
**Ontologies** | [ListAttachmentsResponseV2](docs/v2/Ontologies/models/ListAttachmentsResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListAttachmentsResponseV2` |
**Ontologies** | [ListInterfaceLinkedObjectsResponse](docs/v2/Ontologies/models/ListInterfaceLinkedObjectsResponse.md) | `from foundry_sdk.v2.ontologies.models import ListInterfaceLinkedObjectsResponse` |
**Ontologies** | [ListInterfaceTypesResponse](docs/v2/Ontologies/models/ListInterfaceTypesResponse.md) | `from foundry_sdk.v2.ontologies.models import ListInterfaceTypesResponse` |
**Ontologies** | [ListLinkedObjectsResponseV2](docs/v2/Ontologies/models/ListLinkedObjectsResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListLinkedObjectsResponseV2` |
**Ontologies** | [ListObjectsForInterfaceResponse](docs/v2/Ontologies/models/ListObjectsForInterfaceResponse.md) | `from foundry_sdk.v2.ontologies.models import ListObjectsForInterfaceResponse` |
**Ontologies** | [ListObjectsResponseV2](docs/v2/Ontologies/models/ListObjectsResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListObjectsResponseV2` |
**Ontologies** | [ListObjectTypesV2Response](docs/v2/Ontologies/models/ListObjectTypesV2Response.md) | `from foundry_sdk.v2.ontologies.models import ListObjectTypesV2Response` |
**Ontologies** | [ListOntologiesV2Response](docs/v2/Ontologies/models/ListOntologiesV2Response.md) | `from foundry_sdk.v2.ontologies.models import ListOntologiesV2Response` |
**Ontologies** | [ListOntologyValueTypesResponse](docs/v2/Ontologies/models/ListOntologyValueTypesResponse.md) | `from foundry_sdk.v2.ontologies.models import ListOntologyValueTypesResponse` |
**Ontologies** | [ListOutgoingInterfaceLinkTypesResponse](docs/v2/Ontologies/models/ListOutgoingInterfaceLinkTypesResponse.md) | `from foundry_sdk.v2.ontologies.models import ListOutgoingInterfaceLinkTypesResponse` |
**Ontologies** | [ListOutgoingLinkTypesResponseV2](docs/v2/Ontologies/models/ListOutgoingLinkTypesResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListOutgoingLinkTypesResponseV2` |
**Ontologies** | [ListQueryTypesResponseV2](docs/v2/Ontologies/models/ListQueryTypesResponseV2.md) | `from foundry_sdk.v2.ontologies.models import ListQueryTypesResponseV2` |
**Ontologies** | [LoadObjectSetLinksRequestV2](docs/v2/Ontologies/models/LoadObjectSetLinksRequestV2.md) | `from foundry_sdk.v2.ontologies.models import LoadObjectSetLinksRequestV2` |
**Ontologies** | [LoadObjectSetLinksResponseV2](docs/v2/Ontologies/models/LoadObjectSetLinksResponseV2.md) | `from foundry_sdk.v2.ontologies.models import LoadObjectSetLinksResponseV2` |
**Ontologies** | [LoadObjectSetRequestV2](docs/v2/Ontologies/models/LoadObjectSetRequestV2.md) | `from foundry_sdk.v2.ontologies.models import LoadObjectSetRequestV2` |
**Ontologies** | [LoadObjectSetResponseV2](docs/v2/Ontologies/models/LoadObjectSetResponseV2.md) | `from foundry_sdk.v2.ontologies.models import LoadObjectSetResponseV2` |
**Ontologies** | [LoadObjectSetV2MultipleObjectTypesRequest](docs/v2/Ontologies/models/LoadObjectSetV2MultipleObjectTypesRequest.md) | `from foundry_sdk.v2.ontologies.models import LoadObjectSetV2MultipleObjectTypesRequest` |
**Ontologies** | [LoadObjectSetV2MultipleObjectTypesResponse](docs/v2/Ontologies/models/LoadObjectSetV2MultipleObjectTypesResponse.md) | `from foundry_sdk.v2.ontologies.models import LoadObjectSetV2MultipleObjectTypesResponse` |
**Ontologies** | [LoadObjectSetV2ObjectsOrInterfacesRequest](docs/v2/Ontologies/models/LoadObjectSetV2ObjectsOrInterfacesRequest.md) | `from foundry_sdk.v2.ontologies.models import LoadObjectSetV2ObjectsOrInterfacesRequest` |
**Ontologies** | [LoadObjectSetV2ObjectsOrInterfacesResponse](docs/v2/Ontologies/models/LoadObjectSetV2ObjectsOrInterfacesResponse.md) | `from foundry_sdk.v2.ontologies.models import LoadObjectSetV2ObjectsOrInterfacesResponse` |
**Ontologies** | [LoadOntologyMetadataRequest](docs/v2/Ontologies/models/LoadOntologyMetadataRequest.md) | `from foundry_sdk.v2.ontologies.models import LoadOntologyMetadataRequest` |
**Ontologies** | [LogicRule](docs/v2/Ontologies/models/LogicRule.md) | `from foundry_sdk.v2.ontologies.models import LogicRule` |
**Ontologies** | [LogicRuleArgument](docs/v2/Ontologies/models/LogicRuleArgument.md) | `from foundry_sdk.v2.ontologies.models import LogicRuleArgument` |
**Ontologies** | [LongValue](docs/v2/Ontologies/models/LongValue.md) | `from foundry_sdk.v2.ontologies.models import LongValue` |
**Ontologies** | [LteQueryV2](docs/v2/Ontologies/models/LteQueryV2.md) | `from foundry_sdk.v2.ontologies.models import LteQueryV2` |
**Ontologies** | [LtQueryV2](docs/v2/Ontologies/models/LtQueryV2.md) | `from foundry_sdk.v2.ontologies.models import LtQueryV2` |
**Ontologies** | [MarkingId](docs/v2/Ontologies/models/MarkingId.md) | `from foundry_sdk.v2.ontologies.models import MarkingId` |
**Ontologies** | [MatchRule](docs/v2/Ontologies/models/MatchRule.md) | `from foundry_sdk.v2.ontologies.models import MatchRule` |
**Ontologies** | [MaxAggregationV2](docs/v2/Ontologies/models/MaxAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import MaxAggregationV2` |
**Ontologies** | [MediaMetadata](docs/v2/Ontologies/models/MediaMetadata.md) | `from foundry_sdk.v2.ontologies.models import MediaMetadata` |
**Ontologies** | [MethodObjectSet](docs/v2/Ontologies/models/MethodObjectSet.md) | `from foundry_sdk.v2.ontologies.models import MethodObjectSet` |
**Ontologies** | [MinAggregationV2](docs/v2/Ontologies/models/MinAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import MinAggregationV2` |
**Ontologies** | [ModifyEdit](docs/v2/Ontologies/models/ModifyEdit.md) | `from foundry_sdk.v2.ontologies.models import ModifyEdit` |
**Ontologies** | [ModifyInterfaceLogicRule](docs/v2/Ontologies/models/ModifyInterfaceLogicRule.md) | `from foundry_sdk.v2.ontologies.models import ModifyInterfaceLogicRule` |
**Ontologies** | [ModifyInterfaceObjectRule](docs/v2/Ontologies/models/ModifyInterfaceObjectRule.md) | `from foundry_sdk.v2.ontologies.models import ModifyInterfaceObjectRule` |
**Ontologies** | [ModifyObject](docs/v2/Ontologies/models/ModifyObject.md) | `from foundry_sdk.v2.ontologies.models import ModifyObject` |
**Ontologies** | [ModifyObjectEdit](docs/v2/Ontologies/models/ModifyObjectEdit.md) | `from foundry_sdk.v2.ontologies.models import ModifyObjectEdit` |
**Ontologies** | [ModifyObjectLogicRule](docs/v2/Ontologies/models/ModifyObjectLogicRule.md) | `from foundry_sdk.v2.ontologies.models import ModifyObjectLogicRule` |
**Ontologies** | [ModifyObjectRule](docs/v2/Ontologies/models/ModifyObjectRule.md) | `from foundry_sdk.v2.ontologies.models import ModifyObjectRule` |
**Ontologies** | [MultiplyPropertyExpression](docs/v2/Ontologies/models/MultiplyPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import MultiplyPropertyExpression` |
**Ontologies** | [NearestNeighborsQuery](docs/v2/Ontologies/models/NearestNeighborsQuery.md) | `from foundry_sdk.v2.ontologies.models import NearestNeighborsQuery` |
**Ontologies** | [NearestNeighborsQueryText](docs/v2/Ontologies/models/NearestNeighborsQueryText.md) | `from foundry_sdk.v2.ontologies.models import NearestNeighborsQueryText` |
**Ontologies** | [NegatePropertyExpression](docs/v2/Ontologies/models/NegatePropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import NegatePropertyExpression` |
**Ontologies** | [NestedInterfacePropertyTypeImplementation](docs/v2/Ontologies/models/NestedInterfacePropertyTypeImplementation.md) | `from foundry_sdk.v2.ontologies.models import NestedInterfacePropertyTypeImplementation` |
**Ontologies** | [NestedQueryAggregation](docs/v2/Ontologies/models/NestedQueryAggregation.md) | `from foundry_sdk.v2.ontologies.models import NestedQueryAggregation` |
**Ontologies** | [NotQueryV2](docs/v2/Ontologies/models/NotQueryV2.md) | `from foundry_sdk.v2.ontologies.models import NotQueryV2` |
**Ontologies** | [NumberFormatAffix](docs/v2/Ontologies/models/NumberFormatAffix.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatAffix` |
**Ontologies** | [NumberFormatCurrency](docs/v2/Ontologies/models/NumberFormatCurrency.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatCurrency` |
**Ontologies** | [NumberFormatCurrencyStyle](docs/v2/Ontologies/models/NumberFormatCurrencyStyle.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatCurrencyStyle` |
**Ontologies** | [NumberFormatCustomUnit](docs/v2/Ontologies/models/NumberFormatCustomUnit.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatCustomUnit` |
**Ontologies** | [NumberFormatDuration](docs/v2/Ontologies/models/NumberFormatDuration.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatDuration` |
**Ontologies** | [NumberFormatFixedValues](docs/v2/Ontologies/models/NumberFormatFixedValues.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatFixedValues` |
**Ontologies** | [NumberFormatNotation](docs/v2/Ontologies/models/NumberFormatNotation.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatNotation` |
**Ontologies** | [NumberFormatOptions](docs/v2/Ontologies/models/NumberFormatOptions.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatOptions` |
**Ontologies** | [NumberFormatRatio](docs/v2/Ontologies/models/NumberFormatRatio.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatRatio` |
**Ontologies** | [NumberFormatScale](docs/v2/Ontologies/models/NumberFormatScale.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatScale` |
**Ontologies** | [NumberFormatStandard](docs/v2/Ontologies/models/NumberFormatStandard.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatStandard` |
**Ontologies** | [NumberFormatStandardUnit](docs/v2/Ontologies/models/NumberFormatStandardUnit.md) | `from foundry_sdk.v2.ontologies.models import NumberFormatStandardUnit` |
**Ontologies** | [NumberRatioType](docs/v2/Ontologies/models/NumberRatioType.md) | `from foundry_sdk.v2.ontologies.models import NumberRatioType` |
**Ontologies** | [NumberRoundingMode](docs/v2/Ontologies/models/NumberRoundingMode.md) | `from foundry_sdk.v2.ontologies.models import NumberRoundingMode` |
**Ontologies** | [NumberScaleType](docs/v2/Ontologies/models/NumberScaleType.md) | `from foundry_sdk.v2.ontologies.models import NumberScaleType` |
**Ontologies** | [ObjectEdit](docs/v2/Ontologies/models/ObjectEdit.md) | `from foundry_sdk.v2.ontologies.models import ObjectEdit` |
**Ontologies** | [ObjectEditHistoryEntry](docs/v2/Ontologies/models/ObjectEditHistoryEntry.md) | `from foundry_sdk.v2.ontologies.models import ObjectEditHistoryEntry` |
**Ontologies** | [ObjectEdits](docs/v2/Ontologies/models/ObjectEdits.md) | `from foundry_sdk.v2.ontologies.models import ObjectEdits` |
**Ontologies** | [ObjectLoadingResponseOptions](docs/v2/Ontologies/models/ObjectLoadingResponseOptions.md) | `from foundry_sdk.v2.ontologies.models import ObjectLoadingResponseOptions` |
**Ontologies** | [ObjectParameterPropertyArgument](docs/v2/Ontologies/models/ObjectParameterPropertyArgument.md) | `from foundry_sdk.v2.ontologies.models import ObjectParameterPropertyArgument` |
**Ontologies** | [ObjectPrimaryKey](docs/v2/Ontologies/models/ObjectPrimaryKey.md) | `from foundry_sdk.v2.ontologies.models import ObjectPrimaryKey` |
**Ontologies** | [ObjectPrimaryKeyV2](docs/v2/Ontologies/models/ObjectPrimaryKeyV2.md) | `from foundry_sdk.v2.ontologies.models import ObjectPrimaryKeyV2` |
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
**Ontologies** | [ObjectSetStreamSubscribeRequest](docs/v2/Ontologies/models/ObjectSetStreamSubscribeRequest.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetStreamSubscribeRequest` |
**Ontologies** | [ObjectSetStreamSubscribeRequests](docs/v2/Ontologies/models/ObjectSetStreamSubscribeRequests.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetStreamSubscribeRequests` |
**Ontologies** | [ObjectSetSubscribeResponse](docs/v2/Ontologies/models/ObjectSetSubscribeResponse.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetSubscribeResponse` |
**Ontologies** | [ObjectSetSubscribeResponses](docs/v2/Ontologies/models/ObjectSetSubscribeResponses.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetSubscribeResponses` |
**Ontologies** | [ObjectSetSubtractType](docs/v2/Ontologies/models/ObjectSetSubtractType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetSubtractType` |
**Ontologies** | [ObjectSetUnionType](docs/v2/Ontologies/models/ObjectSetUnionType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetUnionType` |
**Ontologies** | [ObjectSetUpdate](docs/v2/Ontologies/models/ObjectSetUpdate.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetUpdate` |
**Ontologies** | [ObjectSetUpdates](docs/v2/Ontologies/models/ObjectSetUpdates.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetUpdates` |
**Ontologies** | [ObjectSetWithPropertiesType](docs/v2/Ontologies/models/ObjectSetWithPropertiesType.md) | `from foundry_sdk.v2.ontologies.models import ObjectSetWithPropertiesType` |
**Ontologies** | [ObjectState](docs/v2/Ontologies/models/ObjectState.md) | `from foundry_sdk.v2.ontologies.models import ObjectState` |
**Ontologies** | [ObjectTypeApiName](docs/v2/Ontologies/models/ObjectTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeApiName` |
**Ontologies** | [ObjectTypeEdits](docs/v2/Ontologies/models/ObjectTypeEdits.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeEdits` |
**Ontologies** | [ObjectTypeEditsHistoryRequest](docs/v2/Ontologies/models/ObjectTypeEditsHistoryRequest.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeEditsHistoryRequest` |
**Ontologies** | [ObjectTypeEditsHistoryResponse](docs/v2/Ontologies/models/ObjectTypeEditsHistoryResponse.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeEditsHistoryResponse` |
**Ontologies** | [ObjectTypeFullMetadata](docs/v2/Ontologies/models/ObjectTypeFullMetadata.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeFullMetadata` |
**Ontologies** | [ObjectTypeId](docs/v2/Ontologies/models/ObjectTypeId.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeId` |
**Ontologies** | [ObjectTypeInterfaceImplementation](docs/v2/Ontologies/models/ObjectTypeInterfaceImplementation.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeInterfaceImplementation` |
**Ontologies** | [ObjectTypeRid](docs/v2/Ontologies/models/ObjectTypeRid.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeRid` |
**Ontologies** | [ObjectTypeV2](docs/v2/Ontologies/models/ObjectTypeV2.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeV2` |
**Ontologies** | [ObjectTypeVisibility](docs/v2/Ontologies/models/ObjectTypeVisibility.md) | `from foundry_sdk.v2.ontologies.models import ObjectTypeVisibility` |
**Ontologies** | [ObjectUpdate](docs/v2/Ontologies/models/ObjectUpdate.md) | `from foundry_sdk.v2.ontologies.models import ObjectUpdate` |
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
**Ontologies** | [OntologyObjectArrayTypeReducer](docs/v2/Ontologies/models/OntologyObjectArrayTypeReducer.md) | `from foundry_sdk.v2.ontologies.models import OntologyObjectArrayTypeReducer` |
**Ontologies** | [OntologyObjectArrayTypeReducerSortDirection](docs/v2/Ontologies/models/OntologyObjectArrayTypeReducerSortDirection.md) | `from foundry_sdk.v2.ontologies.models import OntologyObjectArrayTypeReducerSortDirection` |
**Ontologies** | [OntologyObjectSetType](docs/v2/Ontologies/models/OntologyObjectSetType.md) | `from foundry_sdk.v2.ontologies.models import OntologyObjectSetType` |
**Ontologies** | [OntologyObjectType](docs/v2/Ontologies/models/OntologyObjectType.md) | `from foundry_sdk.v2.ontologies.models import OntologyObjectType` |
**Ontologies** | [OntologyObjectTypeReferenceType](docs/v2/Ontologies/models/OntologyObjectTypeReferenceType.md) | `from foundry_sdk.v2.ontologies.models import OntologyObjectTypeReferenceType` |
**Ontologies** | [OntologyObjectV2](docs/v2/Ontologies/models/OntologyObjectV2.md) | `from foundry_sdk.v2.ontologies.models import OntologyObjectV2` |
**Ontologies** | [OntologyRid](docs/v2/Ontologies/models/OntologyRid.md) | `from foundry_sdk.v2.ontologies.models import OntologyRid` |
**Ontologies** | [OntologySetType](docs/v2/Ontologies/models/OntologySetType.md) | `from foundry_sdk.v2.ontologies.models import OntologySetType` |
**Ontologies** | [OntologyStructField](docs/v2/Ontologies/models/OntologyStructField.md) | `from foundry_sdk.v2.ontologies.models import OntologyStructField` |
**Ontologies** | [OntologyStructType](docs/v2/Ontologies/models/OntologyStructType.md) | `from foundry_sdk.v2.ontologies.models import OntologyStructType` |
**Ontologies** | [OntologyTransactionId](docs/v2/Ontologies/models/OntologyTransactionId.md) | `from foundry_sdk.v2.ontologies.models import OntologyTransactionId` |
**Ontologies** | [OntologyV2](docs/v2/Ontologies/models/OntologyV2.md) | `from foundry_sdk.v2.ontologies.models import OntologyV2` |
**Ontologies** | [OntologyValueType](docs/v2/Ontologies/models/OntologyValueType.md) | `from foundry_sdk.v2.ontologies.models import OntologyValueType` |
**Ontologies** | [OrderBy](docs/v2/Ontologies/models/OrderBy.md) | `from foundry_sdk.v2.ontologies.models import OrderBy` |
**Ontologies** | [OrderByDirection](docs/v2/Ontologies/models/OrderByDirection.md) | `from foundry_sdk.v2.ontologies.models import OrderByDirection` |
**Ontologies** | [OrQueryV2](docs/v2/Ontologies/models/OrQueryV2.md) | `from foundry_sdk.v2.ontologies.models import OrQueryV2` |
**Ontologies** | [ParameterEvaluatedConstraint](docs/v2/Ontologies/models/ParameterEvaluatedConstraint.md) | `from foundry_sdk.v2.ontologies.models import ParameterEvaluatedConstraint` |
**Ontologies** | [ParameterEvaluationResult](docs/v2/Ontologies/models/ParameterEvaluationResult.md) | `from foundry_sdk.v2.ontologies.models import ParameterEvaluationResult` |
**Ontologies** | [ParameterId](docs/v2/Ontologies/models/ParameterId.md) | `from foundry_sdk.v2.ontologies.models import ParameterId` |
**Ontologies** | [ParameterIdArgument](docs/v2/Ontologies/models/ParameterIdArgument.md) | `from foundry_sdk.v2.ontologies.models import ParameterIdArgument` |
**Ontologies** | [ParameterOption](docs/v2/Ontologies/models/ParameterOption.md) | `from foundry_sdk.v2.ontologies.models import ParameterOption` |
**Ontologies** | [Plaintext](docs/v2/Ontologies/models/Plaintext.md) | `from foundry_sdk.v2.ontologies.models import Plaintext` |
**Ontologies** | [PolygonValue](docs/v2/Ontologies/models/PolygonValue.md) | `from foundry_sdk.v2.ontologies.models import PolygonValue` |
**Ontologies** | [PostTransactionEditsRequest](docs/v2/Ontologies/models/PostTransactionEditsRequest.md) | `from foundry_sdk.v2.ontologies.models import PostTransactionEditsRequest` |
**Ontologies** | [PostTransactionEditsResponse](docs/v2/Ontologies/models/PostTransactionEditsResponse.md) | `from foundry_sdk.v2.ontologies.models import PostTransactionEditsResponse` |
**Ontologies** | [PreciseDuration](docs/v2/Ontologies/models/PreciseDuration.md) | `from foundry_sdk.v2.ontologies.models import PreciseDuration` |
**Ontologies** | [PreciseTimeUnit](docs/v2/Ontologies/models/PreciseTimeUnit.md) | `from foundry_sdk.v2.ontologies.models import PreciseTimeUnit` |
**Ontologies** | [PrefixOnLastTokenRule](docs/v2/Ontologies/models/PrefixOnLastTokenRule.md) | `from foundry_sdk.v2.ontologies.models import PrefixOnLastTokenRule` |
**Ontologies** | [PrimaryKeyValue](docs/v2/Ontologies/models/PrimaryKeyValue.md) | `from foundry_sdk.v2.ontologies.models import PrimaryKeyValue` |
**Ontologies** | [PrimaryKeyValueV2](docs/v2/Ontologies/models/PrimaryKeyValueV2.md) | `from foundry_sdk.v2.ontologies.models import PrimaryKeyValueV2` |
**Ontologies** | [PropertyApiName](docs/v2/Ontologies/models/PropertyApiName.md) | `from foundry_sdk.v2.ontologies.models import PropertyApiName` |
**Ontologies** | [PropertyApiNameSelector](docs/v2/Ontologies/models/PropertyApiNameSelector.md) | `from foundry_sdk.v2.ontologies.models import PropertyApiNameSelector` |
**Ontologies** | [PropertyBooleanFormattingRule](docs/v2/Ontologies/models/PropertyBooleanFormattingRule.md) | `from foundry_sdk.v2.ontologies.models import PropertyBooleanFormattingRule` |
**Ontologies** | [PropertyDateFormattingRule](docs/v2/Ontologies/models/PropertyDateFormattingRule.md) | `from foundry_sdk.v2.ontologies.models import PropertyDateFormattingRule` |
**Ontologies** | [PropertyFilter](docs/v2/Ontologies/models/PropertyFilter.md) | `from foundry_sdk.v2.ontologies.models import PropertyFilter` |
**Ontologies** | [PropertyId](docs/v2/Ontologies/models/PropertyId.md) | `from foundry_sdk.v2.ontologies.models import PropertyId` |
**Ontologies** | [PropertyIdentifier](docs/v2/Ontologies/models/PropertyIdentifier.md) | `from foundry_sdk.v2.ontologies.models import PropertyIdentifier` |
**Ontologies** | [PropertyImplementation](docs/v2/Ontologies/models/PropertyImplementation.md) | `from foundry_sdk.v2.ontologies.models import PropertyImplementation` |
**Ontologies** | [PropertyKnownTypeFormattingRule](docs/v2/Ontologies/models/PropertyKnownTypeFormattingRule.md) | `from foundry_sdk.v2.ontologies.models import PropertyKnownTypeFormattingRule` |
**Ontologies** | [PropertyLoadLevel](docs/v2/Ontologies/models/PropertyLoadLevel.md) | `from foundry_sdk.v2.ontologies.models import PropertyLoadLevel` |
**Ontologies** | [PropertyMarkingSummary](docs/v2/Ontologies/models/PropertyMarkingSummary.md) | `from foundry_sdk.v2.ontologies.models import PropertyMarkingSummary` |
**Ontologies** | [PropertyNumberFormattingRule](docs/v2/Ontologies/models/PropertyNumberFormattingRule.md) | `from foundry_sdk.v2.ontologies.models import PropertyNumberFormattingRule` |
**Ontologies** | [PropertyNumberFormattingRuleType](docs/v2/Ontologies/models/PropertyNumberFormattingRuleType.md) | `from foundry_sdk.v2.ontologies.models import PropertyNumberFormattingRuleType` |
**Ontologies** | [PropertyOrStructFieldOfPropertyImplementation](docs/v2/Ontologies/models/PropertyOrStructFieldOfPropertyImplementation.md) | `from foundry_sdk.v2.ontologies.models import PropertyOrStructFieldOfPropertyImplementation` |
**Ontologies** | [PropertySecurities](docs/v2/Ontologies/models/PropertySecurities.md) | `from foundry_sdk.v2.ontologies.models import PropertySecurities` |
**Ontologies** | [PropertySecurity](docs/v2/Ontologies/models/PropertySecurity.md) | `from foundry_sdk.v2.ontologies.models import PropertySecurity` |
**Ontologies** | [PropertyTimestampFormattingRule](docs/v2/Ontologies/models/PropertyTimestampFormattingRule.md) | `from foundry_sdk.v2.ontologies.models import PropertyTimestampFormattingRule` |
**Ontologies** | [PropertyTypeApiName](docs/v2/Ontologies/models/PropertyTypeApiName.md) | `from foundry_sdk.v2.ontologies.models import PropertyTypeApiName` |
**Ontologies** | [PropertyTypeReference](docs/v2/Ontologies/models/PropertyTypeReference.md) | `from foundry_sdk.v2.ontologies.models import PropertyTypeReference` |
**Ontologies** | [PropertyTypeReferenceOrStringConstant](docs/v2/Ontologies/models/PropertyTypeReferenceOrStringConstant.md) | `from foundry_sdk.v2.ontologies.models import PropertyTypeReferenceOrStringConstant` |
**Ontologies** | [PropertyTypeRid](docs/v2/Ontologies/models/PropertyTypeRid.md) | `from foundry_sdk.v2.ontologies.models import PropertyTypeRid` |
**Ontologies** | [PropertyTypeStatus](docs/v2/Ontologies/models/PropertyTypeStatus.md) | `from foundry_sdk.v2.ontologies.models import PropertyTypeStatus` |
**Ontologies** | [PropertyTypeVisibility](docs/v2/Ontologies/models/PropertyTypeVisibility.md) | `from foundry_sdk.v2.ontologies.models import PropertyTypeVisibility` |
**Ontologies** | [PropertyV2](docs/v2/Ontologies/models/PropertyV2.md) | `from foundry_sdk.v2.ontologies.models import PropertyV2` |
**Ontologies** | [PropertyValue](docs/v2/Ontologies/models/PropertyValue.md) | `from foundry_sdk.v2.ontologies.models import PropertyValue` |
**Ontologies** | [PropertyValueEscapedString](docs/v2/Ontologies/models/PropertyValueEscapedString.md) | `from foundry_sdk.v2.ontologies.models import PropertyValueEscapedString` |
**Ontologies** | [PropertyValueFormattingRule](docs/v2/Ontologies/models/PropertyValueFormattingRule.md) | `from foundry_sdk.v2.ontologies.models import PropertyValueFormattingRule` |
**Ontologies** | [PropertyWithLoadLevelSelector](docs/v2/Ontologies/models/PropertyWithLoadLevelSelector.md) | `from foundry_sdk.v2.ontologies.models import PropertyWithLoadLevelSelector` |
**Ontologies** | [QosError](docs/v2/Ontologies/models/QosError.md) | `from foundry_sdk.v2.ontologies.models import QosError` |
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
**Ontologies** | [Reason](docs/v2/Ontologies/models/Reason.md) | `from foundry_sdk.v2.ontologies.models import Reason` |
**Ontologies** | [ReasonType](docs/v2/Ontologies/models/ReasonType.md) | `from foundry_sdk.v2.ontologies.models import ReasonType` |
**Ontologies** | [ReferenceUpdate](docs/v2/Ontologies/models/ReferenceUpdate.md) | `from foundry_sdk.v2.ontologies.models import ReferenceUpdate` |
**Ontologies** | [ReferenceValue](docs/v2/Ontologies/models/ReferenceValue.md) | `from foundry_sdk.v2.ontologies.models import ReferenceValue` |
**Ontologies** | [RefreshObjectSet](docs/v2/Ontologies/models/RefreshObjectSet.md) | `from foundry_sdk.v2.ontologies.models import RefreshObjectSet` |
**Ontologies** | [RegexConstraint](docs/v2/Ontologies/models/RegexConstraint.md) | `from foundry_sdk.v2.ontologies.models import RegexConstraint` |
**Ontologies** | [RegexQuery](docs/v2/Ontologies/models/RegexQuery.md) | `from foundry_sdk.v2.ontologies.models import RegexQuery` |
**Ontologies** | [RelativeDateRangeBound](docs/v2/Ontologies/models/RelativeDateRangeBound.md) | `from foundry_sdk.v2.ontologies.models import RelativeDateRangeBound` |
**Ontologies** | [RelativeDateRangeQuery](docs/v2/Ontologies/models/RelativeDateRangeQuery.md) | `from foundry_sdk.v2.ontologies.models import RelativeDateRangeQuery` |
**Ontologies** | [RelativePointInTime](docs/v2/Ontologies/models/RelativePointInTime.md) | `from foundry_sdk.v2.ontologies.models import RelativePointInTime` |
**Ontologies** | [RelativeTime](docs/v2/Ontologies/models/RelativeTime.md) | `from foundry_sdk.v2.ontologies.models import RelativeTime` |
**Ontologies** | [RelativeTimeRange](docs/v2/Ontologies/models/RelativeTimeRange.md) | `from foundry_sdk.v2.ontologies.models import RelativeTimeRange` |
**Ontologies** | [RelativeTimeRelation](docs/v2/Ontologies/models/RelativeTimeRelation.md) | `from foundry_sdk.v2.ontologies.models import RelativeTimeRelation` |
**Ontologies** | [RelativeTimeSeriesTimeUnit](docs/v2/Ontologies/models/RelativeTimeSeriesTimeUnit.md) | `from foundry_sdk.v2.ontologies.models import RelativeTimeSeriesTimeUnit` |
**Ontologies** | [RelativeTimeUnit](docs/v2/Ontologies/models/RelativeTimeUnit.md) | `from foundry_sdk.v2.ontologies.models import RelativeTimeUnit` |
**Ontologies** | [RequestId](docs/v2/Ontologies/models/RequestId.md) | `from foundry_sdk.v2.ontologies.models import RequestId` |
**Ontologies** | [ResolvedInterfacePropertyType](docs/v2/Ontologies/models/ResolvedInterfacePropertyType.md) | `from foundry_sdk.v2.ontologies.models import ResolvedInterfacePropertyType` |
**Ontologies** | [ReturnEditsMode](docs/v2/Ontologies/models/ReturnEditsMode.md) | `from foundry_sdk.v2.ontologies.models import ReturnEditsMode` |
**Ontologies** | [RidConstraint](docs/v2/Ontologies/models/RidConstraint.md) | `from foundry_sdk.v2.ontologies.models import RidConstraint` |
**Ontologies** | [RollingAggregateWindowPoints](docs/v2/Ontologies/models/RollingAggregateWindowPoints.md) | `from foundry_sdk.v2.ontologies.models import RollingAggregateWindowPoints` |
**Ontologies** | [SdkPackageName](docs/v2/Ontologies/models/SdkPackageName.md) | `from foundry_sdk.v2.ontologies.models import SdkPackageName` |
**Ontologies** | [SdkPackageRid](docs/v2/Ontologies/models/SdkPackageRid.md) | `from foundry_sdk.v2.ontologies.models import SdkPackageRid` |
**Ontologies** | [SdkVersion](docs/v2/Ontologies/models/SdkVersion.md) | `from foundry_sdk.v2.ontologies.models import SdkVersion` |
**Ontologies** | [SearchJsonQueryV2](docs/v2/Ontologies/models/SearchJsonQueryV2.md) | `from foundry_sdk.v2.ontologies.models import SearchJsonQueryV2` |
**Ontologies** | [SearchObjectsForInterfaceRequest](docs/v2/Ontologies/models/SearchObjectsForInterfaceRequest.md) | `from foundry_sdk.v2.ontologies.models import SearchObjectsForInterfaceRequest` |
**Ontologies** | [SearchObjectsRequestV2](docs/v2/Ontologies/models/SearchObjectsRequestV2.md) | `from foundry_sdk.v2.ontologies.models import SearchObjectsRequestV2` |
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
**Ontologies** | [SpatialFilterMode](docs/v2/Ontologies/models/SpatialFilterMode.md) | `from foundry_sdk.v2.ontologies.models import SpatialFilterMode` |
**Ontologies** | [StartsWithQuery](docs/v2/Ontologies/models/StartsWithQuery.md) | `from foundry_sdk.v2.ontologies.models import StartsWithQuery` |
**Ontologies** | [StaticArgument](docs/v2/Ontologies/models/StaticArgument.md) | `from foundry_sdk.v2.ontologies.models import StaticArgument` |
**Ontologies** | [StreamGeotemporalSeriesValuesRequest](docs/v2/Ontologies/models/StreamGeotemporalSeriesValuesRequest.md) | `from foundry_sdk.v2.ontologies.models import StreamGeotemporalSeriesValuesRequest` |
**Ontologies** | [StreamingOutputFormat](docs/v2/Ontologies/models/StreamingOutputFormat.md) | `from foundry_sdk.v2.ontologies.models import StreamingOutputFormat` |
**Ontologies** | [StreamMessage](docs/v2/Ontologies/models/StreamMessage.md) | `from foundry_sdk.v2.ontologies.models import StreamMessage` |
**Ontologies** | [StreamTimeSeriesPointsRequest](docs/v2/Ontologies/models/StreamTimeSeriesPointsRequest.md) | `from foundry_sdk.v2.ontologies.models import StreamTimeSeriesPointsRequest` |
**Ontologies** | [StreamTimeSeriesValuesRequest](docs/v2/Ontologies/models/StreamTimeSeriesValuesRequest.md) | `from foundry_sdk.v2.ontologies.models import StreamTimeSeriesValuesRequest` |
**Ontologies** | [StringConstant](docs/v2/Ontologies/models/StringConstant.md) | `from foundry_sdk.v2.ontologies.models import StringConstant` |
**Ontologies** | [StringLengthConstraint](docs/v2/Ontologies/models/StringLengthConstraint.md) | `from foundry_sdk.v2.ontologies.models import StringLengthConstraint` |
**Ontologies** | [StringRegexMatchConstraint](docs/v2/Ontologies/models/StringRegexMatchConstraint.md) | `from foundry_sdk.v2.ontologies.models import StringRegexMatchConstraint` |
**Ontologies** | [StringValue](docs/v2/Ontologies/models/StringValue.md) | `from foundry_sdk.v2.ontologies.models import StringValue` |
**Ontologies** | [StructConstraint](docs/v2/Ontologies/models/StructConstraint.md) | `from foundry_sdk.v2.ontologies.models import StructConstraint` |
**Ontologies** | [StructEvaluatedConstraint](docs/v2/Ontologies/models/StructEvaluatedConstraint.md) | `from foundry_sdk.v2.ontologies.models import StructEvaluatedConstraint` |
**Ontologies** | [StructFieldApiName](docs/v2/Ontologies/models/StructFieldApiName.md) | `from foundry_sdk.v2.ontologies.models import StructFieldApiName` |
**Ontologies** | [StructFieldArgument](docs/v2/Ontologies/models/StructFieldArgument.md) | `from foundry_sdk.v2.ontologies.models import StructFieldArgument` |
**Ontologies** | [StructFieldEvaluatedConstraint](docs/v2/Ontologies/models/StructFieldEvaluatedConstraint.md) | `from foundry_sdk.v2.ontologies.models import StructFieldEvaluatedConstraint` |
**Ontologies** | [StructFieldEvaluationResult](docs/v2/Ontologies/models/StructFieldEvaluationResult.md) | `from foundry_sdk.v2.ontologies.models import StructFieldEvaluationResult` |
**Ontologies** | [StructFieldOfPropertyImplementation](docs/v2/Ontologies/models/StructFieldOfPropertyImplementation.md) | `from foundry_sdk.v2.ontologies.models import StructFieldOfPropertyImplementation` |
**Ontologies** | [StructFieldSelector](docs/v2/Ontologies/models/StructFieldSelector.md) | `from foundry_sdk.v2.ontologies.models import StructFieldSelector` |
**Ontologies** | [StructFieldType](docs/v2/Ontologies/models/StructFieldType.md) | `from foundry_sdk.v2.ontologies.models import StructFieldType` |
**Ontologies** | [StructFieldTypeRid](docs/v2/Ontologies/models/StructFieldTypeRid.md) | `from foundry_sdk.v2.ontologies.models import StructFieldTypeRid` |
**Ontologies** | [StructListParameterFieldArgument](docs/v2/Ontologies/models/StructListParameterFieldArgument.md) | `from foundry_sdk.v2.ontologies.models import StructListParameterFieldArgument` |
**Ontologies** | [StructParameterFieldApiName](docs/v2/Ontologies/models/StructParameterFieldApiName.md) | `from foundry_sdk.v2.ontologies.models import StructParameterFieldApiName` |
**Ontologies** | [StructParameterFieldArgument](docs/v2/Ontologies/models/StructParameterFieldArgument.md) | `from foundry_sdk.v2.ontologies.models import StructParameterFieldArgument` |
**Ontologies** | [StructType](docs/v2/Ontologies/models/StructType.md) | `from foundry_sdk.v2.ontologies.models import StructType` |
**Ontologies** | [StructTypeMainValue](docs/v2/Ontologies/models/StructTypeMainValue.md) | `from foundry_sdk.v2.ontologies.models import StructTypeMainValue` |
**Ontologies** | [SubmissionCriteriaEvaluation](docs/v2/Ontologies/models/SubmissionCriteriaEvaluation.md) | `from foundry_sdk.v2.ontologies.models import SubmissionCriteriaEvaluation` |
**Ontologies** | [SubscriptionClosed](docs/v2/Ontologies/models/SubscriptionClosed.md) | `from foundry_sdk.v2.ontologies.models import SubscriptionClosed` |
**Ontologies** | [SubscriptionClosureCause](docs/v2/Ontologies/models/SubscriptionClosureCause.md) | `from foundry_sdk.v2.ontologies.models import SubscriptionClosureCause` |
**Ontologies** | [SubscriptionError](docs/v2/Ontologies/models/SubscriptionError.md) | `from foundry_sdk.v2.ontologies.models import SubscriptionError` |
**Ontologies** | [SubscriptionId](docs/v2/Ontologies/models/SubscriptionId.md) | `from foundry_sdk.v2.ontologies.models import SubscriptionId` |
**Ontologies** | [SubscriptionSuccess](docs/v2/Ontologies/models/SubscriptionSuccess.md) | `from foundry_sdk.v2.ontologies.models import SubscriptionSuccess` |
**Ontologies** | [SubtractPropertyExpression](docs/v2/Ontologies/models/SubtractPropertyExpression.md) | `from foundry_sdk.v2.ontologies.models import SubtractPropertyExpression` |
**Ontologies** | [SumAggregationV2](docs/v2/Ontologies/models/SumAggregationV2.md) | `from foundry_sdk.v2.ontologies.models import SumAggregationV2` |
**Ontologies** | [SyncApplyActionResponseV2](docs/v2/Ontologies/models/SyncApplyActionResponseV2.md) | `from foundry_sdk.v2.ontologies.models import SyncApplyActionResponseV2` |
**Ontologies** | [SynchronousWebhookOutputArgument](docs/v2/Ontologies/models/SynchronousWebhookOutputArgument.md) | `from foundry_sdk.v2.ontologies.models import SynchronousWebhookOutputArgument` |
**Ontologies** | [ThreeDimensionalAggregation](docs/v2/Ontologies/models/ThreeDimensionalAggregation.md) | `from foundry_sdk.v2.ontologies.models import ThreeDimensionalAggregation` |
**Ontologies** | [TimeCodeFormat](docs/v2/Ontologies/models/TimeCodeFormat.md) | `from foundry_sdk.v2.ontologies.models import TimeCodeFormat` |
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
**Ontologies** | [TimestampValue](docs/v2/Ontologies/models/TimestampValue.md) | `from foundry_sdk.v2.ontologies.models import TimestampValue` |
**Ontologies** | [TimeUnit](docs/v2/Ontologies/models/TimeUnit.md) | `from foundry_sdk.v2.ontologies.models import TimeUnit` |
**Ontologies** | [TransactionEdit](docs/v2/Ontologies/models/TransactionEdit.md) | `from foundry_sdk.v2.ontologies.models import TransactionEdit` |
**Ontologies** | [TwoDimensionalAggregation](docs/v2/Ontologies/models/TwoDimensionalAggregation.md) | `from foundry_sdk.v2.ontologies.models import TwoDimensionalAggregation` |
**Ontologies** | [TypeClass](docs/v2/Ontologies/models/TypeClass.md) | `from foundry_sdk.v2.ontologies.models import TypeClass` |
**Ontologies** | [UnevaluableConstraint](docs/v2/Ontologies/models/UnevaluableConstraint.md) | `from foundry_sdk.v2.ontologies.models import UnevaluableConstraint` |
**Ontologies** | [UniqueIdentifierArgument](docs/v2/Ontologies/models/UniqueIdentifierArgument.md) | `from foundry_sdk.v2.ontologies.models import UniqueIdentifierArgument` |
**Ontologies** | [UniqueIdentifierLinkId](docs/v2/Ontologies/models/UniqueIdentifierLinkId.md) | `from foundry_sdk.v2.ontologies.models import UniqueIdentifierLinkId` |
**Ontologies** | [UniqueIdentifierValue](docs/v2/Ontologies/models/UniqueIdentifierValue.md) | `from foundry_sdk.v2.ontologies.models import UniqueIdentifierValue` |
**Ontologies** | [UnsupportedPolicy](docs/v2/Ontologies/models/UnsupportedPolicy.md) | `from foundry_sdk.v2.ontologies.models import UnsupportedPolicy` |
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
**Ontologies** | [WildcardQuery](docs/v2/Ontologies/models/WildcardQuery.md) | `from foundry_sdk.v2.ontologies.models import WildcardQuery` |
**Ontologies** | [WithinBoundingBoxPoint](docs/v2/Ontologies/models/WithinBoundingBoxPoint.md) | `from foundry_sdk.v2.ontologies.models import WithinBoundingBoxPoint` |
**Ontologies** | [WithinBoundingBoxQuery](docs/v2/Ontologies/models/WithinBoundingBoxQuery.md) | `from foundry_sdk.v2.ontologies.models import WithinBoundingBoxQuery` |
**Ontologies** | [WithinDistanceOfQuery](docs/v2/Ontologies/models/WithinDistanceOfQuery.md) | `from foundry_sdk.v2.ontologies.models import WithinDistanceOfQuery` |
**Ontologies** | [WithinPolygonQuery](docs/v2/Ontologies/models/WithinPolygonQuery.md) | `from foundry_sdk.v2.ontologies.models import WithinPolygonQuery` |
**Orchestration** | [AbortOnFailure](docs/v2/Orchestration/models/AbortOnFailure.md) | `from foundry_sdk.v2.orchestration.models import AbortOnFailure` |
**Orchestration** | [Action](docs/v2/Orchestration/models/Action.md) | `from foundry_sdk.v2.orchestration.models import Action` |
**Orchestration** | [AffectedResourcesResponse](docs/v2/Orchestration/models/AffectedResourcesResponse.md) | `from foundry_sdk.v2.orchestration.models import AffectedResourcesResponse` |
**Orchestration** | [AndTrigger](docs/v2/Orchestration/models/AndTrigger.md) | `from foundry_sdk.v2.orchestration.models import AndTrigger` |
**Orchestration** | [Build](docs/v2/Orchestration/models/Build.md) | `from foundry_sdk.v2.orchestration.models import Build` |
**Orchestration** | [BuildableRid](docs/v2/Orchestration/models/BuildableRid.md) | `from foundry_sdk.v2.orchestration.models import BuildableRid` |
**Orchestration** | [BuildStatus](docs/v2/Orchestration/models/BuildStatus.md) | `from foundry_sdk.v2.orchestration.models import BuildStatus` |
**Orchestration** | [BuildTarget](docs/v2/Orchestration/models/BuildTarget.md) | `from foundry_sdk.v2.orchestration.models import BuildTarget` |
**Orchestration** | [ConnectingTarget](docs/v2/Orchestration/models/ConnectingTarget.md) | `from foundry_sdk.v2.orchestration.models import ConnectingTarget` |
**Orchestration** | [CreateBuildRequest](docs/v2/Orchestration/models/CreateBuildRequest.md) | `from foundry_sdk.v2.orchestration.models import CreateBuildRequest` |
**Orchestration** | [CreateScheduleRequest](docs/v2/Orchestration/models/CreateScheduleRequest.md) | `from foundry_sdk.v2.orchestration.models import CreateScheduleRequest` |
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
**Orchestration** | [ReplaceScheduleRequest](docs/v2/Orchestration/models/ReplaceScheduleRequest.md) | `from foundry_sdk.v2.orchestration.models import ReplaceScheduleRequest` |
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
**Orchestration** | [SearchBuildsRequest](docs/v2/Orchestration/models/SearchBuildsRequest.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsRequest` |
**Orchestration** | [SearchBuildsResponse](docs/v2/Orchestration/models/SearchBuildsResponse.md) | `from foundry_sdk.v2.orchestration.models import SearchBuildsResponse` |
**Orchestration** | [TableUpdatedTrigger](docs/v2/Orchestration/models/TableUpdatedTrigger.md) | `from foundry_sdk.v2.orchestration.models import TableUpdatedTrigger` |
**Orchestration** | [TimeTrigger](docs/v2/Orchestration/models/TimeTrigger.md) | `from foundry_sdk.v2.orchestration.models import TimeTrigger` |
**Orchestration** | [TransactionalMediaSetJobOutput](docs/v2/Orchestration/models/TransactionalMediaSetJobOutput.md) | `from foundry_sdk.v2.orchestration.models import TransactionalMediaSetJobOutput` |
**Orchestration** | [Trigger](docs/v2/Orchestration/models/Trigger.md) | `from foundry_sdk.v2.orchestration.models import Trigger` |
**Orchestration** | [UpstreamTarget](docs/v2/Orchestration/models/UpstreamTarget.md) | `from foundry_sdk.v2.orchestration.models import UpstreamTarget` |
**Orchestration** | [UserScope](docs/v2/Orchestration/models/UserScope.md) | `from foundry_sdk.v2.orchestration.models import UserScope` |
**SqlQueries** | [AnyColumnType](docs/v2/SqlQueries/models/AnyColumnType.md) | `from foundry_sdk.v2.sql_queries.models import AnyColumnType` |
**SqlQueries** | [CanceledQueryStatus](docs/v2/SqlQueries/models/CanceledQueryStatus.md) | `from foundry_sdk.v2.sql_queries.models import CanceledQueryStatus` |
**SqlQueries** | [ColumnType](docs/v2/SqlQueries/models/ColumnType.md) | `from foundry_sdk.v2.sql_queries.models import ColumnType` |
**SqlQueries** | [DecimalColumnType](docs/v2/SqlQueries/models/DecimalColumnType.md) | `from foundry_sdk.v2.sql_queries.models import DecimalColumnType` |
**SqlQueries** | [ExecuteOntologySqlQueryRequest](docs/v2/SqlQueries/models/ExecuteOntologySqlQueryRequest.md) | `from foundry_sdk.v2.sql_queries.models import ExecuteOntologySqlQueryRequest` |
**SqlQueries** | [ExecuteSqlQueryRequest](docs/v2/SqlQueries/models/ExecuteSqlQueryRequest.md) | `from foundry_sdk.v2.sql_queries.models import ExecuteSqlQueryRequest` |
**SqlQueries** | [FailedQueryStatus](docs/v2/SqlQueries/models/FailedQueryStatus.md) | `from foundry_sdk.v2.sql_queries.models import FailedQueryStatus` |
**SqlQueries** | [ListColumnType](docs/v2/SqlQueries/models/ListColumnType.md) | `from foundry_sdk.v2.sql_queries.models import ListColumnType` |
**SqlQueries** | [MapColumnType](docs/v2/SqlQueries/models/MapColumnType.md) | `from foundry_sdk.v2.sql_queries.models import MapColumnType` |
**SqlQueries** | [MapParameterKey](docs/v2/SqlQueries/models/MapParameterKey.md) | `from foundry_sdk.v2.sql_queries.models import MapParameterKey` |
**SqlQueries** | [NamedParameterMapping](docs/v2/SqlQueries/models/NamedParameterMapping.md) | `from foundry_sdk.v2.sql_queries.models import NamedParameterMapping` |
**SqlQueries** | [ParameterAnyValue](docs/v2/SqlQueries/models/ParameterAnyValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterAnyValue` |
**SqlQueries** | [ParameterBooleanValue](docs/v2/SqlQueries/models/ParameterBooleanValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterBooleanValue` |
**SqlQueries** | [ParameterDateValue](docs/v2/SqlQueries/models/ParameterDateValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterDateValue` |
**SqlQueries** | [ParameterDecimalValue](docs/v2/SqlQueries/models/ParameterDecimalValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterDecimalValue` |
**SqlQueries** | [ParameterDoubleValue](docs/v2/SqlQueries/models/ParameterDoubleValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterDoubleValue` |
**SqlQueries** | [ParameterFloatValue](docs/v2/SqlQueries/models/ParameterFloatValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterFloatValue` |
**SqlQueries** | [ParameterIntegerValue](docs/v2/SqlQueries/models/ParameterIntegerValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterIntegerValue` |
**SqlQueries** | [ParameterListValue](docs/v2/SqlQueries/models/ParameterListValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterListValue` |
**SqlQueries** | [ParameterLongValue](docs/v2/SqlQueries/models/ParameterLongValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterLongValue` |
**SqlQueries** | [ParameterMapping](docs/v2/SqlQueries/models/ParameterMapping.md) | `from foundry_sdk.v2.sql_queries.models import ParameterMapping` |
**SqlQueries** | [ParameterMapValue](docs/v2/SqlQueries/models/ParameterMapValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterMapValue` |
**SqlQueries** | [ParameterName](docs/v2/SqlQueries/models/ParameterName.md) | `from foundry_sdk.v2.sql_queries.models import ParameterName` |
**SqlQueries** | [ParameterNullValue](docs/v2/SqlQueries/models/ParameterNullValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterNullValue` |
**SqlQueries** | [Parameters](docs/v2/SqlQueries/models/Parameters.md) | `from foundry_sdk.v2.sql_queries.models import Parameters` |
**SqlQueries** | [ParameterShortValue](docs/v2/SqlQueries/models/ParameterShortValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterShortValue` |
**SqlQueries** | [ParameterStringValue](docs/v2/SqlQueries/models/ParameterStringValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterStringValue` |
**SqlQueries** | [ParameterStructValue](docs/v2/SqlQueries/models/ParameterStructValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterStructValue` |
**SqlQueries** | [ParameterTimestampValue](docs/v2/SqlQueries/models/ParameterTimestampValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterTimestampValue` |
**SqlQueries** | [ParameterValue](docs/v2/SqlQueries/models/ParameterValue.md) | `from foundry_sdk.v2.sql_queries.models import ParameterValue` |
**SqlQueries** | [QueryStatus](docs/v2/SqlQueries/models/QueryStatus.md) | `from foundry_sdk.v2.sql_queries.models import QueryStatus` |
**SqlQueries** | [RunningQueryStatus](docs/v2/SqlQueries/models/RunningQueryStatus.md) | `from foundry_sdk.v2.sql_queries.models import RunningQueryStatus` |
**SqlQueries** | [SqlQueryId](docs/v2/SqlQueries/models/SqlQueryId.md) | `from foundry_sdk.v2.sql_queries.models import SqlQueryId` |
**SqlQueries** | [StructColumnFieldType](docs/v2/SqlQueries/models/StructColumnFieldType.md) | `from foundry_sdk.v2.sql_queries.models import StructColumnFieldType` |
**SqlQueries** | [StructColumnType](docs/v2/SqlQueries/models/StructColumnType.md) | `from foundry_sdk.v2.sql_queries.models import StructColumnType` |
**SqlQueries** | [StructElement](docs/v2/SqlQueries/models/StructElement.md) | `from foundry_sdk.v2.sql_queries.models import StructElement` |
**SqlQueries** | [StructElementName](docs/v2/SqlQueries/models/StructElementName.md) | `from foundry_sdk.v2.sql_queries.models import StructElementName` |
**SqlQueries** | [StructFieldKeyValue](docs/v2/SqlQueries/models/StructFieldKeyValue.md) | `from foundry_sdk.v2.sql_queries.models import StructFieldKeyValue` |
**SqlQueries** | [StructFieldRid](docs/v2/SqlQueries/models/StructFieldRid.md) | `from foundry_sdk.v2.sql_queries.models import StructFieldRid` |
**SqlQueries** | [SucceededQueryStatus](docs/v2/SqlQueries/models/SucceededQueryStatus.md) | `from foundry_sdk.v2.sql_queries.models import SucceededQueryStatus` |
**SqlQueries** | [UnnamedParameterValues](docs/v2/SqlQueries/models/UnnamedParameterValues.md) | `from foundry_sdk.v2.sql_queries.models import UnnamedParameterValues` |
**Streams** | [CommitSubscriberOffsetsRequest](docs/v2/Streams/models/CommitSubscriberOffsetsRequest.md) | `from foundry_sdk.v2.streams.models import CommitSubscriberOffsetsRequest` |
**Streams** | [Compressed](docs/v2/Streams/models/Compressed.md) | `from foundry_sdk.v2.streams.models import Compressed` |
**Streams** | [CreateStreamingDatasetRequest](docs/v2/Streams/models/CreateStreamingDatasetRequest.md) | `from foundry_sdk.v2.streams.models import CreateStreamingDatasetRequest` |
**Streams** | [CreateStreamRequest](docs/v2/Streams/models/CreateStreamRequest.md) | `from foundry_sdk.v2.streams.models import CreateStreamRequest` |
**Streams** | [CreateStreamRequestStreamSchema](docs/v2/Streams/models/CreateStreamRequestStreamSchema.md) | `from foundry_sdk.v2.streams.models import CreateStreamRequestStreamSchema` |
**Streams** | [CreateSubscriberRequest](docs/v2/Streams/models/CreateSubscriberRequest.md) | `from foundry_sdk.v2.streams.models import CreateSubscriberRequest` |
**Streams** | [Dataset](docs/v2/Streams/models/Dataset.md) | `from foundry_sdk.v2.streams.models import Dataset` |
**Streams** | [EarliestPosition](docs/v2/Streams/models/EarliestPosition.md) | `from foundry_sdk.v2.streams.models import EarliestPosition` |
**Streams** | [GetEndOffsetsResponse](docs/v2/Streams/models/GetEndOffsetsResponse.md) | `from foundry_sdk.v2.streams.models import GetEndOffsetsResponse` |
**Streams** | [GetRecordsResponse](docs/v2/Streams/models/GetRecordsResponse.md) | `from foundry_sdk.v2.streams.models import GetRecordsResponse` |
**Streams** | [LatestPosition](docs/v2/Streams/models/LatestPosition.md) | `from foundry_sdk.v2.streams.models import LatestPosition` |
**Streams** | [PartitionId](docs/v2/Streams/models/PartitionId.md) | `from foundry_sdk.v2.streams.models import PartitionId` |
**Streams** | [PartitionOffsets](docs/v2/Streams/models/PartitionOffsets.md) | `from foundry_sdk.v2.streams.models import PartitionOffsets` |
**Streams** | [PartitionRecords](docs/v2/Streams/models/PartitionRecords.md) | `from foundry_sdk.v2.streams.models import PartitionRecords` |
**Streams** | [PartitionsCount](docs/v2/Streams/models/PartitionsCount.md) | `from foundry_sdk.v2.streams.models import PartitionsCount` |
**Streams** | [PublishRecordsToStreamRequest](docs/v2/Streams/models/PublishRecordsToStreamRequest.md) | `from foundry_sdk.v2.streams.models import PublishRecordsToStreamRequest` |
**Streams** | [PublishRecordToStreamRequest](docs/v2/Streams/models/PublishRecordToStreamRequest.md) | `from foundry_sdk.v2.streams.models import PublishRecordToStreamRequest` |
**Streams** | [ReadPosition](docs/v2/Streams/models/ReadPosition.md) | `from foundry_sdk.v2.streams.models import ReadPosition` |
**Streams** | [ReadRecordsFromSubscriberRequest](docs/v2/Streams/models/ReadRecordsFromSubscriberRequest.md) | `from foundry_sdk.v2.streams.models import ReadRecordsFromSubscriberRequest` |
**Streams** | [ReadSubscriberRecordsResponse](docs/v2/Streams/models/ReadSubscriberRecordsResponse.md) | `from foundry_sdk.v2.streams.models import ReadSubscriberRecordsResponse` |
**Streams** | [Record](docs/v2/Streams/models/Record.md) | `from foundry_sdk.v2.streams.models import Record` |
**Streams** | [RecordWithOffset](docs/v2/Streams/models/RecordWithOffset.md) | `from foundry_sdk.v2.streams.models import RecordWithOffset` |
**Streams** | [ResetStreamRequest](docs/v2/Streams/models/ResetStreamRequest.md) | `from foundry_sdk.v2.streams.models import ResetStreamRequest` |
**Streams** | [ResetSubscriberOffsetsRequest](docs/v2/Streams/models/ResetSubscriberOffsetsRequest.md) | `from foundry_sdk.v2.streams.models import ResetSubscriberOffsetsRequest` |
**Streams** | [SpecificPosition](docs/v2/Streams/models/SpecificPosition.md) | `from foundry_sdk.v2.streams.models import SpecificPosition` |
**Streams** | [Stream](docs/v2/Streams/models/Stream.md) | `from foundry_sdk.v2.streams.models import Stream` |
**Streams** | [StreamType](docs/v2/Streams/models/StreamType.md) | `from foundry_sdk.v2.streams.models import StreamType` |
**Streams** | [Subscriber](docs/v2/Streams/models/Subscriber.md) | `from foundry_sdk.v2.streams.models import Subscriber` |
**Streams** | [SubscriberId](docs/v2/Streams/models/SubscriberId.md) | `from foundry_sdk.v2.streams.models import SubscriberId` |
**Streams** | [ViewRid](docs/v2/Streams/models/ViewRid.md) | `from foundry_sdk.v2.streams.models import ViewRid` |
**ThirdPartyApplications** | [DeployWebsiteRequest](docs/v2/ThirdPartyApplications/models/DeployWebsiteRequest.md) | `from foundry_sdk.v2.third_party_applications.models import DeployWebsiteRequest` |
**ThirdPartyApplications** | [ListVersionsResponse](docs/v2/ThirdPartyApplications/models/ListVersionsResponse.md) | `from foundry_sdk.v2.third_party_applications.models import ListVersionsResponse` |
**ThirdPartyApplications** | [Subdomain](docs/v2/ThirdPartyApplications/models/Subdomain.md) | `from foundry_sdk.v2.third_party_applications.models import Subdomain` |
**ThirdPartyApplications** | [ThirdPartyApplication](docs/v2/ThirdPartyApplications/models/ThirdPartyApplication.md) | `from foundry_sdk.v2.third_party_applications.models import ThirdPartyApplication` |
**ThirdPartyApplications** | [ThirdPartyApplicationRid](docs/v2/ThirdPartyApplications/models/ThirdPartyApplicationRid.md) | `from foundry_sdk.v2.third_party_applications.models import ThirdPartyApplicationRid` |
**ThirdPartyApplications** | [Version](docs/v2/ThirdPartyApplications/models/Version.md) | `from foundry_sdk.v2.third_party_applications.models import Version` |
**ThirdPartyApplications** | [VersionVersion](docs/v2/ThirdPartyApplications/models/VersionVersion.md) | `from foundry_sdk.v2.third_party_applications.models import VersionVersion` |
**ThirdPartyApplications** | [Website](docs/v2/ThirdPartyApplications/models/Website.md) | `from foundry_sdk.v2.third_party_applications.models import Website` |
**Widgets** | [DevModeSettings](docs/v2/Widgets/models/DevModeSettings.md) | `from foundry_sdk.v2.widgets.models import DevModeSettings` |
**Widgets** | [DevModeStatus](docs/v2/Widgets/models/DevModeStatus.md) | `from foundry_sdk.v2.widgets.models import DevModeStatus` |
**Widgets** | [FilePath](docs/v2/Widgets/models/FilePath.md) | `from foundry_sdk.v2.widgets.models import FilePath` |
**Widgets** | [ListReleasesResponse](docs/v2/Widgets/models/ListReleasesResponse.md) | `from foundry_sdk.v2.widgets.models import ListReleasesResponse` |
**Widgets** | [Release](docs/v2/Widgets/models/Release.md) | `from foundry_sdk.v2.widgets.models import Release` |
**Widgets** | [ReleaseLocator](docs/v2/Widgets/models/ReleaseLocator.md) | `from foundry_sdk.v2.widgets.models import ReleaseLocator` |
**Widgets** | [ReleaseVersion](docs/v2/Widgets/models/ReleaseVersion.md) | `from foundry_sdk.v2.widgets.models import ReleaseVersion` |
**Widgets** | [Repository](docs/v2/Widgets/models/Repository.md) | `from foundry_sdk.v2.widgets.models import Repository` |
**Widgets** | [RepositoryRid](docs/v2/Widgets/models/RepositoryRid.md) | `from foundry_sdk.v2.widgets.models import RepositoryRid` |
**Widgets** | [RepositoryVersion](docs/v2/Widgets/models/RepositoryVersion.md) | `from foundry_sdk.v2.widgets.models import RepositoryVersion` |
**Widgets** | [ScriptEntrypoint](docs/v2/Widgets/models/ScriptEntrypoint.md) | `from foundry_sdk.v2.widgets.models import ScriptEntrypoint` |
**Widgets** | [ScriptType](docs/v2/Widgets/models/ScriptType.md) | `from foundry_sdk.v2.widgets.models import ScriptType` |
**Widgets** | [SetWidgetSetDevModeSettingsByIdRequest](docs/v2/Widgets/models/SetWidgetSetDevModeSettingsByIdRequest.md) | `from foundry_sdk.v2.widgets.models import SetWidgetSetDevModeSettingsByIdRequest` |
**Widgets** | [SetWidgetSetDevModeSettingsRequest](docs/v2/Widgets/models/SetWidgetSetDevModeSettingsRequest.md) | `from foundry_sdk.v2.widgets.models import SetWidgetSetDevModeSettingsRequest` |
**Widgets** | [StylesheetEntrypoint](docs/v2/Widgets/models/StylesheetEntrypoint.md) | `from foundry_sdk.v2.widgets.models import StylesheetEntrypoint` |
**Widgets** | [WidgetDevModeSettings](docs/v2/Widgets/models/WidgetDevModeSettings.md) | `from foundry_sdk.v2.widgets.models import WidgetDevModeSettings` |
**Widgets** | [WidgetId](docs/v2/Widgets/models/WidgetId.md) | `from foundry_sdk.v2.widgets.models import WidgetId` |
**Widgets** | [WidgetRid](docs/v2/Widgets/models/WidgetRid.md) | `from foundry_sdk.v2.widgets.models import WidgetRid` |
**Widgets** | [WidgetSet](docs/v2/Widgets/models/WidgetSet.md) | `from foundry_sdk.v2.widgets.models import WidgetSet` |
**Widgets** | [WidgetSetDevModeSettings](docs/v2/Widgets/models/WidgetSetDevModeSettings.md) | `from foundry_sdk.v2.widgets.models import WidgetSetDevModeSettings` |
**Widgets** | [WidgetSetDevModeSettingsById](docs/v2/Widgets/models/WidgetSetDevModeSettingsById.md) | `from foundry_sdk.v2.widgets.models import WidgetSetDevModeSettingsById` |
**Widgets** | [WidgetSetRid](docs/v2/Widgets/models/WidgetSetRid.md) | `from foundry_sdk.v2.widgets.models import WidgetSetRid` |

<a id="models-v1-link"></a>
## Documentation for V1 models

Namespace | Name | Import |
--------- | ---- | ------ |
**Core** | [AnyType](docs/v1/Core/models/AnyType.md) | `from foundry_sdk.v1.core.models import AnyType` |
**Core** | [AttachmentType](docs/v1/Core/models/AttachmentType.md) | `from foundry_sdk.v1.core.models import AttachmentType` |
**Core** | [Attribution](docs/v1/Core/models/Attribution.md) | `from foundry_sdk.v1.core.models import Attribution` |
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
**Core** | [MediaReferenceType](docs/v1/Core/models/MediaReferenceType.md) | `from foundry_sdk.v1.core.models import MediaReferenceType` |
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
**Core** | [UnsupportedTypeParamKey](docs/v1/Core/models/UnsupportedTypeParamKey.md) | `from foundry_sdk.v1.core.models import UnsupportedTypeParamKey` |
**Core** | [UnsupportedTypeParamValue](docs/v1/Core/models/UnsupportedTypeParamValue.md) | `from foundry_sdk.v1.core.models import UnsupportedTypeParamValue` |
**Core** | [VoidType](docs/v1/Core/models/VoidType.md) | `from foundry_sdk.v1.core.models import VoidType` |
**Datasets** | [Branch](docs/v1/Datasets/models/Branch.md) | `from foundry_sdk.v1.datasets.models import Branch` |
**Datasets** | [BranchId](docs/v1/Datasets/models/BranchId.md) | `from foundry_sdk.v1.datasets.models import BranchId` |
**Datasets** | [CreateBranchRequest](docs/v1/Datasets/models/CreateBranchRequest.md) | `from foundry_sdk.v1.datasets.models import CreateBranchRequest` |
**Datasets** | [CreateDatasetRequest](docs/v1/Datasets/models/CreateDatasetRequest.md) | `from foundry_sdk.v1.datasets.models import CreateDatasetRequest` |
**Datasets** | [CreateTransactionRequest](docs/v1/Datasets/models/CreateTransactionRequest.md) | `from foundry_sdk.v1.datasets.models import CreateTransactionRequest` |
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
**Ontologies** | [AggregateObjectsRequest](docs/v1/Ontologies/models/AggregateObjectsRequest.md) | `from foundry_sdk.v1.ontologies.models import AggregateObjectsRequest` |
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
**Ontologies** | [BatchApplyActionRequest](docs/v1/Ontologies/models/BatchApplyActionRequest.md) | `from foundry_sdk.v1.ontologies.models import BatchApplyActionRequest` |
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
**Ontologies** | [ExecuteQueryRequest](docs/v1/Ontologies/models/ExecuteQueryRequest.md) | `from foundry_sdk.v1.ontologies.models import ExecuteQueryRequest` |
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
**Ontologies** | [InterfacePropertyApiName](docs/v1/Ontologies/models/InterfacePropertyApiName.md) | `from foundry_sdk.v1.ontologies.models import InterfacePropertyApiName` |
**Ontologies** | [InterfaceTypeApiName](docs/v1/Ontologies/models/InterfaceTypeApiName.md) | `from foundry_sdk.v1.ontologies.models import InterfaceTypeApiName` |
**Ontologies** | [InterfaceTypeRid](docs/v1/Ontologies/models/InterfaceTypeRid.md) | `from foundry_sdk.v1.ontologies.models import InterfaceTypeRid` |
**Ontologies** | [IsNullQuery](docs/v1/Ontologies/models/IsNullQuery.md) | `from foundry_sdk.v1.ontologies.models import IsNullQuery` |
**Ontologies** | [LegacyObjectTypeId](docs/v1/Ontologies/models/LegacyObjectTypeId.md) | `from foundry_sdk.v1.ontologies.models import LegacyObjectTypeId` |
**Ontologies** | [LegacyPropertyId](docs/v1/Ontologies/models/LegacyPropertyId.md) | `from foundry_sdk.v1.ontologies.models import LegacyPropertyId` |
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
**Ontologies** | [SearchObjectsRequest](docs/v1/Ontologies/models/SearchObjectsRequest.md) | `from foundry_sdk.v1.ontologies.models import SearchObjectsRequest` |
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
**Ontologies** | [UniqueIdentifierLinkId](docs/v1/Ontologies/models/UniqueIdentifierLinkId.md) | `from foundry_sdk.v1.ontologies.models import UniqueIdentifierLinkId` |
**Ontologies** | [ValidateActionRequest](docs/v1/Ontologies/models/ValidateActionRequest.md) | `from foundry_sdk.v1.ontologies.models import ValidateActionRequest` |
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
**Admin** | CreateMarkingCategoryMissingInitialAdminRole | `from foundry_sdk.v2.admin.errors import CreateMarkingCategoryMissingInitialAdminRole` |
**Admin** | CreateMarkingCategoryMissingOrganization | `from foundry_sdk.v2.admin.errors import CreateMarkingCategoryMissingOrganization` |
**Admin** | CreateMarkingCategoryPermissionDenied | `from foundry_sdk.v2.admin.errors import CreateMarkingCategoryPermissionDenied` |
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
**Admin** | ProfileServiceNotPresent | `from foundry_sdk.v2.admin.errors import ProfileServiceNotPresent` |
**Admin** | RemoveEnrollmentRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import RemoveEnrollmentRoleAssignmentsPermissionDenied` |
**Admin** | RemoveGroupMembersPermissionDenied | `from foundry_sdk.v2.admin.errors import RemoveGroupMembersPermissionDenied` |
**Admin** | RemoveMarkingMembersPermissionDenied | `from foundry_sdk.v2.admin.errors import RemoveMarkingMembersPermissionDenied` |
**Admin** | RemoveMarkingRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import RemoveMarkingRoleAssignmentsPermissionDenied` |
**Admin** | RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed | `from foundry_sdk.v2.admin.errors import RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed` |
**Admin** | RemoveOrganizationRoleAssignmentsPermissionDenied | `from foundry_sdk.v2.admin.errors import RemoveOrganizationRoleAssignmentsPermissionDenied` |
**Admin** | ReplaceGroupMembershipExpirationPolicyPermissionDenied | `from foundry_sdk.v2.admin.errors import ReplaceGroupMembershipExpirationPolicyPermissionDenied` |
**Admin** | ReplaceGroupProviderInfoPermissionDenied | `from foundry_sdk.v2.admin.errors import ReplaceGroupProviderInfoPermissionDenied` |
**Admin** | ReplaceMarkingCategoryPermissionDenied | `from foundry_sdk.v2.admin.errors import ReplaceMarkingCategoryPermissionDenied` |
**Admin** | ReplaceMarkingPermissionDenied | `from foundry_sdk.v2.admin.errors import ReplaceMarkingPermissionDenied` |
**Admin** | ReplaceOrganizationPermissionDenied | `from foundry_sdk.v2.admin.errors import ReplaceOrganizationPermissionDenied` |
**Admin** | ReplaceUserProviderInfoPermissionDenied | `from foundry_sdk.v2.admin.errors import ReplaceUserProviderInfoPermissionDenied` |
**Admin** | RevokeAllTokensUserPermissionDenied | `from foundry_sdk.v2.admin.errors import RevokeAllTokensUserPermissionDenied` |
**Admin** | RoleNotFound | `from foundry_sdk.v2.admin.errors import RoleNotFound` |
**Admin** | SearchGroupsPermissionDenied | `from foundry_sdk.v2.admin.errors import SearchGroupsPermissionDenied` |
**Admin** | SearchUsersPermissionDenied | `from foundry_sdk.v2.admin.errors import SearchUsersPermissionDenied` |
**Admin** | UserDeleted | `from foundry_sdk.v2.admin.errors import UserDeleted` |
**Admin** | UserIsActive | `from foundry_sdk.v2.admin.errors import UserIsActive` |
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
**AipAgents** | DeleteSessionPermissionDenied | `from foundry_sdk.v2.aip_agents.errors import DeleteSessionPermissionDenied` |
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
**AipAgents** | RetryAttemptsExceeded | `from foundry_sdk.v2.aip_agents.errors import RetryAttemptsExceeded` |
**AipAgents** | RetryDeadlineExceeded | `from foundry_sdk.v2.aip_agents.errors import RetryDeadlineExceeded` |
**AipAgents** | SessionExecutionFailed | `from foundry_sdk.v2.aip_agents.errors import SessionExecutionFailed` |
**AipAgents** | SessionNotFound | `from foundry_sdk.v2.aip_agents.errors import SessionNotFound` |
**AipAgents** | SessionTraceIdAlreadyExists | `from foundry_sdk.v2.aip_agents.errors import SessionTraceIdAlreadyExists` |
**AipAgents** | SessionTraceNotFound | `from foundry_sdk.v2.aip_agents.errors import SessionTraceNotFound` |
**AipAgents** | StreamingContinueSessionPermissionDenied | `from foundry_sdk.v2.aip_agents.errors import StreamingContinueSessionPermissionDenied` |
**AipAgents** | UpdateSessionTitlePermissionDenied | `from foundry_sdk.v2.aip_agents.errors import UpdateSessionTitlePermissionDenied` |
**Audit** | GetLogFileContentPermissionDenied | `from foundry_sdk.v2.audit.errors import GetLogFileContentPermissionDenied` |
**Audit** | ListLogFilesPermissionDenied | `from foundry_sdk.v2.audit.errors import ListLogFilesPermissionDenied` |
**Audit** | MissingStartDate | `from foundry_sdk.v2.audit.errors import MissingStartDate` |
**Checkpoints** | CheckpointRecordNotFound | `from foundry_sdk.v2.checkpoints.errors import CheckpointRecordNotFound` |
**Checkpoints** | CheckpointRecordPermissionDenied | `from foundry_sdk.v2.checkpoints.errors import CheckpointRecordPermissionDenied` |
**Checkpoints** | RecordNotFound | `from foundry_sdk.v2.checkpoints.errors import RecordNotFound` |
**Checkpoints** | SearchRecordsPermissionDenied | `from foundry_sdk.v2.checkpoints.errors import SearchRecordsPermissionDenied` |
**Connectivity** | AdditionalSecretsMustBeSpecifiedAsPlaintextValueMap | `from foundry_sdk.v2.connectivity.errors import AdditionalSecretsMustBeSpecifiedAsPlaintextValueMap` |
**Connectivity** | ConnectionDetailsNotDetermined | `from foundry_sdk.v2.connectivity.errors import ConnectionDetailsNotDetermined` |
**Connectivity** | ConnectionNotFound | `from foundry_sdk.v2.connectivity.errors import ConnectionNotFound` |
**Connectivity** | ConnectionTypeNotSupported | `from foundry_sdk.v2.connectivity.errors import ConnectionTypeNotSupported` |
**Connectivity** | CreateConnectionPermissionDenied | `from foundry_sdk.v2.connectivity.errors import CreateConnectionPermissionDenied` |
**Connectivity** | CreateFileImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import CreateFileImportPermissionDenied` |
**Connectivity** | CreateTableImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import CreateTableImportPermissionDenied` |
**Connectivity** | CreateVirtualTablePermissionDenied | `from foundry_sdk.v2.connectivity.errors import CreateVirtualTablePermissionDenied` |
**Connectivity** | DeleteFileImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import DeleteFileImportPermissionDenied` |
**Connectivity** | DeleteTableImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import DeleteTableImportPermissionDenied` |
**Connectivity** | DomainMustUseHttpsWithAuthentication | `from foundry_sdk.v2.connectivity.errors import DomainMustUseHttpsWithAuthentication` |
**Connectivity** | DriverContentMustBeUploadedAsJar | `from foundry_sdk.v2.connectivity.errors import DriverContentMustBeUploadedAsJar` |
**Connectivity** | DriverJarAlreadyExists | `from foundry_sdk.v2.connectivity.errors import DriverJarAlreadyExists` |
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
**Connectivity** | InvalidShareName | `from foundry_sdk.v2.connectivity.errors import InvalidShareName` |
**Connectivity** | InvalidVirtualTableConnection | `from foundry_sdk.v2.connectivity.errors import InvalidVirtualTableConnection` |
**Connectivity** | ParentFolderNotFoundForConnection | `from foundry_sdk.v2.connectivity.errors import ParentFolderNotFoundForConnection` |
**Connectivity** | PortNotInRange | `from foundry_sdk.v2.connectivity.errors import PortNotInRange` |
**Connectivity** | PropertyCannotBeBlank | `from foundry_sdk.v2.connectivity.errors import PropertyCannotBeBlank` |
**Connectivity** | PropertyCannotBeEmpty | `from foundry_sdk.v2.connectivity.errors import PropertyCannotBeEmpty` |
**Connectivity** | ReplaceFileImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import ReplaceFileImportPermissionDenied` |
**Connectivity** | ReplaceTableImportPermissionDenied | `from foundry_sdk.v2.connectivity.errors import ReplaceTableImportPermissionDenied` |
**Connectivity** | SecretNamesDoNotExist | `from foundry_sdk.v2.connectivity.errors import SecretNamesDoNotExist` |
**Connectivity** | TableImportNotFound | `from foundry_sdk.v2.connectivity.errors import TableImportNotFound` |
**Connectivity** | TableImportNotSupportedForConnection | `from foundry_sdk.v2.connectivity.errors import TableImportNotSupportedForConnection` |
**Connectivity** | TableImportTypeNotSupported | `from foundry_sdk.v2.connectivity.errors import TableImportTypeNotSupported` |
**Connectivity** | UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnections | `from foundry_sdk.v2.connectivity.errors import UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnections` |
**Connectivity** | UpdateExportSettingsForConnectionPermissionDenied | `from foundry_sdk.v2.connectivity.errors import UpdateExportSettingsForConnectionPermissionDenied` |
**Connectivity** | UpdateSecretsForConnectionPermissionDenied | `from foundry_sdk.v2.connectivity.errors import UpdateSecretsForConnectionPermissionDenied` |
**Connectivity** | UploadCustomJdbcDriverNotSupportForConnection | `from foundry_sdk.v2.connectivity.errors import UploadCustomJdbcDriverNotSupportForConnection` |
**Connectivity** | UploadCustomJdbcDriversConnectionPermissionDenied | `from foundry_sdk.v2.connectivity.errors import UploadCustomJdbcDriversConnectionPermissionDenied` |
**Connectivity** | VirtualTableAlreadyExists | `from foundry_sdk.v2.connectivity.errors import VirtualTableAlreadyExists` |
**Connectivity** | VirtualTableRegisterFromSourcePermissionDenied | `from foundry_sdk.v2.connectivity.errors import VirtualTableRegisterFromSourcePermissionDenied` |
**Core** | ApiFeaturePreviewUsageOnly | `from foundry_sdk.v2.core.errors import ApiFeaturePreviewUsageOnly` |
**Core** | ApiUsageDenied | `from foundry_sdk.v2.core.errors import ApiUsageDenied` |
**Core** | BatchRequestSizeExceededLimit | `from foundry_sdk.v2.core.errors import BatchRequestSizeExceededLimit` |
**Core** | FolderNotFound | `from foundry_sdk.v2.core.errors import FolderNotFound` |
**Core** | FoundryBranchNotFound | `from foundry_sdk.v2.core.errors import FoundryBranchNotFound` |
**Core** | InvalidAndFilter | `from foundry_sdk.v2.core.errors import InvalidAndFilter` |
**Core** | InvalidAttributionHeader | `from foundry_sdk.v2.core.errors import InvalidAttributionHeader` |
**Core** | InvalidChangeDataCaptureConfiguration | `from foundry_sdk.v2.core.errors import InvalidChangeDataCaptureConfiguration` |
**Core** | InvalidFieldSchema | `from foundry_sdk.v2.core.errors import InvalidFieldSchema` |
**Core** | InvalidFilePath | `from foundry_sdk.v2.core.errors import InvalidFilePath` |
**Core** | InvalidFilterValue | `from foundry_sdk.v2.core.errors import InvalidFilterValue` |
**Core** | InvalidOrFilter | `from foundry_sdk.v2.core.errors import InvalidOrFilter` |
**Core** | InvalidPageSize | `from foundry_sdk.v2.core.errors import InvalidPageSize` |
**Core** | InvalidPageToken | `from foundry_sdk.v2.core.errors import InvalidPageToken` |
**Core** | InvalidParameterCombination | `from foundry_sdk.v2.core.errors import InvalidParameterCombination` |
**Core** | InvalidSchema | `from foundry_sdk.v2.core.errors import InvalidSchema` |
**Core** | InvalidTimeZone | `from foundry_sdk.v2.core.errors import InvalidTimeZone` |
**Core** | MissingBatchRequest | `from foundry_sdk.v2.core.errors import MissingBatchRequest` |
**Core** | MissingPostBody | `from foundry_sdk.v2.core.errors import MissingPostBody` |
**Core** | NotAuthorizedToDeclassifyMarkings | `from foundry_sdk.v2.core.errors import NotAuthorizedToDeclassifyMarkings` |
**Core** | ResourceNameAlreadyExists | `from foundry_sdk.v2.core.errors import ResourceNameAlreadyExists` |
**Core** | SchemaIsNotStreamSchema | `from foundry_sdk.v2.core.errors import SchemaIsNotStreamSchema` |
**Core** | UnknownDistanceUnit | `from foundry_sdk.v2.core.errors import UnknownDistanceUnit` |
**DataHealth** | CheckAlreadyExists | `from foundry_sdk.v2.data_health.errors import CheckAlreadyExists` |
**DataHealth** | CheckNotFound | `from foundry_sdk.v2.data_health.errors import CheckNotFound` |
**DataHealth** | CheckReportLimitAboveMaximum | `from foundry_sdk.v2.data_health.errors import CheckReportLimitAboveMaximum` |
**DataHealth** | CheckReportLimitBelowMinimum | `from foundry_sdk.v2.data_health.errors import CheckReportLimitBelowMinimum` |
**DataHealth** | CheckReportNotFound | `from foundry_sdk.v2.data_health.errors import CheckReportNotFound` |
**DataHealth** | CheckTypeNotSupported | `from foundry_sdk.v2.data_health.errors import CheckTypeNotSupported` |
**DataHealth** | CreateCheckPermissionDenied | `from foundry_sdk.v2.data_health.errors import CreateCheckPermissionDenied` |
**DataHealth** | DeleteCheckPermissionDenied | `from foundry_sdk.v2.data_health.errors import DeleteCheckPermissionDenied` |
**DataHealth** | GetLatestCheckReportsPermissionDenied | `from foundry_sdk.v2.data_health.errors import GetLatestCheckReportsPermissionDenied` |
**DataHealth** | InvalidNumericColumnCheckConfig | `from foundry_sdk.v2.data_health.errors import InvalidNumericColumnCheckConfig` |
**DataHealth** | InvalidPercentageCheckConfig | `from foundry_sdk.v2.data_health.errors import InvalidPercentageCheckConfig` |
**DataHealth** | InvalidTimeCheckConfig | `from foundry_sdk.v2.data_health.errors import InvalidTimeCheckConfig` |
**DataHealth** | InvalidTransactionTimeCheckConfig | `from foundry_sdk.v2.data_health.errors import InvalidTransactionTimeCheckConfig` |
**DataHealth** | InvalidTrendConfig | `from foundry_sdk.v2.data_health.errors import InvalidTrendConfig` |
**DataHealth** | ModifyingCheckTypeNotSupported | `from foundry_sdk.v2.data_health.errors import ModifyingCheckTypeNotSupported` |
**DataHealth** | PercentageValueAboveMaximum | `from foundry_sdk.v2.data_health.errors import PercentageValueAboveMaximum` |
**DataHealth** | PercentageValueBelowMinimum | `from foundry_sdk.v2.data_health.errors import PercentageValueBelowMinimum` |
**DataHealth** | ReplaceCheckPermissionDenied | `from foundry_sdk.v2.data_health.errors import ReplaceCheckPermissionDenied` |
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
**Datasets** | GetDatasetHealthCheckReportsPermissionDenied | `from foundry_sdk.v2.datasets.errors import GetDatasetHealthCheckReportsPermissionDenied` |
**Datasets** | GetDatasetHealthChecksPermissionDenied | `from foundry_sdk.v2.datasets.errors import GetDatasetHealthChecksPermissionDenied` |
**Datasets** | GetDatasetJobsPermissionDenied | `from foundry_sdk.v2.datasets.errors import GetDatasetJobsPermissionDenied` |
**Datasets** | GetDatasetSchedulesPermissionDenied | `from foundry_sdk.v2.datasets.errors import GetDatasetSchedulesPermissionDenied` |
**Datasets** | GetDatasetSchemaPermissionDenied | `from foundry_sdk.v2.datasets.errors import GetDatasetSchemaPermissionDenied` |
**Datasets** | GetFileContentPermissionDenied | `from foundry_sdk.v2.datasets.errors import GetFileContentPermissionDenied` |
**Datasets** | InputBackingDatasetNotInOutputViewProject | `from foundry_sdk.v2.datasets.errors import InputBackingDatasetNotInOutputViewProject` |
**Datasets** | InvalidBranchName | `from foundry_sdk.v2.datasets.errors import InvalidBranchName` |
**Datasets** | InvalidTransactionType | `from foundry_sdk.v2.datasets.errors import InvalidTransactionType` |
**Datasets** | InvalidViewBackingDataset | `from foundry_sdk.v2.datasets.errors import InvalidViewBackingDataset` |
**Datasets** | InvalidViewPrimaryKeyColumnType | `from foundry_sdk.v2.datasets.errors import InvalidViewPrimaryKeyColumnType` |
**Datasets** | InvalidViewPrimaryKeyDeletionColumn | `from foundry_sdk.v2.datasets.errors import InvalidViewPrimaryKeyDeletionColumn` |
**Datasets** | JobTransactionPermissionDenied | `from foundry_sdk.v2.datasets.errors import JobTransactionPermissionDenied` |
**Datasets** | NotAllColumnsInPrimaryKeyArePresent | `from foundry_sdk.v2.datasets.errors import NotAllColumnsInPrimaryKeyArePresent` |
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
**Datasets** | ViewPrimaryKeyDeletionColumnNotInDatasetSchema | `from foundry_sdk.v2.datasets.errors import ViewPrimaryKeyDeletionColumnNotInDatasetSchema` |
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
**Filesystem** | UsageAccountServiceIsNotPresent | `from foundry_sdk.v2.filesystem.errors import UsageAccountServiceIsNotPresent` |
**Functions** | ConsistentSnapshotError | `from foundry_sdk.v2.functions.errors import ConsistentSnapshotError` |
**Functions** | ExecuteQueryPermissionDenied | `from foundry_sdk.v2.functions.errors import ExecuteQueryPermissionDenied` |
**Functions** | FunctionHasNoPublishedVersion | `from foundry_sdk.v2.functions.errors import FunctionHasNoPublishedVersion` |
**Functions** | FunctionNotFound | `from foundry_sdk.v2.functions.errors import FunctionNotFound` |
**Functions** | GetByRidPermissionDenied | `from foundry_sdk.v2.functions.errors import GetByRidPermissionDenied` |
**Functions** | InvalidQueryOutputValue | `from foundry_sdk.v2.functions.errors import InvalidQueryOutputValue` |
**Functions** | InvalidQueryParameterValue | `from foundry_sdk.v2.functions.errors import InvalidQueryParameterValue` |
**Functions** | MissingParameter | `from foundry_sdk.v2.functions.errors import MissingParameter` |
**Functions** | QueryEncounteredUserFacingError | `from foundry_sdk.v2.functions.errors import QueryEncounteredUserFacingError` |
**Functions** | QueryMemoryExceededLimit | `from foundry_sdk.v2.functions.errors import QueryMemoryExceededLimit` |
**Functions** | QueryNotFound | `from foundry_sdk.v2.functions.errors import QueryNotFound` |
**Functions** | QueryRuntimeError | `from foundry_sdk.v2.functions.errors import QueryRuntimeError` |
**Functions** | QueryTimeExceededLimit | `from foundry_sdk.v2.functions.errors import QueryTimeExceededLimit` |
**Functions** | QueryVersionNotFound | `from foundry_sdk.v2.functions.errors import QueryVersionNotFound` |
**Functions** | StreamingExecuteQueryPermissionDenied | `from foundry_sdk.v2.functions.errors import StreamingExecuteQueryPermissionDenied` |
**Functions** | UnknownParameter | `from foundry_sdk.v2.functions.errors import UnknownParameter` |
**Functions** | ValueTypeNotFound | `from foundry_sdk.v2.functions.errors import ValueTypeNotFound` |
**Functions** | VersionIdNotFound | `from foundry_sdk.v2.functions.errors import VersionIdNotFound` |
**LanguageModels** | AnthropicMessagesPermissionDenied | `from foundry_sdk.v2.language_models.errors import AnthropicMessagesPermissionDenied` |
**LanguageModels** | InvalidRequest | `from foundry_sdk.v2.language_models.errors import InvalidRequest` |
**LanguageModels** | LanguageModelInferenceError | `from foundry_sdk.v2.language_models.errors import LanguageModelInferenceError` |
**LanguageModels** | LanguageModelNotAvailable | `from foundry_sdk.v2.language_models.errors import LanguageModelNotAvailable` |
**LanguageModels** | LanguageModelNotFound | `from foundry_sdk.v2.language_models.errors import LanguageModelNotFound` |
**LanguageModels** | LanguageModelPermissionDenied | `from foundry_sdk.v2.language_models.errors import LanguageModelPermissionDenied` |
**LanguageModels** | MultipleSystemPromptsNotSupported | `from foundry_sdk.v2.language_models.errors import MultipleSystemPromptsNotSupported` |
**LanguageModels** | MultipleToolResultContentsNotSupported | `from foundry_sdk.v2.language_models.errors import MultipleToolResultContentsNotSupported` |
**LanguageModels** | OpenAiEmbeddingsPermissionDenied | `from foundry_sdk.v2.language_models.errors import OpenAiEmbeddingsPermissionDenied` |
**MediaSets** | ConflictingMediaSetIdentifiers | `from foundry_sdk.v2.media_sets.errors import ConflictingMediaSetIdentifiers` |
**MediaSets** | GetMediaItemRidByPathPermissionDenied | `from foundry_sdk.v2.media_sets.errors import GetMediaItemRidByPathPermissionDenied` |
**MediaSets** | InvalidMediaItemRid | `from foundry_sdk.v2.media_sets.errors import InvalidMediaItemRid` |
**MediaSets** | InvalidMediaItemSchema | `from foundry_sdk.v2.media_sets.errors import InvalidMediaItemSchema` |
**MediaSets** | MediaItemHasUnsupportedSecuritySettings | `from foundry_sdk.v2.media_sets.errors import MediaItemHasUnsupportedSecuritySettings` |
**MediaSets** | MediaItemImageUnparsable | `from foundry_sdk.v2.media_sets.errors import MediaItemImageUnparsable` |
**MediaSets** | MediaItemIsPasswordProtected | `from foundry_sdk.v2.media_sets.errors import MediaItemIsPasswordProtected` |
**MediaSets** | MediaItemNotFound | `from foundry_sdk.v2.media_sets.errors import MediaItemNotFound` |
**MediaSets** | MediaItemRidAlreadyExists | `from foundry_sdk.v2.media_sets.errors import MediaItemRidAlreadyExists` |
**MediaSets** | MediaItemXmlUnparsable | `from foundry_sdk.v2.media_sets.errors import MediaItemXmlUnparsable` |
**MediaSets** | MediaSetNotFound | `from foundry_sdk.v2.media_sets.errors import MediaSetNotFound` |
**MediaSets** | MediaSetOpenTransactionAlreadyExists | `from foundry_sdk.v2.media_sets.errors import MediaSetOpenTransactionAlreadyExists` |
**MediaSets** | MissingMediaItemContent | `from foundry_sdk.v2.media_sets.errors import MissingMediaItemContent` |
**MediaSets** | MissingMediaItemPath | `from foundry_sdk.v2.media_sets.errors import MissingMediaItemPath` |
**MediaSets** | TemporaryMediaUploadInsufficientPermissions | `from foundry_sdk.v2.media_sets.errors import TemporaryMediaUploadInsufficientPermissions` |
**MediaSets** | TemporaryMediaUploadUnknownFailure | `from foundry_sdk.v2.media_sets.errors import TemporaryMediaUploadUnknownFailure` |
**MediaSets** | TransformationNotFound | `from foundry_sdk.v2.media_sets.errors import TransformationNotFound` |
**MediaSets** | TransformationUnavailable | `from foundry_sdk.v2.media_sets.errors import TransformationUnavailable` |
**MediaSets** | TransformedMediaItemNotFound | `from foundry_sdk.v2.media_sets.errors import TransformedMediaItemNotFound` |
**MediaSets** | UnexpectedMetadataType | `from foundry_sdk.v2.media_sets.errors import UnexpectedMetadataType` |
**Models** | CondaSolveFailureForProvidedPackages | `from foundry_sdk.v2.models.errors import CondaSolveFailureForProvidedPackages` |
**Models** | CreateConfigValidationError | `from foundry_sdk.v2.models.errors import CreateConfigValidationError` |
**Models** | CreateModelPermissionDenied | `from foundry_sdk.v2.models.errors import CreateModelPermissionDenied` |
**Models** | CreateModelStudioConfigVersionPermissionDenied | `from foundry_sdk.v2.models.errors import CreateModelStudioConfigVersionPermissionDenied` |
**Models** | CreateModelStudioPermissionDenied | `from foundry_sdk.v2.models.errors import CreateModelStudioPermissionDenied` |
**Models** | CreateModelVersionPermissionDenied | `from foundry_sdk.v2.models.errors import CreateModelVersionPermissionDenied` |
**Models** | ExperimentArtifactNotFound | `from foundry_sdk.v2.models.errors import ExperimentArtifactNotFound` |
**Models** | ExperimentNotFound | `from foundry_sdk.v2.models.errors import ExperimentNotFound` |
**Models** | ExperimentSeriesNotFound | `from foundry_sdk.v2.models.errors import ExperimentSeriesNotFound` |
**Models** | InferenceFailure | `from foundry_sdk.v2.models.errors import InferenceFailure` |
**Models** | InferenceInvalidInput | `from foundry_sdk.v2.models.errors import InferenceInvalidInput` |
**Models** | InferenceTimeout | `from foundry_sdk.v2.models.errors import InferenceTimeout` |
**Models** | InvalidExperimentSearchFilter | `from foundry_sdk.v2.models.errors import InvalidExperimentSearchFilter` |
**Models** | InvalidModelApi | `from foundry_sdk.v2.models.errors import InvalidModelApi` |
**Models** | InvalidModelStudioCreateRequest | `from foundry_sdk.v2.models.errors import InvalidModelStudioCreateRequest` |
**Models** | JsonExperimentArtifactTablePermissionDenied | `from foundry_sdk.v2.models.errors import JsonExperimentArtifactTablePermissionDenied` |
**Models** | JsonExperimentSeriesPermissionDenied | `from foundry_sdk.v2.models.errors import JsonExperimentSeriesPermissionDenied` |
**Models** | LatestModelStudioConfigVersionsPermissionDenied | `from foundry_sdk.v2.models.errors import LatestModelStudioConfigVersionsPermissionDenied` |
**Models** | LaunchModelStudioPermissionDenied | `from foundry_sdk.v2.models.errors import LaunchModelStudioPermissionDenied` |
**Models** | LiveDeploymentNotFound | `from foundry_sdk.v2.models.errors import LiveDeploymentNotFound` |
**Models** | ModelExperimentNotFound | `from foundry_sdk.v2.models.errors import ModelExperimentNotFound` |
**Models** | ModelNotFound | `from foundry_sdk.v2.models.errors import ModelNotFound` |
**Models** | ModelStudioConfigVersionNotFound | `from foundry_sdk.v2.models.errors import ModelStudioConfigVersionNotFound` |
**Models** | ModelStudioNotFound | `from foundry_sdk.v2.models.errors import ModelStudioNotFound` |
**Models** | ModelStudioTrainerNotFound | `from foundry_sdk.v2.models.errors import ModelStudioTrainerNotFound` |
**Models** | ModelVersionNotFound | `from foundry_sdk.v2.models.errors import ModelVersionNotFound` |
**Models** | ParquetExperimentArtifactTablePermissionDenied | `from foundry_sdk.v2.models.errors import ParquetExperimentArtifactTablePermissionDenied` |
**Models** | ParquetExperimentSeriesPermissionDenied | `from foundry_sdk.v2.models.errors import ParquetExperimentSeriesPermissionDenied` |
**Models** | SearchExperimentsPermissionDenied | `from foundry_sdk.v2.models.errors import SearchExperimentsPermissionDenied` |
**Models** | TrainerNotFound | `from foundry_sdk.v2.models.errors import TrainerNotFound` |
**Models** | TransformJsonLiveDeploymentPermissionDenied | `from foundry_sdk.v2.models.errors import TransformJsonLiveDeploymentPermissionDenied` |
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
**Ontologies** | AggregationMetricNotSupported | `from foundry_sdk.v2.ontologies.errors import AggregationMetricNotSupported` |
**Ontologies** | AggregationNestedObjectSetSizeExceededLimit | `from foundry_sdk.v2.ontologies.errors import AggregationNestedObjectSetSizeExceededLimit` |
**Ontologies** | ApplyActionFailed | `from foundry_sdk.v2.ontologies.errors import ApplyActionFailed` |
**Ontologies** | AttachmentNotFound | `from foundry_sdk.v2.ontologies.errors import AttachmentNotFound` |
**Ontologies** | AttachmentRidAlreadyExists | `from foundry_sdk.v2.ontologies.errors import AttachmentRidAlreadyExists` |
**Ontologies** | AttachmentSizeExceededLimit | `from foundry_sdk.v2.ontologies.errors import AttachmentSizeExceededLimit` |
**Ontologies** | CipherChannelNotFound | `from foundry_sdk.v2.ontologies.errors import CipherChannelNotFound` |
**Ontologies** | CompositePrimaryKeyNotSupported | `from foundry_sdk.v2.ontologies.errors import CompositePrimaryKeyNotSupported` |
**Ontologies** | ConsistentSnapshotError | `from foundry_sdk.v2.ontologies.errors import ConsistentSnapshotError` |
**Ontologies** | DefaultAndNullGroupsNotSupported | `from foundry_sdk.v2.ontologies.errors import DefaultAndNullGroupsNotSupported` |
**Ontologies** | DerivedPropertyApiNamesNotUnique | `from foundry_sdk.v2.ontologies.errors import DerivedPropertyApiNamesNotUnique` |
**Ontologies** | DuplicateOrderBy | `from foundry_sdk.v2.ontologies.errors import DuplicateOrderBy` |
**Ontologies** | EditObjectPermissionDenied | `from foundry_sdk.v2.ontologies.errors import EditObjectPermissionDenied` |
**Ontologies** | FunctionEncounteredUserFacingError | `from foundry_sdk.v2.ontologies.errors import FunctionEncounteredUserFacingError` |
**Ontologies** | FunctionExecutionFailed | `from foundry_sdk.v2.ontologies.errors import FunctionExecutionFailed` |
**Ontologies** | FunctionExecutionTimedOut | `from foundry_sdk.v2.ontologies.errors import FunctionExecutionTimedOut` |
**Ontologies** | FunctionInvalidInput | `from foundry_sdk.v2.ontologies.errors import FunctionInvalidInput` |
**Ontologies** | HighScaleComputationNotEnabled | `from foundry_sdk.v2.ontologies.errors import HighScaleComputationNotEnabled` |
**Ontologies** | IncompatibleNestedObjectSet | `from foundry_sdk.v2.ontologies.errors import IncompatibleNestedObjectSet` |
**Ontologies** | InterfaceBasedObjectSetNotSupported | `from foundry_sdk.v2.ontologies.errors import InterfaceBasedObjectSetNotSupported` |
**Ontologies** | InterfaceLinkTypeNotFound | `from foundry_sdk.v2.ontologies.errors import InterfaceLinkTypeNotFound` |
**Ontologies** | InterfacePropertiesHaveDifferentIds | `from foundry_sdk.v2.ontologies.errors import InterfacePropertiesHaveDifferentIds` |
**Ontologies** | InterfacePropertiesNotFound | `from foundry_sdk.v2.ontologies.errors import InterfacePropertiesNotFound` |
**Ontologies** | InterfacePropertyNotFound | `from foundry_sdk.v2.ontologies.errors import InterfacePropertyNotFound` |
**Ontologies** | InterfaceTypeNotFound | `from foundry_sdk.v2.ontologies.errors import InterfaceTypeNotFound` |
**Ontologies** | InterfaceTypesNotFound | `from foundry_sdk.v2.ontologies.errors import InterfaceTypesNotFound` |
**Ontologies** | InvalidAggregationOrdering | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationOrdering` |
**Ontologies** | InvalidAggregationOrderingWithNullValues | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationOrderingWithNullValues` |
**Ontologies** | InvalidAggregationRange | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationRange` |
**Ontologies** | InvalidAggregationRangePropertyType | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationRangePropertyType` |
**Ontologies** | InvalidAggregationRangePropertyTypeForInterface | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationRangePropertyTypeForInterface` |
**Ontologies** | InvalidAggregationRangeValue | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationRangeValue` |
**Ontologies** | InvalidAggregationRangeValueForInterface | `from foundry_sdk.v2.ontologies.errors import InvalidAggregationRangeValueForInterface` |
**Ontologies** | InvalidApplyActionOptionCombination | `from foundry_sdk.v2.ontologies.errors import InvalidApplyActionOptionCombination` |
**Ontologies** | InvalidContentLength | `from foundry_sdk.v2.ontologies.errors import InvalidContentLength` |
**Ontologies** | InvalidContentType | `from foundry_sdk.v2.ontologies.errors import InvalidContentType` |
**Ontologies** | InvalidDerivedPropertyDefinition | `from foundry_sdk.v2.ontologies.errors import InvalidDerivedPropertyDefinition` |
**Ontologies** | InvalidDurationGroupByPropertyType | `from foundry_sdk.v2.ontologies.errors import InvalidDurationGroupByPropertyType` |
**Ontologies** | InvalidDurationGroupByPropertyTypeForInterface | `from foundry_sdk.v2.ontologies.errors import InvalidDurationGroupByPropertyTypeForInterface` |
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
**Ontologies** | InvalidTransactionEditPropertyValue | `from foundry_sdk.v2.ontologies.errors import InvalidTransactionEditPropertyValue` |
**Ontologies** | InvalidUserId | `from foundry_sdk.v2.ontologies.errors import InvalidUserId` |
**Ontologies** | InvalidVectorDimension | `from foundry_sdk.v2.ontologies.errors import InvalidVectorDimension` |
**Ontologies** | LinkAlreadyExists | `from foundry_sdk.v2.ontologies.errors import LinkAlreadyExists` |
**Ontologies** | LinkedObjectNotFound | `from foundry_sdk.v2.ontologies.errors import LinkedObjectNotFound` |
**Ontologies** | LinkTypeNotFound | `from foundry_sdk.v2.ontologies.errors import LinkTypeNotFound` |
**Ontologies** | LoadObjectSetLinksNotSupported | `from foundry_sdk.v2.ontologies.errors import LoadObjectSetLinksNotSupported` |
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
**Ontologies** | ObjectsModifiedConcurrently | `from foundry_sdk.v2.ontologies.errors import ObjectsModifiedConcurrently` |
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
**Ontologies** | PropertyExactMatchingNotSupported | `from foundry_sdk.v2.ontologies.errors import PropertyExactMatchingNotSupported` |
**Ontologies** | PropertyFiltersNotSupported | `from foundry_sdk.v2.ontologies.errors import PropertyFiltersNotSupported` |
**Ontologies** | PropertyNotFound | `from foundry_sdk.v2.ontologies.errors import PropertyNotFound` |
**Ontologies** | PropertyNotFoundOnObject | `from foundry_sdk.v2.ontologies.errors import PropertyNotFoundOnObject` |
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
**Ontologies** | SimilarityThresholdOutOfRange | `from foundry_sdk.v2.ontologies.errors import SimilarityThresholdOutOfRange` |
**Ontologies** | TooManyNearestNeighborsRequested | `from foundry_sdk.v2.ontologies.errors import TooManyNearestNeighborsRequested` |
**Ontologies** | UnauthorizedCipherOperation | `from foundry_sdk.v2.ontologies.errors import UnauthorizedCipherOperation` |
**Ontologies** | UndecryptableValue | `from foundry_sdk.v2.ontologies.errors import UndecryptableValue` |
**Ontologies** | UniqueIdentifierLinkIdsDoNotExistInActionType | `from foundry_sdk.v2.ontologies.errors import UniqueIdentifierLinkIdsDoNotExistInActionType` |
**Ontologies** | UnknownParameter | `from foundry_sdk.v2.ontologies.errors import UnknownParameter` |
**Ontologies** | UnsupportedInterfaceBasedObjectSet | `from foundry_sdk.v2.ontologies.errors import UnsupportedInterfaceBasedObjectSet` |
**Ontologies** | UnsupportedObjectSet | `from foundry_sdk.v2.ontologies.errors import UnsupportedObjectSet` |
**Ontologies** | ValueTypeNotFound | `from foundry_sdk.v2.ontologies.errors import ValueTypeNotFound` |
**Ontologies** | ViewObjectPermissionDenied | `from foundry_sdk.v2.ontologies.errors import ViewObjectPermissionDenied` |
**Orchestration** | BuildInputsNotFound | `from foundry_sdk.v2.orchestration.errors import BuildInputsNotFound` |
**Orchestration** | BuildInputsPermissionDenied | `from foundry_sdk.v2.orchestration.errors import BuildInputsPermissionDenied` |
**Orchestration** | BuildNotFound | `from foundry_sdk.v2.orchestration.errors import BuildNotFound` |
**Orchestration** | BuildNotRunning | `from foundry_sdk.v2.orchestration.errors import BuildNotRunning` |
**Orchestration** | BuildTargetsMissingJobSpecs | `from foundry_sdk.v2.orchestration.errors import BuildTargetsMissingJobSpecs` |
**Orchestration** | BuildTargetsNotFound | `from foundry_sdk.v2.orchestration.errors import BuildTargetsNotFound` |
**Orchestration** | BuildTargetsPermissionDenied | `from foundry_sdk.v2.orchestration.errors import BuildTargetsPermissionDenied` |
**Orchestration** | BuildTargetsResolutionError | `from foundry_sdk.v2.orchestration.errors import BuildTargetsResolutionError` |
**Orchestration** | BuildTargetsUpToDate | `from foundry_sdk.v2.orchestration.errors import BuildTargetsUpToDate` |
**Orchestration** | CancelBuildPermissionDenied | `from foundry_sdk.v2.orchestration.errors import CancelBuildPermissionDenied` |
**Orchestration** | CreateBuildPermissionDenied | `from foundry_sdk.v2.orchestration.errors import CreateBuildPermissionDenied` |
**Orchestration** | CreateSchedulePermissionDenied | `from foundry_sdk.v2.orchestration.errors import CreateSchedulePermissionDenied` |
**Orchestration** | DeleteSchedulePermissionDenied | `from foundry_sdk.v2.orchestration.errors import DeleteSchedulePermissionDenied` |
**Orchestration** | GetAffectedResourcesSchedulePermissionDenied | `from foundry_sdk.v2.orchestration.errors import GetAffectedResourcesSchedulePermissionDenied` |
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
**SqlQueries** | ExecuteOntologySqlQueryPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import ExecuteOntologySqlQueryPermissionDenied` |
**SqlQueries** | ExecuteSqlQueryPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import ExecuteSqlQueryPermissionDenied` |
**SqlQueries** | GetResultsSqlQueryPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import GetResultsSqlQueryPermissionDenied` |
**SqlQueries** | GetStatusSqlQueryPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import GetStatusSqlQueryPermissionDenied` |
**SqlQueries** | OntologyQueryFailed | `from foundry_sdk.v2.sql_queries.errors import OntologyQueryFailed` |
**SqlQueries** | QueryCanceled | `from foundry_sdk.v2.sql_queries.errors import QueryCanceled` |
**SqlQueries** | QueryFailed | `from foundry_sdk.v2.sql_queries.errors import QueryFailed` |
**SqlQueries** | QueryParseError | `from foundry_sdk.v2.sql_queries.errors import QueryParseError` |
**SqlQueries** | QueryPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import QueryPermissionDenied` |
**SqlQueries** | QueryRunning | `from foundry_sdk.v2.sql_queries.errors import QueryRunning` |
**SqlQueries** | ReadQueryInputsPermissionDenied | `from foundry_sdk.v2.sql_queries.errors import ReadQueryInputsPermissionDenied` |
**Streams** | CannotCreateStreamingDatasetInUserFolder | `from foundry_sdk.v2.streams.errors import CannotCreateStreamingDatasetInUserFolder` |
**Streams** | CannotWriteToTrashedStream | `from foundry_sdk.v2.streams.errors import CannotWriteToTrashedStream` |
**Streams** | CommitSubscriberOffsetsPermissionDenied | `from foundry_sdk.v2.streams.errors import CommitSubscriberOffsetsPermissionDenied` |
**Streams** | CreateStreamingDatasetPermissionDenied | `from foundry_sdk.v2.streams.errors import CreateStreamingDatasetPermissionDenied` |
**Streams** | CreateStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import CreateStreamPermissionDenied` |
**Streams** | CreateSubscriberPermissionDenied | `from foundry_sdk.v2.streams.errors import CreateSubscriberPermissionDenied` |
**Streams** | DeleteSubscriberPermissionDenied | `from foundry_sdk.v2.streams.errors import DeleteSubscriberPermissionDenied` |
**Streams** | FailedToProcessBinaryRecord | `from foundry_sdk.v2.streams.errors import FailedToProcessBinaryRecord` |
**Streams** | GetEndOffsetsForStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import GetEndOffsetsForStreamPermissionDenied` |
**Streams** | GetRecordsFromStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import GetRecordsFromStreamPermissionDenied` |
**Streams** | GetSubscriberReadPositionPermissionDenied | `from foundry_sdk.v2.streams.errors import GetSubscriberReadPositionPermissionDenied` |
**Streams** | InvalidStreamNoSchema | `from foundry_sdk.v2.streams.errors import InvalidStreamNoSchema` |
**Streams** | InvalidStreamType | `from foundry_sdk.v2.streams.errors import InvalidStreamType` |
**Streams** | PublishBinaryRecordToStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import PublishBinaryRecordToStreamPermissionDenied` |
**Streams** | PublishRecordsToStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import PublishRecordsToStreamPermissionDenied` |
**Streams** | PublishRecordToStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import PublishRecordToStreamPermissionDenied` |
**Streams** | ReadRecordsFromSubscriberPermissionDenied | `from foundry_sdk.v2.streams.errors import ReadRecordsFromSubscriberPermissionDenied` |
**Streams** | RecordDoesNotMatchStreamSchema | `from foundry_sdk.v2.streams.errors import RecordDoesNotMatchStreamSchema` |
**Streams** | RecordTooLarge | `from foundry_sdk.v2.streams.errors import RecordTooLarge` |
**Streams** | ResetStreamPermissionDenied | `from foundry_sdk.v2.streams.errors import ResetStreamPermissionDenied` |
**Streams** | ResetSubscriberOffsetsPermissionDenied | `from foundry_sdk.v2.streams.errors import ResetSubscriberOffsetsPermissionDenied` |
**Streams** | StreamNotFound | `from foundry_sdk.v2.streams.errors import StreamNotFound` |
**Streams** | SubscriberAlreadyExists | `from foundry_sdk.v2.streams.errors import SubscriberAlreadyExists` |
**Streams** | SubscriberNotFound | `from foundry_sdk.v2.streams.errors import SubscriberNotFound` |
**Streams** | ViewNotFound | `from foundry_sdk.v2.streams.errors import ViewNotFound` |
**ThirdPartyApplications** | CannotDeleteDeployedVersion | `from foundry_sdk.v2.third_party_applications.errors import CannotDeleteDeployedVersion` |
**ThirdPartyApplications** | DeleteVersionPermissionDenied | `from foundry_sdk.v2.third_party_applications.errors import DeleteVersionPermissionDenied` |
**ThirdPartyApplications** | DeployWebsitePermissionDenied | `from foundry_sdk.v2.third_party_applications.errors import DeployWebsitePermissionDenied` |
**ThirdPartyApplications** | FileCountLimitExceeded | `from foundry_sdk.v2.third_party_applications.errors import FileCountLimitExceeded` |
**ThirdPartyApplications** | FileSizeLimitExceeded | `from foundry_sdk.v2.third_party_applications.errors import FileSizeLimitExceeded` |
**ThirdPartyApplications** | InvalidVersion | `from foundry_sdk.v2.third_party_applications.errors import InvalidVersion` |
**ThirdPartyApplications** | ScanningErrored | `from foundry_sdk.v2.third_party_applications.errors import ScanningErrored` |
**ThirdPartyApplications** | ScanningInProgress | `from foundry_sdk.v2.third_party_applications.errors import ScanningInProgress` |
**ThirdPartyApplications** | SiteAssetHasVulnerabilities | `from foundry_sdk.v2.third_party_applications.errors import SiteAssetHasVulnerabilities` |
**ThirdPartyApplications** | ThirdPartyApplicationNotFound | `from foundry_sdk.v2.third_party_applications.errors import ThirdPartyApplicationNotFound` |
**ThirdPartyApplications** | UndeployWebsitePermissionDenied | `from foundry_sdk.v2.third_party_applications.errors import UndeployWebsitePermissionDenied` |
**ThirdPartyApplications** | UploadSnapshotVersionPermissionDenied | `from foundry_sdk.v2.third_party_applications.errors import UploadSnapshotVersionPermissionDenied` |
**ThirdPartyApplications** | UploadVersionPermissionDenied | `from foundry_sdk.v2.third_party_applications.errors import UploadVersionPermissionDenied` |
**ThirdPartyApplications** | VersionAlreadyExists | `from foundry_sdk.v2.third_party_applications.errors import VersionAlreadyExists` |
**ThirdPartyApplications** | VersionLimitExceeded | `from foundry_sdk.v2.third_party_applications.errors import VersionLimitExceeded` |
**ThirdPartyApplications** | VersionNotFound | `from foundry_sdk.v2.third_party_applications.errors import VersionNotFound` |
**ThirdPartyApplications** | WebsiteNotFound | `from foundry_sdk.v2.third_party_applications.errors import WebsiteNotFound` |
**Widgets** | DeleteReleasePermissionDenied | `from foundry_sdk.v2.widgets.errors import DeleteReleasePermissionDenied` |
**Widgets** | DevModeSettingsNotFound | `from foundry_sdk.v2.widgets.errors import DevModeSettingsNotFound` |
**Widgets** | DisableDevModeSettingsPermissionDenied | `from foundry_sdk.v2.widgets.errors import DisableDevModeSettingsPermissionDenied` |
**Widgets** | EnableDevModeSettingsPermissionDenied | `from foundry_sdk.v2.widgets.errors import EnableDevModeSettingsPermissionDenied` |
**Widgets** | FileCountLimitExceeded | `from foundry_sdk.v2.widgets.errors import FileCountLimitExceeded` |
**Widgets** | FileSizeLimitExceeded | `from foundry_sdk.v2.widgets.errors import FileSizeLimitExceeded` |
**Widgets** | GetDevModeSettingsPermissionDenied | `from foundry_sdk.v2.widgets.errors import GetDevModeSettingsPermissionDenied` |
**Widgets** | InvalidDevModeBaseHref | `from foundry_sdk.v2.widgets.errors import InvalidDevModeBaseHref` |
**Widgets** | InvalidDevModeEntrypointCssCount | `from foundry_sdk.v2.widgets.errors import InvalidDevModeEntrypointCssCount` |
**Widgets** | InvalidDevModeEntrypointJsCount | `from foundry_sdk.v2.widgets.errors import InvalidDevModeEntrypointJsCount` |
**Widgets** | InvalidDevModeFilePath | `from foundry_sdk.v2.widgets.errors import InvalidDevModeFilePath` |
**Widgets** | InvalidDevModeWidgetSettingsCount | `from foundry_sdk.v2.widgets.errors import InvalidDevModeWidgetSettingsCount` |
**Widgets** | InvalidEntrypointCssCount | `from foundry_sdk.v2.widgets.errors import InvalidEntrypointCssCount` |
**Widgets** | InvalidEntrypointJsCount | `from foundry_sdk.v2.widgets.errors import InvalidEntrypointJsCount` |
**Widgets** | InvalidEventCount | `from foundry_sdk.v2.widgets.errors import InvalidEventCount` |
**Widgets** | InvalidEventDisplayName | `from foundry_sdk.v2.widgets.errors import InvalidEventDisplayName` |
**Widgets** | InvalidEventId | `from foundry_sdk.v2.widgets.errors import InvalidEventId` |
**Widgets** | InvalidEventParameter | `from foundry_sdk.v2.widgets.errors import InvalidEventParameter` |
**Widgets** | InvalidEventParameterCount | `from foundry_sdk.v2.widgets.errors import InvalidEventParameterCount` |
**Widgets** | InvalidEventParameterId | `from foundry_sdk.v2.widgets.errors import InvalidEventParameterId` |
**Widgets** | InvalidEventParameterUpdateId | `from foundry_sdk.v2.widgets.errors import InvalidEventParameterUpdateId` |
**Widgets** | InvalidFilePath | `from foundry_sdk.v2.widgets.errors import InvalidFilePath` |
**Widgets** | InvalidManifest | `from foundry_sdk.v2.widgets.errors import InvalidManifest` |
**Widgets** | InvalidObjectSetEventParameterType | `from foundry_sdk.v2.widgets.errors import InvalidObjectSetEventParameterType` |
**Widgets** | InvalidObjectSetParameterType | `from foundry_sdk.v2.widgets.errors import InvalidObjectSetParameterType` |
**Widgets** | InvalidParameterCount | `from foundry_sdk.v2.widgets.errors import InvalidParameterCount` |
**Widgets** | InvalidParameterDisplayName | `from foundry_sdk.v2.widgets.errors import InvalidParameterDisplayName` |
**Widgets** | InvalidParameterId | `from foundry_sdk.v2.widgets.errors import InvalidParameterId` |
**Widgets** | InvalidPublishRepository | `from foundry_sdk.v2.widgets.errors import InvalidPublishRepository` |
**Widgets** | InvalidReleaseDescription | `from foundry_sdk.v2.widgets.errors import InvalidReleaseDescription` |
**Widgets** | InvalidReleaseWidgetsCount | `from foundry_sdk.v2.widgets.errors import InvalidReleaseWidgetsCount` |
**Widgets** | InvalidVersion | `from foundry_sdk.v2.widgets.errors import InvalidVersion` |
**Widgets** | InvalidWidgetDescription | `from foundry_sdk.v2.widgets.errors import InvalidWidgetDescription` |
**Widgets** | InvalidWidgetId | `from foundry_sdk.v2.widgets.errors import InvalidWidgetId` |
**Widgets** | InvalidWidgetName | `from foundry_sdk.v2.widgets.errors import InvalidWidgetName` |
**Widgets** | OntologySdkNotFound | `from foundry_sdk.v2.widgets.errors import OntologySdkNotFound` |
**Widgets** | PauseDevModeSettingsPermissionDenied | `from foundry_sdk.v2.widgets.errors import PauseDevModeSettingsPermissionDenied` |
**Widgets** | PublishReleasePermissionDenied | `from foundry_sdk.v2.widgets.errors import PublishReleasePermissionDenied` |
**Widgets** | ReleaseNotFound | `from foundry_sdk.v2.widgets.errors import ReleaseNotFound` |
**Widgets** | RepositoryNotFound | `from foundry_sdk.v2.widgets.errors import RepositoryNotFound` |
**Widgets** | SetWidgetSetDevModeSettingsByIdPermissionDenied | `from foundry_sdk.v2.widgets.errors import SetWidgetSetDevModeSettingsByIdPermissionDenied` |
**Widgets** | SetWidgetSetDevModeSettingsPermissionDenied | `from foundry_sdk.v2.widgets.errors import SetWidgetSetDevModeSettingsPermissionDenied` |
**Widgets** | VersionAlreadyExists | `from foundry_sdk.v2.widgets.errors import VersionAlreadyExists` |
**Widgets** | VersionLimitExceeded | `from foundry_sdk.v2.widgets.errors import VersionLimitExceeded` |
**Widgets** | WidgetIdNotFound | `from foundry_sdk.v2.widgets.errors import WidgetIdNotFound` |
**Widgets** | WidgetLimitExceeded | `from foundry_sdk.v2.widgets.errors import WidgetLimitExceeded` |
**Widgets** | WidgetSetNotFound | `from foundry_sdk.v2.widgets.errors import WidgetSetNotFound` |
<a id="errors-v1-link"></a>
## Documentation for V1 errors

Namespace | Name | Import |
--------- | ---- | ------ |
**Core** | ApiFeaturePreviewUsageOnly | `from foundry_sdk.v1.core.errors import ApiFeaturePreviewUsageOnly` |
**Core** | ApiUsageDenied | `from foundry_sdk.v1.core.errors import ApiUsageDenied` |
**Core** | FolderNotFound | `from foundry_sdk.v1.core.errors import FolderNotFound` |
**Core** | FoundryBranchNotFound | `from foundry_sdk.v1.core.errors import FoundryBranchNotFound` |
**Core** | InvalidFilePath | `from foundry_sdk.v1.core.errors import InvalidFilePath` |
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
**Ontologies** | AggregationMetricNotSupported | `from foundry_sdk.v1.ontologies.errors import AggregationMetricNotSupported` |
**Ontologies** | AggregationNestedObjectSetSizeExceededLimit | `from foundry_sdk.v1.ontologies.errors import AggregationNestedObjectSetSizeExceededLimit` |
**Ontologies** | ApplyActionFailed | `from foundry_sdk.v1.ontologies.errors import ApplyActionFailed` |
**Ontologies** | AttachmentNotFound | `from foundry_sdk.v1.ontologies.errors import AttachmentNotFound` |
**Ontologies** | AttachmentRidAlreadyExists | `from foundry_sdk.v1.ontologies.errors import AttachmentRidAlreadyExists` |
**Ontologies** | AttachmentSizeExceededLimit | `from foundry_sdk.v1.ontologies.errors import AttachmentSizeExceededLimit` |
**Ontologies** | CipherChannelNotFound | `from foundry_sdk.v1.ontologies.errors import CipherChannelNotFound` |
**Ontologies** | CompositePrimaryKeyNotSupported | `from foundry_sdk.v1.ontologies.errors import CompositePrimaryKeyNotSupported` |
**Ontologies** | ConsistentSnapshotError | `from foundry_sdk.v1.ontologies.errors import ConsistentSnapshotError` |
**Ontologies** | DefaultAndNullGroupsNotSupported | `from foundry_sdk.v1.ontologies.errors import DefaultAndNullGroupsNotSupported` |
**Ontologies** | DerivedPropertyApiNamesNotUnique | `from foundry_sdk.v1.ontologies.errors import DerivedPropertyApiNamesNotUnique` |
**Ontologies** | DuplicateOrderBy | `from foundry_sdk.v1.ontologies.errors import DuplicateOrderBy` |
**Ontologies** | EditObjectPermissionDenied | `from foundry_sdk.v1.ontologies.errors import EditObjectPermissionDenied` |
**Ontologies** | FunctionEncounteredUserFacingError | `from foundry_sdk.v1.ontologies.errors import FunctionEncounteredUserFacingError` |
**Ontologies** | FunctionExecutionFailed | `from foundry_sdk.v1.ontologies.errors import FunctionExecutionFailed` |
**Ontologies** | FunctionExecutionTimedOut | `from foundry_sdk.v1.ontologies.errors import FunctionExecutionTimedOut` |
**Ontologies** | FunctionInvalidInput | `from foundry_sdk.v1.ontologies.errors import FunctionInvalidInput` |
**Ontologies** | HighScaleComputationNotEnabled | `from foundry_sdk.v1.ontologies.errors import HighScaleComputationNotEnabled` |
**Ontologies** | IncompatibleNestedObjectSet | `from foundry_sdk.v1.ontologies.errors import IncompatibleNestedObjectSet` |
**Ontologies** | InterfaceBasedObjectSetNotSupported | `from foundry_sdk.v1.ontologies.errors import InterfaceBasedObjectSetNotSupported` |
**Ontologies** | InterfaceLinkTypeNotFound | `from foundry_sdk.v1.ontologies.errors import InterfaceLinkTypeNotFound` |
**Ontologies** | InterfacePropertiesHaveDifferentIds | `from foundry_sdk.v1.ontologies.errors import InterfacePropertiesHaveDifferentIds` |
**Ontologies** | InterfacePropertiesNotFound | `from foundry_sdk.v1.ontologies.errors import InterfacePropertiesNotFound` |
**Ontologies** | InterfacePropertyNotFound | `from foundry_sdk.v1.ontologies.errors import InterfacePropertyNotFound` |
**Ontologies** | InterfaceTypeNotFound | `from foundry_sdk.v1.ontologies.errors import InterfaceTypeNotFound` |
**Ontologies** | InterfaceTypesNotFound | `from foundry_sdk.v1.ontologies.errors import InterfaceTypesNotFound` |
**Ontologies** | InvalidAggregationOrdering | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationOrdering` |
**Ontologies** | InvalidAggregationOrderingWithNullValues | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationOrderingWithNullValues` |
**Ontologies** | InvalidAggregationRange | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationRange` |
**Ontologies** | InvalidAggregationRangePropertyType | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationRangePropertyType` |
**Ontologies** | InvalidAggregationRangePropertyTypeForInterface | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationRangePropertyTypeForInterface` |
**Ontologies** | InvalidAggregationRangeValue | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationRangeValue` |
**Ontologies** | InvalidAggregationRangeValueForInterface | `from foundry_sdk.v1.ontologies.errors import InvalidAggregationRangeValueForInterface` |
**Ontologies** | InvalidApplyActionOptionCombination | `from foundry_sdk.v1.ontologies.errors import InvalidApplyActionOptionCombination` |
**Ontologies** | InvalidContentLength | `from foundry_sdk.v1.ontologies.errors import InvalidContentLength` |
**Ontologies** | InvalidContentType | `from foundry_sdk.v1.ontologies.errors import InvalidContentType` |
**Ontologies** | InvalidDerivedPropertyDefinition | `from foundry_sdk.v1.ontologies.errors import InvalidDerivedPropertyDefinition` |
**Ontologies** | InvalidDurationGroupByPropertyType | `from foundry_sdk.v1.ontologies.errors import InvalidDurationGroupByPropertyType` |
**Ontologies** | InvalidDurationGroupByPropertyTypeForInterface | `from foundry_sdk.v1.ontologies.errors import InvalidDurationGroupByPropertyTypeForInterface` |
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
**Ontologies** | InvalidTransactionEditPropertyValue | `from foundry_sdk.v1.ontologies.errors import InvalidTransactionEditPropertyValue` |
**Ontologies** | InvalidUserId | `from foundry_sdk.v1.ontologies.errors import InvalidUserId` |
**Ontologies** | InvalidVectorDimension | `from foundry_sdk.v1.ontologies.errors import InvalidVectorDimension` |
**Ontologies** | LinkAlreadyExists | `from foundry_sdk.v1.ontologies.errors import LinkAlreadyExists` |
**Ontologies** | LinkedObjectNotFound | `from foundry_sdk.v1.ontologies.errors import LinkedObjectNotFound` |
**Ontologies** | LinkTypeNotFound | `from foundry_sdk.v1.ontologies.errors import LinkTypeNotFound` |
**Ontologies** | LoadObjectSetLinksNotSupported | `from foundry_sdk.v1.ontologies.errors import LoadObjectSetLinksNotSupported` |
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
**Ontologies** | ObjectsModifiedConcurrently | `from foundry_sdk.v1.ontologies.errors import ObjectsModifiedConcurrently` |
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
**Ontologies** | PropertyExactMatchingNotSupported | `from foundry_sdk.v1.ontologies.errors import PropertyExactMatchingNotSupported` |
**Ontologies** | PropertyFiltersNotSupported | `from foundry_sdk.v1.ontologies.errors import PropertyFiltersNotSupported` |
**Ontologies** | PropertyNotFound | `from foundry_sdk.v1.ontologies.errors import PropertyNotFound` |
**Ontologies** | PropertyNotFoundOnObject | `from foundry_sdk.v1.ontologies.errors import PropertyNotFoundOnObject` |
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
**Ontologies** | SimilarityThresholdOutOfRange | `from foundry_sdk.v1.ontologies.errors import SimilarityThresholdOutOfRange` |
**Ontologies** | TooManyNearestNeighborsRequested | `from foundry_sdk.v1.ontologies.errors import TooManyNearestNeighborsRequested` |
**Ontologies** | UnauthorizedCipherOperation | `from foundry_sdk.v1.ontologies.errors import UnauthorizedCipherOperation` |
**Ontologies** | UndecryptableValue | `from foundry_sdk.v1.ontologies.errors import UndecryptableValue` |
**Ontologies** | UniqueIdentifierLinkIdsDoNotExistInActionType | `from foundry_sdk.v1.ontologies.errors import UniqueIdentifierLinkIdsDoNotExistInActionType` |
**Ontologies** | UnknownParameter | `from foundry_sdk.v1.ontologies.errors import UnknownParameter` |
**Ontologies** | UnsupportedInterfaceBasedObjectSet | `from foundry_sdk.v1.ontologies.errors import UnsupportedInterfaceBasedObjectSet` |
**Ontologies** | UnsupportedObjectSet | `from foundry_sdk.v1.ontologies.errors import UnsupportedObjectSet` |
**Ontologies** | ValueTypeNotFound | `from foundry_sdk.v1.ontologies.errors import ValueTypeNotFound` |
**Ontologies** | ViewObjectPermissionDenied | `from foundry_sdk.v1.ontologies.errors import ViewObjectPermissionDenied` |


## Contributions

This repository does not accept code contributions.

If you have any questions, concerns, or ideas for improvements, create an
issue with Palantir Support.

## License
This project is made available under the [Apache 2.0 License](/LICENSE).
