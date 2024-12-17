# CreateConnectionRequestS3ConnectionConfigurationDict

CreateConnectionRequestS3ConnectionConfiguration

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**bucketUrl** | str | Yes | The URL of the S3 bucket. The URL should contain a trailing slash. |
**authenticationMode** | NotRequired[S3AuthenticationModeDict] | No | The authentication mode to use to connect to the S3 external system. No authentication mode is required to connect to publicly accessible AWS S3 buckets.  |
**type** | Literal["s3"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
