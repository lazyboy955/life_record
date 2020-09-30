from datetime import date, timedelta
from django.db import models
from life_record.models import BaseModel


class Priority:
    URGENT = 0
    NORMAL = 1
    PLAN = 2
    PRIORITY_CHOOSE = [(URGENT, '紧急任务'), (NORMAL, '常规任务'), (PLAN, '规划任务')]


# Create your models here.
class ProjectRequire(BaseModel):
    operator = models.CharField(verbose_name='执行者', max_length=200, blank=False, null=False)
    description = models.TextField(verbose_name='需求说明', blank=False, null=False)
    priority = models.PositiveSmallIntegerField(verbose_name='优先级',
                                                choices=Priority.PRIORITY_CHOOSE,
                                                default=Priority.NORMAL)
    is_complete = models.BooleanField(verbose_name='任务是否完成', default=False)
    limit_date = models.DateField(verbose_name='时间限制', default=date.today() + timedelta(days=3))
    remark = models.CharField(verbose_name='需求评论', max_length=300, blank=True, )

    class Meta:
        db_table = 'require'
        verbose_name = '需求表'
        verbose_name_plural = verbose_name

# todo 建立一个模型记录修改数据
