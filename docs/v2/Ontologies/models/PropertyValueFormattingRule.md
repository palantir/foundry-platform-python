# PropertyValueFormattingRule

This feature is experimental and may change in a future release.
Comprehensive formatting configuration for displaying property values in user interfaces. 
Supports different value types including numbers, dates, timestamps, booleans, and known Foundry types.

Each formatter type provides specific options tailored to that data type:
- Numbers: Support for percentages, currencies, units, scaling, and custom formatting
- Dates/Timestamps: Localized and custom formatting patterns
- Booleans: Custom true/false display text
- Known types: Special formatting for Foundry-specific identifiers


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
PropertyDateFormattingRule | date
PropertyNumberFormattingRule | number
PropertyBooleanFormattingRule | boolean
PropertyKnownTypeFormattingRule | knownType
PropertyTimestampFormattingRule | timestamp


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
