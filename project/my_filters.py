import django_filters
from project.models import ProjectRequire


class ProjectRequireFilter(django_filters.FilterSet):

    class Mata:
        model = ProjectRequire
