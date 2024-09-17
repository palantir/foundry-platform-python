# Foundry Platform SDK

![Supported Python Versions](https://img.shields.io/pypi/pyversions/foundry-platform-sdk)
[![PyPI Version](https://img.shields.io/pypi/v/foundry-platform-sdk)](https://pypi.org/project/foundry-platform-sdk/)
[![License](https://img.shields.io/badge/License-Apache%202.0-lightgrey.svg)](https://opensource.org/licenses/Apache-2.0)

> [!WARNING]
> This SDK is incubating and subject to change.

The Foundry Platform SDK is a Python SDK built on top of the Foundry API. Review [Foundry API documentation](https://www.palantir.com/docs/foundry/api/) for more details.

> [!NOTE]
> This Python package is automatically generated based off our [OpenAPI specification](openapi.yml).


<a id="sdk-vs-sdk"></a>
## Foundry Platform SDK vs. Ontology SDK
Palantir provides two different Python Software Development Kits (SDKs) for interacting with Foundry. Make sure to choose the correct SDK for your use case. As a general rule of thumb, any applications which leverage the Ontology should use the Ontology SDK for a superior development experience.

> [!IMPORTANT]
> Make sure to understand the difference between the Foundry SDK and the Ontology SDK. Review this section before continuing with the installation of this library.

### Ontology SDK
The Ontology SDK allows you to access the full power of the Ontology directly from your development environment. You can generate the Ontology SDK using the Developer Console, a portal for creating and managing applications using Palantir APIs. Review the [Ontology SDK documentation](https://www.palantir.com/docs/foundry/ontology-sdk) for more information.

### Foundry Platform SDK
The Foundry Platform Software Development Kit (SDK) is generated from the Foundry API's OpenAPI specification
file (see [openapi.yml](openapi.yml)). The intention of this SDK is to encompass endpoints related to interacting
with the platform itself. Although there are Ontology services included by this SDK, this SDK surfaces endpoints
for interacting with Ontological resources such as object types, link types, and action types. In contrast, the OSDK allows you to interact with objects, links and Actions (for example, querying your objects, applying an action).

<a id="installation"></a>
## Installation
You can install the Python package using `pip`:

```sh
pip install foundry-platform-sdk
```

Then, import the package:
```python
import foundry
```

<a id="major-version-link"></a>
## API Versioning
Every endpoint of the Foundry API is versioned using a version number that appears in the URL. For example,
v1 endpoints look like this:

```
https://<hostname>/api/v1/...
```

This SDK exposes several clients, one for each major version of the API. For example, the latest major version of the
SDK is **v2** and is exposed using the `FoundryV2Client` located in the
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
foundry_client = foundry.v2.FoundryV2Client(
    auth=foundry.UserTokenAuth(
        hostname="example.palantirfoundry.com",
        token=os.environ["BEARER_TOKEN"],
    ),
    hostname="example.palantirfoundry.com",
)
```

<a id="oauth2-client"></a>
### OAuth2 Client
OAuth2 clients are the recommended way to connect to Foundry in production applications. Currently, this SDK
natively supports the [client credentials grant flow](https://www.palantir.com/docs/foundry/platform-security-third-party/writing-oauth2-clients/#client-credentials-grant).
The token obtained by this grant can be used to access resources on behalf of the created service user. To use this
authentication method, you will first need to register a third-party application in Foundry by following [the guide on third-party application registration](https://www.palantir.com/docs/foundry/platform-security-third-party/register-3pa).

To use the confidential client functionality, you first need to contstruct a `ConfidentialClientAuth` object and initiate
the sign-in process using the `sign_in_as_service_user` method. As these service user tokens have a short lifespan, we
automatically retry all operations one time if a `401` (Unauthorized) error is thrown after refreshing the token.

```python
auth = foundry.ConfidentialClientAuth(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    hostname="example.palantirfoundry.com",
    scopes=["api:read-data"],
)

auth.sign_in_as_service_user()
```

> [!IMPORTANT]
> Make sure to select the appropriate scopes when initializating the `ConfidentialClientAuth`. You can find the relevant scopes
> in the [endpoint documentation](#apis-link).

After creating the `ConfidentialClientAuth` object, pass it in to the `FoundryV2Client`,

```python
foundry_client = foundry.v2.FoundryV2Client(auth=auth, hostname="example.palantirfoundry.com")
```

## Quickstart

Follow the [installation procedure](#installation) and determine which [authentication method](#authorization) is
best suited for your instance before following this example. For simplicity, the `UserTokenAuth` class will be used for demonstration
purposes.

```python
from foundry.v1 import FoundryV1Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV1Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# DatasetRid | datasetRid
dataset_rid = "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"

# Union[CreateBranchRequest, CreateBranchRequestDict] | Body of the request
create_branch_request = {"branchId": "my-branch"}


try:
    api_response = foundry_client.datasets.Dataset.Branch.create(
        dataset_rid,
        create_branch_request,
    )
    print("The create response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Branch.create: %s\n" % e)

```

Want to learn more about this Foundry SDK library? Review the following sections.

↳ [Error handling](#errors): Learn more about HTTP & data validation error handling  
↳ [Pagination](#pagination): Learn how to work with paginated endpoints in the SDK  
↳ [Static type analysis](#static-types): Learn about the static type analysis capabilities of this library

## Error handling
### Data validation
The SDK employs [Pydantic](https://docs.pydantic.dev/latest/) for runtime validation
of arguments. In the example below, we are passing in a number to `transactionRid`
which should actually be a string type:

```python
foundry_client.datasets.Dataset.Branch.create(
    "ri.foundry.main.dataset.abc",
    create_branch_request={"branchId": "123", "transactionRid": 123},
)
```

If you did this, you would receive an error that looks something like:

```
pydantic_core._pydantic_core.ValidationError: 1 validation error for create
create_branch_request.transactionRid
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
When an HTTP error status is returned, a `PalantirRPCException` is thrown. All HTTP error exception classes inherit from `ApiException`.

```python
from foundry import PalantirRPCException


try:
    api_response = foundry_client.datasets.Transaction.abort(dataset_rid, transaction_rid)
    ...
except PalantirRPCException as e:
    print("Another HTTP exception occurred: " + str(e))
```

This exception will have the following properties. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors) for details about the Foundry error information.

| Property          | Type                   | Description                                                                                                                    |
| ----------------- | -----------------------| ------------------------------------------------------------------------------------------------------------------------------ |
| name              | str                    | The Palantir error name. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors).        |
| error_instance_id | str                    | The Palantir error instance ID. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors). |
| parameters        | Dict[str, Any]         | The Palantir error parameters. See the [Foundry API docs](https://www.palantir.com/docs/foundry/api/general/overview/errors).  |


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

This will automatically fetch and iterate through all the pages of data from the specified API endpoint. For more granular control, you can manually fetch each page using the associated page methods.

```python
page = foundry_client.datasets.Dataset.Branch.page(dataset_rid)
while page.next_page_token:
    for branch in page.data:
        print(branch)

    page = foundry_client.datasets.Dataset.Branch.page(dataset_rid, page_token=page.next_page_token)
```


<a id="static-types"></a>
## Static type analysis
This library uses [Pydantic](https://docs.pydantic.dev) for creating and validating data models which you will see in the
method definitions (see [Documentation for Models](#models-link) below for a full list of models). All request parameters with nested
objects use both [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict) and `Pydantic` models (either can
be passed in) whereas responses only use `Pydantic` models. For example, here is how `Branch.create` method is defined in the
datasets namespace:

```python
    def create(
        self,
        dataset_rid: DatasetRid,
        create_branch_request: Union[CreateBranchRequest, CreateBranchRequestDict],
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Branch:
        ...
```

> [!TIP]
> A `Pydantic` model can be converted into its `TypedDict` representation using the `to_dict` method. For example, if you handle
> a variable of type `CreateBranchRequest` and you called `to_dict()` on that variable you would receive a `CreateBranchRequestDict`
> variable.

If you are using a static type checker (for example, [mypy](https://mypy-lang.org), [pyright](https://github.com/microsoft/pyright)), you
get static type analysis for the arguments you provide to the function *and* with the response. For example, if you pass an `int`
to `branchId` while calling `create` and then try to access `branchId` in returned [`Branch`](docs/Branch.md) object (the
property is actually called `branch_id`), you will get the following errors:


```python
branch = foundry_client.datasets.Dataset.Branch.create(
    "ri.foundry.main.dataset.abc",
    create_branch_request={
        # ERROR: "Literal[123]" is incompatible with "BranchId"
        "branchId": 123
    },
)
# ERROR: Cannot access member "branchId" for type "Branch"
print(branch.branchId)
```

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
**Admin** | Group | [**create**](docs/v2/namespaces/Admin/Group.md#create) | **POST** /v2/admin/groups |
**Admin** | Group | [**delete**](docs/v2/namespaces/Admin/Group.md#delete) | **DELETE** /v2/admin/groups/{groupId} |
**Admin** | Group | [**get**](docs/v2/namespaces/Admin/Group.md#get) | **GET** /v2/admin/groups/{groupId} |
**Admin** | Group | [**get_batch**](docs/v2/namespaces/Admin/Group.md#get_batch) | **POST** /v2/admin/groups/getBatch |
**Admin** | Group | [**list**](docs/v2/namespaces/Admin/Group.md#list) | **GET** /v2/admin/groups |
**Admin** | Group | [**page**](docs/v2/namespaces/Admin/Group.md#page) | **GET** /v2/admin/groups |
**Admin** | Group | [**search**](docs/v2/namespaces/Admin/Group.md#search) | **POST** /v2/admin/groups/search |
**Admin** | GroupMember | [**add**](docs/v2/namespaces/Admin/GroupMember.md#add) | **POST** /v2/admin/groups/{groupId}/groupMembers/add |
**Admin** | GroupMember | [**list**](docs/v2/namespaces/Admin/GroupMember.md#list) | **GET** /v2/admin/groups/{groupId}/groupMembers |
**Admin** | GroupMember | [**page**](docs/v2/namespaces/Admin/GroupMember.md#page) | **GET** /v2/admin/groups/{groupId}/groupMembers |
**Admin** | GroupMember | [**remove**](docs/v2/namespaces/Admin/GroupMember.md#remove) | **POST** /v2/admin/groups/{groupId}/groupMembers/remove |
**Admin** | GroupMembership | [**list**](docs/v2/namespaces/Admin/GroupMembership.md#list) | **GET** /v2/admin/users/{userId}/groupMemberships |
**Admin** | GroupMembership | [**page**](docs/v2/namespaces/Admin/GroupMembership.md#page) | **GET** /v2/admin/users/{userId}/groupMemberships |
**Admin** | User | [**delete**](docs/v2/namespaces/Admin/User.md#delete) | **DELETE** /v2/admin/users/{userId} |
**Admin** | User | [**get**](docs/v2/namespaces/Admin/User.md#get) | **GET** /v2/admin/users/{userId} |
**Admin** | User | [**get_batch**](docs/v2/namespaces/Admin/User.md#get_batch) | **POST** /v2/admin/users/getBatch |
**Admin** | User | [**get_current**](docs/v2/namespaces/Admin/User.md#get_current) | **GET** /v2/admin/users/getCurrent |
**Admin** | User | [**list**](docs/v2/namespaces/Admin/User.md#list) | **GET** /v2/admin/users |
**Admin** | User | [**page**](docs/v2/namespaces/Admin/User.md#page) | **GET** /v2/admin/users |
**Admin** | User | [**profile_picture**](docs/v2/namespaces/Admin/User.md#profile_picture) | **GET** /v2/admin/users/{userId}/profilePicture |
**Admin** | User | [**search**](docs/v2/namespaces/Admin/User.md#search) | **POST** /v2/admin/users/search |
**Datasets** | Branch | [**create**](docs/v2/namespaces/Datasets/Branch.md#create) | **POST** /v2/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**delete**](docs/v2/namespaces/Datasets/Branch.md#delete) | **DELETE** /v2/datasets/{datasetRid}/branches/{branchName} |
**Datasets** | Branch | [**get**](docs/v2/namespaces/Datasets/Branch.md#get) | **GET** /v2/datasets/{datasetRid}/branches/{branchName} |
**Datasets** | Branch | [**list**](docs/v2/namespaces/Datasets/Branch.md#list) | **GET** /v2/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**page**](docs/v2/namespaces/Datasets/Branch.md#page) | **GET** /v2/datasets/{datasetRid}/branches |
**Datasets** | Dataset | [**create**](docs/v2/namespaces/Datasets/Dataset.md#create) | **POST** /v2/datasets |
**Datasets** | Dataset | [**get**](docs/v2/namespaces/Datasets/Dataset.md#get) | **GET** /v2/datasets/{datasetRid} |
**Datasets** | Dataset | [**read_table**](docs/v2/namespaces/Datasets/Dataset.md#read_table) | **GET** /v2/datasets/{datasetRid}/readTable |
**Datasets** | File | [**content**](docs/v2/namespaces/Datasets/File.md#content) | **GET** /v2/datasets/{datasetRid}/files/{filePath}/content |
**Datasets** | File | [**delete**](docs/v2/namespaces/Datasets/File.md#delete) | **DELETE** /v2/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**get**](docs/v2/namespaces/Datasets/File.md#get) | **GET** /v2/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**list**](docs/v2/namespaces/Datasets/File.md#list) | **GET** /v2/datasets/{datasetRid}/files |
**Datasets** | File | [**page**](docs/v2/namespaces/Datasets/File.md#page) | **GET** /v2/datasets/{datasetRid}/files |
**Datasets** | File | [**upload**](docs/v2/namespaces/Datasets/File.md#upload) | **POST** /v2/datasets/{datasetRid}/files/{filePath}/upload |
**Datasets** | Transaction | [**abort**](docs/v2/namespaces/Datasets/Transaction.md#abort) | **POST** /v2/datasets/{datasetRid}/transactions/{transactionRid}/abort |
**Datasets** | Transaction | [**commit**](docs/v2/namespaces/Datasets/Transaction.md#commit) | **POST** /v2/datasets/{datasetRid}/transactions/{transactionRid}/commit |
**Datasets** | Transaction | [**create**](docs/v2/namespaces/Datasets/Transaction.md#create) | **POST** /v2/datasets/{datasetRid}/transactions |
**Datasets** | Transaction | [**get**](docs/v2/namespaces/Datasets/Transaction.md#get) | **GET** /v2/datasets/{datasetRid}/transactions/{transactionRid} |
**Ontologies** | Action | [**apply**](docs/v2/namespaces/Ontologies/Action.md#apply) | **POST** /v2/ontologies/{ontology}/actions/{action}/apply |
**Ontologies** | Action | [**apply_batch**](docs/v2/namespaces/Ontologies/Action.md#apply_batch) | **POST** /v2/ontologies/{ontology}/actions/{action}/applyBatch |
**Ontologies** | ActionType | [**get**](docs/v2/namespaces/Ontologies/ActionType.md#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} |
**Ontologies** | ActionType | [**list**](docs/v2/namespaces/Ontologies/ActionType.md#list) | **GET** /v2/ontologies/{ontology}/actionTypes |
**Ontologies** | ActionType | [**page**](docs/v2/namespaces/Ontologies/ActionType.md#page) | **GET** /v2/ontologies/{ontology}/actionTypes |
**Ontologies** | Attachment | [**get**](docs/v2/namespaces/Ontologies/Attachment.md#get) | **GET** /v2/ontologies/attachments/{attachmentRid} |
**Ontologies** | Attachment | [**read**](docs/v2/namespaces/Ontologies/Attachment.md#read) | **GET** /v2/ontologies/attachments/{attachmentRid}/content |
**Ontologies** | Attachment | [**upload**](docs/v2/namespaces/Ontologies/Attachment.md#upload) | **POST** /v2/ontologies/attachments/upload |
**Ontologies** | AttachmentProperty | [**get_attachment**](docs/v2/namespaces/Ontologies/AttachmentProperty.md#get_attachment) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property} |
**Ontologies** | AttachmentProperty | [**get_attachment_by_rid**](docs/v2/namespaces/Ontologies/AttachmentProperty.md#get_attachment_by_rid) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid} |
**Ontologies** | AttachmentProperty | [**read_attachment**](docs/v2/namespaces/Ontologies/AttachmentProperty.md#read_attachment) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/content |
**Ontologies** | AttachmentProperty | [**read_attachment_by_rid**](docs/v2/namespaces/Ontologies/AttachmentProperty.md#read_attachment_by_rid) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}/content |
**Ontologies** | LinkedObject | [**get_linked_object**](docs/v2/namespaces/Ontologies/LinkedObject.md#get_linked_object) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey} |
**Ontologies** | LinkedObject | [**list_linked_objects**](docs/v2/namespaces/Ontologies/LinkedObject.md#list_linked_objects) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType} |
**Ontologies** | LinkedObject | [**page_linked_objects**](docs/v2/namespaces/Ontologies/LinkedObject.md#page_linked_objects) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType} |
**Ontologies** | ObjectType | [**get**](docs/v2/namespaces/Ontologies/ObjectType.md#get) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType} |
**Ontologies** | ObjectType | [**get_outgoing_link_type**](docs/v2/namespaces/Ontologies/ObjectType.md#get_outgoing_link_type) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
**Ontologies** | ObjectType | [**list**](docs/v2/namespaces/Ontologies/ObjectType.md#list) | **GET** /v2/ontologies/{ontology}/objectTypes |
**Ontologies** | ObjectType | [**list_outgoing_link_types**](docs/v2/namespaces/Ontologies/ObjectType.md#list_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | ObjectType | [**page**](docs/v2/namespaces/Ontologies/ObjectType.md#page) | **GET** /v2/ontologies/{ontology}/objectTypes |
**Ontologies** | ObjectType | [**page_outgoing_link_types**](docs/v2/namespaces/Ontologies/ObjectType.md#page_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | Ontology | [**get**](docs/v2/namespaces/Ontologies/Ontology.md#get) | **GET** /v2/ontologies/{ontology} |
**Ontologies** | Ontology | [**get_full_metadata**](docs/v2/namespaces/Ontologies/Ontology.md#get_full_metadata) | **GET** /v2/ontologies/{ontology}/fullMetadata |
**Ontologies** | OntologyInterface | [**aggregate**](docs/v2/namespaces/Ontologies/OntologyInterface.md#aggregate) | **POST** /v2/ontologies/{ontology}/interfaces/{interfaceType}/aggregate |
**Ontologies** | OntologyInterface | [**get**](docs/v2/namespaces/Ontologies/OntologyInterface.md#get) | **GET** /v2/ontologies/{ontology}/interfaceTypes/{interfaceType} |
**Ontologies** | OntologyInterface | [**list**](docs/v2/namespaces/Ontologies/OntologyInterface.md#list) | **GET** /v2/ontologies/{ontology}/interfaceTypes |
**Ontologies** | OntologyInterface | [**page**](docs/v2/namespaces/Ontologies/OntologyInterface.md#page) | **GET** /v2/ontologies/{ontology}/interfaceTypes |
**Ontologies** | OntologyObject | [**aggregate**](docs/v2/namespaces/Ontologies/OntologyObject.md#aggregate) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/aggregate |
**Ontologies** | OntologyObject | [**count**](docs/v2/namespaces/Ontologies/OntologyObject.md#count) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/count |
**Ontologies** | OntologyObject | [**get**](docs/v2/namespaces/Ontologies/OntologyObject.md#get) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey} |
**Ontologies** | OntologyObject | [**list**](docs/v2/namespaces/Ontologies/OntologyObject.md#list) | **GET** /v2/ontologies/{ontology}/objects/{objectType} |
**Ontologies** | OntologyObject | [**page**](docs/v2/namespaces/Ontologies/OntologyObject.md#page) | **GET** /v2/ontologies/{ontology}/objects/{objectType} |
**Ontologies** | OntologyObject | [**search**](docs/v2/namespaces/Ontologies/OntologyObject.md#search) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/search |
**Ontologies** | OntologyObjectSet | [**aggregate**](docs/v2/namespaces/Ontologies/OntologyObjectSet.md#aggregate) | **POST** /v2/ontologies/{ontology}/objectSets/aggregate |
**Ontologies** | OntologyObjectSet | [**create_temporary**](docs/v2/namespaces/Ontologies/OntologyObjectSet.md#create_temporary) | **POST** /v2/ontologies/{ontology}/objectSets/createTemporary |
**Ontologies** | OntologyObjectSet | [**get**](docs/v2/namespaces/Ontologies/OntologyObjectSet.md#get) | **GET** /v2/ontologies/{ontology}/objectSets/{objectSetRid} |
**Ontologies** | OntologyObjectSet | [**load**](docs/v2/namespaces/Ontologies/OntologyObjectSet.md#load) | **POST** /v2/ontologies/{ontology}/objectSets/loadObjects |
**Ontologies** | Query | [**execute**](docs/v2/namespaces/Ontologies/Query.md#execute) | **POST** /v2/ontologies/{ontology}/queries/{queryApiName}/execute |
**Ontologies** | QueryType | [**get**](docs/v2/namespaces/Ontologies/QueryType.md#get) | **GET** /v2/ontologies/{ontology}/queryTypes/{queryApiName} |
**Ontologies** | QueryType | [**list**](docs/v2/namespaces/Ontologies/QueryType.md#list) | **GET** /v2/ontologies/{ontology}/queryTypes |
**Ontologies** | QueryType | [**page**](docs/v2/namespaces/Ontologies/QueryType.md#page) | **GET** /v2/ontologies/{ontology}/queryTypes |
**Ontologies** | TimeSeriesPropertyV2 | [**get_first_point**](docs/v2/namespaces/Ontologies/TimeSeriesPropertyV2.md#get_first_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/firstPoint |
**Ontologies** | TimeSeriesPropertyV2 | [**get_last_point**](docs/v2/namespaces/Ontologies/TimeSeriesPropertyV2.md#get_last_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/lastPoint |
**Ontologies** | TimeSeriesPropertyV2 | [**stream_points**](docs/v2/namespaces/Ontologies/TimeSeriesPropertyV2.md#stream_points) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamPoints |
**Orchestration** | Build | [**create**](docs/v2/namespaces/Orchestration/Build.md#create) | **POST** /v2/orchestration/builds/create |
**Orchestration** | Build | [**get**](docs/v2/namespaces/Orchestration/Build.md#get) | **GET** /v2/orchestration/builds/{buildRid} |
**Orchestration** | Schedule | [**get**](docs/v2/namespaces/Orchestration/Schedule.md#get) | **GET** /v2/orchestration/schedules/{scheduleRid} |
**Orchestration** | Schedule | [**pause**](docs/v2/namespaces/Orchestration/Schedule.md#pause) | **POST** /v2/orchestration/schedules/{scheduleRid}/pause |
**Orchestration** | Schedule | [**run**](docs/v2/namespaces/Orchestration/Schedule.md#run) | **POST** /v2/orchestration/schedules/{scheduleRid}/run |
**Orchestration** | Schedule | [**unpause**](docs/v2/namespaces/Orchestration/Schedule.md#unpause) | **POST** /v2/orchestration/schedules/{scheduleRid}/unpause |
**ThirdPartyApplications** | ThirdPartyApplication | [**get**](docs/v2/namespaces/ThirdPartyApplications/ThirdPartyApplication.md#get) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid} |
**ThirdPartyApplications** | Version | [**delete**](docs/v2/namespaces/ThirdPartyApplications/Version.md#delete) | **DELETE** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion} |
**ThirdPartyApplications** | Version | [**get**](docs/v2/namespaces/ThirdPartyApplications/Version.md#get) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/{versionVersion} |
**ThirdPartyApplications** | Version | [**list**](docs/v2/namespaces/ThirdPartyApplications/Version.md#list) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions |
**ThirdPartyApplications** | Version | [**page**](docs/v2/namespaces/ThirdPartyApplications/Version.md#page) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions |
**ThirdPartyApplications** | Version | [**upload**](docs/v2/namespaces/ThirdPartyApplications/Version.md#upload) | **POST** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/versions/upload |
**ThirdPartyApplications** | Website | [**deploy**](docs/v2/namespaces/ThirdPartyApplications/Website.md#deploy) | **POST** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/deploy |
**ThirdPartyApplications** | Website | [**get**](docs/v2/namespaces/ThirdPartyApplications/Website.md#get) | **GET** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website |
**ThirdPartyApplications** | Website | [**undeploy**](docs/v2/namespaces/ThirdPartyApplications/Website.md#undeploy) | **POST** /v2/thirdPartyApplications/{thirdPartyApplicationRid}/website/undeploy |
<a id="apis-v1-link"></a>
## Documentation for V1 API endpoints

Namespace | Resource | Operation | HTTP request |
------------ | ------------- | ------------- | ------------- |
**Datasets** | Branch | [**create**](docs/v1/namespaces/Datasets/Branch.md#create) | **POST** /v1/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**delete**](docs/v1/namespaces/Datasets/Branch.md#delete) | **DELETE** /v1/datasets/{datasetRid}/branches/{branchId} |
**Datasets** | Branch | [**get**](docs/v1/namespaces/Datasets/Branch.md#get) | **GET** /v1/datasets/{datasetRid}/branches/{branchId} |
**Datasets** | Branch | [**list**](docs/v1/namespaces/Datasets/Branch.md#list) | **GET** /v1/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**page**](docs/v1/namespaces/Datasets/Branch.md#page) | **GET** /v1/datasets/{datasetRid}/branches |
**Datasets** | Dataset | [**create**](docs/v1/namespaces/Datasets/Dataset.md#create) | **POST** /v1/datasets |
**Datasets** | Dataset | [**delete_schema**](docs/v1/namespaces/Datasets/Dataset.md#delete_schema) | **DELETE** /v1/datasets/{datasetRid}/schema |
**Datasets** | Dataset | [**get**](docs/v1/namespaces/Datasets/Dataset.md#get) | **GET** /v1/datasets/{datasetRid} |
**Datasets** | Dataset | [**get_schema**](docs/v1/namespaces/Datasets/Dataset.md#get_schema) | **GET** /v1/datasets/{datasetRid}/schema |
**Datasets** | Dataset | [**read**](docs/v1/namespaces/Datasets/Dataset.md#read) | **GET** /v1/datasets/{datasetRid}/readTable |
**Datasets** | Dataset | [**replace_schema**](docs/v1/namespaces/Datasets/Dataset.md#replace_schema) | **PUT** /v1/datasets/{datasetRid}/schema |
**Datasets** | File | [**delete**](docs/v1/namespaces/Datasets/File.md#delete) | **DELETE** /v1/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**get**](docs/v1/namespaces/Datasets/File.md#get) | **GET** /v1/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**list**](docs/v1/namespaces/Datasets/File.md#list) | **GET** /v1/datasets/{datasetRid}/files |
**Datasets** | File | [**page**](docs/v1/namespaces/Datasets/File.md#page) | **GET** /v1/datasets/{datasetRid}/files |
**Datasets** | File | [**read**](docs/v1/namespaces/Datasets/File.md#read) | **GET** /v1/datasets/{datasetRid}/files/{filePath}/content |
**Datasets** | File | [**upload**](docs/v1/namespaces/Datasets/File.md#upload) | **POST** /v1/datasets/{datasetRid}/files:upload |
**Datasets** | Transaction | [**abort**](docs/v1/namespaces/Datasets/Transaction.md#abort) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/abort |
**Datasets** | Transaction | [**commit**](docs/v1/namespaces/Datasets/Transaction.md#commit) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/commit |
**Datasets** | Transaction | [**create**](docs/v1/namespaces/Datasets/Transaction.md#create) | **POST** /v1/datasets/{datasetRid}/transactions |
**Datasets** | Transaction | [**get**](docs/v1/namespaces/Datasets/Transaction.md#get) | **GET** /v1/datasets/{datasetRid}/transactions/{transactionRid} |
**Ontologies** | Action | [**apply**](docs/v1/namespaces/Ontologies/Action.md#apply) | **POST** /v1/ontologies/{ontologyRid}/actions/{actionType}/apply |
**Ontologies** | Action | [**apply_batch**](docs/v1/namespaces/Ontologies/Action.md#apply_batch) | **POST** /v1/ontologies/{ontologyRid}/actions/{actionType}/applyBatch |
**Ontologies** | Action | [**validate**](docs/v1/namespaces/Ontologies/Action.md#validate) | **POST** /v1/ontologies/{ontologyRid}/actions/{actionType}/validate |
**Ontologies** | ActionType | [**get**](docs/v1/namespaces/Ontologies/ActionType.md#get) | **GET** /v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName} |
**Ontologies** | ActionType | [**list**](docs/v1/namespaces/Ontologies/ActionType.md#list) | **GET** /v1/ontologies/{ontologyRid}/actionTypes |
**Ontologies** | ActionType | [**page**](docs/v1/namespaces/Ontologies/ActionType.md#page) | **GET** /v1/ontologies/{ontologyRid}/actionTypes |
**Ontologies** | ObjectType | [**get**](docs/v1/namespaces/Ontologies/ObjectType.md#get) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType} |
**Ontologies** | ObjectType | [**get_outgoing_link_type**](docs/v1/namespaces/Ontologies/ObjectType.md#get_outgoing_link_type) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
**Ontologies** | ObjectType | [**list**](docs/v1/namespaces/Ontologies/ObjectType.md#list) | **GET** /v1/ontologies/{ontologyRid}/objectTypes |
**Ontologies** | ObjectType | [**list_outgoing_link_types**](docs/v1/namespaces/Ontologies/ObjectType.md#list_outgoing_link_types) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | ObjectType | [**page**](docs/v1/namespaces/Ontologies/ObjectType.md#page) | **GET** /v1/ontologies/{ontologyRid}/objectTypes |
**Ontologies** | ObjectType | [**page_outgoing_link_types**](docs/v1/namespaces/Ontologies/ObjectType.md#page_outgoing_link_types) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | Ontology | [**get**](docs/v1/namespaces/Ontologies/Ontology.md#get) | **GET** /v1/ontologies/{ontologyRid} |
**Ontologies** | Ontology | [**list**](docs/v1/namespaces/Ontologies/Ontology.md#list) | **GET** /v1/ontologies |
**Ontologies** | OntologyObject | [**aggregate**](docs/v1/namespaces/Ontologies/OntologyObject.md#aggregate) | **POST** /v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate |
**Ontologies** | OntologyObject | [**get**](docs/v1/namespaces/Ontologies/OntologyObject.md#get) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey} |
**Ontologies** | OntologyObject | [**get_linked_object**](docs/v1/namespaces/Ontologies/OntologyObject.md#get_linked_object) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey} |
**Ontologies** | OntologyObject | [**list**](docs/v1/namespaces/Ontologies/OntologyObject.md#list) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType} |
**Ontologies** | OntologyObject | [**list_linked_objects**](docs/v1/namespaces/Ontologies/OntologyObject.md#list_linked_objects) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType} |
**Ontologies** | OntologyObject | [**page**](docs/v1/namespaces/Ontologies/OntologyObject.md#page) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType} |
**Ontologies** | OntologyObject | [**page_linked_objects**](docs/v1/namespaces/Ontologies/OntologyObject.md#page_linked_objects) | **GET** /v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType} |
**Ontologies** | OntologyObject | [**search**](docs/v1/namespaces/Ontologies/OntologyObject.md#search) | **POST** /v1/ontologies/{ontologyRid}/objects/{objectType}/search |
**Ontologies** | Query | [**execute**](docs/v1/namespaces/Ontologies/Query.md#execute) | **POST** /v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute |
**Ontologies** | QueryType | [**get**](docs/v1/namespaces/Ontologies/QueryType.md#get) | **GET** /v1/ontologies/{ontologyRid}/queryTypes/{queryApiName} |
**Ontologies** | QueryType | [**list**](docs/v1/namespaces/Ontologies/QueryType.md#list) | **GET** /v1/ontologies/{ontologyRid}/queryTypes |
**Ontologies** | QueryType | [**page**](docs/v1/namespaces/Ontologies/QueryType.md#page) | **GET** /v1/ontologies/{ontologyRid}/queryTypes |


<a id="models-link"></a>
<a id="models-v2-link"></a>
## Documentation for V2 models

- [AbortOnFailure](docs/v2/models/AbortOnFailure.md)
- [AbsoluteTimeRange](docs/v2/models/AbsoluteTimeRange.md)
- [AbsoluteTimeRangeDict](docs/v2/models/AbsoluteTimeRangeDict.md)
- [Action](docs/v2/models/Action.md)
- [ActionDict](docs/v2/models/ActionDict.md)
- [ActionMode](docs/v2/models/ActionMode.md)
- [ActionParameterArrayType](docs/v2/models/ActionParameterArrayType.md)
- [ActionParameterArrayTypeDict](docs/v2/models/ActionParameterArrayTypeDict.md)
- [ActionParameterType](docs/v2/models/ActionParameterType.md)
- [ActionParameterTypeDict](docs/v2/models/ActionParameterTypeDict.md)
- [ActionParameterV2](docs/v2/models/ActionParameterV2.md)
- [ActionParameterV2Dict](docs/v2/models/ActionParameterV2Dict.md)
- [ActionResults](docs/v2/models/ActionResults.md)
- [ActionResultsDict](docs/v2/models/ActionResultsDict.md)
- [ActionRid](docs/v2/models/ActionRid.md)
- [ActionType](docs/v2/models/ActionType.md)
- [ActionTypeApiName](docs/v2/models/ActionTypeApiName.md)
- [ActionTypeDict](docs/v2/models/ActionTypeDict.md)
- [ActionTypeRid](docs/v2/models/ActionTypeRid.md)
- [ActionTypeV2](docs/v2/models/ActionTypeV2.md)
- [ActionTypeV2Dict](docs/v2/models/ActionTypeV2Dict.md)
- [AddGroupMembersRequest](docs/v2/models/AddGroupMembersRequest.md)
- [AddGroupMembersRequestDict](docs/v2/models/AddGroupMembersRequestDict.md)
- [AddLink](docs/v2/models/AddLink.md)
- [AddLinkDict](docs/v2/models/AddLinkDict.md)
- [AddObject](docs/v2/models/AddObject.md)
- [AddObjectDict](docs/v2/models/AddObjectDict.md)
- [AggregateObjectSetRequestV2](docs/v2/models/AggregateObjectSetRequestV2.md)
- [AggregateObjectSetRequestV2Dict](docs/v2/models/AggregateObjectSetRequestV2Dict.md)
- [AggregateObjectsRequest](docs/v2/models/AggregateObjectsRequest.md)
- [AggregateObjectsRequestDict](docs/v2/models/AggregateObjectsRequestDict.md)
- [AggregateObjectsRequestV2](docs/v2/models/AggregateObjectsRequestV2.md)
- [AggregateObjectsRequestV2Dict](docs/v2/models/AggregateObjectsRequestV2Dict.md)
- [AggregateObjectsResponse](docs/v2/models/AggregateObjectsResponse.md)
- [AggregateObjectsResponseDict](docs/v2/models/AggregateObjectsResponseDict.md)
- [AggregateObjectsResponseItem](docs/v2/models/AggregateObjectsResponseItem.md)
- [AggregateObjectsResponseItemDict](docs/v2/models/AggregateObjectsResponseItemDict.md)
- [AggregateObjectsResponseItemV2](docs/v2/models/AggregateObjectsResponseItemV2.md)
- [AggregateObjectsResponseItemV2Dict](docs/v2/models/AggregateObjectsResponseItemV2Dict.md)
- [AggregateObjectsResponseV2](docs/v2/models/AggregateObjectsResponseV2.md)
- [AggregateObjectsResponseV2Dict](docs/v2/models/AggregateObjectsResponseV2Dict.md)
- [Aggregation](docs/v2/models/Aggregation.md)
- [AggregationAccuracy](docs/v2/models/AggregationAccuracy.md)
- [AggregationAccuracyRequest](docs/v2/models/AggregationAccuracyRequest.md)
- [AggregationDict](docs/v2/models/AggregationDict.md)
- [AggregationDurationGrouping](docs/v2/models/AggregationDurationGrouping.md)
- [AggregationDurationGroupingDict](docs/v2/models/AggregationDurationGroupingDict.md)
- [AggregationDurationGroupingV2](docs/v2/models/AggregationDurationGroupingV2.md)
- [AggregationDurationGroupingV2Dict](docs/v2/models/AggregationDurationGroupingV2Dict.md)
- [AggregationExactGrouping](docs/v2/models/AggregationExactGrouping.md)
- [AggregationExactGroupingDict](docs/v2/models/AggregationExactGroupingDict.md)
- [AggregationExactGroupingV2](docs/v2/models/AggregationExactGroupingV2.md)
- [AggregationExactGroupingV2Dict](docs/v2/models/AggregationExactGroupingV2Dict.md)
- [AggregationFixedWidthGrouping](docs/v2/models/AggregationFixedWidthGrouping.md)
- [AggregationFixedWidthGroupingDict](docs/v2/models/AggregationFixedWidthGroupingDict.md)
- [AggregationFixedWidthGroupingV2](docs/v2/models/AggregationFixedWidthGroupingV2.md)
- [AggregationFixedWidthGroupingV2Dict](docs/v2/models/AggregationFixedWidthGroupingV2Dict.md)
- [AggregationGroupBy](docs/v2/models/AggregationGroupBy.md)
- [AggregationGroupByDict](docs/v2/models/AggregationGroupByDict.md)
- [AggregationGroupByV2](docs/v2/models/AggregationGroupByV2.md)
- [AggregationGroupByV2Dict](docs/v2/models/AggregationGroupByV2Dict.md)
- [AggregationGroupKey](docs/v2/models/AggregationGroupKey.md)
- [AggregationGroupKeyV2](docs/v2/models/AggregationGroupKeyV2.md)
- [AggregationGroupValue](docs/v2/models/AggregationGroupValue.md)
- [AggregationGroupValueV2](docs/v2/models/AggregationGroupValueV2.md)
- [AggregationMetricName](docs/v2/models/AggregationMetricName.md)
- [AggregationMetricResult](docs/v2/models/AggregationMetricResult.md)
- [AggregationMetricResultDict](docs/v2/models/AggregationMetricResultDict.md)
- [AggregationMetricResultV2](docs/v2/models/AggregationMetricResultV2.md)
- [AggregationMetricResultV2Dict](docs/v2/models/AggregationMetricResultV2Dict.md)
- [AggregationObjectTypeGrouping](docs/v2/models/AggregationObjectTypeGrouping.md)
- [AggregationObjectTypeGroupingDict](docs/v2/models/AggregationObjectTypeGroupingDict.md)
- [AggregationOrderBy](docs/v2/models/AggregationOrderBy.md)
- [AggregationOrderByDict](docs/v2/models/AggregationOrderByDict.md)
- [AggregationRange](docs/v2/models/AggregationRange.md)
- [AggregationRangeDict](docs/v2/models/AggregationRangeDict.md)
- [AggregationRangesGrouping](docs/v2/models/AggregationRangesGrouping.md)
- [AggregationRangesGroupingDict](docs/v2/models/AggregationRangesGroupingDict.md)
- [AggregationRangesGroupingV2](docs/v2/models/AggregationRangesGroupingV2.md)
- [AggregationRangesGroupingV2Dict](docs/v2/models/AggregationRangesGroupingV2Dict.md)
- [AggregationRangeV2](docs/v2/models/AggregationRangeV2.md)
- [AggregationRangeV2Dict](docs/v2/models/AggregationRangeV2Dict.md)
- [AggregationV2](docs/v2/models/AggregationV2.md)
- [AggregationV2Dict](docs/v2/models/AggregationV2Dict.md)
- [AllTermsQuery](docs/v2/models/AllTermsQuery.md)
- [AllTermsQueryDict](docs/v2/models/AllTermsQueryDict.md)
- [AndQuery](docs/v2/models/AndQuery.md)
- [AndQueryDict](docs/v2/models/AndQueryDict.md)
- [AndQueryV2](docs/v2/models/AndQueryV2.md)
- [AndQueryV2Dict](docs/v2/models/AndQueryV2Dict.md)
- [AndTrigger](docs/v2/models/AndTrigger.md)
- [AndTriggerDict](docs/v2/models/AndTriggerDict.md)
- [AnyTermQuery](docs/v2/models/AnyTermQuery.md)
- [AnyTermQueryDict](docs/v2/models/AnyTermQueryDict.md)
- [AnyType](docs/v2/models/AnyType.md)
- [AnyTypeDict](docs/v2/models/AnyTypeDict.md)
- [ApiDefinition](docs/v2/models/ApiDefinition.md)
- [ApiDefinitionDeprecated](docs/v2/models/ApiDefinitionDeprecated.md)
- [ApiDefinitionDict](docs/v2/models/ApiDefinitionDict.md)
- [ApiDefinitionName](docs/v2/models/ApiDefinitionName.md)
- [ApiDefinitionRid](docs/v2/models/ApiDefinitionRid.md)
- [ApplyActionMode](docs/v2/models/ApplyActionMode.md)
- [ApplyActionRequest](docs/v2/models/ApplyActionRequest.md)
- [ApplyActionRequestDict](docs/v2/models/ApplyActionRequestDict.md)
- [ApplyActionRequestOptions](docs/v2/models/ApplyActionRequestOptions.md)
- [ApplyActionRequestOptionsDict](docs/v2/models/ApplyActionRequestOptionsDict.md)
- [ApplyActionRequestV2](docs/v2/models/ApplyActionRequestV2.md)
- [ApplyActionRequestV2Dict](docs/v2/models/ApplyActionRequestV2Dict.md)
- [ApplyActionResponse](docs/v2/models/ApplyActionResponse.md)
- [ApplyActionResponseDict](docs/v2/models/ApplyActionResponseDict.md)
- [ApproximateDistinctAggregation](docs/v2/models/ApproximateDistinctAggregation.md)
- [ApproximateDistinctAggregationDict](docs/v2/models/ApproximateDistinctAggregationDict.md)
- [ApproximateDistinctAggregationV2](docs/v2/models/ApproximateDistinctAggregationV2.md)
- [ApproximateDistinctAggregationV2Dict](docs/v2/models/ApproximateDistinctAggregationV2Dict.md)
- [ApproximatePercentileAggregationV2](docs/v2/models/ApproximatePercentileAggregationV2.md)
- [ApproximatePercentileAggregationV2Dict](docs/v2/models/ApproximatePercentileAggregationV2Dict.md)
- [ArchiveFileFormat](docs/v2/models/ArchiveFileFormat.md)
- [Arg](docs/v2/models/Arg.md)
- [ArgDict](docs/v2/models/ArgDict.md)
- [ArraySizeConstraint](docs/v2/models/ArraySizeConstraint.md)
- [ArraySizeConstraintDict](docs/v2/models/ArraySizeConstraintDict.md)
- [ArtifactRepositoryRid](docs/v2/models/ArtifactRepositoryRid.md)
- [AsyncActionStatus](docs/v2/models/AsyncActionStatus.md)
- [AsyncApplyActionOperationResponseV2](docs/v2/models/AsyncApplyActionOperationResponseV2.md)
- [AsyncApplyActionOperationResponseV2Dict](docs/v2/models/AsyncApplyActionOperationResponseV2Dict.md)
- [AsyncApplyActionRequest](docs/v2/models/AsyncApplyActionRequest.md)
- [AsyncApplyActionRequestDict](docs/v2/models/AsyncApplyActionRequestDict.md)
- [AsyncApplyActionRequestV2](docs/v2/models/AsyncApplyActionRequestV2.md)
- [AsyncApplyActionRequestV2Dict](docs/v2/models/AsyncApplyActionRequestV2Dict.md)
- [AsyncApplyActionResponse](docs/v2/models/AsyncApplyActionResponse.md)
- [AsyncApplyActionResponseDict](docs/v2/models/AsyncApplyActionResponseDict.md)
- [AsyncApplyActionResponseV2](docs/v2/models/AsyncApplyActionResponseV2.md)
- [AsyncApplyActionResponseV2Dict](docs/v2/models/AsyncApplyActionResponseV2Dict.md)
- [Attachment](docs/v2/models/Attachment.md)
- [AttachmentDict](docs/v2/models/AttachmentDict.md)
- [AttachmentMetadataResponse](docs/v2/models/AttachmentMetadataResponse.md)
- [AttachmentMetadataResponseDict](docs/v2/models/AttachmentMetadataResponseDict.md)
- [AttachmentProperty](docs/v2/models/AttachmentProperty.md)
- [AttachmentPropertyDict](docs/v2/models/AttachmentPropertyDict.md)
- [AttachmentRid](docs/v2/models/AttachmentRid.md)
- [AttachmentType](docs/v2/models/AttachmentType.md)
- [AttachmentTypeDict](docs/v2/models/AttachmentTypeDict.md)
- [AttachmentV2](docs/v2/models/AttachmentV2.md)
- [AttachmentV2Dict](docs/v2/models/AttachmentV2Dict.md)
- [AttributeName](docs/v2/models/AttributeName.md)
- [AttributeValue](docs/v2/models/AttributeValue.md)
- [AttributeValues](docs/v2/models/AttributeValues.md)
- [AvgAggregation](docs/v2/models/AvgAggregation.md)
- [AvgAggregationDict](docs/v2/models/AvgAggregationDict.md)
- [AvgAggregationV2](docs/v2/models/AvgAggregationV2.md)
- [AvgAggregationV2Dict](docs/v2/models/AvgAggregationV2Dict.md)
- [BatchApplyActionRequest](docs/v2/models/BatchApplyActionRequest.md)
- [BatchApplyActionRequestDict](docs/v2/models/BatchApplyActionRequestDict.md)
- [BatchApplyActionRequestItem](docs/v2/models/BatchApplyActionRequestItem.md)
- [BatchApplyActionRequestItemDict](docs/v2/models/BatchApplyActionRequestItemDict.md)
- [BatchApplyActionRequestOptions](docs/v2/models/BatchApplyActionRequestOptions.md)
- [BatchApplyActionRequestOptionsDict](docs/v2/models/BatchApplyActionRequestOptionsDict.md)
- [BatchApplyActionRequestV2](docs/v2/models/BatchApplyActionRequestV2.md)
- [BatchApplyActionRequestV2Dict](docs/v2/models/BatchApplyActionRequestV2Dict.md)
- [BatchApplyActionResponse](docs/v2/models/BatchApplyActionResponse.md)
- [BatchApplyActionResponseDict](docs/v2/models/BatchApplyActionResponseDict.md)
- [BatchApplyActionResponseV2](docs/v2/models/BatchApplyActionResponseV2.md)
- [BatchApplyActionResponseV2Dict](docs/v2/models/BatchApplyActionResponseV2Dict.md)
- [BBox](docs/v2/models/BBox.md)
- [BinaryType](docs/v2/models/BinaryType.md)
- [BinaryTypeDict](docs/v2/models/BinaryTypeDict.md)
- [BlueprintIcon](docs/v2/models/BlueprintIcon.md)
- [BlueprintIconDict](docs/v2/models/BlueprintIconDict.md)
- [BooleanType](docs/v2/models/BooleanType.md)
- [BooleanTypeDict](docs/v2/models/BooleanTypeDict.md)
- [BoundingBoxValue](docs/v2/models/BoundingBoxValue.md)
- [BoundingBoxValueDict](docs/v2/models/BoundingBoxValueDict.md)
- [Branch](docs/v2/models/Branch.md)
- [BranchDict](docs/v2/models/BranchDict.md)
- [BranchId](docs/v2/models/BranchId.md)
- [BranchName](docs/v2/models/BranchName.md)
- [Build](docs/v2/models/Build.md)
- [BuildDict](docs/v2/models/BuildDict.md)
- [BuildRid](docs/v2/models/BuildRid.md)
- [BuildStatus](docs/v2/models/BuildStatus.md)
- [BuildTarget](docs/v2/models/BuildTarget.md)
- [BuildTargetDict](docs/v2/models/BuildTargetDict.md)
- [ByteType](docs/v2/models/ByteType.md)
- [ByteTypeDict](docs/v2/models/ByteTypeDict.md)
- [CenterPoint](docs/v2/models/CenterPoint.md)
- [CenterPointDict](docs/v2/models/CenterPointDict.md)
- [CenterPointTypes](docs/v2/models/CenterPointTypes.md)
- [CenterPointTypesDict](docs/v2/models/CenterPointTypesDict.md)
- [ConnectingTarget](docs/v2/models/ConnectingTarget.md)
- [ConnectingTargetDict](docs/v2/models/ConnectingTargetDict.md)
- [ContainsAllTermsInOrderPrefixLastTerm](docs/v2/models/ContainsAllTermsInOrderPrefixLastTerm.md)
- [ContainsAllTermsInOrderPrefixLastTermDict](docs/v2/models/ContainsAllTermsInOrderPrefixLastTermDict.md)
- [ContainsAllTermsInOrderQuery](docs/v2/models/ContainsAllTermsInOrderQuery.md)
- [ContainsAllTermsInOrderQueryDict](docs/v2/models/ContainsAllTermsInOrderQueryDict.md)
- [ContainsAllTermsQuery](docs/v2/models/ContainsAllTermsQuery.md)
- [ContainsAllTermsQueryDict](docs/v2/models/ContainsAllTermsQueryDict.md)
- [ContainsAnyTermQuery](docs/v2/models/ContainsAnyTermQuery.md)
- [ContainsAnyTermQueryDict](docs/v2/models/ContainsAnyTermQueryDict.md)
- [ContainsQuery](docs/v2/models/ContainsQuery.md)
- [ContainsQueryDict](docs/v2/models/ContainsQueryDict.md)
- [ContainsQueryV2](docs/v2/models/ContainsQueryV2.md)
- [ContainsQueryV2Dict](docs/v2/models/ContainsQueryV2Dict.md)
- [ContentLength](docs/v2/models/ContentLength.md)
- [ContentType](docs/v2/models/ContentType.md)
- [Coordinate](docs/v2/models/Coordinate.md)
- [CountAggregation](docs/v2/models/CountAggregation.md)
- [CountAggregationDict](docs/v2/models/CountAggregationDict.md)
- [CountAggregationV2](docs/v2/models/CountAggregationV2.md)
- [CountAggregationV2Dict](docs/v2/models/CountAggregationV2Dict.md)
- [CountObjectsResponseV2](docs/v2/models/CountObjectsResponseV2.md)
- [CountObjectsResponseV2Dict](docs/v2/models/CountObjectsResponseV2Dict.md)
- [CreateBranchRequest](docs/v2/models/CreateBranchRequest.md)
- [CreateBranchRequestDict](docs/v2/models/CreateBranchRequestDict.md)
- [CreateBuildsRequest](docs/v2/models/CreateBuildsRequest.md)
- [CreateBuildsRequestDict](docs/v2/models/CreateBuildsRequestDict.md)
- [CreateDatasetRequest](docs/v2/models/CreateDatasetRequest.md)
- [CreateDatasetRequestDict](docs/v2/models/CreateDatasetRequestDict.md)
- [CreatedBy](docs/v2/models/CreatedBy.md)
- [CreatedTime](docs/v2/models/CreatedTime.md)
- [CreateGroupRequest](docs/v2/models/CreateGroupRequest.md)
- [CreateGroupRequestDict](docs/v2/models/CreateGroupRequestDict.md)
- [CreateLinkRule](docs/v2/models/CreateLinkRule.md)
- [CreateLinkRuleDict](docs/v2/models/CreateLinkRuleDict.md)
- [CreateObjectRule](docs/v2/models/CreateObjectRule.md)
- [CreateObjectRuleDict](docs/v2/models/CreateObjectRuleDict.md)
- [CreateTemporaryObjectSetRequestV2](docs/v2/models/CreateTemporaryObjectSetRequestV2.md)
- [CreateTemporaryObjectSetRequestV2Dict](docs/v2/models/CreateTemporaryObjectSetRequestV2Dict.md)
- [CreateTemporaryObjectSetResponseV2](docs/v2/models/CreateTemporaryObjectSetResponseV2.md)
- [CreateTemporaryObjectSetResponseV2Dict](docs/v2/models/CreateTemporaryObjectSetResponseV2Dict.md)
- [CreateTransactionRequest](docs/v2/models/CreateTransactionRequest.md)
- [CreateTransactionRequestDict](docs/v2/models/CreateTransactionRequestDict.md)
- [CronExpression](docs/v2/models/CronExpression.md)
- [CustomTypeId](docs/v2/models/CustomTypeId.md)
- [Dataset](docs/v2/models/Dataset.md)
- [DatasetDict](docs/v2/models/DatasetDict.md)
- [DatasetName](docs/v2/models/DatasetName.md)
- [DatasetRid](docs/v2/models/DatasetRid.md)
- [DatasetUpdatedTrigger](docs/v2/models/DatasetUpdatedTrigger.md)
- [DatasetUpdatedTriggerDict](docs/v2/models/DatasetUpdatedTriggerDict.md)
- [DataValue](docs/v2/models/DataValue.md)
- [DateType](docs/v2/models/DateType.md)
- [DateTypeDict](docs/v2/models/DateTypeDict.md)
- [DecimalType](docs/v2/models/DecimalType.md)
- [DecimalTypeDict](docs/v2/models/DecimalTypeDict.md)
- [DeleteLinkRule](docs/v2/models/DeleteLinkRule.md)
- [DeleteLinkRuleDict](docs/v2/models/DeleteLinkRuleDict.md)
- [DeleteObjectRule](docs/v2/models/DeleteObjectRule.md)
- [DeleteObjectRuleDict](docs/v2/models/DeleteObjectRuleDict.md)
- [DeployWebsiteRequest](docs/v2/models/DeployWebsiteRequest.md)
- [DeployWebsiteRequestDict](docs/v2/models/DeployWebsiteRequestDict.md)
- [DisplayName](docs/v2/models/DisplayName.md)
- [Distance](docs/v2/models/Distance.md)
- [DistanceDict](docs/v2/models/DistanceDict.md)
- [DistanceUnit](docs/v2/models/DistanceUnit.md)
- [DoesNotIntersectBoundingBoxQuery](docs/v2/models/DoesNotIntersectBoundingBoxQuery.md)
- [DoesNotIntersectBoundingBoxQueryDict](docs/v2/models/DoesNotIntersectBoundingBoxQueryDict.md)
- [DoesNotIntersectPolygonQuery](docs/v2/models/DoesNotIntersectPolygonQuery.md)
- [DoesNotIntersectPolygonQueryDict](docs/v2/models/DoesNotIntersectPolygonQueryDict.md)
- [DoubleType](docs/v2/models/DoubleType.md)
- [DoubleTypeDict](docs/v2/models/DoubleTypeDict.md)
- [Duration](docs/v2/models/Duration.md)
- [DurationDict](docs/v2/models/DurationDict.md)
- [EqualsQuery](docs/v2/models/EqualsQuery.md)
- [EqualsQueryDict](docs/v2/models/EqualsQueryDict.md)
- [EqualsQueryV2](docs/v2/models/EqualsQueryV2.md)
- [EqualsQueryV2Dict](docs/v2/models/EqualsQueryV2Dict.md)
- [Error](docs/v2/models/Error.md)
- [ErrorDict](docs/v2/models/ErrorDict.md)
- [ErrorName](docs/v2/models/ErrorName.md)
- [ExactDistinctAggregationV2](docs/v2/models/ExactDistinctAggregationV2.md)
- [ExactDistinctAggregationV2Dict](docs/v2/models/ExactDistinctAggregationV2Dict.md)
- [ExecuteQueryRequest](docs/v2/models/ExecuteQueryRequest.md)
- [ExecuteQueryRequestDict](docs/v2/models/ExecuteQueryRequestDict.md)
- [ExecuteQueryResponse](docs/v2/models/ExecuteQueryResponse.md)
- [ExecuteQueryResponseDict](docs/v2/models/ExecuteQueryResponseDict.md)
- [FallbackBranches](docs/v2/models/FallbackBranches.md)
- [Feature](docs/v2/models/Feature.md)
- [FeatureCollection](docs/v2/models/FeatureCollection.md)
- [FeatureCollectionDict](docs/v2/models/FeatureCollectionDict.md)
- [FeatureCollectionTypes](docs/v2/models/FeatureCollectionTypes.md)
- [FeatureCollectionTypesDict](docs/v2/models/FeatureCollectionTypesDict.md)
- [FeatureDict](docs/v2/models/FeatureDict.md)
- [FeaturePropertyKey](docs/v2/models/FeaturePropertyKey.md)
- [FieldNameV1](docs/v2/models/FieldNameV1.md)
- [File](docs/v2/models/File.md)
- [FileDict](docs/v2/models/FileDict.md)
- [Filename](docs/v2/models/Filename.md)
- [FilePath](docs/v2/models/FilePath.md)
- [FilesystemResource](docs/v2/models/FilesystemResource.md)
- [FilesystemResourceDict](docs/v2/models/FilesystemResourceDict.md)
- [FileUpdatedTime](docs/v2/models/FileUpdatedTime.md)
- [FilterValue](docs/v2/models/FilterValue.md)
- [FloatType](docs/v2/models/FloatType.md)
- [FloatTypeDict](docs/v2/models/FloatTypeDict.md)
- [Folder](docs/v2/models/Folder.md)
- [FolderDict](docs/v2/models/FolderDict.md)
- [FolderRid](docs/v2/models/FolderRid.md)
- [ForceBuild](docs/v2/models/ForceBuild.md)
- [FunctionRid](docs/v2/models/FunctionRid.md)
- [FunctionVersion](docs/v2/models/FunctionVersion.md)
- [Fuzzy](docs/v2/models/Fuzzy.md)
- [FuzzyV2](docs/v2/models/FuzzyV2.md)
- [GeoJsonObject](docs/v2/models/GeoJsonObject.md)
- [GeoJsonObjectDict](docs/v2/models/GeoJsonObjectDict.md)
- [Geometry](docs/v2/models/Geometry.md)
- [GeometryCollection](docs/v2/models/GeometryCollection.md)
- [GeometryCollectionDict](docs/v2/models/GeometryCollectionDict.md)
- [GeometryDict](docs/v2/models/GeometryDict.md)
- [GeoPoint](docs/v2/models/GeoPoint.md)
- [GeoPointDict](docs/v2/models/GeoPointDict.md)
- [GeoPointType](docs/v2/models/GeoPointType.md)
- [GeoPointTypeDict](docs/v2/models/GeoPointTypeDict.md)
- [GeoShapeType](docs/v2/models/GeoShapeType.md)
- [GeoShapeTypeDict](docs/v2/models/GeoShapeTypeDict.md)
- [GeotimeSeriesValue](docs/v2/models/GeotimeSeriesValue.md)
- [GeotimeSeriesValueDict](docs/v2/models/GeotimeSeriesValueDict.md)
- [GetGroupsBatchRequestElement](docs/v2/models/GetGroupsBatchRequestElement.md)
- [GetGroupsBatchRequestElementDict](docs/v2/models/GetGroupsBatchRequestElementDict.md)
- [GetGroupsBatchResponse](docs/v2/models/GetGroupsBatchResponse.md)
- [GetGroupsBatchResponseDict](docs/v2/models/GetGroupsBatchResponseDict.md)
- [GetUsersBatchRequestElement](docs/v2/models/GetUsersBatchRequestElement.md)
- [GetUsersBatchRequestElementDict](docs/v2/models/GetUsersBatchRequestElementDict.md)
- [GetUsersBatchResponse](docs/v2/models/GetUsersBatchResponse.md)
- [GetUsersBatchResponseDict](docs/v2/models/GetUsersBatchResponseDict.md)
- [Group](docs/v2/models/Group.md)
- [GroupDict](docs/v2/models/GroupDict.md)
- [GroupMember](docs/v2/models/GroupMember.md)
- [GroupMemberConstraint](docs/v2/models/GroupMemberConstraint.md)
- [GroupMemberConstraintDict](docs/v2/models/GroupMemberConstraintDict.md)
- [GroupMemberDict](docs/v2/models/GroupMemberDict.md)
- [GroupMembership](docs/v2/models/GroupMembership.md)
- [GroupMembershipDict](docs/v2/models/GroupMembershipDict.md)
- [GroupMembershipExpiration](docs/v2/models/GroupMembershipExpiration.md)
- [GroupName](docs/v2/models/GroupName.md)
- [GroupSearchFilter](docs/v2/models/GroupSearchFilter.md)
- [GroupSearchFilterDict](docs/v2/models/GroupSearchFilterDict.md)
- [GteQuery](docs/v2/models/GteQuery.md)
- [GteQueryDict](docs/v2/models/GteQueryDict.md)
- [GteQueryV2](docs/v2/models/GteQueryV2.md)
- [GteQueryV2Dict](docs/v2/models/GteQueryV2Dict.md)
- [GtQuery](docs/v2/models/GtQuery.md)
- [GtQueryDict](docs/v2/models/GtQueryDict.md)
- [GtQueryV2](docs/v2/models/GtQueryV2.md)
- [GtQueryV2Dict](docs/v2/models/GtQueryV2Dict.md)
- [Icon](docs/v2/models/Icon.md)
- [IconDict](docs/v2/models/IconDict.md)
- [IntegerType](docs/v2/models/IntegerType.md)
- [IntegerTypeDict](docs/v2/models/IntegerTypeDict.md)
- [InterfaceLinkType](docs/v2/models/InterfaceLinkType.md)
- [InterfaceLinkTypeApiName](docs/v2/models/InterfaceLinkTypeApiName.md)
- [InterfaceLinkTypeCardinality](docs/v2/models/InterfaceLinkTypeCardinality.md)
- [InterfaceLinkTypeDict](docs/v2/models/InterfaceLinkTypeDict.md)
- [InterfaceLinkTypeLinkedEntityApiName](docs/v2/models/InterfaceLinkTypeLinkedEntityApiName.md)
- [InterfaceLinkTypeLinkedEntityApiNameDict](docs/v2/models/InterfaceLinkTypeLinkedEntityApiNameDict.md)
- [InterfaceLinkTypeRid](docs/v2/models/InterfaceLinkTypeRid.md)
- [InterfaceType](docs/v2/models/InterfaceType.md)
- [InterfaceTypeApiName](docs/v2/models/InterfaceTypeApiName.md)
- [InterfaceTypeDict](docs/v2/models/InterfaceTypeDict.md)
- [InterfaceTypeRid](docs/v2/models/InterfaceTypeRid.md)
- [IntersectsBoundingBoxQuery](docs/v2/models/IntersectsBoundingBoxQuery.md)
- [IntersectsBoundingBoxQueryDict](docs/v2/models/IntersectsBoundingBoxQueryDict.md)
- [IntersectsPolygonQuery](docs/v2/models/IntersectsPolygonQuery.md)
- [IntersectsPolygonQueryDict](docs/v2/models/IntersectsPolygonQueryDict.md)
- [IrVersion](docs/v2/models/IrVersion.md)
- [IsNullQuery](docs/v2/models/IsNullQuery.md)
- [IsNullQueryDict](docs/v2/models/IsNullQueryDict.md)
- [IsNullQueryV2](docs/v2/models/IsNullQueryV2.md)
- [IsNullQueryV2Dict](docs/v2/models/IsNullQueryV2Dict.md)
- [JobSucceededTrigger](docs/v2/models/JobSucceededTrigger.md)
- [JobSucceededTriggerDict](docs/v2/models/JobSucceededTriggerDict.md)
- [LinearRing](docs/v2/models/LinearRing.md)
- [LineString](docs/v2/models/LineString.md)
- [LineStringCoordinates](docs/v2/models/LineStringCoordinates.md)
- [LineStringDict](docs/v2/models/LineStringDict.md)
- [LinkedInterfaceTypeApiName](docs/v2/models/LinkedInterfaceTypeApiName.md)
- [LinkedInterfaceTypeApiNameDict](docs/v2/models/LinkedInterfaceTypeApiNameDict.md)
- [LinkedObjectTypeApiName](docs/v2/models/LinkedObjectTypeApiName.md)
- [LinkedObjectTypeApiNameDict](docs/v2/models/LinkedObjectTypeApiNameDict.md)
- [LinkSideObject](docs/v2/models/LinkSideObject.md)
- [LinkSideObjectDict](docs/v2/models/LinkSideObjectDict.md)
- [LinkTypeApiName](docs/v2/models/LinkTypeApiName.md)
- [LinkTypeRid](docs/v2/models/LinkTypeRid.md)
- [LinkTypeSide](docs/v2/models/LinkTypeSide.md)
- [LinkTypeSideCardinality](docs/v2/models/LinkTypeSideCardinality.md)
- [LinkTypeSideDict](docs/v2/models/LinkTypeSideDict.md)
- [LinkTypeSideV2](docs/v2/models/LinkTypeSideV2.md)
- [LinkTypeSideV2Dict](docs/v2/models/LinkTypeSideV2Dict.md)
- [ListActionTypesResponse](docs/v2/models/ListActionTypesResponse.md)
- [ListActionTypesResponseDict](docs/v2/models/ListActionTypesResponseDict.md)
- [ListActionTypesResponseV2](docs/v2/models/ListActionTypesResponseV2.md)
- [ListActionTypesResponseV2Dict](docs/v2/models/ListActionTypesResponseV2Dict.md)
- [ListAttachmentsResponseV2](docs/v2/models/ListAttachmentsResponseV2.md)
- [ListAttachmentsResponseV2Dict](docs/v2/models/ListAttachmentsResponseV2Dict.md)
- [ListBranchesResponse](docs/v2/models/ListBranchesResponse.md)
- [ListBranchesResponseDict](docs/v2/models/ListBranchesResponseDict.md)
- [ListFilesResponse](docs/v2/models/ListFilesResponse.md)
- [ListFilesResponseDict](docs/v2/models/ListFilesResponseDict.md)
- [ListGroupMembershipsResponse](docs/v2/models/ListGroupMembershipsResponse.md)
- [ListGroupMembershipsResponseDict](docs/v2/models/ListGroupMembershipsResponseDict.md)
- [ListGroupMembersResponse](docs/v2/models/ListGroupMembersResponse.md)
- [ListGroupMembersResponseDict](docs/v2/models/ListGroupMembersResponseDict.md)
- [ListGroupsResponse](docs/v2/models/ListGroupsResponse.md)
- [ListGroupsResponseDict](docs/v2/models/ListGroupsResponseDict.md)
- [ListInterfaceTypesResponse](docs/v2/models/ListInterfaceTypesResponse.md)
- [ListInterfaceTypesResponseDict](docs/v2/models/ListInterfaceTypesResponseDict.md)
- [ListLinkedObjectsResponse](docs/v2/models/ListLinkedObjectsResponse.md)
- [ListLinkedObjectsResponseDict](docs/v2/models/ListLinkedObjectsResponseDict.md)
- [ListLinkedObjectsResponseV2](docs/v2/models/ListLinkedObjectsResponseV2.md)
- [ListLinkedObjectsResponseV2Dict](docs/v2/models/ListLinkedObjectsResponseV2Dict.md)
- [ListObjectsResponse](docs/v2/models/ListObjectsResponse.md)
- [ListObjectsResponseDict](docs/v2/models/ListObjectsResponseDict.md)
- [ListObjectsResponseV2](docs/v2/models/ListObjectsResponseV2.md)
- [ListObjectsResponseV2Dict](docs/v2/models/ListObjectsResponseV2Dict.md)
- [ListObjectTypesResponse](docs/v2/models/ListObjectTypesResponse.md)
- [ListObjectTypesResponseDict](docs/v2/models/ListObjectTypesResponseDict.md)
- [ListObjectTypesV2Response](docs/v2/models/ListObjectTypesV2Response.md)
- [ListObjectTypesV2ResponseDict](docs/v2/models/ListObjectTypesV2ResponseDict.md)
- [ListOntologiesResponse](docs/v2/models/ListOntologiesResponse.md)
- [ListOntologiesResponseDict](docs/v2/models/ListOntologiesResponseDict.md)
- [ListOntologiesV2Response](docs/v2/models/ListOntologiesV2Response.md)
- [ListOntologiesV2ResponseDict](docs/v2/models/ListOntologiesV2ResponseDict.md)
- [ListOutgoingLinkTypesResponse](docs/v2/models/ListOutgoingLinkTypesResponse.md)
- [ListOutgoingLinkTypesResponseDict](docs/v2/models/ListOutgoingLinkTypesResponseDict.md)
- [ListOutgoingLinkTypesResponseV2](docs/v2/models/ListOutgoingLinkTypesResponseV2.md)
- [ListOutgoingLinkTypesResponseV2Dict](docs/v2/models/ListOutgoingLinkTypesResponseV2Dict.md)
- [ListQueryTypesResponse](docs/v2/models/ListQueryTypesResponse.md)
- [ListQueryTypesResponseDict](docs/v2/models/ListQueryTypesResponseDict.md)
- [ListQueryTypesResponseV2](docs/v2/models/ListQueryTypesResponseV2.md)
- [ListQueryTypesResponseV2Dict](docs/v2/models/ListQueryTypesResponseV2Dict.md)
- [ListUsersResponse](docs/v2/models/ListUsersResponse.md)
- [ListUsersResponseDict](docs/v2/models/ListUsersResponseDict.md)
- [ListVersionsResponse](docs/v2/models/ListVersionsResponse.md)
- [ListVersionsResponseDict](docs/v2/models/ListVersionsResponseDict.md)
- [LoadObjectSetRequestV2](docs/v2/models/LoadObjectSetRequestV2.md)
- [LoadObjectSetRequestV2Dict](docs/v2/models/LoadObjectSetRequestV2Dict.md)
- [LoadObjectSetResponseV2](docs/v2/models/LoadObjectSetResponseV2.md)
- [LoadObjectSetResponseV2Dict](docs/v2/models/LoadObjectSetResponseV2Dict.md)
- [LocalFilePath](docs/v2/models/LocalFilePath.md)
- [LocalFilePathDict](docs/v2/models/LocalFilePathDict.md)
- [LogicRule](docs/v2/models/LogicRule.md)
- [LogicRuleDict](docs/v2/models/LogicRuleDict.md)
- [LongType](docs/v2/models/LongType.md)
- [LongTypeDict](docs/v2/models/LongTypeDict.md)
- [LteQuery](docs/v2/models/LteQuery.md)
- [LteQueryDict](docs/v2/models/LteQueryDict.md)
- [LteQueryV2](docs/v2/models/LteQueryV2.md)
- [LteQueryV2Dict](docs/v2/models/LteQueryV2Dict.md)
- [LtQuery](docs/v2/models/LtQuery.md)
- [LtQueryDict](docs/v2/models/LtQueryDict.md)
- [LtQueryV2](docs/v2/models/LtQueryV2.md)
- [LtQueryV2Dict](docs/v2/models/LtQueryV2Dict.md)
- [ManualTarget](docs/v2/models/ManualTarget.md)
- [ManualTargetDict](docs/v2/models/ManualTargetDict.md)
- [MarkingType](docs/v2/models/MarkingType.md)
- [MarkingTypeDict](docs/v2/models/MarkingTypeDict.md)
- [MaxAggregation](docs/v2/models/MaxAggregation.md)
- [MaxAggregationDict](docs/v2/models/MaxAggregationDict.md)
- [MaxAggregationV2](docs/v2/models/MaxAggregationV2.md)
- [MaxAggregationV2Dict](docs/v2/models/MaxAggregationV2Dict.md)
- [MediaSetRid](docs/v2/models/MediaSetRid.md)
- [MediaSetUpdatedTrigger](docs/v2/models/MediaSetUpdatedTrigger.md)
- [MediaSetUpdatedTriggerDict](docs/v2/models/MediaSetUpdatedTriggerDict.md)
- [MediaType](docs/v2/models/MediaType.md)
- [MinAggregation](docs/v2/models/MinAggregation.md)
- [MinAggregationDict](docs/v2/models/MinAggregationDict.md)
- [MinAggregationV2](docs/v2/models/MinAggregationV2.md)
- [MinAggregationV2Dict](docs/v2/models/MinAggregationV2Dict.md)
- [ModifyObject](docs/v2/models/ModifyObject.md)
- [ModifyObjectDict](docs/v2/models/ModifyObjectDict.md)
- [ModifyObjectRule](docs/v2/models/ModifyObjectRule.md)
- [ModifyObjectRuleDict](docs/v2/models/ModifyObjectRuleDict.md)
- [MultiLineString](docs/v2/models/MultiLineString.md)
- [MultiLineStringDict](docs/v2/models/MultiLineStringDict.md)
- [MultiPoint](docs/v2/models/MultiPoint.md)
- [MultiPointDict](docs/v2/models/MultiPointDict.md)
- [MultiPolygon](docs/v2/models/MultiPolygon.md)
- [MultiPolygonDict](docs/v2/models/MultiPolygonDict.md)
- [NestedQueryAggregation](docs/v2/models/NestedQueryAggregation.md)
- [NestedQueryAggregationDict](docs/v2/models/NestedQueryAggregationDict.md)
- [NewLogicTrigger](docs/v2/models/NewLogicTrigger.md)
- [NewLogicTriggerDict](docs/v2/models/NewLogicTriggerDict.md)
- [NotificationsEnabled](docs/v2/models/NotificationsEnabled.md)
- [NotQuery](docs/v2/models/NotQuery.md)
- [NotQueryDict](docs/v2/models/NotQueryDict.md)
- [NotQueryV2](docs/v2/models/NotQueryV2.md)
- [NotQueryV2Dict](docs/v2/models/NotQueryV2Dict.md)
- [NullType](docs/v2/models/NullType.md)
- [NullTypeDict](docs/v2/models/NullTypeDict.md)
- [ObjectEdit](docs/v2/models/ObjectEdit.md)
- [ObjectEditDict](docs/v2/models/ObjectEditDict.md)
- [ObjectEdits](docs/v2/models/ObjectEdits.md)
- [ObjectEditsDict](docs/v2/models/ObjectEditsDict.md)
- [ObjectPrimaryKey](docs/v2/models/ObjectPrimaryKey.md)
- [ObjectPropertyType](docs/v2/models/ObjectPropertyType.md)
- [ObjectPropertyTypeDict](docs/v2/models/ObjectPropertyTypeDict.md)
- [ObjectPropertyValueConstraint](docs/v2/models/ObjectPropertyValueConstraint.md)
- [ObjectPropertyValueConstraintDict](docs/v2/models/ObjectPropertyValueConstraintDict.md)
- [ObjectQueryResultConstraint](docs/v2/models/ObjectQueryResultConstraint.md)
- [ObjectQueryResultConstraintDict](docs/v2/models/ObjectQueryResultConstraintDict.md)
- [ObjectRid](docs/v2/models/ObjectRid.md)
- [ObjectSet](docs/v2/models/ObjectSet.md)
- [ObjectSetBaseType](docs/v2/models/ObjectSetBaseType.md)
- [ObjectSetBaseTypeDict](docs/v2/models/ObjectSetBaseTypeDict.md)
- [ObjectSetDict](docs/v2/models/ObjectSetDict.md)
- [ObjectSetFilterType](docs/v2/models/ObjectSetFilterType.md)
- [ObjectSetFilterTypeDict](docs/v2/models/ObjectSetFilterTypeDict.md)
- [ObjectSetIntersectionType](docs/v2/models/ObjectSetIntersectionType.md)
- [ObjectSetIntersectionTypeDict](docs/v2/models/ObjectSetIntersectionTypeDict.md)
- [ObjectSetReferenceType](docs/v2/models/ObjectSetReferenceType.md)
- [ObjectSetReferenceTypeDict](docs/v2/models/ObjectSetReferenceTypeDict.md)
- [ObjectSetRid](docs/v2/models/ObjectSetRid.md)
- [ObjectSetSearchAroundType](docs/v2/models/ObjectSetSearchAroundType.md)
- [ObjectSetSearchAroundTypeDict](docs/v2/models/ObjectSetSearchAroundTypeDict.md)
- [ObjectSetStaticType](docs/v2/models/ObjectSetStaticType.md)
- [ObjectSetStaticTypeDict](docs/v2/models/ObjectSetStaticTypeDict.md)
- [ObjectSetStreamSubscribeRequest](docs/v2/models/ObjectSetStreamSubscribeRequest.md)
- [ObjectSetStreamSubscribeRequestDict](docs/v2/models/ObjectSetStreamSubscribeRequestDict.md)
- [ObjectSetStreamSubscribeRequests](docs/v2/models/ObjectSetStreamSubscribeRequests.md)
- [ObjectSetStreamSubscribeRequestsDict](docs/v2/models/ObjectSetStreamSubscribeRequestsDict.md)
- [ObjectSetSubscribeResponse](docs/v2/models/ObjectSetSubscribeResponse.md)
- [ObjectSetSubscribeResponseDict](docs/v2/models/ObjectSetSubscribeResponseDict.md)
- [ObjectSetSubscribeResponses](docs/v2/models/ObjectSetSubscribeResponses.md)
- [ObjectSetSubscribeResponsesDict](docs/v2/models/ObjectSetSubscribeResponsesDict.md)
- [ObjectSetSubtractType](docs/v2/models/ObjectSetSubtractType.md)
- [ObjectSetSubtractTypeDict](docs/v2/models/ObjectSetSubtractTypeDict.md)
- [ObjectSetUnionType](docs/v2/models/ObjectSetUnionType.md)
- [ObjectSetUnionTypeDict](docs/v2/models/ObjectSetUnionTypeDict.md)
- [ObjectSetUpdate](docs/v2/models/ObjectSetUpdate.md)
- [ObjectSetUpdateDict](docs/v2/models/ObjectSetUpdateDict.md)
- [ObjectSetUpdates](docs/v2/models/ObjectSetUpdates.md)
- [ObjectSetUpdatesDict](docs/v2/models/ObjectSetUpdatesDict.md)
- [ObjectState](docs/v2/models/ObjectState.md)
- [ObjectType](docs/v2/models/ObjectType.md)
- [ObjectTypeApiName](docs/v2/models/ObjectTypeApiName.md)
- [ObjectTypeDict](docs/v2/models/ObjectTypeDict.md)
- [ObjectTypeEdits](docs/v2/models/ObjectTypeEdits.md)
- [ObjectTypeEditsDict](docs/v2/models/ObjectTypeEditsDict.md)
- [ObjectTypeFullMetadata](docs/v2/models/ObjectTypeFullMetadata.md)
- [ObjectTypeFullMetadataDict](docs/v2/models/ObjectTypeFullMetadataDict.md)
- [ObjectTypeInterfaceImplementation](docs/v2/models/ObjectTypeInterfaceImplementation.md)
- [ObjectTypeInterfaceImplementationDict](docs/v2/models/ObjectTypeInterfaceImplementationDict.md)
- [ObjectTypeRid](docs/v2/models/ObjectTypeRid.md)
- [ObjectTypeV2](docs/v2/models/ObjectTypeV2.md)
- [ObjectTypeV2Dict](docs/v2/models/ObjectTypeV2Dict.md)
- [ObjectTypeVisibility](docs/v2/models/ObjectTypeVisibility.md)
- [ObjectUpdate](docs/v2/models/ObjectUpdate.md)
- [ObjectUpdateDict](docs/v2/models/ObjectUpdateDict.md)
- [OneOfConstraint](docs/v2/models/OneOfConstraint.md)
- [OneOfConstraintDict](docs/v2/models/OneOfConstraintDict.md)
- [Ontology](docs/v2/models/Ontology.md)
- [OntologyApiName](docs/v2/models/OntologyApiName.md)
- [OntologyArrayType](docs/v2/models/OntologyArrayType.md)
- [OntologyArrayTypeDict](docs/v2/models/OntologyArrayTypeDict.md)
- [OntologyDataType](docs/v2/models/OntologyDataType.md)
- [OntologyDataTypeDict](docs/v2/models/OntologyDataTypeDict.md)
- [OntologyDict](docs/v2/models/OntologyDict.md)
- [OntologyFullMetadata](docs/v2/models/OntologyFullMetadata.md)
- [OntologyFullMetadataDict](docs/v2/models/OntologyFullMetadataDict.md)
- [OntologyIdentifier](docs/v2/models/OntologyIdentifier.md)
- [OntologyMapType](docs/v2/models/OntologyMapType.md)
- [OntologyMapTypeDict](docs/v2/models/OntologyMapTypeDict.md)
- [OntologyObject](docs/v2/models/OntologyObject.md)
- [OntologyObjectArrayType](docs/v2/models/OntologyObjectArrayType.md)
- [OntologyObjectArrayTypeDict](docs/v2/models/OntologyObjectArrayTypeDict.md)
- [OntologyObjectDict](docs/v2/models/OntologyObjectDict.md)
- [OntologyObjectSetType](docs/v2/models/OntologyObjectSetType.md)
- [OntologyObjectSetTypeDict](docs/v2/models/OntologyObjectSetTypeDict.md)
- [OntologyObjectType](docs/v2/models/OntologyObjectType.md)
- [OntologyObjectTypeDict](docs/v2/models/OntologyObjectTypeDict.md)
- [OntologyObjectV2](docs/v2/models/OntologyObjectV2.md)
- [OntologyRid](docs/v2/models/OntologyRid.md)
- [OntologySetType](docs/v2/models/OntologySetType.md)
- [OntologySetTypeDict](docs/v2/models/OntologySetTypeDict.md)
- [OntologyStructField](docs/v2/models/OntologyStructField.md)
- [OntologyStructFieldDict](docs/v2/models/OntologyStructFieldDict.md)
- [OntologyStructType](docs/v2/models/OntologyStructType.md)
- [OntologyStructTypeDict](docs/v2/models/OntologyStructTypeDict.md)
- [OntologyV2](docs/v2/models/OntologyV2.md)
- [OntologyV2Dict](docs/v2/models/OntologyV2Dict.md)
- [OrderBy](docs/v2/models/OrderBy.md)
- [OrderByDirection](docs/v2/models/OrderByDirection.md)
- [OrganizationRid](docs/v2/models/OrganizationRid.md)
- [OrQuery](docs/v2/models/OrQuery.md)
- [OrQueryDict](docs/v2/models/OrQueryDict.md)
- [OrQueryV2](docs/v2/models/OrQueryV2.md)
- [OrQueryV2Dict](docs/v2/models/OrQueryV2Dict.md)
- [OrTrigger](docs/v2/models/OrTrigger.md)
- [OrTriggerDict](docs/v2/models/OrTriggerDict.md)
- [PageSize](docs/v2/models/PageSize.md)
- [PageToken](docs/v2/models/PageToken.md)
- [Parameter](docs/v2/models/Parameter.md)
- [ParameterDict](docs/v2/models/ParameterDict.md)
- [ParameterEvaluatedConstraint](docs/v2/models/ParameterEvaluatedConstraint.md)
- [ParameterEvaluatedConstraintDict](docs/v2/models/ParameterEvaluatedConstraintDict.md)
- [ParameterEvaluationResult](docs/v2/models/ParameterEvaluationResult.md)
- [ParameterEvaluationResultDict](docs/v2/models/ParameterEvaluationResultDict.md)
- [ParameterId](docs/v2/models/ParameterId.md)
- [ParameterOption](docs/v2/models/ParameterOption.md)
- [ParameterOptionDict](docs/v2/models/ParameterOptionDict.md)
- [PhraseQuery](docs/v2/models/PhraseQuery.md)
- [PhraseQueryDict](docs/v2/models/PhraseQueryDict.md)
- [Polygon](docs/v2/models/Polygon.md)
- [PolygonDict](docs/v2/models/PolygonDict.md)
- [PolygonValue](docs/v2/models/PolygonValue.md)
- [PolygonValueDict](docs/v2/models/PolygonValueDict.md)
- [Position](docs/v2/models/Position.md)
- [PrefixQuery](docs/v2/models/PrefixQuery.md)
- [PrefixQueryDict](docs/v2/models/PrefixQueryDict.md)
- [PreviewMode](docs/v2/models/PreviewMode.md)
- [PrimaryKeyValue](docs/v2/models/PrimaryKeyValue.md)
- [PrincipalFilterType](docs/v2/models/PrincipalFilterType.md)
- [PrincipalId](docs/v2/models/PrincipalId.md)
- [PrincipalType](docs/v2/models/PrincipalType.md)
- [Project](docs/v2/models/Project.md)
- [ProjectDict](docs/v2/models/ProjectDict.md)
- [ProjectRid](docs/v2/models/ProjectRid.md)
- [ProjectScope](docs/v2/models/ProjectScope.md)
- [ProjectScopeDict](docs/v2/models/ProjectScopeDict.md)
- [Property](docs/v2/models/Property.md)
- [PropertyApiName](docs/v2/models/PropertyApiName.md)
- [PropertyDict](docs/v2/models/PropertyDict.md)
- [PropertyFilter](docs/v2/models/PropertyFilter.md)
- [PropertyId](docs/v2/models/PropertyId.md)
- [PropertyV2](docs/v2/models/PropertyV2.md)
- [PropertyV2Dict](docs/v2/models/PropertyV2Dict.md)
- [PropertyValue](docs/v2/models/PropertyValue.md)
- [PropertyValueEscapedString](docs/v2/models/PropertyValueEscapedString.md)
- [QosError](docs/v2/models/QosError.md)
- [QosErrorDict](docs/v2/models/QosErrorDict.md)
- [QueryAggregation](docs/v2/models/QueryAggregation.md)
- [QueryAggregationDict](docs/v2/models/QueryAggregationDict.md)
- [QueryAggregationKeyType](docs/v2/models/QueryAggregationKeyType.md)
- [QueryAggregationKeyTypeDict](docs/v2/models/QueryAggregationKeyTypeDict.md)
- [QueryAggregationRange](docs/v2/models/QueryAggregationRange.md)
- [QueryAggregationRangeDict](docs/v2/models/QueryAggregationRangeDict.md)
- [QueryAggregationRangeSubType](docs/v2/models/QueryAggregationRangeSubType.md)
- [QueryAggregationRangeSubTypeDict](docs/v2/models/QueryAggregationRangeSubTypeDict.md)
- [QueryAggregationRangeType](docs/v2/models/QueryAggregationRangeType.md)
- [QueryAggregationRangeTypeDict](docs/v2/models/QueryAggregationRangeTypeDict.md)
- [QueryAggregationValueType](docs/v2/models/QueryAggregationValueType.md)
- [QueryAggregationValueTypeDict](docs/v2/models/QueryAggregationValueTypeDict.md)
- [QueryApiName](docs/v2/models/QueryApiName.md)
- [QueryArrayType](docs/v2/models/QueryArrayType.md)
- [QueryArrayTypeDict](docs/v2/models/QueryArrayTypeDict.md)
- [QueryDataType](docs/v2/models/QueryDataType.md)
- [QueryDataTypeDict](docs/v2/models/QueryDataTypeDict.md)
- [QueryOutputV2](docs/v2/models/QueryOutputV2.md)
- [QueryOutputV2Dict](docs/v2/models/QueryOutputV2Dict.md)
- [QueryParameterV2](docs/v2/models/QueryParameterV2.md)
- [QueryParameterV2Dict](docs/v2/models/QueryParameterV2Dict.md)
- [QueryRuntimeErrorParameter](docs/v2/models/QueryRuntimeErrorParameter.md)
- [QuerySetType](docs/v2/models/QuerySetType.md)
- [QuerySetTypeDict](docs/v2/models/QuerySetTypeDict.md)
- [QueryStructField](docs/v2/models/QueryStructField.md)
- [QueryStructFieldDict](docs/v2/models/QueryStructFieldDict.md)
- [QueryStructType](docs/v2/models/QueryStructType.md)
- [QueryStructTypeDict](docs/v2/models/QueryStructTypeDict.md)
- [QueryThreeDimensionalAggregation](docs/v2/models/QueryThreeDimensionalAggregation.md)
- [QueryThreeDimensionalAggregationDict](docs/v2/models/QueryThreeDimensionalAggregationDict.md)
- [QueryTwoDimensionalAggregation](docs/v2/models/QueryTwoDimensionalAggregation.md)
- [QueryTwoDimensionalAggregationDict](docs/v2/models/QueryTwoDimensionalAggregationDict.md)
- [QueryType](docs/v2/models/QueryType.md)
- [QueryTypeDict](docs/v2/models/QueryTypeDict.md)
- [QueryTypeV2](docs/v2/models/QueryTypeV2.md)
- [QueryTypeV2Dict](docs/v2/models/QueryTypeV2Dict.md)
- [QueryUnionType](docs/v2/models/QueryUnionType.md)
- [QueryUnionTypeDict](docs/v2/models/QueryUnionTypeDict.md)
- [RangeConstraint](docs/v2/models/RangeConstraint.md)
- [RangeConstraintDict](docs/v2/models/RangeConstraintDict.md)
- [Realm](docs/v2/models/Realm.md)
- [Reason](docs/v2/models/Reason.md)
- [ReasonDict](docs/v2/models/ReasonDict.md)
- [ReasonType](docs/v2/models/ReasonType.md)
- [ReferenceUpdate](docs/v2/models/ReferenceUpdate.md)
- [ReferenceUpdateDict](docs/v2/models/ReferenceUpdateDict.md)
- [ReferenceValue](docs/v2/models/ReferenceValue.md)
- [ReferenceValueDict](docs/v2/models/ReferenceValueDict.md)
- [RefreshObjectSet](docs/v2/models/RefreshObjectSet.md)
- [RefreshObjectSetDict](docs/v2/models/RefreshObjectSetDict.md)
- [RelativeTime](docs/v2/models/RelativeTime.md)
- [RelativeTimeDict](docs/v2/models/RelativeTimeDict.md)
- [RelativeTimeRange](docs/v2/models/RelativeTimeRange.md)
- [RelativeTimeRangeDict](docs/v2/models/RelativeTimeRangeDict.md)
- [RelativeTimeRelation](docs/v2/models/RelativeTimeRelation.md)
- [RelativeTimeSeriesTimeUnit](docs/v2/models/RelativeTimeSeriesTimeUnit.md)
- [ReleaseStatus](docs/v2/models/ReleaseStatus.md)
- [RemoveGroupMembersRequest](docs/v2/models/RemoveGroupMembersRequest.md)
- [RemoveGroupMembersRequestDict](docs/v2/models/RemoveGroupMembersRequestDict.md)
- [RequestId](docs/v2/models/RequestId.md)
- [Resource](docs/v2/models/Resource.md)
- [ResourceDict](docs/v2/models/ResourceDict.md)
- [ResourceDisplayName](docs/v2/models/ResourceDisplayName.md)
- [ResourcePath](docs/v2/models/ResourcePath.md)
- [ResourceRid](docs/v2/models/ResourceRid.md)
- [ResourceType](docs/v2/models/ResourceType.md)
- [RetryBackoffDuration](docs/v2/models/RetryBackoffDuration.md)
- [RetryBackoffDurationDict](docs/v2/models/RetryBackoffDurationDict.md)
- [RetryCount](docs/v2/models/RetryCount.md)
- [ReturnEditsMode](docs/v2/models/ReturnEditsMode.md)
- [Schedule](docs/v2/models/Schedule.md)
- [ScheduleDict](docs/v2/models/ScheduleDict.md)
- [SchedulePaused](docs/v2/models/SchedulePaused.md)
- [ScheduleRid](docs/v2/models/ScheduleRid.md)
- [ScheduleRun](docs/v2/models/ScheduleRun.md)
- [ScheduleRunDict](docs/v2/models/ScheduleRunDict.md)
- [ScheduleRunError](docs/v2/models/ScheduleRunError.md)
- [ScheduleRunErrorDict](docs/v2/models/ScheduleRunErrorDict.md)
- [ScheduleRunErrorName](docs/v2/models/ScheduleRunErrorName.md)
- [ScheduleRunIgnored](docs/v2/models/ScheduleRunIgnored.md)
- [ScheduleRunIgnoredDict](docs/v2/models/ScheduleRunIgnoredDict.md)
- [ScheduleRunResult](docs/v2/models/ScheduleRunResult.md)
- [ScheduleRunResultDict](docs/v2/models/ScheduleRunResultDict.md)
- [ScheduleRunRid](docs/v2/models/ScheduleRunRid.md)
- [ScheduleRunSubmitted](docs/v2/models/ScheduleRunSubmitted.md)
- [ScheduleRunSubmittedDict](docs/v2/models/ScheduleRunSubmittedDict.md)
- [ScheduleSucceededTrigger](docs/v2/models/ScheduleSucceededTrigger.md)
- [ScheduleSucceededTriggerDict](docs/v2/models/ScheduleSucceededTriggerDict.md)
- [ScheduleVersion](docs/v2/models/ScheduleVersion.md)
- [ScheduleVersionDict](docs/v2/models/ScheduleVersionDict.md)
- [ScheduleVersionRid](docs/v2/models/ScheduleVersionRid.md)
- [ScopeMode](docs/v2/models/ScopeMode.md)
- [ScopeModeDict](docs/v2/models/ScopeModeDict.md)
- [SdkPackageName](docs/v2/models/SdkPackageName.md)
- [SearchGroupsRequest](docs/v2/models/SearchGroupsRequest.md)
- [SearchGroupsRequestDict](docs/v2/models/SearchGroupsRequestDict.md)
- [SearchGroupsResponse](docs/v2/models/SearchGroupsResponse.md)
- [SearchGroupsResponseDict](docs/v2/models/SearchGroupsResponseDict.md)
- [SearchJsonQuery](docs/v2/models/SearchJsonQuery.md)
- [SearchJsonQueryDict](docs/v2/models/SearchJsonQueryDict.md)
- [SearchJsonQueryV2](docs/v2/models/SearchJsonQueryV2.md)
- [SearchJsonQueryV2Dict](docs/v2/models/SearchJsonQueryV2Dict.md)
- [SearchObjectsForInterfaceRequest](docs/v2/models/SearchObjectsForInterfaceRequest.md)
- [SearchObjectsForInterfaceRequestDict](docs/v2/models/SearchObjectsForInterfaceRequestDict.md)
- [SearchObjectsRequest](docs/v2/models/SearchObjectsRequest.md)
- [SearchObjectsRequestDict](docs/v2/models/SearchObjectsRequestDict.md)
- [SearchObjectsRequestV2](docs/v2/models/SearchObjectsRequestV2.md)
- [SearchObjectsRequestV2Dict](docs/v2/models/SearchObjectsRequestV2Dict.md)
- [SearchObjectsResponse](docs/v2/models/SearchObjectsResponse.md)
- [SearchObjectsResponseDict](docs/v2/models/SearchObjectsResponseDict.md)
- [SearchObjectsResponseV2](docs/v2/models/SearchObjectsResponseV2.md)
- [SearchObjectsResponseV2Dict](docs/v2/models/SearchObjectsResponseV2Dict.md)
- [SearchOrderBy](docs/v2/models/SearchOrderBy.md)
- [SearchOrderByDict](docs/v2/models/SearchOrderByDict.md)
- [SearchOrderByV2](docs/v2/models/SearchOrderByV2.md)
- [SearchOrderByV2Dict](docs/v2/models/SearchOrderByV2Dict.md)
- [SearchOrdering](docs/v2/models/SearchOrdering.md)
- [SearchOrderingDict](docs/v2/models/SearchOrderingDict.md)
- [SearchOrderingV2](docs/v2/models/SearchOrderingV2.md)
- [SearchOrderingV2Dict](docs/v2/models/SearchOrderingV2Dict.md)
- [SearchUsersRequest](docs/v2/models/SearchUsersRequest.md)
- [SearchUsersRequestDict](docs/v2/models/SearchUsersRequestDict.md)
- [SearchUsersResponse](docs/v2/models/SearchUsersResponse.md)
- [SearchUsersResponseDict](docs/v2/models/SearchUsersResponseDict.md)
- [SelectedPropertyApiName](docs/v2/models/SelectedPropertyApiName.md)
- [SharedPropertyType](docs/v2/models/SharedPropertyType.md)
- [SharedPropertyTypeApiName](docs/v2/models/SharedPropertyTypeApiName.md)
- [SharedPropertyTypeDict](docs/v2/models/SharedPropertyTypeDict.md)
- [SharedPropertyTypeRid](docs/v2/models/SharedPropertyTypeRid.md)
- [ShortType](docs/v2/models/ShortType.md)
- [ShortTypeDict](docs/v2/models/ShortTypeDict.md)
- [SizeBytes](docs/v2/models/SizeBytes.md)
- [Space](docs/v2/models/Space.md)
- [SpaceDict](docs/v2/models/SpaceDict.md)
- [SpaceRid](docs/v2/models/SpaceRid.md)
- [StartsWithQuery](docs/v2/models/StartsWithQuery.md)
- [StartsWithQueryDict](docs/v2/models/StartsWithQueryDict.md)
- [StreamMessage](docs/v2/models/StreamMessage.md)
- [StreamMessageDict](docs/v2/models/StreamMessageDict.md)
- [StreamTimeSeriesPointsRequest](docs/v2/models/StreamTimeSeriesPointsRequest.md)
- [StreamTimeSeriesPointsRequestDict](docs/v2/models/StreamTimeSeriesPointsRequestDict.md)
- [StreamTimeSeriesPointsResponse](docs/v2/models/StreamTimeSeriesPointsResponse.md)
- [StreamTimeSeriesPointsResponseDict](docs/v2/models/StreamTimeSeriesPointsResponseDict.md)
- [StringLengthConstraint](docs/v2/models/StringLengthConstraint.md)
- [StringLengthConstraintDict](docs/v2/models/StringLengthConstraintDict.md)
- [StringRegexMatchConstraint](docs/v2/models/StringRegexMatchConstraint.md)
- [StringRegexMatchConstraintDict](docs/v2/models/StringRegexMatchConstraintDict.md)
- [StringType](docs/v2/models/StringType.md)
- [StringTypeDict](docs/v2/models/StringTypeDict.md)
- [StructFieldName](docs/v2/models/StructFieldName.md)
- [Subdomain](docs/v2/models/Subdomain.md)
- [SubmissionCriteriaEvaluation](docs/v2/models/SubmissionCriteriaEvaluation.md)
- [SubmissionCriteriaEvaluationDict](docs/v2/models/SubmissionCriteriaEvaluationDict.md)
- [SubscriptionClosed](docs/v2/models/SubscriptionClosed.md)
- [SubscriptionClosedDict](docs/v2/models/SubscriptionClosedDict.md)
- [SubscriptionClosureCause](docs/v2/models/SubscriptionClosureCause.md)
- [SubscriptionClosureCauseDict](docs/v2/models/SubscriptionClosureCauseDict.md)
- [SubscriptionError](docs/v2/models/SubscriptionError.md)
- [SubscriptionErrorDict](docs/v2/models/SubscriptionErrorDict.md)
- [SubscriptionId](docs/v2/models/SubscriptionId.md)
- [SubscriptionSuccess](docs/v2/models/SubscriptionSuccess.md)
- [SubscriptionSuccessDict](docs/v2/models/SubscriptionSuccessDict.md)
- [SumAggregation](docs/v2/models/SumAggregation.md)
- [SumAggregationDict](docs/v2/models/SumAggregationDict.md)
- [SumAggregationV2](docs/v2/models/SumAggregationV2.md)
- [SumAggregationV2Dict](docs/v2/models/SumAggregationV2Dict.md)
- [SyncApplyActionResponseV2](docs/v2/models/SyncApplyActionResponseV2.md)
- [SyncApplyActionResponseV2Dict](docs/v2/models/SyncApplyActionResponseV2Dict.md)
- [TableExportFormat](docs/v2/models/TableExportFormat.md)
- [ThirdPartyApplication](docs/v2/models/ThirdPartyApplication.md)
- [ThirdPartyApplicationDict](docs/v2/models/ThirdPartyApplicationDict.md)
- [ThirdPartyApplicationRid](docs/v2/models/ThirdPartyApplicationRid.md)
- [ThreeDimensionalAggregation](docs/v2/models/ThreeDimensionalAggregation.md)
- [ThreeDimensionalAggregationDict](docs/v2/models/ThreeDimensionalAggregationDict.md)
- [TimeRange](docs/v2/models/TimeRange.md)
- [TimeRangeDict](docs/v2/models/TimeRangeDict.md)
- [TimeSeriesItemType](docs/v2/models/TimeSeriesItemType.md)
- [TimeSeriesItemTypeDict](docs/v2/models/TimeSeriesItemTypeDict.md)
- [TimeSeriesPoint](docs/v2/models/TimeSeriesPoint.md)
- [TimeSeriesPointDict](docs/v2/models/TimeSeriesPointDict.md)
- [TimeseriesType](docs/v2/models/TimeseriesType.md)
- [TimeseriesTypeDict](docs/v2/models/TimeseriesTypeDict.md)
- [TimestampType](docs/v2/models/TimestampType.md)
- [TimestampTypeDict](docs/v2/models/TimestampTypeDict.md)
- [TimeTrigger](docs/v2/models/TimeTrigger.md)
- [TimeTriggerDict](docs/v2/models/TimeTriggerDict.md)
- [TimeUnit](docs/v2/models/TimeUnit.md)
- [TotalCount](docs/v2/models/TotalCount.md)
- [Transaction](docs/v2/models/Transaction.md)
- [TransactionCreatedTime](docs/v2/models/TransactionCreatedTime.md)
- [TransactionDict](docs/v2/models/TransactionDict.md)
- [TransactionRid](docs/v2/models/TransactionRid.md)
- [TransactionStatus](docs/v2/models/TransactionStatus.md)
- [TransactionType](docs/v2/models/TransactionType.md)
- [TrashedStatus](docs/v2/models/TrashedStatus.md)
- [Trigger](docs/v2/models/Trigger.md)
- [TriggerDict](docs/v2/models/TriggerDict.md)
- [TwoDimensionalAggregation](docs/v2/models/TwoDimensionalAggregation.md)
- [TwoDimensionalAggregationDict](docs/v2/models/TwoDimensionalAggregationDict.md)
- [UnevaluableConstraint](docs/v2/models/UnevaluableConstraint.md)
- [UnevaluableConstraintDict](docs/v2/models/UnevaluableConstraintDict.md)
- [UnsupportedType](docs/v2/models/UnsupportedType.md)
- [UnsupportedTypeDict](docs/v2/models/UnsupportedTypeDict.md)
- [UpdatedBy](docs/v2/models/UpdatedBy.md)
- [UpdatedTime](docs/v2/models/UpdatedTime.md)
- [UpstreamTarget](docs/v2/models/UpstreamTarget.md)
- [UpstreamTargetDict](docs/v2/models/UpstreamTargetDict.md)
- [User](docs/v2/models/User.md)
- [UserDict](docs/v2/models/UserDict.md)
- [UserId](docs/v2/models/UserId.md)
- [UserScope](docs/v2/models/UserScope.md)
- [UserScopeDict](docs/v2/models/UserScopeDict.md)
- [UserSearchFilter](docs/v2/models/UserSearchFilter.md)
- [UserSearchFilterDict](docs/v2/models/UserSearchFilterDict.md)
- [UserUsername](docs/v2/models/UserUsername.md)
- [ValidateActionRequest](docs/v2/models/ValidateActionRequest.md)
- [ValidateActionRequestDict](docs/v2/models/ValidateActionRequestDict.md)
- [ValidateActionResponse](docs/v2/models/ValidateActionResponse.md)
- [ValidateActionResponseDict](docs/v2/models/ValidateActionResponseDict.md)
- [ValidateActionResponseV2](docs/v2/models/ValidateActionResponseV2.md)
- [ValidateActionResponseV2Dict](docs/v2/models/ValidateActionResponseV2Dict.md)
- [ValidationResult](docs/v2/models/ValidationResult.md)
- [ValueType](docs/v2/models/ValueType.md)
- [Version](docs/v2/models/Version.md)
- [VersionDict](docs/v2/models/VersionDict.md)
- [VersionVersion](docs/v2/models/VersionVersion.md)
- [Website](docs/v2/models/Website.md)
- [WebsiteDict](docs/v2/models/WebsiteDict.md)
- [WithinBoundingBoxPoint](docs/v2/models/WithinBoundingBoxPoint.md)
- [WithinBoundingBoxPointDict](docs/v2/models/WithinBoundingBoxPointDict.md)
- [WithinBoundingBoxQuery](docs/v2/models/WithinBoundingBoxQuery.md)
- [WithinBoundingBoxQueryDict](docs/v2/models/WithinBoundingBoxQueryDict.md)
- [WithinDistanceOfQuery](docs/v2/models/WithinDistanceOfQuery.md)
- [WithinDistanceOfQueryDict](docs/v2/models/WithinDistanceOfQueryDict.md)
- [WithinPolygonQuery](docs/v2/models/WithinPolygonQuery.md)
- [WithinPolygonQueryDict](docs/v2/models/WithinPolygonQueryDict.md)
- [ZoneId](docs/v2/models/ZoneId.md)

<a id="models-v1-link"></a>
## Documentation for V1 models

- [AbsoluteTimeRange](docs/v1/models/AbsoluteTimeRange.md)
- [AbsoluteTimeRangeDict](docs/v1/models/AbsoluteTimeRangeDict.md)
- [ActionMode](docs/v1/models/ActionMode.md)
- [ActionParameterArrayType](docs/v1/models/ActionParameterArrayType.md)
- [ActionParameterArrayTypeDict](docs/v1/models/ActionParameterArrayTypeDict.md)
- [ActionParameterType](docs/v1/models/ActionParameterType.md)
- [ActionParameterTypeDict](docs/v1/models/ActionParameterTypeDict.md)
- [ActionParameterV2](docs/v1/models/ActionParameterV2.md)
- [ActionParameterV2Dict](docs/v1/models/ActionParameterV2Dict.md)
- [ActionResults](docs/v1/models/ActionResults.md)
- [ActionResultsDict](docs/v1/models/ActionResultsDict.md)
- [ActionRid](docs/v1/models/ActionRid.md)
- [ActionType](docs/v1/models/ActionType.md)
- [ActionTypeApiName](docs/v1/models/ActionTypeApiName.md)
- [ActionTypeDict](docs/v1/models/ActionTypeDict.md)
- [ActionTypeRid](docs/v1/models/ActionTypeRid.md)
- [ActionTypeV2](docs/v1/models/ActionTypeV2.md)
- [ActionTypeV2Dict](docs/v1/models/ActionTypeV2Dict.md)
- [AddLink](docs/v1/models/AddLink.md)
- [AddLinkDict](docs/v1/models/AddLinkDict.md)
- [AddObject](docs/v1/models/AddObject.md)
- [AddObjectDict](docs/v1/models/AddObjectDict.md)
- [AggregateObjectSetRequestV2](docs/v1/models/AggregateObjectSetRequestV2.md)
- [AggregateObjectSetRequestV2Dict](docs/v1/models/AggregateObjectSetRequestV2Dict.md)
- [AggregateObjectsRequest](docs/v1/models/AggregateObjectsRequest.md)
- [AggregateObjectsRequestDict](docs/v1/models/AggregateObjectsRequestDict.md)
- [AggregateObjectsRequestV2](docs/v1/models/AggregateObjectsRequestV2.md)
- [AggregateObjectsRequestV2Dict](docs/v1/models/AggregateObjectsRequestV2Dict.md)
- [AggregateObjectsResponse](docs/v1/models/AggregateObjectsResponse.md)
- [AggregateObjectsResponseDict](docs/v1/models/AggregateObjectsResponseDict.md)
- [AggregateObjectsResponseItem](docs/v1/models/AggregateObjectsResponseItem.md)
- [AggregateObjectsResponseItemDict](docs/v1/models/AggregateObjectsResponseItemDict.md)
- [AggregateObjectsResponseItemV2](docs/v1/models/AggregateObjectsResponseItemV2.md)
- [AggregateObjectsResponseItemV2Dict](docs/v1/models/AggregateObjectsResponseItemV2Dict.md)
- [AggregateObjectsResponseV2](docs/v1/models/AggregateObjectsResponseV2.md)
- [AggregateObjectsResponseV2Dict](docs/v1/models/AggregateObjectsResponseV2Dict.md)
- [Aggregation](docs/v1/models/Aggregation.md)
- [AggregationAccuracy](docs/v1/models/AggregationAccuracy.md)
- [AggregationAccuracyRequest](docs/v1/models/AggregationAccuracyRequest.md)
- [AggregationDict](docs/v1/models/AggregationDict.md)
- [AggregationDurationGrouping](docs/v1/models/AggregationDurationGrouping.md)
- [AggregationDurationGroupingDict](docs/v1/models/AggregationDurationGroupingDict.md)
- [AggregationDurationGroupingV2](docs/v1/models/AggregationDurationGroupingV2.md)
- [AggregationDurationGroupingV2Dict](docs/v1/models/AggregationDurationGroupingV2Dict.md)
- [AggregationExactGrouping](docs/v1/models/AggregationExactGrouping.md)
- [AggregationExactGroupingDict](docs/v1/models/AggregationExactGroupingDict.md)
- [AggregationExactGroupingV2](docs/v1/models/AggregationExactGroupingV2.md)
- [AggregationExactGroupingV2Dict](docs/v1/models/AggregationExactGroupingV2Dict.md)
- [AggregationFixedWidthGrouping](docs/v1/models/AggregationFixedWidthGrouping.md)
- [AggregationFixedWidthGroupingDict](docs/v1/models/AggregationFixedWidthGroupingDict.md)
- [AggregationFixedWidthGroupingV2](docs/v1/models/AggregationFixedWidthGroupingV2.md)
- [AggregationFixedWidthGroupingV2Dict](docs/v1/models/AggregationFixedWidthGroupingV2Dict.md)
- [AggregationGroupBy](docs/v1/models/AggregationGroupBy.md)
- [AggregationGroupByDict](docs/v1/models/AggregationGroupByDict.md)
- [AggregationGroupByV2](docs/v1/models/AggregationGroupByV2.md)
- [AggregationGroupByV2Dict](docs/v1/models/AggregationGroupByV2Dict.md)
- [AggregationGroupKey](docs/v1/models/AggregationGroupKey.md)
- [AggregationGroupKeyV2](docs/v1/models/AggregationGroupKeyV2.md)
- [AggregationGroupValue](docs/v1/models/AggregationGroupValue.md)
- [AggregationGroupValueV2](docs/v1/models/AggregationGroupValueV2.md)
- [AggregationMetricName](docs/v1/models/AggregationMetricName.md)
- [AggregationMetricResult](docs/v1/models/AggregationMetricResult.md)
- [AggregationMetricResultDict](docs/v1/models/AggregationMetricResultDict.md)
- [AggregationMetricResultV2](docs/v1/models/AggregationMetricResultV2.md)
- [AggregationMetricResultV2Dict](docs/v1/models/AggregationMetricResultV2Dict.md)
- [AggregationObjectTypeGrouping](docs/v1/models/AggregationObjectTypeGrouping.md)
- [AggregationObjectTypeGroupingDict](docs/v1/models/AggregationObjectTypeGroupingDict.md)
- [AggregationOrderBy](docs/v1/models/AggregationOrderBy.md)
- [AggregationOrderByDict](docs/v1/models/AggregationOrderByDict.md)
- [AggregationRange](docs/v1/models/AggregationRange.md)
- [AggregationRangeDict](docs/v1/models/AggregationRangeDict.md)
- [AggregationRangesGrouping](docs/v1/models/AggregationRangesGrouping.md)
- [AggregationRangesGroupingDict](docs/v1/models/AggregationRangesGroupingDict.md)
- [AggregationRangesGroupingV2](docs/v1/models/AggregationRangesGroupingV2.md)
- [AggregationRangesGroupingV2Dict](docs/v1/models/AggregationRangesGroupingV2Dict.md)
- [AggregationRangeV2](docs/v1/models/AggregationRangeV2.md)
- [AggregationRangeV2Dict](docs/v1/models/AggregationRangeV2Dict.md)
- [AggregationV2](docs/v1/models/AggregationV2.md)
- [AggregationV2Dict](docs/v1/models/AggregationV2Dict.md)
- [AllTermsQuery](docs/v1/models/AllTermsQuery.md)
- [AllTermsQueryDict](docs/v1/models/AllTermsQueryDict.md)
- [AndQuery](docs/v1/models/AndQuery.md)
- [AndQueryDict](docs/v1/models/AndQueryDict.md)
- [AndQueryV2](docs/v1/models/AndQueryV2.md)
- [AndQueryV2Dict](docs/v1/models/AndQueryV2Dict.md)
- [AnyTermQuery](docs/v1/models/AnyTermQuery.md)
- [AnyTermQueryDict](docs/v1/models/AnyTermQueryDict.md)
- [AnyType](docs/v1/models/AnyType.md)
- [AnyTypeDict](docs/v1/models/AnyTypeDict.md)
- [ApplyActionMode](docs/v1/models/ApplyActionMode.md)
- [ApplyActionRequest](docs/v1/models/ApplyActionRequest.md)
- [ApplyActionRequestDict](docs/v1/models/ApplyActionRequestDict.md)
- [ApplyActionRequestOptions](docs/v1/models/ApplyActionRequestOptions.md)
- [ApplyActionRequestOptionsDict](docs/v1/models/ApplyActionRequestOptionsDict.md)
- [ApplyActionRequestV2](docs/v1/models/ApplyActionRequestV2.md)
- [ApplyActionRequestV2Dict](docs/v1/models/ApplyActionRequestV2Dict.md)
- [ApplyActionResponse](docs/v1/models/ApplyActionResponse.md)
- [ApplyActionResponseDict](docs/v1/models/ApplyActionResponseDict.md)
- [ApproximateDistinctAggregation](docs/v1/models/ApproximateDistinctAggregation.md)
- [ApproximateDistinctAggregationDict](docs/v1/models/ApproximateDistinctAggregationDict.md)
- [ApproximateDistinctAggregationV2](docs/v1/models/ApproximateDistinctAggregationV2.md)
- [ApproximateDistinctAggregationV2Dict](docs/v1/models/ApproximateDistinctAggregationV2Dict.md)
- [ApproximatePercentileAggregationV2](docs/v1/models/ApproximatePercentileAggregationV2.md)
- [ApproximatePercentileAggregationV2Dict](docs/v1/models/ApproximatePercentileAggregationV2Dict.md)
- [ArchiveFileFormat](docs/v1/models/ArchiveFileFormat.md)
- [Arg](docs/v1/models/Arg.md)
- [ArgDict](docs/v1/models/ArgDict.md)
- [ArraySizeConstraint](docs/v1/models/ArraySizeConstraint.md)
- [ArraySizeConstraintDict](docs/v1/models/ArraySizeConstraintDict.md)
- [ArtifactRepositoryRid](docs/v1/models/ArtifactRepositoryRid.md)
- [AsyncActionStatus](docs/v1/models/AsyncActionStatus.md)
- [AsyncApplyActionOperationResponseV2](docs/v1/models/AsyncApplyActionOperationResponseV2.md)
- [AsyncApplyActionOperationResponseV2Dict](docs/v1/models/AsyncApplyActionOperationResponseV2Dict.md)
- [AsyncApplyActionRequest](docs/v1/models/AsyncApplyActionRequest.md)
- [AsyncApplyActionRequestDict](docs/v1/models/AsyncApplyActionRequestDict.md)
- [AsyncApplyActionRequestV2](docs/v1/models/AsyncApplyActionRequestV2.md)
- [AsyncApplyActionRequestV2Dict](docs/v1/models/AsyncApplyActionRequestV2Dict.md)
- [AsyncApplyActionResponse](docs/v1/models/AsyncApplyActionResponse.md)
- [AsyncApplyActionResponseDict](docs/v1/models/AsyncApplyActionResponseDict.md)
- [AsyncApplyActionResponseV2](docs/v1/models/AsyncApplyActionResponseV2.md)
- [AsyncApplyActionResponseV2Dict](docs/v1/models/AsyncApplyActionResponseV2Dict.md)
- [Attachment](docs/v1/models/Attachment.md)
- [AttachmentDict](docs/v1/models/AttachmentDict.md)
- [AttachmentMetadataResponse](docs/v1/models/AttachmentMetadataResponse.md)
- [AttachmentMetadataResponseDict](docs/v1/models/AttachmentMetadataResponseDict.md)
- [AttachmentProperty](docs/v1/models/AttachmentProperty.md)
- [AttachmentPropertyDict](docs/v1/models/AttachmentPropertyDict.md)
- [AttachmentRid](docs/v1/models/AttachmentRid.md)
- [AttachmentType](docs/v1/models/AttachmentType.md)
- [AttachmentTypeDict](docs/v1/models/AttachmentTypeDict.md)
- [AttachmentV2](docs/v1/models/AttachmentV2.md)
- [AttachmentV2Dict](docs/v1/models/AttachmentV2Dict.md)
- [AvgAggregation](docs/v1/models/AvgAggregation.md)
- [AvgAggregationDict](docs/v1/models/AvgAggregationDict.md)
- [AvgAggregationV2](docs/v1/models/AvgAggregationV2.md)
- [AvgAggregationV2Dict](docs/v1/models/AvgAggregationV2Dict.md)
- [BatchApplyActionRequest](docs/v1/models/BatchApplyActionRequest.md)
- [BatchApplyActionRequestDict](docs/v1/models/BatchApplyActionRequestDict.md)
- [BatchApplyActionRequestItem](docs/v1/models/BatchApplyActionRequestItem.md)
- [BatchApplyActionRequestItemDict](docs/v1/models/BatchApplyActionRequestItemDict.md)
- [BatchApplyActionRequestOptions](docs/v1/models/BatchApplyActionRequestOptions.md)
- [BatchApplyActionRequestOptionsDict](docs/v1/models/BatchApplyActionRequestOptionsDict.md)
- [BatchApplyActionRequestV2](docs/v1/models/BatchApplyActionRequestV2.md)
- [BatchApplyActionRequestV2Dict](docs/v1/models/BatchApplyActionRequestV2Dict.md)
- [BatchApplyActionResponse](docs/v1/models/BatchApplyActionResponse.md)
- [BatchApplyActionResponseDict](docs/v1/models/BatchApplyActionResponseDict.md)
- [BatchApplyActionResponseV2](docs/v1/models/BatchApplyActionResponseV2.md)
- [BatchApplyActionResponseV2Dict](docs/v1/models/BatchApplyActionResponseV2Dict.md)
- [BBox](docs/v1/models/BBox.md)
- [BinaryType](docs/v1/models/BinaryType.md)
- [BinaryTypeDict](docs/v1/models/BinaryTypeDict.md)
- [BlueprintIcon](docs/v1/models/BlueprintIcon.md)
- [BlueprintIconDict](docs/v1/models/BlueprintIconDict.md)
- [BooleanType](docs/v1/models/BooleanType.md)
- [BooleanTypeDict](docs/v1/models/BooleanTypeDict.md)
- [BoundingBoxValue](docs/v1/models/BoundingBoxValue.md)
- [BoundingBoxValueDict](docs/v1/models/BoundingBoxValueDict.md)
- [Branch](docs/v1/models/Branch.md)
- [BranchDict](docs/v1/models/BranchDict.md)
- [BranchId](docs/v1/models/BranchId.md)
- [ByteType](docs/v1/models/ByteType.md)
- [ByteTypeDict](docs/v1/models/ByteTypeDict.md)
- [CenterPoint](docs/v1/models/CenterPoint.md)
- [CenterPointDict](docs/v1/models/CenterPointDict.md)
- [CenterPointTypes](docs/v1/models/CenterPointTypes.md)
- [CenterPointTypesDict](docs/v1/models/CenterPointTypesDict.md)
- [ContainsAllTermsInOrderPrefixLastTerm](docs/v1/models/ContainsAllTermsInOrderPrefixLastTerm.md)
- [ContainsAllTermsInOrderPrefixLastTermDict](docs/v1/models/ContainsAllTermsInOrderPrefixLastTermDict.md)
- [ContainsAllTermsInOrderQuery](docs/v1/models/ContainsAllTermsInOrderQuery.md)
- [ContainsAllTermsInOrderQueryDict](docs/v1/models/ContainsAllTermsInOrderQueryDict.md)
- [ContainsAllTermsQuery](docs/v1/models/ContainsAllTermsQuery.md)
- [ContainsAllTermsQueryDict](docs/v1/models/ContainsAllTermsQueryDict.md)
- [ContainsAnyTermQuery](docs/v1/models/ContainsAnyTermQuery.md)
- [ContainsAnyTermQueryDict](docs/v1/models/ContainsAnyTermQueryDict.md)
- [ContainsQuery](docs/v1/models/ContainsQuery.md)
- [ContainsQueryDict](docs/v1/models/ContainsQueryDict.md)
- [ContainsQueryV2](docs/v1/models/ContainsQueryV2.md)
- [ContainsQueryV2Dict](docs/v1/models/ContainsQueryV2Dict.md)
- [ContentLength](docs/v1/models/ContentLength.md)
- [ContentType](docs/v1/models/ContentType.md)
- [Coordinate](docs/v1/models/Coordinate.md)
- [CountAggregation](docs/v1/models/CountAggregation.md)
- [CountAggregationDict](docs/v1/models/CountAggregationDict.md)
- [CountAggregationV2](docs/v1/models/CountAggregationV2.md)
- [CountAggregationV2Dict](docs/v1/models/CountAggregationV2Dict.md)
- [CountObjectsResponseV2](docs/v1/models/CountObjectsResponseV2.md)
- [CountObjectsResponseV2Dict](docs/v1/models/CountObjectsResponseV2Dict.md)
- [CreateBranchRequest](docs/v1/models/CreateBranchRequest.md)
- [CreateBranchRequestDict](docs/v1/models/CreateBranchRequestDict.md)
- [CreateDatasetRequest](docs/v1/models/CreateDatasetRequest.md)
- [CreateDatasetRequestDict](docs/v1/models/CreateDatasetRequestDict.md)
- [CreatedTime](docs/v1/models/CreatedTime.md)
- [CreateLinkRule](docs/v1/models/CreateLinkRule.md)
- [CreateLinkRuleDict](docs/v1/models/CreateLinkRuleDict.md)
- [CreateObjectRule](docs/v1/models/CreateObjectRule.md)
- [CreateObjectRuleDict](docs/v1/models/CreateObjectRuleDict.md)
- [CreateTemporaryObjectSetRequestV2](docs/v1/models/CreateTemporaryObjectSetRequestV2.md)
- [CreateTemporaryObjectSetRequestV2Dict](docs/v1/models/CreateTemporaryObjectSetRequestV2Dict.md)
- [CreateTemporaryObjectSetResponseV2](docs/v1/models/CreateTemporaryObjectSetResponseV2.md)
- [CreateTemporaryObjectSetResponseV2Dict](docs/v1/models/CreateTemporaryObjectSetResponseV2Dict.md)
- [CreateTransactionRequest](docs/v1/models/CreateTransactionRequest.md)
- [CreateTransactionRequestDict](docs/v1/models/CreateTransactionRequestDict.md)
- [CustomTypeId](docs/v1/models/CustomTypeId.md)
- [Dataset](docs/v1/models/Dataset.md)
- [DatasetDict](docs/v1/models/DatasetDict.md)
- [DatasetName](docs/v1/models/DatasetName.md)
- [DatasetRid](docs/v1/models/DatasetRid.md)
- [DataValue](docs/v1/models/DataValue.md)
- [DateType](docs/v1/models/DateType.md)
- [DateTypeDict](docs/v1/models/DateTypeDict.md)
- [DecimalType](docs/v1/models/DecimalType.md)
- [DecimalTypeDict](docs/v1/models/DecimalTypeDict.md)
- [DeleteLinkRule](docs/v1/models/DeleteLinkRule.md)
- [DeleteLinkRuleDict](docs/v1/models/DeleteLinkRuleDict.md)
- [DeleteObjectRule](docs/v1/models/DeleteObjectRule.md)
- [DeleteObjectRuleDict](docs/v1/models/DeleteObjectRuleDict.md)
- [DisplayName](docs/v1/models/DisplayName.md)
- [Distance](docs/v1/models/Distance.md)
- [DistanceDict](docs/v1/models/DistanceDict.md)
- [DistanceUnit](docs/v1/models/DistanceUnit.md)
- [DoesNotIntersectBoundingBoxQuery](docs/v1/models/DoesNotIntersectBoundingBoxQuery.md)
- [DoesNotIntersectBoundingBoxQueryDict](docs/v1/models/DoesNotIntersectBoundingBoxQueryDict.md)
- [DoesNotIntersectPolygonQuery](docs/v1/models/DoesNotIntersectPolygonQuery.md)
- [DoesNotIntersectPolygonQueryDict](docs/v1/models/DoesNotIntersectPolygonQueryDict.md)
- [DoubleType](docs/v1/models/DoubleType.md)
- [DoubleTypeDict](docs/v1/models/DoubleTypeDict.md)
- [Duration](docs/v1/models/Duration.md)
- [EqualsQuery](docs/v1/models/EqualsQuery.md)
- [EqualsQueryDict](docs/v1/models/EqualsQueryDict.md)
- [EqualsQueryV2](docs/v1/models/EqualsQueryV2.md)
- [EqualsQueryV2Dict](docs/v1/models/EqualsQueryV2Dict.md)
- [Error](docs/v1/models/Error.md)
- [ErrorDict](docs/v1/models/ErrorDict.md)
- [ErrorName](docs/v1/models/ErrorName.md)
- [ExactDistinctAggregationV2](docs/v1/models/ExactDistinctAggregationV2.md)
- [ExactDistinctAggregationV2Dict](docs/v1/models/ExactDistinctAggregationV2Dict.md)
- [ExecuteQueryRequest](docs/v1/models/ExecuteQueryRequest.md)
- [ExecuteQueryRequestDict](docs/v1/models/ExecuteQueryRequestDict.md)
- [ExecuteQueryResponse](docs/v1/models/ExecuteQueryResponse.md)
- [ExecuteQueryResponseDict](docs/v1/models/ExecuteQueryResponseDict.md)
- [Feature](docs/v1/models/Feature.md)
- [FeatureCollection](docs/v1/models/FeatureCollection.md)
- [FeatureCollectionDict](docs/v1/models/FeatureCollectionDict.md)
- [FeatureCollectionTypes](docs/v1/models/FeatureCollectionTypes.md)
- [FeatureCollectionTypesDict](docs/v1/models/FeatureCollectionTypesDict.md)
- [FeatureDict](docs/v1/models/FeatureDict.md)
- [FeaturePropertyKey](docs/v1/models/FeaturePropertyKey.md)
- [FieldNameV1](docs/v1/models/FieldNameV1.md)
- [File](docs/v1/models/File.md)
- [FileDict](docs/v1/models/FileDict.md)
- [Filename](docs/v1/models/Filename.md)
- [FilePath](docs/v1/models/FilePath.md)
- [FilesystemResource](docs/v1/models/FilesystemResource.md)
- [FilesystemResourceDict](docs/v1/models/FilesystemResourceDict.md)
- [FilterValue](docs/v1/models/FilterValue.md)
- [FloatType](docs/v1/models/FloatType.md)
- [FloatTypeDict](docs/v1/models/FloatTypeDict.md)
- [FolderRid](docs/v1/models/FolderRid.md)
- [FunctionRid](docs/v1/models/FunctionRid.md)
- [FunctionVersion](docs/v1/models/FunctionVersion.md)
- [Fuzzy](docs/v1/models/Fuzzy.md)
- [FuzzyV2](docs/v1/models/FuzzyV2.md)
- [GeoJsonObject](docs/v1/models/GeoJsonObject.md)
- [GeoJsonObjectDict](docs/v1/models/GeoJsonObjectDict.md)
- [Geometry](docs/v1/models/Geometry.md)
- [GeometryCollection](docs/v1/models/GeometryCollection.md)
- [GeometryCollectionDict](docs/v1/models/GeometryCollectionDict.md)
- [GeometryDict](docs/v1/models/GeometryDict.md)
- [GeoPoint](docs/v1/models/GeoPoint.md)
- [GeoPointDict](docs/v1/models/GeoPointDict.md)
- [GeoPointType](docs/v1/models/GeoPointType.md)
- [GeoPointTypeDict](docs/v1/models/GeoPointTypeDict.md)
- [GeoShapeType](docs/v1/models/GeoShapeType.md)
- [GeoShapeTypeDict](docs/v1/models/GeoShapeTypeDict.md)
- [GeotimeSeriesValue](docs/v1/models/GeotimeSeriesValue.md)
- [GeotimeSeriesValueDict](docs/v1/models/GeotimeSeriesValueDict.md)
- [GroupMemberConstraint](docs/v1/models/GroupMemberConstraint.md)
- [GroupMemberConstraintDict](docs/v1/models/GroupMemberConstraintDict.md)
- [GteQuery](docs/v1/models/GteQuery.md)
- [GteQueryDict](docs/v1/models/GteQueryDict.md)
- [GteQueryV2](docs/v1/models/GteQueryV2.md)
- [GteQueryV2Dict](docs/v1/models/GteQueryV2Dict.md)
- [GtQuery](docs/v1/models/GtQuery.md)
- [GtQueryDict](docs/v1/models/GtQueryDict.md)
- [GtQueryV2](docs/v1/models/GtQueryV2.md)
- [GtQueryV2Dict](docs/v1/models/GtQueryV2Dict.md)
- [Icon](docs/v1/models/Icon.md)
- [IconDict](docs/v1/models/IconDict.md)
- [IntegerType](docs/v1/models/IntegerType.md)
- [IntegerTypeDict](docs/v1/models/IntegerTypeDict.md)
- [InterfaceLinkType](docs/v1/models/InterfaceLinkType.md)
- [InterfaceLinkTypeApiName](docs/v1/models/InterfaceLinkTypeApiName.md)
- [InterfaceLinkTypeCardinality](docs/v1/models/InterfaceLinkTypeCardinality.md)
- [InterfaceLinkTypeDict](docs/v1/models/InterfaceLinkTypeDict.md)
- [InterfaceLinkTypeLinkedEntityApiName](docs/v1/models/InterfaceLinkTypeLinkedEntityApiName.md)
- [InterfaceLinkTypeLinkedEntityApiNameDict](docs/v1/models/InterfaceLinkTypeLinkedEntityApiNameDict.md)
- [InterfaceLinkTypeRid](docs/v1/models/InterfaceLinkTypeRid.md)
- [InterfaceType](docs/v1/models/InterfaceType.md)
- [InterfaceTypeApiName](docs/v1/models/InterfaceTypeApiName.md)
- [InterfaceTypeDict](docs/v1/models/InterfaceTypeDict.md)
- [InterfaceTypeRid](docs/v1/models/InterfaceTypeRid.md)
- [IntersectsBoundingBoxQuery](docs/v1/models/IntersectsBoundingBoxQuery.md)
- [IntersectsBoundingBoxQueryDict](docs/v1/models/IntersectsBoundingBoxQueryDict.md)
- [IntersectsPolygonQuery](docs/v1/models/IntersectsPolygonQuery.md)
- [IntersectsPolygonQueryDict](docs/v1/models/IntersectsPolygonQueryDict.md)
- [IsNullQuery](docs/v1/models/IsNullQuery.md)
- [IsNullQueryDict](docs/v1/models/IsNullQueryDict.md)
- [IsNullQueryV2](docs/v1/models/IsNullQueryV2.md)
- [IsNullQueryV2Dict](docs/v1/models/IsNullQueryV2Dict.md)
- [LinearRing](docs/v1/models/LinearRing.md)
- [LineString](docs/v1/models/LineString.md)
- [LineStringCoordinates](docs/v1/models/LineStringCoordinates.md)
- [LineStringDict](docs/v1/models/LineStringDict.md)
- [LinkedInterfaceTypeApiName](docs/v1/models/LinkedInterfaceTypeApiName.md)
- [LinkedInterfaceTypeApiNameDict](docs/v1/models/LinkedInterfaceTypeApiNameDict.md)
- [LinkedObjectTypeApiName](docs/v1/models/LinkedObjectTypeApiName.md)
- [LinkedObjectTypeApiNameDict](docs/v1/models/LinkedObjectTypeApiNameDict.md)
- [LinkSideObject](docs/v1/models/LinkSideObject.md)
- [LinkSideObjectDict](docs/v1/models/LinkSideObjectDict.md)
- [LinkTypeApiName](docs/v1/models/LinkTypeApiName.md)
- [LinkTypeRid](docs/v1/models/LinkTypeRid.md)
- [LinkTypeSide](docs/v1/models/LinkTypeSide.md)
- [LinkTypeSideCardinality](docs/v1/models/LinkTypeSideCardinality.md)
- [LinkTypeSideDict](docs/v1/models/LinkTypeSideDict.md)
- [LinkTypeSideV2](docs/v1/models/LinkTypeSideV2.md)
- [LinkTypeSideV2Dict](docs/v1/models/LinkTypeSideV2Dict.md)
- [ListActionTypesResponse](docs/v1/models/ListActionTypesResponse.md)
- [ListActionTypesResponseDict](docs/v1/models/ListActionTypesResponseDict.md)
- [ListActionTypesResponseV2](docs/v1/models/ListActionTypesResponseV2.md)
- [ListActionTypesResponseV2Dict](docs/v1/models/ListActionTypesResponseV2Dict.md)
- [ListAttachmentsResponseV2](docs/v1/models/ListAttachmentsResponseV2.md)
- [ListAttachmentsResponseV2Dict](docs/v1/models/ListAttachmentsResponseV2Dict.md)
- [ListBranchesResponse](docs/v1/models/ListBranchesResponse.md)
- [ListBranchesResponseDict](docs/v1/models/ListBranchesResponseDict.md)
- [ListFilesResponse](docs/v1/models/ListFilesResponse.md)
- [ListFilesResponseDict](docs/v1/models/ListFilesResponseDict.md)
- [ListInterfaceTypesResponse](docs/v1/models/ListInterfaceTypesResponse.md)
- [ListInterfaceTypesResponseDict](docs/v1/models/ListInterfaceTypesResponseDict.md)
- [ListLinkedObjectsResponse](docs/v1/models/ListLinkedObjectsResponse.md)
- [ListLinkedObjectsResponseDict](docs/v1/models/ListLinkedObjectsResponseDict.md)
- [ListLinkedObjectsResponseV2](docs/v1/models/ListLinkedObjectsResponseV2.md)
- [ListLinkedObjectsResponseV2Dict](docs/v1/models/ListLinkedObjectsResponseV2Dict.md)
- [ListObjectsResponse](docs/v1/models/ListObjectsResponse.md)
- [ListObjectsResponseDict](docs/v1/models/ListObjectsResponseDict.md)
- [ListObjectsResponseV2](docs/v1/models/ListObjectsResponseV2.md)
- [ListObjectsResponseV2Dict](docs/v1/models/ListObjectsResponseV2Dict.md)
- [ListObjectTypesResponse](docs/v1/models/ListObjectTypesResponse.md)
- [ListObjectTypesResponseDict](docs/v1/models/ListObjectTypesResponseDict.md)
- [ListObjectTypesV2Response](docs/v1/models/ListObjectTypesV2Response.md)
- [ListObjectTypesV2ResponseDict](docs/v1/models/ListObjectTypesV2ResponseDict.md)
- [ListOntologiesResponse](docs/v1/models/ListOntologiesResponse.md)
- [ListOntologiesResponseDict](docs/v1/models/ListOntologiesResponseDict.md)
- [ListOntologiesV2Response](docs/v1/models/ListOntologiesV2Response.md)
- [ListOntologiesV2ResponseDict](docs/v1/models/ListOntologiesV2ResponseDict.md)
- [ListOutgoingLinkTypesResponse](docs/v1/models/ListOutgoingLinkTypesResponse.md)
- [ListOutgoingLinkTypesResponseDict](docs/v1/models/ListOutgoingLinkTypesResponseDict.md)
- [ListOutgoingLinkTypesResponseV2](docs/v1/models/ListOutgoingLinkTypesResponseV2.md)
- [ListOutgoingLinkTypesResponseV2Dict](docs/v1/models/ListOutgoingLinkTypesResponseV2Dict.md)
- [ListQueryTypesResponse](docs/v1/models/ListQueryTypesResponse.md)
- [ListQueryTypesResponseDict](docs/v1/models/ListQueryTypesResponseDict.md)
- [ListQueryTypesResponseV2](docs/v1/models/ListQueryTypesResponseV2.md)
- [ListQueryTypesResponseV2Dict](docs/v1/models/ListQueryTypesResponseV2Dict.md)
- [LoadObjectSetRequestV2](docs/v1/models/LoadObjectSetRequestV2.md)
- [LoadObjectSetRequestV2Dict](docs/v1/models/LoadObjectSetRequestV2Dict.md)
- [LoadObjectSetResponseV2](docs/v1/models/LoadObjectSetResponseV2.md)
- [LoadObjectSetResponseV2Dict](docs/v1/models/LoadObjectSetResponseV2Dict.md)
- [LocalFilePath](docs/v1/models/LocalFilePath.md)
- [LocalFilePathDict](docs/v1/models/LocalFilePathDict.md)
- [LogicRule](docs/v1/models/LogicRule.md)
- [LogicRuleDict](docs/v1/models/LogicRuleDict.md)
- [LongType](docs/v1/models/LongType.md)
- [LongTypeDict](docs/v1/models/LongTypeDict.md)
- [LteQuery](docs/v1/models/LteQuery.md)
- [LteQueryDict](docs/v1/models/LteQueryDict.md)
- [LteQueryV2](docs/v1/models/LteQueryV2.md)
- [LteQueryV2Dict](docs/v1/models/LteQueryV2Dict.md)
- [LtQuery](docs/v1/models/LtQuery.md)
- [LtQueryDict](docs/v1/models/LtQueryDict.md)
- [LtQueryV2](docs/v1/models/LtQueryV2.md)
- [LtQueryV2Dict](docs/v1/models/LtQueryV2Dict.md)
- [MarkingType](docs/v1/models/MarkingType.md)
- [MarkingTypeDict](docs/v1/models/MarkingTypeDict.md)
- [MaxAggregation](docs/v1/models/MaxAggregation.md)
- [MaxAggregationDict](docs/v1/models/MaxAggregationDict.md)
- [MaxAggregationV2](docs/v1/models/MaxAggregationV2.md)
- [MaxAggregationV2Dict](docs/v1/models/MaxAggregationV2Dict.md)
- [MediaType](docs/v1/models/MediaType.md)
- [MinAggregation](docs/v1/models/MinAggregation.md)
- [MinAggregationDict](docs/v1/models/MinAggregationDict.md)
- [MinAggregationV2](docs/v1/models/MinAggregationV2.md)
- [MinAggregationV2Dict](docs/v1/models/MinAggregationV2Dict.md)
- [ModifyObject](docs/v1/models/ModifyObject.md)
- [ModifyObjectDict](docs/v1/models/ModifyObjectDict.md)
- [ModifyObjectRule](docs/v1/models/ModifyObjectRule.md)
- [ModifyObjectRuleDict](docs/v1/models/ModifyObjectRuleDict.md)
- [MultiLineString](docs/v1/models/MultiLineString.md)
- [MultiLineStringDict](docs/v1/models/MultiLineStringDict.md)
- [MultiPoint](docs/v1/models/MultiPoint.md)
- [MultiPointDict](docs/v1/models/MultiPointDict.md)
- [MultiPolygon](docs/v1/models/MultiPolygon.md)
- [MultiPolygonDict](docs/v1/models/MultiPolygonDict.md)
- [NestedQueryAggregation](docs/v1/models/NestedQueryAggregation.md)
- [NestedQueryAggregationDict](docs/v1/models/NestedQueryAggregationDict.md)
- [NotQuery](docs/v1/models/NotQuery.md)
- [NotQueryDict](docs/v1/models/NotQueryDict.md)
- [NotQueryV2](docs/v1/models/NotQueryV2.md)
- [NotQueryV2Dict](docs/v1/models/NotQueryV2Dict.md)
- [NullType](docs/v1/models/NullType.md)
- [NullTypeDict](docs/v1/models/NullTypeDict.md)
- [ObjectEdit](docs/v1/models/ObjectEdit.md)
- [ObjectEditDict](docs/v1/models/ObjectEditDict.md)
- [ObjectEdits](docs/v1/models/ObjectEdits.md)
- [ObjectEditsDict](docs/v1/models/ObjectEditsDict.md)
- [ObjectPrimaryKey](docs/v1/models/ObjectPrimaryKey.md)
- [ObjectPropertyType](docs/v1/models/ObjectPropertyType.md)
- [ObjectPropertyTypeDict](docs/v1/models/ObjectPropertyTypeDict.md)
- [ObjectPropertyValueConstraint](docs/v1/models/ObjectPropertyValueConstraint.md)
- [ObjectPropertyValueConstraintDict](docs/v1/models/ObjectPropertyValueConstraintDict.md)
- [ObjectQueryResultConstraint](docs/v1/models/ObjectQueryResultConstraint.md)
- [ObjectQueryResultConstraintDict](docs/v1/models/ObjectQueryResultConstraintDict.md)
- [ObjectRid](docs/v1/models/ObjectRid.md)
- [ObjectSet](docs/v1/models/ObjectSet.md)
- [ObjectSetBaseType](docs/v1/models/ObjectSetBaseType.md)
- [ObjectSetBaseTypeDict](docs/v1/models/ObjectSetBaseTypeDict.md)
- [ObjectSetDict](docs/v1/models/ObjectSetDict.md)
- [ObjectSetFilterType](docs/v1/models/ObjectSetFilterType.md)
- [ObjectSetFilterTypeDict](docs/v1/models/ObjectSetFilterTypeDict.md)
- [ObjectSetIntersectionType](docs/v1/models/ObjectSetIntersectionType.md)
- [ObjectSetIntersectionTypeDict](docs/v1/models/ObjectSetIntersectionTypeDict.md)
- [ObjectSetReferenceType](docs/v1/models/ObjectSetReferenceType.md)
- [ObjectSetReferenceTypeDict](docs/v1/models/ObjectSetReferenceTypeDict.md)
- [ObjectSetRid](docs/v1/models/ObjectSetRid.md)
- [ObjectSetSearchAroundType](docs/v1/models/ObjectSetSearchAroundType.md)
- [ObjectSetSearchAroundTypeDict](docs/v1/models/ObjectSetSearchAroundTypeDict.md)
- [ObjectSetStaticType](docs/v1/models/ObjectSetStaticType.md)
- [ObjectSetStaticTypeDict](docs/v1/models/ObjectSetStaticTypeDict.md)
- [ObjectSetStreamSubscribeRequest](docs/v1/models/ObjectSetStreamSubscribeRequest.md)
- [ObjectSetStreamSubscribeRequestDict](docs/v1/models/ObjectSetStreamSubscribeRequestDict.md)
- [ObjectSetStreamSubscribeRequests](docs/v1/models/ObjectSetStreamSubscribeRequests.md)
- [ObjectSetStreamSubscribeRequestsDict](docs/v1/models/ObjectSetStreamSubscribeRequestsDict.md)
- [ObjectSetSubscribeResponse](docs/v1/models/ObjectSetSubscribeResponse.md)
- [ObjectSetSubscribeResponseDict](docs/v1/models/ObjectSetSubscribeResponseDict.md)
- [ObjectSetSubscribeResponses](docs/v1/models/ObjectSetSubscribeResponses.md)
- [ObjectSetSubscribeResponsesDict](docs/v1/models/ObjectSetSubscribeResponsesDict.md)
- [ObjectSetSubtractType](docs/v1/models/ObjectSetSubtractType.md)
- [ObjectSetSubtractTypeDict](docs/v1/models/ObjectSetSubtractTypeDict.md)
- [ObjectSetUnionType](docs/v1/models/ObjectSetUnionType.md)
- [ObjectSetUnionTypeDict](docs/v1/models/ObjectSetUnionTypeDict.md)
- [ObjectSetUpdate](docs/v1/models/ObjectSetUpdate.md)
- [ObjectSetUpdateDict](docs/v1/models/ObjectSetUpdateDict.md)
- [ObjectSetUpdates](docs/v1/models/ObjectSetUpdates.md)
- [ObjectSetUpdatesDict](docs/v1/models/ObjectSetUpdatesDict.md)
- [ObjectState](docs/v1/models/ObjectState.md)
- [ObjectType](docs/v1/models/ObjectType.md)
- [ObjectTypeApiName](docs/v1/models/ObjectTypeApiName.md)
- [ObjectTypeDict](docs/v1/models/ObjectTypeDict.md)
- [ObjectTypeEdits](docs/v1/models/ObjectTypeEdits.md)
- [ObjectTypeEditsDict](docs/v1/models/ObjectTypeEditsDict.md)
- [ObjectTypeFullMetadata](docs/v1/models/ObjectTypeFullMetadata.md)
- [ObjectTypeFullMetadataDict](docs/v1/models/ObjectTypeFullMetadataDict.md)
- [ObjectTypeInterfaceImplementation](docs/v1/models/ObjectTypeInterfaceImplementation.md)
- [ObjectTypeInterfaceImplementationDict](docs/v1/models/ObjectTypeInterfaceImplementationDict.md)
- [ObjectTypeRid](docs/v1/models/ObjectTypeRid.md)
- [ObjectTypeV2](docs/v1/models/ObjectTypeV2.md)
- [ObjectTypeV2Dict](docs/v1/models/ObjectTypeV2Dict.md)
- [ObjectTypeVisibility](docs/v1/models/ObjectTypeVisibility.md)
- [ObjectUpdate](docs/v1/models/ObjectUpdate.md)
- [ObjectUpdateDict](docs/v1/models/ObjectUpdateDict.md)
- [OneOfConstraint](docs/v1/models/OneOfConstraint.md)
- [OneOfConstraintDict](docs/v1/models/OneOfConstraintDict.md)
- [Ontology](docs/v1/models/Ontology.md)
- [OntologyApiName](docs/v1/models/OntologyApiName.md)
- [OntologyArrayType](docs/v1/models/OntologyArrayType.md)
- [OntologyArrayTypeDict](docs/v1/models/OntologyArrayTypeDict.md)
- [OntologyDataType](docs/v1/models/OntologyDataType.md)
- [OntologyDataTypeDict](docs/v1/models/OntologyDataTypeDict.md)
- [OntologyDict](docs/v1/models/OntologyDict.md)
- [OntologyFullMetadata](docs/v1/models/OntologyFullMetadata.md)
- [OntologyFullMetadataDict](docs/v1/models/OntologyFullMetadataDict.md)
- [OntologyIdentifier](docs/v1/models/OntologyIdentifier.md)
- [OntologyMapType](docs/v1/models/OntologyMapType.md)
- [OntologyMapTypeDict](docs/v1/models/OntologyMapTypeDict.md)
- [OntologyObject](docs/v1/models/OntologyObject.md)
- [OntologyObjectArrayType](docs/v1/models/OntologyObjectArrayType.md)
- [OntologyObjectArrayTypeDict](docs/v1/models/OntologyObjectArrayTypeDict.md)
- [OntologyObjectDict](docs/v1/models/OntologyObjectDict.md)
- [OntologyObjectSetType](docs/v1/models/OntologyObjectSetType.md)
- [OntologyObjectSetTypeDict](docs/v1/models/OntologyObjectSetTypeDict.md)
- [OntologyObjectType](docs/v1/models/OntologyObjectType.md)
- [OntologyObjectTypeDict](docs/v1/models/OntologyObjectTypeDict.md)
- [OntologyObjectV2](docs/v1/models/OntologyObjectV2.md)
- [OntologyRid](docs/v1/models/OntologyRid.md)
- [OntologySetType](docs/v1/models/OntologySetType.md)
- [OntologySetTypeDict](docs/v1/models/OntologySetTypeDict.md)
- [OntologyStructField](docs/v1/models/OntologyStructField.md)
- [OntologyStructFieldDict](docs/v1/models/OntologyStructFieldDict.md)
- [OntologyStructType](docs/v1/models/OntologyStructType.md)
- [OntologyStructTypeDict](docs/v1/models/OntologyStructTypeDict.md)
- [OntologyV2](docs/v1/models/OntologyV2.md)
- [OntologyV2Dict](docs/v1/models/OntologyV2Dict.md)
- [OrderBy](docs/v1/models/OrderBy.md)
- [OrderByDirection](docs/v1/models/OrderByDirection.md)
- [OrQuery](docs/v1/models/OrQuery.md)
- [OrQueryDict](docs/v1/models/OrQueryDict.md)
- [OrQueryV2](docs/v1/models/OrQueryV2.md)
- [OrQueryV2Dict](docs/v1/models/OrQueryV2Dict.md)
- [PageSize](docs/v1/models/PageSize.md)
- [PageToken](docs/v1/models/PageToken.md)
- [Parameter](docs/v1/models/Parameter.md)
- [ParameterDict](docs/v1/models/ParameterDict.md)
- [ParameterEvaluatedConstraint](docs/v1/models/ParameterEvaluatedConstraint.md)
- [ParameterEvaluatedConstraintDict](docs/v1/models/ParameterEvaluatedConstraintDict.md)
- [ParameterEvaluationResult](docs/v1/models/ParameterEvaluationResult.md)
- [ParameterEvaluationResultDict](docs/v1/models/ParameterEvaluationResultDict.md)
- [ParameterId](docs/v1/models/ParameterId.md)
- [ParameterOption](docs/v1/models/ParameterOption.md)
- [ParameterOptionDict](docs/v1/models/ParameterOptionDict.md)
- [PhraseQuery](docs/v1/models/PhraseQuery.md)
- [PhraseQueryDict](docs/v1/models/PhraseQueryDict.md)
- [Polygon](docs/v1/models/Polygon.md)
- [PolygonDict](docs/v1/models/PolygonDict.md)
- [PolygonValue](docs/v1/models/PolygonValue.md)
- [PolygonValueDict](docs/v1/models/PolygonValueDict.md)
- [Position](docs/v1/models/Position.md)
- [PrefixQuery](docs/v1/models/PrefixQuery.md)
- [PrefixQueryDict](docs/v1/models/PrefixQueryDict.md)
- [PreviewMode](docs/v1/models/PreviewMode.md)
- [PrimaryKeyValue](docs/v1/models/PrimaryKeyValue.md)
- [Property](docs/v1/models/Property.md)
- [PropertyApiName](docs/v1/models/PropertyApiName.md)
- [PropertyDict](docs/v1/models/PropertyDict.md)
- [PropertyFilter](docs/v1/models/PropertyFilter.md)
- [PropertyId](docs/v1/models/PropertyId.md)
- [PropertyV2](docs/v1/models/PropertyV2.md)
- [PropertyV2Dict](docs/v1/models/PropertyV2Dict.md)
- [PropertyValue](docs/v1/models/PropertyValue.md)
- [PropertyValueEscapedString](docs/v1/models/PropertyValueEscapedString.md)
- [QosError](docs/v1/models/QosError.md)
- [QosErrorDict](docs/v1/models/QosErrorDict.md)
- [QueryAggregation](docs/v1/models/QueryAggregation.md)
- [QueryAggregationDict](docs/v1/models/QueryAggregationDict.md)
- [QueryAggregationKeyType](docs/v1/models/QueryAggregationKeyType.md)
- [QueryAggregationKeyTypeDict](docs/v1/models/QueryAggregationKeyTypeDict.md)
- [QueryAggregationRange](docs/v1/models/QueryAggregationRange.md)
- [QueryAggregationRangeDict](docs/v1/models/QueryAggregationRangeDict.md)
- [QueryAggregationRangeSubType](docs/v1/models/QueryAggregationRangeSubType.md)
- [QueryAggregationRangeSubTypeDict](docs/v1/models/QueryAggregationRangeSubTypeDict.md)
- [QueryAggregationRangeType](docs/v1/models/QueryAggregationRangeType.md)
- [QueryAggregationRangeTypeDict](docs/v1/models/QueryAggregationRangeTypeDict.md)
- [QueryAggregationValueType](docs/v1/models/QueryAggregationValueType.md)
- [QueryAggregationValueTypeDict](docs/v1/models/QueryAggregationValueTypeDict.md)
- [QueryApiName](docs/v1/models/QueryApiName.md)
- [QueryArrayType](docs/v1/models/QueryArrayType.md)
- [QueryArrayTypeDict](docs/v1/models/QueryArrayTypeDict.md)
- [QueryDataType](docs/v1/models/QueryDataType.md)
- [QueryDataTypeDict](docs/v1/models/QueryDataTypeDict.md)
- [QueryOutputV2](docs/v1/models/QueryOutputV2.md)
- [QueryOutputV2Dict](docs/v1/models/QueryOutputV2Dict.md)
- [QueryParameterV2](docs/v1/models/QueryParameterV2.md)
- [QueryParameterV2Dict](docs/v1/models/QueryParameterV2Dict.md)
- [QueryRuntimeErrorParameter](docs/v1/models/QueryRuntimeErrorParameter.md)
- [QuerySetType](docs/v1/models/QuerySetType.md)
- [QuerySetTypeDict](docs/v1/models/QuerySetTypeDict.md)
- [QueryStructField](docs/v1/models/QueryStructField.md)
- [QueryStructFieldDict](docs/v1/models/QueryStructFieldDict.md)
- [QueryStructType](docs/v1/models/QueryStructType.md)
- [QueryStructTypeDict](docs/v1/models/QueryStructTypeDict.md)
- [QueryThreeDimensionalAggregation](docs/v1/models/QueryThreeDimensionalAggregation.md)
- [QueryThreeDimensionalAggregationDict](docs/v1/models/QueryThreeDimensionalAggregationDict.md)
- [QueryTwoDimensionalAggregation](docs/v1/models/QueryTwoDimensionalAggregation.md)
- [QueryTwoDimensionalAggregationDict](docs/v1/models/QueryTwoDimensionalAggregationDict.md)
- [QueryType](docs/v1/models/QueryType.md)
- [QueryTypeDict](docs/v1/models/QueryTypeDict.md)
- [QueryTypeV2](docs/v1/models/QueryTypeV2.md)
- [QueryTypeV2Dict](docs/v1/models/QueryTypeV2Dict.md)
- [QueryUnionType](docs/v1/models/QueryUnionType.md)
- [QueryUnionTypeDict](docs/v1/models/QueryUnionTypeDict.md)
- [RangeConstraint](docs/v1/models/RangeConstraint.md)
- [RangeConstraintDict](docs/v1/models/RangeConstraintDict.md)
- [Reason](docs/v1/models/Reason.md)
- [ReasonDict](docs/v1/models/ReasonDict.md)
- [ReasonType](docs/v1/models/ReasonType.md)
- [ReferenceUpdate](docs/v1/models/ReferenceUpdate.md)
- [ReferenceUpdateDict](docs/v1/models/ReferenceUpdateDict.md)
- [ReferenceValue](docs/v1/models/ReferenceValue.md)
- [ReferenceValueDict](docs/v1/models/ReferenceValueDict.md)
- [RefreshObjectSet](docs/v1/models/RefreshObjectSet.md)
- [RefreshObjectSetDict](docs/v1/models/RefreshObjectSetDict.md)
- [RelativeTime](docs/v1/models/RelativeTime.md)
- [RelativeTimeDict](docs/v1/models/RelativeTimeDict.md)
- [RelativeTimeRange](docs/v1/models/RelativeTimeRange.md)
- [RelativeTimeRangeDict](docs/v1/models/RelativeTimeRangeDict.md)
- [RelativeTimeRelation](docs/v1/models/RelativeTimeRelation.md)
- [RelativeTimeSeriesTimeUnit](docs/v1/models/RelativeTimeSeriesTimeUnit.md)
- [ReleaseStatus](docs/v1/models/ReleaseStatus.md)
- [RequestId](docs/v1/models/RequestId.md)
- [ResourcePath](docs/v1/models/ResourcePath.md)
- [ReturnEditsMode](docs/v1/models/ReturnEditsMode.md)
- [SdkPackageName](docs/v1/models/SdkPackageName.md)
- [SearchJsonQuery](docs/v1/models/SearchJsonQuery.md)
- [SearchJsonQueryDict](docs/v1/models/SearchJsonQueryDict.md)
- [SearchJsonQueryV2](docs/v1/models/SearchJsonQueryV2.md)
- [SearchJsonQueryV2Dict](docs/v1/models/SearchJsonQueryV2Dict.md)
- [SearchObjectsForInterfaceRequest](docs/v1/models/SearchObjectsForInterfaceRequest.md)
- [SearchObjectsForInterfaceRequestDict](docs/v1/models/SearchObjectsForInterfaceRequestDict.md)
- [SearchObjectsRequest](docs/v1/models/SearchObjectsRequest.md)
- [SearchObjectsRequestDict](docs/v1/models/SearchObjectsRequestDict.md)
- [SearchObjectsRequestV2](docs/v1/models/SearchObjectsRequestV2.md)
- [SearchObjectsRequestV2Dict](docs/v1/models/SearchObjectsRequestV2Dict.md)
- [SearchObjectsResponse](docs/v1/models/SearchObjectsResponse.md)
- [SearchObjectsResponseDict](docs/v1/models/SearchObjectsResponseDict.md)
- [SearchObjectsResponseV2](docs/v1/models/SearchObjectsResponseV2.md)
- [SearchObjectsResponseV2Dict](docs/v1/models/SearchObjectsResponseV2Dict.md)
- [SearchOrderBy](docs/v1/models/SearchOrderBy.md)
- [SearchOrderByDict](docs/v1/models/SearchOrderByDict.md)
- [SearchOrderByV2](docs/v1/models/SearchOrderByV2.md)
- [SearchOrderByV2Dict](docs/v1/models/SearchOrderByV2Dict.md)
- [SearchOrdering](docs/v1/models/SearchOrdering.md)
- [SearchOrderingDict](docs/v1/models/SearchOrderingDict.md)
- [SearchOrderingV2](docs/v1/models/SearchOrderingV2.md)
- [SearchOrderingV2Dict](docs/v1/models/SearchOrderingV2Dict.md)
- [SelectedPropertyApiName](docs/v1/models/SelectedPropertyApiName.md)
- [SharedPropertyType](docs/v1/models/SharedPropertyType.md)
- [SharedPropertyTypeApiName](docs/v1/models/SharedPropertyTypeApiName.md)
- [SharedPropertyTypeDict](docs/v1/models/SharedPropertyTypeDict.md)
- [SharedPropertyTypeRid](docs/v1/models/SharedPropertyTypeRid.md)
- [ShortType](docs/v1/models/ShortType.md)
- [ShortTypeDict](docs/v1/models/ShortTypeDict.md)
- [SizeBytes](docs/v1/models/SizeBytes.md)
- [StartsWithQuery](docs/v1/models/StartsWithQuery.md)
- [StartsWithQueryDict](docs/v1/models/StartsWithQueryDict.md)
- [StreamMessage](docs/v1/models/StreamMessage.md)
- [StreamMessageDict](docs/v1/models/StreamMessageDict.md)
- [StreamTimeSeriesPointsRequest](docs/v1/models/StreamTimeSeriesPointsRequest.md)
- [StreamTimeSeriesPointsRequestDict](docs/v1/models/StreamTimeSeriesPointsRequestDict.md)
- [StreamTimeSeriesPointsResponse](docs/v1/models/StreamTimeSeriesPointsResponse.md)
- [StreamTimeSeriesPointsResponseDict](docs/v1/models/StreamTimeSeriesPointsResponseDict.md)
- [StringLengthConstraint](docs/v1/models/StringLengthConstraint.md)
- [StringLengthConstraintDict](docs/v1/models/StringLengthConstraintDict.md)
- [StringRegexMatchConstraint](docs/v1/models/StringRegexMatchConstraint.md)
- [StringRegexMatchConstraintDict](docs/v1/models/StringRegexMatchConstraintDict.md)
- [StringType](docs/v1/models/StringType.md)
- [StringTypeDict](docs/v1/models/StringTypeDict.md)
- [StructFieldName](docs/v1/models/StructFieldName.md)
- [SubmissionCriteriaEvaluation](docs/v1/models/SubmissionCriteriaEvaluation.md)
- [SubmissionCriteriaEvaluationDict](docs/v1/models/SubmissionCriteriaEvaluationDict.md)
- [SubscriptionClosed](docs/v1/models/SubscriptionClosed.md)
- [SubscriptionClosedDict](docs/v1/models/SubscriptionClosedDict.md)
- [SubscriptionClosureCause](docs/v1/models/SubscriptionClosureCause.md)
- [SubscriptionClosureCauseDict](docs/v1/models/SubscriptionClosureCauseDict.md)
- [SubscriptionError](docs/v1/models/SubscriptionError.md)
- [SubscriptionErrorDict](docs/v1/models/SubscriptionErrorDict.md)
- [SubscriptionId](docs/v1/models/SubscriptionId.md)
- [SubscriptionSuccess](docs/v1/models/SubscriptionSuccess.md)
- [SubscriptionSuccessDict](docs/v1/models/SubscriptionSuccessDict.md)
- [SumAggregation](docs/v1/models/SumAggregation.md)
- [SumAggregationDict](docs/v1/models/SumAggregationDict.md)
- [SumAggregationV2](docs/v1/models/SumAggregationV2.md)
- [SumAggregationV2Dict](docs/v1/models/SumAggregationV2Dict.md)
- [SyncApplyActionResponseV2](docs/v1/models/SyncApplyActionResponseV2.md)
- [SyncApplyActionResponseV2Dict](docs/v1/models/SyncApplyActionResponseV2Dict.md)
- [TableExportFormat](docs/v1/models/TableExportFormat.md)
- [ThreeDimensionalAggregation](docs/v1/models/ThreeDimensionalAggregation.md)
- [ThreeDimensionalAggregationDict](docs/v1/models/ThreeDimensionalAggregationDict.md)
- [TimeRange](docs/v1/models/TimeRange.md)
- [TimeRangeDict](docs/v1/models/TimeRangeDict.md)
- [TimeSeriesItemType](docs/v1/models/TimeSeriesItemType.md)
- [TimeSeriesItemTypeDict](docs/v1/models/TimeSeriesItemTypeDict.md)
- [TimeSeriesPoint](docs/v1/models/TimeSeriesPoint.md)
- [TimeSeriesPointDict](docs/v1/models/TimeSeriesPointDict.md)
- [TimeseriesType](docs/v1/models/TimeseriesType.md)
- [TimeseriesTypeDict](docs/v1/models/TimeseriesTypeDict.md)
- [TimestampType](docs/v1/models/TimestampType.md)
- [TimestampTypeDict](docs/v1/models/TimestampTypeDict.md)
- [TimeUnit](docs/v1/models/TimeUnit.md)
- [TotalCount](docs/v1/models/TotalCount.md)
- [Transaction](docs/v1/models/Transaction.md)
- [TransactionDict](docs/v1/models/TransactionDict.md)
- [TransactionRid](docs/v1/models/TransactionRid.md)
- [TransactionStatus](docs/v1/models/TransactionStatus.md)
- [TransactionType](docs/v1/models/TransactionType.md)
- [TwoDimensionalAggregation](docs/v1/models/TwoDimensionalAggregation.md)
- [TwoDimensionalAggregationDict](docs/v1/models/TwoDimensionalAggregationDict.md)
- [UnevaluableConstraint](docs/v1/models/UnevaluableConstraint.md)
- [UnevaluableConstraintDict](docs/v1/models/UnevaluableConstraintDict.md)
- [UnsupportedType](docs/v1/models/UnsupportedType.md)
- [UnsupportedTypeDict](docs/v1/models/UnsupportedTypeDict.md)
- [UpdatedTime](docs/v1/models/UpdatedTime.md)
- [UserId](docs/v1/models/UserId.md)
- [ValidateActionRequest](docs/v1/models/ValidateActionRequest.md)
- [ValidateActionRequestDict](docs/v1/models/ValidateActionRequestDict.md)
- [ValidateActionResponse](docs/v1/models/ValidateActionResponse.md)
- [ValidateActionResponseDict](docs/v1/models/ValidateActionResponseDict.md)
- [ValidateActionResponseV2](docs/v1/models/ValidateActionResponseV2.md)
- [ValidateActionResponseV2Dict](docs/v1/models/ValidateActionResponseV2Dict.md)
- [ValidationResult](docs/v1/models/ValidationResult.md)
- [ValueType](docs/v1/models/ValueType.md)
- [WithinBoundingBoxPoint](docs/v1/models/WithinBoundingBoxPoint.md)
- [WithinBoundingBoxPointDict](docs/v1/models/WithinBoundingBoxPointDict.md)
- [WithinBoundingBoxQuery](docs/v1/models/WithinBoundingBoxQuery.md)
- [WithinBoundingBoxQueryDict](docs/v1/models/WithinBoundingBoxQueryDict.md)
- [WithinDistanceOfQuery](docs/v1/models/WithinDistanceOfQuery.md)
- [WithinDistanceOfQueryDict](docs/v1/models/WithinDistanceOfQueryDict.md)
- [WithinPolygonQuery](docs/v1/models/WithinPolygonQuery.md)
- [WithinPolygonQueryDict](docs/v1/models/WithinPolygonQueryDict.md)


## Contributions

This repository does not accept code contributions.

If you have any questions, concerns, or ideas for improvements, create an
issue with Palantir Support.

## License
This project is made available under the [Apache 2.0 License](/LICENSE).
