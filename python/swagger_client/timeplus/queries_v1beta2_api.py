# coding: utf-8

"""
    Timeplus

    Welcome to the Timeplus HTTP REST API specification.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@timeplus.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class QueriesV1beta2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1beta2_format_post(self, body, **kwargs):  # noqa: E501
        """format a query.  # noqa: E501

        Format the given query and make it easy to read.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_format_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FormatQueryRequest body: the query SQL to be formatted (required)
        :return: FormatQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_format_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_format_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1beta2_format_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """format a query.  # noqa: E501

        Format the given query and make it easy to read.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_format_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FormatQueryRequest body: the query SQL to be formatted (required)
        :return: FormatQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_format_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1beta2_format_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/format', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormatQueryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_queries_get(self, **kwargs):  # noqa: E501
        """list queries.  # noqa: E501

        Get all queries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag: filter by tag
        :return: list[Query]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_queries_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_queries_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1beta2_queries_get_with_http_info(self, **kwargs):  # noqa: E501
        """list queries.  # noqa: E501

        Get all queries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag: filter by tag
        :return: list[Query]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_queries_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/queries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Query]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_queries_id_cancel_post(self, id, **kwargs):  # noqa: E501
        """cancel a query.  # noqa: E501

        Cancel the query with the given ID. If given query is not running, the request will do nothing. Otherwise, the query will be canceled and the `status` will be set to `canceled`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_id_cancel_post(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: query ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_queries_id_cancel_post_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_queries_id_cancel_post_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1beta2_queries_id_cancel_post_with_http_info(self, id, **kwargs):  # noqa: E501
        """cancel a query.  # noqa: E501

        Cancel the query with the given ID. If given query is not running, the request will do nothing. Otherwise, the query will be canceled and the `status` will be set to `canceled`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_id_cancel_post_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: query ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_queries_id_cancel_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1beta2_queries_id_cancel_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/queries/{id}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_queries_id_delete(self, id, **kwargs):  # noqa: E501
        """delete a query.  # noqa: E501

        Delete the query with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: query ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_queries_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_queries_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1beta2_queries_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """delete a query.  # noqa: E501

        Delete the query with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: query ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_queries_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1beta2_queries_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/queries/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_queries_id_get(self, id, **kwargs):  # noqa: E501
        """get a query.  # noqa: E501

        Get the query with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: query ID (required)
        :return: Query
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_queries_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_queries_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1beta2_queries_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """get a query.  # noqa: E501

        Get the query with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: query ID (required)
        :return: Query
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_queries_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1beta2_queries_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/queries/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Query',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_queries_id_pipeline_get(self, id, **kwargs):  # noqa: E501
        """get the pipeline for a query  # noqa: E501

        get the pipeline for a query  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_id_pipeline_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: query ID (required)
        :return: QueryPipeline
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_queries_id_pipeline_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_queries_id_pipeline_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1beta2_queries_id_pipeline_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """get the pipeline for a query  # noqa: E501

        get the pipeline for a query  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_id_pipeline_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: query ID (required)
        :return: QueryPipeline
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_queries_id_pipeline_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1beta2_queries_id_pipeline_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/queries/{id}/pipeline', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QueryPipeline',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_queries_post(self, body, **kwargs):  # noqa: E501
        """execute a query and return the results.  # noqa: E501

        Execute a query and return the results. * If the request fails, the response content type will be `application/json`. Please refer to the failure codes in Responses section below. * If the query is executed successfully, the response content type will be `text/event-stream`. **For SSE** There are 3 types of data that will be sent to SSE channel 1. Query (type `query`): The first event of the result will ALWAYS be this type. 2. Metrics (type `metrics`): The query metrics in JSON. They will be sent every 1 seconds. 3. Data (the type is empty): The query result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateQueryRequestV1Beta2 body: query request parameters (required)
        :return: Query
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_queries_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_queries_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1beta2_queries_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """execute a query and return the results.  # noqa: E501

        Execute a query and return the results. * If the request fails, the response content type will be `application/json`. Please refer to the failure codes in Responses section below. * If the query is executed successfully, the response content type will be `text/event-stream`. **For SSE** There are 3 types of data that will be sent to SSE channel 1. Query (type `query`): The first event of the result will ALWAYS be this type. 2. Metrics (type `metrics`): The query metrics in JSON. They will be sent every 1 seconds. 3. Data (the type is empty): The query result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_queries_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateQueryRequestV1Beta2 body: query request parameters (required)
        :return: Query
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_queries_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1beta2_queries_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/event-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/queries', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Query',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_sqlanalyze_post(self, body, **kwargs):  # noqa: E501
        """analyze sql  # noqa: E501

        analyze sql  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sqlanalyze_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnalyzeSQLRequest body: sql request parameters (required)
        :return: SQLAnalyzeResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_sqlanalyze_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_sqlanalyze_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1beta2_sqlanalyze_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """analyze sql  # noqa: E501

        analyze sql  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_sqlanalyze_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnalyzeSQLRequest body: sql request parameters (required)
        :return: SQLAnalyzeResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_sqlanalyze_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1beta2_sqlanalyze_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/sqlanalyze', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SQLAnalyzeResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
