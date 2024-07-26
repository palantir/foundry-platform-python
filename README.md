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
foundry_client = foundry.FoundryClient(
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
> in the [endpoint documentation](#api-documentation).

After creating the `ConfidentialClientAuth` object, pass it in to the `FoundryClient`,

```python
foundry_client = foundry.FoundryClient(auth=auth, hostname="example.palantirfoundry.com")
```

## Quickstart

Follow the [installation procedure](#installation) and determine which [authentication method](#authorization) is
best suited for your instance before following this example. For simplicity, the `UserTokenAuth` class will be used for demonstration
purposes.

```python
from foundry import FoundryClient
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryClient(
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
method definitions (see [Documentation for Models](#models) below for a full list of models). All request parameters with nested
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

<a id="api-documentation"></a>
## Documentation for API endpoints

Namespace | Resource | Operation | HTTP request |
------------ | ------------- | ------------- | ------------- |
**Admin** | Group | [**create**](docs/namespaces/Admin/Group.md#create) | **POST** /v2/admin/groups |
**Admin** | Group | [**delete**](docs/namespaces/Admin/Group.md#delete) | **DELETE** /v2/admin/groups/{groupId} |
**Admin** | Group | [**get**](docs/namespaces/Admin/Group.md#get) | **GET** /v2/admin/groups/{groupId} |
**Admin** | Group | [**list**](docs/namespaces/Admin/Group.md#list) | **GET** /v2/admin/groups |
**Admin** | Group | [**page**](docs/namespaces/Admin/Group.md#page) | **GET** /v2/admin/groups |
**Admin** | Group | [**search**](docs/namespaces/Admin/Group.md#search) | **POST** /v2/admin/groups/search |
**Admin** | GroupMember | [**add**](docs/namespaces/Admin/GroupMember.md#add) | **POST** /v2/admin/groups/{groupId}/groupMembers/add |
**Admin** | GroupMember | [**list**](docs/namespaces/Admin/GroupMember.md#list) | **GET** /v2/admin/groups/{groupId}/groupMembers |
**Admin** | GroupMember | [**page**](docs/namespaces/Admin/GroupMember.md#page) | **GET** /v2/admin/groups/{groupId}/groupMembers |
**Admin** | GroupMember | [**remove**](docs/namespaces/Admin/GroupMember.md#remove) | **POST** /v2/admin/groups/{groupId}/groupMembers/remove |
**Admin** | GroupMembership | [**list**](docs/namespaces/Admin/GroupMembership.md#list) | **GET** /v2/admin/users/{userId}/groupMemberships |
**Admin** | GroupMembership | [**page**](docs/namespaces/Admin/GroupMembership.md#page) | **GET** /v2/admin/users/{userId}/groupMemberships |
**Admin** | User | [**delete**](docs/namespaces/Admin/User.md#delete) | **DELETE** /v2/admin/users/{userId} |
**Admin** | User | [**get**](docs/namespaces/Admin/User.md#get) | **GET** /v2/admin/users/{userId} |
**Admin** | User | [**get_current**](docs/namespaces/Admin/User.md#get_current) | **GET** /v2/admin/users/getCurrent |
**Admin** | User | [**list**](docs/namespaces/Admin/User.md#list) | **GET** /v2/admin/users |
**Admin** | User | [**page**](docs/namespaces/Admin/User.md#page) | **GET** /v2/admin/users |
**Admin** | User | [**profile_picture**](docs/namespaces/Admin/User.md#profile_picture) | **GET** /v2/admin/users/{userId}/profilePicture |
**Admin** | User | [**search**](docs/namespaces/Admin/User.md#search) | **POST** /v2/admin/users/search |
**Datasets** | Branch | [**create**](docs/namespaces/Datasets/Branch.md#create) | **POST** /v1/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**delete**](docs/namespaces/Datasets/Branch.md#delete) | **DELETE** /v1/datasets/{datasetRid}/branches/{branchId} |
**Datasets** | Branch | [**get**](docs/namespaces/Datasets/Branch.md#get) | **GET** /v1/datasets/{datasetRid}/branches/{branchId} |
**Datasets** | Branch | [**list**](docs/namespaces/Datasets/Branch.md#list) | **GET** /v1/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**page**](docs/namespaces/Datasets/Branch.md#page) | **GET** /v1/datasets/{datasetRid}/branches |
**Datasets** | Dataset | [**create**](docs/namespaces/Datasets/Dataset.md#create) | **POST** /v1/datasets |
**Datasets** | Dataset | [**delete_schema**](docs/namespaces/Datasets/Dataset.md#delete_schema) | **DELETE** /v1/datasets/{datasetRid}/schema |
**Datasets** | Dataset | [**get**](docs/namespaces/Datasets/Dataset.md#get) | **GET** /v1/datasets/{datasetRid} |
**Datasets** | Dataset | [**get_schema**](docs/namespaces/Datasets/Dataset.md#get_schema) | **GET** /v1/datasets/{datasetRid}/schema |
**Datasets** | Dataset | [**read**](docs/namespaces/Datasets/Dataset.md#read) | **GET** /v1/datasets/{datasetRid}/readTable |
**Datasets** | Dataset | [**replace_schema**](docs/namespaces/Datasets/Dataset.md#replace_schema) | **PUT** /v1/datasets/{datasetRid}/schema |
**Datasets** | File | [**delete**](docs/namespaces/Datasets/File.md#delete) | **DELETE** /v1/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**get**](docs/namespaces/Datasets/File.md#get) | **GET** /v1/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**list**](docs/namespaces/Datasets/File.md#list) | **GET** /v1/datasets/{datasetRid}/files |
**Datasets** | File | [**page**](docs/namespaces/Datasets/File.md#page) | **GET** /v1/datasets/{datasetRid}/files |
**Datasets** | File | [**read**](docs/namespaces/Datasets/File.md#read) | **GET** /v1/datasets/{datasetRid}/files/{filePath}/content |
**Datasets** | File | [**upload**](docs/namespaces/Datasets/File.md#upload) | **POST** /v1/datasets/{datasetRid}/files:upload |
**Datasets** | Transaction | [**abort**](docs/namespaces/Datasets/Transaction.md#abort) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/abort |
**Datasets** | Transaction | [**commit**](docs/namespaces/Datasets/Transaction.md#commit) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/commit |
**Datasets** | Transaction | [**create**](docs/namespaces/Datasets/Transaction.md#create) | **POST** /v1/datasets/{datasetRid}/transactions |
**Datasets** | Transaction | [**get**](docs/namespaces/Datasets/Transaction.md#get) | **GET** /v1/datasets/{datasetRid}/transactions/{transactionRid} |
**Ontologies** | ActionType | [**get**](docs/namespaces/Ontologies/ActionType.md#get) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} |
**Ontologies** | ActionType | [**list**](docs/namespaces/Ontologies/ActionType.md#list) | **GET** /v2/ontologies/{ontology}/actionTypes |
**Ontologies** | ActionType | [**page**](docs/namespaces/Ontologies/ActionType.md#page) | **GET** /v2/ontologies/{ontology}/actionTypes |
**Ontologies** | ObjectType | [**get**](docs/namespaces/Ontologies/ObjectType.md#get) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType} |
**Ontologies** | ObjectType | [**get_outgoing_link_type**](docs/namespaces/Ontologies/ObjectType.md#get_outgoing_link_type) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
**Ontologies** | ObjectType | [**list**](docs/namespaces/Ontologies/ObjectType.md#list) | **GET** /v2/ontologies/{ontology}/objectTypes |
**Ontologies** | ObjectType | [**list_outgoing_link_types**](docs/namespaces/Ontologies/ObjectType.md#list_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | ObjectType | [**page**](docs/namespaces/Ontologies/ObjectType.md#page) | **GET** /v2/ontologies/{ontology}/objectTypes |
**Ontologies** | ObjectType | [**page_outgoing_link_types**](docs/namespaces/Ontologies/ObjectType.md#page_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | Ontology | [**get**](docs/namespaces/Ontologies/Ontology.md#get) | **GET** /v2/ontologies/{ontology} |
**Ontologies** | Ontology | [**get_full_metadata**](docs/namespaces/Ontologies/Ontology.md#get_full_metadata) | **GET** /v2/ontologies/{ontology}/fullMetadata |
**Ontologies** | Ontology | [**list**](docs/namespaces/Ontologies/Ontology.md#list) | **GET** /v2/ontologies |
**Ontologies** | QueryType | [**get**](docs/namespaces/Ontologies/QueryType.md#get) | **GET** /v2/ontologies/{ontology}/queryTypes/{queryApiName} |
**Ontologies** | QueryType | [**list**](docs/namespaces/Ontologies/QueryType.md#list) | **GET** /v2/ontologies/{ontology}/queryTypes |
**Ontologies** | QueryType | [**page**](docs/namespaces/Ontologies/QueryType.md#page) | **GET** /v2/ontologies/{ontology}/queryTypes |


<a id="models"></a>
## Documentation for models

- [AbsoluteTimeRange](docs/models/AbsoluteTimeRange.md)
- [AbsoluteTimeRangeDict](docs/models/AbsoluteTimeRangeDict.md)
- [ActionMode](docs/models/ActionMode.md)
- [ActionParameterArrayType](docs/models/ActionParameterArrayType.md)
- [ActionParameterArrayTypeDict](docs/models/ActionParameterArrayTypeDict.md)
- [ActionParameterType](docs/models/ActionParameterType.md)
- [ActionParameterTypeDict](docs/models/ActionParameterTypeDict.md)
- [ActionParameterV2](docs/models/ActionParameterV2.md)
- [ActionParameterV2Dict](docs/models/ActionParameterV2Dict.md)
- [ActionResults](docs/models/ActionResults.md)
- [ActionResultsDict](docs/models/ActionResultsDict.md)
- [ActionRid](docs/models/ActionRid.md)
- [ActionType](docs/models/ActionType.md)
- [ActionTypeApiName](docs/models/ActionTypeApiName.md)
- [ActionTypeDict](docs/models/ActionTypeDict.md)
- [ActionTypeRid](docs/models/ActionTypeRid.md)
- [ActionTypeV2](docs/models/ActionTypeV2.md)
- [ActionTypeV2Dict](docs/models/ActionTypeV2Dict.md)
- [AddGroupMembersRequest](docs/models/AddGroupMembersRequest.md)
- [AddGroupMembersRequestDict](docs/models/AddGroupMembersRequestDict.md)
- [AddLink](docs/models/AddLink.md)
- [AddLinkDict](docs/models/AddLinkDict.md)
- [AddObject](docs/models/AddObject.md)
- [AddObjectDict](docs/models/AddObjectDict.md)
- [AggregateObjectSetRequestV2](docs/models/AggregateObjectSetRequestV2.md)
- [AggregateObjectSetRequestV2Dict](docs/models/AggregateObjectSetRequestV2Dict.md)
- [AggregateObjectsRequest](docs/models/AggregateObjectsRequest.md)
- [AggregateObjectsRequestDict](docs/models/AggregateObjectsRequestDict.md)
- [AggregateObjectsRequestV2](docs/models/AggregateObjectsRequestV2.md)
- [AggregateObjectsRequestV2Dict](docs/models/AggregateObjectsRequestV2Dict.md)
- [AggregateObjectsResponse](docs/models/AggregateObjectsResponse.md)
- [AggregateObjectsResponseDict](docs/models/AggregateObjectsResponseDict.md)
- [AggregateObjectsResponseItem](docs/models/AggregateObjectsResponseItem.md)
- [AggregateObjectsResponseItemDict](docs/models/AggregateObjectsResponseItemDict.md)
- [AggregateObjectsResponseItemV2](docs/models/AggregateObjectsResponseItemV2.md)
- [AggregateObjectsResponseItemV2Dict](docs/models/AggregateObjectsResponseItemV2Dict.md)
- [AggregateObjectsResponseV2](docs/models/AggregateObjectsResponseV2.md)
- [AggregateObjectsResponseV2Dict](docs/models/AggregateObjectsResponseV2Dict.md)
- [Aggregation](docs/models/Aggregation.md)
- [AggregationAccuracy](docs/models/AggregationAccuracy.md)
- [AggregationAccuracyRequest](docs/models/AggregationAccuracyRequest.md)
- [AggregationDict](docs/models/AggregationDict.md)
- [AggregationDurationGrouping](docs/models/AggregationDurationGrouping.md)
- [AggregationDurationGroupingDict](docs/models/AggregationDurationGroupingDict.md)
- [AggregationDurationGroupingV2](docs/models/AggregationDurationGroupingV2.md)
- [AggregationDurationGroupingV2Dict](docs/models/AggregationDurationGroupingV2Dict.md)
- [AggregationExactGrouping](docs/models/AggregationExactGrouping.md)
- [AggregationExactGroupingDict](docs/models/AggregationExactGroupingDict.md)
- [AggregationExactGroupingV2](docs/models/AggregationExactGroupingV2.md)
- [AggregationExactGroupingV2Dict](docs/models/AggregationExactGroupingV2Dict.md)
- [AggregationFixedWidthGrouping](docs/models/AggregationFixedWidthGrouping.md)
- [AggregationFixedWidthGroupingDict](docs/models/AggregationFixedWidthGroupingDict.md)
- [AggregationFixedWidthGroupingV2](docs/models/AggregationFixedWidthGroupingV2.md)
- [AggregationFixedWidthGroupingV2Dict](docs/models/AggregationFixedWidthGroupingV2Dict.md)
- [AggregationGroupBy](docs/models/AggregationGroupBy.md)
- [AggregationGroupByDict](docs/models/AggregationGroupByDict.md)
- [AggregationGroupByV2](docs/models/AggregationGroupByV2.md)
- [AggregationGroupByV2Dict](docs/models/AggregationGroupByV2Dict.md)
- [AggregationGroupKey](docs/models/AggregationGroupKey.md)
- [AggregationGroupKeyV2](docs/models/AggregationGroupKeyV2.md)
- [AggregationGroupValue](docs/models/AggregationGroupValue.md)
- [AggregationGroupValueV2](docs/models/AggregationGroupValueV2.md)
- [AggregationMetricName](docs/models/AggregationMetricName.md)
- [AggregationMetricResult](docs/models/AggregationMetricResult.md)
- [AggregationMetricResultDict](docs/models/AggregationMetricResultDict.md)
- [AggregationMetricResultV2](docs/models/AggregationMetricResultV2.md)
- [AggregationMetricResultV2Dict](docs/models/AggregationMetricResultV2Dict.md)
- [AggregationObjectTypeGrouping](docs/models/AggregationObjectTypeGrouping.md)
- [AggregationObjectTypeGroupingDict](docs/models/AggregationObjectTypeGroupingDict.md)
- [AggregationOrderBy](docs/models/AggregationOrderBy.md)
- [AggregationOrderByDict](docs/models/AggregationOrderByDict.md)
- [AggregationRange](docs/models/AggregationRange.md)
- [AggregationRangeDict](docs/models/AggregationRangeDict.md)
- [AggregationRangesGrouping](docs/models/AggregationRangesGrouping.md)
- [AggregationRangesGroupingDict](docs/models/AggregationRangesGroupingDict.md)
- [AggregationRangesGroupingV2](docs/models/AggregationRangesGroupingV2.md)
- [AggregationRangesGroupingV2Dict](docs/models/AggregationRangesGroupingV2Dict.md)
- [AggregationRangeV2](docs/models/AggregationRangeV2.md)
- [AggregationRangeV2Dict](docs/models/AggregationRangeV2Dict.md)
- [AggregationV2](docs/models/AggregationV2.md)
- [AggregationV2Dict](docs/models/AggregationV2Dict.md)
- [AllTermsQuery](docs/models/AllTermsQuery.md)
- [AllTermsQueryDict](docs/models/AllTermsQueryDict.md)
- [AndQuery](docs/models/AndQuery.md)
- [AndQueryDict](docs/models/AndQueryDict.md)
- [AndQueryV2](docs/models/AndQueryV2.md)
- [AndQueryV2Dict](docs/models/AndQueryV2Dict.md)
- [AnyTermQuery](docs/models/AnyTermQuery.md)
- [AnyTermQueryDict](docs/models/AnyTermQueryDict.md)
- [AnyType](docs/models/AnyType.md)
- [AnyTypeDict](docs/models/AnyTypeDict.md)
- [ApplyActionMode](docs/models/ApplyActionMode.md)
- [ApplyActionRequest](docs/models/ApplyActionRequest.md)
- [ApplyActionRequestDict](docs/models/ApplyActionRequestDict.md)
- [ApplyActionRequestOptions](docs/models/ApplyActionRequestOptions.md)
- [ApplyActionRequestOptionsDict](docs/models/ApplyActionRequestOptionsDict.md)
- [ApplyActionRequestV2](docs/models/ApplyActionRequestV2.md)
- [ApplyActionRequestV2Dict](docs/models/ApplyActionRequestV2Dict.md)
- [ApplyActionResponse](docs/models/ApplyActionResponse.md)
- [ApplyActionResponseDict](docs/models/ApplyActionResponseDict.md)
- [ApproximateDistinctAggregation](docs/models/ApproximateDistinctAggregation.md)
- [ApproximateDistinctAggregationDict](docs/models/ApproximateDistinctAggregationDict.md)
- [ApproximateDistinctAggregationV2](docs/models/ApproximateDistinctAggregationV2.md)
- [ApproximateDistinctAggregationV2Dict](docs/models/ApproximateDistinctAggregationV2Dict.md)
- [ApproximatePercentileAggregationV2](docs/models/ApproximatePercentileAggregationV2.md)
- [ApproximatePercentileAggregationV2Dict](docs/models/ApproximatePercentileAggregationV2Dict.md)
- [ArchiveFileFormat](docs/models/ArchiveFileFormat.md)
- [Arg](docs/models/Arg.md)
- [ArgDict](docs/models/ArgDict.md)
- [ArraySizeConstraint](docs/models/ArraySizeConstraint.md)
- [ArraySizeConstraintDict](docs/models/ArraySizeConstraintDict.md)
- [ArtifactRepositoryRid](docs/models/ArtifactRepositoryRid.md)
- [AsyncActionStatus](docs/models/AsyncActionStatus.md)
- [AsyncApplyActionOperationResponseV2](docs/models/AsyncApplyActionOperationResponseV2.md)
- [AsyncApplyActionOperationResponseV2Dict](docs/models/AsyncApplyActionOperationResponseV2Dict.md)
- [AsyncApplyActionRequest](docs/models/AsyncApplyActionRequest.md)
- [AsyncApplyActionRequestDict](docs/models/AsyncApplyActionRequestDict.md)
- [AsyncApplyActionRequestV2](docs/models/AsyncApplyActionRequestV2.md)
- [AsyncApplyActionRequestV2Dict](docs/models/AsyncApplyActionRequestV2Dict.md)
- [AsyncApplyActionResponse](docs/models/AsyncApplyActionResponse.md)
- [AsyncApplyActionResponseDict](docs/models/AsyncApplyActionResponseDict.md)
- [AsyncApplyActionResponseV2](docs/models/AsyncApplyActionResponseV2.md)
- [AsyncApplyActionResponseV2Dict](docs/models/AsyncApplyActionResponseV2Dict.md)
- [Attachment](docs/models/Attachment.md)
- [AttachmentDict](docs/models/AttachmentDict.md)
- [AttachmentMetadataResponse](docs/models/AttachmentMetadataResponse.md)
- [AttachmentMetadataResponseDict](docs/models/AttachmentMetadataResponseDict.md)
- [AttachmentProperty](docs/models/AttachmentProperty.md)
- [AttachmentPropertyDict](docs/models/AttachmentPropertyDict.md)
- [AttachmentRid](docs/models/AttachmentRid.md)
- [AttachmentType](docs/models/AttachmentType.md)
- [AttachmentTypeDict](docs/models/AttachmentTypeDict.md)
- [AttachmentV2](docs/models/AttachmentV2.md)
- [AttachmentV2Dict](docs/models/AttachmentV2Dict.md)
- [AttributeName](docs/models/AttributeName.md)
- [AttributeValue](docs/models/AttributeValue.md)
- [AttributeValues](docs/models/AttributeValues.md)
- [AvgAggregation](docs/models/AvgAggregation.md)
- [AvgAggregationDict](docs/models/AvgAggregationDict.md)
- [AvgAggregationV2](docs/models/AvgAggregationV2.md)
- [AvgAggregationV2Dict](docs/models/AvgAggregationV2Dict.md)
- [BatchApplyActionRequest](docs/models/BatchApplyActionRequest.md)
- [BatchApplyActionRequestDict](docs/models/BatchApplyActionRequestDict.md)
- [BatchApplyActionRequestItem](docs/models/BatchApplyActionRequestItem.md)
- [BatchApplyActionRequestItemDict](docs/models/BatchApplyActionRequestItemDict.md)
- [BatchApplyActionRequestOptions](docs/models/BatchApplyActionRequestOptions.md)
- [BatchApplyActionRequestOptionsDict](docs/models/BatchApplyActionRequestOptionsDict.md)
- [BatchApplyActionRequestV2](docs/models/BatchApplyActionRequestV2.md)
- [BatchApplyActionRequestV2Dict](docs/models/BatchApplyActionRequestV2Dict.md)
- [BatchApplyActionResponse](docs/models/BatchApplyActionResponse.md)
- [BatchApplyActionResponseDict](docs/models/BatchApplyActionResponseDict.md)
- [BatchApplyActionResponseV2](docs/models/BatchApplyActionResponseV2.md)
- [BatchApplyActionResponseV2Dict](docs/models/BatchApplyActionResponseV2Dict.md)
- [BBox](docs/models/BBox.md)
- [BinaryType](docs/models/BinaryType.md)
- [BinaryTypeDict](docs/models/BinaryTypeDict.md)
- [BooleanType](docs/models/BooleanType.md)
- [BooleanTypeDict](docs/models/BooleanTypeDict.md)
- [BoundingBoxValue](docs/models/BoundingBoxValue.md)
- [BoundingBoxValueDict](docs/models/BoundingBoxValueDict.md)
- [Branch](docs/models/Branch.md)
- [BranchDict](docs/models/BranchDict.md)
- [BranchId](docs/models/BranchId.md)
- [ByteType](docs/models/ByteType.md)
- [ByteTypeDict](docs/models/ByteTypeDict.md)
- [CenterPoint](docs/models/CenterPoint.md)
- [CenterPointDict](docs/models/CenterPointDict.md)
- [CenterPointTypes](docs/models/CenterPointTypes.md)
- [CenterPointTypesDict](docs/models/CenterPointTypesDict.md)
- [ChatCompletionChoice](docs/models/ChatCompletionChoice.md)
- [ChatCompletionChoiceDict](docs/models/ChatCompletionChoiceDict.md)
- [ChatCompletionRequest](docs/models/ChatCompletionRequest.md)
- [ChatCompletionRequestDict](docs/models/ChatCompletionRequestDict.md)
- [ChatCompletionResponse](docs/models/ChatCompletionResponse.md)
- [ChatCompletionResponseDict](docs/models/ChatCompletionResponseDict.md)
- [ChatMessage](docs/models/ChatMessage.md)
- [ChatMessageDict](docs/models/ChatMessageDict.md)
- [ChatMessageRole](docs/models/ChatMessageRole.md)
- [ContainsAllTermsInOrderPrefixLastTerm](docs/models/ContainsAllTermsInOrderPrefixLastTerm.md)
- [ContainsAllTermsInOrderPrefixLastTermDict](docs/models/ContainsAllTermsInOrderPrefixLastTermDict.md)
- [ContainsAllTermsInOrderQuery](docs/models/ContainsAllTermsInOrderQuery.md)
- [ContainsAllTermsInOrderQueryDict](docs/models/ContainsAllTermsInOrderQueryDict.md)
- [ContainsAllTermsQuery](docs/models/ContainsAllTermsQuery.md)
- [ContainsAllTermsQueryDict](docs/models/ContainsAllTermsQueryDict.md)
- [ContainsAnyTermQuery](docs/models/ContainsAnyTermQuery.md)
- [ContainsAnyTermQueryDict](docs/models/ContainsAnyTermQueryDict.md)
- [ContainsQuery](docs/models/ContainsQuery.md)
- [ContainsQueryDict](docs/models/ContainsQueryDict.md)
- [ContainsQueryV2](docs/models/ContainsQueryV2.md)
- [ContainsQueryV2Dict](docs/models/ContainsQueryV2Dict.md)
- [ContentLength](docs/models/ContentLength.md)
- [ContentType](docs/models/ContentType.md)
- [Coordinate](docs/models/Coordinate.md)
- [CountAggregation](docs/models/CountAggregation.md)
- [CountAggregationDict](docs/models/CountAggregationDict.md)
- [CountAggregationV2](docs/models/CountAggregationV2.md)
- [CountAggregationV2Dict](docs/models/CountAggregationV2Dict.md)
- [CountObjectsResponseV2](docs/models/CountObjectsResponseV2.md)
- [CountObjectsResponseV2Dict](docs/models/CountObjectsResponseV2Dict.md)
- [CreateBranchRequest](docs/models/CreateBranchRequest.md)
- [CreateBranchRequestDict](docs/models/CreateBranchRequestDict.md)
- [CreateDatasetRequest](docs/models/CreateDatasetRequest.md)
- [CreateDatasetRequestDict](docs/models/CreateDatasetRequestDict.md)
- [CreatedBy](docs/models/CreatedBy.md)
- [CreatedTime](docs/models/CreatedTime.md)
- [CreateGroupRequest](docs/models/CreateGroupRequest.md)
- [CreateGroupRequestDict](docs/models/CreateGroupRequestDict.md)
- [CreateLinkRule](docs/models/CreateLinkRule.md)
- [CreateLinkRuleDict](docs/models/CreateLinkRuleDict.md)
- [CreateObjectRule](docs/models/CreateObjectRule.md)
- [CreateObjectRuleDict](docs/models/CreateObjectRuleDict.md)
- [CreateTemporaryObjectSetRequestV2](docs/models/CreateTemporaryObjectSetRequestV2.md)
- [CreateTemporaryObjectSetRequestV2Dict](docs/models/CreateTemporaryObjectSetRequestV2Dict.md)
- [CreateTemporaryObjectSetResponseV2](docs/models/CreateTemporaryObjectSetResponseV2.md)
- [CreateTemporaryObjectSetResponseV2Dict](docs/models/CreateTemporaryObjectSetResponseV2Dict.md)
- [CreateTransactionRequest](docs/models/CreateTransactionRequest.md)
- [CreateTransactionRequestDict](docs/models/CreateTransactionRequestDict.md)
- [CustomTypeId](docs/models/CustomTypeId.md)
- [Dataset](docs/models/Dataset.md)
- [DatasetDict](docs/models/DatasetDict.md)
- [DatasetName](docs/models/DatasetName.md)
- [DatasetRid](docs/models/DatasetRid.md)
- [DataValue](docs/models/DataValue.md)
- [DateType](docs/models/DateType.md)
- [DateTypeDict](docs/models/DateTypeDict.md)
- [DecimalType](docs/models/DecimalType.md)
- [DecimalTypeDict](docs/models/DecimalTypeDict.md)
- [DeleteLinkRule](docs/models/DeleteLinkRule.md)
- [DeleteLinkRuleDict](docs/models/DeleteLinkRuleDict.md)
- [DeleteObjectRule](docs/models/DeleteObjectRule.md)
- [DeleteObjectRuleDict](docs/models/DeleteObjectRuleDict.md)
- [DeployWebsiteRequest](docs/models/DeployWebsiteRequest.md)
- [DeployWebsiteRequestDict](docs/models/DeployWebsiteRequestDict.md)
- [DisplayName](docs/models/DisplayName.md)
- [Distance](docs/models/Distance.md)
- [DistanceDict](docs/models/DistanceDict.md)
- [DistanceUnit](docs/models/DistanceUnit.md)
- [DoesNotIntersectBoundingBoxQuery](docs/models/DoesNotIntersectBoundingBoxQuery.md)
- [DoesNotIntersectBoundingBoxQueryDict](docs/models/DoesNotIntersectBoundingBoxQueryDict.md)
- [DoesNotIntersectPolygonQuery](docs/models/DoesNotIntersectPolygonQuery.md)
- [DoesNotIntersectPolygonQueryDict](docs/models/DoesNotIntersectPolygonQueryDict.md)
- [DoubleType](docs/models/DoubleType.md)
- [DoubleTypeDict](docs/models/DoubleTypeDict.md)
- [Duration](docs/models/Duration.md)
- [EqualsQuery](docs/models/EqualsQuery.md)
- [EqualsQueryDict](docs/models/EqualsQueryDict.md)
- [EqualsQueryV2](docs/models/EqualsQueryV2.md)
- [EqualsQueryV2Dict](docs/models/EqualsQueryV2Dict.md)
- [Error](docs/models/Error.md)
- [ErrorDict](docs/models/ErrorDict.md)
- [ErrorName](docs/models/ErrorName.md)
- [ExecuteQueryRequest](docs/models/ExecuteQueryRequest.md)
- [ExecuteQueryRequestDict](docs/models/ExecuteQueryRequestDict.md)
- [ExecuteQueryResponse](docs/models/ExecuteQueryResponse.md)
- [ExecuteQueryResponseDict](docs/models/ExecuteQueryResponseDict.md)
- [Feature](docs/models/Feature.md)
- [FeatureCollection](docs/models/FeatureCollection.md)
- [FeatureCollectionDict](docs/models/FeatureCollectionDict.md)
- [FeatureCollectionTypes](docs/models/FeatureCollectionTypes.md)
- [FeatureCollectionTypesDict](docs/models/FeatureCollectionTypesDict.md)
- [FeatureDict](docs/models/FeatureDict.md)
- [FeaturePropertyKey](docs/models/FeaturePropertyKey.md)
- [FieldNameV1](docs/models/FieldNameV1.md)
- [File](docs/models/File.md)
- [FileDict](docs/models/FileDict.md)
- [Filename](docs/models/Filename.md)
- [FilePath](docs/models/FilePath.md)
- [FilesystemResource](docs/models/FilesystemResource.md)
- [FilesystemResourceDict](docs/models/FilesystemResourceDict.md)
- [FileUpdatedTime](docs/models/FileUpdatedTime.md)
- [FilterValue](docs/models/FilterValue.md)
- [FloatType](docs/models/FloatType.md)
- [FloatTypeDict](docs/models/FloatTypeDict.md)
- [FolderRid](docs/models/FolderRid.md)
- [FunctionRid](docs/models/FunctionRid.md)
- [FunctionVersion](docs/models/FunctionVersion.md)
- [Fuzzy](docs/models/Fuzzy.md)
- [FuzzyV2](docs/models/FuzzyV2.md)
- [GeoJsonObject](docs/models/GeoJsonObject.md)
- [GeoJsonObjectDict](docs/models/GeoJsonObjectDict.md)
- [Geometry](docs/models/Geometry.md)
- [GeometryCollection](docs/models/GeometryCollection.md)
- [GeometryCollectionDict](docs/models/GeometryCollectionDict.md)
- [GeometryDict](docs/models/GeometryDict.md)
- [GeoPoint](docs/models/GeoPoint.md)
- [GeoPointDict](docs/models/GeoPointDict.md)
- [GeoPointType](docs/models/GeoPointType.md)
- [GeoPointTypeDict](docs/models/GeoPointTypeDict.md)
- [GeoShapeType](docs/models/GeoShapeType.md)
- [GeoShapeTypeDict](docs/models/GeoShapeTypeDict.md)
- [GeotimeSeriesValue](docs/models/GeotimeSeriesValue.md)
- [GeotimeSeriesValueDict](docs/models/GeotimeSeriesValueDict.md)
- [Group](docs/models/Group.md)
- [GroupDict](docs/models/GroupDict.md)
- [GroupMember](docs/models/GroupMember.md)
- [GroupMemberConstraint](docs/models/GroupMemberConstraint.md)
- [GroupMemberConstraintDict](docs/models/GroupMemberConstraintDict.md)
- [GroupMemberDict](docs/models/GroupMemberDict.md)
- [GroupMembership](docs/models/GroupMembership.md)
- [GroupMembershipDict](docs/models/GroupMembershipDict.md)
- [GroupMembershipExpiration](docs/models/GroupMembershipExpiration.md)
- [GroupName](docs/models/GroupName.md)
- [GroupSearchFilter](docs/models/GroupSearchFilter.md)
- [GroupSearchFilterDict](docs/models/GroupSearchFilterDict.md)
- [GteQuery](docs/models/GteQuery.md)
- [GteQueryDict](docs/models/GteQueryDict.md)
- [GteQueryV2](docs/models/GteQueryV2.md)
- [GteQueryV2Dict](docs/models/GteQueryV2Dict.md)
- [GtQuery](docs/models/GtQuery.md)
- [GtQueryDict](docs/models/GtQueryDict.md)
- [GtQueryV2](docs/models/GtQueryV2.md)
- [GtQueryV2Dict](docs/models/GtQueryV2Dict.md)
- [IntegerType](docs/models/IntegerType.md)
- [IntegerTypeDict](docs/models/IntegerTypeDict.md)
- [InterfaceLinkType](docs/models/InterfaceLinkType.md)
- [InterfaceLinkTypeApiName](docs/models/InterfaceLinkTypeApiName.md)
- [InterfaceLinkTypeCardinality](docs/models/InterfaceLinkTypeCardinality.md)
- [InterfaceLinkTypeDict](docs/models/InterfaceLinkTypeDict.md)
- [InterfaceLinkTypeLinkedEntityApiName](docs/models/InterfaceLinkTypeLinkedEntityApiName.md)
- [InterfaceLinkTypeLinkedEntityApiNameDict](docs/models/InterfaceLinkTypeLinkedEntityApiNameDict.md)
- [InterfaceLinkTypeRid](docs/models/InterfaceLinkTypeRid.md)
- [InterfaceType](docs/models/InterfaceType.md)
- [InterfaceTypeApiName](docs/models/InterfaceTypeApiName.md)
- [InterfaceTypeDict](docs/models/InterfaceTypeDict.md)
- [InterfaceTypeRid](docs/models/InterfaceTypeRid.md)
- [IntersectsBoundingBoxQuery](docs/models/IntersectsBoundingBoxQuery.md)
- [IntersectsBoundingBoxQueryDict](docs/models/IntersectsBoundingBoxQueryDict.md)
- [IntersectsPolygonQuery](docs/models/IntersectsPolygonQuery.md)
- [IntersectsPolygonQueryDict](docs/models/IntersectsPolygonQueryDict.md)
- [IsNullQuery](docs/models/IsNullQuery.md)
- [IsNullQueryDict](docs/models/IsNullQueryDict.md)
- [IsNullQueryV2](docs/models/IsNullQueryV2.md)
- [IsNullQueryV2Dict](docs/models/IsNullQueryV2Dict.md)
- [LanguageModel](docs/models/LanguageModel.md)
- [LanguageModelApiName](docs/models/LanguageModelApiName.md)
- [LanguageModelDict](docs/models/LanguageModelDict.md)
- [LanguageModelSource](docs/models/LanguageModelSource.md)
- [LinearRing](docs/models/LinearRing.md)
- [LineString](docs/models/LineString.md)
- [LineStringCoordinates](docs/models/LineStringCoordinates.md)
- [LineStringDict](docs/models/LineStringDict.md)
- [LinkedInterfaceTypeApiName](docs/models/LinkedInterfaceTypeApiName.md)
- [LinkedInterfaceTypeApiNameDict](docs/models/LinkedInterfaceTypeApiNameDict.md)
- [LinkedObjectTypeApiName](docs/models/LinkedObjectTypeApiName.md)
- [LinkedObjectTypeApiNameDict](docs/models/LinkedObjectTypeApiNameDict.md)
- [LinkSideObject](docs/models/LinkSideObject.md)
- [LinkSideObjectDict](docs/models/LinkSideObjectDict.md)
- [LinkTypeApiName](docs/models/LinkTypeApiName.md)
- [LinkTypeRid](docs/models/LinkTypeRid.md)
- [LinkTypeSide](docs/models/LinkTypeSide.md)
- [LinkTypeSideCardinality](docs/models/LinkTypeSideCardinality.md)
- [LinkTypeSideDict](docs/models/LinkTypeSideDict.md)
- [LinkTypeSideV2](docs/models/LinkTypeSideV2.md)
- [LinkTypeSideV2Dict](docs/models/LinkTypeSideV2Dict.md)
- [ListActionTypesResponse](docs/models/ListActionTypesResponse.md)
- [ListActionTypesResponseDict](docs/models/ListActionTypesResponseDict.md)
- [ListActionTypesResponseV2](docs/models/ListActionTypesResponseV2.md)
- [ListActionTypesResponseV2Dict](docs/models/ListActionTypesResponseV2Dict.md)
- [ListAttachmentsResponseV2](docs/models/ListAttachmentsResponseV2.md)
- [ListAttachmentsResponseV2Dict](docs/models/ListAttachmentsResponseV2Dict.md)
- [ListBranchesResponse](docs/models/ListBranchesResponse.md)
- [ListBranchesResponseDict](docs/models/ListBranchesResponseDict.md)
- [ListFilesResponse](docs/models/ListFilesResponse.md)
- [ListFilesResponseDict](docs/models/ListFilesResponseDict.md)
- [ListGroupMembershipsResponse](docs/models/ListGroupMembershipsResponse.md)
- [ListGroupMembershipsResponseDict](docs/models/ListGroupMembershipsResponseDict.md)
- [ListGroupMembersResponse](docs/models/ListGroupMembersResponse.md)
- [ListGroupMembersResponseDict](docs/models/ListGroupMembersResponseDict.md)
- [ListGroupsResponse](docs/models/ListGroupsResponse.md)
- [ListGroupsResponseDict](docs/models/ListGroupsResponseDict.md)
- [ListInterfaceTypesResponse](docs/models/ListInterfaceTypesResponse.md)
- [ListInterfaceTypesResponseDict](docs/models/ListInterfaceTypesResponseDict.md)
- [ListLanguageModelsResponse](docs/models/ListLanguageModelsResponse.md)
- [ListLanguageModelsResponseDict](docs/models/ListLanguageModelsResponseDict.md)
- [ListLinkedObjectsResponse](docs/models/ListLinkedObjectsResponse.md)
- [ListLinkedObjectsResponseDict](docs/models/ListLinkedObjectsResponseDict.md)
- [ListLinkedObjectsResponseV2](docs/models/ListLinkedObjectsResponseV2.md)
- [ListLinkedObjectsResponseV2Dict](docs/models/ListLinkedObjectsResponseV2Dict.md)
- [ListObjectsResponse](docs/models/ListObjectsResponse.md)
- [ListObjectsResponseDict](docs/models/ListObjectsResponseDict.md)
- [ListObjectsResponseV2](docs/models/ListObjectsResponseV2.md)
- [ListObjectsResponseV2Dict](docs/models/ListObjectsResponseV2Dict.md)
- [ListObjectTypesResponse](docs/models/ListObjectTypesResponse.md)
- [ListObjectTypesResponseDict](docs/models/ListObjectTypesResponseDict.md)
- [ListObjectTypesV2Response](docs/models/ListObjectTypesV2Response.md)
- [ListObjectTypesV2ResponseDict](docs/models/ListObjectTypesV2ResponseDict.md)
- [ListOntologiesResponse](docs/models/ListOntologiesResponse.md)
- [ListOntologiesResponseDict](docs/models/ListOntologiesResponseDict.md)
- [ListOntologiesV2Response](docs/models/ListOntologiesV2Response.md)
- [ListOntologiesV2ResponseDict](docs/models/ListOntologiesV2ResponseDict.md)
- [ListOutgoingLinkTypesResponse](docs/models/ListOutgoingLinkTypesResponse.md)
- [ListOutgoingLinkTypesResponseDict](docs/models/ListOutgoingLinkTypesResponseDict.md)
- [ListOutgoingLinkTypesResponseV2](docs/models/ListOutgoingLinkTypesResponseV2.md)
- [ListOutgoingLinkTypesResponseV2Dict](docs/models/ListOutgoingLinkTypesResponseV2Dict.md)
- [ListQueryTypesResponse](docs/models/ListQueryTypesResponse.md)
- [ListQueryTypesResponseDict](docs/models/ListQueryTypesResponseDict.md)
- [ListQueryTypesResponseV2](docs/models/ListQueryTypesResponseV2.md)
- [ListQueryTypesResponseV2Dict](docs/models/ListQueryTypesResponseV2Dict.md)
- [ListUsersResponse](docs/models/ListUsersResponse.md)
- [ListUsersResponseDict](docs/models/ListUsersResponseDict.md)
- [ListVersionsResponse](docs/models/ListVersionsResponse.md)
- [ListVersionsResponseDict](docs/models/ListVersionsResponseDict.md)
- [LoadObjectSetRequestV2](docs/models/LoadObjectSetRequestV2.md)
- [LoadObjectSetRequestV2Dict](docs/models/LoadObjectSetRequestV2Dict.md)
- [LoadObjectSetResponseV2](docs/models/LoadObjectSetResponseV2.md)
- [LoadObjectSetResponseV2Dict](docs/models/LoadObjectSetResponseV2Dict.md)
- [LocalFilePath](docs/models/LocalFilePath.md)
- [LocalFilePathDict](docs/models/LocalFilePathDict.md)
- [LogicRule](docs/models/LogicRule.md)
- [LogicRuleDict](docs/models/LogicRuleDict.md)
- [LongType](docs/models/LongType.md)
- [LongTypeDict](docs/models/LongTypeDict.md)
- [LteQuery](docs/models/LteQuery.md)
- [LteQueryDict](docs/models/LteQueryDict.md)
- [LteQueryV2](docs/models/LteQueryV2.md)
- [LteQueryV2Dict](docs/models/LteQueryV2Dict.md)
- [LtQuery](docs/models/LtQuery.md)
- [LtQueryDict](docs/models/LtQueryDict.md)
- [LtQueryV2](docs/models/LtQueryV2.md)
- [LtQueryV2Dict](docs/models/LtQueryV2Dict.md)
- [MarkingType](docs/models/MarkingType.md)
- [MarkingTypeDict](docs/models/MarkingTypeDict.md)
- [MaxAggregation](docs/models/MaxAggregation.md)
- [MaxAggregationDict](docs/models/MaxAggregationDict.md)
- [MaxAggregationV2](docs/models/MaxAggregationV2.md)
- [MaxAggregationV2Dict](docs/models/MaxAggregationV2Dict.md)
- [MediaType](docs/models/MediaType.md)
- [MinAggregation](docs/models/MinAggregation.md)
- [MinAggregationDict](docs/models/MinAggregationDict.md)
- [MinAggregationV2](docs/models/MinAggregationV2.md)
- [MinAggregationV2Dict](docs/models/MinAggregationV2Dict.md)
- [ModifyObject](docs/models/ModifyObject.md)
- [ModifyObjectDict](docs/models/ModifyObjectDict.md)
- [ModifyObjectRule](docs/models/ModifyObjectRule.md)
- [ModifyObjectRuleDict](docs/models/ModifyObjectRuleDict.md)
- [MultiLineString](docs/models/MultiLineString.md)
- [MultiLineStringDict](docs/models/MultiLineStringDict.md)
- [MultiPoint](docs/models/MultiPoint.md)
- [MultiPointDict](docs/models/MultiPointDict.md)
- [MultiPolygon](docs/models/MultiPolygon.md)
- [MultiPolygonDict](docs/models/MultiPolygonDict.md)
- [NestedQueryAggregation](docs/models/NestedQueryAggregation.md)
- [NestedQueryAggregationDict](docs/models/NestedQueryAggregationDict.md)
- [NotQuery](docs/models/NotQuery.md)
- [NotQueryDict](docs/models/NotQueryDict.md)
- [NotQueryV2](docs/models/NotQueryV2.md)
- [NotQueryV2Dict](docs/models/NotQueryV2Dict.md)
- [NullType](docs/models/NullType.md)
- [NullTypeDict](docs/models/NullTypeDict.md)
- [ObjectEdit](docs/models/ObjectEdit.md)
- [ObjectEditDict](docs/models/ObjectEditDict.md)
- [ObjectEdits](docs/models/ObjectEdits.md)
- [ObjectEditsDict](docs/models/ObjectEditsDict.md)
- [ObjectPrimaryKey](docs/models/ObjectPrimaryKey.md)
- [ObjectPropertyType](docs/models/ObjectPropertyType.md)
- [ObjectPropertyTypeDict](docs/models/ObjectPropertyTypeDict.md)
- [ObjectPropertyValueConstraint](docs/models/ObjectPropertyValueConstraint.md)
- [ObjectPropertyValueConstraintDict](docs/models/ObjectPropertyValueConstraintDict.md)
- [ObjectQueryResultConstraint](docs/models/ObjectQueryResultConstraint.md)
- [ObjectQueryResultConstraintDict](docs/models/ObjectQueryResultConstraintDict.md)
- [ObjectRid](docs/models/ObjectRid.md)
- [ObjectSet](docs/models/ObjectSet.md)
- [ObjectSetBaseType](docs/models/ObjectSetBaseType.md)
- [ObjectSetBaseTypeDict](docs/models/ObjectSetBaseTypeDict.md)
- [ObjectSetDict](docs/models/ObjectSetDict.md)
- [ObjectSetFilterType](docs/models/ObjectSetFilterType.md)
- [ObjectSetFilterTypeDict](docs/models/ObjectSetFilterTypeDict.md)
- [ObjectSetIntersectionType](docs/models/ObjectSetIntersectionType.md)
- [ObjectSetIntersectionTypeDict](docs/models/ObjectSetIntersectionTypeDict.md)
- [ObjectSetReferenceType](docs/models/ObjectSetReferenceType.md)
- [ObjectSetReferenceTypeDict](docs/models/ObjectSetReferenceTypeDict.md)
- [ObjectSetRid](docs/models/ObjectSetRid.md)
- [ObjectSetSearchAroundType](docs/models/ObjectSetSearchAroundType.md)
- [ObjectSetSearchAroundTypeDict](docs/models/ObjectSetSearchAroundTypeDict.md)
- [ObjectSetStaticType](docs/models/ObjectSetStaticType.md)
- [ObjectSetStaticTypeDict](docs/models/ObjectSetStaticTypeDict.md)
- [ObjectSetStreamSubscribeRequest](docs/models/ObjectSetStreamSubscribeRequest.md)
- [ObjectSetStreamSubscribeRequestDict](docs/models/ObjectSetStreamSubscribeRequestDict.md)
- [ObjectSetStreamSubscribeRequests](docs/models/ObjectSetStreamSubscribeRequests.md)
- [ObjectSetStreamSubscribeRequestsDict](docs/models/ObjectSetStreamSubscribeRequestsDict.md)
- [ObjectSetSubscribeResponse](docs/models/ObjectSetSubscribeResponse.md)
- [ObjectSetSubscribeResponseDict](docs/models/ObjectSetSubscribeResponseDict.md)
- [ObjectSetSubscribeResponses](docs/models/ObjectSetSubscribeResponses.md)
- [ObjectSetSubscribeResponsesDict](docs/models/ObjectSetSubscribeResponsesDict.md)
- [ObjectSetSubtractType](docs/models/ObjectSetSubtractType.md)
- [ObjectSetSubtractTypeDict](docs/models/ObjectSetSubtractTypeDict.md)
- [ObjectSetUnionType](docs/models/ObjectSetUnionType.md)
- [ObjectSetUnionTypeDict](docs/models/ObjectSetUnionTypeDict.md)
- [ObjectSetUpdate](docs/models/ObjectSetUpdate.md)
- [ObjectSetUpdateDict](docs/models/ObjectSetUpdateDict.md)
- [ObjectSetUpdates](docs/models/ObjectSetUpdates.md)
- [ObjectSetUpdatesDict](docs/models/ObjectSetUpdatesDict.md)
- [ObjectState](docs/models/ObjectState.md)
- [ObjectType](docs/models/ObjectType.md)
- [ObjectTypeApiName](docs/models/ObjectTypeApiName.md)
- [ObjectTypeDict](docs/models/ObjectTypeDict.md)
- [ObjectTypeEdits](docs/models/ObjectTypeEdits.md)
- [ObjectTypeEditsDict](docs/models/ObjectTypeEditsDict.md)
- [ObjectTypeFullMetadata](docs/models/ObjectTypeFullMetadata.md)
- [ObjectTypeFullMetadataDict](docs/models/ObjectTypeFullMetadataDict.md)
- [ObjectTypeInterfaceImplementation](docs/models/ObjectTypeInterfaceImplementation.md)
- [ObjectTypeInterfaceImplementationDict](docs/models/ObjectTypeInterfaceImplementationDict.md)
- [ObjectTypeRid](docs/models/ObjectTypeRid.md)
- [ObjectTypeV2](docs/models/ObjectTypeV2.md)
- [ObjectTypeV2Dict](docs/models/ObjectTypeV2Dict.md)
- [ObjectTypeVisibility](docs/models/ObjectTypeVisibility.md)
- [ObjectUpdate](docs/models/ObjectUpdate.md)
- [ObjectUpdateDict](docs/models/ObjectUpdateDict.md)
- [OneOfConstraint](docs/models/OneOfConstraint.md)
- [OneOfConstraintDict](docs/models/OneOfConstraintDict.md)
- [Ontology](docs/models/Ontology.md)
- [OntologyApiName](docs/models/OntologyApiName.md)
- [OntologyArrayType](docs/models/OntologyArrayType.md)
- [OntologyArrayTypeDict](docs/models/OntologyArrayTypeDict.md)
- [OntologyDataType](docs/models/OntologyDataType.md)
- [OntologyDataTypeDict](docs/models/OntologyDataTypeDict.md)
- [OntologyDict](docs/models/OntologyDict.md)
- [OntologyFullMetadata](docs/models/OntologyFullMetadata.md)
- [OntologyFullMetadataDict](docs/models/OntologyFullMetadataDict.md)
- [OntologyIdentifier](docs/models/OntologyIdentifier.md)
- [OntologyMapType](docs/models/OntologyMapType.md)
- [OntologyMapTypeDict](docs/models/OntologyMapTypeDict.md)
- [OntologyObject](docs/models/OntologyObject.md)
- [OntologyObjectArrayType](docs/models/OntologyObjectArrayType.md)
- [OntologyObjectArrayTypeDict](docs/models/OntologyObjectArrayTypeDict.md)
- [OntologyObjectDict](docs/models/OntologyObjectDict.md)
- [OntologyObjectSetType](docs/models/OntologyObjectSetType.md)
- [OntologyObjectSetTypeDict](docs/models/OntologyObjectSetTypeDict.md)
- [OntologyObjectType](docs/models/OntologyObjectType.md)
- [OntologyObjectTypeDict](docs/models/OntologyObjectTypeDict.md)
- [OntologyObjectV2](docs/models/OntologyObjectV2.md)
- [OntologyRid](docs/models/OntologyRid.md)
- [OntologySetType](docs/models/OntologySetType.md)
- [OntologySetTypeDict](docs/models/OntologySetTypeDict.md)
- [OntologyStructField](docs/models/OntologyStructField.md)
- [OntologyStructFieldDict](docs/models/OntologyStructFieldDict.md)
- [OntologyStructType](docs/models/OntologyStructType.md)
- [OntologyStructTypeDict](docs/models/OntologyStructTypeDict.md)
- [OntologyV2](docs/models/OntologyV2.md)
- [OntologyV2Dict](docs/models/OntologyV2Dict.md)
- [OrderBy](docs/models/OrderBy.md)
- [OrderByDirection](docs/models/OrderByDirection.md)
- [OrganizationRid](docs/models/OrganizationRid.md)
- [OrQuery](docs/models/OrQuery.md)
- [OrQueryDict](docs/models/OrQueryDict.md)
- [OrQueryV2](docs/models/OrQueryV2.md)
- [OrQueryV2Dict](docs/models/OrQueryV2Dict.md)
- [PageSize](docs/models/PageSize.md)
- [PageToken](docs/models/PageToken.md)
- [Parameter](docs/models/Parameter.md)
- [ParameterDict](docs/models/ParameterDict.md)
- [ParameterEvaluatedConstraint](docs/models/ParameterEvaluatedConstraint.md)
- [ParameterEvaluatedConstraintDict](docs/models/ParameterEvaluatedConstraintDict.md)
- [ParameterEvaluationResult](docs/models/ParameterEvaluationResult.md)
- [ParameterEvaluationResultDict](docs/models/ParameterEvaluationResultDict.md)
- [ParameterId](docs/models/ParameterId.md)
- [ParameterKey](docs/models/ParameterKey.md)
- [ParameterOption](docs/models/ParameterOption.md)
- [ParameterOptionDict](docs/models/ParameterOptionDict.md)
- [ParameterValue](docs/models/ParameterValue.md)
- [PhraseQuery](docs/models/PhraseQuery.md)
- [PhraseQueryDict](docs/models/PhraseQueryDict.md)
- [Polygon](docs/models/Polygon.md)
- [PolygonDict](docs/models/PolygonDict.md)
- [PolygonValue](docs/models/PolygonValue.md)
- [PolygonValueDict](docs/models/PolygonValueDict.md)
- [Position](docs/models/Position.md)
- [PrefixQuery](docs/models/PrefixQuery.md)
- [PrefixQueryDict](docs/models/PrefixQueryDict.md)
- [PreviewMode](docs/models/PreviewMode.md)
- [PrimaryKeyValue](docs/models/PrimaryKeyValue.md)
- [PrincipalFilterType](docs/models/PrincipalFilterType.md)
- [PrincipalId](docs/models/PrincipalId.md)
- [PrincipalType](docs/models/PrincipalType.md)
- [Property](docs/models/Property.md)
- [PropertyApiName](docs/models/PropertyApiName.md)
- [PropertyDict](docs/models/PropertyDict.md)
- [PropertyFilter](docs/models/PropertyFilter.md)
- [PropertyId](docs/models/PropertyId.md)
- [PropertyV2](docs/models/PropertyV2.md)
- [PropertyV2Dict](docs/models/PropertyV2Dict.md)
- [PropertyValue](docs/models/PropertyValue.md)
- [PropertyValueEscapedString](docs/models/PropertyValueEscapedString.md)
- [QosError](docs/models/QosError.md)
- [QosErrorDict](docs/models/QosErrorDict.md)
- [QueryAggregation](docs/models/QueryAggregation.md)
- [QueryAggregationDict](docs/models/QueryAggregationDict.md)
- [QueryAggregationKeyType](docs/models/QueryAggregationKeyType.md)
- [QueryAggregationKeyTypeDict](docs/models/QueryAggregationKeyTypeDict.md)
- [QueryAggregationRange](docs/models/QueryAggregationRange.md)
- [QueryAggregationRangeDict](docs/models/QueryAggregationRangeDict.md)
- [QueryAggregationRangeSubType](docs/models/QueryAggregationRangeSubType.md)
- [QueryAggregationRangeSubTypeDict](docs/models/QueryAggregationRangeSubTypeDict.md)
- [QueryAggregationRangeType](docs/models/QueryAggregationRangeType.md)
- [QueryAggregationRangeTypeDict](docs/models/QueryAggregationRangeTypeDict.md)
- [QueryAggregationValueType](docs/models/QueryAggregationValueType.md)
- [QueryAggregationValueTypeDict](docs/models/QueryAggregationValueTypeDict.md)
- [QueryApiName](docs/models/QueryApiName.md)
- [QueryArrayType](docs/models/QueryArrayType.md)
- [QueryArrayTypeDict](docs/models/QueryArrayTypeDict.md)
- [QueryDataType](docs/models/QueryDataType.md)
- [QueryDataTypeDict](docs/models/QueryDataTypeDict.md)
- [QueryOutputV2](docs/models/QueryOutputV2.md)
- [QueryOutputV2Dict](docs/models/QueryOutputV2Dict.md)
- [QueryParameterV2](docs/models/QueryParameterV2.md)
- [QueryParameterV2Dict](docs/models/QueryParameterV2Dict.md)
- [QuerySetType](docs/models/QuerySetType.md)
- [QuerySetTypeDict](docs/models/QuerySetTypeDict.md)
- [QueryStructField](docs/models/QueryStructField.md)
- [QueryStructFieldDict](docs/models/QueryStructFieldDict.md)
- [QueryStructType](docs/models/QueryStructType.md)
- [QueryStructTypeDict](docs/models/QueryStructTypeDict.md)
- [QueryThreeDimensionalAggregation](docs/models/QueryThreeDimensionalAggregation.md)
- [QueryThreeDimensionalAggregationDict](docs/models/QueryThreeDimensionalAggregationDict.md)
- [QueryTwoDimensionalAggregation](docs/models/QueryTwoDimensionalAggregation.md)
- [QueryTwoDimensionalAggregationDict](docs/models/QueryTwoDimensionalAggregationDict.md)
- [QueryType](docs/models/QueryType.md)
- [QueryTypeDict](docs/models/QueryTypeDict.md)
- [QueryTypeV2](docs/models/QueryTypeV2.md)
- [QueryTypeV2Dict](docs/models/QueryTypeV2Dict.md)
- [QueryUnionType](docs/models/QueryUnionType.md)
- [QueryUnionTypeDict](docs/models/QueryUnionTypeDict.md)
- [RangeConstraint](docs/models/RangeConstraint.md)
- [RangeConstraintDict](docs/models/RangeConstraintDict.md)
- [Realm](docs/models/Realm.md)
- [ReferenceUpdate](docs/models/ReferenceUpdate.md)
- [ReferenceUpdateDict](docs/models/ReferenceUpdateDict.md)
- [ReferenceValue](docs/models/ReferenceValue.md)
- [ReferenceValueDict](docs/models/ReferenceValueDict.md)
- [RefreshObjectSet](docs/models/RefreshObjectSet.md)
- [RefreshObjectSetDict](docs/models/RefreshObjectSetDict.md)
- [RelativeTime](docs/models/RelativeTime.md)
- [RelativeTimeDict](docs/models/RelativeTimeDict.md)
- [RelativeTimeRange](docs/models/RelativeTimeRange.md)
- [RelativeTimeRangeDict](docs/models/RelativeTimeRangeDict.md)
- [RelativeTimeRelation](docs/models/RelativeTimeRelation.md)
- [RelativeTimeSeriesTimeUnit](docs/models/RelativeTimeSeriesTimeUnit.md)
- [ReleaseStatus](docs/models/ReleaseStatus.md)
- [RemoveGroupMembersRequest](docs/models/RemoveGroupMembersRequest.md)
- [RemoveGroupMembersRequestDict](docs/models/RemoveGroupMembersRequestDict.md)
- [RequestId](docs/models/RequestId.md)
- [ResourcePath](docs/models/ResourcePath.md)
- [ReturnEditsMode](docs/models/ReturnEditsMode.md)
- [SdkPackageName](docs/models/SdkPackageName.md)
- [SearchGroupsRequest](docs/models/SearchGroupsRequest.md)
- [SearchGroupsRequestDict](docs/models/SearchGroupsRequestDict.md)
- [SearchGroupsResponse](docs/models/SearchGroupsResponse.md)
- [SearchGroupsResponseDict](docs/models/SearchGroupsResponseDict.md)
- [SearchJsonQuery](docs/models/SearchJsonQuery.md)
- [SearchJsonQueryDict](docs/models/SearchJsonQueryDict.md)
- [SearchJsonQueryV2](docs/models/SearchJsonQueryV2.md)
- [SearchJsonQueryV2Dict](docs/models/SearchJsonQueryV2Dict.md)
- [SearchObjectsForInterfaceRequest](docs/models/SearchObjectsForInterfaceRequest.md)
- [SearchObjectsForInterfaceRequestDict](docs/models/SearchObjectsForInterfaceRequestDict.md)
- [SearchObjectsRequest](docs/models/SearchObjectsRequest.md)
- [SearchObjectsRequestDict](docs/models/SearchObjectsRequestDict.md)
- [SearchObjectsRequestV2](docs/models/SearchObjectsRequestV2.md)
- [SearchObjectsRequestV2Dict](docs/models/SearchObjectsRequestV2Dict.md)
- [SearchObjectsResponse](docs/models/SearchObjectsResponse.md)
- [SearchObjectsResponseDict](docs/models/SearchObjectsResponseDict.md)
- [SearchObjectsResponseV2](docs/models/SearchObjectsResponseV2.md)
- [SearchObjectsResponseV2Dict](docs/models/SearchObjectsResponseV2Dict.md)
- [SearchOrderBy](docs/models/SearchOrderBy.md)
- [SearchOrderByDict](docs/models/SearchOrderByDict.md)
- [SearchOrderByV2](docs/models/SearchOrderByV2.md)
- [SearchOrderByV2Dict](docs/models/SearchOrderByV2Dict.md)
- [SearchOrdering](docs/models/SearchOrdering.md)
- [SearchOrderingDict](docs/models/SearchOrderingDict.md)
- [SearchOrderingV2](docs/models/SearchOrderingV2.md)
- [SearchOrderingV2Dict](docs/models/SearchOrderingV2Dict.md)
- [SearchUsersRequest](docs/models/SearchUsersRequest.md)
- [SearchUsersRequestDict](docs/models/SearchUsersRequestDict.md)
- [SearchUsersResponse](docs/models/SearchUsersResponse.md)
- [SearchUsersResponseDict](docs/models/SearchUsersResponseDict.md)
- [SelectedPropertyApiName](docs/models/SelectedPropertyApiName.md)
- [SharedPropertyType](docs/models/SharedPropertyType.md)
- [SharedPropertyTypeApiName](docs/models/SharedPropertyTypeApiName.md)
- [SharedPropertyTypeDict](docs/models/SharedPropertyTypeDict.md)
- [SharedPropertyTypeRid](docs/models/SharedPropertyTypeRid.md)
- [ShortType](docs/models/ShortType.md)
- [ShortTypeDict](docs/models/ShortTypeDict.md)
- [SizeBytes](docs/models/SizeBytes.md)
- [StartsWithQuery](docs/models/StartsWithQuery.md)
- [StartsWithQueryDict](docs/models/StartsWithQueryDict.md)
- [StreamMessage](docs/models/StreamMessage.md)
- [StreamMessageDict](docs/models/StreamMessageDict.md)
- [StreamTimeSeriesPointsRequest](docs/models/StreamTimeSeriesPointsRequest.md)
- [StreamTimeSeriesPointsRequestDict](docs/models/StreamTimeSeriesPointsRequestDict.md)
- [StreamTimeSeriesPointsResponse](docs/models/StreamTimeSeriesPointsResponse.md)
- [StreamTimeSeriesPointsResponseDict](docs/models/StreamTimeSeriesPointsResponseDict.md)
- [StringLengthConstraint](docs/models/StringLengthConstraint.md)
- [StringLengthConstraintDict](docs/models/StringLengthConstraintDict.md)
- [StringRegexMatchConstraint](docs/models/StringRegexMatchConstraint.md)
- [StringRegexMatchConstraintDict](docs/models/StringRegexMatchConstraintDict.md)
- [StringType](docs/models/StringType.md)
- [StringTypeDict](docs/models/StringTypeDict.md)
- [StructFieldName](docs/models/StructFieldName.md)
- [Subdomain](docs/models/Subdomain.md)
- [SubmissionCriteriaEvaluation](docs/models/SubmissionCriteriaEvaluation.md)
- [SubmissionCriteriaEvaluationDict](docs/models/SubmissionCriteriaEvaluationDict.md)
- [SubscriptionClosed](docs/models/SubscriptionClosed.md)
- [SubscriptionClosedDict](docs/models/SubscriptionClosedDict.md)
- [SubscriptionError](docs/models/SubscriptionError.md)
- [SubscriptionErrorDict](docs/models/SubscriptionErrorDict.md)
- [SubscriptionId](docs/models/SubscriptionId.md)
- [SubscriptionSuccess](docs/models/SubscriptionSuccess.md)
- [SubscriptionSuccessDict](docs/models/SubscriptionSuccessDict.md)
- [SumAggregation](docs/models/SumAggregation.md)
- [SumAggregationDict](docs/models/SumAggregationDict.md)
- [SumAggregationV2](docs/models/SumAggregationV2.md)
- [SumAggregationV2Dict](docs/models/SumAggregationV2Dict.md)
- [SyncApplyActionResponseV2](docs/models/SyncApplyActionResponseV2.md)
- [SyncApplyActionResponseV2Dict](docs/models/SyncApplyActionResponseV2Dict.md)
- [TableExportFormat](docs/models/TableExportFormat.md)
- [ThirdPartyApplication](docs/models/ThirdPartyApplication.md)
- [ThirdPartyApplicationDict](docs/models/ThirdPartyApplicationDict.md)
- [ThirdPartyApplicationRid](docs/models/ThirdPartyApplicationRid.md)
- [ThreeDimensionalAggregation](docs/models/ThreeDimensionalAggregation.md)
- [ThreeDimensionalAggregationDict](docs/models/ThreeDimensionalAggregationDict.md)
- [TimeRange](docs/models/TimeRange.md)
- [TimeRangeDict](docs/models/TimeRangeDict.md)
- [TimeSeriesItemType](docs/models/TimeSeriesItemType.md)
- [TimeSeriesItemTypeDict](docs/models/TimeSeriesItemTypeDict.md)
- [TimeSeriesPoint](docs/models/TimeSeriesPoint.md)
- [TimeSeriesPointDict](docs/models/TimeSeriesPointDict.md)
- [TimeseriesType](docs/models/TimeseriesType.md)
- [TimeseriesTypeDict](docs/models/TimeseriesTypeDict.md)
- [TimestampType](docs/models/TimestampType.md)
- [TimestampTypeDict](docs/models/TimestampTypeDict.md)
- [TimeUnit](docs/models/TimeUnit.md)
- [TotalCount](docs/models/TotalCount.md)
- [Transaction](docs/models/Transaction.md)
- [TransactionCreatedTime](docs/models/TransactionCreatedTime.md)
- [TransactionDict](docs/models/TransactionDict.md)
- [TransactionRid](docs/models/TransactionRid.md)
- [TransactionStatus](docs/models/TransactionStatus.md)
- [TransactionType](docs/models/TransactionType.md)
- [TwoDimensionalAggregation](docs/models/TwoDimensionalAggregation.md)
- [TwoDimensionalAggregationDict](docs/models/TwoDimensionalAggregationDict.md)
- [UnevaluableConstraint](docs/models/UnevaluableConstraint.md)
- [UnevaluableConstraintDict](docs/models/UnevaluableConstraintDict.md)
- [UnsupportedType](docs/models/UnsupportedType.md)
- [UnsupportedTypeDict](docs/models/UnsupportedTypeDict.md)
- [UpdatedBy](docs/models/UpdatedBy.md)
- [UpdatedTime](docs/models/UpdatedTime.md)
- [User](docs/models/User.md)
- [UserDict](docs/models/UserDict.md)
- [UserId](docs/models/UserId.md)
- [UserSearchFilter](docs/models/UserSearchFilter.md)
- [UserSearchFilterDict](docs/models/UserSearchFilterDict.md)
- [UserUsername](docs/models/UserUsername.md)
- [ValidateActionRequest](docs/models/ValidateActionRequest.md)
- [ValidateActionRequestDict](docs/models/ValidateActionRequestDict.md)
- [ValidateActionResponse](docs/models/ValidateActionResponse.md)
- [ValidateActionResponseDict](docs/models/ValidateActionResponseDict.md)
- [ValidateActionResponseV2](docs/models/ValidateActionResponseV2.md)
- [ValidateActionResponseV2Dict](docs/models/ValidateActionResponseV2Dict.md)
- [ValidationResult](docs/models/ValidationResult.md)
- [ValueType](docs/models/ValueType.md)
- [Version](docs/models/Version.md)
- [VersionDict](docs/models/VersionDict.md)
- [VersionVersion](docs/models/VersionVersion.md)
- [Website](docs/models/Website.md)
- [WebsiteDict](docs/models/WebsiteDict.md)
- [WithinBoundingBoxPoint](docs/models/WithinBoundingBoxPoint.md)
- [WithinBoundingBoxPointDict](docs/models/WithinBoundingBoxPointDict.md)
- [WithinBoundingBoxQuery](docs/models/WithinBoundingBoxQuery.md)
- [WithinBoundingBoxQueryDict](docs/models/WithinBoundingBoxQueryDict.md)
- [WithinDistanceOfQuery](docs/models/WithinDistanceOfQuery.md)
- [WithinDistanceOfQueryDict](docs/models/WithinDistanceOfQueryDict.md)
- [WithinPolygonQuery](docs/models/WithinPolygonQuery.md)
- [WithinPolygonQueryDict](docs/models/WithinPolygonQueryDict.md)

## Contributions

This repository does not accept code contributions.

If you have any questions, concerns, or ideas for improvements, create an
issue with Palantir Support.

## License
This project is made available under the [Apache 2.0 License](/LICENSE).
