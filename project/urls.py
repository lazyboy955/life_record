from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = 'project'
router = DefaultRouter()
router.register('require', views.ProjectRequireViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
