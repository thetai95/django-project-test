from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'comment', 'published']
    search_fields = ['title', 'summary']


admin.site.register(News, NewsAdmin)
