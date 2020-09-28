from rest_framework.viewsets import ModelViewSet
from project.models import ProjectRequire
from project.serializers import ProjectRequireSerializer


# Create your views here.

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
