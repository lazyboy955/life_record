from rest_framework import serializers


# 通用时间处理序列化器
class TimeSerializerModel(serializers.ModelSerializer):
    update_time = serializers.SerializerMethodField()
    create_time = serializers.SerializerMethodField()

    @staticmethod
    def get_update_time(obj):
        return obj.update_time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_create_time(obj):
        return obj.create_time.strftime("%Y-%m-%d %H:%M:%S")
