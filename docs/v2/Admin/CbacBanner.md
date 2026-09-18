# CbacBanner

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get**](#get) | **GET** /v2/admin/cbacBanner | Public Beta |
[**get_for_resources**](#get_for_resources) | **POST** /v2/admin/cbacBanner/getForResources | Private Beta |

# **get**
Returns a classification banner string and colors for the given set of marking IDs.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**display_type** | Optional[ClassificationBannerDisplayType] | The display type of the banner. Defaults to PORTION_MARKING. BANNER_LINE is the long classification string used in the header of a document; PORTION_MARKING is a short classification string used for individual paragraphs | [optional] |
**marking_ids** | Optional[List[MarkingId]] | The marking IDs for which to generate a banner. Duplicate entries are ignored. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**CbacBanner**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Optional[ClassificationBannerDisplayType] | The display type of the banner. Defaults to PORTION_MARKING. BANNER_LINE is the long classification string used in the header of a document; PORTION_MARKING is a short classification string used for individual paragraphs
display_type = "PORTION_MARKING"
# Optional[List[MarkingId]] | The marking IDs for which to generate a banner. Duplicate entries are ignored.
marking_ids = ["MTS", "MNF"]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.CbacBanner.get(
        display_type=display_type, marking_ids=marking_ids, preview=preview
    )
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling CbacBanner.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CbacBanner  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get_for_resources**
Returns a combined CBAC banner for the requested resources.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**resource_rids** | List[RID] | Resource RIDs to include. The caller must have access to every resource. |  |
**display_type** | Optional[ClassificationBannerDisplayType] | The display type of the banner. Defaults to PORTION_MARKING. BANNER_LINE is the long classification string used in the header of a document; PORTION_MARKING is a short classification string used for individual paragraphs | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**CbacBanner**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[RID] | Resource RIDs to include. The caller must have access to every resource.
resource_rids = [
    "ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da",
    "ri.compass.main.folder.c410f510-2937-420e-8ea3-8c9bcb3c1791",
]
# Optional[ClassificationBannerDisplayType] | The display type of the banner. Defaults to PORTION_MARKING. BANNER_LINE is the long classification string used in the header of a document; PORTION_MARKING is a short classification string used for individual paragraphs
display_type = "BANNER_LINE"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.admin.CbacBanner.get_for_resources(
        resource_rids=resource_rids, display_type=display_type, preview=preview
    )
    print("The get_for_resources response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling CbacBanner.get_for_resources: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CbacBanner  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

