# LinearRing

A linear ring is a closed LineString with four or more positions.

The first and last positions are equivalent, and they MUST contain
identical values; their representation SHOULD also be identical.

A linear ring is the boundary of a surface or the boundary of a hole in
a surface.

A linear ring MUST follow the right-hand rule with respect to the area
it bounds, i.e., exterior rings are counterclockwise, and holes are
clockwise.


## Type
```python
List[Position]
```


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
