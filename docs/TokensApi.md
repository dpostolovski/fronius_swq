# swagger_client.TokensApi

All URIs are relative to */swqapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_jwt**](TokensApi.md#generate_jwt) | **POST** /iam/jwt | 
[**iam_redirect**](TokensApi.md#iam_redirect) | **GET** /iam/jwt | 
[**refresh_jwt**](TokensApi.md#refresh_jwt) | **PATCH** /iam/jwt/{refreshToken} | 

# **generate_jwt**
> Token generate_jwt(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessKeyId
configuration = swagger_client.Configuration()
configuration.api_key['AccessKeyId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessKeyId'] = 'Bearer'
# Configure API key authorization: AccessKeyValue
configuration = swagger_client.Configuration()
configuration.api_key['AccessKeyValue'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessKeyValue'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TokensApi(swagger_client.ApiClient(configuration))
body = swagger_client.InputNewToken() # InputNewToken |  (optional)

try:
    api_response = api_instance.generate_jwt(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->generate_jwt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputNewToken**](InputNewToken.md)|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_redirect**
> iam_redirect(redirect_uri=redirect_uri)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessKeyId
configuration = swagger_client.Configuration()
configuration.api_key['AccessKeyId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessKeyId'] = 'Bearer'
# Configure API key authorization: AccessKeyValue
configuration = swagger_client.Configuration()
configuration.api_key['AccessKeyValue'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessKeyValue'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TokensApi(swagger_client.ApiClient(configuration))
redirect_uri = 'redirect_uri_example' # str |  (optional)

try:
    api_instance.iam_redirect(redirect_uri=redirect_uri)
except ApiException as e:
    print("Exception when calling TokensApi->iam_redirect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_uri** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_jwt**
> Token refresh_jwt(refresh_token)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessKeyId
configuration = swagger_client.Configuration()
configuration.api_key['AccessKeyId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessKeyId'] = 'Bearer'
# Configure API key authorization: AccessKeyValue
configuration = swagger_client.Configuration()
configuration.api_key['AccessKeyValue'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessKeyValue'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TokensApi(swagger_client.ApiClient(configuration))
refresh_token = 'refresh_token_example' # str | 

try:
    api_response = api_instance.refresh_jwt(refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->refresh_jwt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**|  | 

### Return type

[**Token**](Token.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

