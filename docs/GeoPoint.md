# GeoPoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | **List\[float\]** | A GeoJSON object MAY have a member named \&quot;bbox\&quot; to include information on the coordinate range for its Geometries, Features, or FeatureCollections. The value of the bbox member MUST be an array of length 2\*n where n is the number of dimensions represented in the contained geometries, with all axes of the most southwesterly point followed by all axes of the more northeasterly point. The axes order of a bbox follows the axes order of geometries.  | \[optional\]
**coordinates** | **List\[float\]** | GeoJSon fundamental geometry construct.  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.  Implementations SHOULD NOT extend positions beyond three elements because the semantics of extra elements are unspecified and ambiguous. Historically, some implementations have used a fourth element to carry a linear referencing measure (sometimes denoted as \&quot;M\&quot;) or a numerical timestamp, but in most situations a parser will not be able to properly interpret these values. The interpretation and meaning of additional elements is beyond the scope of this specification, and additional elements MAY be ignored by parsers.  |
**type** | **str** |  |

## Example

```python
from foundry.models import GeoPoint

# TODO update the JSON string below
json = "{}"
# create an instance of GeoPoint from a JSON string
geo_point_instance = GeoPoint.from_json(json)
# print the JSON string representation of the object
print(GeoPoint.to_json())

# convert the object into a dict
geo_point_dict = geo_point_instance.to_dict()
# create an instance of GeoPoint from a dict
geo_point_form_dict = geo_point.from_dict(geo_point_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
