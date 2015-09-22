from django.contrib import admin
from .models import base

class TaskAdmin(admin.ModelAdmin):
    
    fields = ('user', 'time_due', 'description')
    list_display = ('user', 'time_due', 'description')
    
admin.site.register(base, TaskAdmin)
