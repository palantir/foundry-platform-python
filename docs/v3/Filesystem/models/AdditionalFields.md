# AdditionalFields

Optional properties of a resource. An additional field is returned if and only if it was explicitly
requested by the caller.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**contact_information** | Optional[ContactInformationField] | No | Empty if the `CONTACT_INFORMATION` additional field was not requested. |
**default_branch** | Optional[DefaultBranchField] | No | Empty if the `DEFAULT_BRANCH` additional field was not requested. |
**description** | Optional[DescriptionField] | No | Empty if the `DESCRIPTION` additional field was not requested. |
**documentation** | Optional[DocumentationField] | No | Empty if the `DOCUMENTATION` additional field was not requested. |
**named_ancestors** | Optional[NamedAncestorsField] | No | Empty if the `NAMED_ANCESTORS` additional field was not requested. |
**path** | Optional[PathField] | No | Empty if the `PATH` additional field was not requested. |
**space_rid** | Optional[SpaceRidField] | No | Empty if the `SPACE_RID` additional field was not requested. |
**trash_status** | Optional[TrashStatusField] | No | Empty if the `TRASH_STATUS` additional field was not requested. |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
