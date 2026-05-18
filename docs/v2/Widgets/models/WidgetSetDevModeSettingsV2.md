# WidgetSetDevModeSettingsV2

The settings for a widget set in development mode (v2), keyed by widget ID.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**base_href** | str | Yes | The base path for the HTML file used to render the widget in dev mode.  |
**input_spec** | Optional[WidgetSetInputSpec] | No | The input spec for the widget set in dev mode. |
**widget_settings** | Dict[WidgetId, WidgetDevModeSettingsV2] | Yes | The dev mode settings for each widget in the widget set, keyed by widget IDs.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
