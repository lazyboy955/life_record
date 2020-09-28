from project.models import ProjectRequire
from life_record.serializers import TimeSerializerModel


class ProjectRequireSerializer(TimeSerializerModel):
    class Meta:
        model = ProjectRequire
        exclude = ['is_delete']
