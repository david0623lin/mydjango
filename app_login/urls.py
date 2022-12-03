from django.urls import path

from app_login import views

urlpatterns = [
    path('', views.index, name='index'),
]
