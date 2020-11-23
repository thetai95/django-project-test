from django.contrib import admin
from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    search_fields = ['name', 'city']


admin.site.register(Department, DepartmentAdmin)
