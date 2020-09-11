from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WeightSerializer
from .models import Weight


# test
class HelloWorld(APIView):
    def get(self, request):
        return Response('test', status=400)


class WeightViewSet(ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    # todo 1.每次存储完，告知过去一个月，该时段的平均值，并计算出来增减幅度
