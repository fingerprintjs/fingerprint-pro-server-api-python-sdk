# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fingerprint_pro_server_api_sdk.api_client import ApiClient
from fingerprint_pro_server_api_sdk.extend_exception import extend_exception
from fingerprint_pro_server_api_sdk.rest import ApiException


class FingerprintApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, configuration=None, pool=None):
        if configuration is None:
            raise ValueError("Missing the required parameter `configuration` when calling `FingerprintApi`")  # noqa: E501
        self.api_client = ApiClient(configuration, pool=pool)

    def get_event(self, request_id, **kwargs):  # noqa: E501
        """Get event by requestId  # noqa: E501

        This endpoint allows you to get a detailed analysis of an individual request.  **Only for Enterprise customers:** Please note that the response includes mobile signals (e.g. `rootApps`) even if the request originated from a non-mobile platform. It is highly recommended that you **ignore** the mobile signals for such requests.   Use `requestId` as the URL path parameter. This API method is scoped to a request, i.e. all returned information is by `requestId`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event(request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str request_id: The unique [identifier](https://dev.fingerprint.com/docs/js-agent#requestid) of each analysis request. (required)
        :return: EventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_event_with_http_info(request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_event_with_http_info(request_id, **kwargs)  # noqa: E501
            return data

    def get_event_with_http_info(self, request_id, **kwargs):  # noqa: E501
        """Get event by requestId  # noqa: E501

        This endpoint allows you to get a detailed analysis of an individual request.  **Only for Enterprise customers:** Please note that the response includes mobile signals (e.g. `rootApps`) even if the request originated from a non-mobile platform. It is highly recommended that you **ignore** the mobile signals for such requests.   Use `requestId` as the URL path parameter. This API method is scoped to a request, i.e. all returned information is by `requestId`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_with_http_info(request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str request_id: The unique [identifier](https://dev.fingerprint.com/docs/js-agent#requestid) of each analysis request. (required)
        :return: EventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request_id' is set
        if ('request_id' not in params or
                                                       params['request_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `request_id` when calling `get_event`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'request_id' in params:
            path_params['request_id'] = params['request_id']  # noqa: E501

        query_params = []
        query_params.append(('ii', 'fingerprint-pro-server-python-sdk/6.0.0'))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

        try:
            return self.api_client.call_api(
                '/events/{request_id}', 'GET',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type='EventResponse',  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats)
        except ApiException as e:
            if e.status == 403:
                error = self.api_client.deserialize(e, 'ErrorEvent403Response', True)
                raise extend_exception(e, error)
            if e.status == 404:
                error = self.api_client.deserialize(e, 'ErrorEvent404Response', True)
                raise extend_exception(e, error)
            raise e

    def get_visits(self, visitor_id, **kwargs):  # noqa: E501
        """Get visits by visitorId  # noqa: E501

        This endpoint allows you to get a history of visits for a specific `visitorId`. Use the `visitorId` as a URL path parameter. Only information from the _Identification_ product is returned.  #### Headers  * `Retry-After` — Present in case of `429 Too many requests`. Indicates how long you should wait before making a follow-up request. The value is non-negative decimal integer indicating the seconds to delay after the response is received.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_visits(visitor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str visitor_id: Unique identifier of the visitor issued by Fingerprint Pro. (required)
        :param str request_id: Filter visits by `requestId`.   Every identification request has a unique identifier associated with it called `requestId`. This identifier is returned to the client in the identification [result](https://dev.fingerprint.com/docs/js-agent#requestid). When you filter visits by `requestId`, only one visit will be returned. 
        :param str linked_id: Filter visits by your custom identifier.   You can use [`linkedId`](https://dev.fingerprint.com/docs/js-agent#linkedid) to associate identification requests with your own identifier, for example: session ID, purchase ID, or transaction ID. You can then use this `linked_id` parameter to retrieve all events associated with your custom identifier. 
        :param int limit: Limit scanned results.   For performance reasons, the API first scans some number of events before filtering them. Use `limit` to specify how many events are scanned before they are filtered by `requestId` or `linkedId`. Results are always returned sorted by the timestamp (most recent first). By default, the most recent 100 visits are scanned, the maximum is 500. 
        :param str pagination_key: Use `paginationKey` to get the next page of results.   When more results are available (e.g., you requested 200 results using `limit` parameter, but a total of 600 results are available), the `paginationKey` top-level attribute is added to the response. The key corresponds to the `requestId` of the last returned event. In the following request, use that value in the `paginationKey` parameter to get the next page of results:  1. First request, returning most recent 200 events: `GET api-base-url/visitors/:visitorId?limit=200` 2. Use `response.paginationKey` to get the next page of results: `GET api-base-url/visitors/:visitorId?limit=200&paginationKey=1683900801733.Ogvu1j`  Pagination happens during scanning and before filtering, so you can get less visits than the `limit` you specified with more available on the next page. When there are no more results available for scanning, the `paginationKey` attribute is not returned. 
        :param int before: ⚠️ Deprecated pagination method, please use `paginationKey` instead. Timestamp (in milliseconds since epoch) used to paginate results. 
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_visits_with_http_info(visitor_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_visits_with_http_info(visitor_id, **kwargs)  # noqa: E501
            return data

    def get_visits_with_http_info(self, visitor_id, **kwargs):  # noqa: E501
        """Get visits by visitorId  # noqa: E501

        This endpoint allows you to get a history of visits for a specific `visitorId`. Use the `visitorId` as a URL path parameter. Only information from the _Identification_ product is returned.  #### Headers  * `Retry-After` — Present in case of `429 Too many requests`. Indicates how long you should wait before making a follow-up request. The value is non-negative decimal integer indicating the seconds to delay after the response is received.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_visits_with_http_info(visitor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str visitor_id: Unique identifier of the visitor issued by Fingerprint Pro. (required)
        :param str request_id: Filter visits by `requestId`.   Every identification request has a unique identifier associated with it called `requestId`. This identifier is returned to the client in the identification [result](https://dev.fingerprint.com/docs/js-agent#requestid). When you filter visits by `requestId`, only one visit will be returned. 
        :param str linked_id: Filter visits by your custom identifier.   You can use [`linkedId`](https://dev.fingerprint.com/docs/js-agent#linkedid) to associate identification requests with your own identifier, for example: session ID, purchase ID, or transaction ID. You can then use this `linked_id` parameter to retrieve all events associated with your custom identifier. 
        :param int limit: Limit scanned results.   For performance reasons, the API first scans some number of events before filtering them. Use `limit` to specify how many events are scanned before they are filtered by `requestId` or `linkedId`. Results are always returned sorted by the timestamp (most recent first). By default, the most recent 100 visits are scanned, the maximum is 500. 
        :param str pagination_key: Use `paginationKey` to get the next page of results.   When more results are available (e.g., you requested 200 results using `limit` parameter, but a total of 600 results are available), the `paginationKey` top-level attribute is added to the response. The key corresponds to the `requestId` of the last returned event. In the following request, use that value in the `paginationKey` parameter to get the next page of results:  1. First request, returning most recent 200 events: `GET api-base-url/visitors/:visitorId?limit=200` 2. Use `response.paginationKey` to get the next page of results: `GET api-base-url/visitors/:visitorId?limit=200&paginationKey=1683900801733.Ogvu1j`  Pagination happens during scanning and before filtering, so you can get less visits than the `limit` you specified with more available on the next page. When there are no more results available for scanning, the `paginationKey` attribute is not returned. 
        :param int before: ⚠️ Deprecated pagination method, please use `paginationKey` instead. Timestamp (in milliseconds since epoch) used to paginate results. 
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['visitor_id', 'request_id', 'linked_id', 'limit', 'pagination_key', 'before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_visits" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'visitor_id' is set
        if ('visitor_id' not in params or
                                                       params['visitor_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `visitor_id` when calling `get_visits`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'visitor_id' in params:
            path_params['visitor_id'] = params['visitor_id']  # noqa: E501

        query_params = []
        query_params.append(('ii', 'fingerprint-pro-server-python-sdk/6.0.0'))
        if 'request_id' in params:
            query_params.append(('request_id', params['request_id']))  # noqa: E501
        if 'linked_id' in params:
            query_params.append(('linked_id', params['linked_id']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'pagination_key' in params:
            query_params.append(('paginationKey', params['pagination_key']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

        try:
            return self.api_client.call_api(
                '/visitors/{visitor_id}', 'GET',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type='Response',  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats)
        except ApiException as e:
            if e.status == 403:
                error = self.api_client.deserialize(e, 'ErrorVisits403', True)
                raise extend_exception(e, error)
            if e.status == 429:
                error = self.api_client.deserialize(e, 'ManyRequestsResponse', True)
                raise extend_exception(e, error)
            raise e
