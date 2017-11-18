import os
import unittest

from hurriyet.api import Api

api_key = os.environ.get('API_KEY', '')


class HurriyetTestCase(unittest.TestCase):
    api_key = api_key

    def setUp(self):
        self.api = Api(self.api_key)
