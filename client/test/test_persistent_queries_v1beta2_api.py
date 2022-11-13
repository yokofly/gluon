# coding: utf-8

"""
    Timeplus

    Welcome to the Timeplus HTTP REST API specification.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: support@timeplus.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import timeplus_client
from timeplus_client.api.persistent_queries_v1beta2_api import (
    PersistentQueriesV1beta2Api,
)  # noqa: E501
from timeplus_client.rest import ApiException


class TestPersistentQueriesV1beta2Api(unittest.TestCase):
    """PersistentQueriesV1beta2Api unit test stubs"""

    def setUp(self):
        self.api = PersistentQueriesV1beta2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1beta2_persistent_queries_get(self):
        """Test case for v1beta2_persistent_queries_get

        list persistent-queries.  # noqa: E501
        """
        pass

    def test_v1beta2_persistent_queries_id_data_get(self):
        """Test case for v1beta2_persistent_queries_id_data_get

        stream persistent query result via websocket  # noqa: E501
        """
        pass

    def test_v1beta2_persistent_queries_id_delete(self):
        """Test case for v1beta2_persistent_queries_id_delete

        delete a persistent query.  # noqa: E501
        """
        pass

    def test_v1beta2_persistent_queries_id_get(self):
        """Test case for v1beta2_persistent_queries_id_get

        get a persistent query.  # noqa: E501
        """
        pass

    def test_v1beta2_persistent_queries_post(self):
        """Test case for v1beta2_persistent_queries_post

        execute a persistent query.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
