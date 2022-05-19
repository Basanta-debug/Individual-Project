from django.test import TestCase, Client
from django.urls import reverse, resolve
from power.models import *
import json



class TestViews(TestCase):
    def test_test_homepage(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)