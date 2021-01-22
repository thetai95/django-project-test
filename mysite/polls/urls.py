from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.ListItem.as_view(), name="index"),

    path('invoke_lambda_function', views.InvokeLambdaFunction.as_view(),
         name="invoke_lambda_function"),

    path('test_celery/', views.TestCelery.as_view(), name="test_celery"),

    path('send_email/', views.send_email, name='send_email'),

    path('create_city/', views.create_city, name='create_city'),

    path('test_fetch/', views.test_fetch, name='test_fetch'),

]
