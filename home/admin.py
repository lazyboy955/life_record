from django.contrib import admin
from .models import Weight, User


# Register your models here.

class WeightAdmin(admin.ModelAdmin):
    list_display = ['username', 'weight', 'remark']
    list_filter = ['username', 'period_of_time']
    # fields = ['username']


admin.site.register(Weight, WeightAdmin)
admin.site.register(User)
