# S3ConnectionConfiguration

The configuration needed to connect to an [AWS S3 external system (or any other S3-like external systems that
implement the s3a protocol)](/docs/foundry/available-connectors/amazon-s3/#amazon-s3).


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**bucket_url** | pydantic.StrictStr | Yes | The URL of the S3 bucket. The URL should contain a trailing slash. |
**authentication_mode** | Optional[S3AuthenticationMode] | No | The authentication mode to use to connect to the S3 external system. No authentication mode is required to connect to publicly accessible AWS S3 buckets.  |
**type** | Literal["s3"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
