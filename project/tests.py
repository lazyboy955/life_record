from datetime import date, timedelta
from django.test import TestCase, Client
from home.models import User
from project.models import ProjectRequire
from project.tasks import check_deadline

default_email = 'test@qq.com'


# Create your tests here.
class TestRequire(TestCase):
    """测试新需求发送邮件功能"""

    def setUp(self) -> None:
        User.objects.create(username='yyy', email=default_email)
        ProjectRequire.objects.create(operator='yyy', description='test1', limit_date=date.today())
        ProjectRequire.objects.create(operator='yyy', description='test12', limit_date=date.today() + timedelta(days=1))

        self.client = Client()

    def test_send_email(self):
        """测试新需求发送邮件功能"""
        response = self.client.post('/project/require/', data={'operator': 'yyy', 'description': '测试邮件功能', })
        self.assertEqual(response.status_code, 201)

    def test_deadline_check(self):
        """测试逾期任务检查"""
        check_deadline()
