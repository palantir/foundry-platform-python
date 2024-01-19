# DeploymentApi

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transform** | [**DeploymentTransformApi**](DeploymentTransformApi.md) |  | \[optional\]

## Example

```python
from foundry.models import DeploymentApi

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentApi from a JSON string
deployment_api_instance = DeploymentApi.from_json(json)
# print the JSON string representation of the object
print(DeploymentApi.to_json())

# convert the object into a dict
deployment_api_dict = deployment_api_instance.to_dict()
# create an instance of DeploymentApi from a dict
deployment_api_form_dict = deployment_api.from_dict(deployment_api_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
