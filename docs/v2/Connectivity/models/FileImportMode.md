# FileImportMode

Import mode governs how raw files are read from an external system, and written into a Foundry dataset. 

SNAPSHOT: Defines a new dataset state consisting only of files from a particular import execution.
APPEND: Purely additive and yields data from previous import executions in addition to newly added files.
UPDATE: Replaces existing files from previous import executions based on file names.


| **Value** |
| --------- |
| `"SNAPSHOT"` |
| `"APPEND"` |
| `"UPDATE"` |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
