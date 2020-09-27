from django.db import models


class BaseModel(models.Model):
    """基础模型，包含必备字段"""
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)

    class Meta:
        abstract = True
