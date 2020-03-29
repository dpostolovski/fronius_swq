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
from api.metadata_api import MetadataApi  # noqa: E501
from fronius_api.rest import ApiException


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = api.metadata_api.MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_device_count(self):
        """Test case for get_device_count

        This method returns number of devices contained within single PV System  # noqa: E501
        """
        pass

    def test_get_device_id_list(self):
        """Test case for get_device_id_list

        This method returns list of all device ids, within single PV System  # noqa: E501
        """
        pass

    def test_get_device_meta_data(self):
        """Test case for get_device_meta_data

        This method returns single device and its details  # noqa: E501
        """
        pass

    def test_get_device_meta_data_list(self):
        """Test case for get_device_meta_data_list

        This method returns list of all devices contained within single PV System  # noqa: E501
        """
        pass

    def test_get_system_count(self):
        """Test case for get_system_count

        This method returns number of PV Systems owned by user  # noqa: E501
        """
        pass

    def test_get_system_id_list(self):
        """Test case for get_system_id_list

        This method returns list of all PV Systems (ids only) owned by user  # noqa: E501
        """
        pass

    def test_get_system_meta_data(self):
        """Test case for get_system_meta_data

        This method returns single PV System and its details  # noqa: E501
        """
        pass

    def test_get_system_meta_data_list(self):
        """Test case for get_system_meta_data_list

        This method returns list of all PV Systems and their details owned by user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
