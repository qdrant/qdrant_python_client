# openapi_client.PointsApi

All URIs are relative to *http://localhost:6333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_point**](PointsApi.md#get_point) | **GET** /collections/{name}/points/{id} | Retrieve point by id
[**get_points**](PointsApi.md#get_points) | **POST** /collections/{name}/points | Retrieve points by ids
[**search_points**](PointsApi.md#search_points) | **POST** /collections/{name}/points/search | Search points
[**update_points**](PointsApi.md#update_points) | **POST** /collections/{name} | Update points in collection


# **get_point**
> InlineResponse2004 get_point(name, id)

Retrieve point by id

### Example

```python
import time
import qdrant_openapi_client
from qdrant_openapi_client.api import points_api
from qdrant_openapi_client.model.error_response import ErrorResponse
from qdrant_openapi_client.model.inline_response2004 import InlineResponse2004
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi_client.Configuration(
    host = "http://localhost:6333"
)


# Enter a context with an instance of the API client
with qdrant_openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = points_api.PointsApi(api_client)
    name = "name_example" # str | Name of the collection to retrieve from
    id = 1 # int | Id of the point

    # example passing only required values which don't have defaults set
    try:
        # Retrieve point by id
        api_response = api_instance.get_point(name, id)
        pprint(api_response)
    except qdrant_openapi_client.ApiException as e:
        print("Exception when calling PointsApi->get_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the collection to retrieve from |
 **id** | **int**| Id of the point |

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_points**
> InlineResponse2005 get_points(name)

Retrieve points by ids

### Example

```python
import time
import qdrant_openapi_client
from qdrant_openapi_client.api import points_api
from qdrant_openapi_client.model.error_response import ErrorResponse
from qdrant_openapi_client.model.inline_response2005 import InlineResponse2005
from qdrant_openapi_client.model.point_request import PointRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi_client.Configuration(
    host = "http://localhost:6333"
)


# Enter a context with an instance of the API client
with qdrant_openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = points_api.PointsApi(api_client)
    name = "name_example" # str | Name of the collection to retrieve from
    point_request = PointRequest(
        ids=[
            0,
        ],
    ) # PointRequest | List of points to retrieve (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve points by ids
        api_response = api_instance.get_points(name)
        pprint(api_response)
    except qdrant_openapi_client.ApiException as e:
        print("Exception when calling PointsApi->get_points: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve points by ids
        api_response = api_instance.get_points(name, point_request=point_request)
        pprint(api_response)
    except qdrant_openapi_client.ApiException as e:
        print("Exception when calling PointsApi->get_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the collection to retrieve from |
 **point_request** | [**PointRequest**](PointRequest.md)| List of points to retrieve | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_points**
> InlineResponse2006 search_points(name)

Search points

### Example

```python
import time
import qdrant_openapi_client
from qdrant_openapi_client.api import points_api
from qdrant_openapi_client.model.error_response import ErrorResponse
from qdrant_openapi_client.model.inline_response2006 import InlineResponse2006
from qdrant_openapi_client.model.search_request import SearchRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi_client.Configuration(
    host = "http://localhost:6333"
)


# Enter a context with an instance of the API client
with qdrant_openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = points_api.PointsApi(api_client)
    name = "name_example" # str | Name of the collection to search in
    search_request = SearchRequest(
        filter=,
        params=,
        top=0,
        vector=[
            3.14,
        ],
    ) # SearchRequest | Search request with optional filtering (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search points
        api_response = api_instance.search_points(name)
        pprint(api_response)
    except qdrant_openapi_client.ApiException as e:
        print("Exception when calling PointsApi->search_points: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search points
        api_response = api_instance.search_points(name, search_request=search_request)
        pprint(api_response)
    except qdrant_openapi_client.ApiException as e:
        print("Exception when calling PointsApi->search_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the collection to search in |
 **search_request** | [**SearchRequest**](SearchRequest.md)| Search request with optional filtering | [optional]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_points**
> InlineResponse2003 update_points(name)

Update points in collection

### Example

```python
import time
import qdrant_openapi_client
from qdrant_openapi_client.api import points_api
from qdrant_openapi_client.model.inline_response2003 import InlineResponse2003
from qdrant_openapi_client.model.error_response import ErrorResponse
from qdrant_openapi_client.model.collection_update_operations import CollectionUpdateOperations
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi_client.Configuration(
    host = "http://localhost:6333"
)


# Enter a context with an instance of the API client
with qdrant_openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = points_api.PointsApi(api_client)
    name = "name_example" # str | Name of the collection to search in
    collection_update_operations = CollectionUpdateOperations() # CollectionUpdateOperations | Points update operations (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update points in collection
        api_response = api_instance.update_points(name)
        pprint(api_response)
    except qdrant_openapi_client.ApiException as e:
        print("Exception when calling PointsApi->update_points: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update points in collection
        api_response = api_instance.update_points(name, collection_update_operations=collection_update_operations)
        pprint(api_response)
    except qdrant_openapi_client.ApiException as e:
        print("Exception when calling PointsApi->update_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the collection to search in |
 **collection_update_operations** | [**CollectionUpdateOperations**](CollectionUpdateOperations.md)| Points update operations | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

