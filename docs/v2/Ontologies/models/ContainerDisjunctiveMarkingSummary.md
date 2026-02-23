# ContainerDisjunctiveMarkingSummary

The disjunctive set of markings for the container of this property value,
such as the project of a dataset. These markings may differ from the marking
on the actual property value, but still must be satisfied for accessing the property        
All markings from a conjunctive set must be met for access.

Disjunctive markings are represented as a conjunctive list of disjunctive sets.
The top-level set is a conjunction of sets, where each inner set should be 
treated as a unit where any marking within the set can satisfy the set.
All sets within the top level set should be satisfied.


## Type
```python
List[List[MarkingId]]
```


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
