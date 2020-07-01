from home.models import Weight
from rest_framework import serializers


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'
