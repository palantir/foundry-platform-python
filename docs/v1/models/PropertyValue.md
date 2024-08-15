# PropertyValue

Represents the value of a property in the following format.

| Type       | JSON encoding                                         | Example                                                                                            |
|----------- |-------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Array      | array                                                 | `["alpha", "bravo", "charlie"]`                                                                    |
| Attachment | JSON encoded `AttachmentProperty` object              | `{"rid":"ri.blobster.main.attachment.2f944bae-5851-4204-8615-920c969a9f2e"}`                       |
| Boolean    | boolean                                               | `true`                                                                                             |
| Byte       | number                                                | `31`                                                                                               |
| Date       | ISO 8601 extended local date string                   | `"2021-05-01"`                                                                                     |
| Decimal    | string                                                | `"2.718281828"`                                                                                    |
| Double     | number                                                | `3.14159265`                                                                                       |
| Float      | number                                                | `3.14159265`                                                                                       |
| GeoPoint   | geojson                                               | `{"type":"Point","coordinates":[102.0,0.5]}`                                                       |
| GeoShape   | geojson                                               | `{"type":"LineString","coordinates":[[102.0,0.0],[103.0,1.0],[104.0,0.0],[105.0,1.0]]}`            |
| Integer    | number                                                | `238940`                                                                                           |
| Long       | string                                                | `"58319870951433"`                                                                                 |
| Short      | number                                                | `8739`                                                                                             |
| String     | string                                                | `"Call me Ishmael"`                                                                                |
| Timestamp  | ISO 8601 extended offset date-time string in UTC zone | `"2021-01-04T05:00:00Z"`                                                                           |

Note that for backwards compatibility, the Boolean, Byte, Double, Float, Integer, and Short types can also be encoded as JSON strings.


## Type
```python
Any
```


[[Back to Model list]](../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
