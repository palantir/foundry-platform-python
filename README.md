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

foundry_client = foundry.v2.FoundryClient(
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
import foundry

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

After creating the `ConfidentialClientAuth` object, pass it in to the `FoundryClient`,

```python
import foundry.v2

foundry_client = foundry.v2.FoundryClient(auth=auth, hostname="example.palantirfoundry.com")
```

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
↳ [Static type analysis](#static-types): Learn about the static type analysis capabilities of this library

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
When an HTTP error status is returned, a `PalantirRPCException` is thrown.

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
models use a [TypedDict](https://docs.python.org/3/library/typing.html#typing.TypedDict) whereas responses use `Pydantic`
models. For example, here is how `Group.search` method is defined in the `Admin` namespace:

```python
    @pydantic.validate_call
    @handle_unexpected
    def search(
        self,
        *,
        where: GroupSearchFilterDict,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> SearchGroupsResponse:
        ...
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
**Admin** | MarkingMember | [**add**](docs/v2/Admin/MarkingMember.md#add) | **POST** /v2/admin/markings/{markingId}/markingMembers/add |
**Admin** | MarkingMember | [**list**](docs/v2/Admin/MarkingMember.md#list) | **GET** /v2/admin/markings/{markingId}/markingMembers |
**Admin** | MarkingMember | [**page**](docs/v2/Admin/MarkingMember.md#page) | **GET** /v2/admin/markings/{markingId}/markingMembers |
**Admin** | MarkingMember | [**remove**](docs/v2/Admin/MarkingMember.md#remove) | **POST** /v2/admin/markings/{markingId}/markingMembers/remove |
**Admin** | User | [**delete**](docs/v2/Admin/User.md#delete) | **DELETE** /v2/admin/users/{userId} |
**Admin** | User | [**get**](docs/v2/Admin/User.md#get) | **GET** /v2/admin/users/{userId} |
**Admin** | User | [**get_batch**](docs/v2/Admin/User.md#get_batch) | **POST** /v2/admin/users/getBatch |
**Admin** | User | [**get_current**](docs/v2/Admin/User.md#get_current) | **GET** /v2/admin/users/getCurrent |
**Admin** | User | [**list**](docs/v2/Admin/User.md#list) | **GET** /v2/admin/users |
**Admin** | User | [**page**](docs/v2/Admin/User.md#page) | **GET** /v2/admin/users |
**Admin** | User | [**profile_picture**](docs/v2/Admin/User.md#profile_picture) | **GET** /v2/admin/users/{userId}/profilePicture |
**Admin** | User | [**search**](docs/v2/Admin/User.md#search) | **POST** /v2/admin/users/search |
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
**OntologiesV2** | Action | [**apply**](docs/v2/OntologiesV2/Action.md#apply) | **POST** /v2/ontologies/{ontology}/actions/{action}/apply |
**OntologiesV2** | Action | [**apply_batch**](docs/v2/OntologiesV2/Action.md#apply_batch) | **POST** /v2/ontologies/{ontology}/actions/{action}/applyBatch |
**OntologiesV2** | ActionTypeV2 | [**get**](docs/v2/OntologiesV2/ActionTypeV2.md#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} |
**OntologiesV2** | ActionTypeV2 | [**list**](docs/v2/OntologiesV2/ActionTypeV2.md#list) | **GET** /v2/ontologies/{ontology}/actionTypes |
**OntologiesV2** | ActionTypeV2 | [**page**](docs/v2/OntologiesV2/ActionTypeV2.md#page) | **GET** /v2/ontologies/{ontology}/actionTypes |
**OntologiesV2** | Attachment | [**read**](docs/v2/OntologiesV2/Attachment.md#read) | **GET** /v2/ontologies/attachments/{attachmentRid}/content |
**OntologiesV2** | Attachment | [**upload**](docs/v2/OntologiesV2/Attachment.md#upload) | **POST** /v2/ontologies/attachments/upload |
**OntologiesV2** | AttachmentPropertyV2 | [**get_attachment**](docs/v2/OntologiesV2/AttachmentPropertyV2.md#get_attachment) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property} |
**OntologiesV2** | AttachmentPropertyV2 | [**get_attachment_by_rid**](docs/v2/OntologiesV2/AttachmentPropertyV2.md#get_attachment_by_rid) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid} |
**OntologiesV2** | AttachmentPropertyV2 | [**read_attachment**](docs/v2/OntologiesV2/AttachmentPropertyV2.md#read_attachment) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/content |
**OntologiesV2** | AttachmentPropertyV2 | [**read_attachment_by_rid**](docs/v2/OntologiesV2/AttachmentPropertyV2.md#read_attachment_by_rid) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}/content |
**OntologiesV2** | LinkedObjectV2 | [**get_linked_object**](docs/v2/OntologiesV2/LinkedObjectV2.md#get_linked_object) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey} |
**OntologiesV2** | LinkedObjectV2 | [**list_linked_objects**](docs/v2/OntologiesV2/LinkedObjectV2.md#list_linked_objects) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType} |
**OntologiesV2** | LinkedObjectV2 | [**page_linked_objects**](docs/v2/OntologiesV2/LinkedObjectV2.md#page_linked_objects) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType} |
**OntologiesV2** | ObjectTypeV2 | [**get**](docs/v2/OntologiesV2/ObjectTypeV2.md#get) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType} |
**OntologiesV2** | ObjectTypeV2 | [**get_outgoing_link_type**](docs/v2/OntologiesV2/ObjectTypeV2.md#get_outgoing_link_type) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
**OntologiesV2** | ObjectTypeV2 | [**list**](docs/v2/OntologiesV2/ObjectTypeV2.md#list) | **GET** /v2/ontologies/{ontology}/objectTypes |
**OntologiesV2** | ObjectTypeV2 | [**list_outgoing_link_types**](docs/v2/OntologiesV2/ObjectTypeV2.md#list_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
**OntologiesV2** | ObjectTypeV2 | [**page**](docs/v2/OntologiesV2/ObjectTypeV2.md#page) | **GET** /v2/ontologies/{ontology}/objectTypes |
**OntologiesV2** | ObjectTypeV2 | [**page_outgoing_link_types**](docs/v2/OntologiesV2/ObjectTypeV2.md#page_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
**OntologiesV2** | OntologyObjectSet | [**aggregate**](docs/v2/OntologiesV2/OntologyObjectSet.md#aggregate) | **POST** /v2/ontologies/{ontology}/objectSets/aggregate |
**OntologiesV2** | OntologyObjectSet | [**load**](docs/v2/OntologiesV2/OntologyObjectSet.md#load) | **POST** /v2/ontologies/{ontology}/objectSets/loadObjects |
**OntologiesV2** | OntologyObjectV2 | [**aggregate**](docs/v2/OntologiesV2/OntologyObjectV2.md#aggregate) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/aggregate |
**OntologiesV2** | OntologyObjectV2 | [**get**](docs/v2/OntologiesV2/OntologyObjectV2.md#get) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey} |
**OntologiesV2** | OntologyObjectV2 | [**list**](docs/v2/OntologiesV2/OntologyObjectV2.md#list) | **GET** /v2/ontologies/{ontology}/objects/{objectType} |
**OntologiesV2** | OntologyObjectV2 | [**page**](docs/v2/OntologiesV2/OntologyObjectV2.md#page) | **GET** /v2/ontologies/{ontology}/objects/{objectType} |
**OntologiesV2** | OntologyObjectV2 | [**search**](docs/v2/OntologiesV2/OntologyObjectV2.md#search) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/search |
**OntologiesV2** | OntologyV2 | [**get**](docs/v2/OntologiesV2/OntologyV2.md#get) | **GET** /v2/ontologies/{ontology} |
**OntologiesV2** | Query | [**execute**](docs/v2/OntologiesV2/Query.md#execute) | **POST** /v2/ontologies/{ontology}/queries/{queryApiName}/execute |
**OntologiesV2** | QueryType | [**get**](docs/v2/OntologiesV2/QueryType.md#get) | **GET** /v2/ontologies/{ontology}/queryTypes/{queryApiName} |
**OntologiesV2** | QueryType | [**list**](docs/v2/OntologiesV2/QueryType.md#list) | **GET** /v2/ontologies/{ontology}/queryTypes |
**OntologiesV2** | QueryType | [**page**](docs/v2/OntologiesV2/QueryType.md#page) | **GET** /v2/ontologies/{ontology}/queryTypes |
**OntologiesV2** | TimeSeriesPropertyV2 | [**get_first_point**](docs/v2/OntologiesV2/TimeSeriesPropertyV2.md#get_first_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/firstPoint |
**OntologiesV2** | TimeSeriesPropertyV2 | [**get_last_point**](docs/v2/OntologiesV2/TimeSeriesPropertyV2.md#get_last_point) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/lastPoint |
**OntologiesV2** | TimeSeriesPropertyV2 | [**stream_points**](docs/v2/OntologiesV2/TimeSeriesPropertyV2.md#stream_points) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamPoints |
**Orchestration** | Build | [**create**](docs/v2/Orchestration/Build.md#create) | **POST** /v2/orchestration/builds/create |
**Orchestration** | Build | [**get**](docs/v2/Orchestration/Build.md#get) | **GET** /v2/orchestration/builds/{buildRid} |
**Orchestration** | Schedule | [**create**](docs/v2/Orchestration/Schedule.md#create) | **POST** /v2/orchestration/schedules |
**Orchestration** | Schedule | [**delete**](docs/v2/Orchestration/Schedule.md#delete) | **DELETE** /v2/orchestration/schedules/{scheduleRid} |
**Orchestration** | Schedule | [**get**](docs/v2/Orchestration/Schedule.md#get) | **GET** /v2/orchestration/schedules/{scheduleRid} |
**Orchestration** | Schedule | [**pause**](docs/v2/Orchestration/Schedule.md#pause) | **POST** /v2/orchestration/schedules/{scheduleRid}/pause |
**Orchestration** | Schedule | [**replace**](docs/v2/Orchestration/Schedule.md#replace) | **PUT** /v2/orchestration/schedules/{scheduleRid} |
**Orchestration** | Schedule | [**run**](docs/v2/Orchestration/Schedule.md#run) | **POST** /v2/orchestration/schedules/{scheduleRid}/run |
**Orchestration** | Schedule | [**unpause**](docs/v2/Orchestration/Schedule.md#unpause) | **POST** /v2/orchestration/schedules/{scheduleRid}/unpause |
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

- [AttributeName](docs/v2/models/AttributeName.md)
- [AttributeValue](docs/v2/models/AttributeValue.md)
- [AttributeValues](docs/v2/models/AttributeValues.md)
- [Enrollment](docs/v2/models/Enrollment.md)
- [EnrollmentDict](docs/v2/models/EnrollmentDict.md)
- [EnrollmentName](docs/v2/models/EnrollmentName.md)
- [GetGroupsBatchRequestElementDict](docs/v2/models/GetGroupsBatchRequestElementDict.md)
- [GetGroupsBatchResponse](docs/v2/models/GetGroupsBatchResponse.md)
- [GetGroupsBatchResponseDict](docs/v2/models/GetGroupsBatchResponseDict.md)
- [GetMarkingsBatchRequestElementDict](docs/v2/models/GetMarkingsBatchRequestElementDict.md)
- [GetMarkingsBatchResponse](docs/v2/models/GetMarkingsBatchResponse.md)
- [GetMarkingsBatchResponseDict](docs/v2/models/GetMarkingsBatchResponseDict.md)
- [GetUserMarkingsResponse](docs/v2/models/GetUserMarkingsResponse.md)
- [GetUserMarkingsResponseDict](docs/v2/models/GetUserMarkingsResponseDict.md)
- [GetUsersBatchRequestElementDict](docs/v2/models/GetUsersBatchRequestElementDict.md)
- [GetUsersBatchResponse](docs/v2/models/GetUsersBatchResponse.md)
- [GetUsersBatchResponseDict](docs/v2/models/GetUsersBatchResponseDict.md)
- [Group](docs/v2/models/Group.md)
- [GroupDict](docs/v2/models/GroupDict.md)
- [GroupMember](docs/v2/models/GroupMember.md)
- [GroupMemberDict](docs/v2/models/GroupMemberDict.md)
- [GroupMembership](docs/v2/models/GroupMembership.md)
- [GroupMembershipDict](docs/v2/models/GroupMembershipDict.md)
- [GroupMembershipExpiration](docs/v2/models/GroupMembershipExpiration.md)
- [GroupName](docs/v2/models/GroupName.md)
- [GroupSearchFilterDict](docs/v2/models/GroupSearchFilterDict.md)
- [Host](docs/v2/models/Host.md)
- [HostDict](docs/v2/models/HostDict.md)
- [HostName](docs/v2/models/HostName.md)
- [ListGroupMembershipsResponse](docs/v2/models/ListGroupMembershipsResponse.md)
- [ListGroupMembershipsResponseDict](docs/v2/models/ListGroupMembershipsResponseDict.md)
- [ListGroupMembersResponse](docs/v2/models/ListGroupMembersResponse.md)
- [ListGroupMembersResponseDict](docs/v2/models/ListGroupMembersResponseDict.md)
- [ListGroupsResponse](docs/v2/models/ListGroupsResponse.md)
- [ListGroupsResponseDict](docs/v2/models/ListGroupsResponseDict.md)
- [ListHostsResponse](docs/v2/models/ListHostsResponse.md)
- [ListHostsResponseDict](docs/v2/models/ListHostsResponseDict.md)
- [ListMarkingCategoriesResponse](docs/v2/models/ListMarkingCategoriesResponse.md)
- [ListMarkingCategoriesResponseDict](docs/v2/models/ListMarkingCategoriesResponseDict.md)
- [ListMarkingMembersResponse](docs/v2/models/ListMarkingMembersResponse.md)
- [ListMarkingMembersResponseDict](docs/v2/models/ListMarkingMembersResponseDict.md)
- [ListMarkingsResponse](docs/v2/models/ListMarkingsResponse.md)
- [ListMarkingsResponseDict](docs/v2/models/ListMarkingsResponseDict.md)
- [ListUsersResponse](docs/v2/models/ListUsersResponse.md)
- [ListUsersResponseDict](docs/v2/models/ListUsersResponseDict.md)
- [Marking](docs/v2/models/Marking.md)
- [MarkingCategory](docs/v2/models/MarkingCategory.md)
- [MarkingCategoryDict](docs/v2/models/MarkingCategoryDict.md)
- [MarkingCategoryDisplayName](docs/v2/models/MarkingCategoryDisplayName.md)
- [MarkingCategoryId](docs/v2/models/MarkingCategoryId.md)
- [MarkingCategoryType](docs/v2/models/MarkingCategoryType.md)
- [MarkingDict](docs/v2/models/MarkingDict.md)
- [MarkingDisplayName](docs/v2/models/MarkingDisplayName.md)
- [MarkingMember](docs/v2/models/MarkingMember.md)
- [MarkingMemberDict](docs/v2/models/MarkingMemberDict.md)
- [MarkingType](docs/v2/models/MarkingType.md)
- [PrincipalFilterType](docs/v2/models/PrincipalFilterType.md)
- [SearchGroupsResponse](docs/v2/models/SearchGroupsResponse.md)
- [SearchGroupsResponseDict](docs/v2/models/SearchGroupsResponseDict.md)
- [SearchUsersResponse](docs/v2/models/SearchUsersResponse.md)
- [SearchUsersResponseDict](docs/v2/models/SearchUsersResponseDict.md)
- [User](docs/v2/models/User.md)
- [UserDict](docs/v2/models/UserDict.md)
- [UserSearchFilterDict](docs/v2/models/UserSearchFilterDict.md)
- [UserUsername](docs/v2/models/UserUsername.md)
- [Agent](docs/v2/models/Agent.md)
- [AgentDict](docs/v2/models/AgentDict.md)
- [AgentMarkdownResponse](docs/v2/models/AgentMarkdownResponse.md)
- [AgentMetadata](docs/v2/models/AgentMetadata.md)
- [AgentMetadataDict](docs/v2/models/AgentMetadataDict.md)
- [AgentRid](docs/v2/models/AgentRid.md)
- [AgentSessionRagContextResponse](docs/v2/models/AgentSessionRagContextResponse.md)
- [AgentSessionRagContextResponseDict](docs/v2/models/AgentSessionRagContextResponseDict.md)
- [AgentsSessionsPage](docs/v2/models/AgentsSessionsPage.md)
- [AgentsSessionsPageDict](docs/v2/models/AgentsSessionsPageDict.md)
- [AgentVersion](docs/v2/models/AgentVersion.md)
- [AgentVersionDetails](docs/v2/models/AgentVersionDetails.md)
- [AgentVersionDetailsDict](docs/v2/models/AgentVersionDetailsDict.md)
- [AgentVersionDict](docs/v2/models/AgentVersionDict.md)
- [AgentVersionString](docs/v2/models/AgentVersionString.md)
- [CancelSessionResponse](docs/v2/models/CancelSessionResponse.md)
- [CancelSessionResponseDict](docs/v2/models/CancelSessionResponseDict.md)
- [Content](docs/v2/models/Content.md)
- [ContentDict](docs/v2/models/ContentDict.md)
- [InputContextDict](docs/v2/models/InputContextDict.md)
- [ListAgentVersionsResponse](docs/v2/models/ListAgentVersionsResponse.md)
- [ListAgentVersionsResponseDict](docs/v2/models/ListAgentVersionsResponseDict.md)
- [ListSessionsResponse](docs/v2/models/ListSessionsResponse.md)
- [ListSessionsResponseDict](docs/v2/models/ListSessionsResponseDict.md)
- [MessageId](docs/v2/models/MessageId.md)
- [ObjectContext](docs/v2/models/ObjectContext.md)
- [ObjectContextDict](docs/v2/models/ObjectContextDict.md)
- [ObjectSetParameter](docs/v2/models/ObjectSetParameter.md)
- [ObjectSetParameterDict](docs/v2/models/ObjectSetParameterDict.md)
- [ObjectSetParameterValueDict](docs/v2/models/ObjectSetParameterValueDict.md)
- [ObjectSetParameterValueUpdate](docs/v2/models/ObjectSetParameterValueUpdate.md)
- [ObjectSetParameterValueUpdateDict](docs/v2/models/ObjectSetParameterValueUpdateDict.md)
- [PageSize](docs/v2/models/PageSize.md)
- [PageToken](docs/v2/models/PageToken.md)
- [Parameter](docs/v2/models/Parameter.md)
- [ParameterAccessMode](docs/v2/models/ParameterAccessMode.md)
- [ParameterDict](docs/v2/models/ParameterDict.md)
- [ParameterId](docs/v2/models/ParameterId.md)
- [ParameterType](docs/v2/models/ParameterType.md)
- [ParameterTypeDict](docs/v2/models/ParameterTypeDict.md)
- [ParameterValueDict](docs/v2/models/ParameterValueDict.md)
- [ParameterValueUpdate](docs/v2/models/ParameterValueUpdate.md)
- [ParameterValueUpdateDict](docs/v2/models/ParameterValueUpdateDict.md)
- [Session](docs/v2/models/Session.md)
- [SessionDict](docs/v2/models/SessionDict.md)
- [SessionExchange](docs/v2/models/SessionExchange.md)
- [SessionExchangeContexts](docs/v2/models/SessionExchangeContexts.md)
- [SessionExchangeContextsDict](docs/v2/models/SessionExchangeContextsDict.md)
- [SessionExchangeDict](docs/v2/models/SessionExchangeDict.md)
- [SessionExchangeResult](docs/v2/models/SessionExchangeResult.md)
- [SessionExchangeResultDict](docs/v2/models/SessionExchangeResultDict.md)
- [SessionMetadata](docs/v2/models/SessionMetadata.md)
- [SessionMetadataDict](docs/v2/models/SessionMetadataDict.md)
- [SessionRid](docs/v2/models/SessionRid.md)
- [StringParameter](docs/v2/models/StringParameter.md)
- [StringParameterDict](docs/v2/models/StringParameterDict.md)
- [StringParameterValue](docs/v2/models/StringParameterValue.md)
- [StringParameterValueDict](docs/v2/models/StringParameterValueDict.md)
- [UserTextInput](docs/v2/models/UserTextInput.md)
- [UserTextInputDict](docs/v2/models/UserTextInputDict.md)
- [AgentProxyRuntime](docs/v2/models/AgentProxyRuntime.md)
- [AgentProxyRuntimeDict](docs/v2/models/AgentProxyRuntimeDict.md)
- [AgentRid](docs/v2/models/AgentRid.md)
- [AgentWorkerRuntime](docs/v2/models/AgentWorkerRuntime.md)
- [AgentWorkerRuntimeDict](docs/v2/models/AgentWorkerRuntimeDict.md)
- [Connection](docs/v2/models/Connection.md)
- [ConnectionDict](docs/v2/models/ConnectionDict.md)
- [ConnectionDisplayName](docs/v2/models/ConnectionDisplayName.md)
- [ConnectionRid](docs/v2/models/ConnectionRid.md)
- [DirectConnectionRuntime](docs/v2/models/DirectConnectionRuntime.md)
- [DirectConnectionRuntimeDict](docs/v2/models/DirectConnectionRuntimeDict.md)
- [FileAnyPathMatchesFilter](docs/v2/models/FileAnyPathMatchesFilter.md)
- [FileAnyPathMatchesFilterDict](docs/v2/models/FileAnyPathMatchesFilterDict.md)
- [FileAtLeastCountFilter](docs/v2/models/FileAtLeastCountFilter.md)
- [FileAtLeastCountFilterDict](docs/v2/models/FileAtLeastCountFilterDict.md)
- [FileChangedSinceLastUploadFilter](docs/v2/models/FileChangedSinceLastUploadFilter.md)
- [FileChangedSinceLastUploadFilterDict](docs/v2/models/FileChangedSinceLastUploadFilterDict.md)
- [FileImport](docs/v2/models/FileImport.md)
- [FileImportCustomFilter](docs/v2/models/FileImportCustomFilter.md)
- [FileImportCustomFilterDict](docs/v2/models/FileImportCustomFilterDict.md)
- [FileImportDict](docs/v2/models/FileImportDict.md)
- [FileImportDisplayName](docs/v2/models/FileImportDisplayName.md)
- [FileImportFilter](docs/v2/models/FileImportFilter.md)
- [FileImportFilterDict](docs/v2/models/FileImportFilterDict.md)
- [FileImportMode](docs/v2/models/FileImportMode.md)
- [FileImportRid](docs/v2/models/FileImportRid.md)
- [FileLastModifiedAfterFilter](docs/v2/models/FileLastModifiedAfterFilter.md)
- [FileLastModifiedAfterFilterDict](docs/v2/models/FileLastModifiedAfterFilterDict.md)
- [FilePathMatchesFilter](docs/v2/models/FilePathMatchesFilter.md)
- [FilePathMatchesFilterDict](docs/v2/models/FilePathMatchesFilterDict.md)
- [FilePathNotMatchesFilter](docs/v2/models/FilePathNotMatchesFilter.md)
- [FilePathNotMatchesFilterDict](docs/v2/models/FilePathNotMatchesFilterDict.md)
- [FileProperty](docs/v2/models/FileProperty.md)
- [FilesCountLimitFilter](docs/v2/models/FilesCountLimitFilter.md)
- [FilesCountLimitFilterDict](docs/v2/models/FilesCountLimitFilterDict.md)
- [FileSizeFilter](docs/v2/models/FileSizeFilter.md)
- [FileSizeFilterDict](docs/v2/models/FileSizeFilterDict.md)
- [ListFileImportsResponse](docs/v2/models/ListFileImportsResponse.md)
- [ListFileImportsResponseDict](docs/v2/models/ListFileImportsResponseDict.md)
- [NetworkEgressPolicyRid](docs/v2/models/NetworkEgressPolicyRid.md)
- [PlaintextValue](docs/v2/models/PlaintextValue.md)
- [RuntimePlatform](docs/v2/models/RuntimePlatform.md)
- [RuntimePlatformDict](docs/v2/models/RuntimePlatformDict.md)
- [SecretName](docs/v2/models/SecretName.md)
- [ArrayFieldType](docs/v2/models/ArrayFieldType.md)
- [ArrayFieldTypeDict](docs/v2/models/ArrayFieldTypeDict.md)
- [AttachmentType](docs/v2/models/AttachmentType.md)
- [AttachmentTypeDict](docs/v2/models/AttachmentTypeDict.md)
- [BinaryType](docs/v2/models/BinaryType.md)
- [BinaryTypeDict](docs/v2/models/BinaryTypeDict.md)
- [BooleanType](docs/v2/models/BooleanType.md)
- [BooleanTypeDict](docs/v2/models/BooleanTypeDict.md)
- [ByteType](docs/v2/models/ByteType.md)
- [ByteTypeDict](docs/v2/models/ByteTypeDict.md)
- [ChangeDataCaptureConfiguration](docs/v2/models/ChangeDataCaptureConfiguration.md)
- [ChangeDataCaptureConfigurationDict](docs/v2/models/ChangeDataCaptureConfigurationDict.md)
- [ContentLength](docs/v2/models/ContentLength.md)
- [ContentType](docs/v2/models/ContentType.md)
- [CreatedBy](docs/v2/models/CreatedBy.md)
- [CreatedTime](docs/v2/models/CreatedTime.md)
- [CustomMetadata](docs/v2/models/CustomMetadata.md)
- [DateType](docs/v2/models/DateType.md)
- [DateTypeDict](docs/v2/models/DateTypeDict.md)
- [DecimalType](docs/v2/models/DecimalType.md)
- [DecimalTypeDict](docs/v2/models/DecimalTypeDict.md)
- [DisplayName](docs/v2/models/DisplayName.md)
- [Distance](docs/v2/models/Distance.md)
- [DistanceDict](docs/v2/models/DistanceDict.md)
- [DistanceUnit](docs/v2/models/DistanceUnit.md)
- [DoubleType](docs/v2/models/DoubleType.md)
- [DoubleTypeDict](docs/v2/models/DoubleTypeDict.md)
- [Duration](docs/v2/models/Duration.md)
- [DurationDict](docs/v2/models/DurationDict.md)
- [EnrollmentRid](docs/v2/models/EnrollmentRid.md)
- [Field](docs/v2/models/Field.md)
- [FieldDataType](docs/v2/models/FieldDataType.md)
- [FieldDataTypeDict](docs/v2/models/FieldDataTypeDict.md)
- [FieldDict](docs/v2/models/FieldDict.md)
- [FieldName](docs/v2/models/FieldName.md)
- [FieldSchema](docs/v2/models/FieldSchema.md)
- [FieldSchemaDict](docs/v2/models/FieldSchemaDict.md)
- [Filename](docs/v2/models/Filename.md)
- [FilePath](docs/v2/models/FilePath.md)
- [FloatType](docs/v2/models/FloatType.md)
- [FloatTypeDict](docs/v2/models/FloatTypeDict.md)
- [FullRowChangeDataCaptureConfiguration](docs/v2/models/FullRowChangeDataCaptureConfiguration.md)
- [FullRowChangeDataCaptureConfigurationDict](docs/v2/models/FullRowChangeDataCaptureConfigurationDict.md)
- [GeoPointType](docs/v2/models/GeoPointType.md)
- [GeoPointTypeDict](docs/v2/models/GeoPointTypeDict.md)
- [GeoShapeType](docs/v2/models/GeoShapeType.md)
- [GeoShapeTypeDict](docs/v2/models/GeoShapeTypeDict.md)
- [GeotimeSeriesReferenceType](docs/v2/models/GeotimeSeriesReferenceType.md)
- [GeotimeSeriesReferenceTypeDict](docs/v2/models/GeotimeSeriesReferenceTypeDict.md)
- [IntegerType](docs/v2/models/IntegerType.md)
- [IntegerTypeDict](docs/v2/models/IntegerTypeDict.md)
- [LongType](docs/v2/models/LongType.md)
- [LongTypeDict](docs/v2/models/LongTypeDict.md)
- [MapFieldType](docs/v2/models/MapFieldType.md)
- [MapFieldTypeDict](docs/v2/models/MapFieldTypeDict.md)
- [MarkingId](docs/v2/models/MarkingId.md)
- [MarkingType](docs/v2/models/MarkingType.md)
- [MarkingTypeDict](docs/v2/models/MarkingTypeDict.md)
- [MediaReferenceType](docs/v2/models/MediaReferenceType.md)
- [MediaReferenceTypeDict](docs/v2/models/MediaReferenceTypeDict.md)
- [MediaSetRid](docs/v2/models/MediaSetRid.md)
- [MediaType](docs/v2/models/MediaType.md)
- [NullType](docs/v2/models/NullType.md)
- [NullTypeDict](docs/v2/models/NullTypeDict.md)
- [OrganizationRid](docs/v2/models/OrganizationRid.md)
- [PageSize](docs/v2/models/PageSize.md)
- [PageToken](docs/v2/models/PageToken.md)
- [PreviewMode](docs/v2/models/PreviewMode.md)
- [PrincipalId](docs/v2/models/PrincipalId.md)
- [PrincipalType](docs/v2/models/PrincipalType.md)
- [Realm](docs/v2/models/Realm.md)
- [ReleaseStatus](docs/v2/models/ReleaseStatus.md)
- [ShortType](docs/v2/models/ShortType.md)
- [ShortTypeDict](docs/v2/models/ShortTypeDict.md)
- [SizeBytes](docs/v2/models/SizeBytes.md)
- [StreamSchema](docs/v2/models/StreamSchema.md)
- [StreamSchemaDict](docs/v2/models/StreamSchemaDict.md)
- [StringType](docs/v2/models/StringType.md)
- [StringTypeDict](docs/v2/models/StringTypeDict.md)
- [StructFieldName](docs/v2/models/StructFieldName.md)
- [StructFieldType](docs/v2/models/StructFieldType.md)
- [StructFieldTypeDict](docs/v2/models/StructFieldTypeDict.md)
- [TimeSeriesItemType](docs/v2/models/TimeSeriesItemType.md)
- [TimeSeriesItemTypeDict](docs/v2/models/TimeSeriesItemTypeDict.md)
- [TimeseriesType](docs/v2/models/TimeseriesType.md)
- [TimeseriesTypeDict](docs/v2/models/TimeseriesTypeDict.md)
- [TimestampType](docs/v2/models/TimestampType.md)
- [TimestampTypeDict](docs/v2/models/TimestampTypeDict.md)
- [TimeUnit](docs/v2/models/TimeUnit.md)
- [TotalCount](docs/v2/models/TotalCount.md)
- [UnsupportedType](docs/v2/models/UnsupportedType.md)
- [UnsupportedTypeDict](docs/v2/models/UnsupportedTypeDict.md)
- [UpdatedBy](docs/v2/models/UpdatedBy.md)
- [UpdatedTime](docs/v2/models/UpdatedTime.md)
- [UserId](docs/v2/models/UserId.md)
- [ZoneId](docs/v2/models/ZoneId.md)
- [Branch](docs/v2/models/Branch.md)
- [BranchDict](docs/v2/models/BranchDict.md)
- [BranchName](docs/v2/models/BranchName.md)
- [Dataset](docs/v2/models/Dataset.md)
- [DatasetDict](docs/v2/models/DatasetDict.md)
- [DatasetName](docs/v2/models/DatasetName.md)
- [DatasetRid](docs/v2/models/DatasetRid.md)
- [File](docs/v2/models/File.md)
- [FileDict](docs/v2/models/FileDict.md)
- [FileUpdatedTime](docs/v2/models/FileUpdatedTime.md)
- [ListBranchesResponse](docs/v2/models/ListBranchesResponse.md)
- [ListBranchesResponseDict](docs/v2/models/ListBranchesResponseDict.md)
- [ListFilesResponse](docs/v2/models/ListFilesResponse.md)
- [ListFilesResponseDict](docs/v2/models/ListFilesResponseDict.md)
- [TableExportFormat](docs/v2/models/TableExportFormat.md)
- [Transaction](docs/v2/models/Transaction.md)
- [TransactionCreatedTime](docs/v2/models/TransactionCreatedTime.md)
- [TransactionDict](docs/v2/models/TransactionDict.md)
- [TransactionRid](docs/v2/models/TransactionRid.md)
- [TransactionStatus](docs/v2/models/TransactionStatus.md)
- [TransactionType](docs/v2/models/TransactionType.md)
- [Folder](docs/v2/models/Folder.md)
- [FolderDict](docs/v2/models/FolderDict.md)
- [FolderRid](docs/v2/models/FolderRid.md)
- [FolderType](docs/v2/models/FolderType.md)
- [ListChildrenOfFolderResponse](docs/v2/models/ListChildrenOfFolderResponse.md)
- [ListChildrenOfFolderResponseDict](docs/v2/models/ListChildrenOfFolderResponseDict.md)
- [Project](docs/v2/models/Project.md)
- [ProjectDict](docs/v2/models/ProjectDict.md)
- [ProjectRid](docs/v2/models/ProjectRid.md)
- [Resource](docs/v2/models/Resource.md)
- [ResourceDict](docs/v2/models/ResourceDict.md)
- [ResourceDisplayName](docs/v2/models/ResourceDisplayName.md)
- [ResourcePath](docs/v2/models/ResourcePath.md)
- [ResourceRid](docs/v2/models/ResourceRid.md)
- [ResourceType](docs/v2/models/ResourceType.md)
- [SpaceRid](docs/v2/models/SpaceRid.md)
- [TrashStatus](docs/v2/models/TrashStatus.md)
- [DataValue](docs/v2/models/DataValue.md)
- [ExecuteQueryResponse](docs/v2/models/ExecuteQueryResponse.md)
- [ExecuteQueryResponseDict](docs/v2/models/ExecuteQueryResponseDict.md)
- [FunctionRid](docs/v2/models/FunctionRid.md)
- [FunctionVersion](docs/v2/models/FunctionVersion.md)
- [Parameter](docs/v2/models/Parameter.md)
- [ParameterDict](docs/v2/models/ParameterDict.md)
- [ParameterId](docs/v2/models/ParameterId.md)
- [Query](docs/v2/models/Query.md)
- [QueryAggregationKeyType](docs/v2/models/QueryAggregationKeyType.md)
- [QueryAggregationKeyTypeDict](docs/v2/models/QueryAggregationKeyTypeDict.md)
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
- [QueryDict](docs/v2/models/QueryDict.md)
- [QuerySetType](docs/v2/models/QuerySetType.md)
- [QuerySetTypeDict](docs/v2/models/QuerySetTypeDict.md)
- [QueryStructField](docs/v2/models/QueryStructField.md)
- [QueryStructFieldDict](docs/v2/models/QueryStructFieldDict.md)
- [QueryStructType](docs/v2/models/QueryStructType.md)
- [QueryStructTypeDict](docs/v2/models/QueryStructTypeDict.md)
- [QueryUnionType](docs/v2/models/QueryUnionType.md)
- [QueryUnionTypeDict](docs/v2/models/QueryUnionTypeDict.md)
- [StructFieldName](docs/v2/models/StructFieldName.md)
- [ThreeDimensionalAggregation](docs/v2/models/ThreeDimensionalAggregation.md)
- [ThreeDimensionalAggregationDict](docs/v2/models/ThreeDimensionalAggregationDict.md)
- [TwoDimensionalAggregation](docs/v2/models/TwoDimensionalAggregation.md)
- [TwoDimensionalAggregationDict](docs/v2/models/TwoDimensionalAggregationDict.md)
- [ValueType](docs/v2/models/ValueType.md)
- [ValueTypeApiName](docs/v2/models/ValueTypeApiName.md)
- [ValueTypeDataType](docs/v2/models/ValueTypeDataType.md)
- [ValueTypeDataTypeArrayType](docs/v2/models/ValueTypeDataTypeArrayType.md)
- [ValueTypeDataTypeArrayTypeDict](docs/v2/models/ValueTypeDataTypeArrayTypeDict.md)
- [ValueTypeDataTypeBinaryType](docs/v2/models/ValueTypeDataTypeBinaryType.md)
- [ValueTypeDataTypeBinaryTypeDict](docs/v2/models/ValueTypeDataTypeBinaryTypeDict.md)
- [ValueTypeDataTypeBooleanType](docs/v2/models/ValueTypeDataTypeBooleanType.md)
- [ValueTypeDataTypeBooleanTypeDict](docs/v2/models/ValueTypeDataTypeBooleanTypeDict.md)
- [ValueTypeDataTypeByteType](docs/v2/models/ValueTypeDataTypeByteType.md)
- [ValueTypeDataTypeByteTypeDict](docs/v2/models/ValueTypeDataTypeByteTypeDict.md)
- [ValueTypeDataTypeDateType](docs/v2/models/ValueTypeDataTypeDateType.md)
- [ValueTypeDataTypeDateTypeDict](docs/v2/models/ValueTypeDataTypeDateTypeDict.md)
- [ValueTypeDataTypeDecimalType](docs/v2/models/ValueTypeDataTypeDecimalType.md)
- [ValueTypeDataTypeDecimalTypeDict](docs/v2/models/ValueTypeDataTypeDecimalTypeDict.md)
- [ValueTypeDataTypeDict](docs/v2/models/ValueTypeDataTypeDict.md)
- [ValueTypeDataTypeDoubleType](docs/v2/models/ValueTypeDataTypeDoubleType.md)
- [ValueTypeDataTypeDoubleTypeDict](docs/v2/models/ValueTypeDataTypeDoubleTypeDict.md)
- [ValueTypeDataTypeFloatType](docs/v2/models/ValueTypeDataTypeFloatType.md)
- [ValueTypeDataTypeFloatTypeDict](docs/v2/models/ValueTypeDataTypeFloatTypeDict.md)
- [ValueTypeDataTypeIntegerType](docs/v2/models/ValueTypeDataTypeIntegerType.md)
- [ValueTypeDataTypeIntegerTypeDict](docs/v2/models/ValueTypeDataTypeIntegerTypeDict.md)
- [ValueTypeDataTypeLongType](docs/v2/models/ValueTypeDataTypeLongType.md)
- [ValueTypeDataTypeLongTypeDict](docs/v2/models/ValueTypeDataTypeLongTypeDict.md)
- [ValueTypeDataTypeMapType](docs/v2/models/ValueTypeDataTypeMapType.md)
- [ValueTypeDataTypeMapTypeDict](docs/v2/models/ValueTypeDataTypeMapTypeDict.md)
- [ValueTypeDataTypeOptionalType](docs/v2/models/ValueTypeDataTypeOptionalType.md)
- [ValueTypeDataTypeOptionalTypeDict](docs/v2/models/ValueTypeDataTypeOptionalTypeDict.md)
- [ValueTypeDataTypeReferencedType](docs/v2/models/ValueTypeDataTypeReferencedType.md)
- [ValueTypeDataTypeReferencedTypeDict](docs/v2/models/ValueTypeDataTypeReferencedTypeDict.md)
- [ValueTypeDataTypeShortType](docs/v2/models/ValueTypeDataTypeShortType.md)
- [ValueTypeDataTypeShortTypeDict](docs/v2/models/ValueTypeDataTypeShortTypeDict.md)
- [ValueTypeDataTypeStringType](docs/v2/models/ValueTypeDataTypeStringType.md)
- [ValueTypeDataTypeStringTypeDict](docs/v2/models/ValueTypeDataTypeStringTypeDict.md)
- [ValueTypeDataTypeStructElement](docs/v2/models/ValueTypeDataTypeStructElement.md)
- [ValueTypeDataTypeStructElementDict](docs/v2/models/ValueTypeDataTypeStructElementDict.md)
- [ValueTypeDataTypeStructFieldIdentifier](docs/v2/models/ValueTypeDataTypeStructFieldIdentifier.md)
- [ValueTypeDataTypeStructType](docs/v2/models/ValueTypeDataTypeStructType.md)
- [ValueTypeDataTypeStructTypeDict](docs/v2/models/ValueTypeDataTypeStructTypeDict.md)
- [ValueTypeDataTypeTimestampType](docs/v2/models/ValueTypeDataTypeTimestampType.md)
- [ValueTypeDataTypeTimestampTypeDict](docs/v2/models/ValueTypeDataTypeTimestampTypeDict.md)
- [ValueTypeDataTypeUnionType](docs/v2/models/ValueTypeDataTypeUnionType.md)
- [ValueTypeDataTypeUnionTypeDict](docs/v2/models/ValueTypeDataTypeUnionTypeDict.md)
- [ValueTypeDescription](docs/v2/models/ValueTypeDescription.md)
- [ValueTypeDict](docs/v2/models/ValueTypeDict.md)
- [ValueTypeReference](docs/v2/models/ValueTypeReference.md)
- [ValueTypeReferenceDict](docs/v2/models/ValueTypeReferenceDict.md)
- [ValueTypeRid](docs/v2/models/ValueTypeRid.md)
- [ValueTypeVersion](docs/v2/models/ValueTypeVersion.md)
- [ValueTypeVersionId](docs/v2/models/ValueTypeVersionId.md)
- [VersionId](docs/v2/models/VersionId.md)
- [VersionIdDict](docs/v2/models/VersionIdDict.md)
- [BBox](docs/v2/models/BBox.md)
- [Coordinate](docs/v2/models/Coordinate.md)
- [GeoPoint](docs/v2/models/GeoPoint.md)
- [GeoPointDict](docs/v2/models/GeoPointDict.md)
- [LinearRing](docs/v2/models/LinearRing.md)
- [Polygon](docs/v2/models/Polygon.md)
- [PolygonDict](docs/v2/models/PolygonDict.md)
- [Position](docs/v2/models/Position.md)
- [AbsoluteTimeRangeDict](docs/v2/models/AbsoluteTimeRangeDict.md)
- [ActionParameterArrayType](docs/v2/models/ActionParameterArrayType.md)
- [ActionParameterArrayTypeDict](docs/v2/models/ActionParameterArrayTypeDict.md)
- [ActionParameterType](docs/v2/models/ActionParameterType.md)
- [ActionParameterTypeDict](docs/v2/models/ActionParameterTypeDict.md)
- [ActionParameterV2](docs/v2/models/ActionParameterV2.md)
- [ActionParameterV2Dict](docs/v2/models/ActionParameterV2Dict.md)
- [ActionResults](docs/v2/models/ActionResults.md)
- [ActionResultsDict](docs/v2/models/ActionResultsDict.md)
- [ActionTypeApiName](docs/v2/models/ActionTypeApiName.md)
- [ActionTypeRid](docs/v2/models/ActionTypeRid.md)
- [ActionTypeV2](docs/v2/models/ActionTypeV2.md)
- [ActionTypeV2Dict](docs/v2/models/ActionTypeV2Dict.md)
- [AddLink](docs/v2/models/AddLink.md)
- [AddLinkDict](docs/v2/models/AddLinkDict.md)
- [AddObject](docs/v2/models/AddObject.md)
- [AddObjectDict](docs/v2/models/AddObjectDict.md)
- [AggregateObjectsResponseItemV2](docs/v2/models/AggregateObjectsResponseItemV2.md)
- [AggregateObjectsResponseItemV2Dict](docs/v2/models/AggregateObjectsResponseItemV2Dict.md)
- [AggregateObjectsResponseV2](docs/v2/models/AggregateObjectsResponseV2.md)
- [AggregateObjectsResponseV2Dict](docs/v2/models/AggregateObjectsResponseV2Dict.md)
- [AggregationAccuracy](docs/v2/models/AggregationAccuracy.md)
- [AggregationAccuracyRequest](docs/v2/models/AggregationAccuracyRequest.md)
- [AggregationDurationGroupingV2Dict](docs/v2/models/AggregationDurationGroupingV2Dict.md)
- [AggregationExactGroupingV2Dict](docs/v2/models/AggregationExactGroupingV2Dict.md)
- [AggregationFixedWidthGroupingV2Dict](docs/v2/models/AggregationFixedWidthGroupingV2Dict.md)
- [AggregationGroupByV2Dict](docs/v2/models/AggregationGroupByV2Dict.md)
- [AggregationGroupKeyV2](docs/v2/models/AggregationGroupKeyV2.md)
- [AggregationGroupValueV2](docs/v2/models/AggregationGroupValueV2.md)
- [AggregationMetricName](docs/v2/models/AggregationMetricName.md)
- [AggregationMetricResultV2](docs/v2/models/AggregationMetricResultV2.md)
- [AggregationMetricResultV2Dict](docs/v2/models/AggregationMetricResultV2Dict.md)
- [AggregationRangesGroupingV2Dict](docs/v2/models/AggregationRangesGroupingV2Dict.md)
- [AggregationRangeV2Dict](docs/v2/models/AggregationRangeV2Dict.md)
- [AggregationV2Dict](docs/v2/models/AggregationV2Dict.md)
- [AndQueryV2](docs/v2/models/AndQueryV2.md)
- [AndQueryV2Dict](docs/v2/models/AndQueryV2Dict.md)
- [ApplyActionMode](docs/v2/models/ApplyActionMode.md)
- [ApplyActionRequestOptionsDict](docs/v2/models/ApplyActionRequestOptionsDict.md)
- [ApproximateDistinctAggregationV2Dict](docs/v2/models/ApproximateDistinctAggregationV2Dict.md)
- [ApproximatePercentileAggregationV2Dict](docs/v2/models/ApproximatePercentileAggregationV2Dict.md)
- [ArraySizeConstraint](docs/v2/models/ArraySizeConstraint.md)
- [ArraySizeConstraintDict](docs/v2/models/ArraySizeConstraintDict.md)
- [ArtifactRepositoryRid](docs/v2/models/ArtifactRepositoryRid.md)
- [AttachmentMetadataResponse](docs/v2/models/AttachmentMetadataResponse.md)
- [AttachmentMetadataResponseDict](docs/v2/models/AttachmentMetadataResponseDict.md)
- [AttachmentRid](docs/v2/models/AttachmentRid.md)
- [AttachmentV2](docs/v2/models/AttachmentV2.md)
- [AttachmentV2Dict](docs/v2/models/AttachmentV2Dict.md)
- [AvgAggregationV2Dict](docs/v2/models/AvgAggregationV2Dict.md)
- [BatchApplyActionRequestItemDict](docs/v2/models/BatchApplyActionRequestItemDict.md)
- [BatchApplyActionRequestOptionsDict](docs/v2/models/BatchApplyActionRequestOptionsDict.md)
- [BatchApplyActionResponseV2](docs/v2/models/BatchApplyActionResponseV2.md)
- [BatchApplyActionResponseV2Dict](docs/v2/models/BatchApplyActionResponseV2Dict.md)
- [BlueprintIcon](docs/v2/models/BlueprintIcon.md)
- [BlueprintIconDict](docs/v2/models/BlueprintIconDict.md)
- [BoundingBoxValue](docs/v2/models/BoundingBoxValue.md)
- [BoundingBoxValueDict](docs/v2/models/BoundingBoxValueDict.md)
- [CenterPoint](docs/v2/models/CenterPoint.md)
- [CenterPointDict](docs/v2/models/CenterPointDict.md)
- [CenterPointTypes](docs/v2/models/CenterPointTypes.md)
- [CenterPointTypesDict](docs/v2/models/CenterPointTypesDict.md)
- [ContainsAllTermsInOrderPrefixLastTerm](docs/v2/models/ContainsAllTermsInOrderPrefixLastTerm.md)
- [ContainsAllTermsInOrderPrefixLastTermDict](docs/v2/models/ContainsAllTermsInOrderPrefixLastTermDict.md)
- [ContainsAllTermsInOrderQuery](docs/v2/models/ContainsAllTermsInOrderQuery.md)
- [ContainsAllTermsInOrderQueryDict](docs/v2/models/ContainsAllTermsInOrderQueryDict.md)
- [ContainsAllTermsQuery](docs/v2/models/ContainsAllTermsQuery.md)
- [ContainsAllTermsQueryDict](docs/v2/models/ContainsAllTermsQueryDict.md)
- [ContainsAnyTermQuery](docs/v2/models/ContainsAnyTermQuery.md)
- [ContainsAnyTermQueryDict](docs/v2/models/ContainsAnyTermQueryDict.md)
- [ContainsQueryV2](docs/v2/models/ContainsQueryV2.md)
- [ContainsQueryV2Dict](docs/v2/models/ContainsQueryV2Dict.md)
- [CountAggregationV2Dict](docs/v2/models/CountAggregationV2Dict.md)
- [CountObjectsResponseV2](docs/v2/models/CountObjectsResponseV2.md)
- [CountObjectsResponseV2Dict](docs/v2/models/CountObjectsResponseV2Dict.md)
- [CreateInterfaceObjectRule](docs/v2/models/CreateInterfaceObjectRule.md)
- [CreateInterfaceObjectRuleDict](docs/v2/models/CreateInterfaceObjectRuleDict.md)
- [CreateLinkRule](docs/v2/models/CreateLinkRule.md)
- [CreateLinkRuleDict](docs/v2/models/CreateLinkRuleDict.md)
- [CreateObjectRule](docs/v2/models/CreateObjectRule.md)
- [CreateObjectRuleDict](docs/v2/models/CreateObjectRuleDict.md)
- [CreateTemporaryObjectSetResponseV2](docs/v2/models/CreateTemporaryObjectSetResponseV2.md)
- [CreateTemporaryObjectSetResponseV2Dict](docs/v2/models/CreateTemporaryObjectSetResponseV2Dict.md)
- [DataValue](docs/v2/models/DataValue.md)
- [DeleteLinkRule](docs/v2/models/DeleteLinkRule.md)
- [DeleteLinkRuleDict](docs/v2/models/DeleteLinkRuleDict.md)
- [DeleteObjectRule](docs/v2/models/DeleteObjectRule.md)
- [DeleteObjectRuleDict](docs/v2/models/DeleteObjectRuleDict.md)
- [DoesNotIntersectBoundingBoxQuery](docs/v2/models/DoesNotIntersectBoundingBoxQuery.md)
- [DoesNotIntersectBoundingBoxQueryDict](docs/v2/models/DoesNotIntersectBoundingBoxQueryDict.md)
- [DoesNotIntersectPolygonQuery](docs/v2/models/DoesNotIntersectPolygonQuery.md)
- [DoesNotIntersectPolygonQueryDict](docs/v2/models/DoesNotIntersectPolygonQueryDict.md)
- [EqualsQueryV2](docs/v2/models/EqualsQueryV2.md)
- [EqualsQueryV2Dict](docs/v2/models/EqualsQueryV2Dict.md)
- [ExactDistinctAggregationV2Dict](docs/v2/models/ExactDistinctAggregationV2Dict.md)
- [ExecuteQueryResponse](docs/v2/models/ExecuteQueryResponse.md)
- [ExecuteQueryResponseDict](docs/v2/models/ExecuteQueryResponseDict.md)
- [FunctionRid](docs/v2/models/FunctionRid.md)
- [FunctionVersion](docs/v2/models/FunctionVersion.md)
- [FuzzyV2](docs/v2/models/FuzzyV2.md)
- [GroupMemberConstraint](docs/v2/models/GroupMemberConstraint.md)
- [GroupMemberConstraintDict](docs/v2/models/GroupMemberConstraintDict.md)
- [GteQueryV2](docs/v2/models/GteQueryV2.md)
- [GteQueryV2Dict](docs/v2/models/GteQueryV2Dict.md)
- [GtQueryV2](docs/v2/models/GtQueryV2.md)
- [GtQueryV2Dict](docs/v2/models/GtQueryV2Dict.md)
- [Icon](docs/v2/models/Icon.md)
- [IconDict](docs/v2/models/IconDict.md)
- [InQuery](docs/v2/models/InQuery.md)
- [InQueryDict](docs/v2/models/InQueryDict.md)
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
- [IsNullQueryV2](docs/v2/models/IsNullQueryV2.md)
- [IsNullQueryV2Dict](docs/v2/models/IsNullQueryV2Dict.md)
- [LinkedInterfaceTypeApiName](docs/v2/models/LinkedInterfaceTypeApiName.md)
- [LinkedInterfaceTypeApiNameDict](docs/v2/models/LinkedInterfaceTypeApiNameDict.md)
- [LinkedObjectTypeApiName](docs/v2/models/LinkedObjectTypeApiName.md)
- [LinkedObjectTypeApiNameDict](docs/v2/models/LinkedObjectTypeApiNameDict.md)
- [LinkSideObject](docs/v2/models/LinkSideObject.md)
- [LinkSideObjectDict](docs/v2/models/LinkSideObjectDict.md)
- [LinkTypeApiName](docs/v2/models/LinkTypeApiName.md)
- [LinkTypeRid](docs/v2/models/LinkTypeRid.md)
- [LinkTypeSideCardinality](docs/v2/models/LinkTypeSideCardinality.md)
- [LinkTypeSideV2](docs/v2/models/LinkTypeSideV2.md)
- [LinkTypeSideV2Dict](docs/v2/models/LinkTypeSideV2Dict.md)
- [ListActionTypesResponseV2](docs/v2/models/ListActionTypesResponseV2.md)
- [ListActionTypesResponseV2Dict](docs/v2/models/ListActionTypesResponseV2Dict.md)
- [ListAttachmentsResponseV2](docs/v2/models/ListAttachmentsResponseV2.md)
- [ListAttachmentsResponseV2Dict](docs/v2/models/ListAttachmentsResponseV2Dict.md)
- [ListInterfaceTypesResponse](docs/v2/models/ListInterfaceTypesResponse.md)
- [ListInterfaceTypesResponseDict](docs/v2/models/ListInterfaceTypesResponseDict.md)
- [ListLinkedObjectsResponseV2](docs/v2/models/ListLinkedObjectsResponseV2.md)
- [ListLinkedObjectsResponseV2Dict](docs/v2/models/ListLinkedObjectsResponseV2Dict.md)
- [ListObjectsResponseV2](docs/v2/models/ListObjectsResponseV2.md)
- [ListObjectsResponseV2Dict](docs/v2/models/ListObjectsResponseV2Dict.md)
- [ListObjectTypesV2Response](docs/v2/models/ListObjectTypesV2Response.md)
- [ListObjectTypesV2ResponseDict](docs/v2/models/ListObjectTypesV2ResponseDict.md)
- [ListOutgoingLinkTypesResponseV2](docs/v2/models/ListOutgoingLinkTypesResponseV2.md)
- [ListOutgoingLinkTypesResponseV2Dict](docs/v2/models/ListOutgoingLinkTypesResponseV2Dict.md)
- [ListQueryTypesResponseV2](docs/v2/models/ListQueryTypesResponseV2.md)
- [ListQueryTypesResponseV2Dict](docs/v2/models/ListQueryTypesResponseV2Dict.md)
- [LoadObjectSetResponseV2](docs/v2/models/LoadObjectSetResponseV2.md)
- [LoadObjectSetResponseV2Dict](docs/v2/models/LoadObjectSetResponseV2Dict.md)
- [LogicRule](docs/v2/models/LogicRule.md)
- [LogicRuleDict](docs/v2/models/LogicRuleDict.md)
- [LteQueryV2](docs/v2/models/LteQueryV2.md)
- [LteQueryV2Dict](docs/v2/models/LteQueryV2Dict.md)
- [LtQueryV2](docs/v2/models/LtQueryV2.md)
- [LtQueryV2Dict](docs/v2/models/LtQueryV2Dict.md)
- [MaxAggregationV2Dict](docs/v2/models/MaxAggregationV2Dict.md)
- [MinAggregationV2Dict](docs/v2/models/MinAggregationV2Dict.md)
- [ModifyInterfaceObjectRule](docs/v2/models/ModifyInterfaceObjectRule.md)
- [ModifyInterfaceObjectRuleDict](docs/v2/models/ModifyInterfaceObjectRuleDict.md)
- [ModifyObject](docs/v2/models/ModifyObject.md)
- [ModifyObjectDict](docs/v2/models/ModifyObjectDict.md)
- [ModifyObjectRule](docs/v2/models/ModifyObjectRule.md)
- [ModifyObjectRuleDict](docs/v2/models/ModifyObjectRuleDict.md)
- [NotQueryV2](docs/v2/models/NotQueryV2.md)
- [NotQueryV2Dict](docs/v2/models/NotQueryV2Dict.md)
- [ObjectEdit](docs/v2/models/ObjectEdit.md)
- [ObjectEditDict](docs/v2/models/ObjectEditDict.md)
- [ObjectEdits](docs/v2/models/ObjectEdits.md)
- [ObjectEditsDict](docs/v2/models/ObjectEditsDict.md)
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
- [ObjectSetSubtractType](docs/v2/models/ObjectSetSubtractType.md)
- [ObjectSetSubtractTypeDict](docs/v2/models/ObjectSetSubtractTypeDict.md)
- [ObjectSetUnionType](docs/v2/models/ObjectSetUnionType.md)
- [ObjectSetUnionTypeDict](docs/v2/models/ObjectSetUnionTypeDict.md)
- [ObjectTypeApiName](docs/v2/models/ObjectTypeApiName.md)
- [ObjectTypeEdits](docs/v2/models/ObjectTypeEdits.md)
- [ObjectTypeEditsDict](docs/v2/models/ObjectTypeEditsDict.md)
- [ObjectTypeFullMetadata](docs/v2/models/ObjectTypeFullMetadata.md)
- [ObjectTypeFullMetadataDict](docs/v2/models/ObjectTypeFullMetadataDict.md)
- [ObjectTypeId](docs/v2/models/ObjectTypeId.md)
- [ObjectTypeInterfaceImplementation](docs/v2/models/ObjectTypeInterfaceImplementation.md)
- [ObjectTypeInterfaceImplementationDict](docs/v2/models/ObjectTypeInterfaceImplementationDict.md)
- [ObjectTypeRid](docs/v2/models/ObjectTypeRid.md)
- [ObjectTypeV2](docs/v2/models/ObjectTypeV2.md)
- [ObjectTypeV2Dict](docs/v2/models/ObjectTypeV2Dict.md)
- [ObjectTypeVisibility](docs/v2/models/ObjectTypeVisibility.md)
- [OneOfConstraint](docs/v2/models/OneOfConstraint.md)
- [OneOfConstraintDict](docs/v2/models/OneOfConstraintDict.md)
- [OntologyApiName](docs/v2/models/OntologyApiName.md)
- [OntologyFullMetadata](docs/v2/models/OntologyFullMetadata.md)
- [OntologyFullMetadataDict](docs/v2/models/OntologyFullMetadataDict.md)
- [OntologyIdentifier](docs/v2/models/OntologyIdentifier.md)
- [OntologyObjectArrayType](docs/v2/models/OntologyObjectArrayType.md)
- [OntologyObjectArrayTypeDict](docs/v2/models/OntologyObjectArrayTypeDict.md)
- [OntologyObjectSetType](docs/v2/models/OntologyObjectSetType.md)
- [OntologyObjectSetTypeDict](docs/v2/models/OntologyObjectSetTypeDict.md)
- [OntologyObjectType](docs/v2/models/OntologyObjectType.md)
- [OntologyObjectTypeDict](docs/v2/models/OntologyObjectTypeDict.md)
- [OntologyObjectV2](docs/v2/models/OntologyObjectV2.md)
- [OntologyRid](docs/v2/models/OntologyRid.md)
- [OntologyV2](docs/v2/models/OntologyV2.md)
- [OntologyV2Dict](docs/v2/models/OntologyV2Dict.md)
- [OrderBy](docs/v2/models/OrderBy.md)
- [OrderByDirection](docs/v2/models/OrderByDirection.md)
- [OrQueryV2](docs/v2/models/OrQueryV2.md)
- [OrQueryV2Dict](docs/v2/models/OrQueryV2Dict.md)
- [ParameterEvaluatedConstraint](docs/v2/models/ParameterEvaluatedConstraint.md)
- [ParameterEvaluatedConstraintDict](docs/v2/models/ParameterEvaluatedConstraintDict.md)
- [ParameterEvaluationResult](docs/v2/models/ParameterEvaluationResult.md)
- [ParameterEvaluationResultDict](docs/v2/models/ParameterEvaluationResultDict.md)
- [ParameterId](docs/v2/models/ParameterId.md)
- [ParameterOption](docs/v2/models/ParameterOption.md)
- [ParameterOptionDict](docs/v2/models/ParameterOptionDict.md)
- [PolygonValue](docs/v2/models/PolygonValue.md)
- [PolygonValueDict](docs/v2/models/PolygonValueDict.md)
- [PropertyApiName](docs/v2/models/PropertyApiName.md)
- [PropertyTypeRid](docs/v2/models/PropertyTypeRid.md)
- [PropertyV2](docs/v2/models/PropertyV2.md)
- [PropertyV2Dict](docs/v2/models/PropertyV2Dict.md)
- [PropertyValue](docs/v2/models/PropertyValue.md)
- [PropertyValueEscapedString](docs/v2/models/PropertyValueEscapedString.md)
- [QueryAggregationKeyType](docs/v2/models/QueryAggregationKeyType.md)
- [QueryAggregationKeyTypeDict](docs/v2/models/QueryAggregationKeyTypeDict.md)
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
- [QueryParameterV2](docs/v2/models/QueryParameterV2.md)
- [QueryParameterV2Dict](docs/v2/models/QueryParameterV2Dict.md)
- [QuerySetType](docs/v2/models/QuerySetType.md)
- [QuerySetTypeDict](docs/v2/models/QuerySetTypeDict.md)
- [QueryStructField](docs/v2/models/QueryStructField.md)
- [QueryStructFieldDict](docs/v2/models/QueryStructFieldDict.md)
- [QueryStructType](docs/v2/models/QueryStructType.md)
- [QueryStructTypeDict](docs/v2/models/QueryStructTypeDict.md)
- [QueryTypeV2](docs/v2/models/QueryTypeV2.md)
- [QueryTypeV2Dict](docs/v2/models/QueryTypeV2Dict.md)
- [QueryUnionType](docs/v2/models/QueryUnionType.md)
- [QueryUnionTypeDict](docs/v2/models/QueryUnionTypeDict.md)
- [RangeConstraint](docs/v2/models/RangeConstraint.md)
- [RangeConstraintDict](docs/v2/models/RangeConstraintDict.md)
- [RelativeTimeDict](docs/v2/models/RelativeTimeDict.md)
- [RelativeTimeRangeDict](docs/v2/models/RelativeTimeRangeDict.md)
- [RelativeTimeRelation](docs/v2/models/RelativeTimeRelation.md)
- [RelativeTimeSeriesTimeUnit](docs/v2/models/RelativeTimeSeriesTimeUnit.md)
- [ReturnEditsMode](docs/v2/models/ReturnEditsMode.md)
- [SdkPackageName](docs/v2/models/SdkPackageName.md)
- [SearchJsonQueryV2](docs/v2/models/SearchJsonQueryV2.md)
- [SearchJsonQueryV2Dict](docs/v2/models/SearchJsonQueryV2Dict.md)
- [SearchObjectsResponseV2](docs/v2/models/SearchObjectsResponseV2.md)
- [SearchObjectsResponseV2Dict](docs/v2/models/SearchObjectsResponseV2Dict.md)
- [SearchOrderByV2Dict](docs/v2/models/SearchOrderByV2Dict.md)
- [SearchOrderingV2Dict](docs/v2/models/SearchOrderingV2Dict.md)
- [SelectedPropertyApiName](docs/v2/models/SelectedPropertyApiName.md)
- [SharedPropertyType](docs/v2/models/SharedPropertyType.md)
- [SharedPropertyTypeApiName](docs/v2/models/SharedPropertyTypeApiName.md)
- [SharedPropertyTypeDict](docs/v2/models/SharedPropertyTypeDict.md)
- [SharedPropertyTypeRid](docs/v2/models/SharedPropertyTypeRid.md)
- [StartsWithQuery](docs/v2/models/StartsWithQuery.md)
- [StartsWithQueryDict](docs/v2/models/StartsWithQueryDict.md)
- [StringLengthConstraint](docs/v2/models/StringLengthConstraint.md)
- [StringLengthConstraintDict](docs/v2/models/StringLengthConstraintDict.md)
- [StringRegexMatchConstraint](docs/v2/models/StringRegexMatchConstraint.md)
- [StringRegexMatchConstraintDict](docs/v2/models/StringRegexMatchConstraintDict.md)
- [SubmissionCriteriaEvaluation](docs/v2/models/SubmissionCriteriaEvaluation.md)
- [SubmissionCriteriaEvaluationDict](docs/v2/models/SubmissionCriteriaEvaluationDict.md)
- [SumAggregationV2Dict](docs/v2/models/SumAggregationV2Dict.md)
- [SyncApplyActionResponseV2](docs/v2/models/SyncApplyActionResponseV2.md)
- [SyncApplyActionResponseV2Dict](docs/v2/models/SyncApplyActionResponseV2Dict.md)
- [ThreeDimensionalAggregation](docs/v2/models/ThreeDimensionalAggregation.md)
- [ThreeDimensionalAggregationDict](docs/v2/models/ThreeDimensionalAggregationDict.md)
- [TimeRangeDict](docs/v2/models/TimeRangeDict.md)
- [TimeSeriesPoint](docs/v2/models/TimeSeriesPoint.md)
- [TimeSeriesPointDict](docs/v2/models/TimeSeriesPointDict.md)
- [TwoDimensionalAggregation](docs/v2/models/TwoDimensionalAggregation.md)
- [TwoDimensionalAggregationDict](docs/v2/models/TwoDimensionalAggregationDict.md)
- [UnevaluableConstraint](docs/v2/models/UnevaluableConstraint.md)
- [UnevaluableConstraintDict](docs/v2/models/UnevaluableConstraintDict.md)
- [ValidateActionResponseV2](docs/v2/models/ValidateActionResponseV2.md)
- [ValidateActionResponseV2Dict](docs/v2/models/ValidateActionResponseV2Dict.md)
- [ValidationResult](docs/v2/models/ValidationResult.md)
- [WithinBoundingBoxPoint](docs/v2/models/WithinBoundingBoxPoint.md)
- [WithinBoundingBoxPointDict](docs/v2/models/WithinBoundingBoxPointDict.md)
- [WithinBoundingBoxQuery](docs/v2/models/WithinBoundingBoxQuery.md)
- [WithinBoundingBoxQueryDict](docs/v2/models/WithinBoundingBoxQueryDict.md)
- [WithinDistanceOfQuery](docs/v2/models/WithinDistanceOfQuery.md)
- [WithinDistanceOfQueryDict](docs/v2/models/WithinDistanceOfQueryDict.md)
- [WithinPolygonQuery](docs/v2/models/WithinPolygonQuery.md)
- [WithinPolygonQueryDict](docs/v2/models/WithinPolygonQueryDict.md)
- [AbortOnFailure](docs/v2/models/AbortOnFailure.md)
- [Action](docs/v2/models/Action.md)
- [ActionDict](docs/v2/models/ActionDict.md)
- [AndTrigger](docs/v2/models/AndTrigger.md)
- [AndTriggerDict](docs/v2/models/AndTriggerDict.md)
- [Build](docs/v2/models/Build.md)
- [BuildableRid](docs/v2/models/BuildableRid.md)
- [BuildDict](docs/v2/models/BuildDict.md)
- [BuildRid](docs/v2/models/BuildRid.md)
- [BuildStatus](docs/v2/models/BuildStatus.md)
- [BuildTarget](docs/v2/models/BuildTarget.md)
- [BuildTargetDict](docs/v2/models/BuildTargetDict.md)
- [ConnectingTarget](docs/v2/models/ConnectingTarget.md)
- [ConnectingTargetDict](docs/v2/models/ConnectingTargetDict.md)
- [CreateScheduleRequestActionBuildTargetConnectingTargetDict](docs/v2/models/CreateScheduleRequestActionBuildTargetConnectingTargetDict.md)
- [CreateScheduleRequestActionBuildTargetDict](docs/v2/models/CreateScheduleRequestActionBuildTargetDict.md)
- [CreateScheduleRequestActionBuildTargetManualTargetDict](docs/v2/models/CreateScheduleRequestActionBuildTargetManualTargetDict.md)
- [CreateScheduleRequestActionBuildTargetUpstreamTargetDict](docs/v2/models/CreateScheduleRequestActionBuildTargetUpstreamTargetDict.md)
- [CreateScheduleRequestActionDict](docs/v2/models/CreateScheduleRequestActionDict.md)
- [CreateScheduleRequestScopeModeDict](docs/v2/models/CreateScheduleRequestScopeModeDict.md)
- [CreateScheduleRequestScopeModeProjectScopeDict](docs/v2/models/CreateScheduleRequestScopeModeProjectScopeDict.md)
- [CreateScheduleRequestScopeModeUserScopeDict](docs/v2/models/CreateScheduleRequestScopeModeUserScopeDict.md)
- [CronExpression](docs/v2/models/CronExpression.md)
- [DatasetUpdatedTrigger](docs/v2/models/DatasetUpdatedTrigger.md)
- [DatasetUpdatedTriggerDict](docs/v2/models/DatasetUpdatedTriggerDict.md)
- [FallbackBranches](docs/v2/models/FallbackBranches.md)
- [ForceBuild](docs/v2/models/ForceBuild.md)
- [JobSucceededTrigger](docs/v2/models/JobSucceededTrigger.md)
- [JobSucceededTriggerDict](docs/v2/models/JobSucceededTriggerDict.md)
- [ManualTarget](docs/v2/models/ManualTarget.md)
- [ManualTargetDict](docs/v2/models/ManualTargetDict.md)
- [MediaSetUpdatedTrigger](docs/v2/models/MediaSetUpdatedTrigger.md)
- [MediaSetUpdatedTriggerDict](docs/v2/models/MediaSetUpdatedTriggerDict.md)
- [NewLogicTrigger](docs/v2/models/NewLogicTrigger.md)
- [NewLogicTriggerDict](docs/v2/models/NewLogicTriggerDict.md)
- [NotificationsEnabled](docs/v2/models/NotificationsEnabled.md)
- [OrTrigger](docs/v2/models/OrTrigger.md)
- [OrTriggerDict](docs/v2/models/OrTriggerDict.md)
- [ProjectScope](docs/v2/models/ProjectScope.md)
- [ProjectScopeDict](docs/v2/models/ProjectScopeDict.md)
- [ReplaceScheduleRequestActionBuildTargetConnectingTargetDict](docs/v2/models/ReplaceScheduleRequestActionBuildTargetConnectingTargetDict.md)
- [ReplaceScheduleRequestActionBuildTargetDict](docs/v2/models/ReplaceScheduleRequestActionBuildTargetDict.md)
- [ReplaceScheduleRequestActionBuildTargetManualTargetDict](docs/v2/models/ReplaceScheduleRequestActionBuildTargetManualTargetDict.md)
- [ReplaceScheduleRequestActionBuildTargetUpstreamTargetDict](docs/v2/models/ReplaceScheduleRequestActionBuildTargetUpstreamTargetDict.md)
- [ReplaceScheduleRequestActionDict](docs/v2/models/ReplaceScheduleRequestActionDict.md)
- [ReplaceScheduleRequestScopeModeDict](docs/v2/models/ReplaceScheduleRequestScopeModeDict.md)
- [ReplaceScheduleRequestScopeModeProjectScopeDict](docs/v2/models/ReplaceScheduleRequestScopeModeProjectScopeDict.md)
- [ReplaceScheduleRequestScopeModeUserScopeDict](docs/v2/models/ReplaceScheduleRequestScopeModeUserScopeDict.md)
- [RetryBackoffDuration](docs/v2/models/RetryBackoffDuration.md)
- [RetryBackoffDurationDict](docs/v2/models/RetryBackoffDurationDict.md)
- [RetryCount](docs/v2/models/RetryCount.md)
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
- [ScheduleVersionRid](docs/v2/models/ScheduleVersionRid.md)
- [ScopeMode](docs/v2/models/ScopeMode.md)
- [ScopeModeDict](docs/v2/models/ScopeModeDict.md)
- [TimeTrigger](docs/v2/models/TimeTrigger.md)
- [TimeTriggerDict](docs/v2/models/TimeTriggerDict.md)
- [Trigger](docs/v2/models/Trigger.md)
- [TriggerDict](docs/v2/models/TriggerDict.md)
- [UpstreamTarget](docs/v2/models/UpstreamTarget.md)
- [UpstreamTargetDict](docs/v2/models/UpstreamTargetDict.md)
- [UserScope](docs/v2/models/UserScope.md)
- [UserScopeDict](docs/v2/models/UserScopeDict.md)
- [Compressed](docs/v2/models/Compressed.md)
- [CreateStreamRequestStreamSchemaDict](docs/v2/models/CreateStreamRequestStreamSchemaDict.md)
- [Dataset](docs/v2/models/Dataset.md)
- [DatasetDict](docs/v2/models/DatasetDict.md)
- [PartitionsCount](docs/v2/models/PartitionsCount.md)
- [Record](docs/v2/models/Record.md)
- [Stream](docs/v2/models/Stream.md)
- [StreamDict](docs/v2/models/StreamDict.md)
- [StreamType](docs/v2/models/StreamType.md)
- [ViewRid](docs/v2/models/ViewRid.md)
- [ListVersionsResponse](docs/v2/models/ListVersionsResponse.md)
- [ListVersionsResponseDict](docs/v2/models/ListVersionsResponseDict.md)
- [Subdomain](docs/v2/models/Subdomain.md)
- [ThirdPartyApplication](docs/v2/models/ThirdPartyApplication.md)
- [ThirdPartyApplicationDict](docs/v2/models/ThirdPartyApplicationDict.md)
- [ThirdPartyApplicationRid](docs/v2/models/ThirdPartyApplicationRid.md)
- [Version](docs/v2/models/Version.md)
- [VersionDict](docs/v2/models/VersionDict.md)
- [VersionVersion](docs/v2/models/VersionVersion.md)
- [Website](docs/v2/models/Website.md)
- [WebsiteDict](docs/v2/models/WebsiteDict.md)

<a id="models-v1-link"></a>
## Documentation for V1 models

- [AnyType](docs/v1/models/AnyType.md)
- [AnyTypeDict](docs/v1/models/AnyTypeDict.md)
- [BinaryType](docs/v1/models/BinaryType.md)
- [BinaryTypeDict](docs/v1/models/BinaryTypeDict.md)
- [BooleanType](docs/v1/models/BooleanType.md)
- [BooleanTypeDict](docs/v1/models/BooleanTypeDict.md)
- [ByteType](docs/v1/models/ByteType.md)
- [ByteTypeDict](docs/v1/models/ByteTypeDict.md)
- [DateType](docs/v1/models/DateType.md)
- [DateTypeDict](docs/v1/models/DateTypeDict.md)
- [DecimalType](docs/v1/models/DecimalType.md)
- [DecimalTypeDict](docs/v1/models/DecimalTypeDict.md)
- [DisplayName](docs/v1/models/DisplayName.md)
- [DoubleType](docs/v1/models/DoubleType.md)
- [DoubleTypeDict](docs/v1/models/DoubleTypeDict.md)
- [Duration](docs/v1/models/Duration.md)
- [FilePath](docs/v1/models/FilePath.md)
- [FloatType](docs/v1/models/FloatType.md)
- [FloatTypeDict](docs/v1/models/FloatTypeDict.md)
- [FolderRid](docs/v1/models/FolderRid.md)
- [IntegerType](docs/v1/models/IntegerType.md)
- [IntegerTypeDict](docs/v1/models/IntegerTypeDict.md)
- [LongType](docs/v1/models/LongType.md)
- [LongTypeDict](docs/v1/models/LongTypeDict.md)
- [MarkingType](docs/v1/models/MarkingType.md)
- [MarkingTypeDict](docs/v1/models/MarkingTypeDict.md)
- [PageSize](docs/v1/models/PageSize.md)
- [PageToken](docs/v1/models/PageToken.md)
- [PreviewMode](docs/v1/models/PreviewMode.md)
- [ReleaseStatus](docs/v1/models/ReleaseStatus.md)
- [ShortType](docs/v1/models/ShortType.md)
- [ShortTypeDict](docs/v1/models/ShortTypeDict.md)
- [StringType](docs/v1/models/StringType.md)
- [StringTypeDict](docs/v1/models/StringTypeDict.md)
- [StructFieldName](docs/v1/models/StructFieldName.md)
- [TimestampType](docs/v1/models/TimestampType.md)
- [TimestampTypeDict](docs/v1/models/TimestampTypeDict.md)
- [TotalCount](docs/v1/models/TotalCount.md)
- [UnsupportedType](docs/v1/models/UnsupportedType.md)
- [UnsupportedTypeDict](docs/v1/models/UnsupportedTypeDict.md)
- [Branch](docs/v1/models/Branch.md)
- [BranchDict](docs/v1/models/BranchDict.md)
- [BranchId](docs/v1/models/BranchId.md)
- [Dataset](docs/v1/models/Dataset.md)
- [DatasetDict](docs/v1/models/DatasetDict.md)
- [DatasetName](docs/v1/models/DatasetName.md)
- [DatasetRid](docs/v1/models/DatasetRid.md)
- [File](docs/v1/models/File.md)
- [FileDict](docs/v1/models/FileDict.md)
- [ListBranchesResponse](docs/v1/models/ListBranchesResponse.md)
- [ListBranchesResponseDict](docs/v1/models/ListBranchesResponseDict.md)
- [ListFilesResponse](docs/v1/models/ListFilesResponse.md)
- [ListFilesResponseDict](docs/v1/models/ListFilesResponseDict.md)
- [TableExportFormat](docs/v1/models/TableExportFormat.md)
- [Transaction](docs/v1/models/Transaction.md)
- [TransactionDict](docs/v1/models/TransactionDict.md)
- [TransactionRid](docs/v1/models/TransactionRid.md)
- [TransactionStatus](docs/v1/models/TransactionStatus.md)
- [TransactionType](docs/v1/models/TransactionType.md)
- [ActionType](docs/v1/models/ActionType.md)
- [ActionTypeApiName](docs/v1/models/ActionTypeApiName.md)
- [ActionTypeDict](docs/v1/models/ActionTypeDict.md)
- [ActionTypeRid](docs/v1/models/ActionTypeRid.md)
- [AggregateObjectsResponse](docs/v1/models/AggregateObjectsResponse.md)
- [AggregateObjectsResponseDict](docs/v1/models/AggregateObjectsResponseDict.md)
- [AggregateObjectsResponseItem](docs/v1/models/AggregateObjectsResponseItem.md)
- [AggregateObjectsResponseItemDict](docs/v1/models/AggregateObjectsResponseItemDict.md)
- [AggregationDict](docs/v1/models/AggregationDict.md)
- [AggregationDurationGroupingDict](docs/v1/models/AggregationDurationGroupingDict.md)
- [AggregationExactGroupingDict](docs/v1/models/AggregationExactGroupingDict.md)
- [AggregationFixedWidthGroupingDict](docs/v1/models/AggregationFixedWidthGroupingDict.md)
- [AggregationGroupByDict](docs/v1/models/AggregationGroupByDict.md)
- [AggregationGroupKey](docs/v1/models/AggregationGroupKey.md)
- [AggregationGroupValue](docs/v1/models/AggregationGroupValue.md)
- [AggregationMetricName](docs/v1/models/AggregationMetricName.md)
- [AggregationMetricResult](docs/v1/models/AggregationMetricResult.md)
- [AggregationMetricResultDict](docs/v1/models/AggregationMetricResultDict.md)
- [AggregationRangeDict](docs/v1/models/AggregationRangeDict.md)
- [AggregationRangesGroupingDict](docs/v1/models/AggregationRangesGroupingDict.md)
- [AllTermsQueryDict](docs/v1/models/AllTermsQueryDict.md)
- [AndQueryDict](docs/v1/models/AndQueryDict.md)
- [AnyTermQueryDict](docs/v1/models/AnyTermQueryDict.md)
- [ApplyActionRequestDict](docs/v1/models/ApplyActionRequestDict.md)
- [ApplyActionResponse](docs/v1/models/ApplyActionResponse.md)
- [ApplyActionResponseDict](docs/v1/models/ApplyActionResponseDict.md)
- [ApproximateDistinctAggregationDict](docs/v1/models/ApproximateDistinctAggregationDict.md)
- [ArraySizeConstraint](docs/v1/models/ArraySizeConstraint.md)
- [ArraySizeConstraintDict](docs/v1/models/ArraySizeConstraintDict.md)
- [AvgAggregationDict](docs/v1/models/AvgAggregationDict.md)
- [BatchApplyActionResponse](docs/v1/models/BatchApplyActionResponse.md)
- [BatchApplyActionResponseDict](docs/v1/models/BatchApplyActionResponseDict.md)
- [ContainsQueryDict](docs/v1/models/ContainsQueryDict.md)
- [CountAggregationDict](docs/v1/models/CountAggregationDict.md)
- [CreateInterfaceObjectRule](docs/v1/models/CreateInterfaceObjectRule.md)
- [CreateInterfaceObjectRuleDict](docs/v1/models/CreateInterfaceObjectRuleDict.md)
- [CreateLinkRule](docs/v1/models/CreateLinkRule.md)
- [CreateLinkRuleDict](docs/v1/models/CreateLinkRuleDict.md)
- [CreateObjectRule](docs/v1/models/CreateObjectRule.md)
- [CreateObjectRuleDict](docs/v1/models/CreateObjectRuleDict.md)
- [DataValue](docs/v1/models/DataValue.md)
- [DeleteLinkRule](docs/v1/models/DeleteLinkRule.md)
- [DeleteLinkRuleDict](docs/v1/models/DeleteLinkRuleDict.md)
- [DeleteObjectRule](docs/v1/models/DeleteObjectRule.md)
- [DeleteObjectRuleDict](docs/v1/models/DeleteObjectRuleDict.md)
- [EqualsQueryDict](docs/v1/models/EqualsQueryDict.md)
- [ExecuteQueryResponse](docs/v1/models/ExecuteQueryResponse.md)
- [ExecuteQueryResponseDict](docs/v1/models/ExecuteQueryResponseDict.md)
- [FieldNameV1](docs/v1/models/FieldNameV1.md)
- [FunctionRid](docs/v1/models/FunctionRid.md)
- [FunctionVersion](docs/v1/models/FunctionVersion.md)
- [Fuzzy](docs/v1/models/Fuzzy.md)
- [GroupMemberConstraint](docs/v1/models/GroupMemberConstraint.md)
- [GroupMemberConstraintDict](docs/v1/models/GroupMemberConstraintDict.md)
- [GteQueryDict](docs/v1/models/GteQueryDict.md)
- [GtQueryDict](docs/v1/models/GtQueryDict.md)
- [IsNullQueryDict](docs/v1/models/IsNullQueryDict.md)
- [LinkTypeApiName](docs/v1/models/LinkTypeApiName.md)
- [LinkTypeSide](docs/v1/models/LinkTypeSide.md)
- [LinkTypeSideCardinality](docs/v1/models/LinkTypeSideCardinality.md)
- [LinkTypeSideDict](docs/v1/models/LinkTypeSideDict.md)
- [ListActionTypesResponse](docs/v1/models/ListActionTypesResponse.md)
- [ListActionTypesResponseDict](docs/v1/models/ListActionTypesResponseDict.md)
- [ListLinkedObjectsResponse](docs/v1/models/ListLinkedObjectsResponse.md)
- [ListLinkedObjectsResponseDict](docs/v1/models/ListLinkedObjectsResponseDict.md)
- [ListObjectsResponse](docs/v1/models/ListObjectsResponse.md)
- [ListObjectsResponseDict](docs/v1/models/ListObjectsResponseDict.md)
- [ListObjectTypesResponse](docs/v1/models/ListObjectTypesResponse.md)
- [ListObjectTypesResponseDict](docs/v1/models/ListObjectTypesResponseDict.md)
- [ListOntologiesResponse](docs/v1/models/ListOntologiesResponse.md)
- [ListOntologiesResponseDict](docs/v1/models/ListOntologiesResponseDict.md)
- [ListOutgoingLinkTypesResponse](docs/v1/models/ListOutgoingLinkTypesResponse.md)
- [ListOutgoingLinkTypesResponseDict](docs/v1/models/ListOutgoingLinkTypesResponseDict.md)
- [ListQueryTypesResponse](docs/v1/models/ListQueryTypesResponse.md)
- [ListQueryTypesResponseDict](docs/v1/models/ListQueryTypesResponseDict.md)
- [LogicRule](docs/v1/models/LogicRule.md)
- [LogicRuleDict](docs/v1/models/LogicRuleDict.md)
- [LteQueryDict](docs/v1/models/LteQueryDict.md)
- [LtQueryDict](docs/v1/models/LtQueryDict.md)
- [MaxAggregationDict](docs/v1/models/MaxAggregationDict.md)
- [MinAggregationDict](docs/v1/models/MinAggregationDict.md)
- [ModifyInterfaceObjectRule](docs/v1/models/ModifyInterfaceObjectRule.md)
- [ModifyInterfaceObjectRuleDict](docs/v1/models/ModifyInterfaceObjectRuleDict.md)
- [ModifyObjectRule](docs/v1/models/ModifyObjectRule.md)
- [ModifyObjectRuleDict](docs/v1/models/ModifyObjectRuleDict.md)
- [NotQueryDict](docs/v1/models/NotQueryDict.md)
- [ObjectPropertyValueConstraint](docs/v1/models/ObjectPropertyValueConstraint.md)
- [ObjectPropertyValueConstraintDict](docs/v1/models/ObjectPropertyValueConstraintDict.md)
- [ObjectQueryResultConstraint](docs/v1/models/ObjectQueryResultConstraint.md)
- [ObjectQueryResultConstraintDict](docs/v1/models/ObjectQueryResultConstraintDict.md)
- [ObjectRid](docs/v1/models/ObjectRid.md)
- [ObjectType](docs/v1/models/ObjectType.md)
- [ObjectTypeApiName](docs/v1/models/ObjectTypeApiName.md)
- [ObjectTypeDict](docs/v1/models/ObjectTypeDict.md)
- [ObjectTypeRid](docs/v1/models/ObjectTypeRid.md)
- [ObjectTypeVisibility](docs/v1/models/ObjectTypeVisibility.md)
- [OneOfConstraint](docs/v1/models/OneOfConstraint.md)
- [OneOfConstraintDict](docs/v1/models/OneOfConstraintDict.md)
- [Ontology](docs/v1/models/Ontology.md)
- [OntologyApiName](docs/v1/models/OntologyApiName.md)
- [OntologyArrayType](docs/v1/models/OntologyArrayType.md)
- [OntologyArrayTypeDict](docs/v1/models/OntologyArrayTypeDict.md)
- [OntologyDataType](docs/v1/models/OntologyDataType.md)
- [OntologyDataTypeDict](docs/v1/models/OntologyDataTypeDict.md)
- [OntologyDict](docs/v1/models/OntologyDict.md)
- [OntologyMapType](docs/v1/models/OntologyMapType.md)
- [OntologyMapTypeDict](docs/v1/models/OntologyMapTypeDict.md)
- [OntologyObject](docs/v1/models/OntologyObject.md)
- [OntologyObjectDict](docs/v1/models/OntologyObjectDict.md)
- [OntologyObjectSetType](docs/v1/models/OntologyObjectSetType.md)
- [OntologyObjectSetTypeDict](docs/v1/models/OntologyObjectSetTypeDict.md)
- [OntologyObjectType](docs/v1/models/OntologyObjectType.md)
- [OntologyObjectTypeDict](docs/v1/models/OntologyObjectTypeDict.md)
- [OntologyRid](docs/v1/models/OntologyRid.md)
- [OntologySetType](docs/v1/models/OntologySetType.md)
- [OntologySetTypeDict](docs/v1/models/OntologySetTypeDict.md)
- [OntologyStructField](docs/v1/models/OntologyStructField.md)
- [OntologyStructFieldDict](docs/v1/models/OntologyStructFieldDict.md)
- [OntologyStructType](docs/v1/models/OntologyStructType.md)
- [OntologyStructTypeDict](docs/v1/models/OntologyStructTypeDict.md)
- [OrderBy](docs/v1/models/OrderBy.md)
- [OrQueryDict](docs/v1/models/OrQueryDict.md)
- [Parameter](docs/v1/models/Parameter.md)
- [ParameterDict](docs/v1/models/ParameterDict.md)
- [ParameterEvaluatedConstraint](docs/v1/models/ParameterEvaluatedConstraint.md)
- [ParameterEvaluatedConstraintDict](docs/v1/models/ParameterEvaluatedConstraintDict.md)
- [ParameterEvaluationResult](docs/v1/models/ParameterEvaluationResult.md)
- [ParameterEvaluationResultDict](docs/v1/models/ParameterEvaluationResultDict.md)
- [ParameterId](docs/v1/models/ParameterId.md)
- [ParameterOption](docs/v1/models/ParameterOption.md)
- [ParameterOptionDict](docs/v1/models/ParameterOptionDict.md)
- [PhraseQueryDict](docs/v1/models/PhraseQueryDict.md)
- [PrefixQueryDict](docs/v1/models/PrefixQueryDict.md)
- [Property](docs/v1/models/Property.md)
- [PropertyApiName](docs/v1/models/PropertyApiName.md)
- [PropertyDict](docs/v1/models/PropertyDict.md)
- [PropertyValue](docs/v1/models/PropertyValue.md)
- [PropertyValueEscapedString](docs/v1/models/PropertyValueEscapedString.md)
- [QueryApiName](docs/v1/models/QueryApiName.md)
- [QueryType](docs/v1/models/QueryType.md)
- [QueryTypeDict](docs/v1/models/QueryTypeDict.md)
- [RangeConstraint](docs/v1/models/RangeConstraint.md)
- [RangeConstraintDict](docs/v1/models/RangeConstraintDict.md)
- [SearchJsonQueryDict](docs/v1/models/SearchJsonQueryDict.md)
- [SearchObjectsResponse](docs/v1/models/SearchObjectsResponse.md)
- [SearchObjectsResponseDict](docs/v1/models/SearchObjectsResponseDict.md)
- [SearchOrderByDict](docs/v1/models/SearchOrderByDict.md)
- [SearchOrderingDict](docs/v1/models/SearchOrderingDict.md)
- [SelectedPropertyApiName](docs/v1/models/SelectedPropertyApiName.md)
- [StringLengthConstraint](docs/v1/models/StringLengthConstraint.md)
- [StringLengthConstraintDict](docs/v1/models/StringLengthConstraintDict.md)
- [StringRegexMatchConstraint](docs/v1/models/StringRegexMatchConstraint.md)
- [StringRegexMatchConstraintDict](docs/v1/models/StringRegexMatchConstraintDict.md)
- [SubmissionCriteriaEvaluation](docs/v1/models/SubmissionCriteriaEvaluation.md)
- [SubmissionCriteriaEvaluationDict](docs/v1/models/SubmissionCriteriaEvaluationDict.md)
- [SumAggregationDict](docs/v1/models/SumAggregationDict.md)
- [UnevaluableConstraint](docs/v1/models/UnevaluableConstraint.md)
- [UnevaluableConstraintDict](docs/v1/models/UnevaluableConstraintDict.md)
- [ValidateActionResponse](docs/v1/models/ValidateActionResponse.md)
- [ValidateActionResponseDict](docs/v1/models/ValidateActionResponseDict.md)
- [ValidationResult](docs/v1/models/ValidationResult.md)
- [ValueType](docs/v1/models/ValueType.md)


## Contributions

This repository does not accept code contributions.

If you have any questions, concerns, or ideas for improvements, create an
issue with Palantir Support.

## License
This project is made available under the [Apache 2.0 License](/LICENSE).
