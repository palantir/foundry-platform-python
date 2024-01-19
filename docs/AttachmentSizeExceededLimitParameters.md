# AttachmentSizeExceededLimitParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_limit_bytes** | **str** |  |
**file_size_bytes** | **str** |  |

## Example

```python
from foundry.models import AttachmentSizeExceededLimitParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentSizeExceededLimitParameters from a JSON string
attachment_size_exceeded_limit_parameters_instance = AttachmentSizeExceededLimitParameters.from_json(json)
# print the JSON string representation of the object
print(AttachmentSizeExceededLimitParameters.to_json())

# convert the object into a dict
attachment_size_exceeded_limit_parameters_dict = attachment_size_exceeded_limit_parameters_instance.to_dict()
# create an instance of AttachmentSizeExceededLimitParameters from a dict
attachment_size_exceeded_limit_parameters_form_dict = attachment_size_exceeded_limit_parameters.from_dict(attachment_size_exceeded_limit_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
