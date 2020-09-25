"""life_record URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# 设置一个默认根路由
router = routers.DefaultRouter()

urlpatterns = [
    # 功能型模块
    path('', include(router.urls)),
    path('admin/', admin.site.urls),  # 管理员登录界面
    path('api-auth/', include('rest_framework.urls')),  # 设置用户登入(这步必须先设置，swagger会调用）
    # 项目内模块
    path('home/', include('home.urls')),
]
