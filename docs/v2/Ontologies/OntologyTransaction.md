# OntologyTransaction

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**post_edits**](#post_edits) | **POST** /v2/ontologies/{ontology}/transactions/{transactionRid}/edits | Private Beta |

# **post_edits**
Applies a set of edits to a transaction in order.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**transaction_rid** | OntologyTransactionRid | The RID of the transaction to apply edits to.  |  |
**edits** | List[TransactionEdit] |  |  |

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
# OntologyTransactionRid | The RID of the transaction to apply edits to.
transaction_rid = None
# List[TransactionEdit]
edits = None


try:
    api_response = client.ontologies.OntologyTransaction.post_edits(
        ontology, transaction_rid, edits=edits
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

