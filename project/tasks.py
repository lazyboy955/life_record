import logging
import json
from celery import shared_task
from datetime import date
from project.models import ProjectRequire
from project.serializers import ProjectRequireSerializer
from home.models import User
from life_record.utils.email_client import send_message

logger = logging.getLogger("project")


# todo 整理业务逻辑来写一下单元测试，重新设计一下模型
@shared_task
def check_deadline():
    """将逾期的需求逻辑删除并发送邮件给创建者"""
    objs = ProjectRequire.objects.filter(is_delete=False, is_complete=False, limit_date__gte=date.today())
    operators = list(objs.values_list('operator', flat=True).distinct())
    expire_people_list = []
    for operator in operators:
        user = User.objects.get(username=operator)
        expire_tasks = objs.filter(operator=operator, limit_date__gt=date.today())
        last_day_tasks = objs.filter(operator=operator, limit_date=date.today())
        if expire_tasks:
            expire_tasks.update(is_delete=True, remark='任务逾期！！！')
            expire_tasks_data = ProjectRequireSerializer(expire_tasks, many=True).data
            expire_people_list.append(operators)
            send_message('任务逾期', json.dumps(expire_tasks_data, ensure_ascii=False), [user.email], logger)
        if last_day_tasks:
            last_day_data = ProjectRequireSerializer(last_day_tasks, many=True).data
            send_message('还有一天过期任务', json.dumps(last_day_data, ensure_ascii=False), [user.email], logger)

    logger.info(f'以下人员有逾期任务：{expire_people_list}')
    logger.info('扫描逾期任务结束')
