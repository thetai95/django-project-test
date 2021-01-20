from django.contrib import admin
from .models import Department, City, DepartmentInfomation


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    search_fields = ['name', 'city']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(DepartmentInfomation)
admin.site.register(City)
