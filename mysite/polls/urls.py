from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.ListItem.as_view(), name="index"),
    path('invoke_lambda_function', views.InvokeLambdaFunction.as_view(), name="invoke_lambda_function"),
]
