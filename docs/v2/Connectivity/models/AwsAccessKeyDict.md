# AwsAccessKeyDict

[Access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) are long-term 
credentials for an IAM user or the AWS account root user.
Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE) and a secret access 
key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY). You must use both the access key ID and 
secret access key together to authenticate your requests.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**accessKeyId** | str | Yes |  |
**secretAccessKey** | EncryptedPropertyDict | Yes |  |
**type** | typing.Literal["awsAccessKey"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
