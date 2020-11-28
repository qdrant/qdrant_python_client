# coding: utf-8

"""
    Qdrant API

    API description for Qdrant vector search engine. Describes CRUD and search operations on collections of points (vectors with payload).  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: andrey@vasnetsov.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qdrant_openapi_client
from qdrant_openapi_client.model.error_response_status import ErrorResponseStatus
globals()['ErrorResponseStatus'] = ErrorResponseStatus
from qdrant_openapi_client.model.error_response import ErrorResponse


class TestErrorResponse(unittest.TestCase):
    """ErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testErrorResponse(self):
        """Test ErrorResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ErrorResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
