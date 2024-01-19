# CompositePrimaryKeyNotSupported

Primary keys consisting of multiple properties are not supported by this API. If you need support for this, please reach out to Palantir Support.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**CompositePrimaryKeyNotSupportedParameters**](CompositePrimaryKeyNotSupportedParameters.md) |  |

## Example

```python
from foundry.models import CompositePrimaryKeyNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of CompositePrimaryKeyNotSupported from a JSON string
composite_primary_key_not_supported_instance = CompositePrimaryKeyNotSupported.from_json(json)
# print the JSON string representation of the object
print(CompositePrimaryKeyNotSupported.to_json())

# convert the object into a dict
composite_primary_key_not_supported_dict = composite_primary_key_not_supported_instance.to_dict()
# create an instance of CompositePrimaryKeyNotSupported from a dict
composite_primary_key_not_supported_form_dict = composite_primary_key_not_supported.from_dict(composite_primary_key_not_supported_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
