# CbacBanner

CbacBanner

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**classification_string** | CbacBannerClassificationString | Yes | The formatted classification string for the requested markings and display type. |
**markings** | List[MarkingId] | Yes | The marking IDs that the banner represents, with duplicates removed. Marking IDs that the current CBAC configuration does not recognize are omitted. The order is unspecified.  |
**text_color** | Color | Yes | The color to use for the banner text.  |
**background_colors** | List[Color] | Yes | The background colors to use when displaying the banner. The list currently contains a single color, which should be used as a solid background. If more than one color is returned, use the first.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
