# BBox

A GeoJSON object MAY have a member named "bbox" to include
information on the coordinate range for its Geometries, Features, or
FeatureCollections. The value of the bbox member MUST be an array of
length 2*n where n is the number of dimensions represented in the
contained geometries, with all axes of the most southwesterly point
followed by all axes of the more northeasterly point. The axes order
of a bbox follows the axes order of geometries.


## Type
```python
List[Coordinate]
```


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to README]](../../../README.md)