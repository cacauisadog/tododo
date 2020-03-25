import unittest
import os
import json
from config import DevelopmentConfig
from app import api, db


class UserAuthActionsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = api.config.from_object(DevelopmentConfig)
        self.client = self.app.test_client
