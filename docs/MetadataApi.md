# swagger_client.MetadataApi

All URIs are relative to */swqapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_count**](MetadataApi.md#get_device_count) | **GET** /pvsystems/{pvSystemId}/devices-count | This method returns number of devices contained within single PV System
[**get_device_id_list**](MetadataApi.md#get_device_id_list) | **GET** /pvsystems/{pvSystemId}/devices-list | This method returns list of all device ids, within single PV System
[**get_device_meta_data**](MetadataApi.md#get_device_meta_data) | **GET** /pvsystems/{pvSystemId}/devices/{deviceId} | This method returns single device and its details
[**get_device_meta_data_list**](MetadataApi.md#get_device_meta_data_list) | **GET** /pvsystems/{pvSystemId}/devices | This method returns list of all devices contained within single PV System
[**get_system_count**](MetadataApi.md#get_system_count) | **GET** /pvsystems-count | This method returns number of PV Systems owned by user
[**get_system_id_list**](MetadataApi.md#get_system_id_list) | **GET** /pvsystems-list | This method returns list of all PV Systems (ids only) owned by user
[**get_system_meta_data**](MetadataApi.md#get_system_meta_data) | **GET** /pvsystems/{pvSystemId} | This method returns single PV System and its details
[**get_system_meta_data_list**](MetadataApi.md#get_system_meta_data_list) | **GET** /pvsystems | This method returns list of all PV Systems and their details owned by user

# **get_device_count**
> Counter get_device_count(pv_system_id, type=type, is_active=is_active)

This method returns number of devices contained within single PV System

Metadata method - this method takes PV System ID as its parameter and will return number of devices within that PV System (also owned by user whose api key was used to send request)

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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a PV System whose devices are requested for inspection
type = 'type_example' # str | Type filter - one or more (coma separated, no spaces) types of devices. (optional)
is_active = true # bool | If set to \"true\", only active devices will be selected. If set to \"false\" only inactive devices will be selected. If it's not defined, both active and inactive devices will be selected. (optional)

try:
    # This method returns number of devices contained within single PV System
    api_response = api_instance.get_device_count(pv_system_id, type=type, is_active=is_active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_device_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| ID of a PV System whose devices are requested for inspection | 
 **type** | **str**| Type filter - one or more (coma separated, no spaces) types of devices. | [optional] 
 **is_active** | **bool**| If set to \&quot;true\&quot;, only active devices will be selected. If set to \&quot;false\&quot; only inactive devices will be selected. If it&#x27;s not defined, both active and inactive devices will be selected. | [optional] 

### Return type

[**Counter**](Counter.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_id_list**
> DeviceIdsOnly get_device_id_list(pv_system_id, type=type, offset=offset, limit=limit, is_active=is_active)

This method returns list of all device ids, within single PV System

Metadata method - this method takes PV System ID as its parameter and will return list of all devices (their ids), contained within that PV System (also owned by user whose api key was used to send request)

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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a PV System whose devices are requested for inspection
type = 'type_example' # str | Type filter - one or more (coma separated, no spaces) types of devices that pv system should contain. (optional)
offset = 56 # int | Skip this many elements. (optional)
limit = 56 # int | Return max this many elements. (optional)
is_active = true # bool | If set to \"true\", only active devices will be selected. If set to \"false\" only inactive devices will be selected. If it's not defined, both active and inactive devices will be selected. (optional)

try:
    # This method returns list of all device ids, within single PV System
    api_response = api_instance.get_device_id_list(pv_system_id, type=type, offset=offset, limit=limit, is_active=is_active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_device_id_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| ID of a PV System whose devices are requested for inspection | 
 **type** | **str**| Type filter - one or more (coma separated, no spaces) types of devices that pv system should contain. | [optional] 
 **offset** | **int**| Skip this many elements. | [optional] 
 **limit** | **int**| Return max this many elements. | [optional] 
 **is_active** | **bool**| If set to \&quot;true\&quot;, only active devices will be selected. If set to \&quot;false\&quot; only inactive devices will be selected. If it&#x27;s not defined, both active and inactive devices will be selected. | [optional] 

### Return type

[**DeviceIdsOnly**](DeviceIdsOnly.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_meta_data**
> Device get_device_meta_data(pv_system_id, device_id)

This method returns single device and its details

Metadata method - this method takes PV System ID and device ID as parameters and returns device (and its details) whose id was sent with request

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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a PV System which contains certain device
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a device user requires to inspect

try:
    # This method returns single device and its details
    api_response = api_instance.get_device_meta_data(pv_system_id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_device_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| ID of a PV System which contains certain device | 
 **device_id** | [**str**](.md)| ID of a device user requires to inspect | 

### Return type

[**Device**](Device.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_meta_data_list**
> DeviceList get_device_meta_data_list(pv_system_id, type=type, offset=offset, limit=limit, is_active=is_active)

This method returns list of all devices contained within single PV System

Metadata method - this method takes PV System ID as its parameter and will return list of all devices and their details contained within that PV System (also owned by user whose api key was used to send request)

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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a PV System whose devices are requested for inspection
type = 'type_example' # str | Type filter - one or more (coma separated, no spaces) types of devices that pv system should contain. (optional)
offset = 56 # int | Skip this many elements. (optional)
limit = 56 # int | Return max this many elements. (optional)
is_active = true # bool | If set to \"true\", only active devices will be selected. If set to \"false\" only inactive devices will be selected. If it's not defined, both active and inactive devices will be selected. (optional)

try:
    # This method returns list of all devices contained within single PV System
    api_response = api_instance.get_device_meta_data_list(pv_system_id, type=type, offset=offset, limit=limit, is_active=is_active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_device_meta_data_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| ID of a PV System whose devices are requested for inspection | 
 **type** | **str**| Type filter - one or more (coma separated, no spaces) types of devices that pv system should contain. | [optional] 
 **offset** | **int**| Skip this many elements. | [optional] 
 **limit** | **int**| Return max this many elements. | [optional] 
 **is_active** | **bool**| If set to \&quot;true\&quot;, only active devices will be selected. If set to \&quot;false\&quot; only inactive devices will be selected. If it&#x27;s not defined, both active and inactive devices will be selected. | [optional] 

### Return type

[**DeviceList**](DeviceList.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_count**
> Counter get_system_count(type=type)

This method returns number of PV Systems owned by user

Metadata method - this method takes no parameters and will return number of PV Systems that are owned by a user whose api key was used to send request

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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Type filter - one or more (coma separated, no spaces) types of devices that pv system should contain. (optional)

try:
    # This method returns number of PV Systems owned by user
    api_response = api_instance.get_system_count(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_system_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type filter - one or more (coma separated, no spaces) types of devices that pv system should contain. | [optional] 

### Return type

[**Counter**](Counter.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_id_list**
> PvSystemIdsOnly get_system_id_list(type=type, offset=offset, limit=limit)

This method returns list of all PV Systems (ids only) owned by user

Metadata method - this method takes no parameters and will return list of PV System IDs that are owned by a user whose api key was used to send request

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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Type filter - one or more (coma separated, no spaces) types of devices that pv system should contain. (optional)
offset = 56 # int | Skip this many elements. (optional)
limit = 56 # int | Return max this many elements. (optional)

try:
    # This method returns list of all PV Systems (ids only) owned by user
    api_response = api_instance.get_system_id_list(type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_system_id_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type filter - one or more (coma separated, no spaces) types of devices that pv system should contain. | [optional] 
 **offset** | **int**| Skip this many elements. | [optional] 
 **limit** | **int**| Return max this many elements. | [optional] 

### Return type

[**PvSystemIdsOnly**](PvSystemIdsOnly.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_meta_data**
> PvSystem get_system_meta_data(pv_system_id)

This method returns single PV System and its details

Metadata method - this method takes PV System ID as its parameter and will return details of that PV Systems, also owned by user whose api key was used to send request

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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a PV System user requires to inspect

try:
    # This method returns single PV System and its details
    api_response = api_instance.get_system_meta_data(pv_system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_system_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| ID of a PV System user requires to inspect | 

### Return type

[**PvSystem**](PvSystem.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_meta_data_list**
> PvSystemList get_system_meta_data_list(type=type, offset=offset, limit=limit)

This method returns list of all PV Systems and their details owned by user

Metadata method - this method takes no parameters and will return list of PV Systems that are owned by a user whose api key was used to send request

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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Type filter - one or more (coma separated, no spaces) types of devices that pv system should contain. (optional)
offset = 56 # int | Skip this many elements. (optional)
limit = 56 # int | Return max this many elements. (optional)

try:
    # This method returns list of all PV Systems and their details owned by user
    api_response = api_instance.get_system_meta_data_list(type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_system_meta_data_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type filter - one or more (coma separated, no spaces) types of devices that pv system should contain. | [optional] 
 **offset** | **int**| Skip this many elements. | [optional] 
 **limit** | **int**| Return max this many elements. | [optional] 

### Return type

[**PvSystemList**](PvSystemList.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

