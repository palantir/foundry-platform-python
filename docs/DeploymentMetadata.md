# DeploymentMetadata

Metadata related to a model deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | [**DeploymentApi**](DeploymentApi.md) |  |
**api_name** | **str** |  |
**description** | **str** | A description or explanation of what this model deployment does and is intended to be used for.  | \[optional\]

## Example

```python
from foundry.models import DeploymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentMetadata from a JSON string
deployment_metadata_instance = DeploymentMetadata.from_json(json)
# print the JSON string representation of the object
print(DeploymentMetadata.to_json())

# convert the object into a dict
deployment_metadata_dict = deployment_metadata_instance.to_dict()
# create an instance of DeploymentMetadata from a dict
deployment_metadata_form_dict = deployment_metadata.from_dict(deployment_metadata_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
