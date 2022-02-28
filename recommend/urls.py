from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend),
    path('detail/', views.detail)
]
