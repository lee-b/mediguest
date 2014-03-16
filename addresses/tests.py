"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *

class SimpleTest(TestCase):
    fixtures = [ 'test_addresses.json' ]

    def test_inline_address(self):
        a = Address.objects.get(id=1)
        inline_addr = a.address_inline()
        expected_addr = "Test Address, Test Town, Test Region, BT1 1NN, U.K."
        self.assertEqual(inline_addr, expected_addr)

