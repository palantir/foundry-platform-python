# InvalidAggregationRangePropertyTypeParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the \`List object types\` endpoint or check the **Ontology Manager**.  |
**var_property** | **str** | The name of the property in the API. To find the API name for your property, use the \`Get object type\` endpoint or check the **Ontology Manager**.  |
**property_base_type** | **str** | A string indicating the type of each data value. Note that these types can be nested, for example an array of structs.  | Type                | JSON value                                                                                                        | |---------------------|-------------------------------------------------------------------------------------------------------------------| | Array               | \`Array\<T>\`, where \`T\` is the type of the array elements, e.g. \`Array\<String>\`.                                    | | Attachment          | \`Attachment\`                                                                                                      | | Boolean             | \`Boolean\`                                                                                                         | | Byte                | \`Byte\`                                                                                                            | | Date                | \`LocalDate\`                                                                                                       | | Decimal             | \`Decimal\`                                                                                                         | | Double              | \`Double\`                                                                                                          | | Float               | \`Float\`                                                                                                           | | Integer             | \`Integer\`                                                                                                         | | Long                | \`Long\`                                                                                                            | | OntologyObject      | \`OntologyObject\<T>\` where \`T\` is the API name of the referenced object type.                                      | | Short               | \`Short\`                                                                                                           | | String              | \`String\`                                                                                                          | | Struct              | \`Struct\<T>\` where \`T\` contains field name and type pairs, e.g. \`Struct\<{ firstName: String, lastName: string }>\`  | | Timeseries          | \`TimeSeries\<T>\` where \`T\` is either \`String\` for an enum series or \`Double\` for a numeric series.                 | | Timestamp           | \`Timestamp\`                                                                                                       |  |

## Example

```python
from foundry.models import InvalidAggregationRangePropertyTypeParameters

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidAggregationRangePropertyTypeParameters from a JSON string
invalid_aggregation_range_property_type_parameters_instance = InvalidAggregationRangePropertyTypeParameters.from_json(json)
# print the JSON string representation of the object
print(InvalidAggregationRangePropertyTypeParameters.to_json())

# convert the object into a dict
invalid_aggregation_range_property_type_parameters_dict = invalid_aggregation_range_property_type_parameters_instance.to_dict()
# create an instance of InvalidAggregationRangePropertyTypeParameters from a dict
invalid_aggregation_range_property_type_parameters_form_dict = invalid_aggregation_range_property_type_parameters.from_dict(invalid_aggregation_range_property_type_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
