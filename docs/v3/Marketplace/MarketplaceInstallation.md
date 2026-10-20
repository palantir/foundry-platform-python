# MarketplaceInstallation

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v3/platform/marketplaceInstallations | Public Beta |
[**get**](#get) | **GET** /v3/platform/marketplaceInstallations/{marketplaceInstallationRid} | Public Beta |

# **create**
Register a product installation in the given project or folder without running an installation job or
installing product resources. Returns the created installation with its current Compass metadata and
no latest target version. A subsequent installation job selects the version to install.

This operation is not idempotent. Repeated requests create separate installations unless the selected
product version's singleton policy prohibits another installation in the destination namespace, in
which case SingletonMarketplaceInstallationAlreadyExists is returned.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marketplace_rid** | MarketplaceRid |  |  |
**parent_folder_rid** | FolderRid | The RID of the Compass project or folder that currently contains the installation. On creation, this is the destination where the installation is registered and its jobs create resources. |  |
**product_id** | ProductId |  |  |
**installation_suffix** | Optional[str] | An optional suffix appended to the product title to form the initial display name, for example "Product title - CI staging". If omitted, the display name uses the product title alone. | [optional] |
**ontology_rid** | Optional[OntologyRid] | The ontology where jobs for this installation create or update ontology resources. Omit if the product does not interact with the ontology. | [optional] |
**preview** | Optional[PreviewMode] |  | [optional] |
**target_version_hint** | Optional[ProductVersionSelector] | If provided:  - validations that are version specific (e.g. singleton validations) are executed assuming     the installation will later have a job run to transition it to this specific target version.  - the installation title is resolved from the product title at that version.  If not provided, the latest released version of the product is used to resolve information for the steps above. | [optional] |

### Return type
**MarketplaceInstallation**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarketplaceRid
marketplace_rid = "ri.marketplace.main.local.e74f7e10-08b7-4ed6-aad8-2ffbe901b115"
# FolderRid | The RID of the Compass project or folder that currently contains the installation. On creation, this is the destination where the installation is registered and its jobs create resources.
parent_folder_rid = "ri.compass.main.folder.0e77e9f7-683b-4e70-90b5-e35609d37864"
# ProductId
product_id = "4d9a2e36-52c7-49be-8d10-1fb0cc7481a2"
# Optional[str] | An optional suffix appended to the product title to form the initial display name, for example "Product title - CI staging". If omitted, the display name uses the product title alone.
installation_suffix = "my suffix"
# Optional[OntologyRid] | The ontology where jobs for this installation create or update ontology resources. Omit if the product does not interact with the ontology.
ontology_rid = "ri.ontology.main.ontology.c1e96527-1a20-4c7b-b17a-b3c7cfc8f024"
# Optional[PreviewMode]
preview = None
# Optional[ProductVersionSelector] | If provided:  - validations that are version specific (e.g. singleton validations) are executed assuming     the installation will later have a job run to transition it to this specific target version.  - the installation title is resolved from the product title at that version.  If not provided, the latest released version of the product is used to resolve information for the steps above.
target_version_hint = {"versionId": "7a6f2c81-38b5-4e6d-a294-3f85d069b7c0", "type": "versionId"}


try:
    api_response = client.marketplace.MarketplaceInstallation.create(
        marketplace_rid=marketplace_rid,
        parent_folder_rid=parent_folder_rid,
        product_id=product_id,
        installation_suffix=installation_suffix,
        ontology_rid=ontology_rid,
        preview=preview,
        target_version_hint=target_version_hint,
    )
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MarketplaceInstallation.create: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:marketplace-installation:write:create]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MarketplaceInstallation  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

# **get**
Get a registered installation and the product version targeted by its latest submitted job.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**marketplace_installation_rid** | MarketplaceInstallationRid |  |  |
**preview** | Optional[PreviewMode] |  | [optional] |

### Return type
**MarketplaceInstallation**

### Example

```python
from foundry_sdk.v3 import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MarketplaceInstallationRid
marketplace_installation_rid = None
# Optional[PreviewMode]
preview = None


try:
    api_response = client.marketplace.MarketplaceInstallation.get(
        marketplace_installation_rid, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling MarketplaceInstallation.get: %s\n" % e)

```



### Authorization

Required scopes: [api:v3:marketplace-installation:read:get]

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | MarketplaceInstallation  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v3-link) [[Back to Model list]](../../../README.md#models-v3-link) [[Back to README]](../../../README.md)

