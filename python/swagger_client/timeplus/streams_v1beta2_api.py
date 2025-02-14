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


class StreamsV1beta2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1beta2_streams_external_post(self, body, **kwargs):  # noqa: E501
        """create an external stream  # noqa: E501

        Create an external stream.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_external_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExternalStreamDef body: create external stream request parameters (required)
        :return: ExternalStreamDef
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_streams_external_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_streams_external_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1beta2_streams_external_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """create an external stream  # noqa: E501

        Create an external stream.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_external_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExternalStreamDef body: create external stream request parameters (required)
        :return: ExternalStreamDef
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
                    " to method v1beta2_streams_external_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1beta2_streams_external_post`")  # noqa: E501

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
            '/v1beta2/streams/external', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExternalStreamDef',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_streams_get(self, **kwargs):  # noqa: E501
        """list streams  # noqa: E501

        Get all streams.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Stream]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_streams_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_streams_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1beta2_streams_get_with_http_info(self, **kwargs):  # noqa: E501
        """list streams  # noqa: E501

        Get all streams.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Stream]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_streams_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1beta2/streams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Stream]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_streams_name_delete(self, name, **kwargs):  # noqa: E501
        """delete a stream  # noqa: E501

        Delete the stream with the given name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_name_delete(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: stream name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_streams_name_delete_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_streams_name_delete_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def v1beta2_streams_name_delete_with_http_info(self, name, **kwargs):  # noqa: E501
        """delete a stream  # noqa: E501

        Delete the stream with the given name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_name_delete_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: stream name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_streams_name_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `v1beta2_streams_name_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/v1beta2/streams/{name}', 'DELETE',
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

    def v1beta2_streams_name_get(self, name, **kwargs):  # noqa: E501
        """get a stream  # noqa: E501

        Get a stream with the given name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_name_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: stream name (required)
        :return: Stream
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_streams_name_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_streams_name_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def v1beta2_streams_name_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """get a stream  # noqa: E501

        Get a stream with the given name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_name_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: stream name (required)
        :return: Stream
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_streams_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `v1beta2_streams_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/v1beta2/streams/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Stream',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_streams_name_ingest_post(self, body, name, **kwargs):  # noqa: E501
        """ingest data  # noqa: E501

        Ingest data to a stream with the given name. For formats are supported: * compact JSON: when `Content-Type` is set to one of `application/json`, `application/json;format=compact`, `application/vnd.timeplus+json`, `application/vnd.timeplus+json;format=compat`, or set `format` query parameter with value `compact`. And this is the API's default format. * JSON stream: when `Content-Type` is set to one of `application/json;format=streaming`, `application/vnd.timeplus+json;format=streaming`, or set `format` query parameter with value `streaming`. * raw string: when `Content-Type` is set to one of `text/plain`, `text/plain;format=raw`, or set `format` query parameter with value `raw`. * string lines: when `Content-Type` is set to `text/plain;format=lines`, or set `format` query parameter with value `lines`. * refer to https://docs.timeplus.com/docs/ingest-api for more information *   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_name_ingest_post(body, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IngestData body: ingest data (required)
        :param str name: stream name (required)
        :param str format: enfoce payload format, if it is set, it overwrite the Content-Type header
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_streams_name_ingest_post_with_http_info(body, name, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_streams_name_ingest_post_with_http_info(body, name, **kwargs)  # noqa: E501
            return data

    def v1beta2_streams_name_ingest_post_with_http_info(self, body, name, **kwargs):  # noqa: E501
        """ingest data  # noqa: E501

        Ingest data to a stream with the given name. For formats are supported: * compact JSON: when `Content-Type` is set to one of `application/json`, `application/json;format=compact`, `application/vnd.timeplus+json`, `application/vnd.timeplus+json;format=compat`, or set `format` query parameter with value `compact`. And this is the API's default format. * JSON stream: when `Content-Type` is set to one of `application/json;format=streaming`, `application/vnd.timeplus+json;format=streaming`, or set `format` query parameter with value `streaming`. * raw string: when `Content-Type` is set to one of `text/plain`, `text/plain;format=raw`, or set `format` query parameter with value `raw`. * string lines: when `Content-Type` is set to `text/plain;format=lines`, or set `format` query parameter with value `lines`. * refer to https://docs.timeplus.com/docs/ingest-api for more information *   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_name_ingest_post_with_http_info(body, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IngestData body: ingest data (required)
        :param str name: stream name (required)
        :param str format: enfoce payload format, if it is set, it overwrite the Content-Type header
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'name', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_streams_name_ingest_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1beta2_streams_name_ingest_post`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `v1beta2_streams_name_ingest_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501

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
            ['application/json', 'application/vnd.timeplus+json', 'application/json;format=compat', 'application/vnd.timeplus+json;format=compat', 'application/json;format=stream', 'application/vnd.timeplus+json;format=stream', 'application/x-ndjson', 'text/plain', 'text/plain;format=raw', 'text/plain;format=lines'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/streams/{name}/ingest', 'POST',
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

    def v1beta2_streams_name_patch(self, body, name, **kwargs):  # noqa: E501
        """update a stream  # noqa: E501

        Update the specific stream with the given name. Right now it only supports updating data retention-related settings. Altering stream or updating external stream is not supported yet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_name_patch(body, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateStreamRequest body: update stream request parameters (required)
        :param str name: name of the stream (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_streams_name_patch_with_http_info(body, name, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_streams_name_patch_with_http_info(body, name, **kwargs)  # noqa: E501
            return data

    def v1beta2_streams_name_patch_with_http_info(self, body, name, **kwargs):  # noqa: E501
        """update a stream  # noqa: E501

        Update the specific stream with the given name. Right now it only supports updating data retention-related settings. Altering stream or updating external stream is not supported yet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_name_patch_with_http_info(body, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateStreamRequest body: update stream request parameters (required)
        :param str name: name of the stream (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_streams_name_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1beta2_streams_name_patch`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `v1beta2_streams_name_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/v1beta2/streams/{name}', 'PATCH',
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

    def v1beta2_streams_name_stats_get(self, name, **kwargs):  # noqa: E501
        """get the stats of a stream  # noqa: E501

        Get the stats of a stream with the given name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_name_stats_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: stream name (required)
        :return: StreamStats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_streams_name_stats_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_streams_name_stats_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def v1beta2_streams_name_stats_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """get the stats of a stream  # noqa: E501

        Get the stats of a stream with the given name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_name_stats_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: stream name (required)
        :return: StreamStats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_streams_name_stats_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `v1beta2_streams_name_stats_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/v1beta2/streams/{name}/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamStats',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1beta2_streams_post(self, body, **kwargs):  # noqa: E501
        """create a stream  # noqa: E501

        Create a stream. Please refer to the documentation of [stream](https://docs.timeplus.com/working-with-streams) for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StreamDef body: create stream request parameters (required)
        :return: Stream
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_streams_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_streams_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1beta2_streams_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """create a stream  # noqa: E501

        Create a stream. Please refer to the documentation of [stream](https://docs.timeplus.com/working-with-streams) for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_streams_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StreamDef body: create stream request parameters (required)
        :return: Stream
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
                    " to method v1beta2_streams_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1beta2_streams_post`")  # noqa: E501

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
            '/v1beta2/streams', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Stream',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
