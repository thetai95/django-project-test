from django.urls import path
from . import views

app_name = "crawl"
urlpatterns = [
    path('', views.ListNews.as_view(), name="index"),
    path('add/', views.AddNews.as_view(), name="add"),
    path('edit/<int:pk>', views.UpdateNews.as_view(), name="update"),
    path('delete/<int:pk>', views.DestroyNews.as_view(), name="delete"),
]
