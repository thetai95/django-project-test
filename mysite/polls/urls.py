from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.ListItem.as_view(), name="index"),
]
