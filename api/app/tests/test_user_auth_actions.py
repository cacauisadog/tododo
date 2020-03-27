import unittest
import os
import json
from config import TestingConfig
from app import create_app, db


class UserAuthActionsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client
