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

import openapi_client
from openapi_client.model.condition_any_of import ConditionAnyOf
from openapi_client.model.condition_any_of1 import ConditionAnyOf1
from openapi_client.model.condition_any_of2 import ConditionAnyOf2
from openapi_client.model.condition_any_of3 import ConditionAnyOf3
from openapi_client.model.condition_any_of4 import ConditionAnyOf4
from openapi_client.model.filter import Filter
from openapi_client.model.geo_bounding_box import GeoBoundingBox
from openapi_client.model.match import Match
from openapi_client.model.range import Range
globals()['ConditionAnyOf'] = ConditionAnyOf
globals()['ConditionAnyOf1'] = ConditionAnyOf1
globals()['ConditionAnyOf2'] = ConditionAnyOf2
globals()['ConditionAnyOf3'] = ConditionAnyOf3
globals()['ConditionAnyOf4'] = ConditionAnyOf4
globals()['Filter'] = Filter
globals()['GeoBoundingBox'] = GeoBoundingBox
globals()['Match'] = Match
globals()['Range'] = Range
from openapi_client.model.condition import Condition


class TestCondition(unittest.TestCase):
    """Condition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCondition(self):
        """Test Condition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Condition()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
