# DecimalType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**precision** | **int** |  | \[optional\]
**scale** | **int** |  | \[optional\]
**type** | **str** |  |

## Example

```python
from foundry.models import DecimalType

# TODO update the JSON string below
json = "{}"
# create an instance of DecimalType from a JSON string
decimal_type_instance = DecimalType.from_json(json)
# print the JSON string representation of the object
print(DecimalType.to_json())

# convert the object into a dict
decimal_type_dict = decimal_type_instance.to_dict()
# create an instance of DecimalType from a dict
decimal_type_form_dict = decimal_type.from_dict(decimal_type_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
