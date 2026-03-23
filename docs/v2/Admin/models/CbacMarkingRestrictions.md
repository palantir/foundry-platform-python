# CbacMarkingRestrictions

CbacMarkingRestrictions

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**disallowed_markings** | List[MarkingId] | Yes | The union of all markings that are disallowed for each of the provided markings. This includes all disallowed markings, not just those present in the provided set. |
**implied_markings** | List[MarkingId] | Yes | The union of all markings implied by each of the provided markings. If marking A implies marking B, then membership in A grants membership in B. |
**required_markings** | List[List[MarkingId]] | Yes | The required markings for the provided markings. At least one marking from each inner list must be added to the provided markingIds to form a valid classification. |
**user_satisfies_markings** | CbacMarkingRestrictionsUserSatisfiesMarkings | Yes | True if the current user satisfies the provided markings. The user must be a member of all conjunctive markings. The provided disjunctive markings are grouped by category, and the user must be a member of at least one marking in each group. |
**is_valid** | CbacMarkingRestrictionsIsValid | Yes | True if the provided markings contain no disallowed markings and each list of required markings is satisfied by the provided markings. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
