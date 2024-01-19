# DeploymentNotFound

The requested model deployment is not found, or the client token does not have access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  |
**error_instance_id** | **str** |  | \[optional\]
**error_name** | **str** |  |
**parameters** | [**DeploymentNotAvailableParameters**](DeploymentNotAvailableParameters.md) |  |

## Example

```python
from foundry.models import DeploymentNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentNotFound from a JSON string
deployment_not_found_instance = DeploymentNotFound.from_json(json)
# print the JSON string representation of the object
print(DeploymentNotFound.to_json())

# convert the object into a dict
deployment_not_found_dict = deployment_not_found_instance.to_dict()
# create an instance of DeploymentNotFound from a dict
deployment_not_found_form_dict = deployment_not_found.from_dict(deployment_not_found_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
