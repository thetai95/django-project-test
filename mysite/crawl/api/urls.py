from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

urlpatterns = [
    path('news', CRUDNews.as_view(), name='crud-news'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
