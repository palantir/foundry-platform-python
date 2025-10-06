# NumberFormatOptions

Base number formatting options that can be applied to all number formatters.
Controls precision, grouping, rounding, and notation. Consistent with JavaScript's Intl.NumberFormat.

Examples:
- useGrouping: true makes 1234567 display as "1,234,567"
- maximumFractionDigits: 2 makes 3.14159 display as "3.14"
- notation: SCIENTIFIC makes 1234 display as "1.234E3"


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**use_grouping** | Optional[bool] | No | If true, show a locale-appropriate number grouping (e.g. thousands for en). |
**convert_negative_to_parenthesis** | Optional[bool] | No | If true, wrap negative numbers in parentheses instead of a minus sign. |
**minimum_integer_digits** | Optional[int] | No |  |
**minimum_fraction_digits** | Optional[int] | No |  |
**maximum_fraction_digits** | Optional[int] | No |  |
**minimum_significant_digits** | Optional[int] | No |  |
**maximum_significant_digits** | Optional[int] | No |  |
**notation** | Optional[NumberFormatNotation] | No |  |
**rounding_mode** | Optional[NumberRoundingMode] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
