# DisjunctiveMarkingSummary

The disjunctive set of markings required to access the property value.
Disjunctive markings are represented as a conjunctive list of disjunctive sets.
The top-level set is a conjunction of sets, where each inner set should be 
treated as a unit where any marking within the set can satisfy the set.
All sets within the top level set should be satisfied.


## Type
```python
List[List[MarkingId]]
```


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
