# DevModeSettings

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**enable**](#enable) | **POST** /v2/widgets/devModeSettings/enable | Private Beta |
[**set_widget_set_by_id**](#set_widget_set_by_id) | **POST** /v2/widgets/devModeSettings/setWidgetSetById | Private Beta |

# **enable**
Enable dev mode for the user associated with the provided token.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**DevModeSettings**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.widgets.DevModeSettings.enable(preview=preview)
    print("The enable response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling DevModeSettings.enable: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | DevModeSettings  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **set_widget_set_by_id**
Set the dev mode settings for the given widget set for the user associated with the
provided token. Uses widget IDs to identify widgets within the set.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**settings** | WidgetSetDevModeSettingsById |  |  |
**widget_set_rid** | WidgetSetRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**DevModeSettings**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# WidgetSetDevModeSettingsById
settings = {
    "widgetSettings": {
        "myCustomWidget": {
            "stylesheetEntrypoints": [{"filePath": "dist/app.js"}],
            "scriptEntrypoints": [{"filePath": "dist/app.js", "scriptType": "DEFAULT"}],
        }
    }
}
# WidgetSetRid
widget_set_rid = "ri.widgetregistry..widget-set.21dt2c42-b7df-4b23-880b-1436a3dred2e"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.widgets.DevModeSettings.set_widget_set_by_id(
        settings=settings, widget_set_rid=widget_set_rid, preview=preview
    )
    print("The set_widget_set_by_id response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling DevModeSettings.set_widget_set_by_id: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | DevModeSettings  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

