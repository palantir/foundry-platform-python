# CreateConnectionRequestSnowflakeConnectionConfiguration

CreateConnectionRequestSnowflakeConnectionConfiguration

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**schema_** | Optional[str] | No | Specifies the default schema to use for the specified database once connected. If unspecified,  defaults to the empty string. The specified schema should be an existing schema for which the specified default role has privileges.  See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#schema  |
**database** | Optional[str] | No | Specifies the default database to use once connected. If unspecified, defaults to the empty string. The specified database should be an existing database for which the specified default role has privileges.  See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#db  |
**role** | Optional[str] | No | Specifies the default access control role to use in the Snowflake session initiated by the driver.  If unspecified, no role will be used when the session is initiated by the driver.  The specified role should be an existing role that has already been assigned to the specified user for  the driver. If the specified role has not already been assigned to the user, the role is not used when  the session is initiated by the driver.  See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#role  |
**account_identifier** | str | Yes | An [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier) uniquely  identifies a Snowflake account within your organization, as well as throughout the global network of  Snowflake-supported cloud platforms and cloud regions.  The URL for an account uses the following format: <account_identifier>.snowflakecomputing.com. An example URL is https://acme-test_aws_us_east_2.snowflakecomputing.com.  |
**jdbc_properties** | JdbcProperties | Yes |  |
**warehouse** | Optional[str] | No | Specifies the virtual warehouse to use once connected. If unspecified, defaults to the empty string.  The specified warehouse should be an existing warehouse for which the specified default role has privileges.  See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#warehouse  |
**authentication_mode** | CreateConnectionRequestSnowflakeAuthenticationMode | Yes | The authentication mode to use to connect to the Snowflake database.  |
**type** | Literal["snowflake"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
