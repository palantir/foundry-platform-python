# CipherTextProperty

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**decrypt**](#decrypt) | **GET** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/decrypt | Stable |
[**encrypt**](#encrypt) | **POST** /v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/encrypt | Private Beta |
[**encrypt_with_default_channel**](#encrypt_with_default_channel) | **POST** /v2/ontologies/{ontology}/objectTypes/{objectType}/ciphertexts/{property}/encrypt | Private Beta |

# **decrypt**
Decrypt the value of a ciphertext property.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object with the CipherText property.  |  |
**property** | PropertyApiName | The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to read from. If not specified, the default branch will be used.  | [optional] |

### Return type
**DecryptionResult**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the object with the CipherText property.
primary_key = 50030
# PropertyApiName | The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.
property = "performance"
# Optional[FoundryBranch] | The Foundry branch to read from. If not specified, the default branch will be used.
branch = None


try:
    api_response = client.ontologies.CipherTextProperty.decrypt(
        ontology, object_type, primary_key, property, branch=branch
    )
    print("The decrypt response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling CipherTextProperty.decrypt: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | DecryptionResult  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **encrypt**
Encrypt a plaintext value into a CipherText value for the given object's CipherText property.

The Cipher Channel used is resolved based on the supplied `cipherChannelStrategy`, using the channel of the
object's existing ciphertext value and/or the default channel configured for the property in ontology metadata.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**primary_key** | PropertyValueEscapedString | The primary key of the object with the CipherText property.  |  |
**property** | PropertyApiName | The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**plaintext** | Plaintext |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to read from. If not specified, the default branch will be used.  | [optional] |
**cipher_channel_strategy** | Optional[CipherChannelStrategy] | The strategy controlling which Cipher Channel is used to encrypt the value. If not specified, defaults to `PREFER_EXISTING`.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**EncryptionResult**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyValueEscapedString | The primary key of the object with the CipherText property.
primary_key = 50030
# PropertyApiName | The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.
property = "performance"
# Plaintext
plaintext = "Jane Doe"
# Optional[FoundryBranch] | The Foundry branch to read from. If not specified, the default branch will be used.
branch = None
# Optional[CipherChannelStrategy] | The strategy controlling which Cipher Channel is used to encrypt the value. If not specified, defaults to `PREFER_EXISTING`.
cipher_channel_strategy = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.CipherTextProperty.encrypt(
        ontology,
        object_type,
        primary_key,
        property,
        plaintext=plaintext,
        branch=branch,
        cipher_channel_strategy=cipher_channel_strategy,
        preview=preview,
    )
    print("The encrypt response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling CipherTextProperty.encrypt: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EncryptionResult  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

# **encrypt_with_default_channel**
Encrypt a plaintext value into a CipherText value for the given object type property.

The Cipher Channel used is the default channel configured for the property in ontology metadata. This
endpoint requires the CipherText property to have a configured `defaultCipherChannelRid`; if none is
configured an error will be thrown. To encrypt against the channel of an existing object's value, use the
**Encrypt** endpoint that accepts a `primaryKey` instead.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**ontology** | OntologyIdentifier |  |  |
**object_type** | ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.  |  |
**property** | PropertyApiName | The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.  |  |
**plaintext** | Plaintext |  |  |
**branch** | Optional[FoundryBranch] | The Foundry branch to read from. If not specified, the default branch will be used.  | [optional] |
**preview** | Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.  | [optional] |

### Return type
**EncryptionResult**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# OntologyIdentifier
ontology = "palantir"
# ObjectTypeApiName | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
object_type = "employee"
# PropertyApiName | The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint.
property = "performance"
# Plaintext
plaintext = "Jane Doe"
# Optional[FoundryBranch] | The Foundry branch to read from. If not specified, the default branch will be used.
branch = None
# Optional[PreviewMode] | A boolean flag that, when set to true, enables the use of beta features in preview mode.
preview = None


try:
    api_response = client.ontologies.CipherTextProperty.encrypt_with_default_channel(
        ontology, object_type, property, plaintext=plaintext, branch=branch, preview=preview
    )
    print("The encrypt_with_default_channel response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling CipherTextProperty.encrypt_with_default_channel: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EncryptionResult  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

