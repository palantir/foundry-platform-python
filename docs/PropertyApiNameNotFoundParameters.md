# PropertyApiNameNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_base_type** | **str** | A string indicating the type of each data value. Note that these types can be nested, for example an array of structs.  | Type                | JSON value                                                                                                        | |---------------------|-------------------------------------------------------------------------------------------------------------------| | Array               | \`Array\<T>\`, where \`T\` is the type of the array elements, e.g. \`Array\<String>\`.                                    | | Attachment          | \`Attachment\`                                                                                                      | | Boolean             | \`Boolean\`                                                                                                         | | Byte                | \`Byte\`                                                                                                            | | Date                | \`LocalDate\`                                                                                                       | | Decimal             | \`Decimal\`                                                                                                         | | Double              | \`Double\`                                                                                                          | | Float               | \`Float\`                                                                                                           | | Integer             | \`Integer\`                                                                                                         | | Long                | \`Long\`                                                                                                            | | OntologyObject      | \`OntologyObject\<T>\` where \`T\` is the API name of the referenced object type.                                      | | Short               | \`Short\`                                                                                                           | | String              | \`String\`                                                                                                          | | Struct              | \`Struct\<T>\` where \`T\` contains field name and type pairs, e.g. \`Struct\<{ firstName: String, lastName: string }>\`  | | Timeseries          | \`TimeSeries\<T>\` where \`T\` is either \`String\` for an enum series or \`Double\` for a numeric series.                 | | Timestamp           | \`Timestamp\`                                                                                                       |  |
**property_id** | **str** | The immutable ID of a property. Property IDs are only used to identify properties in the **Ontology Manager** application and assign them API names. In every other case, API names should be used instead of property IDs.  |

## Example

```python
from foundry.models import PropertyApiNameNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyApiNameNotFoundParameters from a JSON string
property_api_name_not_found_parameters_instance = PropertyApiNameNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(PropertyApiNameNotFoundParameters.to_json())

# convert the object into a dict
property_api_name_not_found_parameters_dict = property_api_name_not_found_parameters_instance.to_dict()
# create an instance of PropertyApiNameNotFoundParameters from a dict
property_api_name_not_found_parameters_form_dict = property_api_name_not_found_parameters.from_dict(property_api_name_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
