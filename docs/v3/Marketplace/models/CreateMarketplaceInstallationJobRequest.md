# CreateMarketplaceInstallationJobRequest

CreateMarketplaceInstallationJobRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**installations** | List[InstallationJobTarget] | Yes | Existing installations to upgrade to their target versions, along with their input mappings. |
**recommendations** | List[RecommendationStrategy] | Yes | Strategies for selecting other installations whose outputs can fulfill the targets' inputs. Targets in this request may still supply inputs to one another, independent of recommendation strategy. |
**submission_mode** | Optional[InstallationJobSubmissionMode] | No |  |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
