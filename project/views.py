import logging
import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from project.models import ProjectRequire
from project.serializers import ProjectRequireSerializer
from home.models import User
from life_record.utils.email_client import send_message

# Create your views here.
logger = logging.getLogger("project")


class ProjectRequireViewSet(ModelViewSet):
    """
    create:新增需求
    list: 展示需求记录
    retrieve: 获取单条需求信息
    update: 更新需求信息
    destroy: 删除需求信息
    """
    queryset = ProjectRequire.objects.filter(is_delete=False)
    serializer_class = ProjectRequireSerializer

    # filterset_fields = ['username', 'period_of_time']
    # search_fields = ['username']

    # todo 考虑一下外键的事，还有是否需要做一个检查用户是否存在的装饰器
    def create(self, request, *args, **kwargs):
        new_data = request.data
        try:
            operator = User.objects.get(username=new_data['operator'])
        except User.DoesNotExist:
            return Response('该用户不存在，请先创建该用户！', status=status.HTTP_401_UNAUTHORIZED)
        resp = super(ProjectRequireViewSet, self).create(request, *args, **kwargs)
        send_message('新需求', json.dumps(resp.data, ensure_ascii=False), [operator.email], logger)
        return resp
