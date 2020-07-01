from rest_framework.viewsets import ModelViewSet
from .serializers import WeightSerializer
from .models import Weight


class WeightViewSet(ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    # todo 1.每次存储完，告知过去一个月，该时段的平均值，并计算出来增减幅度
