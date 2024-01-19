# DeploymentNotAvailable

The requested model deployment does not have a model deployed. It may be disabled or failed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**DeploymentNotAvailableParameters**](DeploymentNotAvailableParameters.md) |  |

## Example

```python
from foundry.models import DeploymentNotAvailable

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentNotAvailable from a JSON string
deployment_not_available_instance = DeploymentNotAvailable.from_json(json)
# print the JSON string representation of the object
print(DeploymentNotAvailable.to_json())

# convert the object into a dict
deployment_not_available_dict = deployment_not_available_instance.to_dict()
# create an instance of DeploymentNotAvailable from a dict
deployment_not_available_form_dict = deployment_not_available.from_dict(deployment_not_available_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
