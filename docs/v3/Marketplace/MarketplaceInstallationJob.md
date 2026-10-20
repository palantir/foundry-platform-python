# MarketplaceInstallationJob

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**abort**](#abort) | **POST** /v3/platform/marketplaceInstallationJobs/{marketplaceInstallationJobRid}/abort | Public Beta |
[**create**](#create) | **POST** /v3/platform/marketplaceInstallationJobs | Public Beta |
[**discover_inputs**](#discover_inputs) | **POST** /v3/platform/marketplaceInstallationJobs/discoverInputs | Public Beta |
[**get**](#get) | **GET** /v3/platform/marketplaceInstallationJobs/{marketplaceInstallationJobRid} | Public Beta |

# **abort**
Abort an installation job draft or request cancellation of a submitted installation job. This operation is
idempotent while the job remains available. Poll the job with `get` after aborting: submitted jobs may report
`ABORTING` before reaching `ABORTED`. Aborting a job that has already finished leaves its terminal status
unchanged.

A submitted job may already have created resources. Cancelling it can leave the installation in an
inconsistent state. To recover to a consistent state, attempt a new job to the same target version.

An aborted draft remains queryable only until automatic cleanup.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marketplace_installation_job_rid** | MarketplaceInstallationJobRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarketplaceInstallationJobRid
marketplace_installation_job_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.marketplace.MarketplaceInstallationJob.abort(
        marketplace_installation_job_rid, preview=preview
    )
    print("The abort response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MarketplaceInstallationJob.abort: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:marketplace-installation-job:write:abort]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **create**
Create a job to upgrade existing installations to their target versions.

The operation returns before preparation and validation complete. Poll the job's status to track progress.

Specify 1 to 10 distinct installations, with at most one installation per product. Targets must share a
namespace and marketplace and have at most one resulting ontology after applying overrides.

For each target, `values` and `explicitlyUnset` replace all previously provided values and explicit unsets.

Inputs omitted from both fields may be fulfilled by defaults, automatic mapping, or recommendations. Use
`discoverInputs` to inspect available sources.

This operation is not idempotent. Repeating it may create another draft or return a conflict.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**installations** | List[InstallationJobTarget] | Existing installations to upgrade to their target versions, along with their input mappings. |  |
**recommendations** | List[RecommendationStrategy] | Strategies for selecting other installations whose outputs can fulfill the targets' inputs. Targets in this request may still supply inputs to one another, independent of recommendation strategy. |  |
**preview** | Optional[PreviewMode] |  | [optional] |
**submission_mode** | Optional[InstallationJobSubmissionMode] |  | [optional] |

### Return type
**MarketplaceInstallationJob**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[InstallationJobTarget] | Existing installations to upgrade to their target versions, along with their input mappings.
installations = [
    {
        "installationRid": "ri.marketplace.main.block-set-installation.5b2d8f31-6c42-4a7e-9a13-8e0a3e6d9c52",
        "targetVersion": {"type": "latest"},
        "overrides": {
            "ontology": {
                "ontologyRid": "ri.ontology.main.ontology.c1e96527-1a20-4c7b-b17a-b3c7cfc8f024",
                "type": "set",
            }
        },
        "inputs": {
            "values": {
                "myDataset": {
                    "type": "rid",
                    "rid": "ri.foundry.main.dataset.2f6d7c83-9e41-4b5a-8d20-1c7a34f0e6b9",
                },
                "myDataset.address": {"type": "string", "value": "address"},
            },
            "explicitlyUnset": ["myDataset.postcode"],
        },
    }
]
# List[RecommendationStrategy] | Strategies for selecting other installations whose outputs can fulfill the targets' inputs. Targets in this request may still supply inputs to one another, independent of recommendation strategy.
recommendations = [{"suffixFilter": "shared", "type": "sameNamespace"}]
# Optional[PreviewMode]
preview = None
# Optional[InstallationJobSubmissionMode]
submission_mode = {"type": "draft"}


try:
    api_response = client.marketplace.MarketplaceInstallationJob.create(
        installations=installations,
        recommendations=recommendations,
        preview=preview,
        submission_mode=submission_mode,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MarketplaceInstallationJob.create: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:marketplace-installation-job:write:create]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MarketplaceInstallationJob  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **discover_inputs**
Discover required and optional inputs for existing installations and their proposed target versions.

Resolves input requirements and available sources using the requested target versions, location overrides,
and recommendation strategies.

The request token must have permission to edit each target. Every input in the target product versions must
have an API name.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**installations** | List[InstallationTarget] | Between 1 and 10 distinct installations, with at most one installation per product. Targets must share a namespace and marketplace and have at most one resulting ontology after applying overrides. |  |
**recommendations** | List[RecommendationStrategy] | An empty list disables recommendations from installations outside the requested targets. Targets in this request may still supply inputs to one another. |  |
**preview** | Optional[PreviewMode] |  | [optional] |
**source_filter** | Optional[SourceFilter] | When supplied, excludes an input if any of its available sources appears in `excludedSources`. If omitted, returns only inputs whose sole available source is `MANUAL`. Inputs with no available source are always omitted. | [optional] |

### Return type
**DiscoverInstallationJobInputsResponse**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[InstallationTarget] | Between 1 and 10 distinct installations, with at most one installation per product. Targets must share a namespace and marketplace and have at most one resulting ontology after applying overrides.
installations = [
    {
        "installationRid": "ri.marketplace.main.block-set-installation.5b2d8f31-6c42-4a7e-9a13-8e0a3e6d9c52",
        "targetVersion": {"type": "latest"},
        "overrides": {
            "ontology": {
                "ontologyRid": "ri.ontology.main.ontology.c1e96527-1a20-4c7b-b17a-b3c7cfc8f024",
                "type": "set",
            }
        },
    }
]
# List[RecommendationStrategy] | An empty list disables recommendations from installations outside the requested targets. Targets in this request may still supply inputs to one another.
recommendations = [{"suffixFilter": "shared", "type": "sameNamespace"}]
# Optional[PreviewMode]
preview = None
# Optional[SourceFilter] | When supplied, excludes an input if any of its available sources appears in `excludedSources`. If omitted, returns only inputs whose sole available source is `MANUAL`. Inputs with no available source are always omitted.
source_filter = {"excludedSources": ["AUTO_MAPPED"]}


try:
    api_response = client.marketplace.MarketplaceInstallationJob.discover_inputs(
        installations=installations,
        recommendations=recommendations,
        preview=preview,
        source_filter=source_filter,
    )
    print("The discover_inputs response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MarketplaceInstallationJob.discover_inputs: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:marketplace-installation-job:read:discover-inputs]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | DiscoverInstallationJobInputsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get**
Get the current status of an installation job through draft preparation and execution.

The request token must have permission to view the draft or submitted job. Missing or inaccessible jobs return
`MarketplaceInstallationJobNotFound`. A failed or aborted job still returns HTTP 200 with its current status.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marketplace_installation_job_rid** | MarketplaceInstallationJobRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**MarketplaceInstallationJob**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarketplaceInstallationJobRid
marketplace_installation_job_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.marketplace.MarketplaceInstallationJob.get(
        marketplace_installation_job_rid, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MarketplaceInstallationJob.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:marketplace-installation-job:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MarketplaceInstallationJob  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

