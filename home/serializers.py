from home.models import Weight
# from rest_framework import serializers
from life_record.serializers import TimeSerializerModel


class WeightSerializer(TimeSerializerModel):
    class Meta:
        model = Weight
        exclude = ['is_delete']
