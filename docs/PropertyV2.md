# PropertyV2

Details about some property of an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | [**ObjectPropertyType**](ObjectPropertyType.md) |  |
**description** | **str** |  | \[optional\]
**display_name** | **str** | The display name of the entity. | \[optional\]

## Example

```python
from foundry.models import PropertyV2

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyV2 from a JSON string
property_v2_instance = PropertyV2.from_json(json)
# print the JSON string representation of the object
print(PropertyV2.to_json())

# convert the object into a dict
property_v2_dict = property_v2_instance.to_dict()
# create an instance of PropertyV2 from a dict
property_v2_form_dict = property_v2.from_dict(property_v2_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
