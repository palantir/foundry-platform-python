# Action

Method | HTTP request |
------------- | ------------- |
[**apply**](#apply) | **POST** /v1/ontologies/{ontologyRid}/actions/{actionType}/apply |
[**apply_batch**](#apply_batch) | **POST** /v1/ontologies/{ontologyRid}/actions/{actionType}/applyBatch |
[**validate**](#validate) | **POST** /v1/ontologies/{ontologyRid}/actions/{actionType}/validate |

# **apply**
Applies an action using the given parameters. Changes to the Ontology are eventually consistent and may take
some time to be visible.

Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) are not currently supported by
this endpoint.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read api:ontologies-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**action_type** | ActionTypeApiName | actionType |  |
**apply_action_request** | Union[ApplyActionRequest, ApplyActionRequestDict] | Body of the request |  |

### Return type
**ApplyActionResponse**

### Example

```python
from foundry.v1 import FoundryV1Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV1Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"

# ActionTypeApiName | actionType
action_type = "rename-employee"

# Union[ApplyActionRequest, ApplyActionRequestDict] | Body of the request
apply_action_request = {"parameters": {"id": 80060, "newName": "Anna Smith-Doe"}}


try:
    api_response = foundry_client.ontologies.Action.apply(
        ontology_rid,
        action_type,
        apply_action_request,
    )
    print("The apply response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Action.apply: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ApplyActionResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v1-link) [[Back to README]](../../../../README.md)

# **apply_batch**
Applies multiple actions (of the same Action Type) using the given parameters.
Changes to the Ontology are eventually consistent and may take some time to be visible.

Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
call Functions may receive a higher limit.

Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) and
[notifications](/docs/foundry/action-types/notifications/) are not currently supported by this endpoint.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read api:ontologies-write`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**action_type** | ActionTypeApiName | actionType |  |
**batch_apply_action_request** | Union[BatchApplyActionRequest, BatchApplyActionRequestDict] | Body of the request |  |

### Return type
**BatchApplyActionResponse**

### Example

```python
from foundry.v1 import FoundryV1Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV1Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"

# ActionTypeApiName | actionType
action_type = "rename-employee"

# Union[BatchApplyActionRequest, BatchApplyActionRequestDict] | Body of the request
batch_apply_action_request = {
    "requests": [
        {"parameters": {"id": 80060, "newName": "Anna Smith-Doe"}},
        {"parameters": {"id": 80061, "newName": "Joe Bloggs"}},
    ]
}


try:
    api_response = foundry_client.ontologies.Action.apply_batch(
        ontology_rid,
        action_type,
        batch_apply_action_request,
    )
    print("The apply_batch response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Action.apply_batch: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | BatchApplyActionResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v1-link) [[Back to README]](../../../../README.md)

# **validate**
Validates if an action can be run with the given set of parameters.
The response contains the evaluation of parameters and **submission criteria**
that determine if the request is `VALID` or `INVALID`.
For performance reasons, validations will not consider existing objects or other data in Foundry.
For example, the uniqueness of a primary key or the existence of a user ID will not be checked.
Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) are not currently supported by
this endpoint. Unspecified parameters will be given a default value of `null`.

Third-party applications using this endpoint via OAuth2 must request the
following operation scopes: `api:ontologies-read`.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology_rid** | OntologyRid | ontologyRid |  |
**action_type** | ActionTypeApiName | actionType |  |
**validate_action_request** | Union[ValidateActionRequest, ValidateActionRequestDict] | Body of the request |  |

### Return type
**ValidateActionResponse**

### Example

```python
from foundry.v1 import FoundryV1Client
from foundry import PalantirRPCException
from pprint import pprint

foundry_client = FoundryV1Client(
    auth=foundry.UserTokenAuth(...), hostname="example.palantirfoundry.com"
)

# OntologyRid | ontologyRid
ontology_rid = "ri.ontology.main.ontology.c61d9ab5-2919-4127-a0a1-ac64c0ce6367"

# ActionTypeApiName | actionType
action_type = "rename-employee"

# Union[ValidateActionRequest, ValidateActionRequestDict] | Body of the request
validate_action_request = {
    "parameters": {
        "id": "2",
        "firstName": "Chuck",
        "lastName": "Jones",
        "age": 17,
        "date": "2021-05-01",
        "numbers": [1, 2, 3],
        "hasObjectSet": true,
        "objectSet": "ri.object-set.main.object-set.39a9f4bd-f77e-45ce-9772-70f25852f623",
        "reference": "Chuck",
        "percentage": 41.3,
        "differentObjectId": "2",
    }
}


try:
    api_response = foundry_client.ontologies.Action.validate(
        ontology_rid,
        action_type,
        validate_action_request,
    )
    print("The validate response:\n")
    pprint(api_response)
except PalantirRPCException as e:
    print("HTTP error when calling Action.validate: %s\n" % e)

```



### Authorization

See [README](../../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | ValidateActionResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../../README.md#models-v1-link) [[Back to README]](../../../../README.md)

