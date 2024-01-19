# GeometryCollection

GeoJSon geometry collection  GeometryCollections composed of a single part or a number of parts of a single type SHOULD be avoided when that single part or a single object of multipart type (MultiPoint, MultiLineString, or MultiPolygon) could be used instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | **List\[float\]** | A GeoJSON object MAY have a member named \&quot;bbox\&quot; to include information on the coordinate range for its Geometries, Features, or FeatureCollections. The value of the bbox member MUST be an array of length 2\*n where n is the number of dimensions represented in the contained geometries, with all axes of the most southwesterly point followed by all axes of the more northeasterly point. The axes order of a bbox follows the axes order of geometries.  | \[optional\]
**geometries** | [**List\[Geometry\]**](Geometry.md) |  | \[optional\]
**type** | **str** |  |

## Example

```python
from foundry.models import GeometryCollection

# TODO update the JSON string below
json = "{}"
# create an instance of GeometryCollection from a JSON string
geometry_collection_instance = GeometryCollection.from_json(json)
# print the JSON string representation of the object
print(GeometryCollection.to_json())

# convert the object into a dict
geometry_collection_dict = geometry_collection_instance.to_dict()
# create an instance of GeometryCollection from a dict
geometry_collection_form_dict = geometry_collection.from_dict(geometry_collection_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
