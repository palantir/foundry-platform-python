# PropertyFilter

Represents a filter used on properties.

Endpoints that accept this supports optional parameters that have the form:
`properties.{propertyApiName}.{propertyFilter}={propertyValueEscapedString}` to filter the returned objects.
For instance, you may use `properties.firstName.eq=John` to find objects that contain a property called
"firstName" that has the exact value of "John".

The following are a list of supported property filters:

- `properties.{propertyApiName}.contains` - supported on arrays and can be used to filter array properties
  that have at least one of the provided values. If multiple query parameters are provided, then objects
  that have any of the given values for the specified property will be matched.
- `properties.{propertyApiName}.eq` - used to filter objects that have the exact value for the provided
  property. If multiple query parameters are provided, then objects that have any of the given values
  will be matched. For instance, if the user provides a request by doing
  `?properties.firstName.eq=John&properties.firstName.eq=Anna`, then objects that have a firstName property
  of either John or Anna will be matched. This filter is supported on all property types except Arrays.
- `properties.{propertyApiName}.neq` - used to filter objects that do not have the provided property values.
  Similar to the `eq` filter, if multiple values are provided, then objects that have any of the given values
  will be excluded from the result.
- `properties.{propertyApiName}.lt`, `properties.{propertyApiName}.lte`, `properties.{propertyApiName}.gt`
  `properties.{propertyApiName}.gte` - represent less than, less than or equal to, greater than, and greater
  than or equal to respectively. These are supported on date, timestamp, byte, integer, long, double, decimal.
- `properties.{propertyApiName}.isNull` - used to filter objects where the provided property is (or is not) null.
  This filter is supported on all property types.


## Type
```python
StrictStr
```


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)
