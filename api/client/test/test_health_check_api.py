# Copyright 2021 The MLX Contributors
# 
# SPDX-License-Identifier: Apache-2.0 
# coding: utf-8

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.30-upload-catalog-from-url
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.health_check_api import HealthCheckApi  # noqa: E501
from swagger_client.rest import ApiException


class TestHealthCheckApi(unittest.TestCase):
    """HealthCheckApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.health_check_api.HealthCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_check(self):
        """Test case for health_check

        Checks if the server is running  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
