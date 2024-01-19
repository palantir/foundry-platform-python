# AttachmentNotFoundParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_rid** | **str** | The unique resource identifier of an attachment. | \[optional\]

## Example

```python
from foundry.models import AttachmentNotFoundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentNotFoundParameters from a JSON string
attachment_not_found_parameters_instance = AttachmentNotFoundParameters.from_json(json)
# print the JSON string representation of the object
print(AttachmentNotFoundParameters.to_json())

# convert the object into a dict
attachment_not_found_parameters_dict = attachment_not_found_parameters_instance.to_dict()
# create an instance of AttachmentNotFoundParameters from a dict
attachment_not_found_parameters_form_dict = attachment_not_found_parameters.from_dict(attachment_not_found_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
