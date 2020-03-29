# swagger_client.HistoricalApi

All URIs are relative to */swqapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**historical_data**](HistoricalApi.md#historical_data) | **GET** /pvsystems/{pvSystemId}/histdata | This method returns the past time detail values for a specific PV system. The data is returned in granularity of 5 minute intervals.
[**historical_data_for_specific_device**](HistoricalApi.md#historical_data_for_specific_device) | **GET** /pvsystems/{pvSystemId}/devices/{deviceId}/histdata | This method returns the past time detail values for a specific device. The data is returned in granularity of 5 minute intervals.

# **historical_data**
> HistoricalValues historical_data(pv_system_id, _from, to, channel=channel, offset=offset, limit=limit)

This method returns the past time detail values for a specific PV system. The data is returned in granularity of 5 minute intervals.

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
api_instance = swagger_client.HistoricalApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
_from = '_from_example' # str | Date time format yyyy-MM-ddTHH:mm:ssZ or Unix time
to = 'to_example' # str | Date time format yyyy-MM-ddTHH:mm:ssZ or Unix time
channel = 'channel_example' # str |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # This method returns the past time detail values for a specific PV system. The data is returned in granularity of 5 minute intervals.
    api_response = api_instance.historical_data(pv_system_id, _from, to, channel=channel, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoricalApi->historical_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **_from** | **str**| Date time format yyyy-MM-ddTHH:mm:ssZ or Unix time | 
 **to** | **str**| Date time format yyyy-MM-ddTHH:mm:ssZ or Unix time | 
 **channel** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**HistoricalValues**](HistoricalValues.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **historical_data_for_specific_device**
> HistoricalValues historical_data_for_specific_device(pv_system_id, device_id, _from, to, channel=channel, offset=offset, limit=limit)

This method returns the past time detail values for a specific device. The data is returned in granularity of 5 minute intervals.

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
api_instance = swagger_client.HistoricalApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
_from = '_from_example' # str | Date time format yyyy-MM-ddTHH:mm:ssZ or Unix time
to = 'to_example' # str | Date time format yyyy-MM-ddTHH:mm:ssZ or Unix time
channel = 'channel_example' # str |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # This method returns the past time detail values for a specific device. The data is returned in granularity of 5 minute intervals.
    api_response = api_instance.historical_data_for_specific_device(pv_system_id, device_id, _from, to, channel=channel, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoricalApi->historical_data_for_specific_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **device_id** | [**str**](.md)|  | 
 **_from** | **str**| Date time format yyyy-MM-ddTHH:mm:ssZ or Unix time | 
 **to** | **str**| Date time format yyyy-MM-ddTHH:mm:ssZ or Unix time | 
 **channel** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**HistoricalValues**](HistoricalValues.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

