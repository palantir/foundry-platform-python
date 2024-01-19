# ListDeploymentsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployments** | [**List\[DeploymentListing\]**](DeploymentListing.md) |  | \[optional\]

## Example

```python
from foundry.models import ListDeploymentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDeploymentsResponse from a JSON string
list_deployments_response_instance = ListDeploymentsResponse.from_json(json)
# print the JSON string representation of the object
print(ListDeploymentsResponse.to_json())

# convert the object into a dict
list_deployments_response_dict = list_deployments_response_instance.to_dict()
# create an instance of ListDeploymentsResponse from a dict
list_deployments_response_form_dict = list_deployments_response.from_dict(list_deployments_response_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
