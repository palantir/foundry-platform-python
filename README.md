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

create_dataset_request = {
    "name": "My Dataset",
    "parentFolderRid": "ri.foundry.main.folder.bfe58487-4c56-4c58-aba7-25defd6163c4",
}  # CreateDatasetRequest | CreateDatasetRequest


try:
    api_response = foundry_client.datasets.Dataset.create(
        create_dataset_request=create_dataset_request
    )
    print("The Dataset.create response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Dataset.create: %s\n" % e)

```

Want to learn more about this Foundry SDK library? Review the following sections.

↳ [Error handling](#errors): Learn more about HTTP & data validation error handling  
↳ [Static type analysis](#static-types): Learn about the static type analysis capabilities of this library

## Error handling
### Data validation
The SDK employs [Pydantic](https://docs.pydantic.dev/latest/) for runtime validation
of arguments. In the example below, we are passing in a number to `transactionRid`
which should actually be a string type:

```python
foundry_client.datasets.Branch.create(
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

<a id="static-types"></a>
## Static type analysis
This library uses [Pydantic](https://docs.pydantic.dev) for creating and validating data models which you will see in the
method definitions (see [Documentation for Models](#models) below for a full list of models). All request parameters with nested
objects used [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict) whereas responses use Pydantic models.
For example, here is how `Branch.create` method is defined in the datasets namespace:

```python
    def create(
        self,
        dataset_rid: DatasetRid,
        *,
        create_branch_request: CreateBranchRequest,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Branch:
        ...
```

If you are using a static type checker (for example, [mypy](https://mypy-lang.org), [pyright](https://github.com/microsoft/pyright)), you
get static type analysis for the arguments you provide to the function *and* with the response. For example, if you pass an `int`
to `branchId` while calling `create` and then try to access `branchId` in returned [`Branch`](docs/Branch.md) object (the
property is actually called `branch_id`), you will get the following errors:


```python
branch = foundry_client.datasets.Branch.create(
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
**Datasets** | Dataset | [**create**](docs/namespaces/Datasets/Dataset.md#create) | **POST** /v1/datasets |
**Datasets** | Dataset | [**get**](docs/namespaces/Datasets/Dataset.md#get) | **GET** /v1/datasets/{datasetRid} |
**Datasets** | Dataset | [**read_table**](docs/namespaces/Datasets/Dataset.md#read_table) | **GET** /v1/datasets/{datasetRid}/readTable |
**Datasets** | Dataset | [**put_schema**](docs/namespaces/Datasets/Dataset.md#put_schema) | **PUT** /v1/datasets/{datasetRid}/schema |
**Datasets** | Dataset | [**get_schema**](docs/namespaces/Datasets/Dataset.md#get_schema) | **GET** /v1/datasets/{datasetRid}/schema |
**Datasets** | Dataset | [**delete_schema**](docs/namespaces/Datasets/Dataset.md#delete_schema) | **DELETE** /v1/datasets/{datasetRid}/schema |
**Datasets** | Branch | [**create**](docs/namespaces/Datasets/Branch.md#create) | **POST** /v1/datasets/{datasetRid}/branches |
**Datasets** | Branch | [**get**](docs/namespaces/Datasets/Branch.md#get) | **GET** /v1/datasets/{datasetRid}/branches/{branchId} |
**Datasets** | Branch | [**delete**](docs/namespaces/Datasets/Branch.md#delete) | **DELETE** /v1/datasets/{datasetRid}/branches/{branchId} |
**Datasets** | Branch | [**iterator**](docs/namespaces/Datasets/Branch.md#iterator) | **GET** /v1/datasets/{datasetRid}/branches |
**Datasets** | Transaction | [**create**](docs/namespaces/Datasets/Transaction.md#create) | **POST** /v1/datasets/{datasetRid}/transactions |
**Datasets** | Transaction | [**get**](docs/namespaces/Datasets/Transaction.md#get) | **GET** /v1/datasets/{datasetRid}/transactions/{transactionRid} |
**Datasets** | Transaction | [**commit**](docs/namespaces/Datasets/Transaction.md#commit) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/commit |
**Datasets** | Transaction | [**abort**](docs/namespaces/Datasets/Transaction.md#abort) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/abort |
**Datasets** | File | [**iterator**](docs/namespaces/Datasets/File.md#iterator) | **GET** /v1/datasets/{datasetRid}/files |
**Datasets** | File | [**upload**](docs/namespaces/Datasets/File.md#upload) | **POST** /v1/datasets/{datasetRid}/files:upload |
**Datasets** | File | [**get_metadata**](docs/namespaces/Datasets/File.md#get_metadata) | **GET** /v1/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**delete**](docs/namespaces/Datasets/File.md#delete) | **DELETE** /v1/datasets/{datasetRid}/files/{filePath} |
**Datasets** | File | [**get_content**](docs/namespaces/Datasets/File.md#get_content) | **GET** /v1/datasets/{datasetRid}/files/{filePath}/content |
**Ontologies** | Ontology | [**iterator**](docs/namespaces/Ontologies/Ontology.md#iterator) | **GET** /v1/ontologies |
**Ontologies** | Ontology | [**get**](docs/namespaces/Ontologies/Ontology.md#get) | **GET** /v1/ontologies/{ontologyRid} |
**Ontologies** | ObjectType | [**iterator**](docs/namespaces/Ontologies/ObjectType.md#iterator) | **GET** /v1/ontologies/{ontologyRid}/objectTypes |
**Ontologies** | ObjectType | [**get**](docs/namespaces/Ontologies/ObjectType.md#get) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType} |
**Ontologies** | ObjectType | [**list_outgoing_link_types**](docs/namespaces/Ontologies/ObjectType.md#list_outgoing_link_types) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes |
**Ontologies** | ObjectType | [**get_outgoing_link_type**](docs/namespaces/Ontologies/ObjectType.md#get_outgoing_link_type) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} |
**Ontologies** | ActionType | [**iterator**](docs/namespaces/Ontologies/ActionType.md#iterator) | **GET** /v1/ontologies/{ontologyRid}/actionTypes |
**Ontologies** | ActionType | [**get**](docs/namespaces/Ontologies/ActionType.md#get) | **GET** /v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName} |
**Ontologies** | QueryType | [**iterator**](docs/namespaces/Ontologies/QueryType.md#iterator) | **GET** /v1/ontologies/{ontologyRid}/queryTypes |
**Ontologies** | QueryType | [**get**](docs/namespaces/Ontologies/QueryType.md#get) | **GET** /v1/ontologies/{ontologyRid}/queryTypes/{queryApiName} |


<a id="models"></a>
## Documentation for models

- [CreateDatasetRequest](docs/models/CreateDatasetRequest.md)
- [DatasetName](docs/models/DatasetName.md)
- [FolderRid](docs/models/FolderRid.md)
- [Dataset](docs/models/Dataset.md)
- [DatasetRid](docs/models/DatasetRid.md)
- [BranchId](docs/models/BranchId.md)
- [TransactionRid](docs/models/TransactionRid.md)
- [TableExportFormat](docs/models/TableExportFormat.md)
- [PreviewMode](docs/models/PreviewMode.md)
- [CreateBranchRequest](docs/models/CreateBranchRequest.md)
- [Branch](docs/models/Branch.md)
- [PageSize](docs/models/PageSize.md)
- [PageToken](docs/models/PageToken.md)
- [ListBranchesResponse](docs/models/ListBranchesResponse.md)
- [CreateTransactionRequest](docs/models/CreateTransactionRequest.md)
- [TransactionType](docs/models/TransactionType.md)
- [Transaction](docs/models/Transaction.md)
- [TransactionStatus](docs/models/TransactionStatus.md)
- [ListFilesResponse](docs/models/ListFilesResponse.md)
- [File](docs/models/File.md)
- [FilePath](docs/models/FilePath.md)
- [ListOntologiesResponse](docs/models/ListOntologiesResponse.md)
- [Ontology](docs/models/Ontology.md)
- [OntologyApiName](docs/models/OntologyApiName.md)
- [DisplayName](docs/models/DisplayName.md)
- [OntologyRid](docs/models/OntologyRid.md)
- [ListObjectTypesResponse](docs/models/ListObjectTypesResponse.md)
- [ObjectType](docs/models/ObjectType.md)
- [ObjectTypeApiName](docs/models/ObjectTypeApiName.md)
- [ReleaseStatus](docs/models/ReleaseStatus.md)
- [ObjectTypeVisibility](docs/models/ObjectTypeVisibility.md)
- [PropertyApiName](docs/models/PropertyApiName.md)
- [Property](docs/models/Property.md)
- [ValueType](docs/models/ValueType.md)
- [ObjectTypeRid](docs/models/ObjectTypeRid.md)
- [ListActionTypesResponse](docs/models/ListActionTypesResponse.md)
- [ActionType](docs/models/ActionType.md)
- [ActionTypeApiName](docs/models/ActionTypeApiName.md)
- [Parameter](docs/models/Parameter.md)
- [OntologyDataType](docs/models/OntologyDataType.md)
- [AnyType](docs/models/AnyType.md)
- [BinaryType](docs/models/BinaryType.md)
- [BooleanType](docs/models/BooleanType.md)
- [ByteType](docs/models/ByteType.md)
- [DateType](docs/models/DateType.md)
- [DecimalType](docs/models/DecimalType.md)
- [DoubleType](docs/models/DoubleType.md)
- [FloatType](docs/models/FloatType.md)
- [IntegerType](docs/models/IntegerType.md)
- [LongType](docs/models/LongType.md)
- [ShortType](docs/models/ShortType.md)
- [StringType](docs/models/StringType.md)
- [TimestampType](docs/models/TimestampType.md)
- [OntologyArrayType](docs/models/OntologyArrayType.md)
- [OntologyMapType](docs/models/OntologyMapType.md)
- [OntologySetType](docs/models/OntologySetType.md)
- [OntologyStructType](docs/models/OntologyStructType.md)
- [OntologyStructField](docs/models/OntologyStructField.md)
- [StructFieldName](docs/models/StructFieldName.md)
- [OntologyObjectType](docs/models/OntologyObjectType.md)
- [OntologyObjectSetType](docs/models/OntologyObjectSetType.md)
- [UnsupportedType](docs/models/UnsupportedType.md)
- [ActionTypeRid](docs/models/ActionTypeRid.md)
- [LogicRule](docs/models/LogicRule.md)
- [CreateObjectRule](docs/models/CreateObjectRule.md)
- [ModifyObjectRule](docs/models/ModifyObjectRule.md)
- [DeleteObjectRule](docs/models/DeleteObjectRule.md)
- [CreateLinkRule](docs/models/CreateLinkRule.md)
- [LinkTypeApiName](docs/models/LinkTypeApiName.md)
- [DeleteLinkRule](docs/models/DeleteLinkRule.md)
- [SelectedPropertyApiName](docs/models/SelectedPropertyApiName.md)
- [OrderBy](docs/models/OrderBy.md)
- [ListObjectsResponse](docs/models/ListObjectsResponse.md)
- [OntologyObject](docs/models/OntologyObject.md)
- [PropertyValue](docs/models/PropertyValue.md)
- [ObjectRid](docs/models/ObjectRid.md)
- [PropertyValueEscapedString](docs/models/PropertyValueEscapedString.md)
- [ListLinkedObjectsResponse](docs/models/ListLinkedObjectsResponse.md)
- [ApplyActionRequest](docs/models/ApplyActionRequest.md)
- [DataValue](docs/models/DataValue.md)
- [ApplyActionResponse](docs/models/ApplyActionResponse.md)
- [BatchApplyActionRequest](docs/models/BatchApplyActionRequest.md)
- [BatchApplyActionResponse](docs/models/BatchApplyActionResponse.md)
- [AsyncApplyActionRequest](docs/models/AsyncApplyActionRequest.md)
- [AsyncActionOperation](docs/models/AsyncActionOperation.md)
- [ActionRid](docs/models/ActionRid.md)
- [ListQueryTypesResponse](docs/models/ListQueryTypesResponse.md)
- [QueryType](docs/models/QueryType.md)
- [QueryApiName](docs/models/QueryApiName.md)
- [FunctionRid](docs/models/FunctionRid.md)
- [FunctionVersion](docs/models/FunctionVersion.md)
- [ExecuteQueryRequest](docs/models/ExecuteQueryRequest.md)
- [ExecuteQueryResponse](docs/models/ExecuteQueryResponse.md)
- [SearchObjectsRequest](docs/models/SearchObjectsRequest.md)
- [SearchJsonQueryRequest](docs/models/SearchJsonQueryRequest.md)
- [LtQueryRequest](docs/models/LtQueryRequest.md)
- [GtQueryRequest](docs/models/GtQueryRequest.md)
- [LteQueryRequest](docs/models/LteQueryRequest.md)
- [GteQueryRequest](docs/models/GteQueryRequest.md)
- [EqualsQueryRequest](docs/models/EqualsQueryRequest.md)
- [IsNullQueryRequest](docs/models/IsNullQueryRequest.md)
- [ContainsQueryRequest](docs/models/ContainsQueryRequest.md)
- [AndQueryRequest](docs/models/AndQueryRequest.md)
- [OrQueryRequest](docs/models/OrQueryRequest.md)
- [NotQueryRequest](docs/models/NotQueryRequest.md)
- [PrefixQueryRequest](docs/models/PrefixQueryRequest.md)
- [PhraseQueryRequest](docs/models/PhraseQueryRequest.md)
- [AnyTermQueryRequest](docs/models/AnyTermQueryRequest.md)
- [Fuzzy](docs/models/Fuzzy.md)
- [AllTermsQueryRequest](docs/models/AllTermsQueryRequest.md)
- [SearchOrderByRequest](docs/models/SearchOrderByRequest.md)
- [SearchOrderingRequest](docs/models/SearchOrderingRequest.md)
- [SearchObjectsResponse](docs/models/SearchObjectsResponse.md)
- [ValidateActionRequest](docs/models/ValidateActionRequest.md)
- [ValidateActionResponse](docs/models/ValidateActionResponse.md)
- [ValidationResult](docs/models/ValidationResult.md)
- [SubmissionCriteriaEvaluation](docs/models/SubmissionCriteriaEvaluation.md)
- [ParameterEvaluationResult](docs/models/ParameterEvaluationResult.md)
- [ParameterEvaluatedConstraint](docs/models/ParameterEvaluatedConstraint.md)
- [ArraySize](docs/models/ArraySize.md)
- [GroupMember](docs/models/GroupMember.md)
- [ObjectPropertyValue](docs/models/ObjectPropertyValue.md)
- [ObjectQueryResult](docs/models/ObjectQueryResult.md)
- [OneOf](docs/models/OneOf.md)
- [ParameterOption](docs/models/ParameterOption.md)
- [Range](docs/models/Range.md)
- [StringLength](docs/models/StringLength.md)
- [StringRegexMatch](docs/models/StringRegexMatch.md)
- [Unevaluable](docs/models/Unevaluable.md)
- [ContentLength](docs/models/ContentLength.md)
- [ContentType](docs/models/ContentType.md)
- [Filename](docs/models/Filename.md)
- [Attachment](docs/models/Attachment.md)
- [AttachmentRid](docs/models/AttachmentRid.md)
- [SizeBytes](docs/models/SizeBytes.md)
- [MediaType](docs/models/MediaType.md)
- [AggregateObjectsRequest](docs/models/AggregateObjectsRequest.md)
- [AggregationRequest](docs/models/AggregationRequest.md)
- [MaxAggregationRequest](docs/models/MaxAggregationRequest.md)
- [AggregationMetricName](docs/models/AggregationMetricName.md)
- [MinAggregationRequest](docs/models/MinAggregationRequest.md)
- [AvgAggregationRequest](docs/models/AvgAggregationRequest.md)
- [SumAggregationRequest](docs/models/SumAggregationRequest.md)
- [CountAggregationRequest](docs/models/CountAggregationRequest.md)
- [ApproximateDistinctAggregationRequest](docs/models/ApproximateDistinctAggregationRequest.md)
- [AggregationGroupByRequest](docs/models/AggregationGroupByRequest.md)
- [AggregationFixedWidthGroupingRequest](docs/models/AggregationFixedWidthGroupingRequest.md)
- [AggregationRangesGroupingRequest](docs/models/AggregationRangesGroupingRequest.md)
- [AggregationRangeRequest](docs/models/AggregationRangeRequest.md)
- [AggregationExactGroupingRequest](docs/models/AggregationExactGroupingRequest.md)
- [AggregationDurationGroupingRequest](docs/models/AggregationDurationGroupingRequest.md)
- [Duration](docs/models/Duration.md)
- [AggregateObjectsResponse](docs/models/AggregateObjectsResponse.md)
- [AggregateObjectsResponseItem](docs/models/AggregateObjectsResponseItem.md)
- [AggregationGroupValue](docs/models/AggregationGroupValue.md)
- [AggregationMetricResult](docs/models/AggregationMetricResult.md)
- [ListOutgoingLinkTypesResponse](docs/models/ListOutgoingLinkTypesResponse.md)
- [LinkTypeSide](docs/models/LinkTypeSide.md)
- [LinkTypeSideCardinality](docs/models/LinkTypeSideCardinality.md)

## Contributions

This repository does not accept code contributions.

If you have any questions, concerns, or ideas for improvements, create an
issue with Palantir Support.

## License
This project is made available under the [Apache 2.0 License](/LICENSE).
