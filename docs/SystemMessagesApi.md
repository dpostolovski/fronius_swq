# swagger_client.SystemMessagesApi

All URIs are relative to */swqapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_messages**](SystemMessagesApi.md#get_device_messages) | **GET** /pvsystems/{pvSystemId}/devices/{deviceId}/messages/{languageCode} | 
[**get_device_messages_count**](SystemMessagesApi.md#get_device_messages_count) | **GET** /pvsystems/{pvSystemId}/devices/{deviceId}/messages-count | 
[**get_system_messages**](SystemMessagesApi.md#get_system_messages) | **GET** /pvsystems/{pvSystemId}/messages/{languageCode} | 
[**get_system_messages_count**](SystemMessagesApi.md#get_system_messages_count) | **GET** /pvsystems/{pvSystemId}/messages-count | 

# **get_device_messages**
> SystemMessageList get_device_messages(pv_system_id, device_id, _from, language_code, state_type=state_type, state_code=state_code, to=to, offset=offset, limit=limit)



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
api_instance = swagger_client.SystemMessagesApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
_from = '_from_example' # str | 
language_code = 'language_code_example' # str | 
state_type = 'state_type_example' # str |  (optional)
state_code = 56 # int |  (optional)
to = 'to_example' # str |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    api_response = api_instance.get_device_messages(pv_system_id, device_id, _from, language_code, state_type=state_type, state_code=state_code, to=to, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemMessagesApi->get_device_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **device_id** | [**str**](.md)|  | 
 **_from** | **str**|  | 
 **language_code** | **str**|  | 
 **state_type** | **str**|  | [optional] 
 **state_code** | **int**|  | [optional] 
 **to** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**SystemMessageList**](SystemMessageList.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_messages_count**
> SystemMessageList get_device_messages_count(pv_system_id, device_id, _from, state_type=state_type, state_code=state_code, to=to, language_code=language_code)



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
api_instance = swagger_client.SystemMessagesApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
_from = '_from_example' # str | 
state_type = 'state_type_example' # str |  (optional)
state_code = 56 # int |  (optional)
to = 'to_example' # str |  (optional)
language_code = 'language_code_example' # str |  (optional)

try:
    api_response = api_instance.get_device_messages_count(pv_system_id, device_id, _from, state_type=state_type, state_code=state_code, to=to, language_code=language_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemMessagesApi->get_device_messages_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **device_id** | [**str**](.md)|  | 
 **_from** | **str**|  | 
 **state_type** | **str**|  | [optional] 
 **state_code** | **int**|  | [optional] 
 **to** | **str**|  | [optional] 
 **language_code** | **str**|  | [optional] 

### Return type

[**SystemMessageList**](SystemMessageList.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_messages**
> SystemMessageList get_system_messages(pv_system_id, _from, language_code, state_type=state_type, state_code=state_code, to=to, type=type, offset=offset, limit=limit)



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
api_instance = swagger_client.SystemMessagesApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
_from = '_from_example' # str | 
language_code = 'language_code_example' # str | 
state_type = 'state_type_example' # str |  (optional)
state_code = 56 # int |  (optional)
to = 'to_example' # str |  (optional)
type = 'type_example' # str |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    api_response = api_instance.get_system_messages(pv_system_id, _from, language_code, state_type=state_type, state_code=state_code, to=to, type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemMessagesApi->get_system_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **_from** | **str**|  | 
 **language_code** | **str**|  | 
 **state_type** | **str**|  | [optional] 
 **state_code** | **int**|  | [optional] 
 **to** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**SystemMessageList**](SystemMessageList.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_messages_count**
> SystemMessageList get_system_messages_count(pv_system_id, _from, state_type=state_type, state_code=state_code, to=to, type=type, language_code=language_code)



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
api_instance = swagger_client.SystemMessagesApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
_from = '_from_example' # str | 
state_type = 'state_type_example' # str |  (optional)
state_code = 56 # int |  (optional)
to = 'to_example' # str |  (optional)
type = 'type_example' # str |  (optional)
language_code = 'language_code_example' # str |  (optional)

try:
    api_response = api_instance.get_system_messages_count(pv_system_id, _from, state_type=state_type, state_code=state_code, to=to, type=type, language_code=language_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemMessagesApi->get_system_messages_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **_from** | **str**|  | 
 **state_type** | **str**|  | [optional] 
 **state_code** | **int**|  | [optional] 
 **to** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **language_code** | **str**|  | [optional] 

### Return type

[**SystemMessageList**](SystemMessageList.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

