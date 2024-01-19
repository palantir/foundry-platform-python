# ParameterTypeNotSupportedParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_base_type** | **str** | A string indicating the type of each data value. Note that these types can be nested, for example an array of structs.  | Type                | JSON value                                                                                                        | |---------------------|-------------------------------------------------------------------------------------------------------------------| | Array               | \`Array\<T>\`, where \`T\` is the type of the array elements, e.g. \`Array\<String>\`.                                    | | Attachment          | \`Attachment\`                                                                                                      | | Boolean             | \`Boolean\`                                                                                                         | | Byte                | \`Byte\`                                                                                                            | | Date                | \`LocalDate\`                                                                                                       | | Decimal             | \`Decimal\`                                                                                                         | | Double              | \`Double\`                                                                                                          | | Float               | \`Float\`                                                                                                           | | Integer             | \`Integer\`                                                                                                         | | Long                | \`Long\`                                                                                                            | | OntologyObject      | \`OntologyObject\<T>\` where \`T\` is the API name of the referenced object type.                                      | | Short               | \`Short\`                                                                                                           | | String              | \`String\`                                                                                                          | | Struct              | \`Struct\<T>\` where \`T\` contains field name and type pairs, e.g. \`Struct\<{ firstName: String, lastName: string }>\`  | | Timeseries          | \`TimeSeries\<T>\` where \`T\` is either \`String\` for an enum series or \`Double\` for a numeric series.                 | | Timestamp           | \`Timestamp\`                                                                                                       |  |
**parameter_id** | **str** | The unique identifier of the parameter. Parameters are used as inputs when an action or query is applied. Parameters can be viewed and managed in the **Ontology Manager**.  |

## Example

```python
from foundry.models import ParameterTypeNotSupportedParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterTypeNotSupportedParameters from a JSON string
parameter_type_not_supported_parameters_instance = ParameterTypeNotSupportedParameters.from_json(json)
# print the JSON string representation of the object
print(ParameterTypeNotSupportedParameters.to_json())

# convert the object into a dict
parameter_type_not_supported_parameters_dict = parameter_type_not_supported_parameters_instance.to_dict()
# create an instance of ParameterTypeNotSupportedParameters from a dict
parameter_type_not_supported_parameters_form_dict = parameter_type_not_supported_parameters.from_dict(parameter_type_not_supported_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
