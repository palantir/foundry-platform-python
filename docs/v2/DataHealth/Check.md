# Check

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /v2/dataHealth/checks | Public Beta |
[**delete**](#delete) | **DELETE** /v2/dataHealth/checks/{checkRid} | Public Beta |
[**get**](#get) | **GET** /v2/dataHealth/checks/{checkRid} | Public Beta |
[**replace**](#replace) | **PUT** /v2/dataHealth/checks/{checkRid} | Public Beta |

# **create**
Creates a new Check.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**config** | CheckConfig |  |  |
**intent** | Optional[CheckIntent] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Check**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# CheckConfig
config = None
# Optional[CheckIntent]
intent = "Check to ensure builds are passing."
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.data_health.Check.create(config=config, intent=intent, preview=preview)
    print("The create response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Check.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Check  | The created Check | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **delete**
Delete the Check with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**check_rid** | CheckRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**None**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# CheckRid
check_rid = "ri.data-health.main.check.8e27b13a-e21b-4232-ae1b-76ccf5ff42b3"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.data_health.Check.delete(check_rid, preview=preview)
    print("The delete response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Check.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**204** | None  |  | None |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **get**
Get the Check with the specified rid.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**check_rid** | CheckRid |  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Check**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# CheckRid
check_rid = "ri.data-health.main.check.8e27b13a-e21b-4232-ae1b-76ccf5ff42b3"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.data_health.Check.get(check_rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Check.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Check  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **replace**
Replace the Check with the specified rid. Changing the type of a check after it has been created  is not supported.

### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**check_rid** | CheckRid |  |  |
**config** | ReplaceCheckConfig |  |  |
**intent** | Optional[CheckIntent] |  | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**Check**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# CheckRid
check_rid = "ri.data-health.main.check.8e27b13a-e21b-4232-ae1b-76ccf5ff42b3"
# ReplaceCheckConfig
config = None
# Optional[CheckIntent]
intent = "Check to ensure builds are passing."
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.data_health.Check.replace(
        check_rid, config=config, intent=intent, preview=preview
    )
    print("The replace response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling Check.replace: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | Check  | The replaced Check | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

