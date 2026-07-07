# ObjectTypeUnsupportedDatasource

A datasource of a kind not yet exposed in the public API. The `unsupportedType` discriminator supplies the
underlying OMS variant so callers can recognize known but unmodelled cases (e.g., derived properties). Variants
the adapter does not recognise at all are returned with an `"unknown"` discriminator. The `properties` list
enumerates the property API names this datasource backs. The `properties` will be empty for `"unknown"`
datasources.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**unsupported_type** | str | Yes | A short, stable discriminator naming the underlying OMS variant. E.g., `"derivedProperties"` for derived-properties datasources or `"unknown"` for variants the adapter does not recognize.  |
**properties** | List[PropertyApiName] | Yes | The property API names that this datasource backs. |
**type** | Literal["unsupported"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
