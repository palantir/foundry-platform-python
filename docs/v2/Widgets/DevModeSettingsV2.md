# DevModeSettingsV2

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**enable**](#enable) | **POST** /v2/widgets/devModeSettingsV2/enable | Private Beta |
[**set_widget_set_manifest**](#set_widget_set_manifest) | **POST** /v2/widgets/devModeSettingsV2/setWidgetSetManifest | Private Beta |

# **enable**
Enable dev mode for the user associated with the provided token.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**DevModeSettingsV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.widgets.DevModeSettingsV2.enable(preview=preview)
    print("The enable response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling DevModeSettingsV2.enable: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | DevModeSettingsV2  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **set_widget_set_manifest**
Set the dev mode settings for the given widget set using the manifest format.
The request body is a dev settings manifest JSON object with the following
structure:

  {
    "manifestVersion": "1.0.0",
    "devSettings": {
      "baseHref": "...",
      "widgets": { ... },
      "inputSpec": { ... }
    }
  }

See https://github.com/palantir/osdk-ts for the widget library API types for the
dev settings manifest.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**manifest** | Any |  |  |
**widget_set_rid** | WidgetSetRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**DevModeSettingsV2**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Any
manifest = None
# WidgetSetRid
widget_set_rid = "ri.widgetregistry..widget-set.21dt2c42-b7df-4b23-880b-1436a3dred2e"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.widgets.DevModeSettingsV2.set_widget_set_manifest(
        manifest=manifest, widget_set_rid=widget_set_rid, preview=preview
    )
    print("The set_widget_set_manifest response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling DevModeSettingsV2.set_widget_set_manifest: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | DevModeSettingsV2  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

