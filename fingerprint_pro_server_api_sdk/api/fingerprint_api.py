# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API provides a way for validating visitors’ data issued by Fingerprint Pro.  # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fingerprint_pro_server_api_sdk.api_client import ApiClient


class FingerprintApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, configuration=None):
        if configuration is None:
            raise ValueError("Missing the required parameter `configuration` when calling `FingerprintApi`")  # noqa: E501
        self.api_client = ApiClient(configuration)

    def get_event(self, request_id, **kwargs):  # noqa: E501
        """Get event by request ID  # noqa: E501

        This endpoint allows you to get events with all the information from each activated product - BOTD and Fingerprinting. Use the requestId as a URL path :request_id parameter. This API method is scoped to a request, i.e. all returned information is by requestId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event(request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str request_id: Request ID (required)
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
        """Get event by request ID  # noqa: E501

        This endpoint allows you to get events with all the information from each activated product - BOTD and Fingerprinting. Use the requestId as a URL path :request_id parameter. This API method is scoped to a request, i.e. all returned information is by requestId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_with_http_info(request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str request_id: Request ID (required)
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
        query_params.append(('ii', 'fingerprint-pro-server-python-sdk/1.3.0'))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

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

    def get_visits(self, visitor_id, **kwargs):  # noqa: E501
        """get_visits  # noqa: E501

        This endpoint allows you to get a history of visits with all available information. Use the visitorId as a URL path parameter. This API method is scoped to a visitor, i.e. all returned information is by visitorId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_visits(visitor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str visitor_id: (required)
        :param str request_id: Filter events by requestId
        :param str linked_id: Filter events by custom identifier
        :param int limit: Limit scanned results
        :param int before: Used to paginate results
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
        """get_visits  # noqa: E501

        This endpoint allows you to get a history of visits with all available information. Use the visitorId as a URL path parameter. This API method is scoped to a visitor, i.e. all returned information is by visitorId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_visits_with_http_info(visitor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str visitor_id: (required)
        :param str request_id: Filter events by requestId
        :param str linked_id: Filter events by custom identifier
        :param int limit: Limit scanned results
        :param int before: Used to paginate results
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['visitor_id', 'request_id', 'linked_id', 'limit', 'before']  # noqa: E501
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
        query_params.append(('ii', 'fingerprint-pro-server-python-sdk/1.3.0'))
        if 'request_id' in params:
            query_params.append(('request_id', params['request_id']))  # noqa: E501
        if 'linked_id' in params:
            query_params.append(('linked_id', params['linked_id']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
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
