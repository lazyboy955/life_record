from django.db.models import Avg
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from home.serializers import WeightSerializer
from home.models import Weight, get_default_period_of_time
from datetime import date, timedelta
from drf_yasg.utils import swagger_auto_schema
import logging

logger = logging.getLogger('home')


# test
class HelloWorld(APIView):
    """测试接口"""

    @staticmethod
    def get(request):
        logger.info('TEST!')
        return Response('test', status=400)


class WeightViewSet(ModelViewSet):
    """
    create:新增体重信息
    list: 展示体重记录
    retrieve: 获取单条体重信息
    update: 更新体重信息
    destroy: 删除体重信息
    """
    queryset = Weight.objects.filter(is_delete=False)
    serializer_class = WeightSerializer
    # filterset_class= WeightFilter
    filterset_fields = ['username', 'period_of_time']
    search_fields = ['username']

    @swagger_auto_schema(responses={
        201: '返回新增的体重信息，十天体重均值，昨天体重'
    })
    def create(self, request, *args, **kwargs):
        obj_data = request.data
        logger.info(f'更新数据如下：{obj_data}')
        # 时段值可能为空，设置默认值
        if not obj_data['period_of_time']:
            obj_data['period_of_time'] = get_default_period_of_time()
        # 同一天早晚时段，只能存在一个体重记录
        period_of_time = obj_data['period_of_time']
        prev_objs = self.queryset.filter(period_of_time=period_of_time,
                                         username=obj_data['username'],
                                         update_time__gte=date.today())
        response = super(WeightViewSet, self).create(request, *args, **kwargs)
        # todo 可能会存在有多个问题，正常情况应该只有一个，需要反馈一下告知用户修改的事,可以加个定时任务清除一下
        if prev_objs:
            # todo 存在一个bug，有时候新创建也会进入到这里
            prev_obj = prev_objs.first()
            prev_obj.is_delete = True
            prev_obj.save()
            logger.info('替换当日同时间记录记录如下：')
            logger.info(WeightSerializer(prev_obj).data)
        resp_data = response.data
        # 平均体重数据（10天)
        start_day = date.today() - timedelta(days=9)
        end_day = date.today() + timedelta(days=1)
        objs = Weight.objects.filter(create_time__range=(start_day, end_day),
                                     period_of_time=period_of_time,
                                     username=obj_data['username'], )
        resp_data['平均值(过去十天）'] = round(objs.aggregate(Avg('weight'))['weight__avg'], 2)
        if len(objs) >= 2:
            resp_data['上一次体重'] = objs[:-2].weight
        response.data = resp_data
        return response
