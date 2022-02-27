from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('index1/', views.index1),
]
