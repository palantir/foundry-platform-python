# ApplyActionRequestOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**ApplyActionMode**](ApplyActionMode.md) |  | \[optional\]
**return_edits** | [**ReturnEditsMode**](ReturnEditsMode.md) |  | \[optional\]

## Example

```python
from foundry.models import ApplyActionRequestOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyActionRequestOptions from a JSON string
apply_action_request_options_instance = ApplyActionRequestOptions.from_json(json)
# print the JSON string representation of the object
print(ApplyActionRequestOptions.to_json())

# convert the object into a dict
apply_action_request_options_dict = apply_action_request_options_instance.to_dict()
# create an instance of ApplyActionRequestOptions from a dict
apply_action_request_options_form_dict = apply_action_request_options.from_dict(apply_action_request_options_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
