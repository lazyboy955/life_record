from django.contrib import admin
from .models import ProjectRequire


# Register your models here.

class ProjectRequireAdmin(admin.ModelAdmin):
    list_display = ['username', 'description', 'limit_date']
    list_filter = ['username', 'limit_date']
    # fields = ['username']


admin.site.register(ProjectRequire, ProjectRequireAdmin)