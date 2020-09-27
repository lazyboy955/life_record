import django_filters
from home.models import Weight


class WeightFilter(django_filters.FilterSet):

    class Mata:
        model = Weight
        fields = ['username']
