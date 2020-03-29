# coding: utf-8

"""
    Solar.web Query API (SWQAPI)

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fronius_api
from api.historical_api import HistoricalApi  # noqa: E501
from fronius_api.rest import ApiException


class TestHistoricalApi(unittest.TestCase):
    """HistoricalApi unit test stubs"""

    def setUp(self):
        self.api = api.historical_api.HistoricalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_historical_data(self):
        """Test case for historical_data

        This method returns the past time detail values for a specific PV system. The data is returned in granularity of 5 minute intervals.  # noqa: E501
        """
        pass

    def test_historical_data_for_specific_device(self):
        """Test case for historical_data_for_specific_device

        This method returns the past time detail values for a specific device. The data is returned in granularity of 5 minute intervals.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()