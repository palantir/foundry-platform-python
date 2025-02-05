# S3ConnectionConfiguration

The configuration needed to connect to an [AWS S3 external system (or any other S3-like external systems that
implement the s3a protocol)](/docs/foundry/available-connectors/amazon-s3/#amazon-s3).


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**bucket_url** | str | Yes | The URL of the S3 bucket. The URL should contain a trailing slash. |
**s3_endpoint** | Optional[str] | No | The endpoint of the S3 service. This is used to connect to a custom S3 service that is not AWS S3. If not specified, defaults to the [AWS S3 endpoint](https://docs.aws.amazon.com/general/latest/gr/s3.html). Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.  |
**region** | Optional[Region] | No | The region representing the location of the S3 bucket. Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.  |
**authentication_mode** | Optional[S3AuthenticationMode] | No | The authentication mode to use to connect to the S3 external system. No authentication mode is required to connect to publicly accessible AWS S3 buckets.  |
**s3_endpoint_signing_region** | Optional[Region] | No | The region used when constructing the S3 client using a custom endpoint. This is often not required and would only be needed if you are using the S3 connector with an S3-compliant third-party API, and are also setting a custom endpoint that requires a non-default region.  |
**client_kms_configuration** | Optional[S3KmsConfiguration] | No | The client-side KMS key to use for encryption and decryption of data in the S3 bucket. If not specified, the default KMS key for the bucket is used.  |
**sts_role_configuration** | Optional[StsRoleConfiguration] | No | The configuration needed to assume a role to connect to the S3 external system. |
**proxy_configuration** | Optional[S3ProxyConfiguration] | No | The configuration needed to connect to the S3 external system through a proxy. |
**max_connections** | Optional[int] | No | The maximum number of HTTP connections to the S3 service per sync. If not specified, defaults to 50 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_MAX_CONNECTIONS).  |
**connection_timeout_millis** | Optional[Long] | No | The amount of time (in milliseconds) to wait when initially establishing a connection before giving up and timing out. If not specified, defaults to 10000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_CONNECTION_TIMEOUT).  |
**socket_timeout_millis** | Optional[Long] | No | The amount of time (in milliseconds) to wait for data to be transferred over an established, open connection. If not specified, defaults to 50000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_SOCKET_TIMEOUT).  |
**max_error_retry** | Optional[int] | No | The maximum number of retry attempts for failed requests to the S3 service. If not specified, defaults to 3 as defined by the [AWS SDK default](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/retry-strategy.html#retry-strategies).  |
**match_subfolder_exactly** | Optional[bool] | No | If true, only files in the subfolder specified in the bucket URL will be synced. If false, all files in the bucket will be synced. If not specified, defaults to false.  |
**enable_requester_pays** | Optional[bool] | No | Defaults to false, unless set and overwritten. If true, includes the [requester pays header](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in requests, allowing reads from requester pays buckets.  |
**type** | Literal["s3"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
