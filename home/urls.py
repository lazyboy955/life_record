from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = 'home'
router = DefaultRouter()  # 可以处理视图的路由器
router.register('weights', views.WeightViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]
