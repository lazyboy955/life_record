from django.db import models
from django.contrib.auth.models import AbstractUser
import time


# 时间段字段
class PeriodField:
    DAY = 0
    NIGHT = 1
    PERIOD_CHOICES = [
        (DAY, 'day'),
        (NIGHT, 'night')
    ]


class BaseModel(models.Model):
    """基础模型，包含必备字段"""
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)

    class Meta:
        abstract = True


class User(AbstractUser):
    """用户模型"""
    mobile = models.CharField(verbose_name='手机号', max_length=11, unique=True, )
    weight = models.FloatField(verbose_name='体重', blank=True, null=True)
    height = models.IntegerField(verbose_name='身高', blank=True, null=True)

    class Meta:
        db_table = 'users'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


def get_default_period_of_time():
    return PeriodField.DAY if int(time.strftime('%H')) <= 12 else PeriodField.NIGHT


class Weight(BaseModel):
    """记录用户的体重"""
    username = models.CharField(verbose_name='用户名', max_length=200)
    weight = models.FloatField(verbose_name='体重')
    remark = models.CharField(verbose_name='备注', max_length=300, default='')
    period_of_time = models.PositiveSmallIntegerField(verbose_name='时间段', choices=PeriodField.PERIOD_CHOICES,
                                                      default=get_default_period_of_time)

    class Meta:
        db_table = 'weight'
        verbose_name = '体重表'
        verbose_name_plural = verbose_name
