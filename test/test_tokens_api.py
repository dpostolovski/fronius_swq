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
from api.tokens_api import TokensApi  # noqa: E501
from fronius_api.rest import ApiException


class TestTokensApi(unittest.TestCase):
    """TokensApi unit test stubs"""

    def setUp(self):
        self.api = api.tokens_api.TokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_jwt(self):
        """Test case for generate_jwt

        """
        pass

    def test_iam_redirect(self):
        """Test case for iam_redirect

        """
        pass

    def test_refresh_jwt(self):
        """Test case for refresh_jwt

        """
        pass


if __name__ == '__main__':
    unittest.main()
