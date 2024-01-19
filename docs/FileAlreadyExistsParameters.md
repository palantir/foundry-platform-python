# FileAlreadyExistsParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_rid** | **str** | The Resource Identifier (RID) of a Dataset. Example: \`ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da\`.  |
**path** | **str** | The path to a File within Foundry. Examples: \`my-file.txt\`, \`path/to/my-file.jpg\`, \`dataframe.snappy.parquet\`.  |
**transaction_rid** | **str** | The Resource Identifier (RID) of a Transaction. Example: \`ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4\`.  |

## Example

```python
from foundry.models import FileAlreadyExistsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of FileAlreadyExistsParameters from a JSON string
file_already_exists_parameters_instance = FileAlreadyExistsParameters.from_json(json)
# print the JSON string representation of the object
print(FileAlreadyExistsParameters.to_json())

# convert the object into a dict
file_already_exists_parameters_dict = file_already_exists_parameters_instance.to_dict()
# create an instance of FileAlreadyExistsParameters from a dict
file_already_exists_parameters_form_dict = file_already_exists_parameters.from_dict(file_already_exists_parameters_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
