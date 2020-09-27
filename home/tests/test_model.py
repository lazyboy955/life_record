from django.test import TestCase
from home.models import Weight, get_default_period_of_time


class WeightTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_period =  Weight.objects.create(weight=666, username='test', remark='test_period')

    def test_default_period_value(self):
        """Weight that the default period value is correctly identified"""
        self.assertEqual(self.test_period.period_of_time, get_default_period_of_time())
