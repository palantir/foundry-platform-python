# CbacMarkingRestrictions

CbacMarkingRestrictions

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**disallowed_markings** | List[MarkingId] | Yes | Markings that cannot appear in conjunction with the provided markings. This includes all such markings, not just those present in the provided set. |
**implied_markings** | List[MarkingId] | Yes | Markings that are automatically granted when a user has membership in any of the provided markings. |
**required_markings** | List[List[MarkingId]] | Yes | Markings that must appear in conjunction with the provided markings. Each list contains the requirements for one of the provided markings, and at least one marking from each must be included in the provided markingIds to constitute a valid classification. |
**user_satisfies_markings** | CbacMarkingRestrictionsUserSatisfiesMarkings | Yes | True if the current user satisfies the provided markings. The user must be a member of all conjunctive markings. The provided disjunctive markings are grouped by category, and the user must be a member of at least one marking in each group. |
**is_valid** | CbacMarkingRestrictionsIsValid | Yes | True if the provided markings constitute a valid classification, containing no disallowed markings and satisfying all required marking constraints. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
