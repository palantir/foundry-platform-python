# Experiment

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/models/{modelRid}/experiments/{experimentRid} | Private Beta |
[**search**](#search) | **POST** /v2/models/{modelRid}/experiments/search | Private Beta |

# **get**
Retrieve a single experiment with all metadata, parameters, series metadata, and summary metrics.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**experiment_rid** | ExperimentRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Experiment**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelRid
model_rid = None
# ExperimentRid
experiment_rid = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.Model.Experiment.get(model_rid, experiment_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Experiment.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Experiment  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **search**
Search experiments using complex nested queries on experiment metadata, parameters, series,
and summary metrics. Supports AND/OR/NOT combinations and various predicates.
Returns a maximum of 100 results per page.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**order_by** | Optional[SearchExperimentsOrderBy] | The field to sort by. Default is to sort by relevance. | [optional] |
**page_size** | Optional[PageSize] | The maximum number of results to return. Default 50, maximum of 100. | [optional] |
**page_token** | Optional[PageToken] | PageToken to identify the next page to retrieve. Leave empty for the first request. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**where** | Optional[SearchExperimentsFilter] | Optional search filter for filtering experiments. If not provided, all experiments for the model are returned. | [optional] |

### Return type
**SearchExperimentsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelRid
model_rid = None
# Optional[SearchExperimentsOrderBy] | The field to sort by. Default is to sort by relevance.
order_by = {"field": "EXPERIMENT_NAME", "direction": "ASC"}
# Optional[PageSize] | The maximum number of results to return. Default 50, maximum of 100.
page_size = 100
# Optional[PageToken] | PageToken to identify the next page to retrieve. Leave empty for the first request.
page_token = "v1.QnVpbGQgdGhlIEZ1dHVyZTogaHR0cHM6Ly93d3cucGFsYW50aXIuY29tL2NhcmVlcnMvP2xldmVyLXNvdXJjZSU1YiU1ZD1BUElEb2NzI29wZW4tcG9zaXRpb25z"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[SearchExperimentsFilter] | Optional search filter for filtering experiments. If not provided, all experiments for the model are returned.
where = None


try:
    api_response = client.models.Model.Experiment.search(
        model_rid,
        order_by=order_by,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
        where=where,
    )
    print("The search response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Experiment.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchExperimentsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

