# ViewPrimaryKey

The primary key of the dataset. Primary keys are treated as guarantees provided by the creator of the
dataset.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**columns** | List[str] | Yes | The columns that constitute the primary key. These columns must satisfy the following constraints: - The list of columns must be non-empty. - The list must not contain duplicate columns after applying column normalization. - Each referenced column must exist in the schema. - The type of each referenced column must be one of the following: `BYTE`, `SHORT`, `DECIMAL`, `INTEGER`,   `LONG`, `STRING`, `BOOLEAN`, `TIMESTAMP` or `DATE`.  |
**resolution** | ViewPrimaryKeyResolution | Yes | The semantics of the primary key within the dataset. For example, the unique resolution means that every row in the dataset has a distinct primary key. The value of this field represents a contract for writers of the dataset. Writers are responsible for maintaining any related invariants, and readers may make optimizations based on this. Violating the assumptions of the resolution can cause undefined behavior, for example, having duplicate primary keys with the unique resolution.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
