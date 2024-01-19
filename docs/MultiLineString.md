# MultiLineString

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | **List\[float\]** | A GeoJSON object MAY have a member named \&quot;bbox\&quot; to include information on the coordinate range for its Geometries, Features, or FeatureCollections. The value of the bbox member MUST be an array of length 2\*n where n is the number of dimensions represented in the contained geometries, with all axes of the most southwesterly point followed by all axes of the more northeasterly point. The axes order of a bbox follows the axes order of geometries.  | \[optional\]
**coordinates** | **List\[List\[List\[float\]\]\]** |  | \[optional\]
**type** | **str** |  |

## Example

```python
from foundry.models import MultiLineString

# TODO update the JSON string below
json = "{}"
# create an instance of MultiLineString from a JSON string
multi_line_string_instance = MultiLineString.from_json(json)
# print the JSON string representation of the object
print(MultiLineString.to_json())

# convert the object into a dict
multi_line_string_dict = multi_line_string_instance.to_dict()
# create an instance of MultiLineString from a dict
multi_line_string_form_dict = multi_line_string.from_dict(multi_line_string_dict)
```

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
