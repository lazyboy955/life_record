from django.test import Client, TestCase


class WeightViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_details(self):
        response = self.client.get('/home/weights/')
        self.assertEqual(response.status_code, 200)
