# swagger_client.AggregatedApi

All URIs are relative to */swqapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregated_data_days**](AggregatedApi.md#get_aggregated_data_days) | **GET** /pvsystems/{pvSystemId}/aggdata/years/{year}/months/{month}/days | This method returns daily aggregated data for a specific PV system for a specific month of a year.
[**get_aggregated_data_months**](AggregatedApi.md#get_aggregated_data_months) | **GET** /pvsystems/{pvSystemId}/aggdata/years/{year}/months | This method returns monthly aggregated data for a specific PV system for a specific year.
[**get_aggregated_data_specific_day**](AggregatedApi.md#get_aggregated_data_specific_day) | **GET** /pvsystems/{pvSystemId}/aggdata/years/{year}/months/{month}/days/{day} | This method returns daily aggregated data for a specific PV system for a specific date.
[**get_aggregated_data_specific_month**](AggregatedApi.md#get_aggregated_data_specific_month) | **GET** /pvsystems/{pvSystemId}/aggdata/years/{year}/months/{month} | This method returns monthly aggregated data for a specific PV system for a specific month of a year.
[**get_aggregated_data_specific_year**](AggregatedApi.md#get_aggregated_data_specific_year) | **GET** /pvsystems/{pvSystemId}/aggdata/years/{year} | This method returns annual aggregated data for a specific PV system for a specific year.
[**get_aggregated_data_total**](AggregatedApi.md#get_aggregated_data_total) | **GET** /pvsystems/{pvSystemId}/aggdata | This method returns total lifetime aggregated data for a specific PV system.
[**get_aggregated_data_years**](AggregatedApi.md#get_aggregated_data_years) | **GET** /pvsystems/{pvSystemId}/aggdata/years | This method returns annual aggregated data for a specific PV system for all years since installation.

# **get_aggregated_data_days**
> AggregatedValues get_aggregated_data_days(pv_system_id, year, month, channel=channel)

This method returns daily aggregated data for a specific PV system for a specific month of a year.

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
api_instance = swagger_client.AggregatedApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
year = 56 # int | 
month = 56 # int | 
channel = 'channel_example' # str |  (optional)

try:
    # This method returns daily aggregated data for a specific PV system for a specific month of a year.
    api_response = api_instance.get_aggregated_data_days(pv_system_id, year, month, channel=channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatedApi->get_aggregated_data_days: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **year** | **int**|  | 
 **month** | **int**|  | 
 **channel** | **str**|  | [optional] 

### Return type

[**AggregatedValues**](AggregatedValues.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_data_months**
> AggregatedValues get_aggregated_data_months(pv_system_id, year, channel=channel)

This method returns monthly aggregated data for a specific PV system for a specific year.

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
api_instance = swagger_client.AggregatedApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
year = 56 # int | 
channel = 'channel_example' # str |  (optional)

try:
    # This method returns monthly aggregated data for a specific PV system for a specific year.
    api_response = api_instance.get_aggregated_data_months(pv_system_id, year, channel=channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatedApi->get_aggregated_data_months: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **year** | **int**|  | 
 **channel** | **str**|  | [optional] 

### Return type

[**AggregatedValues**](AggregatedValues.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_data_specific_day**
> AggregatedValues get_aggregated_data_specific_day(pv_system_id, year, month, day, channel=channel)

This method returns daily aggregated data for a specific PV system for a specific date.

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
api_instance = swagger_client.AggregatedApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
year = 56 # int | 
month = 56 # int | 
day = 56 # int | 
channel = 'channel_example' # str |  (optional)

try:
    # This method returns daily aggregated data for a specific PV system for a specific date.
    api_response = api_instance.get_aggregated_data_specific_day(pv_system_id, year, month, day, channel=channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatedApi->get_aggregated_data_specific_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **year** | **int**|  | 
 **month** | **int**|  | 
 **day** | **int**|  | 
 **channel** | **str**|  | [optional] 

### Return type

[**AggregatedValues**](AggregatedValues.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_data_specific_month**
> AggregatedValues get_aggregated_data_specific_month(pv_system_id, year, month, channel=channel)

This method returns monthly aggregated data for a specific PV system for a specific month of a year.

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
api_instance = swagger_client.AggregatedApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
year = 56 # int | 
month = 56 # int | 
channel = 'channel_example' # str |  (optional)

try:
    # This method returns monthly aggregated data for a specific PV system for a specific month of a year.
    api_response = api_instance.get_aggregated_data_specific_month(pv_system_id, year, month, channel=channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatedApi->get_aggregated_data_specific_month: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **year** | **int**|  | 
 **month** | **int**|  | 
 **channel** | **str**|  | [optional] 

### Return type

[**AggregatedValues**](AggregatedValues.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_data_specific_year**
> AggregatedValues get_aggregated_data_specific_year(pv_system_id, year, channel=channel)

This method returns annual aggregated data for a specific PV system for a specific year.

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
api_instance = swagger_client.AggregatedApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
year = 56 # int | 
channel = 'channel_example' # str |  (optional)

try:
    # This method returns annual aggregated data for a specific PV system for a specific year.
    api_response = api_instance.get_aggregated_data_specific_year(pv_system_id, year, channel=channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatedApi->get_aggregated_data_specific_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **year** | **int**|  | 
 **channel** | **str**|  | [optional] 

### Return type

[**AggregatedValues**](AggregatedValues.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_data_total**
> AggregatedValues get_aggregated_data_total(pv_system_id, channel=channel)

This method returns total lifetime aggregated data for a specific PV system.

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
api_instance = swagger_client.AggregatedApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
channel = 'channel_example' # str |  (optional)

try:
    # This method returns total lifetime aggregated data for a specific PV system.
    api_response = api_instance.get_aggregated_data_total(pv_system_id, channel=channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatedApi->get_aggregated_data_total: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **channel** | **str**|  | [optional] 

### Return type

[**AggregatedValues**](AggregatedValues.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_data_years**
> AggregatedValues get_aggregated_data_years(pv_system_id, channel=channel)

This method returns annual aggregated data for a specific PV system for all years since installation.

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
api_instance = swagger_client.AggregatedApi(swagger_client.ApiClient(configuration))
pv_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
channel = 'channel_example' # str |  (optional)

try:
    # This method returns annual aggregated data for a specific PV system for all years since installation.
    api_response = api_instance.get_aggregated_data_years(pv_system_id, channel=channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatedApi->get_aggregated_data_years: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pv_system_id** | [**str**](.md)|  | 
 **channel** | **str**|  | [optional] 

### Return type

[**AggregatedValues**](AggregatedValues.md)

### Authorization

[AccessKeyId](../README.md#AccessKeyId), [AccessKeyValue](../README.md#AccessKeyValue), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

