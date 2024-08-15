# DataValue

Represents the value of data in the following format. Note that these values can be nested, for example an array of structs.
| Type                        | JSON encoding                                         | Example                                                                       |
|-----------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------|
| Array                       | array                                                 | `["alpha", "bravo", "charlie"]`                                               |
| Attachment                  | string                                                | `"ri.attachments.main.attachment.2f944bae-5851-4204-8615-920c969a9f2e"`       |
| Boolean                     | boolean                                               | `true`                                                                        |
| Byte                        | number                                                | `31`                                                                          |
| Date                        | ISO 8601 extended local date string                   | `"2021-05-01"`                                                                |
| Decimal                     | string                                                | `"2.718281828"`                                                               |
| Float                       | number                                                | `3.14159265`                                                                  |
| Double                      | number                                                | `3.14159265`                                                                  |
| Integer                     | number                                                | `238940`                                                                      |
| Long                        | string                                                | `"58319870951433"`                                                            |
| Marking                     | string                                                | `"MU"`                                                                        |
| Null                        | null                                                  | `null`                                                                        |
| Object Set                  | string OR the object set definition                   | `ri.object-set.main.versioned-object-set.h13274m8-23f5-431c-8aee-a4554157c57z`|
| Ontology Object Reference   | JSON encoding of the object's primary key             | `10033123` or `"EMP1234"`                                                     |
| Set                         | array                                                 | `["alpha", "bravo", "charlie"]`                                               |
| Short                       | number                                                | `8739`                                                                        |
| String                      | string                                                | `"Call me Ishmael"`                                                           |
| Struct                      | JSON object                                           | `{"name": "John Doe", "age": 42}`                                             |
| TwoDimensionalAggregation   | JSON object                                           | `{"groups": [{"key": "alpha", "value": 100}, {"key": "beta", "value": 101}]}` |
| ThreeDimensionalAggregation | JSON object                                           | `{"groups": [{"key": "NYC", "groups": [{"key": "Engineer", "value" : 100}]}]}`|
| Timestamp                   | ISO 8601 extended offset date-time string in UTC zone | `"2021-01-04T05:00:00Z"`                                                      |


## Type
```python
Any
```


[[Back to Model list]](../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
