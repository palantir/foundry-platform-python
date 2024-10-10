# SubmissionCriteriaEvaluation

Contains the status of the **submission criteria**.
**Submission criteria** are the prerequisites that need to be satisfied before an Action can be applied.
These are configured in the **Ontology Manager**.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**configured_failure_message** | Optional[pydantic.StrictStr] | No | The message indicating one of the **submission criteria** was not satisfied. This is configured per **submission criteria** in the **Ontology Manager**.  |
**result** | ValidationResult | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
