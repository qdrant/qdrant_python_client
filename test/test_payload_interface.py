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
from openapi_client.model.payload_interface_any_of import PayloadInterfaceAnyOf
from openapi_client.model.payload_interface_any_of1 import PayloadInterfaceAnyOf1
from openapi_client.model.payload_interface_any_of2 import PayloadInterfaceAnyOf2
from openapi_client.model.payload_interface_any_of3 import PayloadInterfaceAnyOf3
from openapi_client.model.payload_variant_for_geo_point import PayloadVariantForGeoPoint
globals()['PayloadInterfaceAnyOf'] = PayloadInterfaceAnyOf
globals()['PayloadInterfaceAnyOf1'] = PayloadInterfaceAnyOf1
globals()['PayloadInterfaceAnyOf2'] = PayloadInterfaceAnyOf2
globals()['PayloadInterfaceAnyOf3'] = PayloadInterfaceAnyOf3
globals()['PayloadVariantForGeoPoint'] = PayloadVariantForGeoPoint
from openapi_client.model.payload_interface import PayloadInterface


class TestPayloadInterface(unittest.TestCase):
    """PayloadInterface unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPayloadInterface(self):
        """Test PayloadInterface"""
        # FIXME: construct object with mandatory attributes with example values
        model = PayloadInterface(value=[123], type='integer', _check_type=False)  # noqa: E501
        print("model", model.to_dict())


if __name__ == '__main__':
    unittest.main()
