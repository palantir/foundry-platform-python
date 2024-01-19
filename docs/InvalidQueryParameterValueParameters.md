# InvalidQueryParameterValueParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_data_type** | [**QueryDataType**](QueryDataType.md) |  |
**parameter_id** | **str** | The unique identifier of the parameter. Parameters are used as inputs when an action or query is applied. Parameters can be viewed and managed in the **Ontology Manager**.  |
**parameter_value** | **object** | Represents the value of data in the following format. Note that these values can be nested, for example an array of structs. | Type                        | JSON encoding                                         | Example                                                                       | |-----------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------| | Array                       | array                                                 | \`\[\&quot;alpha\&quot;, \&quot;bravo\&quot;, \&quot;charlie\&quot;\]\`                                               | | Attachment                  | string                                                | \`\&quot;ri.attachments.main.attachment.2f944bae-5851-4204-8615-920c969a9f2e\&quot;\`       | | Boolean                     | boolean                                               | \`true\`                                                                        | | Byte                        | number                                                | \`31\`                                                                          | | Date                        | ISO 8601 extended local date string                   | \`\&quot;2021-05-01\&quot;\`                                                                | | Decimal                     | string                                                | \`\&quot;2.718281828\&quot;\`                                                               | | Float                       | number                                                | \`3.14159265\`                                                                  | | Double                      | number                                                | \`3.14159265\`                                                                  | | Integer                     | number                                                | \`238940\`                                                                      | | Long                        | string                                                | \`\&quot;58319870951433\&quot;\`                                                            | | Null                        | null                                                  | \`null\`                                                                        | | Object Set                  | string                                                | \`ri.object-set.main.versioned-object-set.h13274m8-23f5-431c-8aee-a4554157c57z\`| | Ontology Object Reference   | JSON encoding of the object's primary key             | \`10033123\` or \`\&quot;EMP1234\&quot;\`                                                     | | Set                         | array                                                 | \`\[\&quot;alpha\&quot;, \&quot;bravo\&quot;, \&quot;charlie\&quot;\]\`                                               | | Short                       | number                                                | \`8739\`                                                                        | | String                      | string                                                | \`\&quot;Call me Ishmael\&quot;\`                                                           | | Struct                      | JSON object                                           | \`{\&quot;name\&quot;: \&quot;John Doe\&quot;, \&quot;age\&quot;: 42}\`                                             | | TwoDimensionalAggregation   | JSON object                                           | \`{\&quot;groups\&quot;: \[{\&quot;key\&quot;: \&quot;alpha\&quot;, \&quot;value\&quot;: 100}, {\&quot;key\&quot;: \&quot;beta\&quot;, \&quot;value\&quot;: 101}\]}\` | | ThreeDimensionalAggregation | JSON object                                           | \`{\&quot;groups\&quot;: \[{\&quot;key\&quot;: \&quot;NYC\&quot;, \&quot;groups\&quot;: \[{\&quot;key\&quot;: \&quot;Engineer\&quot;, \&quot;value\&quot; : 100}\]}\]}\`| | Timestamp                   | ISO 8601 extended offset date-time string in UTC zone | \`\&quot;2021-01-04T05:00:00Z\&quot;\`                                                      |  | \[optional\]

## Example

```python
from foundry.models import InvalidQueryParameterValueParameters

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidQueryParameterValueParameters from a JSON string
invalid_query_parameter_value_parameters_instance = InvalidQueryParameterValueParameters.from_json(json)
# print the JSON string representation of the object
print(InvalidQueryParameterValueParameters.to_json())

# convert the object into a dict
invalid_query_parameter_value_parameters_dict = invalid_query_parameter_value_parameters_instance.to_dict()
# create an instance of InvalidQueryParameterValueParameters from a dict
invalid_query_parameter_value_parameters_form_dict = invalid_query_parameter_value_parameters.from_dict(invalid_query_parameter_value_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
