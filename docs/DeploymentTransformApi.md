# DeploymentTransformApi

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**List\[ModelApiDataType\]**](ModelApiDataType.md) |  | \[optional\]
**outputs** | [**List\[ModelApiDataType\]**](ModelApiDataType.md) |  | \[optional\]

## Example

```python
from foundry.models import DeploymentTransformApi

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentTransformApi from a JSON string
deployment_transform_api_instance = DeploymentTransformApi.from_json(json)
# print the JSON string representation of the object
print(DeploymentTransformApi.to_json())

# convert the object into a dict
deployment_transform_api_dict = deployment_transform_api_instance.to_dict()
# create an instance of DeploymentTransformApi from a dict
deployment_transform_api_form_dict = deployment_transform_api.from_dict(deployment_transform_api_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
