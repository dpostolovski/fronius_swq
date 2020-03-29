# swagger_client.EnergyFlowApi

All URIs are relative to */swqapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_flow_data**](EnergyFlowApi.md#get_flow_data) | **GET** /pvsystems/{pvSystemId}/flowdata | This method returns energy flow values for a specific PV system
[**get_flow_data_for_specific_device**](EnergyFlowApi.md#get_flow_data_for_specific_device) | **GET** /pvsystems/{pvSystemId}/devices/{deviceId}/flowdata | 

# **get_flow_data**
> EnergyFlow get_flow_data(pv_system_id)

This method returns energy flow values for a specific PV system

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
api_instance = swagger_client.EnergyFlowApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of a PV System

try:
    # This method returns energy flow values for a specific PV system
    api_response = api_instance.get_flow_data(pv_system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnergyFlowApi->get_flow_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)| ID of a PV System | 

### Return type

[**EnergyFlow**](EnergyFlow.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_data_for_specific_device**
> EnergyFlow get_flow_data_for_specific_device(pv_system_id, device_id)



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
api_instance = swagger_client.EnergyFlowApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.get_flow_data_for_specific_device(pv_system_id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnergyFlowApi->get_flow_data_for_specific_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **device_id** | [**str**](.md)|  | 

### Return type

[**EnergyFlow**](EnergyFlow.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

