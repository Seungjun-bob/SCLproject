from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend, name='recommend'),
    path('detail/', views.detail, name='detail')
]
