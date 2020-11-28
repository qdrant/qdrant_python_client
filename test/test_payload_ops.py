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
from openapi_client.model.payload_ops_any_of import PayloadOpsAnyOf
from openapi_client.model.payload_ops_any_of1 import PayloadOpsAnyOf1
from openapi_client.model.payload_ops_any_of1_delete_payload import PayloadOpsAnyOf1DeletePayload
from openapi_client.model.payload_ops_any_of2 import PayloadOpsAnyOf2
from openapi_client.model.payload_ops_any_of2_clear_payload import PayloadOpsAnyOf2ClearPayload
from openapi_client.model.payload_ops_any_of_set_payload import PayloadOpsAnyOfSetPayload
globals()['PayloadOpsAnyOf'] = PayloadOpsAnyOf
globals()['PayloadOpsAnyOf1'] = PayloadOpsAnyOf1
globals()['PayloadOpsAnyOf1DeletePayload'] = PayloadOpsAnyOf1DeletePayload
globals()['PayloadOpsAnyOf2'] = PayloadOpsAnyOf2
globals()['PayloadOpsAnyOf2ClearPayload'] = PayloadOpsAnyOf2ClearPayload
globals()['PayloadOpsAnyOfSetPayload'] = PayloadOpsAnyOfSetPayload
from openapi_client.model.payload_ops import PayloadOps


class TestPayloadOps(unittest.TestCase):
    """PayloadOps unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPayloadOps(self):
        """Test PayloadOps"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PayloadOps()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
