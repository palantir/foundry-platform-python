# DeploymentListing

Name and description associated with a model deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** |  |
**description** | **str** | A description or explanation of what this model deployment does and is intended to be used for.  | \[optional\]

## Example

```python
from foundry.models import DeploymentListing

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentListing from a JSON string
deployment_listing_instance = DeploymentListing.from_json(json)
# print the JSON string representation of the object
print(DeploymentListing.to_json())

# convert the object into a dict
deployment_listing_dict = deployment_listing_instance.to_dict()
# create an instance of DeploymentListing from a dict
deployment_listing_form_dict = deployment_listing.from_dict(deployment_listing_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
