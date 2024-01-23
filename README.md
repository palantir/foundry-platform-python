# Foundry Platform SDK

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/foundry-platform-sdk)
[![PyPI](https://img.shields.io/pypi/v/foundry-platform-sdk)](https://pypi.org/project/foundry-platform-sdk/)
[![License](https://img.shields.io/badge/License-Apache%202.0-lightgrey.svg)](https://opensource.org/licenses/Apache-2.0)

> [!WARNING]
> This SDK is incubating and subject to change.

The Foundry Platform SDK is a Python SDK built on top of the Foundry API. Review [Foundry API documentation](https://www.palantir.com/docs/foundry/api/) for more details.

> [!NOTE]
> This Python package is automatically generated using the [OpenAPI Generator](https://openapi-generator.tech) tool.


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

import time
import foundry
from foundry.rest import ApiException
from foundry import FoundryClient
from foundry import UserTokenAuth
from pprint import pprint

foundry_client = FoundryClient(auth=UserTokenAuth(...), hostname="example.palantirfoundry.com")

dataset_rid = 'ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da' # str | The Resource Identifier (RID) of the Dataset that contains the Transaction.
transaction_rid = 'ri.foundry.main.transaction.abffc380-ea68-4843-9be1-9f44d2565496' # str | The Resource Identifier (RID) of the Transaction.

try:
    api_response = foundry_client.datasets.abort_transaction(dataset_rid, transaction_rid)
    print("The response of DatasetsApiServiceApi -> abort_transaction:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApiServiceApi -> abort_transaction: %s\n" % e)

```

Want to learn more about this Foundry SDK library? Review the following sections.

↳ [Error handling](#errors): Learn more about HTTP & data validation error handling  
<!--
↳ [Search query builders](#docs-for-search-query-builders): Learn about to efficiently contstruct ontology search queries using the query builders  
-->
↳ [Static type analysis](#static-types): Learn about the static type analysis capabilities of this library

## Error handling
### Data validation
The SDK employs [Pydantic](https://docs.pydantic.dev/latest/) for runtime validation
of arguments. In the example below, we are passing in a number to `transactionRid`
which should actually be a string type:

```python
foundry_client.datasets.create_branch(
    "ri.foundry.main.dataset.abc",
    # Alternatively, you could have passed in a dict {"branchId": "123", "transactionRid": 123}
    create_branch_request=CreateBranchRequest(branchId="123", transactionRid=123),
)
```

If you did this, you would receive an error that looks something like:

```
pydantic_core._pydantic_core.ValidationError: 1 validation error for CreateBranchRequest
transactionRid
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
    api_response = foundry_client.datasets.abort_transaction(dataset_rid, transaction_rid)
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
This library uses [Pydantic](https://docs.pydantic.dev) for creating data models which you will see in the
method definitions (see [Documentation for Models](#models) below for a full list of models). For
example, here is how `create_branch` method is defined in the dataset service:

```python
    def create_branch(
        self,
        dataset_rid: Annotated[StrictStr, Field(description="The Resource Identifier (RID) of the Dataset on which to create the Branch.")],
        create_branch_request: CreateBranchRequest,
        ...
    ) -> Branch:
        ...
```

If you are using a static type checker (for example, [mypy](https://mypy-lang.org), [pyright](https://github.com/microsoft/pyright)), you
get static type analysis for the arguments you provide to the function *and* with the response. For example, if you pass an `int`
to `branchId` while calling `create_branch` and then try to access `branchId` in returned [`Branch`](docs/Branch.md) object (the
property is actually called `branch_id`), you will get the following errors:


```python
branch = foundry_client.datasets.create_branch(
    "ri.foundry.main.dataset.abc",
    create_branch_request=CreateBranchRequest(
        # ERROR: Argument of type "Literal[123]" cannot be assigned to parameter "branchId" of type "StrictStr" in function "__init__"
        branchId=123
    ),
)
# ERROR: Cannot access member "branchId" for type "Branch"
print(branch.branchId)
```

> [!IMPORTANT]
> For static type analysis to work when passing in a request body, you *must* use the class
instead of passing in a dictionary.

<!--
<a id="docs-for-search-query-builders"></a>
## Search Query Builders

> [!TIP]
> For a more tailored developer experience, we recommend using the OSDK for interacting with your
ontology. See [Foundry Platform SDK vs. Ontology SDK](#sdk-vs-sdk) for more information.

Performing Ontology queries can invovle building large dictionaries depending
on the complexity of the query. Additionally, when using dictionaries, you get
no static type analysis.

To address these limitations, the `SearchQueryBuilder` and `SearchQueryBuilderV2`
Python classes allow you to easily create complex search queries without having
to manually build dictionaries. These classes provide a more expressive and readable way
to define queries using a simple and intuitive syntax.

### Usage
To use the builder classes, you just need to import them from the `builders`
package. The class you use depends on your version of the Ontology API.

```python
from foundry.builders import SearchQuery
# OR
from foundry.builders import SearchQueryV2
```

### Examples
Here are some more examples to help you get started with the query builders:

Simple equality query:
```python
query = SearchQuery.eq(field="status", value="active")
```

Query with multiple conditions:
```python
query = SearchQuery.and_(
    SearchQuery.eq(field="status", value="active"),
    SearchQuery.contains(field="tags", value="urgent"),
)
```

Query with nested conditions:
```python
query = SearchQuery.and_(
    SearchQuery.eq(field="status", value="active"),
    SearchQuery.or_(
        SearchQuery.contains(field="tags", value="urgent"),
        SearchQuery.gt(field="priority", value=3),
    ),
)
```

Further details can be found in the corresponding class documentation:

- [SearchQuery](docs/SearchQuery.md)
- [SearchQueryV2](docs/SearchQueryV2.md)
-->

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

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DatasetsApiServiceApi* | [**abort_transaction**](docs/DatasetsApiServiceApi.md#abort_transaction) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/abort | 
*DatasetsApiServiceApi* | [**commit_transaction**](docs/DatasetsApiServiceApi.md#commit_transaction) | **POST** /v1/datasets/{datasetRid}/transactions/{transactionRid}/commit | 
*DatasetsApiServiceApi* | [**create_branch**](docs/DatasetsApiServiceApi.md#create_branch) | **POST** /v1/datasets/{datasetRid}/branches | 
*DatasetsApiServiceApi* | [**create_dataset**](docs/DatasetsApiServiceApi.md#create_dataset) | **POST** /v1/datasets | 
*DatasetsApiServiceApi* | [**create_transaction**](docs/DatasetsApiServiceApi.md#create_transaction) | **POST** /v1/datasets/{datasetRid}/transactions | 
*DatasetsApiServiceApi* | [**delete_branch**](docs/DatasetsApiServiceApi.md#delete_branch) | **DELETE** /v1/datasets/{datasetRid}/branches/{branchId} | 
*DatasetsApiServiceApi* | [**delete_file**](docs/DatasetsApiServiceApi.md#delete_file) | **DELETE** /v1/datasets/{datasetRid}/files/{filePath} | 
*DatasetsApiServiceApi* | [**delete_schema**](docs/DatasetsApiServiceApi.md#delete_schema) | **DELETE** /v1/datasets/{datasetRid}/schema | 
*DatasetsApiServiceApi* | [**get_branch**](docs/DatasetsApiServiceApi.md#get_branch) | **GET** /v1/datasets/{datasetRid}/branches/{branchId} | 
*DatasetsApiServiceApi* | [**get_dataset**](docs/DatasetsApiServiceApi.md#get_dataset) | **GET** /v1/datasets/{datasetRid} | 
*DatasetsApiServiceApi* | [**get_file_content**](docs/DatasetsApiServiceApi.md#get_file_content) | **GET** /v1/datasets/{datasetRid}/files/{filePath}/content | 
*DatasetsApiServiceApi* | [**get_file_metadata**](docs/DatasetsApiServiceApi.md#get_file_metadata) | **GET** /v1/datasets/{datasetRid}/files/{filePath} | 
*DatasetsApiServiceApi* | [**get_schema**](docs/DatasetsApiServiceApi.md#get_schema) | **GET** /v1/datasets/{datasetRid}/schema | 
*DatasetsApiServiceApi* | [**get_transaction**](docs/DatasetsApiServiceApi.md#get_transaction) | **GET** /v1/datasets/{datasetRid}/transactions/{transactionRid} | 
*DatasetsApiServiceApi* | [**list_branches**](docs/DatasetsApiServiceApi.md#list_branches) | **GET** /v1/datasets/{datasetRid}/branches | 
*DatasetsApiServiceApi* | [**list_files**](docs/DatasetsApiServiceApi.md#list_files) | **GET** /v1/datasets/{datasetRid}/files | 
*DatasetsApiServiceApi* | [**put_schema**](docs/DatasetsApiServiceApi.md#put_schema) | **PUT** /v1/datasets/{datasetRid}/schema | 
*DatasetsApiServiceApi* | [**read_table**](docs/DatasetsApiServiceApi.md#read_table) | **GET** /v1/datasets/{datasetRid}/readTable | 
*DatasetsApiServiceApi* | [**upload_file**](docs/DatasetsApiServiceApi.md#upload_file) | **POST** /v1/datasets/{datasetRid}/files:upload | 
*OntologiesApiServiceApi* | [**get_action_type**](docs/OntologiesApiServiceApi.md#get_action_type) | **GET** /v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName} | 
*OntologiesApiServiceApi* | [**get_object_type**](docs/OntologiesApiServiceApi.md#get_object_type) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType} | 
*OntologiesApiServiceApi* | [**get_ontology**](docs/OntologiesApiServiceApi.md#get_ontology) | **GET** /v1/ontologies/{ontologyRid} | 
*OntologiesApiServiceApi* | [**get_outgoing_link_type**](docs/OntologiesApiServiceApi.md#get_outgoing_link_type) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} | 
*OntologiesApiServiceApi* | [**get_query_type**](docs/OntologiesApiServiceApi.md#get_query_type) | **GET** /v1/ontologies/{ontologyRid}/queryTypes/{queryApiName} | 
*OntologiesApiServiceApi* | [**list_action_types**](docs/OntologiesApiServiceApi.md#list_action_types) | **GET** /v1/ontologies/{ontologyRid}/actionTypes | 
*OntologiesApiServiceApi* | [**list_object_types**](docs/OntologiesApiServiceApi.md#list_object_types) | **GET** /v1/ontologies/{ontologyRid}/objectTypes | 
*OntologiesApiServiceApi* | [**list_ontologies**](docs/OntologiesApiServiceApi.md#list_ontologies) | **GET** /v1/ontologies | 
*OntologiesApiServiceApi* | [**list_outgoing_link_types**](docs/OntologiesApiServiceApi.md#list_outgoing_link_types) | **GET** /v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes | 
*OntologiesApiServiceApi* | [**list_query_types**](docs/OntologiesApiServiceApi.md#list_query_types) | **GET** /v1/ontologies/{ontologyRid}/queryTypes | 
*OntologiesV2ApiServiceApi* | [**get_action_type**](docs/OntologiesV2ApiServiceApi.md#get_action_type) | **GET** /v2/ontologies/{ontology}/actionTypes/{actionType} | 
*OntologiesV2ApiServiceApi* | [**get_deployment**](docs/OntologiesV2ApiServiceApi.md#get_deployment) | **GET** /v2/ontologies/{ontology}/models/deployments/{deployment} | 
*OntologiesV2ApiServiceApi* | [**get_object_type**](docs/OntologiesV2ApiServiceApi.md#get_object_type) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType} | 
*OntologiesV2ApiServiceApi* | [**get_ontology_full_metadata**](docs/OntologiesV2ApiServiceApi.md#get_ontology_full_metadata) | **GET** /v2/ontologies/{ontology}/fullMetadata | 
*OntologiesV2ApiServiceApi* | [**get_ontology**](docs/OntologiesV2ApiServiceApi.md#get_ontology) | **GET** /v2/ontologies/{ontology} | 
*OntologiesV2ApiServiceApi* | [**get_outgoing_link_type**](docs/OntologiesV2ApiServiceApi.md#get_outgoing_link_type) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType} | 
*OntologiesV2ApiServiceApi* | [**get_query_type**](docs/OntologiesV2ApiServiceApi.md#get_query_type) | **GET** /v2/ontologies/{ontology}/queryTypes/{queryApiName} | 
*OntologiesV2ApiServiceApi* | [**list_action_types**](docs/OntologiesV2ApiServiceApi.md#list_action_types) | **GET** /v2/ontologies/{ontology}/actionTypes | 
*OntologiesV2ApiServiceApi* | [**list_deployments**](docs/OntologiesV2ApiServiceApi.md#list_deployments) | **GET** /v2/ontologies/{ontology}/models/deployments | 
*OntologiesV2ApiServiceApi* | [**list_object_types**](docs/OntologiesV2ApiServiceApi.md#list_object_types) | **GET** /v2/ontologies/{ontology}/objectTypes | 
*OntologiesV2ApiServiceApi* | [**list_ontologies**](docs/OntologiesV2ApiServiceApi.md#list_ontologies) | **GET** /v2/ontologies | 
*OntologiesV2ApiServiceApi* | [**list_outgoing_link_types**](docs/OntologiesV2ApiServiceApi.md#list_outgoing_link_types) | **GET** /v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes | 
*OntologiesV2ApiServiceApi* | [**list_query_types**](docs/OntologiesV2ApiServiceApi.md#list_query_types) | **GET** /v2/ontologies/{ontology}/queryTypes | 


<a id="models"></a>
## Documentation for models

 - [ActionParameterArrayType](docs/ActionParameterArrayType.md)
 - [ActionParameterType](docs/ActionParameterType.md)
 - [ActionParameterV2](docs/ActionParameterV2.md)
 - [ActionType](docs/ActionType.md)
 - [ActionTypeV2](docs/ActionTypeV2.md)
 - [AnyType](docs/AnyType.md)
 - [AttachmentType](docs/AttachmentType.md)
 - [BinaryType](docs/BinaryType.md)
 - [BooleanType](docs/BooleanType.md)
 - [Branch](docs/Branch.md)
 - [ByteType](docs/ByteType.md)
 - [CreateBranchRequest](docs/CreateBranchRequest.md)
 - [CreateDatasetRequest](docs/CreateDatasetRequest.md)
 - [CreateLinkRule](docs/CreateLinkRule.md)
 - [CreateObjectRule](docs/CreateObjectRule.md)
 - [CreateTransactionRequest](docs/CreateTransactionRequest.md)
 - [Dataset](docs/Dataset.md)
 - [DateType](docs/DateType.md)
 - [DecimalType](docs/DecimalType.md)
 - [DeleteLinkRule](docs/DeleteLinkRule.md)
 - [DeleteObjectRule](docs/DeleteObjectRule.md)
 - [DeploymentApi](docs/DeploymentApi.md)
 - [DeploymentListing](docs/DeploymentListing.md)
 - [DeploymentMetadata](docs/DeploymentMetadata.md)
 - [DeploymentTransformApi](docs/DeploymentTransformApi.md)
 - [DoubleType](docs/DoubleType.md)
 - [File](docs/File.md)
 - [FloatType](docs/FloatType.md)
 - [GeoPoint](docs/GeoPoint.md)
 - [GeoPointType](docs/GeoPointType.md)
 - [GeoShapeType](docs/GeoShapeType.md)
 - [Geometry](docs/Geometry.md)
 - [GeometryCollection](docs/GeometryCollection.md)
 - [IntegerType](docs/IntegerType.md)
 - [LineString](docs/LineString.md)
 - [LinkTypeSide](docs/LinkTypeSide.md)
 - [LinkTypeSideCardinality](docs/LinkTypeSideCardinality.md)
 - [LinkTypeSideV2](docs/LinkTypeSideV2.md)
 - [ListActionTypesResponse](docs/ListActionTypesResponse.md)
 - [ListActionTypesResponseV2](docs/ListActionTypesResponseV2.md)
 - [ListBranchesResponse](docs/ListBranchesResponse.md)
 - [ListDeploymentsResponse](docs/ListDeploymentsResponse.md)
 - [ListFilesResponse](docs/ListFilesResponse.md)
 - [ListObjectTypesResponse](docs/ListObjectTypesResponse.md)
 - [ListObjectTypesV2Response](docs/ListObjectTypesV2Response.md)
 - [ListOntologiesResponse](docs/ListOntologiesResponse.md)
 - [ListOntologiesV2Response](docs/ListOntologiesV2Response.md)
 - [ListOutgoingLinkTypesResponse](docs/ListOutgoingLinkTypesResponse.md)
 - [ListOutgoingLinkTypesResponseV2](docs/ListOutgoingLinkTypesResponseV2.md)
 - [ListQueryTypesResponse](docs/ListQueryTypesResponse.md)
 - [ListQueryTypesResponseV2](docs/ListQueryTypesResponseV2.md)
 - [LogicRule](docs/LogicRule.md)
 - [LongType](docs/LongType.md)
 - [ModelApiArrayType](docs/ModelApiArrayType.md)
 - [ModelApiDataType](docs/ModelApiDataType.md)
 - [ModelApiMapType](docs/ModelApiMapType.md)
 - [ModelApiStructField](docs/ModelApiStructField.md)
 - [ModelApiStructType](docs/ModelApiStructType.md)
 - [ModelApiType](docs/ModelApiType.md)
 - [ModelApiUnionType](docs/ModelApiUnionType.md)
 - [ModelProperty](docs/ModelProperty.md)
 - [ModifyObjectRule](docs/ModifyObjectRule.md)
 - [MultiLineString](docs/MultiLineString.md)
 - [MultiPoint](docs/MultiPoint.md)
 - [MultiPolygon](docs/MultiPolygon.md)
 - [NullType](docs/NullType.md)
 - [ObjectPropertyType](docs/ObjectPropertyType.md)
 - [ObjectType](docs/ObjectType.md)
 - [ObjectTypeV2](docs/ObjectTypeV2.md)
 - [ObjectTypeVisibility](docs/ObjectTypeVisibility.md)
 - [ObjectTypeWithLink](docs/ObjectTypeWithLink.md)
 - [Ontology](docs/Ontology.md)
 - [OntologyArrayType](docs/OntologyArrayType.md)
 - [OntologyDataType](docs/OntologyDataType.md)
 - [OntologyFullMetadata](docs/OntologyFullMetadata.md)
 - [OntologyMapType](docs/OntologyMapType.md)
 - [OntologyObjectArrayType](docs/OntologyObjectArrayType.md)
 - [OntologyObjectSetType](docs/OntologyObjectSetType.md)
 - [OntologyObjectType](docs/OntologyObjectType.md)
 - [OntologySetType](docs/OntologySetType.md)
 - [OntologyStructField](docs/OntologyStructField.md)
 - [OntologyStructType](docs/OntologyStructType.md)
 - [OntologyV2](docs/OntologyV2.md)
 - [Parameter](docs/Parameter.md)
 - [Polygon](docs/Polygon.md)
 - [PropertyV2](docs/PropertyV2.md)
 - [QueryAggregationKeyType](docs/QueryAggregationKeyType.md)
 - [QueryAggregationRangeSubType](docs/QueryAggregationRangeSubType.md)
 - [QueryAggregationRangeType](docs/QueryAggregationRangeType.md)
 - [QueryAggregationValueType](docs/QueryAggregationValueType.md)
 - [QueryArrayType](docs/QueryArrayType.md)
 - [QueryDataType](docs/QueryDataType.md)
 - [QueryParameterV2](docs/QueryParameterV2.md)
 - [QuerySetType](docs/QuerySetType.md)
 - [QueryStructField](docs/QueryStructField.md)
 - [QueryStructType](docs/QueryStructType.md)
 - [QueryType](docs/QueryType.md)
 - [QueryTypeV2](docs/QueryTypeV2.md)
 - [QueryUnionType](docs/QueryUnionType.md)
 - [ReleaseStatus](docs/ReleaseStatus.md)
 - [ShortType](docs/ShortType.md)
 - [StringType](docs/StringType.md)
 - [TableExportFormat](docs/TableExportFormat.md)
 - [ThreeDimensionalAggregation](docs/ThreeDimensionalAggregation.md)
 - [TimeSeriesItemType](docs/TimeSeriesItemType.md)
 - [TimeseriesType](docs/TimeseriesType.md)
 - [TimestampType](docs/TimestampType.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionStatus](docs/TransactionStatus.md)
 - [TransactionType](docs/TransactionType.md)
 - [TwoDimensionalAggregation](docs/TwoDimensionalAggregation.md)
 - [UnsupportedType](docs/UnsupportedType.md)


## Contributions

This repository does not accept code contributions.

If you have any questions, concerns, or ideas for improvements, create an
issue with Palantir Support.

## License
This project is made available under the [Apache 2.0 License](/LICENSE).
