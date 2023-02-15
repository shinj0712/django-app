from django.urls import path, include
from . import views


app_name ='accounts'

urlpatterns = [
    path('login', views.TopView.as_view(), name='login')
]