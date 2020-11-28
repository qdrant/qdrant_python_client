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
from qdrant_openapi_client.model.search_params_any_of import SearchParamsAnyOf
from qdrant_openapi_client.model.search_params_any_of_hnsw import SearchParamsAnyOfHnsw
globals()['SearchParamsAnyOf'] = SearchParamsAnyOf
globals()['SearchParamsAnyOfHnsw'] = SearchParamsAnyOfHnsw
from qdrant_openapi_client.model.search_params import SearchParams


class TestSearchParams(unittest.TestCase):
    """SearchParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchParams(self):
        """Test SearchParams"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchParams()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
