# DeploymentNotAvailableParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_api_name** | **str** |  | \[optional\]
**ontology_api_name** | **str** |  | \[optional\]

## Example

```python
from foundry.models import DeploymentNotAvailableParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentNotAvailableParameters from a JSON string
deployment_not_available_parameters_instance = DeploymentNotAvailableParameters.from_json(json)
# print the JSON string representation of the object
print(DeploymentNotAvailableParameters.to_json())

# convert the object into a dict
deployment_not_available_parameters_dict = deployment_not_available_parameters_instance.to_dict()
# create an instance of DeploymentNotAvailableParameters from a dict
deployment_not_available_parameters_form_dict = deployment_not_available_parameters.from_dict(deployment_not_available_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
