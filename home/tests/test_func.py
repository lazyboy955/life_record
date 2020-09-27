from django.test import TestCase


# Create your tests here.

class AddTestCase(TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)
