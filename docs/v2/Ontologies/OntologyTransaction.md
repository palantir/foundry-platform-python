# OntologyTransaction

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**post_edits**](#post_edits) | **POST** /v2/ontologies/{ontology}/transactions/{transactionId}/edits | Private Beta |

# **post_edits**
Applies a set of edits to a transaction in order.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**transaction_id** | OntologyTransactionId | The ID of the transaction to apply edits to. Transactions are an experimental feature and all workflows may not be supported.  |  |
**edits** | List[TransactionEdit] |  |  |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |
**sdk_package_rid** | Optional[SdkPackageRid] | The package rid of the generated SDK.  | [optional] |
**sdk_version** | Optional[SdkVersion] | The version of the generated SDK.  | [optional] |

### Return type
**PostTransactionEditsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# OntologyTransactionId | The ID of the transaction to apply edits to. Transactions are an experimental feature and all workflows may not be supported.
transaction_id = None
# List[TransactionEdit]
edits = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None
# Optional[SdkPackageRid] | The package rid of the generated SDK.
sdk_package_rid = None
# Optional[SdkVersion] | The version of the generated SDK.
sdk_version = None


try:
    api_response = client.ontologies.OntologyTransaction.post_edits(
        ontology,
        transaction_id,
        edits=edits,
        preview=preview,
        sdk_package_rid=sdk_package_rid,
        sdk_version=sdk_version,
    )
    print("The post_edits response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OntologyTransaction.post_edits: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | PostTransactionEditsResponse  | Transaction edits were applied successfully. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

