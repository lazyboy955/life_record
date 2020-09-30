from django.contrib import admin
from .models import ProjectRequire


# Register your models here.

class ProjectRequireAdmin(admin.ModelAdmin):
    list_display = ['operator', 'description', 'limit_date']
    list_filter = ['operator', 'limit_date']
    # fields = ['username']


admin.site.register(ProjectRequire, ProjectRequireAdmin)