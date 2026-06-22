# ExperimentSeries

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**json**](#json) | **GET** /v2/models/{modelRid}/experiments/{experimentRid}/series/{experimentSeriesName}/json | Public Beta |
[**parquet**](#parquet) | **GET** /v2/models/{modelRid}/experiments/{experimentRid}/series/{experimentSeriesName}/parquet | Public Beta |

# **json**
Retrieve raw time-series data for a single series in JSON format.
Results are paginated with a default page size of 200 and a maximum of 1000.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**experiment_rid** | ExperimentRid |  |  |
**experiment_series_name** | SeriesName |  |  |
**offset** | Optional[int] | Number of values to skip from the beginning. Defaults to 0. | [optional] |
**page_size** | Optional[PageSize] | Maximum number of values to return per page. Default is 200, maximum is 1000. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Series**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelRid
model_rid = None
# ExperimentRid
experiment_rid = None
# SeriesName
experiment_series_name = None
# Optional[int] | Number of values to skip from the beginning. Defaults to 0.
offset = None
# Optional[PageSize] | Maximum number of values to return per page. Default is 200, maximum is 1000.
page_size = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.Model.Experiment.Series.json(
        model_rid,
        experiment_rid,
        experiment_series_name,
        offset=offset,
        page_size=page_size,
        preview=preview,
    )
    print("The json response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Series.json: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Series  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **parquet**
Retrieve raw time-series data for a single series as a streamed binary response in Apache Parquet format.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**model_rid** | ModelRid |  |  |
**experiment_rid** | ExperimentRid |  |  |
**experiment_series_name** | SeriesName |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**bytes**

> [!TIP]
> This operation returns tabular data that can be converted to data frame formats:
>
> ```python
> # Get data in Arrow format
> table_data = client.models.Model.Experiment.Series.parquet(model_rid, experiment_rid, experiment_series_name, preview=preview)
>
> # Convert to a PyArrow Table
> arrow_table = table_data.to_pyarrow()
>
> # Convert to a Pandas DataFrame
> pandas_df = table_data.to_pandas()
>
> # Convert to a Polars DataFrame
> polars_df = table_data.to_polars()
>
> # Convert to a DuckDB relation
> duckdb_relation = table_data.to_duckdb()
> ```
>
> For more details, see the [Data Frames section](../../../README.md#data-frames) in the README.

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ModelRid
model_rid = None
# ExperimentRid
experiment_rid = None
# SeriesName
experiment_series_name = None
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.models.Model.Experiment.Series.parquet(
        model_rid, experiment_rid, experiment_series_name, preview=preview
    )
    print("The parquet response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Series.parquet: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  |  | application/octet-stream |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

