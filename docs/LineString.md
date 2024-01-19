# LineString

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | **List\[float\]** | A GeoJSON object MAY have a member named \&quot;bbox\&quot; to include information on the coordinate range for its Geometries, Features, or FeatureCollections. The value of the bbox member MUST be an array of length 2\*n where n is the number of dimensions represented in the contained geometries, with all axes of the most southwesterly point followed by all axes of the more northeasterly point. The axes order of a bbox follows the axes order of geometries.  | \[optional\]
**coordinates** | **List\[List\[float\]\]** | GeoJSon fundamental geometry construct, array of two or more positions.  | \[optional\]
**type** | **str** |  |

## Example

```python
from foundry.models import LineString

# TODO update the JSON string below
json = "{}"
# create an instance of LineString from a JSON string
line_string_instance = LineString.from_json(json)
# print the JSON string representation of the object
print(LineString.to_json())

# convert the object into a dict
line_string_dict = line_string_instance.to_dict()
# create an instance of LineString from a dict
line_string_form_dict = line_string.from_dict(line_string_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
